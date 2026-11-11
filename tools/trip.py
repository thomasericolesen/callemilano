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
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from trip_core import cmd_nearby, cmd_places  # noqa: E402
from trip_weather import cmd_weather  # noqa: E402
from trip_traffic import cmd_traffic  # noqa: E402
from trip_restaurants import cmd_check_restaurants, cmd_coverage, cmd_restaurants  # noqa: E402
from trip_plan import cmd_hours_status, cmd_plan  # noqa: E402
from trip_render import cmd_render  # noqa: E402
# Ældre kode og tests importerer disse fra trip; de bor nu i modulerne ovenfor.
from trip_core import current_route_departure, load_places, route_minutes_between  # noqa: E402,F401


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
