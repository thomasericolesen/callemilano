"""Fælles grundlag for turforslag: stedlisten, ruter mellem stop, hentning og JSON-output.

Del af tools/trip.py; kør kommandoerne gennem den.
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request

from common import CATALOG, LAYER_MEMBERSHIP, LOCAL_MAX_MIN, ORIGIN, haversine_km, minutes


ORIGIN_NAME = "Casa de la Familia, Las Lagunas de Mijas"

UA = {"User-Agent": "CalleMilano-trip-planner/1.0"}


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
