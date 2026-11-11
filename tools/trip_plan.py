"""Fase 2 (Bravo + Delta som regler): helligdage, åbningsstatus, gruppen, forslag og selve planen.

Del af tools/trip.py; kør kommandoerne gennem den.
"""
from __future__ import annotations

import csv
import datetime as dt
import json
from pathlib import Path

from common import LOCAL_MAX_MIN, ROOT, haversine_km, load_front_matter
from trip_core import (
    ORIGIN_NAME,
    current_route_departure,
    eligible,
    load_places,
    maps_dir_url,
    now_iso,
    out,
    pick_places,
    route_minutes_between,
)
from trip_weather import get_weather, weather_advice
from trip_traffic import get_traffic
from trip_restaurants import load_restaurants, lookup_restaurants


HOLIDAYS = ROOT / "data" / "holidays.csv"

HOURS_FRESH_DAYS = 60        # åbningstider tjekket for højst 60 dage siden regnes som aktuelle

# Kategorier, hvor et sted normalt har faste åbningstider (strand, by og natur er åbne områder).
HOURS_CATEGORIES = {"Family activities", "Excursions"}


def load_holidays():
    if not HOLIDAYS.exists():
        return []
    return list(csv.DictReader(HOLIDAYS.open(encoding="utf-8")))


def holidays_on(date_str, municipality=None):
    return [h for h in load_holidays() if h["date"] == date_str
            and (not h["municipality"] or h["municipality"] == municipality)]


def holiday_years():
    return {h["date"][:4] for h in load_holidays()}


def _as_date(v):
    if isinstance(v, dt.date):
        return v
    try:
        return dt.date.fromisoformat(str(v)[:10])
    except ValueError:
        return None


def opening_info(p, today):
    """Åbningsstatus fra stedposten. Fortolker ikke fritekst; vurderer kun om den findes og er aktuel."""
    rec = load_front_matter(ROOT / p["record_file"])
    vi = rec.get("visit_information") or {}
    links = rec.get("links") or {}
    sched = vi.get("schedule")
    def covers_schedule(e):
        toks = {t.strip() for t in str(e.get("field", "")).split(",")}
        return bool(toks & {"visit_information", "visit_information.schedule"})
    ev = [e for e in rec.get("evidence") or [] if covers_schedule(e)]
    checked = [d for d in (_as_date(e.get("checked_at")) for e in ev) if d]
    last = max(checked) if checked else None
    srcs = list(dict.fromkeys(e.get("source_url") for e in ev if e.get("source_url")))
    needs = p["category"] in HOURS_CATEGORIES or "Museum" in p["tags"]
    valid_until = _as_date(vi.get("valid_until"))
    if sched:
        if not last:
            state = "uden_dato"
        elif (today - last).days > HOURS_FRESH_DAYS or (valid_until and valid_until < today):
            state = "forældet"
        else:
            state = "aktuel"
    else:
        state = "ukendt" if needs else "åbent_område"
    return {"state": state, "schedule": sched, "last_checked": last.isoformat() if last else None,
            "sources": srcs, "official_website": links.get("official_website"),
            "booking": links.get("booking"), "booking_lead_time": vi.get("booking_lead_time"),
            "typical_duration": vi.get("typical_duration"), "cost_basis": vi.get("cost_basis"),
            "record_status": rec.get("status"), "description_short": rec.get("description_short"),
            "energy_level": rec.get("energy_level"), "needs_fixed_hours": needs}


def parse_group(args):
    ages = [int(a) for a in (args.children or "").split(",") if a.strip()]
    return {"adults": args.adults, "children_ages": ages, "seniors": args.seniors,
            "reduced_mobility": args.reduced_mobility,
            "has_children": bool(ages), "small_children": any(a <= 6 for a in ages)}


def nearby_suggestions(places, chosen, wet, small_kids, limit=4):
    chosen_slugs = {c["slug"] for c in chosen}
    chosen_cats = {c["category"] for c in chosen}
    radius = 10.0 if all(c["layer"] == "local_30km" for c in chosen) else 25.0
    out_ = []
    for p in eligible(places).values():
        if p["slug"] in chosen_slugs:
            continue
        nearest = min(chosen, key=lambda c: haversine_km(c["lat"], c["lon"], p["lat"], p["lon"]))
        d = haversine_km(nearest["lat"], nearest["lon"], p["lat"], p["lon"])
        if d > radius:
            continue
        score = d
        if p["category"] not in chosen_cats:
            score -= 2      # variation: fx by eller aktivitet efter en strand
        if wet and "Rainy day" in p["tags"]:
            score -= 5
        if wet and p["category"] == "Beaches":
            score += 5
        if small_kids and (p["driving_min"] or 999) > LOCAL_MAX_MIN:
            score += 3
        out_.append((score, {"slug": p["slug"], "name": p["name"], "category": p["category"],
                             "tags": p["tags"], "near": nearest["slug"], "straight_line_km": round(d, 1),
                             "driving_time_from_casa": p["driving_time"], "record_status": p["status"]}))
    out_.sort(key=lambda x: x[0])
    return [x for _, x in out_[:limit]]


