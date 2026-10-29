# Change log

## 2026-10-29 - Rule for local_30km: Google driving time, whole layer (no schema change)

Owner decision 2026-10-29: membership of `local_30km` is decided by a one-way driving time of at most 30 minutes, taken as Google Maps' main figure, not by straight-line distance. The rule applies to the whole layer, not only to beaches. This supersedes the "Layer boundary rule" bullet in the entry "2026-10-15 - Layer-boundary decision and post-fact-check corrections" (straight-line placement).

Measurement method (beaches): measured by the owner in Google Maps on Saturday 2026-07-18 at 10:00, one sample, from Calle Milano 35, 29649 Las Lagunas de Mijas (36.5356, -4.6627) to Google's marker for the destination (Cabopino: the parking point). Google's main figure is stored in `driving_time_from_casa_de_la_familia.duration`; the typical range, the owner's own figure where given, and the method are stored in its note.

- Rio Real was removed (draft; it does not become a record). 13 beach drafts exist in `docs/places/` (status `draft`, local, not pushed).
- Google main figures (min): Cabopino 20, Los Monteros 28, La Butibamba 16, Castillo-Ejido 12, Fuengirola centrum 18, Boliches-Gaviotas 16, Carvajal 20, Santa Ana 28, Fuente de la Salud 30, La Carihuela 30, El Bajondillo 28, Playamar 28, Los Alamos 30. All 13 are measured and within the limit. Fuente de la Salud, La Carihuela and Los Alamos sit exactly on it and stay in the layer. Los Alamos is measured (30 min).
- Moved out of `local_30km` by the new rule: Malaga (36 min), Marbella old town (34 min, `data/route-checks-2026-10-16.csv`) and Tolox (56 min). Owner decision: they return to `excursions_4h`, where they were before 2026-10-15. This entry does not itself edit `data/layer-membership.csv`.
- Not changed by this entry: `AGENTS.md` line 9, `data/layers.csv`, `data/layer-membership.csv`, schema, categories, tags, enums.
- Open: update `AGENTS.md` line 9 and the `local_30km` rule text in `data/layers.csv` to the new rule; apply the layer moves in `data/layer-membership.csv`; the beach measurement is one summer-Saturday sample.
- Local only. Not pushed or merged.

## 2026-10-16 — Senior itineraries (draft package; additive, no schema change)

Owner request: day trips and overnight routes for fit seniors (about 60–75), from Casa de la Familia as far as the Portuguese border. **Draft; not editor-approved.**

- Added `docs/senior-itineraries.md` (scope, fact-check ledger, open decisions), `data/senior-itineraries.csv` (14 itineraries referencing existing record IDs) and `data/route-checks-2026-10-16.csv` (12 new OSRM route checks with approximate destination coordinates).
- Not changed: place records, `AGENTS.md`, `data/layers.csv`, `data/layer-membership.csv`, schema, categories, tags, enums.
- Owner decisions the same day: the time limit is extended to about 5 h one-way, added as layer `excursions_5h` in `data/layers.csv` (`excursions_4h` unchanged); Portuguese places are out of scope for now (Vila Real de Santo António and Tavira removed from the itineraries, route checks kept and marked out of scope). `AGENTS.md` got a matching bullet.
- Open editor decisions: creation of draft records for the places that have none (Mijas Pueblo, Casares, Arcos de la Frontera, Grazalema, El Rocío, Ayamonte); whether seniors become a named audience of the excursion layers.
- Merge target named by the owner: `christiano-ez/callemilano`. Not merged.

## 2026-10-15 — New controlled tag: Overnight

Editor-approved schema change: added `Overnight` to the controlled tag vocabulary in `docs/place-schema.md`, `AGENTS.md`, and `tools/places.py`'s `TAGS` set. `Overnight` replaces `Full day` for a destination whose realistic one-way drive time makes a day trip impractical (e.g. Sevilla, Córdoba in the excursion layer); a record uses one or the other, never both.

## 2026-10-15 — Non-Spain territory code in the place ID format

Editor-approved schema change: `docs/place-schema.md`'s `id` format now documents the leading segment as the place's own country/territory code (`ES` for Spain, or another appropriate code — e.g. `GI` for Gibraltar, a British Overseas Territory — for a place outside Spain), with a shorter `{TERRITORY}-{PLACE}-{NNN}` form for a territory without Spain's region/province structure.

Gibraltar's ID is corrected from the borrowed `ES-AND-CAD-GIBRALTAR-001` to `GI-GIBRALTAR-001`. The old ID is retired (not deleted) in `data/place-id-registry.csv`; the new ID is allocated under a new `GI` namespace. Updated: `docs/places/gibraltar.md` (`id` field, `not_spain` review issue resolved), `data/place-id-registry.csv`, `data/layer-membership.csv`. No other record's ID changes — this correction was made before the record left draft/review status, per the stable-ID rule (never change an ID after `approved`).

## 2026-10-15 — Layer-boundary decision and post-fact-check corrections

Editor-of-record decisions following fact-check of the 17 excursion-layer records:

