# CalleMilano project state

**Last updated:** 2026-10-03  
**Purpose:** Handoff for a future Codex session. Treat `AGENTS.md` and `docs/place-schema.md` as the primary project instructions and data contract.

## Project and current architecture

CalleMilano is a family travel guide to Andalusia and Spain. Google Maps saved places are discovery inputs; factual claims must be checked against official or otherwise appropriate sources.

- **Canonical place data:** Markdown files with YAML front matter in `docs/places/`. The front matter is the only editable structured source of truth.
- **Contract and operating guidance:** `AGENTS.md`, `docs/place-schema.md` (schema version 1.0.0), `docs/maps-import-agent-spec.md`, and `docs/multi-agent-workflow.md`.
- **Workflow:** Maps Import → Fact Check → Editorial → SEO → validation → human editor-of-record approval. Publication is a separate process; agents do not approve or publish.
- **Registries and queue:** `data/place-id-registry.csv` allocates stable IDs; `data/import-queue.csv` tracks per-place import work. `data/place-catalog.csv` is specified as a generated, read-only index but does not currently exist.
- **Media:** assets belong in `images/`; image rights are meant to be tracked in `data/image-rights.csv`, which does not currently exist.
- **Other project material:** `docs/examples/` contains illustrative examples, `prompts/` contains reusable prompts, and architecture/remediation/change/pilot review documents record design history.

The schema covers identity and geography, categories and tags, driving time from Casa de la Familia, audience and family suitability, energy and seasonality, access and facilities, cost and visit details, descriptions and SEO, images and rights, evidence, review issues, lifecycle, and maintenance dates.

## Completed work

- Created the project structure, README, and project guidance.
- Specified the place schema and a Nerja schema example; added examples for Marbella Club Hotel, La Herradura, and Caminito del Rey.
- Designed the Maps Import Agent and the four-stage multi-agent workflow. These are specifications, not implemented agents or automation.
- Completed an architecture review and remediation plan; applied the documented P0/P1 documentation remediation and recorded it in `docs/change-log.md`.
- Created five draft place records in `docs/places/`: Frigiliana, Ronda, Marbella Old Town, Selwo Aventura, and Zahara de la Sierra. All are `needs_fact_check`, and their intake items are assigned to fact check.
- Reviewed those five records in `docs/pilot-review.md`. No obvious hard schema or enum violations were found, but tag interpretation, evidence coverage, place scope, SEO conventions, and difficult-to-verify values need attention. This review did not independently re-verify destination facts.
- ID allocations and queue entries exist for the five drafts. The examples are illustrative only, not canonical records.

## Outstanding issues

### Workflow implementation

- No executable schema/YAML validator or automated catalog generator exists. Until implemented, the workflow requires a named person to perform and record the validation checklist manually.
- `data/place-catalog.csv` and `data/image-rights.csv` are referenced as operational files but are absent. The import queue and ID registry exist as CSVs; automation and lifecycle handling are not implemented.
- The five intake items and corresponding records remain at `needs_fact_check`; they are not approved or publishable.

### Schema and editorial rules

- Define record scope for town-scale records: what the selected pin represents and whether amenities/tags apply to the point, core experience, or wider municipality.
- Clarify `last_verified` semantics because partial source checks coexist with open fact-check issues. Consider per-field/source dates for volatile information.
- Establish criteria for duration, seasonality, and tags such as `Nature`, `Museum`, `Viewpoint`, and `Restaurant`. Duration tags currently lack `typical_duration` values in the pilot drafts.
- Define how age-group suitability differs from family ratings, and how energy differs from visit duration. Keep editorial judgments visibly distinct from sourced facts.
- Clarify town-level cost basis and rules for variable prices, driving-time source/method, representative coordinates, and the scope of accessibility/facility claims.
- Standardize SEO title and description conventions, including length/truncation guidance and family-focused wording.
- The pilot review identifies overlap between top-level `wheelchair_friendly` and detailed accessibility data; schema guidance says the summary is derived, but a precise mapping/validation rule remains to be established.
- Earlier remediation plan items beyond P0/P1 (including governance, correction intake, localization/style, and broader page/catalog design) may remain outstanding; consult `docs/remediation-plan.md` before expanding scope.

## Next recommended actions

1. **Set operating rules before scaling:** decide place scope/pin selection, tag and duration criteria, suitability and energy guidance, cost basis, verification dates, and SEO conventions. Update the schema/guidance together and record changes in `docs/change-log.md`.
2. **Fact-check the five pilot records:** confirm saved-place identity and representative pins, add claim-specific authoritative evidence, resolve driving routes and durations where possible, and retain unknowns with review issues where facts cannot be established. Keep the records in review statuses until complete.
3. **Build the minimum validation path:** implement a validator for YAML syntax, required fields/types/enums, IDs/slugs and registry matching, evidence/issues, and lifecycle requirements; record validation outcomes. Generate the catalog from canonical records instead of editing it by hand.
4. **Establish media-rights tracking before adding publishable images:** create and maintain the specified rights register; only use approved assets with complete metadata and contextual alt text.
5. **Then expand intake in batches:** deduplicate each input, reserve IDs, create drafts, track queue states and blockers, and validate each draft. A larger import can proceed as draft work, but do not treat volume as approval or publication readiness.

## Resume checklist

At the start of the next session, read `AGENTS.md`, `docs/place-schema.md`, `docs/project-state.md`, and the relevant current review/workflow documents. Check repository state and the five place records before editing. Do not assume the destination facts in the pilot records have been independently verified; do not mark records approved or published without the documented validation and human review.
