"""Spisesteder til turforslag (Charlie): stedposter først, derefter data/restaurant-directory.csv.

Del af tools/trip.py; kør kommandoerne gennem den.
"""
from __future__ import annotations

import csv
import datetime as dt
import re
import sys

from common import PLACES as PLACES_DIR, ROOT, haversine_km, load_front_matter
from trip_core import load_places, now_iso, out, pick_places


RESTAURANTS = ROOT / "data" / "restaurant-directory.csv"

AREAS = ROOT / "data" / "restaurant-areas.csv"

RESTAURANT_STALE_DAYS = 183  # restaurantrækker ældre end ca. 6 måneder markeres

WALK_KM = 0.8          # ca. 10 minutters gang (ejerbeslutning 2026-11-01)

FALLBACK_KM = 3.0      # luftlinje; bruges kun når der er for få restauranter i gåafstand

PICK = {"dyr": 3, "mellem": 3, "billig": 4}

PRICE_BANDS = {"billig", "mellem", "dyr"}

KIDS = {"ja", "nej", "ukendt"}

KIDS_BASIS = {"egen kilde", "anmeldelser", "-"}

DRESS = {"ingen", "pæn afslappet", "formel", "ukendt"}

# konverteret: er blevet stedpost (slug i notes); fravalgt: ejeren har fravalgt den (ejerbeslutning 2026-11-02).
R_STATUS = {"aktiv", "skal tjekkes", "lukket", "konverteret", "fravalgt"}

R_COLUMNS = [
    "restaurant_id", "area_id", "name", "address", "municipality", "latitude", "longitude", "phone", "website",
    "cuisine", "price_band", "price_basis", "kids_welcome", "kids_basis", "dress_code",
    "hours_note", "sources", "checked_at", "checked_by", "status", "notes",
]

COST_TO_BAND = {"€": "billig", "€€": "mellem", "€€€": "dyr", "€€€€": "dyr"}

RECORD_STATUSES = {"needs_fact_check", "needs_editorial_review", "approved", "published"}


def restaurants_from_records():
    """Restaurant place records (docs/places, category Restaurants) in directory-row format.

    Owner decision 2026-11-02: restaurants are full place records; the directory CSV is a light
    lead list that is converted into records over time. Bars are skipped (owner bar rule:
    taxi or Uber, drink-safety note), as are records without a checked status.
    """
    rows = []
    for f in sorted(PLACES_DIR.glob("*.md")):
        try:
            d = load_front_matter(f)
        except Exception:
            continue
        if d.get("category") != "Restaurants" or d.get("status") not in RECORD_STATUSES:
            continue
        c = d.get("coordinates") or {}
        if c.get("latitude") is None:
            continue
        text = (d.get("description_long") or "").lower()
        if "keep an eye on your drink" in text or "take a taxi or uber" in text:
            continue  # bar records carry the drink-safety note; not for family meal suggestions
        vi = d.get("visit_information") or {}
        rows.append({
            "restaurant_id": d["slug"], "area_id": "", "name": d["name"],
            "address": (c.get("label") or "").replace(" (Google Places listing)", ""),
            "municipality": d.get("municipality", ""), "latitude": str(c["latitude"]),
            "longitude": str(c["longitude"]), "phone": "", "website": (d.get("links") or {}).get("official_website") or "",
            "cuisine": d.get("description_short", ""), "price_band": COST_TO_BAND.get(d.get("cost_level"), "ukendt"),
            "price_basis": f"cost_level {d.get('cost_level')} i stedposten", "kids_welcome": "ukendt", "kids_basis": "-",
            "dress_code": "ukendt", "hours_note": vi.get("schedule") or "ukendt",
            "sources": " ".join(sorted({e.get("source_url", "") for e in d.get("evidence", []) if e.get("source_url")})),
            "checked_at": str(d.get("updated_at") or ""), "checked_by": "stedpost", "status": "aktiv",
            "notes": f"Stedpost {d['slug']} (status {d['status']})",
        })
    return rows


def load_restaurants():
    """Directory rows plus restaurant place records; a record wins over a directory row for the same place."""
    recs = restaurants_from_records()
    rows = list(csv.DictReader(RESTAURANTS.open(encoding="utf-8"))) if RESTAURANTS.exists() else []
    keep = []
    for r in rows:
        try:
            lat, lon = float(r["latitude"]), float(r["longitude"])
        except ValueError:
            keep.append(r); continue
        dup = any(x["name"].lower() == r["name"].lower() or
                  haversine_km(lat, lon, float(x["latitude"]), float(x["longitude"])) < 0.04 for x in recs)
        if not dup:
            keep.append(r)
    return keep + recs


def load_areas():
    if not AREAS.exists():
        return {}
    return {r["area_id"]: {**r, "slugs": [x for x in r["place_slugs"].split(";") if x]}
            for r in csv.DictReader(AREAS.open(encoding="utf-8"))}


