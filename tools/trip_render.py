"""Ecco: gør trips/<id>/trip.json til turforslag.html (og PDF, hvis Playwright findes).

Del af tools/trip.py; kør kommandoerne gennem den.
"""
from __future__ import annotations

import html
import json
import re
import shutil
import subprocess
from pathlib import Path

from trip_core import ORIGIN_NAME


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
