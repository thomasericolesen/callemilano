#!/usr/bin/env python3
"""Monthly freshness job for CalleMilano place records (owner decision 2026-11-11, "Freshness" in AGENTS.md).

Usage:
  python3 tools/freshness.py [--today YYYY-MM-DD] [--apply] [--json OUT.json]

Checks every record shown in the app (status needs_fact_check or later, see tools/app_export.py):
  - overdue:  next_review_at on or before today; with --apply, fact-checked records go back to
              needs_fact_check with a `review_overdue` warning (level A; the official sources are then
              read again and only conflicts go to the editor).
  - due soon: next_review_at within the next 30 days.
  - missing:  fact-checked records without next_review_at.
  - import token: days until the token for POST /api/import-places expires (renew before then; see
              docs/multi-agent-workflow.md).
No AI and no network. Exit code 0 always; read the report.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json

from common import CHECKED, PLACES, SHOWN, load_front_matter, read_record, write_record

TOKEN_EXPIRES = dt.date(2027, 2, 9)  # created 2026-11-11, 90 days; update when the token is renewed
TOKEN_WARN_DAYS = 30


def as_date(v) -> dt.date | None:
    if v in (None, ""):
        return None
    if isinstance(v, dt.date):
        return v
    return dt.date.fromisoformat(str(v)[:10])


def scan(today: dt.date) -> dict:
    out = {"today": today.isoformat(), "overdue": [], "due_soon": [], "missing": []}
    for p in sorted(PLACES.glob("*.md")):
        d = load_front_matter(p)
        if d.get("status") not in SHOWN:
            continue
        nr = as_date(d.get("next_review_at"))
        row = {"slug": d["slug"], "status": d["status"], "next_review_at": nr.isoformat() if nr else None}
        if nr is None:
            if d["status"] in CHECKED:
                out["missing"].append(row)
        elif nr <= today:
            out["overdue"].append(row)
        elif nr <= today + dt.timedelta(days=30):
            out["due_soon"].append(row)
    days = (TOKEN_EXPIRES - today).days
    out["import_token"] = {"expires": TOKEN_EXPIRES.isoformat(), "days_left": days, "renew_now": days <= TOKEN_WARN_DAYS}
    return out


def set_back(slug: str, today: dt.date) -> bool:
    p = PLACES / f"{slug}.md"
    d, body = read_record(p)
    if d.get("status") not in CHECKED:
        return False
    d["status"] = "needs_fact_check"
    issues = [i for i in d.get("review_issues") or [] if i.get("code") != "review_overdue"]
    issues.append({
        "code": "review_overdue", "severity": "warning", "owner": "fact_check",
        "fields": ["visit_information", "cost_level", "booking_required"], "retryable": True,
        "description": f"next_review_at {d.get('next_review_at')} passed; set back by tools/freshness.py on {today}. "
                       "Read the official sources again, then lift to needs_editorial_review and set a new next_review_at.",
    })
    d["review_issues"] = issues
    d["updated_at"] = today.isoformat()
    write_record(p, d, body)
    return True


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--today", type=dt.date.fromisoformat, default=dt.date.today())
    ap.add_argument("--apply", action="store_true", help="set overdue fact-checked records back to needs_fact_check")
    ap.add_argument("--json", help="write the report as JSON to this path")
    a = ap.parse_args(argv)
    r = scan(a.today)
    if a.apply:
        r["set_back"] = [x["slug"] for x in r["overdue"] if set_back(x["slug"], a.today)]
    t = r["import_token"]
    print(f"freshness {r['today']}: {len(r['overdue'])} overdue, {len(r['due_soon'])} due within 30 days, "
          f"{len(r['missing'])} fact-checked without next_review_at")
    for k in ("overdue", "due_soon", "missing"):
        if r[k]:
            print(f"  {k}: " + ", ".join(f"{x['slug']} ({x['next_review_at']})" for x in r[k]))
    if a.apply:
        print(f"  set back to needs_fact_check: {len(r['set_back'])}")
    print(f"import token expires {t['expires']} ({t['days_left']} days)" + (" - RENEW NOW" if t["renew_now"] else ""))
    if a.json:
        json.dump(r, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
