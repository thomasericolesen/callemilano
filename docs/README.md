# Documentation map

Start with `../AGENTS.md`, then `project-state.md`. Files marked **(history)** record analyses or decisions that later documents supersede; read them for context, not as current rules.

## Current status
- `project-state.md` — what exists, what is open, what to do next
- `change-log.md` — approved changes to guidance, schema and taxonomy
- `data-dictionary.md` — every CSV in `data/` explained

## Data contract and records
- `place-schema.md` — canonical schema 1.0.0 for `places/*.md`
- `destination-record-spec.md` — fuller five-part editorial record (target model; not yet implemented in the schema)
- `knowledge-model.md` — verified facts vs. editorial advice vs. guest reports
- `places/` — canonical place records
- `published/` — hand-written gold-standard page drafts (not lifecycle-approved)
- `examples/` — illustrative examples only
- `identity-clarification-report.md` — unresolved place identities

## Workflow and production
- `multi-agent-workflow.md`, `maps-import-agent-spec.md`, `maps-import-workflow.md`, `google-maps-import-spec.md`
- `import-batch-template.md`, `import-batch-01.md`
- `content-production-system.md`, `content-types.md`, `editorial-rules.md`, `editorial-checklist.md`
- `gold-standard-destination.md`, `gold-standard-sample-set.md`

## Guests and product
- `user-needs-analysis.md`, `user-journeys.md`, `schema-gap-analysis.md`, `executive-summary.md`
- `mvp-features.md`, `mvp-screen-spec.md`, `wireframes.md`
- `beach-feedback-survey.md` — Facebook survey for first-hand family beach experience
- `launch-candidates.md`, `launch-backlog.md`, `pilot-content-plan.md`, `production-test.md`

## Recommendation engine
- `recommendation-engine-spec.md` — current V1 scoring formula
- `guest-questionnaire-spec.md` — V1 three-question flow
- `group-composition-v2.md` — V2 design (group composition)
- `metadata-roadmap.md` — which metadata to add next
- `recommendation-test-cases.md`, `end-to-end-demo.md` **(history)** — V1 outputs on the Spain-wide set
- `v1-vs-v2-comparison.md`, `v2-vs-v3-analysis.md`, `discrimination-analysis.md` **(history)**
- `destination-collections.md` **(history)** — owner-interest ranking of the original collection

## Reviews **(history)**
- `architecture-review.md`, `remediation-plan.md` (P0/P1 applied 2026-10-03), `pilot-review.md`

Note: the engine documents were written for the original Spain-wide collection. They need revision for the 30 km scope (drive-time bands, durations, personas); see `project-state.md`.
