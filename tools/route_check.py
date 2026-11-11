#!/usr/bin/env python3
"""Route-check driving times from Casa de la Familia using Google's Routes
API (computeRouteMatrix -- the legacy Distance Matrix API's replacement;
Google Cloud Console now surfaces it only under "Routes API"), and write
the results into docs/places/*.md.

Replaces manual screenshot-based checking. Matches the owner's established
convention: Google's default route (toll roads NOT avoided, like the main
figure in Google Maps), live traffic at time of check (not a fixed future
date/time -- per owner decision 2026-11-01, "today" and a pinned future
date/time give effectively the same result).

Usage (from the repo root):
    export GOOGLE_MAPS_API_KEY=...           # needs "Routes API" enabled + billing
    python3 tools/route_check.py                      # dry run: every place missing a duration
    python3 tools/route_check.py --slugs malaga tarifa # dry run: just these
    python3 tools/route_check.py --apply               # write the results into docs/places/*.md

Dry run only prints a table -- nothing is written until --apply. Never
overwrites a place that already has a duration unless --force is given
(so it won't clobber a manually fact-checked entry by accident).

What it does NOT give you (unlike a manual Google Maps screenshot):
route description ("via AP-7"), tested-day/time chosen by hand, alternate
parking-point comparisons. Add those by hand in `note:` afterwards if you
want that level of detail for a particular place; the API still gives a
solid, timestamped, link-backed duration for everything else.
"""
import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# Casa de la Familia: Plus Code 8C8QG8PP+7W, the project constant in AGENTS.md and
# tools/places.py (CASA_LAT, CASA_LON). Pass --origin to override.
DEFAULT_ORIGIN_LATLNG = "36.5356875,-4.6626875"
DEFAULT_ORIGIN_LABEL = "Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain"

ROUTE_MATRIX_URL = "https://routes.googleapis.com/distanceMatrix/v2:computeRouteMatrix"
FIELD_MASK = "originIndex,destinationIndex,duration,distanceMeters,condition,status"
MAX_DESTINATIONS_PER_CALL = 20  # Google's cap is 25 elements per origin; stay safely under it.

FRONTMATTER_END = "\n---"


def format_duration(seconds: int) -> str:
    hours, mins = divmod(round(seconds / 60), 60)
    if hours and mins:
        return f"{hours} hour{'s' if hours != 1 else ''} {mins} min"
    if hours:
        return f"{hours} hour{'s' if hours != 1 else ''}"
    return f"{mins} min"


def format_distance(meters: int) -> str:
    return f"{meters / 1000:.1f} km"


def waypoint(query: str) -> dict:
    """query is either "lat,lng" (has coordinates) or a free-text address."""
    parts = query.split(",")
    if len(parts) >= 2:
        try:
            lat, lng = float(parts[0]), float(parts[1])
            return {"waypoint": {"location": {"latLng": {"latitude": lat, "longitude": lng}}}}
        except ValueError:
            pass
    return {"waypoint": {"address": query}}


def load_frontmatter(path: Path) -> dict:
    import yaml  # local import: only needed for reading, not for writing (see replace_block)

    text = path.read_text(encoding="utf-8")
    end = text.index(FRONTMATTER_END, 4)
    return yaml.safe_load(text[4:end])


def find_destination_query(front: dict) -> str:
    """Prefer coordinates when the record already has them; else a text address."""
    coords = front.get("coordinates") or {}
    lat, lng = coords.get("latitude"), coords.get("longitude")
    if lat is not None and lng is not None:
        return f"{lat},{lng}"
    name = front.get("name")
    muni = front.get("municipality")
    parts = [name, muni if muni != name else None, front.get("country") or "Spain"]
    return ", ".join(p for p in parts if p and p != "Unknown")


def destination_label(front: dict) -> str:
    coords = front.get("coordinates") or {}
    lat, lng = coords.get("latitude"), coords.get("longitude")
    name = front.get("name") or front.get("slug")
    if lat is not None and lng is not None:
        return f"{name} ({lat}, {lng})"
    muni = front.get("municipality")
    return f"{name}, {muni}" if muni and muni not in (None, "Unknown", name) else name


