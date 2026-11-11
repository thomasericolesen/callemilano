"""Shared helpers for the CalleMilano tools: project paths, the origin point, record reading and drive times.

Import from here instead of redefining these in each tool, so a fix lands everywhere at once.
"""
from __future__ import annotations

import math
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PLACES = ROOT / "docs" / "places"
REGISTRY = ROOT / "data" / "place-id-registry.csv"
CATALOG = ROOT / "data" / "place-catalog.csv"
LAYER_MEMBERSHIP = ROOT / "data" / "layer-membership.csv"

# Casa de la Familia, Urb. Cerros del Águila, 29649 Las Lagunas de Mijas.
# Plus Code 8C8QG8PP+7W (centre of the ~14 m code area), supplied by the owner 2026-10-05; see AGENTS.md.
CASA_LAT, CASA_LON = 36.5356875, -4.6626875
ORIGIN = (CASA_LAT, CASA_LON)
ORIGIN_TEXT = "Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain"

# Primary area: route-checked one-way drive of at most 30 minutes (owner decision 2026-10-29).
LOCAL_MAX_MIN = 30


def haversine_km(lat1, lon1, lat2, lon2):
    r = 6371.0088
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def load_front_matter(path: Path) -> dict:
    """The YAML front matter of a place record, as a dict. Raises ValueError on a malformed file."""
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


_HOURS = re.compile(r"(\d+)\s*(?:h|hr|hrs|hour|hours|t)\b")
_MINS = re.compile(r"(\d+)\s*(?:m|min|mins|minute|minutes)\b")


def minutes(text) -> int | None:
    """Drive time text -> minutes. '22 min', '1 h 15 min', '2 hours 35 mins' -> 22, 75, 155; None if unparsable."""
    if not text:
        return None
    s = str(text).lower()
    h, m = _HOURS.search(s), _MINS.search(s)
    if not h and not m:
        return None
    return (int(h.group(1)) * 60 if h else 0) + (int(m.group(1)) if m else 0)
