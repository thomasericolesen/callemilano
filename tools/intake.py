#!/usr/bin/env python3
"""CalleMilano intake pipeline: deterministic steps, no AI judgement.

Subcommands (all JSON in / JSON out, so agents never need to read raw pages):

  sweep   IN.json OUT.json      Google Places identity + Routes drive time for named places.
          IN: [{"key": "...", "query": "...", "group": "..."}]
  nearby  IN.json OUT.json      Several candidates around a point (e.g. restaurants by a beach).
          IN: [{"key": "...", "lat": .., "lng": .., "queries": ["..."], "max_m": 1200}]
          Ratings/review counts are returned only for shortlisting; never copy them into records.
  fetch   IN.json OUTDIR        Fetch pages and save plain text (OUTDIR/<key>.txt). Free steps first:
          curl; PDFs via pdftotext; pages that need JavaScript via headless Chromium
          (tools/render_page.mjs, Playwright). IN: [{"key": "...", "url": "..."}]. Writes
          OUTDIR/_status.json with method and menu/carta/PDF links to follow; pages that still
          block (403/429/CAPTCHA/empty) are marked "needs_extract" (Tavily tavily_extract next); Facebook/Instagram pages are
          marked "login_wall" (use an owner screenshot instead).
  create  IN.json               Create draft records from sweep results + editorial fields.
          IN: [{"sweep": "sweep.json", "key": "...", "slug": "...", "name": "...",
                "category": "...", "municipality": "...", "what": "...", "energy": "Low",
                "tags": [], "purpose": "venue", "related_places": [], "layer": "excursions_4h",
                "catalogue_group": "Tæt på", "note": "..."}]
          Allocates IDs in data/place-id-registry.csv, adds layer membership when "layer" is set.
  apply   IN.json               Apply checked facts to existing records (the record-writer output).
          IN: [{"slug": "...", "status": "needs_fact_check", "set": {"field": value, ...},
                "evidence": [{...}], "resolve_issues": ["code"], "add_issues": [{...}]}]
          Refuses approved/published/archived records and statuses beyond needs_fact_check.
  checklist IN.json OUT.html --title T --heading H --lede L
          Build an owner checklist page (artifact with the db capability, collection "choices").
          IN: [{"key": "A", "da": "Group name", "items": [{"id", "name", "what", "drive",
                "note", "maps", "site"}]}]

Origin, departure time and route settings follow AGENTS.md. Google calls go through the
session proxy (header X-Goog-Api-Key: dummy). Run `python3 tools/places.py validate` and
`python3 tools/places.py catalog` after create/apply.
"""
from __future__ import annotations

import argparse
import copy
import csv
import datetime as dt
import html as htmlmod
import json
import math
import re
import shutil
import subprocess
import sys
import urllib.parse
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import LAYER_MEMBERSHIP as MEMBERSHIP, ORIGIN, ORIGIN_TEXT, PLACES, REGISTRY, ROOT  # noqa: E402,F401

TEMPLATES = Path(__file__).resolve().parent / "templates"
def _next_saturday():
    d = dt.date.today() + dt.timedelta(days=1)
    while d.weekday() != 5:
        d += dt.timedelta(days=1)
    return f"{d.isoformat()}T09:00:00Z"  # 10:00 Europe/Madrid in winter (11:00 in summer time)


DEPARTURE = _next_saturday()  # Routes API needs a future time; always the next Saturday
PLACE_MASK = ("places.id,places.displayName,places.formattedAddress,places.location,places.googleMapsUri,"
              "places.websiteUri,places.primaryType,places.businessStatus")
TODAY = dt.date.today().isoformat()
LOCKED = {"approved", "published", "archived"}
DUMP = dict(allow_unicode=True, sort_keys=False, width=100000)


def _post(url, body, mask):
    r = subprocess.run(["curl", "-sS", "-X", "POST", url, "-H", "Content-Type: application/json",
                        "-H", "X-Goog-Api-Key: dummy", "-H", f"X-Goog-FieldMask: {mask}",
                        "-d", json.dumps(body)], capture_output=True, text=True)
    return json.loads(r.stdout or "{}")


