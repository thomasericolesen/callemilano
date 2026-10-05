# Change log

## 2026-10-05 — Google Maps intake list

- Added `data/maps-intake-projekt-spanien.csv`: the 212 places in the owner's "Projekt Spanien" Maps list, with triage coordinates and distance rings from Casa. Coordinates are approximate (the export has none); see `docs/data-dictionary.md`. Result: 13 places within 30 km, 25 at 30–60 km, 17 at 60–100 km, 138 beyond 100 km, 18 unplaced, plus the Casa address.

## 2026-10-05 — Local scope, tooling, and documentation consistency

Owner decision plus consistency fixes from the 2026-10-05 repository review. No place record, category, tag, enum or schema field was changed.

### Scope decision (owner)
- First phase limited to destinations within about 30 km of Casa de la Familia, confirmed by route-checked driving time. Primary audience: families with children who prefer short drives; secondary: adults, seniors, teenagers. Spain-wide records are kept as an archive. Recorded in `AGENTS.md`, `README.md` and `docs/project-state.md`.
- Origin coordinates fixed from the owner's Plus Code `8C8QG8PP+7W` = 36.5356875, -4.6626875.

### Tooling
- Added `tools/places.py` with `validate` (structural validation gate: YAML, schema version, required fields, enums, ID/slug/registry, duplicate SEO titles, approval gate; warnings for missing coordinates and unresolved driving times) and `catalog` (generates `data/place-catalog.csv` with distance from Casa and a within-30-km flag). Fact accuracy and evidence adequacy remain human checks.
- Generated `data/place-catalog.csv` for the first time.

### Files
- Created `data/image-rights.csv` (header only) and `images/` so the files named in `AGENTS.md` exist.
- Removed `demo 2/index.html`, a byte-identical duplicate of `demo/index.html`.
- Added `docs/data-dictionary.md` (all CSVs) and `docs/README.md` (documentation map).

### Documentation
- `README.md`: `Cities` → `City`; corrected the description of `data/` (registers and analytical datasets, not place records); added scope, folders and tooling.
- `AGENTS.md`: added scope and audience; stated that the recommendation datasets in `data/` are analytical, non-canonical inputs with their own tag vocabulary; stated that `docs/published/` pages are drafts outside the lifecycle; referenced the validator.
- `docs/project-state.md`: rewritten to reflect 30 records, the new scope, tooling, and current open issues.

### Not changed (needs editor-of-record decision)
- `energy_level: null` in six identity-unresolved drafts (schema allows no unknown value); questionable categories for Alcázar de Segovia, Mercado de Atarazanas and Baelo Claudia; mapping between schema tags and collection tags; revision of the recommendation engine for the local scope.

## 2026-10-03 — P0/P1 documentation remediation

Applied the P0 contract decisions and P1 operational design from `docs/remediation-plan.md`. This update changes project guidance and specifications; it does not implement executable validators, create registry/queue data files, migrate standalone examples, or publish place records.

### `AGENTS.md`

- Made `docs/places/` the sole canonical home for editable place records and specified Markdown with YAML front matter as their single source of truth. This resolves conflicting storage guidance and prevents editable duplicates.
- Defined roles for the ID registry, generated catalog, and image-rights register under `data/`, while retaining `images/` for image assets. This assigns canonical responsibilities to project folders.
- Reconciled category labels by making `City` canonical and replacing informal audience wording with the schema's exact age groups and separate suitability scores. This prevents enum drift.
- Added lifecycle and unknown-value rules, stable ID/slug rules, source evidence expectations, asset-rights policy, and named human editor-of-record authority. This aligns agent guidance with the review and approval process.
- Added a mandatory pre-approval validation checklist and review of volatile facts. This establishes a quality gate for future records.

### `docs/place-schema.md`

