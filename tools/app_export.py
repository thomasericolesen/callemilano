#!/usr/bin/env python3
"""Export place records for the callemilano.dk app (Lovable project "Vores Spanske Hjem").

Usage:  python3 tools/app_export.py            # writes data/app-export/
        python3 tools/app_export.py --check    # prints counts only

Owner decisions 2026-11-02 (docs/webapp-byggeplan.md):
  * the app shows records with status needs_fact_check or later; drafts and archived records are left out;
  * records that are not yet fact-checked are labelled in the app ("Ikke faktatjekket"); a fact-checked
    record (needs_editorial_review) counts as approved (owner decision 2026-11-10);
  * only the current phase is exported: the primary area (route-checked drive <= 30 min) and records listed
    in data/layer-membership.csv. Other out-of-area records are archive (AGENTS.md) and are not exported.

The output is derived data, like data/place-catalog.csv: never edit it by hand; re-run this script after
record changes. The structured `guide` object follows the app's schema in src/lib/guide.ts. Texts are the
records' English texts; Danish texts already written in the app are kept by the app's import.

Danish texts (owner request 2026-11-08): data/app-texts-da.json holds Danish `summary` and `practical` per
place ID, each tied to a hash (`source_sha`) of the English texts it was translated from. When the hash still
matches, the export sends the Danish texts with text_language "da"; when the English texts have changed
(new price, new hours), the export falls back to English and lists the place under manifest.danish_stale, so a
stale translation never hides a newer fact. `--da-todo OUT.json` writes the places that need a (new)
translation, with the English texts and their hash.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import LOCAL_MAX_MIN, PLACES, ROOT, minutes  # noqa: E402
from common import load_front_matter as front_matter  # noqa: E402
OUT = ROOT / "data" / "app-export"
DA_FILE = ROOT / "data" / "app-texts-da.json"
SHOWN = {"needs_fact_check", "needs_editorial_review", "approved", "published"}

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


def yes_no(v):
    return True if v is True or v == "yes" else False if v is False or v == "no" else None


def wheelchair(d: dict) -> str:
    v = (((d.get("accessibility") or {}).get("mobility") or {}).get("wheelchair_route"))
    v = v if v not in (None, "unknown") else d.get("wheelchair_friendly")
    return {"yes": "ja", True: "ja", "no": "nej", False: "nej"}.get(v, "ukendt")


def covers_schedule(e: dict) -> bool:
    toks = {x.strip() for x in str(e.get("field", "")).split(",")}
    return bool(toks & {"visit_information", "visit_information.schedule"})


def trip_info(d: dict) -> dict:
    """Fields the app's planTrip needs (same rules as tools/trip.py: opening_info, bars, rainy-day plan B)."""
    vi = d.get("visit_information") or {}
    tags = d.get("tags") or []
    sched_dates = sorted(str(e.get("checked_at"))[:10] for e in d.get("evidence") or []
                         if covers_schedule(e) and e.get("checked_at"))
    text = (d.get("description_long") or "").lower()
    contact = (d.get("links") or {}).get("contact") or ""
    return {
        "record_category": d["category"],
        "municipality": d.get("municipality"),
        "schedule": vi.get("schedule"),
        "schedule_checked_at": sched_dates[-1] if sched_dates else None,
        "valid_until": str(vi["valid_until"])[:10] if vi.get("valid_until") else None,
        "needs_fixed_hours": d["category"] in ("Family activities", "Excursions") or "Museum" in tags,
        "rainy_day": "Rainy day" in tags,
        "is_bar": "keep an eye on your drink" in text or "take a taxi or uber" in text,
        "phone": contact[4:] if contact.startswith("tel:") else None,
        "booking_lead_time": vi.get("booking_lead_time"),
        "typical_duration": vi.get("typical_duration"),
        "updated_at": str(d.get("updated_at") or "")[:10] or None,
    }


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
        "trip": trip_info(d),
    }


def source_sha(g: dict) -> str:
    """Hash of the English texts a Danish translation is made from."""
    src = json.dumps({"summary": g.get("summary"), "practical": g.get("practical")}, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(src.encode("utf-8")).hexdigest()[:16]


def apply_danish(places: list[dict], da: dict) -> tuple[int, list[str], list[dict]]:
    """Swap in current Danish texts; return (count applied, stale ids, todo list)."""
    applied, stale, todo = 0, [], []
    for p in places:
        g = p["guide"]
        sha = source_sha(g)
        t = da.get(p["id"])
        if t and t.get("source_sha") == sha:
            g["summary"] = t.get("summary") or g["summary"]
            g["practical"] = t.get("practical") or g["practical"]
            g["text_language"] = "da"
            applied += 1
            continue
        if t:
            stale.append(p["id"])
        todo.append({"id": p["id"], "name": p["name"], "category": p["category"], "source_sha": sha,
                     "summary": g.get("summary"), "practical": g.get("practical"),
                     "previous_da": t if t else None})
    return applied, stale, todo


def main(check_only: bool, da_todo: str | None = None) -> None:
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
            # Formal approved/published only. Since 2026-11-10 a fact-checked record (needs_editorial_review)
            # also counts as approved for display; the app does not read this field.
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
    da = json.loads(DA_FILE.read_text(encoding="utf-8")) if DA_FILE.exists() else {}
    da_applied, da_stale, todo = apply_danish(places, da)
    print(f"danish: {da_applied} applied, {len(da_stale)} stale {da_stale}")
    if da_todo:
        Path(da_todo).write_text(json.dumps(todo, ensure_ascii=False, indent=1) + "\n")
        print(f"wrote {da_todo} ({len(todo)} places without current Danish texts)")
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
                "rule": "status needs_fact_check or later; primary area (drive <= 30 min) or layer membership",
                "danish": da_applied, "danish_stale": da_stale}
    (OUT / "places.json").write_text(json.dumps({"manifest": manifest, "records": places}, ensure_ascii=False, indent=1) + "\n")
    (OUT / "holidays.json").write_text(json.dumps({"manifest": manifest, "holidays": holidays}, ensure_ascii=False, indent=1) + "\n")
    print(f"wrote {OUT.relative_to(ROOT)}/places.json and holidays.json")


if __name__ == "__main__":
    todo_path = sys.argv[sys.argv.index("--da-todo") + 1] if "--da-todo" in sys.argv else None
    main("--check" in sys.argv, todo_path)