def _route(lat, lng):
    body = {"origin": {"location": {"latLng": {"latitude": ORIGIN[0], "longitude": ORIGIN[1]}}},
            "destination": {"location": {"latLng": {"latitude": lat, "longitude": lng}}},
            "travelMode": "DRIVE", "routingPreference": "TRAFFIC_AWARE_OPTIMAL", "departureTime": DEPARTURE}
    r = (_post("https://routes.googleapis.com/directions/v2:computeRoutes", body,
               "routes.duration,routes.distanceMeters").get("routes") or [{}])[0]
    if not r.get("duration"):
        return None, None
    return round(int(r["duration"][:-1]) / 60), round(r["distanceMeters"] / 1000, 1)


def _dist_m(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(b[1] - a[1]) / 2) ** 2
    return round(2 * 6371000 * math.asin(math.sqrt(h)))


def _place(p):
    return {"name": p["displayName"]["text"], "addr": p.get("formattedAddress"), "type": p.get("primaryType"),
            "status": p.get("businessStatus"), "maps": p["googleMapsUri"].split("&")[0],
            "web": p.get("websiteUri") or "", "lat": p["location"]["latitude"],
            "lng": p["location"]["longitude"], "place_id": p["id"]}


def cmd_sweep(inp, out):
    res = []
    for q in json.load(open(inp)):
        r = _post("https://places.googleapis.com/v1/places:searchText",
                  {"textQuery": q["query"], "languageCode": "es", "maxResultCount": 1,
                   "locationBias": {"circle": {"center": {"latitude": ORIGIN[0], "longitude": ORIGIN[1]},
                                               "radius": 50000}}}, PLACE_MASK)
        p = (r.get("places") or [None])[0]
        row = {**q, "found": bool(p)}
        if p:
            row.update(_place(p))
            row["drive_min"], row["drive_km"] = _route(row["lat"], row["lng"])
        res.append(row)
        print(f"{q['key']}: " + (f"{row['name']} | {row['drive_min']} min | {row['type']} {row['status']}"
                                 if p else "NOT FOUND"))
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)


def cmd_nearby(inp, out):
    mask = PLACE_MASK + ",places.rating,places.userRatingCount,places.priceLevel"
    res = {}
    for spec in json.load(open(inp)):
        c = (spec["lat"], spec["lng"]); seen = {}
        for q in spec["queries"]:
            r = _post("https://places.googleapis.com/v1/places:searchText",
                      {"textQuery": q, "languageCode": "es", "maxResultCount": 15,
                       "locationBias": {"circle": {"center": {"latitude": c[0], "longitude": c[1]}, "radius": 1000}}},
                      mask)
            for p in r.get("places", []):
                if p.get("businessStatus") != "OPERATIONAL":
                    continue
                row = _place(p)
                row["m"] = _dist_m(c, (row["lat"], row["lng"]))
                if row["m"] > spec.get("max_m", 1200):
                    continue
                row.update(rating=p.get("rating"), n=p.get("userRatingCount") or 0, price=p.get("priceLevel"))
                seen[row["place_id"]] = row
        res[spec["key"]] = sorted(seen.values(), key=lambda v: v["m"])
        print(f"{spec['key']}: {len(seen)} candidates")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)


def _text(raw):
    raw = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</(p|div|li|h\d|tr|section)>", "\n", raw)
    t = htmlmod.unescape(re.sub(r"<[^>]+>", " ", raw))
    lines = [re.sub(r"[ \t]+", " ", l).strip() for l in t.split("\n")]
    return "\n".join(l for l in lines if l)


MENU_LINK = re.compile(r"(?i)menu|men[uú]|carta|card|\.pdf")
RENDER = Path(__file__).with_name("render_page.mjs")


def _blocked(code, txt):
    return (str(code) != "200" or len(txt) < 300
            or bool(re.search(r"(?i)captcha|verify you are human|enable javascript|iniciar sesi[oó]n en facebook"
                              r"|log ?in(to| to) facebook", txt[:2000])))


LOGIN_WALL = re.compile(r"(?i)^https?://([a-z0-9-]+\.)?(facebook|instagram)\.com/")


def _curl(url, dest=None):
    args = ["curl", "-sSL", "-m", "30", "-A", "Mozilla/5.0 (CalleMilano fact check)",
            "-w", "\n%{http_code} %{content_type}", url]
    if dest:
        args[1:1] = ["-o", str(dest)]
    r = subprocess.run(args, capture_output=True, text=True, errors="ignore")
    body, _, tail = r.stdout.rpartition("\n")
    code, _, ctype = tail.partition(" ")
    return (body if not dest else ""), code, ctype


