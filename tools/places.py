#!/usr/bin/env python3
"""CalleMilano place-record tooling.

Usage:
  python3 tools/places.py validate   # check every record in docs/places/ against docs/place-schema.md
  python3 tools/places.py catalog    # regenerate data/place-catalog.csv (read-only index)

Requires PyYAML (pip install pyyaml). Exit code 1 if validation finds errors.

The validator implements the structural checks in the AGENTS.md validation gate
(YAML, schema version, required fields, enums, ID/slug/registry, lifecycle gate).
It does NOT check whether facts are true, whether evidence is adequate, or SEO
uniqueness beyond exact duplicates; those remain human review steps.
"""
from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PLACES = ROOT / "docs" / "places"
REGISTRY = ROOT / "data" / "place-id-registry.csv"
CATALOG = ROOT / "data" / "place-catalog.csv"

SCHEMA_VERSION = "1.0.0"

# Casa de la Familia, Urb. Cerros del Águila, 29649 Las Lagunas de Mijas.
# Plus Code 8C8QG8PP+7W (centre of the ~14 m code area), supplied by the owner 2026-10-05.
CASA_LAT, CASA_LON = 36.5356875, -4.6626875
PRIMARY_RADIUS_KM = 30.0

REQUIRED = [
    "schema_version", "status", "id", "slug", "name", "category", "tags", "coordinates",
    "google_maps_url", "external_ids", "municipality", "province", "autonomous_community",
    "country", "driving_time_from_casa_de_la_familia", "age_groups", "family_score",
    "energy_level", "seasonality", "accessibility", "wheelchair_friendly", "parking",
    "transport_options", "booking_required", "dog_friendly", "toilets_available",
    "food_available", "cost_level", "visit_information", "links", "related_places",
    "description_short", "description_long", "seo_title", "seo_description", "images",
    "evidence", "review_issues", "created_at", "updated_at", "last_verified",
    "last_reviewed_at", "next_review_at", "review_decision", "redirects",
]

STATUSES = {"draft", "needs_fact_check", "needs_editorial_review", "approved", "published", "archived"}
DRAFT_STATUSES = {"draft", "needs_fact_check", "needs_editorial_review"}
CATEGORIES = {"Restaurants", "Beaches", "Excursions", "Nature", "City", "Family activities"}
TAGS = {"Beach", "Restaurant", "Nature", "Hiking", "Viewpoint", "Historic town", "Museum",
        "Adventure", "Rainy day", "Half day", "Full day", "Free", "Premium"}
AGE_GROUPS = {"Small children (0-6)", "Children (7-12)", "Teenagers (13-17)", "Adults", "Seniors"}
FAMILY_KEYS = {"small_children", "children", "teenagers", "adults", "seniors"}
FAMILY_VALUES = {"low", "medium", "high", "unknown"}
ENERGY = {"Low", "Medium", "High"}
SEASONS = {"Spring", "Summer", "Autumn", "Winter", "All year"}
YES_NO_PARTIAL = {"yes", "no", "partial", "unknown"}
YES_NO = {"yes", "no", "unknown"}
COST = {"Free", "€", "€€", "€€€", "€€€€", "Unknown"}
COORD_PURPOSE = {"venue", "entrance", "town_center", "representative_point"}


def haversine_km(lat1, lon1, lat2, lon2):
    r = 6371.0088
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def load_front_matter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("file does not start with YAML front matter (---)")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("front matter is not closed with ---")
    data = yaml.safe_load(parts[1])
    if not isinstance(data, dict):
        raise ValueError("front matter is not a mapping")
    return data


def load_registry():
    with REGISTRY.open(encoding="utf-8") as fh:
        return {row["id"]: row for row in csv.DictReader(fh)}


def coords_of(rec):
    c = rec.get("coordinates")
    if isinstance(c, dict):
        lat, lon = c.get("latitude"), c.get("longitude")
        if isinstance(lat, (int, float)) and isinstance(lon, (int, float)):
            return float(lat), float(lon)
    return None