def call_route_matrix(api_key: str, origin: str, destinations: list[str]) -> list[dict]:
    """One origin, many destinations, one call. departureTime is left out on
    purpose: with routingPreference TRAFFIC_AWARE that means "now", which is
    the live-traffic reading the owner wants (no fixed future date/time)."""
    # No routeModifiers: toll roads are allowed, as in Google Maps' main figure
    # (owner decision 2026-10-29) and in the existing records.
    origin_obj = waypoint(origin)
    body = {
        "origins": [origin_obj],
        "destinations": [waypoint(d) for d in destinations],
        "travelMode": "DRIVE",
        "routingPreference": "TRAFFIC_AWARE",
        "units": "METRIC",
    }
    req = urllib.request.Request(
        ROUTE_MATRIX_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "X-Goog-Api-Key": api_key,
            "X-Goog-FieldMask": FIELD_MASK,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            elements = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        sys.exit(f"Routes API error (HTTP {e.code}): {detail}")
    # Sort back into destination order -- the API does not guarantee response order.
    elements.sort(key=lambda el: el.get("destinationIndex", 0))
    return elements


def directions_url(origin: str, destination: str) -> str:
    params = {
        "api": "1",
        "origin": origin,
        "destination": destination,
        "travelmode": "driving",
    }
    return f"https://www.google.com/maps/dir/?{urllib.parse.urlencode(params)}"


def replace_block(text: str, duration: str, source: str, checked_at: str, note: str) -> str:
    """Line-based, in-place patch of the driving_time_from_casa_de_la_familia
    block -- never a full YAML parse+dump, which would reformat the whole
    file (quote style, key order) and blow up the diff. Mirrors how
    tools/migrate_young_adults.py already patches these files."""
    lines = text.split("\n")
    start = next(i for i, l in enumerate(lines) if l.rstrip() == "driving_time_from_casa_de_la_familia:")
    end = start + 1
    while end < len(lines) and (lines[end].startswith("  ") or lines[end].strip() == ""):
        end += 1
    block = lines[start:end]

    def set_field(block, key, value):
        pattern = re.compile(rf"^  {key}:.*$")
        for i, l in enumerate(block):
            if pattern.match(l):
                block[i] = f"  {key}: {value}"
                return block
        # Field not present (e.g. no note yet): insert right after checked_at, else at block end.
        insert_at = len(block)
        for i, l in enumerate(block):
            if l.startswith("  checked_at:"):
                insert_at = i + 1
                break
        block.insert(insert_at, f"  {key}: {value}")
        return block

    dump = lambda s: json.dumps(s, ensure_ascii=False)
    block = set_field(block, "duration", dump(duration))
    block = set_field(block, "source", dump(source))
    block = set_field(block, "checked_at", checked_at)
    block = set_field(block, "note", dump(note))
    # Drop the placeholder "note not checked" line if it's still the old generic one.
    block = [
        l for l in block
        if "Route not checked; do not estimate from memory." not in l or l.strip().startswith("note: " + json.dumps(note)[:1])
    ]
    return "\n".join(lines[:start] + block + lines[end:])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--api-key", default=None, help="Defaults to $GOOGLE_MAPS_API_KEY")
    ap.add_argument("--origin", default=DEFAULT_ORIGIN_LATLNG)
    ap.add_argument("--slugs", nargs="*", default=None, help="Only these slugs; default: every place missing a duration")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--force", action="store_true", help="Overwrite a place that already has a duration")
    args = ap.parse_args()

    import os
    api_key = args.api_key or os.environ.get("GOOGLE_MAPS_API_KEY")
    if not api_key:
        sys.exit("No API key. Pass --api-key or set GOOGLE_MAPS_API_KEY.")

    root = Path(args.repo).resolve()
    places_dir = root / "docs" / "places"
    if not places_dir.is_dir():
        sys.exit(f"Not a CalleMilano data repo ({places_dir} missing). Run from the repo root.")

    candidates = []
    for path in sorted(places_dir.glob("*.md")):
        front = load_frontmatter(path)
        slug = front.get("slug") or path.stem
        if args.slugs and slug not in args.slugs:
            continue
        dt = front.get("driving_time_from_casa_de_la_familia") or {}
        if dt.get("duration") is not None and not args.force:
            continue
        candidates.append((path, front))

    if not candidates:
        print("Nothing to check (use --force to re-check places that already have a duration).")
        return

    checked_at = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    now_local = datetime.now().strftime("%A %Y-%m-%d, about %H:%M")

    rows = []
    for i in range(0, len(candidates), MAX_DESTINATIONS_PER_CALL):
        chunk = candidates[i:i + MAX_DESTINATIONS_PER_CALL]
        dest_queries = [find_destination_query(front) for _, front in chunk]
        elements = call_route_matrix(api_key, args.origin, dest_queries)
        for (path, front), element, dest_query in zip(chunk, elements, dest_queries):
            slug = front.get("slug") or path.stem
            condition = element.get("condition", "UNKNOWN")
            if condition != "ROUTE_EXISTS":
                rows.append((slug, None, None, condition))
                continue
            dur_text = format_duration(int(element["duration"].rstrip("s")))
            dist_text = format_distance(element["distanceMeters"])
            rows.append((slug, dur_text, dist_text, "OK"))
            if args.apply:
                dest_label = destination_label(front)
                url = directions_url(args.origin, dest_query)
                source = (
                    f"Google Routes API (computeRouteMatrix), checked by script on {checked_at} "
                    f"from {DEFAULT_ORIGIN_LABEL} ({args.origin}); toll roads not avoided - {url}"
                )
                note = f"Live traffic {now_local}. {dist_text}. Measured programmatically (Routes API)."
                text = path.read_text(encoding="utf-8")
                text = replace_block(text, dur_text, source, checked_at, note)
                # Fill the destination line too, so it stops saying "Unknown; named visitor point not established".
                # Repl is a function, not an f-string: a literal backslash in dest_label (accented
                # characters would otherwise need \uXXXX escaping) must never be read as a regex
                # backreference by re.sub.
                dest_line = f"  destination: {json.dumps(dest_label, ensure_ascii=False)}"
                text = re.sub(
                    r"^  destination:.*$",
                    lambda m, line=dest_line: line,
                    text,
                    count=1,
                    flags=re.MULTILINE,
                )
                path.write_text(text, encoding="utf-8")

    width = max(len(r[0]) for r in rows)
    print(f"{'slug':<{width}}  {'duration':<12} {'distance':<10} status")
    for slug, dur, dist, status in rows:
        print(f"{slug:<{width}}  {dur or '-':<12} {dist or '-':<10} {status}")

    if not args.apply:
        print(f"\n{len(rows)} place(s) checked -- DRY RUN, nothing written. Re-run with --apply to write.")
    else:
        print(f"\n{len(rows)} place(s) updated in docs/places/*.md.")


if __name__ == "__main__":
    main()
