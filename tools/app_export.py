#!/usr/bin/env python3
"""Export place records for the callemilano.dk app (Lovable project "Vores Spanske Hjem").

Usage:  python3 tools/app_export.py            # writes data/app-export/
        python3 tools/app_export.py --check    # prints counts only

Owner decisions 2026-11-02 (docs/webapp-byggeplan.md):
  * the app shows records with status needs_fact_check or later; drafts and archived records are left out;
  * non-approved records are labelled in the app ("Ikke endeligt godkendt");
  * only the current phase is exported: the primary area (route-checked drive <= 30 min) and records listed
    in data/layer-membership.csv. Other out-of-area records are archive (AGENTS.md) and are not exported.

The output is derived data, like data/place-catalog.csv: never edit it by hand; re-run this script after
record changes. The structured `guide` object follows the app's schema in src/lib/guide.ts. Texts are the
records' English texts; Danish texts already written in the app are kept by the app's import.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PLACES = ROOT / "docs" / "places"
OUT = ROOT / "data" / "app-export"
SHOWN = {"needs_fact_check", "needs_editorial_review", "approved", "published"}
LOCAL_MAX_MIN = 30

CATEGORY = {"Restaurants": "restaurant", "Beaches": "strand", "Excursions": "udflugt", "Nature": "natur",
            "City": "by", "Family activities": "sevaerdighed"}
LAYER = {"excursions_4h": "udflugt_4t", "excursions_5h": "udflugt_5t"}
AGE = {"Small children (0-6)": "smaa_boern", "Children (7-12)": "boern", "Young adults": "unge_voksne",
       "Seniors": "seniorer"}
FIT_KEY = {"small_children": "smaa_boern", "children": "boern", "young_adults": "unge_voksne", "seniors": "seniorer"}
FIT = {"high": "hoej", "medium": "middel", "low": "lav"}
ENERGY = {"Low": "lav", "Medium": "middel", "High": "hoej"}
SEASON = {"Spring": ["foraar"], "Summer": ["sommer"], "Autumn": ["efteraar"], "Winter": ["vinter"],
          "All year": ["foraar", "sommer", "efteraar", "vinter"]}
THEME = {"Beach": "strand", "Hiking": "vandring", "Historic town": "historisk-by", "Museum": "museum",
         "Viewpoint": "udsigt", "Nature": "natur", "Adventure": "eventyr", "Restaurant": "spisested"}
DURATION = {"Overnight": "overnatning", "Full day": "hel_dag", "Half day": "halv_dag"}
COST = {"Free": "gratis", "€": "lav", "€€": "middel", "€€€": "hoej", "€€€€": "hoej"}
STATUS = {"needs_fact_check": "needs_fact_check", "needs_editorial_review": "needs_editorial_review",
          "approved": "approved", "published": "published"}


def front_matter(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8").split("---\n", 2)[1])


def minutes(text) -> int | None:
    """'22 min', '75 min', '1 h 15 min', '9 hours 21 min' -> minutes; None when unparsable."""
    if not text:
        return None
    s = str(text).lower()
    h = re.search(r"(\d+)\s*(h|hour|hours|t)\b", s)
    m = re.search(r"(\d+)\s*(min|m)\b", s)
    if not h and not m:
        return None
    return (int(h.group(1)) * 60 if h else 0) + (int(m.group(1)) if m else 0)


def yes_no(v):
    return True if v is True or v == "yes" else False if v is False or v == "no" else None


def wheelchair(d: dict) -> str:
    v = (((d.get("accessibility") or {}).get("mobility") or {}).get("wheelchair_route"))
    v = v if v not in (None, "unknown") else d.get("wheelchair_friendly")
    return {"yes": "ja", True: "ja", "no": "nej", False: "nej"}.get(v, "ukendt")


def guide(d: dict, layer: str | None, drive: int | None) -> dict:
    tags = d.get("tags") or []
    themes = [THEME[t] for t in tags if t in THEME]
    if d["category"] == "Family activities":
        themes.append("familieaktivitet")
    seasons: list[str] = []
    for s in d.get("seasonality") or []:
        seasons += [x for x in SEASON.get(s, []) if x not in seasons]
    vi = d.get("visit_information") or {}
    practical = []
    if vi.get("schedule"):
        practical.append({"label": "Åbningstider", "text": str(vi["schedule"])})
    if vi.get("cost_basis"):
        practical.append({"label": "Pris", "text": str(vi["cost_basis"])})
    links = d.get("links") or {}
    checked = sorted(str(e.get("checked_at")) for e in d.get("evidence") or [] if e.get("checked_at"))
    return {
        "source": "thomasericolesen/callemilano",
        "status": STATUS[d["status"]],
        "layer": LAYER.get(layer) if layer else "lokal",
        "drive_minutes": drive,
        "distance_km": None,
        "duration": next((DURATION[t] for t in ("Overnight", "Full day", "Half day") if t in tags), None),
        "age_groups": [AGE[a] for a in d.get("age_groups") or [] if a in AGE],
        "fit": {FIT_KEY[k]: FIT.get(v, "ukendt") for k, v in (d.get("family_score") or {}).items() if k in FIT_KEY},
        "energy": ENERGY.get(d.get("energy_level")),
        "seasons": seasons,
        "themes": themes,
        "cost_level": COST.get(d.get("cost_level")),
        "booking_required": yes_no(d.get("booking_required")),
        "wheelchair": wheelchair(d),
        "summary": d.get("description_short") or None,
        "practical": practical,
        "links": {"official": links.get("official_website"), "booking": links.get("booking"),
                  "info": links.get("visitor_information")},
        "checked_at": checked[-1] if checked else None,
        "text_language": "en",
    }


def main(check_only: bool) -> None:
    membership = {r["slug"]: r for r in csv.DictReader(open(ROOT / "data" / "layer-membership.csv", encoding="utf-8"))}
    places, skipped = [], {"status": 0, "out_of_area": 0}
    for f in sorted(PLACES.glob("*.md")):
        d = front_matter(f)
        if d.get("status") not in SHOWN:
            skipped["status"] += 1
            continue
        mem = membership.get(d["slug"])
        drive = minutes((d.get("driving_time_from_casa_de_la_familia") or {}).get("duration"))
        if not mem and (drive is None or drive > LOCAL_MAX_MIN):
            skipped["out_of_area"] += 1
            continue
        c = d.get("coordinates") or {}
        places.append({
            "id": d["id"], "slug": d["slug"], "name": d["name"], "category": CATEGORY[d["category"]],
            "record_category": d["category"], "record_status": d["status"],
            "approved": d["status"] in ("approved", "published"),
            "municipality": d.get("municipality"), "lat": c.get("latitude"), "lng": c.get("longitude"),
            "google_maps_url": d.get("google_maps_url"),
            "google_place_id": (d.get("external_ids") or {}).get("google_place_id"),
            "url": (d.get("links") or {}).get("official_website"),
            "tags": [THEME.get(t, t) for t in d.get("tags") or []],
            "description": d.get("description_long") or None,
            "catalogue_group": mem["catalogue_group"] if mem else None,
            "guide": guide(d, mem["layer"] if mem else None, drive),
        })
    holidays = [{k: r[k] for k in ("date", "name", "scope", "municipality", "source_url")}
                for r in csv.DictReader(open(ROOT / "data" / "holidays.csv", encoding="utf-8"))]
    by_cat: dict[str, int] = {}
    for p in places:
        by_cat[p["category"]] = by_cat.get(p["category"], 0) + 1
    print(f"places: {len(places)} {by_cat}; skipped: {skipped}; holidays: {len(holidays)}")
    if check_only:
        return
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {"generated": date.today().isoformat(), "source": "thomasericolesen/callemilano",
                "script": "tools/app_export.py", "places": len(places), "holidays": len(holidays),
                "rule": "status needs_fact_check or later; primary area (drive <= 30 min) or layer membership"}
    (OUT / "places.json").write_text(json.dumps({"manifest": manifest, "records": places}, ensure_ascii=False, indent=1) + "\n")
    (OUT / "holidays.json").write_text(json.dumps({"manifest": manifest, "holidays": holidays}, ensure_ascii=False, indent=1) + "\n")
    print(f"wrote {OUT.relative_to(ROOT)}/places.json and holidays.json")


if __name__ == "__main__":
    main("--check" in sys.argv)
