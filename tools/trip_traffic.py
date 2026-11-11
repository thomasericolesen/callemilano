"""Trafik til turforslag (Bravo): aktive DGT-hændelser nær ruten fra Casa de la Familia.

Del af tools/trip.py; kør kommandoerne gennem den.
"""
from __future__ import annotations

import math
import xml.etree.ElementTree as ET

from common import ORIGIN, haversine_km
from trip_core import fetch, maps_dir_url, now_iso, out, pick_places


DGT_FEED = "https://nap.dgt.es/datex2/v3/dgt/SituationPublication/datex2_v37.xml"


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
