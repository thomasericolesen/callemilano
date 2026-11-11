# Documentation map

Start with `../AGENTS.md`, then `project-state.md` and the newest `status-*.md`. Paths below are relative to `docs/`.

The top level of `docs/` holds the current rules and everything `AGENTS.md`, the agents, the skills and the tools point to. Subfolders hold supporting material; `history/` and `decisions/` record analyses and decisions that later documents or `AGENTS.md` supersede, so read them for context, not as current rules.

## Current status and rules (top level)
- `project-state.md` — what exists, what is open, what to do next
- `status-2026-11-12.md` — the newest status handover; when a new one is written, move the previous one to `history/`
- `change-log.md` — approved changes to guidance, schema and taxonomy
- `owner-decisions-2026-11-02.md` — owner decisions still cited by `AGENTS.md`
- `data-dictionary.md` — every CSV in `data/` explained
- `place-schema.md` — canonical schema 1.0.0 for `places/*.md`
- `knowledge-model.md` — verified facts vs. editorial advice vs. guest reports
- `editorial-rules.md`, `editorial-checklist.md`
- `multi-agent-workflow.md` (editor workflow, review intervals, import), `agent-pipeline.md`, `maps-import-agent-spec.md`
- `trip-planner-agents.md` — trip plans (Alpha, Charlie, Ecco and `tools/trip.py`)
- `senior-itineraries.md`
- `enriched-place-metadata.csv` — analytical dataset (not place records)

## Records and pages
- `places/` — canonical place records
- `published/` — hand-written gold-standard page drafts (not lifecycle-approved)
- `examples/` — illustrative examples only
- `archive/` — copies of app rows removed from the app

## `content/` — content production and import
- `destination-record-spec.md` — fuller five-part editorial record (target model; not yet implemented in the schema)
- `content-production-system.md`, `content-types.md`
- `gold-standard-destination.md`, `gold-standard-sample-set.md`
- `maps-import-workflow.md`, `google-maps-import-spec.md`, `import-batch-template.md`, `import-batch-01.md`
- `identity-clarification-report.md` — unresolved place identities

## `product/` — guests, app and launch
- `user-needs-analysis.md`, `user-journeys.md`, `schema-gap-analysis.md`, `executive-summary.md`
- `mvp-features.md`, `mvp-screen-spec.md`, `wireframes.md`
- `webapp-byggeplan.md`, `byggeplan-oplev.md`, `oplev-category-images-2026-11-08.json`, `vurdering-familieadgang-turforslag.md`
- `beach-feedback-survey.md` — Facebook survey for first-hand family beach experience
- `launch-candidates.md`, `launch-backlog.md`, `pilot-content-plan.md`, `production-test.md`, `content-priority-list.md`

## `engine/` — recommendation engine
- `recommendation-engine-spec.md` — current V1 scoring formula
- `guest-questionnaire-spec.md` — V1 three-question flow
- `group-composition-v2.md` — V2 design (group composition)
- `metadata-roadmap.md` — which metadata to add next

Note: the engine documents were written for the original Spain-wide collection. They need revision for the 30-minute scope (drive-time bands, durations, personas); see `project-state.md`.

## `decisions/` — dated intake, selection and decision notes
Intake and selection rounds from 2026-11-01 to 2026-11-08 (`*-intake-*`, `*-selection-*`), owner approvals and family assessments (`approval-decisions-*`, `family-assessment-*`, `cost-level-proposals-*`), the fact-check list of 2026-11-08, the excursion-layer notes, the young-adults schema proposal and the season and practical-information drafts. Decisions that apply going forward are in `AGENTS.md` and `change-log.md`.

## `history/` — superseded analyses and old handovers
- Status and handovers before the newest: `status-2026-11-09` to `-11`, `status-rapport-*`, `handoff-*`, `codex-handover.md`
- Reviews: `architecture-review.md`, `remediation-plan.md` (P0/P1 applied 2026-10-03), `pilot-review.md`
- Engine analyses on the Spain-wide set: `recommendation-test-cases.md`, `end-to-end-demo.md`, `v1-vs-v2-comparison.md`, `v2-vs-v3-analysis.md`, `discrimination-analysis.md`, `destination-collections.md`