def _pdf_text(url, tmpdir):
    """Download a PDF and extract its text with pdftotext (poppler); '' if unavailable."""
    dest = Path(tmpdir) / "page.pdf"
    _, code, _ = _curl(url, dest)
    if code != "200" or not shutil.which("pdftotext"):
        return code, ""
    r = subprocess.run(["pdftotext", "-layout", str(dest), "-"], capture_output=True, text=True, errors="ignore")
    return code, "\n".join(l.rstrip() for l in r.stdout.split("\n") if l.strip())


def _render(url, timeout_ms=45000):
    """Render with headless Chromium via tools/render_page.mjs; None if Node/Playwright is missing."""
    if not shutil.which("node") or not RENDER.exists():
        return None
    try:
        r = subprocess.run(["node", str(RENDER), url, str(timeout_ms)], capture_output=True, text=True,
                           timeout=timeout_ms / 1000 + 30, errors="ignore")
        o = json.loads(r.stdout.strip().splitlines()[-1])
    except (subprocess.TimeoutExpired, json.JSONDecodeError, IndexError):
        return {"error": "render_failed"}
    return None if o.get("error") == "playwright_not_installed" else o


def _links(raw, base):
    out = []
    for href, label in re.findall(r'(?is)<a[^>]+href="([^"#][^"]*)"[^>]*>(.*?)</a>', raw):
        label = re.sub(r"<[^>]+>|\s+", " ", label).strip()[:80]
        if MENU_LINK.search(href + " " + label):
            out.append({"text": label, "href": urllib.parse.urljoin(base, htmlmod.unescape(href))})
    return out[:20]


def cmd_fetch(inp, outdir):
    """curl -> PDF text -> headless Chromium -> needs_extract (Tavily). Free steps first (owner, 2026-11-03)."""
    outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True); status = {}
    for it in json.load(open(inp)):
        url = it["url"]; method = "curl"; links = []
        if LOGIN_WALL.search(url):
            # Neither curl, Chromium nor Tavily gets past the login wall: use an owner screenshot.
            (outdir / f"{it['key']}.txt").write_text(f"URL: {url}\nFETCHED: {TODAY}\nMETHOD: none\n\n")
            status[it["key"]] = {"url": url, "http": None, "chars": 0, "method": "none",
                                 "result": "login_wall", "menu_links": []}
            print(f"{it['key']}: login_wall (owner screenshot needed)")
            continue
        if re.search(r"(?i)\.pdf(\?|$)", url):
            code, txt = _pdf_text(url, outdir); method = "pdf"
        else:
            body, code, ctype = _curl(url)
            if "pdf" in ctype.lower():
                code, txt = _pdf_text(url, outdir); method = "pdf"
            else:
                txt = _text(body) if code == "200" else ""
                links = _links(body, url) if code == "200" else []
                if _blocked(code, txt):
                    o = _render(url)
                    if o and not o.get("error"):
                        rtxt = o.get("text") or ""
                        if not _blocked(o.get("http"), rtxt) and len(rtxt) > len(txt):
                            code, txt, method = str(o.get("http")), rtxt, "playwright"
                        links = o.get("menu_links") or links
        blocked = _blocked(code, txt)
        (outdir / f"{it['key']}.txt").write_text(f"URL: {url}\nFETCHED: {TODAY}\nHTTP: {code}\nMETHOD: {method}\n\n{txt}")
        status[it["key"]] = {"url": url, "http": code, "chars": len(txt), "method": method,
                             "result": "needs_extract" if blocked else "ok",
                             "menu_links": [l for l in links if l["href"] != url][:10]}
        print(f"{it['key']}: {status[it['key']]['result']} ({method}, {code}, {len(txt)} chars, "
              f"{len(status[it['key']]['menu_links'])} menu links)")
    pdf = outdir / "page.pdf"
    if pdf.exists():
        pdf.unlink()
    json.dump(status, open(outdir / "_status.json", "w"), indent=1, ensure_ascii=False)


def _slug_ok(slug):
    return re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug)