def cmd_hours_status(_args):
    """Fase 1 (Alpha): hvilke steder mangler aktuelle åbningstider i stedposten?"""
    today = dt.date.today()
    rows = []
    for p in sorted(eligible(load_places()).values(), key=lambda p: (p["driving_min"] or 999)):
        op = opening_info(p, today)
        rows.append({"slug": p["slug"], "name": p["name"], "layer": p["layer"], "category": p["category"],
                     "state": op["state"], "last_checked": op["last_checked"],
                     "needs_work": op["state"] in ("ukendt", "forældet", "uden_dato")})
    out({"today": today.isoformat(), "fresh_days": HOURS_FRESH_DAYS,
         "needs_work": [r["slug"] for r in rows if r["needs_work"]], "places": rows})


def cmd_plan(args):
    today = dt.date.today()
    places, chosen = pick_places(args.slugs)
    date = dt.date.fromisoformat(args.date)
    group = parse_group(args)
    checks = []

    def chk(level, code, msg, slug=None):
        checks.append({"level": level, "code": code, "message": msg, "slug": slug})

    if date < today:
        chk("blokeret", "dato_i_fortiden", f"Turdatoen {args.date} ligger før i dag ({today}).")
    if args.date[:4] not in holiday_years():
        chk("forbehold", "helligdage_mangler", f"Helligdagskalenderen dækker ikke {args.date[:4]}.")

    wd = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"][date.weekday()]
    for h in holidays_on(args.date):
        if not h["municipality"]:
            lvl = "info" if h["scope"] == "festdag_soendag" else "forbehold"
            chk(lvl, "helligdag", f"{args.date} er helligdag i Andalusien ({h['name']}): åbningstider kan "
                "afvige fra normalen; ring eller tjek stedets side.")

    weather = get_weather(chosen, args.date)
    w_by = {w["slug"]: w for w in weather.get("places", [])}
    traffic = get_traffic(chosen)
    t_by = {r["slug"]: r for r in traffic.get("routes", [])}
    if weather.get("note"):
        chk("info", "vejr_for_langt_frem", weather["note"])
    if traffic.get("error"):
        chk("forbehold", "trafik_utilgængelig", "Trafikdata kunne ikke hentes; brug live-linket før afgang.")
    elif date != today:
        chk("info", "trafik_nu_billede", "Trafikhændelser er nu-billedet fra i dag; turen er en anden dag.")

    rest_rows = [r for r in load_restaurants() if r.get("status") == "aktiv"]
    any_wet = False
    stops = []
    route_departure = current_route_departure()
    previous = None
    for p in chosen:
        op = opening_info(p, today)
        hol = holidays_on(args.date, p["municipality"])
        w = w_by.get(p["slug"])
        advice, wet = (weather_advice(w, p["category"], group["small_children"]) if w and "error" not in w
                       else ([], False))
        any_wet = any_wet or wet
        rest = lookup_restaurants(p, group["has_children"], rest_rows, today)
        from_previous = None
        if previous:
            straight_line_m = round(haversine_km(previous["lat"], previous["lon"],
                                                 p["lat"], p["lon"]) * 1000)
            leg_minutes = route_minutes_between(previous, p, route_departure)
            from_previous = {"slug": previous["slug"], "name": previous["name"],
                             "reach": "drive", "straight_line_m": straight_line_m,
                             "drive_min": leg_minutes,
                             "source": "Google Routes API computeRoutes" if leg_minutes is not None else None,
                             "route_checked": leg_minutes is not None}
        stops.append({"slug": p["slug"], "name": p["name"], "category": p["category"], "tags": p["tags"],
                      "municipality": p["municipality"], "layer": p["layer"],
                      "driving_time": p["driving_time"], "driving_min": p["driving_min"],
                      "from_previous": from_previous,
                      "maps_url": maps_dir_url(p["lat"], p["lon"]), "opening": op, "holidays": hol,
                      "weather": w, "weather_advice": advice, "traffic": t_by.get(p["slug"]),
                      "restaurants": rest})
        previous = p
        s_ = p["slug"]
        # Owner decision 2026-11-10: a fact-checked record (needs_editorial_review) counts as approved.
        if op["record_status"] not in ("needs_editorial_review", "approved", "published"):
            chk("info", "udkast", f"{p['name']}: stedposten er '{op['record_status']}', ikke faktatjekket.", s_)
        if op["state"] in ("ukendt", "forældet", "uden_dato"):
            why = {"ukendt": "ingen åbningstider i stedposten", "forældet": f"sidst tjekket {op['last_checked']}",
                   "uden_dato": "åbningstider uden tjekdato"}[op["state"]]
            chk("tjek", "åbningstid_" + op["state"], f"{p['name']}: {why}. Alpha skal lave et hurtigt tjek.", s_)
        elif op["state"] == "aktuel":
            chk("info", "åbningstid_fortolkes", f"{p['name']}: åbningstiderne er fritekst; Ecco skal læse dem for "
                f"{args.date} ({wd}).", s_)
        for h in [h for h in hol if h["municipality"]]:
            chk("forbehold", "lokal_helligdag", f"{p['name']}: {args.date} er lokal helligdag i "
                f"{h['municipality']} ({h['name']}); åbningstider kan afvige.", s_)
        if wet and p["category"] == "Beaches":
            chk("forbehold", "regn_strand", f"{p['name']}: regn er sandsynlig; foreslå plan B.", s_)
        if group["small_children"] and (p["driving_min"] or 999) > LOCAL_MAX_MIN:
            chk("forbehold", "lang_køretur_små_børn",
                f"{p['name']}: {p['driving_time']} kørsel er lang for små børn.", s_)
        if group["has_children"] and p["layer"] != "local_30km":
            chk("forbehold", "udflugtslag_familie", f"{p['name']}: ligger i udflugtslaget ({p['layer']}), som er "
                "målrettet unge voksne; overvej om dagen passer til børnene.", s_)
        if w and "error" not in w and w.get("rain_prob_max_pct") is None:
            chk("info", "vejr_reserve", f"{p['name']}: vejret er fra met.no (reserve); regnrisiko i %, UV og "
                "solopgang/-nedgang mangler.", s_)
        if p["driving_min"] is None:
            chk("forbehold", "køretid_ukendt", f"{p['name']}: køretiden er ikke route-tjekket.", s_)
        if rest["gaps"]:
            chk("forbehold", "restauranthuller", f"{p['name']}: færre spisesteder end målet "
                f"({', '.join(rest['gaps'])}). Kør /restaurant-indsamling.", s_)
        stale = [r["name"] for band in rest["restaurants"].values() for r in band if r["stale"]]
        if stale:
            chk("forbehold", "restauranter_gamle", f"{p['name']}: over 6 måneder siden tjek: {', '.join(stale)}.", s_)
        unknown_kids = [r["name"] for band in rest["restaurants"].values() for r in band
                        if r["kids_welcome"] == "ukendt"]
        if group["has_children"] and unknown_kids:
            chk("info", "børn_ukendt", f"{p['name']}: børn velkomne er ukendt for {len(unknown_kids)} spisested(er).", s_)
        if group["reduced_mobility"] or group["seniors"]:
            chk("info", "tilgængelighed", f"{p['name']}: tilgængelighed er ikke vurderet af redaktøren; "
                "omtal den som ukendt, medmindre stedposten har det.", s_)

    levels = {c["level"] for c in checks}
    verdict = ("blokeret" if "blokeret" in levels else "kræver_tjek" if "tjek" in levels
               else "ok_med_forbehold" if "forbehold" in levels else "ok")
    plan = {
        "generated_at": now_iso(), "today": today.isoformat(), "date": args.date,
        "weekday": wd,
        "origin": ORIGIN_NAME, "group": group, "wishes": args.wishes or "",
        "stops": stops,
        "first_stop_driving_min": stops[0]["driving_min"] if stops else None,
        "suggestions": nearby_suggestions(places, chosen, any_wet, group["small_children"]),
        "weather_source": weather.get("source"), "weather_note": weather.get("note"),
        "traffic_source": {"source": traffic.get("source"), "url": traffic.get("source_url"),
                           "dgt_publication_time": traffic.get("dgt_publication_time"),
                           "method": traffic.get("method")},
        "checks": checks, "verdict": verdict,
        "needs_quick_check": sorted({c["slug"] for c in checks if c["level"] == "tjek" and c["slug"]}),
    }
    if args.out:
        d = Path(args.out)
        d.mkdir(parents=True, exist_ok=True)
        (d / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        print(json.dumps({"plan": str(d / "plan.json"), "verdict": verdict,
                          "needs_quick_check": plan["needs_quick_check"],
                          "checks": [f"[{c['level']}] {c['message']}" for c in checks]},
                         ensure_ascii=False, indent=2))
    else:
        print(json.dumps(plan, ensure_ascii=False, indent=2, default=str))
