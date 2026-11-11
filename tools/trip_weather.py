"""Vejr til turforslag (Bravo): MET Norway først, Open-Meteo som reserve, og vejrråd.

Del af tools/trip.py; kør kommandoerne gennem den.
"""
from __future__ import annotations

import datetime as dt
import json
import urllib.parse
import urllib.request

from trip_core import fetch, now_iso, out, pick_places


OPEN_METEO = "https://api.open-meteo.com/v1/forecast"

WMO_DA = {
    0: "klart", 1: "overvejende klart", 2: "delvis skyet", 3: "overskyet", 45: "tåge", 48: "rimtåge",
    51: "let støvregn", 53: "støvregn", 55: "kraftig støvregn", 61: "let regn", 63: "regn",
    65: "kraftig regn", 66: "isslag", 67: "kraftigt isslag", 71: "let sne", 73: "sne", 75: "kraftig sne",
    77: "snekorn", 80: "lette byger", 81: "byger", 82: "kraftige byger", 85: "snebyger",
    86: "kraftige snebyger", 95: "torden", 96: "torden med hagl", 99: "kraftig torden med hagl",
}


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