def validate():
    registry = load_registry()
    errors, warnings = [], []
    seen_ids, seen_slugs, seen_seo = {}, {}, {}
    records = sorted(PLACES.glob("*.md"))

    for path in records:
        name = path.name
        err = lambda m: errors.append(f"{name}: {m}")
        warn = lambda m: warnings.append(f"{name}: {m}")
        try:
            rec = load_front_matter(path)
        except Exception as exc:  # noqa: BLE001
            err(f"YAML: {exc}")
            continue

        for field in REQUIRED:
            if field not in rec:
                err(f"missing required field `{field}`")

        status = rec.get("status")
        is_draft = status in DRAFT_STATUSES
        if status not in STATUSES:
            err(f"invalid status {status!r}")
        if rec.get("schema_version") != SCHEMA_VERSION:
            err(f"schema_version {rec.get('schema_version')!r} != {SCHEMA_VERSION}")

        slug = rec.get("slug")
        if slug != path.stem:
            err(f"slug {slug!r} does not match file name")
        if slug in seen_slugs:
            err(f"duplicate slug {slug!r} (also {seen_slugs[slug]})")
        seen_slugs[slug] = name

        rid = rec.get("id")
        if rid is None:
            if is_draft:
                warn("id is null (identity unresolved; allocate in registry before fact check)"
                     if status == "draft" else "id is null outside `draft` status")
                if status != "draft":
                    err("id must be allocated before leaving `draft`")
            else:
                err("id is null")
        else:
            if rid in seen_ids:
                err(f"duplicate id {rid} (also {seen_ids[rid]})")
            seen_ids[rid] = name
            reg = registry.get(rid)
            if not reg:
                err(f"id {rid} not in data/place-id-registry.csv")
            elif reg.get("slug") != slug:
                err(f"registry slug {reg.get('slug')!r} != record slug {slug!r}")

        if rec.get("category") not in CATEGORIES:
            err(f"invalid category {rec.get('category')!r}")
        for t in rec.get("tags") or []:
            if t not in TAGS:
                err(f"invalid tag {t!r}")
        for g in rec.get("age_groups") or []:
            if g not in AGE_GROUPS:
                err(f"invalid age group {g!r}")
        fs = rec.get("family_score")
        if isinstance(fs, dict):
            if set(fs) != FAMILY_KEYS:
                err(f"family_score keys {sorted(fs)} != {sorted(FAMILY_KEYS)}")
            for k, v in fs.items():
                if v not in FAMILY_VALUES:
                    err(f"family_score.{k} invalid value {v!r}")
        elif "family_score" in rec:
            err("family_score is not an object")
        if rec.get("energy_level") not in ENERGY:
            err(f"invalid energy_level {rec.get('energy_level')!r}")
        for s in rec.get("seasonality") or []:
            if s not in SEASONS:
                err(f"invalid season {s!r}")
        for field, allowed in (("wheelchair_friendly", YES_NO_PARTIAL), ("dog_friendly", YES_NO_PARTIAL),
                               ("toilets_available", YES_NO), ("food_available", YES_NO),
                               ("cost_level", COST)):
            if field in rec and rec[field] not in allowed:
                err(f"invalid {field} {rec[field]!r}")
        if rec.get("booking_required") not in (True, False, "unknown"):
            err(f"invalid booking_required {rec.get('booking_required')!r}")

        c = rec.get("coordinates")
        if isinstance(c, dict):
            if c.get("purpose") not in COORD_PURPOSE:
                err(f"invalid coordinates.purpose {c.get('purpose')!r}")
            if coords_of(rec) is None:
                (warn if is_draft else err)("coordinates missing (needed for radius filter)")
        else:
            err("coordinates is not an object")

        dt = rec.get("driving_time_from_casa_de_la_familia")
        if isinstance(dt, dict) and dt.get("duration") is None:
            (warn if is_draft else err)("driving time not route-checked (duration null)")

        seo = rec.get("seo_title")
        if seo:
            if seo in seen_seo:
                err(f"duplicate seo_title (also {seen_seo[seo]})")
            seen_seo[seo] = name

        if status in {"approved", "published"}:
            if not rec.get("review_decision"):
                err("approved/published without review_decision")
            if rec.get("review_issues"):
                err("approved/published with open review_issues")
            if not rec.get("evidence"):
                err("approved/published without evidence")

    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"\n{len(records)} records, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


def catalog():
    rows = []
    for path in sorted(PLACES.glob("*.md")):
        rec = load_front_matter(path)
        xy = coords_of(rec)
        dist = round(haversine_km(CASA_LAT, CASA_LON, *xy), 1) if xy else ""
        dt = rec.get("driving_time_from_casa_de_la_familia") or {}
        rows.append({
            "id": rec.get("id") or "",
            "slug": rec.get("slug"),
            "name": rec.get("name"),
            "status": rec.get("status"),
            "category": rec.get("category"),
            "tags": "; ".join(rec.get("tags") or []),
            "municipality": rec.get("municipality") or "",
            "province": rec.get("province") or "",
            "latitude": xy[0] if xy else "",
            "longitude": xy[1] if xy else "",
            "distance_km_from_casa": dist,
            "within_primary_radius": "" if dist == "" else ("yes" if dist <= PRIMARY_RADIUS_KM else "no"),
            "driving_time": dt.get("duration") or "",
            "record_file": f"docs/places/{path.name}",
        })
    rows.sort(key=lambda r: (r["distance_km_from_casa"] == "", r["distance_km_from_casa"] or 0, r["slug"]))
    with CATALOG.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {CATALOG.relative_to(ROOT)} ({len(rows)} records)")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "validate":
        sys.exit(validate())
    if cmd == "catalog":
        sys.exit(catalog())
    print(__doc__)
    sys.exit(2)