def cmd_create(inp):
    tmpl = yaml.safe_load((TEMPLATES / "record-template.yaml").read_text())
    reg_text = REGISTRY.read_text(); reg = reg_text.rstrip("\n").split("\n")
    mem = MEMBERSHIP.read_text().rstrip("\n"); cache = {}
    for s in json.load(open(inp)):
        slug = s["slug"]
        assert _slug_ok(slug), f"bad slug {slug}"
        assert not (PLACES / f"{slug}.md").exists() and f",{slug}," not in reg_text, f"exists: {slug}"
        if s["sweep"] not in cache:
            cache[s["sweep"]] = {r["key"]: r for r in json.load(open(s["sweep"]))}
        o = cache[s["sweep"]][s["key"]]
        assert o.get("found"), f"not found in sweep: {s['key']}"
        if o.get("drive_min") is None:
            o["drive_min"], o["drive_km"] = _route(o["lat"], o["lng"])
        rid = f"ES-AND-MAL-{slug.upper()}-001"
        lat, lng, mins, km = o["lat"], o["lng"], o["drive_min"], o["drive_km"]
        dirurl = (f"https://www.google.com/maps/dir/?api=1&origin={ORIGIN[0]}%2C{ORIGIN[1]}"
                  f"&destination={lat}%2C{lng}&travelmode=driving")
        d = copy.deepcopy(tmpl)
        d.update(id=rid, slug=slug, name=s["name"], category=s["category"], tags=s.get("tags", []),
                 municipality=s["municipality"], google_maps_url=o["maps"],
                 external_ids={"google_place_id": o["place_id"]}, energy_level=s.get("energy", "Low"),
                 related_places=s.get("related_places", []), seasonality=s.get("seasonality", []),
                 created_at=TODAY, updated_at=TODAY)
        d["coordinates"] = {"latitude": lat, "longitude": lng, "purpose": s.get("purpose", "venue"),
                            "label": f"{o['name']}, {o['addr']} (Google Places listing)",
                            "source": f"Google Places API (New), place {o['place_id']}, read {TODAY}",
                            "checked_at": TODAY}
        d["driving_time_from_casa_de_la_familia"] = {
            "duration": f"{mins} min", "origin": ORIGIN_TEXT, "destination": f"{o['name']}, {o['addr']}",
            "source": (f"Google Routes API computeRoutes, run {TODAY} from the project origin ({ORIGIN[0]},{ORIGIN[1]}) "
                       f"to the Google Places coordinates ({lat},{lng}); departure {DEPARTURE} (next Saturday "
                       f"morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - {dirurl}"),
            "checked_at": TODAY, "note": f"Routes API figure: {mins} min, {km} km. One predicted sample."}
        d["links"]["official_website"] = o.get("web") or None
        what = s.get("what", "")
        d["description_short"] = f"{s['name']}: {what}, about {mins} min by car from Casa de la Familia. Draft; facts not yet checked."
        d["description_long"] = (f"{s['name']} is {what}. About {mins} minutes by car from Casa de la Familia "
                                 f"(Google route check, Saturday 10:00). Other facts have not been checked yet.")
        d["seo_title"] = f"{s['name']}, {s['municipality']} | CalleMilano draft record"
        d["seo_description"] = f"Draft record for {s['name']} ({s['municipality']}): location and driving time from Casa de la Familia."
        by = s.get("checked_by", "Claude (intake pipeline)")
        d["evidence"] = [
            {"field": "name, coordinates, google_maps_url, external_ids, municipality",
             "claim": f"Google Places lists '{o['name']}' at {o['addr']} ({lat},{lng}), status {o['status']}, type {o['type']}.",
             "source_url": o["maps"], "source_type": "maps_identity", "checked_at": TODAY, "checked_by": by,
             "confidence": "medium", "notes": "Google Places API (New). Identity and position only." + (f" {s['note']}" if s.get("note") else "")},
            {"field": "driving_time_from_casa_de_la_familia",
             "claim": f"From Casa de la Familia: {mins} min by car ({km} km, Saturday 10:00 predicted traffic).",
             "source_url": dirurl, "source_type": "secondary", "checked_at": TODAY, "checked_by": by,
             "confidence": "medium", "notes": "Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL."}]
        d["review_issues"] = [
            {"code": "facts_not_checked", "severity": "warning",
             "fields": ["description_long", "visit_information", "cost_level", "accessibility", "parking"],
             "description": "Created from Google Places identity and a route check only; needs official or own sources.",
             "retryable": True, "owner": "fact_check"},
            {"code": "family_suitability_not_assessed", "severity": "warning",
             "fields": ["age_groups", "family_score", "energy_level", "tags"],
             "description": "Age groups, family scores and tags are not assessed; energy_level is an editorial estimate.",
             "retryable": True, "owner": "human_editor"}]
        (PLACES / f"{slug}.md").write_text("---\n" + yaml.safe_dump(d, **DUMP) + "---\n")
        reg.append(f"ES-AND-MAL,{rid},{slug},{s['name']},allocated,{TODAY}")
        if s.get("layer"):
            mem += (f"\n{slug},{rid},{s['layer']},{s.get('catalogue_group', '')},route_checked_{TODAY},"
                    f"{s.get('membership_note', 'Owner selection ' + TODAY)}")
        print(f"created {slug} ({mins} min)")
    REGISTRY.write_text("\n".join(reg) + "\n"); MEMBERSHIP.write_text(mem + "\n")