def lookup_restaurants(p, kids=False, rows=None, today=None):
    """Vælg 3 dyre, 3 mellem og 4 billige nær stedet. Med børn udelades 'nej' og 'ja' prioriteres."""
    today = today or dt.date.today()
    if rows is None:
        rows = [r for r in load_restaurants() if r.get("status") == "aktiv"]
    scored = []
    for r in rows:
        try:
            d = haversine_km(p["lat"], p["lon"], float(r["latitude"]), float(r["longitude"]))
        except ValueError:
            continue
        if kids and r.get("kids_welcome") == "nej":
            continue
        scored.append((d, r))
    scored.sort(key=lambda x: x[0])
    picked, gaps = {}, []
    for band, n in PICK.items():
        pool = [(d, r) for d, r in scored if r["price_band"] == band]
        near = [(d, r) for d, r in pool if d <= WALK_KM]
        far = [(d, r) for d, r in pool if WALK_KM < d <= FALLBACK_KM]
        if kids:
            near.sort(key=lambda x: (x[1]["kids_welcome"] != "ja", x[0]))
            far.sort(key=lambda x: (x[1]["kids_welcome"] != "ja", x[0]))
        sel = near[:n] + far[: max(0, n - len(near))]
        if len(sel) < n:
            gaps.append(f"{band}: {len(sel)} af {n}")
        items = []
        for d, r in sel:
            try:
                age = (today - dt.date.fromisoformat(r["checked_at"])).days
            except ValueError:
                age = None
            items.append({**{k: r[k] for k in R_COLUMNS if k not in ("latitude", "longitude")},
                          "straight_line_m": int(round(d * 1000)),
                          "reach": "gåafstand" if d <= WALK_KM else "kort kørsel (uden for gåafstand)",
                          "stale": age is None or age > RESTAURANT_STALE_DAYS})
        picked[band] = items
    return {"restaurants": picked, "gaps": gaps, "needs_collection": bool(gaps)}


def cmd_restaurants(args):
    _, chosen = pick_places(args.slugs)
    res = {"generated_at": now_iso(), "directory": str(RESTAURANTS.relative_to(ROOT)),
           "walk_radius_km_straight_line": WALK_KM, "places": []}
    for p in chosen:
        res["places"].append({"slug": p["slug"], "name": p["name"], **lookup_restaurants(p, args.kids)})
    out(res)


def cmd_coverage(_args):
    places = load_places()
    rows = [r for r in load_restaurants() if r.get("status") == "aktiv"]
    report = []
    for aid, a in sorted(load_areas().items(), key=lambda kv: int(kv[1]["priority"] or 99)):
        per_place = []
        for slug in a["slugs"]:
            p = places.get(slug)
            if not p:
                per_place.append({"slug": slug, "error": "ukendt slug"})
                continue
            cnt = {b: 0 for b in PICK}
            for r in rows:
                try:
                    d = haversine_km(p["lat"], p["lon"], float(r["latitude"]), float(r["longitude"]))
                except ValueError:
                    continue
                if d <= WALK_KM and r["price_band"] in cnt:
                    cnt[r["price_band"]] += 1
            per_place.append({"slug": slug, **cnt, "complete": all(cnt[b] >= n for b, n in PICK.items())})
        report.append({"area_id": aid, "name": a["name"], "priority": a["priority"],
                       "rows_in_area": sum(1 for r in rows if r.get("area_id") == aid),
                       "complete": all(x.get("complete") for x in per_place), "places": per_place})
    covered = {s for a in load_areas().values() for s in a["slugs"]}
    missing = sorted(p["slug"] for p in places.values() if p["layer"] == "local_30km" and p["slug"] not in covered)
    out({"areas": report, "local_places_without_area": missing})


def cmd_check_restaurants(_args):
    errors = []
    if not RESTAURANTS.exists():
        out({"ok": False, "errors": ["filen mangler"]})
        sys.exit(1)
    with RESTAURANTS.open(encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != R_COLUMNS:
            errors.append(f"kolonner skal være: {','.join(R_COLUMNS)}")
        rows = list(reader)
    ids = set()
    areas = load_areas()
    for i, r in enumerate(rows, start=2):
        tag = f"linje {i} ({r.get('name') or '?'})"
        if r.get("area_id") not in areas:
            errors.append(f"{tag}: area_id={r.get('area_id')!r} findes ikke i data/restaurant-areas.csv")
        rid = r.get("restaurant_id", "")
        if not re.fullmatch(r"R-\d{4}", rid):
            errors.append(f"{tag}: restaurant_id skal være R-0001-format")
        if rid in ids:
            errors.append(f"{tag}: dublet-id {rid}")
        ids.add(rid)
        for f in ("name", "address", "municipality", "sources", "checked_at", "checked_by"):
            if not r.get(f, "").strip():
                errors.append(f"{tag}: {f} mangler")
        try:
            lat, lon = float(r["latitude"]), float(r["longitude"])
            if not (35 < lat < 44 and -10 < lon < 5):
                errors.append(f"{tag}: koordinater uden for Spanien")
        except (ValueError, KeyError):
            errors.append(f"{tag}: ugyldige koordinater")
        checks = [("price_band", PRICE_BANDS), ("kids_welcome", KIDS), ("kids_basis", KIDS_BASIS),
                  ("dress_code", DRESS), ("status", R_STATUS)]
        for f, allowed in checks:
            if r.get(f) not in allowed:
                errors.append(f"{tag}: {f}={r.get(f)!r} er ikke en af {sorted(allowed)}")
        if r.get("kids_welcome") in ("ja", "nej") and r.get("kids_basis") == "-":
            errors.append(f"{tag}: kids_welcome={r['kids_welcome']} kræver kids_basis")
        if not r.get("phone") and not r.get("website"):
            errors.append(f"{tag}: mindst telefon eller hjemmeside er påkrævet")
        if r.get("price_band") and not r.get("price_basis"):
            errors.append(f"{tag}: price_basis mangler (hvordan prisklassen er fundet)")
        for u in [s for s in r.get("sources", "").split(" ") if s] + ([r["website"]] if r.get("website") else []):
            if not u.startswith("https://") and not u.startswith("http://"):
                errors.append(f"{tag}: ugyldig URL {u!r}")
        try:
            dt.date.fromisoformat(r.get("checked_at", ""))
        except ValueError:
            errors.append(f"{tag}: checked_at skal være ÅÅÅÅ-MM-DD")
    out({"ok": not errors, "rows": len(rows), "errors": errors})
    sys.exit(0 if not errors else 1)
