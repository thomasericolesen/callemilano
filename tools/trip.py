#!/usr/bin/env python3
"""Hjælpeværktøj til turforslag (agenterne Alpha, Bravo, Charlie, Delta, Ecco).

Kommandoer:
  places                      Vis de steder, der må indgå i turforslag (lokalt lag + udflugtslag).
  nearby SLUG [SLUG ...]      Alpha: andre steder i nærheden af de valgte (fra kataloget).
  weather SLUG [...] --date D Bravo: vejrudsigt fra Open-Meteo for valgte steder og dato.
  traffic SLUG [SLUG ...]     Bravo: aktive DGT-trafikhændelser nær ruten fra Casa de la Familia.
  restaurants SLUG [...]      Restaurant-stedposter først, derefter data/restaurant-directory.csv (3 dyre, 3 mellem, 4 billige).
  hours-status                Alpha (fase 1): steder, hvis åbningstider mangler eller er forældede.
  coverage                    Charlie: hvor mange restauranter hvert sted har i kataloget.
  check-restaurants           Charlie/Delta: valider data/restaurant-directory.csv.
  plan SLUG [...] --date D     Fase 2: samler steder, åbningsstatus, helligdage, vejr, trafik, restauranter,
                              forslag og automatiske tjek (Delta) i trips/<id>/plan.json.
  render TRIP_DIR             Ecco: lav turforslag.html (og turforslag.pdf, hvis Playwright findes).

Alle kommandoer skriver JSON til stdout (undtagen render), så agenterne kan gemme resultatet.
Værktøjet gætter aldrig fakta: mangler data, svares der "ukendt" med en forklaring.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import html
import json
import math
import re
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    CATALOG, LAYER_MEMBERSHIP, ORIGIN, PLACES as PLACES_DIR, ROOT, haversine_km, load_front_matter, minutes,
)

ORIGIN_NAME = "Casa de la Familia, Las Lagunas de Mijas"
RESTAURANTS = ROOT / "data" / "restaurant-directory.csv"
AREAS = ROOT / "data" / "restaurant-areas.csv"
HOLIDAYS = ROOT / "data" / "holidays.csv"
HOURS_FRESH_DAYS = 60        # åbningstider tjekket for højst 60 dage siden regnes som aktuelle
RESTAURANT_STALE_DAYS = 183  # restaurantrækker ældre end ca. 6 måneder markeres
# Kategorier, hvor et sted normalt har faste åbningstider (strand, by og natur er åbne områder).
HOURS_CATEGORIES = {"Family activities", "Excursions"}
LOCAL_MAX_MIN = 30
WALK_KM = 0.8          # ca. 10 minutters gang (ejerbeslutning 2026-11-01)
FALLBACK_KM = 3.0      # luftlinje; bruges kun når der er for få restauranter i gåafstand
PICK = {"dyr": 3, "mellem": 3, "billig": 4}
PRICE_BANDS = {"billig", "mellem", "dyr"}
KIDS = {"ja", "nej", "ukendt"}
KIDS_BASIS = {"egen kilde", "anmeldelser", "-"}
DRESS = {"ingen", "pæn afslappet", "formel", "ukendt"}
R_STATUS = {"aktiv", "skal tjekkes", "lukket"}
R_COLUMNS = [
    "restaurant_id", "area_id", "name", "address", "municipality", "latitude", "longitude", "phone", "website",
    "cuisine", "price_band", "price_basis", "kids_welcome", "kids_basis", "dress_code",
    "hours_note", "sources", "checked_at", "checked_by", "status", "notes",
]
OPEN_METEO = "https://api.open-meteo.com/v1/forecast"
DGT_FEED = "https://nap.dgt.es/datex2/v3/dgt/SituationPublication/datex2_v37.xml"
UA = {"User-Agent": "CalleMilano-trip-planner/1.0"}

WMO_DA = {
    0: "klart", 1: "overvejende klart", 2: "delvis skyet", 3: "overskyet", 45: "tåge", 48: "rimtåge",
    51: "let støvregn", 53: "støvregn", 55: "kraftig støvregn", 61: "let regn", 63: "regn",
    65: "kraftig regn", 66: "isslag", 67: "kraftigt isslag", 71: "let sne", 73: "sne", 75: "kraftig sne",
    77: "snekorn", 80: "lette byger", 81: "byger", 82: "kraftige byger", 85: "snebyger",
    86: "kraftige snebyger", 95: "torden", 96: "torden med hagl", 99: "kraftig torden med hagl",
}


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="minutes")


def load_places():
    layers = {}
    if LAYER_MEMBERSHIP.exists():
        for r in csv.DictReader(LAYER_MEMBERSHIP.open(encoding="utf-8")):
            layers[r["slug"]] = r["layer"]
    out = {}
    for r in csv.DictReader(CATALOG.open(encoding="utf-8")):
        if not r.get("latitude") or not r.get("longitude"):
            continue
        mins = minutes(r.get("driving_time", ""))
        if mins is not None and mins <= LOCAL_MAX_MIN:
            layer = "local_30km"
        else:
            layer = layers.get(r["slug"], "archive")
        out[r["slug"]] = {
            "slug": r["slug"], "id": r["id"], "name": r["name"], "status": r["status"],
            "category": r["category"], "tags": [t.strip() for t in r["tags"].split(";") if t.strip()] if r["tags"] else [],
            "municipality": r["municipality"], "lat": float(r["latitude"]), "lon": float(r["longitude"]),
            "driving_time": r["driving_time"] or "ukendt (ikke route-tjekket)",
            "driving_min": mins, "layer": layer, "record_file": r["record_file"],
        }
    return out


def eligible(places):
    return {k: v for k, v in places.items() if v["layer"] != "archive"}


def pick_places(slugs):
    places = load_places()
    chosen, errors = [], []
    for s in slugs:
        p = places.get(s)
        if not p:
            errors.append(f"ukendt slug: {s}")
        elif p["layer"] == "archive":
            errors.append(f"{s} er arkiv (uden for lokalt lag og udflugtslag) og må ikke anbefales")
        else:
            chosen.append(p)
    if errors:
        print(json.dumps({"errors": errors}, ensure_ascii=False, indent=2))
        sys.exit(2)
    return places, chosen


def maps_dir_url(lat, lon):
    q = urllib.parse.urlencode({"api": 1, "origin": f"{ORIGIN[0]},{ORIGIN[1]}",
                                "destination": f"{lat},{lon}", "travelmode": "driving"})
    return f"https://www.google.com/maps/dir/?{q}"


def route_minutes_between(origin, destination, departure_time):
    """Return traffic-aware Google route time between stops, or None when unavailable."""
    body = {"origin": {"location": {"latLng": {"latitude": origin["lat"], "longitude": origin["lon"]}}},
            "destination": {"location": {"latLng": {"latitude": destination["lat"], "longitude": destination["lon"]}}},
            "travelMode": "DRIVE", "routingPreference": "TRAFFIC_AWARE_OPTIMAL", "departureTime": departure_time}
    try:
        response = subprocess.run(
            ["curl", "-sS", "-m", "20", "-X", "POST", "https://routes.googleapis.com/directions/v2:computeRoutes",
             "-H", "Content-Type: application/json", "-H", "X-Goog-Api-Key: dummy",
             "-H", "X-Goog-FieldMask: routes.duration,routes.distanceMeters", "-d", json.dumps(body)],
            capture_output=True, text=True, timeout=25, check=False)
        route = (json.loads(response.stdout or "{}").get("routes") or [{}])[0]
        match = re.fullmatch(r"(\d+(?:\.\d+)?)s", route.get("duration", ""))
        if response.returncode == 0 and match:
            return round(float(match.group(1)) / 60)
    except (OSError, subprocess.TimeoutExpired, ValueError, TypeError):
        pass
    return None


def current_route_departure(now=None):
    """Return the current instant as UTC RFC 3339 for Google Routes traffic estimates."""
    now = now or dt.datetime.now(dt.timezone.utc)
    return now.astimezone(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def fetch(url, timeout=40, retries=4):
    """Hent en URL; ved HTTP 429/5xx prøves igen med stigende ventetid (2, 4, 8, 16 s)."""
    import time
    import urllib.error
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers=UA)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as err:
            if attempt == retries or not (err.code == 429 or err.code >= 500):
                raise
            time.sleep(2 ** (attempt + 1))


def out(obj):
    print(json.dumps(obj, ensure_ascii=False, indent=2))


# ---------------------------------------------------------------- places / nearby (Alpha)
def cmd_places(_args):
    rows = sorted(eligible(load_places()).values(), key=lambda p: (p["driving_min"] or 999, p["name"]))
    out([{k: p[k] for k in ("slug", "name", "category", "layer", "driving_time", "status")} for p in rows])


def cmd_nearby(args):
    places, chosen = pick_places(args.slugs)
    chosen_slugs = {p["slug"] for p in chosen}
    cands = []
    for p in eligible(places).values():
        if p["slug"] in chosen_slugs:
            continue
        d = min(haversine_km(c["lat"], c["lon"], p["lat"], p["lon"]) for c in chosen)
        if d <= args.km:
            nearest = min(chosen, key=lambda c: haversine_km(c["lat"], c["lon"], p["lat"], p["lon"]))
            cands.append({
                "slug": p["slug"], "name": p["name"], "category": p["category"], "layer": p["layer"],
                "status": p["status"], "straight_line_km_to_nearest_choice": round(d, 1),
                "nearest_choice": nearest["slug"], "driving_time_from_casa": p["driving_time"],
            })
    cands.sort(key=lambda c: c["straight_line_km_to_nearest_choice"])
    out({"generated_at": now_iso(), "radius_km_straight_line": args.km,
         "note": "Afstand er luftlinje mellem stedernes kortpunkter; den er ikke en køretid.",
         "chosen": [c["slug"] for c in chosen], "candidates": cands})


# ---------------------------------------------------------------- weather (Bravo)
def get_weather(chosen, date_str):
    date = dt.date.fromisoformat(date_str)
    today = dt.date.today()
    horizon = (date - today).days
    res = {"generated_at": now_iso(), "date": date_str,
           "source": "Open-Meteo (api.open-meteo.com); reserve: met.no", "places": []}
    if horizon < 0 or horizon > 15:
        res["note"] = ("Datoen ligger uden for Open-Meteos 16-dages prognose. Der gives ingen vejrudsigt; "
                       "tjek igen tættere på turen.")
        return res
    for p in chosen:
        try:
            res["places"].append(_weather_open_meteo(p, date_str))
        except Exception as e1:  # noqa: BLE001
            if horizon > 8:
                res["places"].append({"slug": p["slug"], "name": p["name"],
                                      "error": f"Open-Meteo fejlede ({e1}); met.no dækker kun ca. 9 dage frem"})
                continue
            try:
                res["places"].append(_weather_met_no(p, date_str))
            except Exception as e2:  # noqa: BLE001
                res["places"].append({"slug": p["slug"], "name": p["name"],
                                      "error": f"Open-Meteo: {e1}; met.no: {e2}"})
    return res


def cmd_weather(args):
    _, chosen = pick_places(args.slugs)
    out(get_weather(chosen, args.date))


MET_NO = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
MET_NO_UA = {"User-Agent": "CalleMilano-trip-planner/1.0 github.com/thomasericolesen/callemilano"}
MET_SYMBOL_DA = {
    "clearsky": "klart", "fair": "overvejende klart", "partlycloudy": "delvis skyet", "cloudy": "overskyet",
    "fog": "tåge", "lightrain": "let regn", "rain": "regn", "heavyrain": "kraftig regn",
    "lightrainshowers": "lette byger", "rainshowers": "byger", "heavyrainshowers": "kraftige byger",
    "rainandthunder": "regn og torden", "lightrainshowersandthunder": "byger med torden",
    "rainshowersandthunder": "byger med torden", "heavyrainandthunder": "kraftig regn og torden",
    "lightsleet": "let slud", "sleet": "slud", "lightsnow": "let sne", "snow": "sne",
}


def _weather_met_no(p, date):
    from zoneinfo import ZoneInfo
    url = f"{MET_NO}?lat={p['lat']:.4f}&lon={p['lon']:.4f}"
    req = urllib.request.Request(url, headers=MET_NO_UA)
    with urllib.request.urlopen(req, timeout=40) as resp:
        data = json.loads(resp.read())
    tz = ZoneInfo("Europe/Madrid")
    temps, winds, rain, hours, noon = [], [], 0.0, [], None
    for ts in data["properties"]["timeseries"]:
        t = dt.datetime.fromisoformat(ts["time"].replace("Z", "+00:00")).astimezone(tz)
        if t.date().isoformat() != date:
            continue
        det = ts["data"]["instant"]["details"]
        temps.append(det["air_temperature"])
        winds.append(det.get("wind_speed", 0) * 3.6)
        n1 = ts["data"].get("next_1_hours")
        if n1:
            rain += n1["details"].get("precipitation_amount", 0)
        sym = (n1 or ts["data"].get("next_6_hours") or {}).get("summary", {}).get("symbol_code", "")
        text = MET_SYMBOL_DA.get(sym.split("_")[0], sym or "ukendt")
        if t.hour in (9, 12, 15, 18):
            hours.append({"time": t.strftime("%H:%M"), "temp_c": det["air_temperature"],
                          "rain_prob_pct": None, "text": text})
        if t.hour == 12 or (noon is None and t.hour > 9):
            noon = text
    if not temps:
        raise ValueError("ingen data for datoen")
    return {"slug": p["slug"], "name": p["name"], "text": noon or "ukendt",
            "temp_min_c": round(min(temps), 1), "temp_max_c": round(max(temps), 1),
            "rain_prob_max_pct": None, "rain_mm": round(rain, 1), "wind_max_kmh": round(max(winds)),
            "gusts_max_kmh": None, "uv_max": None, "sunrise": None, "sunset": None, "hours": hours,
            "source": "met.no Locationforecast (reserve, da Open-Meteo ikke svarede)", "source_url": url}


def _weather_open_meteo(p, date):
    q = urllib.parse.urlencode({
        "latitude": p["lat"], "longitude": p["lon"], "timezone": "Europe/Madrid",
        "start_date": date, "end_date": date,
        "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,"
                 "precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,uv_index_max,sunrise,sunset",
        "hourly": "temperature_2m,precipitation_probability,weather_code",
    })
    url = f"{OPEN_METEO}?{q}"
    data = json.loads(fetch(url, retries=2))
    d = data["daily"]
    hours = []
    for i, t in enumerate(data["hourly"]["time"]):
        if int(t[11:13]) in (9, 12, 15, 18):
            hours.append({"time": t[11:16], "temp_c": data["hourly"]["temperature_2m"][i],
                          "rain_prob_pct": data["hourly"]["precipitation_probability"][i],
                          "text": WMO_DA.get(data["hourly"]["weather_code"][i], "ukendt")})
    return {
        "slug": p["slug"], "name": p["name"], "text": WMO_DA.get(d["weather_code"][0], "ukendt"),
        "temp_min_c": d["temperature_2m_min"][0], "temp_max_c": d["temperature_2m_max"][0],
        "rain_prob_max_pct": d["precipitation_probability_max"][0],
        "rain_mm": d["precipitation_sum"][0], "wind_max_kmh": d["wind_speed_10m_max"][0],
        "gusts_max_kmh": d["wind_gusts_10m_max"][0], "uv_max": d["uv_index_max"][0],
        "sunrise": d["sunrise"][0][11:16], "sunset": d["sunset"][0][11:16],
        "hours": hours, "source": "Open-Meteo", "source_url": url,
    }


# ---------------------------------------------------------------- traffic (Bravo)
def _local(tag):
    return tag.rsplit("}", 1)[-1]


def _seg_dist_km(p, a, b):
    """Afstand (km) fra punkt p til linjestykket a-b, med en simpel ækvirektangulær projektion."""
    lat0 = math.radians((a[0] + b[0]) / 2)
    def xy(q):
        return (math.radians(q[1]) * math.cos(lat0) * 6371.0, math.radians(q[0]) * 6371.0)
    px, py = xy(p)
    ax, ay = xy(a)
    bx, by = xy(b)
    dx, dy = bx - ax, by - ay
    L = dx * dx + dy * dy
    t = 0 if L == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / L))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy))


def parse_dgt(raw):
    root = ET.fromstring(raw)
    pub = next((e.text for e in root.iter() if _local(e.tag) == "publicationTime"), None)
    items = []
    for rec in root.iter():
        if _local(rec.tag) != "situationRecord":
            continue
        info = {"id": rec.get("id"), "type": (rec.get("{http://www.w3.org/2001/XMLSchema-instance}type") or "")
                .split(":")[-1], "points": [], "roads": set(), "municipalities": set(), "km": []}
        for e in rec.iter():
            n = _local(e.tag)
            if n == "pointCoordinates":
                lat = lon = None
                for c in e:
                    if _local(c.tag) == "latitude":
                        lat = float(c.text)
                    elif _local(c.tag) == "longitude":
                        lon = float(c.text)
                if lat is not None and lon is not None:
                    info["points"].append((lat, lon))
            elif n == "roadName" and e.text:
                info["roads"].add(e.text)
            elif n == "municipality" and e.text:
                info["municipalities"].add(e.text)
            elif n == "kilometerPoint" and e.text:
                info["km"].append(e.text)
            elif n in ("causeType", "roadMaintenanceType", "accidentType", "obstructionType",
                       "roadOrCarriagewayOrLaneManagementType", "poorEnvironmentType", "trafficConstrictionType",
                       "abnormalTrafficType", "severity", "overallStartTime", "overallEndTime",
                       "validityStatus", "comment") and e.text and e.text.strip():
                info.setdefault(n, e.text.strip())
        items.append(info)
    return pub, items


def get_traffic(chosen, buffer_km=3.0):
    try:
        raw = fetch(DGT_FEED, timeout=90)
    except Exception as e:  # noqa: BLE001
        return {"generated_at": now_iso(), "error": f"DGT-feed kunne ikke hentes: {e}", "source": DGT_FEED,
                "routes": [{"slug": p["slug"], "name": p["name"], "route_checked_driving_time": p["driving_time"],
                            "incidents": [], "live_route_link": maps_dir_url(p["lat"], p["lon"])} for p in chosen]}
    pub, items = parse_dgt(raw)
    res = {"generated_at": now_iso(), "source": "DGT DATEX II (nap.dgt.es), aktive hændelser",
           "source_url": DGT_FEED, "dgt_publication_time": pub,
           "method": ("Hændelser med et kortpunkt inden for en korridor omkring luftlinjen fra Casa de la Familia "
                      "til stedet. Korridoren følger ikke vejen præcist; vurdér om vejen faktisk ligger på ruten."),
           "routes": []}
    for p in chosen:
        dest = (p["lat"], p["lon"])
        length = haversine_km(*ORIGIN, *dest)
        buf = max(buffer_km, 0.15 * length)
        hits = []
        for it in items:
            if not it["points"]:
                continue
            d = min(_seg_dist_km(pt, ORIGIN, dest) for pt in it["points"])
            if d <= buf:
                hits.append({
                    "roads": sorted(it["roads"]), "municipalities": sorted(it["municipalities"]),
                    "km_points": it["km"], "record_type": it["type"],
                    "cause": it.get("causeType"),
                    "detail": it.get("roadMaintenanceType") or it.get("accidentType") or it.get("obstructionType")
                    or it.get("poorEnvironmentType") or it.get("abnormalTrafficType"),
                    "management": it.get("roadOrCarriagewayOrLaneManagementType"),
                    "start": it.get("overallStartTime"), "end": it.get("overallEndTime"),
                    "km_from_corridor_line": round(d, 1),
                })
        hits.sort(key=lambda h: (h["roads"], h["start"] or ""))
        res["routes"].append({
            "slug": p["slug"], "name": p["name"], "route_checked_driving_time": p["driving_time"],
            "straight_line_km": round(length, 1), "corridor_km": round(buf, 1),
            "incidents": hits, "live_route_link": maps_dir_url(p["lat"], p["lon"]),
            "forecast_note": ("Ingen gratis trafikprognose. Brug den route-tjekkede normale køretid og åbn "
                              "live-linket lige før afgang."),
        })
    return res


def cmd_traffic(args):
    _, chosen = pick_places(args.slugs)
    out(get_traffic(chosen, args.buffer_km))


# ---------------------------------------------------------------- restaurants (Charlie)
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


# ---------------------------------------------------------------- plan (fase 2: Bravo + Delta som regler)
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


def weather_advice(w, category, small_kids):
    adv, wet = [], False
    rp, mm = w.get("rain_prob_max_pct"), w.get("rain_mm") or 0
    text = " ".join([w.get("text") or ""] + [h.get("text") or "" for h in w.get("hours", [])])
    showers = any(k in text for k in ("regn", "byger", "torden", "støvregn"))
    if (rp is not None and rp >= 50) or mm >= 2:
        wet = True
        adv.append("Regn er sandsynlig" + (": strand frarådes, brug plan B" if category == "Beaches" else "; tag regntøj med"))
    elif rp is None and showers:
        adv.append("Mulighed for byger i løbet af dagen; hav en plan B klar")
    if (w.get("gusts_max_kmh") or 0) >= 40 or (w.get("wind_max_kmh") or 0) >= 30:
        adv.append("Blæsende: strand og udsigtspunkter er mindre behagelige")
    if (w.get("uv_max") or 0) >= 6:
        adv.append("Høj UV: solcreme, hat og skygge" + (", især for de små" if small_kids else ""))
    if (w.get("temp_max_c") or 0) >= 32:
        adv.append("Meget varmt: undgå lange gåture midt på dagen")
    return adv, wet


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


# ---------------------------------------------------------------- render (Ecco)
CSS = """
@page { size: A4; margin: 14mm 14mm 16mm; }
:root { --ink:#1d2327; --muted:#5b6670; --line:#d9dee2; --accent:#b4532a; --soft:#f6f1ec; }
* { box-sizing: border-box; }
body { font: 11pt/1.45 -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; color: var(--ink);
       background:#fff; margin: 0 auto; max-width: 820px; padding: 16px; }
h1 { font-size: 21pt; margin: 0 0 2px; } h2 { font-size: 13.5pt; margin: 20px 0 6px; color: var(--accent);
     border-bottom: 1.5px solid var(--line); padding-bottom: 3px; break-after: avoid; }
h3 { font-size: 11.5pt; margin: 10px 0 2px; }
.meta { color: var(--muted); font-size: 9.5pt; } .summary { background: var(--soft); padding: 10px 12px; border-radius: 6px; }
.badge { display:inline-block; font-size:8.5pt; padding:1px 7px; border-radius:9px; border:1px solid var(--line); color:var(--muted); }
.warn { background:#fff4e5; border-left: 4px solid #e08a1e; padding: 8px 10px; margin: 8px 0; font-size: 10pt; }
.stop { border:1px solid var(--line); border-radius:6px; padding:8px 10px; margin:8px 0; break-inside: avoid; }
.stop .time { font-weight:700; color: var(--accent); margin-right: 6px; }
table { width:100%; border-collapse: collapse; font-size: 9.5pt; margin: 4px 0 8px; }
th, td { text-align:left; vertical-align: top; padding: 4px 5px; border-bottom: 1px solid var(--line); }
th { background: var(--soft); font-weight: 600; } tr { break-inside: avoid; }
a { color: #1f5f8b; text-decoration: none; word-break: break-word; }
ul { margin: 4px 0 4px 18px; padding: 0; } .small { font-size: 8.5pt; color: var(--muted); }
@media screen and (max-width: 600px) { body { padding: 12px 16px; font-size: 12pt; } table { font-size: 10.5pt; }
  .rtable thead { display:none; } .rtable tr { display:block; border-bottom: 1px solid var(--line); padding:6px 0; }
  .rtable td { display:block; border: none; padding: 1px 0; } .lbl { display:inline; } }
.lbl { display:none; color: var(--muted); }
"""


def e(x):
    return html.escape("" if x is None else str(x))


def link(url, label=None):
    if not url:
        return ""
    return f'<a href="{e(url)}">{e(label or url)}</a>'


def tel(phone):
    if not phone:
        return ""
    return f'<a href="tel:{e(re.sub(r"[^0-9+]", "", phone))}">{e(phone)}</a>'


def render_html(t):
    p = []
    p.append(f"<!doctype html><html lang='da'><head><meta charset='utf-8'>"
             f"<meta name='viewport' content='width=device-width, initial-scale=1'>"
             f"<title>{e(t.get('title', 'Turforslag'))}</title><style>{CSS}</style></head><body>")
    p.append(f"<h1>{e(t.get('title'))}</h1>")
    p.append(f"<div class='meta'>{e(t.get('date_label') or t.get('date'))} · {e(t.get('group'))} · "
             f"Udarbejdet {e(t.get('prepared_at'))}</div>")
    if t.get("status_note"):
        p.append(f"<div class='warn'>{e(t['status_note'])}</div>")
    if t.get("summary"):
        p.append(f"<p class='summary'>{e(t['summary'])}</p>")

    if t.get("stops"):
        p.append("<h2>Dagens plan</h2>")
        for s in t["stops"]:
            p.append("<div class='stop'>")
            p.append(f"<h3><span class='time'>{e(s.get('time'))}</span>{e(s.get('name'))}</h3>")
            if s.get("what"):
                p.append(f"<div>{e(s['what'])}</div>")
            facts = []
            if s.get("drive"):
                facts.append(f"Kørsel: {e(s['drive'])}")
            if s.get("opening"):
                facts.append(f"Åbent: {e(s['opening'])}")
            if s.get("price"):
                facts.append(f"Pris: {e(s['price'])}")
            if facts:
                p.append(f"<div class='small'>{' · '.join(facts)}</div>")
            for n in s.get("notes", []):
                p.append(f"<div class='small'>• {e(n)}</div>")
            links = [link(s.get("maps_url"), "Rute i Google Maps"), link(s.get("website"), "Officiel side")]
            links = [x for x in links if x]
            if links:
                p.append(f"<div class='small'>{' · '.join(links)}</div>")
            p.append("</div>")

    if t.get("weather"):
        p.append("<h2>Vejret</h2><table><tr><th>Sted</th><th>Vejr</th><th>Temp.</th><th>Regn</th>"
                 "<th>Vind</th><th>UV</th></tr>")
        for w in t["weather"]:
            p.append(f"<tr><td>{e(w.get('place'))}</td><td>{e(w.get('text'))}</td>"
                     f"<td>{e(w.get('temp'))}</td><td>{e(w.get('rain'))}</td><td>{e(w.get('wind'))}</td>"
                     f"<td>{e(w.get('uv'))}</td></tr>")
        p.append("</table>")
        if t.get("weather_note"):
            p.append(f"<div class='small'>{e(t['weather_note'])}</div>")

    tr = t.get("traffic") or {}
    if tr:
        p.append("<h2>Trafik</h2>")
        if tr.get("summary"):
            p.append(f"<p>{e(tr['summary'])}</p>")
        for i in tr.get("incidents", []):
            p.append(f"<div class='small'>• {e(i)}</div>")
        if tr.get("note"):
            p.append(f"<div class='small'>{e(tr['note'])}</div>")

    rs = t.get("restaurants") or {}
    labels = [("dyr", "Dyre (over 50 € pr. voksen)"), ("mellem", "Mellem (20–50 € pr. voksen)"),
              ("billig", "Billige (under 20 € pr. voksen)")]
    if any(rs.get(k) for k, _ in labels):
        p.append("<h2>Spisesteder</h2>")
        for key, lab in labels:
            items = rs.get(key) or []
            if not items:
                continue
            p.append(f"<h3>{e(lab)}</h3><table class='rtable'><thead><tr><th>Navn</th><th>Adresse</th>"
                     "<th>Kontakt</th><th>Børn</th><th>Påklædning</th></tr></thead><tbody>")
            for r in items:
                near = f" <span class='small'>({e(r.get('near'))})</span>" if r.get("near") else ""
                p.append(f"<tr><td><b>{e(r.get('name'))}</b>{near}<br><span class='small'>{e(r.get('cuisine'))}</span></td>"
                         f"<td>{e(r.get('address'))}</td>"
                         f"<td>{tel(r.get('phone'))}<br>{link(r.get('website'), 'Hjemmeside')}</td>"
                         f"<td><span class='lbl'>Børn: </span>{e(r.get('kids'))}</td>"
                         f"<td><span class='lbl'>Påklædning: </span>{e(r.get('dress'))}</td></tr>")
            p.append("</tbody></table>")

    if t.get("also_nearby"):
        p.append("<h2>Hvis I har tid: i nærheden</h2><ul>")
        for a in t["also_nearby"]:
            p.append(f"<li><b>{e(a.get('name'))}</b>: {e(a.get('why'))}</li>")
        p.append("</ul>")

    if t.get("caveats"):
        p.append("<h2>Godt at vide</h2><ul>")
        for c in t["caveats"]:
            p.append(f"<li>{e(c)}</li>")
        p.append("</ul>")

    if t.get("sources"):
        p.append("<h2>Kilder</h2><ul class='small'>")
        for s in t["sources"]:
            p.append(f"<li>{e(s.get('label'))}: {link(s.get('url'))} "
                     f"<span class='small'>(tjekket {e(s.get('checked_at'))})</span></li>")
        p.append("</ul>")
    p.append(f"<p class='small'>CalleMilano · Fra {e(ORIGIN_NAME)}. Åbningstider, priser og trafik kan ændre sig; "
             "tjek før afgang.</p></body></html>")
    return "\n".join(p)


def cmd_render(args):
    d = Path(args.trip_dir)
    t = json.loads((d / "trip.json").read_text(encoding="utf-8"))
    html_path = d / "turforslag.html"
    html_path.write_text(render_html(t), encoding="utf-8")
    print(f"HTML: {html_path}")
    pdf_path = d / "turforslag.pdf"
    node = shutil.which("node")
    if node:
        js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
              "const p=await b.newPage();await p.goto('file://'+process.argv[1]);"
              "await p.pdf({path:process.argv[2],format:'A4',printBackground:true});await b.close();})()"
              ".catch(e=>{console.error(e.message);process.exit(1)});")
        r = subprocess.run([node, "-e", js, str(html_path.resolve()), str(pdf_path.resolve())],
                           capture_output=True, text=True)
        if r.returncode == 0:
            print(f"PDF:  {pdf_path}")
            return
        print(f"PDF ikke lavet (Playwright): {r.stderr.strip()[:300]}")
    print("Åbn HTML-filen i en browser og vælg 'Udskriv → Gem som PDF'.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("places")
    s = sub.add_parser("nearby"); s.add_argument("slugs", nargs="+"); s.add_argument("--km", type=float, default=10.0)
    s = sub.add_parser("weather"); s.add_argument("slugs", nargs="+"); s.add_argument("--date", required=True)
    s = sub.add_parser("traffic"); s.add_argument("slugs", nargs="+"); s.add_argument("--buffer-km", type=float, default=3.0)
    s = sub.add_parser("restaurants"); s.add_argument("slugs", nargs="+")
    s.add_argument("--kids", action="store_true", help="prioritér steder hvor børn er velkomne")
    s = sub.add_parser("plan", help="fase 2: saml alt til et turforslag")
    s.add_argument("slugs", nargs="+"); s.add_argument("--date", required=True)
    s.add_argument("--adults", type=int, default=2); s.add_argument("--children", default="",
                   help="børns alder, kommasepareret, fx 4,9")
    s.add_argument("--seniors", type=int, default=0); s.add_argument("--reduced-mobility", action="store_true")
    s.add_argument("--wishes", default=""); s.add_argument("--out", help="turmappe, fx trips/2026-11-03-fuengirola")
    sub.add_parser("hours-status")
    sub.add_parser("coverage")
    sub.add_parser("check-restaurants")
    s = sub.add_parser("render"); s.add_argument("trip_dir")
    args = ap.parse_args()
    {"places": cmd_places, "nearby": cmd_nearby, "weather": cmd_weather, "traffic": cmd_traffic,
     "restaurants": cmd_restaurants, "plan": cmd_plan, "hours-status": cmd_hours_status, "coverage": cmd_coverage, "check-restaurants": cmd_check_restaurants,
     "render": cmd_render}[args.cmd](args)


if __name__ == "__main__":
    main()