def cmd_apply(inp):
    for u in json.load(open(inp)):
        p = PLACES / f"{u['slug']}.md"
        _, fm, body = p.read_text().split("---\n", 2); d = yaml.safe_load(fm)
        if d["status"] in LOCKED:
            print(f"SKIP {u['slug']}: status {d['status']} is locked (owner only)"); continue
        st = u.get("status")
        if st and st not in ("draft", "needs_fact_check"):
            print(f"SKIP {u['slug']}: agents may not set status {st}"); continue
        for k, v in (u.get("set") or {}).items():
            node = d; parts = k.split(".")
            for part in parts[:-1]:
                node = node.setdefault(part, {})
            node[parts[-1]] = v
        for e in u.get("evidence", []):
            e.setdefault("checked_at", TODAY)
            missing = {"field", "claim", "source_url", "source_type", "checked_at", "checked_by", "confidence"} - set(e)
            assert not missing, f"{u['slug']}: evidence missing {missing}"
            d["evidence"].append(e)
        rm = set(u.get("resolve_issues", []))
        d["review_issues"] = [i for i in d["review_issues"] if i.get("code") not in rm] + u.get("add_issues", [])
        if st:
            d["status"] = st
        d["updated_at"] = TODAY
        p.write_text("---\n" + yaml.safe_dump(d, **DUMP) + "---\n" + body)
        print(f"applied {u['slug']} -> {d['status']}")


def cmd_checklist(inp, out, title, heading, lede):
    h = (TEMPLATES / "checklist.html").read_text()
    groups = json.load(open(inp))
    ids = [i["id"] for g in groups for i in g["items"]]
    assert len(ids) == len(set(ids)), "duplicate item ids"
    names = [i["name"] for g in groups for i in g["items"]]
    dup = {n for n in names if names.count(n) > 1}
    if dup:
        print(f"WARNING duplicate names: {sorted(dup)}")
    esc = lambda s: htmlmod.escape(s, quote=False)
    h = (h.replace("{{TITLE}}", esc(title)).replace("{{HEADING}}", esc(heading)).replace("{{LEDE}}", esc(lede))
          .replace("{{GROUPS}}", json.dumps(groups, ensure_ascii=False).replace("</", "<\\/")))
    Path(out).write_text(h)
    print(f"wrote {out} ({len(ids)} items)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    for name, args in (("sweep", ["inp", "out"]), ("nearby", ["inp", "out"]), ("fetch", ["inp", "outdir"]),
                       ("create", ["inp"]), ("apply", ["inp"])):
        s = sp.add_parser(name)
        for a in args:
            s.add_argument(a)
    c = sp.add_parser("checklist")
    for a in ("inp", "out"):
        c.add_argument(a)
    c.add_argument("--title", required=True); c.add_argument("--heading", required=True); c.add_argument("--lede", required=True)
    a = ap.parse_args()
    if a.cmd == "sweep": cmd_sweep(a.inp, a.out)
    elif a.cmd == "nearby": cmd_nearby(a.inp, a.out)
    elif a.cmd == "fetch": cmd_fetch(a.inp, a.outdir)
    elif a.cmd == "create": cmd_create(a.inp)
    elif a.cmd == "apply": cmd_apply(a.inp)
    elif a.cmd == "checklist": cmd_checklist(a.inp, a.out, a.title, a.heading, a.lede)


if __name__ == "__main__":
    main()