- *Superseded 2026-10-29, see the "Rule for local_30km" entry above.* **Layer boundary rule:** for records whose route-checked driving time was now known, the editor decided layer placement (`local_30km` vs `excursions_4h`) by straight-line km distance rather than driving time, since driving time varies with traffic/route. Málaga (29.9 km, `malaga.md`) and Tolox (27.7 km, `tolox.md`) fall within the 30 km primary radius and were moved from `excursions_4h` to `local_30km` in `data/layer-membership.csv`; their `layer_boundary_open` and `excursion_layer_scope` review issues were resolved and removed.
- **Gibraltar border treaty confirmed:** the previously secondary-sourced claim that routine checks were removed at the Gibraltar-Spain land frontier is now confirmed directly from an official Government of Gibraltar press release (15 July 2026, frontier gates/barrier removed). `gibraltar.md`'s `border_treaty_unconfirmed` blocking issue is resolved; a narrower, non-blocking issue remains for downstream mechanics (exact Schengen/customs handling, current queue conditions) that are still only secondary-sourced. Status advanced to `needs_editorial_review`.
- **Jerez bodega-tasting age policy:** editor decision — no venue-specific minimum age needs chasing beyond Spain's standard legal drinking age (18), which governs the tasting regardless of how the tour is marketed. `jerez-de-la-frontera.md`'s `alcohol_age_policy_unknown` blocking issue is resolved and removed.

## 2026-10-15 — Young adults migration

Editor-approved schema change: age groups `Teenagers (13-17)` and `Adults` merged into `Young adults`; `family_score` keys `teenagers` and `adults` merged into `young_adults` (rule: max; `unknown` if either input is unknown). Updated: all `docs/places/*.md`, `tools/places.py` constants, `data/personas.csv` (weights summed), `AGENTS.md`, `docs/place-schema.md`. Analytical datasets and the engine spec were not migrated by this commit; see `docs/schema-change-proposal-young-adults.md` and issue #5 for the follow-up below, which completes that work.

## 2026-10-16 — Young adults migration: analytical datasets and recommendation engine (closes #5)

Completes the follow-up issue #5 raised by the schema migration above. Two PRs, in order:

- **`data/destination-metadata.csv`**: merged `teen_score`/`adult_score` into a single `young_adult_score` column, same max rule as the schema migration. **`docs/recommendation-engine-spec.md`**: `base_score` formula and factor list updated to use `young_adult_score`/`young_adult_suitability_weight` (this also fixed a real bug — the spec still referenced `teen_suitability_weight`/`adult_suitability_weight`, which `personas.csv` no longer had since the original migration already merged them). **`docs/data-dictionary.md`** and **`docs/guest-questionnaire-spec.md`**: column references updated to match. **`docs/examples/*.md`** (4 files): illustrative `age_groups`/`family_score` examples updated to `Young adults`, merged with the same max rule, so they don't teach the deprecated taxonomy.
- **`docs/end-to-end-demo.md`**: all 10 worked guest-session scenarios recomputed against the current formula and data (a throwaway script implementing the spec exactly); 7 of 10 changed ranking or top-5 membership, since several destinations had `teen_score` ≠ `adult_score` pre-merge. A genuine exact tie in scenario 5 (aviation enthusiast) is broken alphabetically and noted in the document, since the engine spec defines no tie-break rule. **`docs/group-composition-v2.md`**: this document's party-composition formula weights age-suitability terms by headcount rather than selecting a persona-level score, so the main migration's max-rule approach didn't directly transfer; teenager and adult headcounts now combine into one `(teenagers + adults) × young_adult_score` term, and all 4 worked examples were recomputed. This collapses `party_suitability` to exactly `young_adult_score` for an all-adult/teenager party (Example 2), which is flagged explicitly in the document as a real behavior change, not just a rename.

Deliberately **not** migrated, per editor review (see issue #5 and the original proposal): `data/demo-groups.csv` (headcounts describing a synthetic test group's composition, not suitability scores — merging would lose information), `docs/gold-standard-sample-set.md` (uses "teen"/"adult" as ordinary English in editorial prose, not as schema field references), `docs/discrimination-analysis.md` (a historical analysis snapshot of the old data, not a live spec). `README.md` and `demo/index.html` were checked and already carried no stale references.

`python3 tools/places.py validate` unaffected both times (same 6 pre-existing errors in unrelated archive records).

## 2026-10-15 — Excursion layer (additive; no schema change)

Owner decision: add a second layer, `excursions_4h` (route-checked one-way drive up to about 4 h), beside the 30 km primary area.

- Added 17 draft records in `docs/places/` (Málaga, Sierra de las Nieves, Tolox, Caminito del Rey, Setenil de las Bodegas, Antequera, El Torcal de Antequera, Nerja, Tarifa, Vejer de la Frontera, Granada, Sevilla, Córdoba, Cádiz, Jerez de la Frontera, Gibraltar, Las Alpujarras). All `draft`, no coordinates, no route-checked driving time, no sourced facts; blocking review issues on each.
- Reserved the 17 IDs in `data/place-id-registry.csv` and added 17 rows to `data/import-queue.csv`.
- Added `data/layers.csv` and `data/layer-membership.csv`.
- Added persona `Young adults` to `data/personas.csv` (weights are editorial estimates).
- Added the scope section to `AGENTS.md` and a bullet to `README.md`; added `docs/excursions-layer.md` and `docs/excursions-layer-overlap.md`.
- Not changed: existing place records, categories, tags, enums, schema. The merge of `Teenagers (13-17)` and `Adults` into `Young adults` is a separate proposal: `docs/schema-change-proposal-young-adults.md`.

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
