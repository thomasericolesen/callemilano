# Schema change proposal: merge `Teenagers (13-17)` and `Adults` into `Young adults`

**Requested by:** owner, 2026-10-15. **Status:** proposal; needs approval by the editor-of-record (AGENTS.md). Not applied by the layer package.

## Change

| Item | Now | Proposed |
|---|---|---|
| `age_groups` values | `Small children (0-6)`, `Children (7-12)`, `Teenagers (13-17)`, `Adults`, `Seniors` | `Small children (0-6)`, `Children (7-12)`, `Young adults`, `Seniors` |
| `family_score` keys | `small_children`, `children`, `teenagers`, `adults`, `seniors` | `small_children`, `children`, `young_adults`, `seniors` |
| Persona weights | `teen_suitability_weight`, `adult_suitability_weight` | `young_adult_suitability_weight` (sum of the two) |

## Decisions the editor must make

1. **Label and boundary.** `Young adults` without an age range in the label. Owner decision 2026-10-15: adults are 18+, teenagers remain 13-17, so the merged group covers 13 and up; the schema text must say this.
2. **Adults.** The merge removes the separate `Adults` group (18+); older adults are covered only by the merged group and `Seniors`.
3. **Merge rule for `family_score`.** Owner decision 2026-10-15: `max` (the higher of teenagers and adults); `unknown` if either is unknown. The script defaults to `max`; `--rule min` exists for comparison.
4. **Persona names** such as `Family with teenagers` and the demo groups keep their wording; they describe family compositions, not schema values. Check they still make sense.

## What the migration script changes

`tools/migrate_young_adults.py` (dry run by default; idempotent):

- `docs/places/*.md`: `age_groups` and `family_score` blocks.
- `tools/places.py`: `AGE_GROUPS`, `FAMILY_KEYS`.
- `data/personas.csv`: the two weight columns become one.
- `AGENTS.md`, `docs/place-schema.md`: enum lists and the schema example.
- `docs/change-log.md`: entry.

## What it does not change (manual review)

The script ends by printing every other file that still mentions the old groups. Known: `data/demo-groups.csv`, `data/destination-metadata.csv` (`teen_score`, `adult_score`), `docs/recommendation-engine-spec.md`, `docs/end-to-end-demo.md`, `docs/discrimination-analysis.md`, `docs/gold-standard-sample-set.md`, `README.md`, the demo. The recommendation engine reads the analytical CSVs and must be updated together with them.

## Order of work

1. Approve this proposal (answer the four questions).
2. Run `python3 tools/migrate_young_adults.py`, read the dry-run output, then run with `--apply`.
3. Run `python3 tools/places.py validate` and `catalog`.
4. Update the manual-review files in a separate commit.
