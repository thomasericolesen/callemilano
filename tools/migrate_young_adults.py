#!/usr/bin/env python3
"""Merge the audience groups `Teenagers (13-17)` and `Adults` into `Young adults`.

Schema-change migration. Run ONLY after the editor-of-record has approved
docs/schema-change-proposal-young-adults.md.

Default is a dry run. Use --apply to write. Idempotent: running it twice changes nothing.

Touches: docs/places/*.md, tools/places.py, data/personas.csv, AGENTS.md,
docs/place-schema.md, docs/change-log.md.
Does NOT touch (printed as a manual-review list): analytical CSVs, engine spec, demos.

family_score merge rule (--rule): `max` (default, owner decision 2026-10-15) takes the higher of
teenagers/adults (`min` available); if either is `unknown` the result is `unknown`.
"""
import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

ORDER = {"low": 0, "medium": 1, "high": 2}
MARK = "Young adults migration"
SKIP = {"./tools/migrate_young_adults.py", "./docs/schema-change-proposal-young-adults.md", "./docs/change-log.md"}


def merge_score(t, a, rule):
    if t not in ORDER or a not in ORDER:
        return "unknown"
    pick = min if rule == "min" else max
    return pick((t, a), key=lambda v: ORDER[v])


def migrate_record(text, rule):
    lines = text.split("\n")
    out, i, changed = [], 0, False
    while i < len(lines):
        line = lines[i]
        if line.rstrip() == "age_groups:":
            j = i + 1
            items = []
            while j < len(lines) and lines[j].startswith("  - "):
                items.append(lines[j][4:].strip())
                j += 1
            if "Teenagers (13-17)" in items or "Adults" in items:
                new, placed = [], False
                for it in items:
                    if it in ("Teenagers (13-17)", "Adults"):
                        if not placed:
                            new.append("Young adults")
                            placed = True
                    else:
                        new.append(it)
                out.append(line)
                out.extend(f"  - {it}" for it in new)
                changed = True
            else:
                out.extend(lines[i:j])
            i = j
            continue
        if line.rstrip() == "family_score:":
            j = i + 1
            block = []
            while j < len(lines) and re.match(r"^  \w+:", lines[j]):
                block.append(lines[j])
                j += 1
            kv = {}
            for b in block:
                k, v = b.strip().split(":", 1)
                kv[k] = v.strip()
            if "teenagers" in kv or "adults" in kv:
                merged = merge_score(kv.get("teenagers"), kv.get("adults"), rule)
                out.append(line)
                done = False
                for b in block:
                    k = b.strip().split(":", 1)[0]
                    if k in ("teenagers", "adults"):
                        if not done:
                            out.append(f"  young_adults: {merged}")
                            done = True
                    else:
                        out.append(b)
                changed = True
            else:
                out.extend(lines[i:j])
            i = j
            continue
        out.append(line)
        i += 1
    return "\n".join(out), changed


def replace_exact(path, old, new, apply, report):
    text = path.read_text(encoding="utf-8")
    if new in text and old not in text:
        return
    if old not in text:
        report.append(f"MANUAL: expected text not found in {path}: {old[:60]!r}")
        return
    report.append(f"patch {path}")
    if apply:
        path.write_text(text.replace(old, new), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--rule", choices=["min", "max"], default="max")
    args = ap.parse_args()
    root = Path(args.repo)
    report = []

    for path in sorted((root / "docs/places").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        new, changed = migrate_record(text, args.rule)
        if changed and new != text:
            report.append(f"record {path.name}")
            if args.apply:
                path.write_text(new, encoding="utf-8")

    replace_exact(root / "tools/places.py",
                  '"Children (7-12)", "Teenagers (13-17)", "Adults", "Seniors"}',
                  '"Children (7-12)", "Young adults", "Seniors"}', args.apply, report)
    replace_exact(root / "tools/places.py",
                  '"children", "teenagers", "adults", "seniors"}',
                  '"children", "young_adults", "seniors"}', args.apply, report)
    replace_exact(root / "AGENTS.md", "`Teenagers (13-17)`, `Adults`, `Seniors`",
                  "`Young adults`, `Seniors`", args.apply, report)
    replace_exact(root / "docs/place-schema.md", "`Teenagers (13-17)`, `Adults`, `Seniors`",
                  "`Young adults`, `Seniors`", args.apply, report)
    replace_exact(root / "docs/place-schema.md", "`children`, `teenagers`, `adults`, `seniors`",
                  "`children`, `young_adults`, `seniors`", args.apply, report)
    replace_exact(root / "docs/place-schema.md", "has all five keys", "has all four keys", args.apply, report)
    replace_exact(root / "docs/place-schema.md", "  - Teenagers (13-17)\n  - Adults\n", "  - Young adults\n", args.apply, report)
    replace_exact(root / "docs/place-schema.md", "  teenagers: unknown\n  adults: unknown\n", "  young_adults: unknown\n", args.apply, report)

    pcsv = root / "data/personas.csv"
    with pcsv.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh))
    head = rows[0]
    if "teen_suitability_weight" in head:
        ti, ai = head.index("teen_suitability_weight"), head.index("adult_suitability_weight")
        report.append("patch data/personas.csv (teen + adult weights summed into young_adult_suitability_weight)")
        newrows = []
        for r in rows:
            if r is head:
                r = r[:]
                r[ti] = "young_adult_suitability_weight"
            else:
                r = r[:]
                r[ti] = str(int(r[ti]) + int(r[ai]))
            del r[ai]
            newrows.append(r)
        if args.apply:
            with pcsv.open("w", encoding="utf-8", newline="") as fh:
                csv.writer(fh, lineterminator="\n").writerows(newrows)

    cl = root / "docs/change-log.md"
    text = cl.read_text(encoding="utf-8")
    if MARK not in text:
        entry = (
            f"## 2026-10-15 — {MARK}\n\n"
            "Editor-approved schema change: age groups `Teenagers (13-17)` and `Adults` merged into `Young adults`; "
            "`family_score` keys `teenagers` and `adults` merged into `young_adults` "
            f"(rule: {args.rule}; `unknown` if either input is unknown). Updated: all `docs/places/*.md`, "
            "`tools/places.py` constants, `data/personas.csv` (weights summed), `AGENTS.md`, `docs/place-schema.md`. "
            "Analytical datasets and the engine spec are not migrated; see "
            "`docs/schema-change-proposal-young-adults.md`.\n\n"
        )
        report.append("change-log entry")
        if args.apply:
            cl.write_text(text.replace("# Change log\n\n", "# Change log\n\n" + entry, 1), encoding="utf-8")

    print("\n".join(report) or "nothing to do")
    print("\nManual review (still mention the old groups):")
    hits = subprocess.run(
        ["grep", "-rIlE", r"Teenagers \(13-17\)|teen_|adult_score|adult_suitability|,teenagers,|^ *teenagers:|^ *adults:", "--exclude-dir=.git", "."],
        cwd=root, capture_output=True, text=True).stdout.split()
    for h in sorted(hits):
        if not h.startswith("./docs/places/") and h not in SKIP:
            print("  ", h)
    print("\n" + ("APPLIED" if args.apply else "DRY RUN — use --apply to write"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