- Declared schema version `1.0.0` and the canonical Markdown/front-matter format. This gives records and agents a versioned contract.
- Added required `status` and documented lifecycle transitions, approval ownership, draft-only unresolved values, and publication blockers. This resolves the missing lifecycle and inconsistent completeness rules.
- Standardized category `City`, controlled audience labels, and family-score keys. This aligns the schema with project vocabulary.
- Specified registered stable IDs, unique slugs, redirects on slug changes, external identifiers, coordinate purpose, and a representative-point convention. This reduces ambiguity and collisions.
- Added autonomous community and country fields. This makes Spanish administrative geography complete and supports future regional expansion.
- Added typed official/booking/visitor/transport/contact links and structured visit information for schedules, durations, booking lead time, validity, and cost basis. This provides a home for useful, time-sensitive visitor data.
- Added structured accessibility dimensions and made `wheelchair_friendly` a derived summary. This avoids contradictory access fields and makes mobility/sensory information explicit.
- Expanded parking details and added structured non-car transport options. This supports accurate arrival planning.
- Defined qualitative per-person cost tiers, required cost basis and checked date, and separated incidental costs. This makes comparisons less ambiguous.
- Added stable image asset IDs, image roles, rights status, and centralized rights-register requirements. This separates rights lifecycle from place facts.
- Added claim-level evidence and review-issue structures, including source type, checked date, checker, confidence, severity, owner, and retryability. This makes verification traceable and handoffs actionable.
- Added related-place references and record creation/update/review dates plus human review decisions. This supports catalog relationships and content maintenance.
- Replaced the embedded Nerja data illustration with a clearly labeled draft example using the new schema, explicit unknowns, and an illustrative claim-level citation. This demonstrates status, evidence, and unknown-value handling without presenting unresolved details as verified.
- Clarified that files in `docs/examples/` are illustrations, not canonical place records. This prevents examples from being confused with approved content.
- Created the empty `docs/places/` output directory so the newly designated canonical record location exists for future drafts.

### `docs/maps-import-agent-spec.md`

- Aligned record output with `docs/places/` and front matter; defined the roles of the ID registry, generated catalog, import queue, and image-rights register. This makes intake and storage consistent.
- Added batch queue fields and states, duplicate detection, ID/slug reservation, ambiguity persistence, and resume behavior. This covers bulk imports and clarification loops.
- Required claim-level evidence, schema version, complete fields, source dates, route evidence, and explicit review issues. This makes drafts verifiable and schema-bound.
- Defined image asset rights handling, validation requirements, handoff report, retry/escalation rules, and explicit limits on agent authority. This makes import outputs safer to review and operate.

### `docs/multi-agent-workflow.md`

- Aligned all stages to the canonical record path, ID registry, generated catalog, and image-rights register. This removes conflicting data locations.
- Added batch queue lifecycle, per-item progress, duplicate checks, clarification pause/resume, and update-versus-create behavior. This supports scalable intake.
- Clarified each agent's responsibilities and handoff outputs; allowed independent factual checks to run in parallel while retaining risk-based fact-check and human-review gates. This reduces unnecessary serial delay without weakening review of consequential facts.
- Added single-file ownership and version-checked edits. This prevents concurrent agents from overwriting one another.
- Added a validation gate covering YAML, schema/version, enums, ID/slug uniqueness, evidence, links, duplicate identity/SEO, and image rights. Until an executable validator exists, the workflow requires a named reviewer to perform and record this check manually.
- Defined shared issue format, retry limit, escalation authority, approval sign-off, rework, corrections, archives, stale-data handling, image-rights withdrawal, and taxonomy/schema change control. This completes operational handoffs and assigns accountability.
- Clarified that approval is a human action and publication remains a separate process. This keeps agent work within the editorial boundary.

## Implementation notes

- The specifications name `data/place-id-registry.csv`, `data/import-queue.csv`, `data/place-catalog.csv`, and `data/image-rights.csv` as canonical operational files. Their headers, generated catalog process, and queue/registry tooling still need implementation before those workflows can run operationally.
- The workflow now defines a mandatory validator but does not add validator code. Until that exists, perform and record the stated validation checklist manually.
- Standalone files under `docs/examples/` were not migrated in this change. They remain examples only; copy none into `docs/places/` without converting it to schema version `1.0.0`, adding required fields, and resolving its review issues.
- No website, publication, deployment, or external service was changed.
