# CalleMilano project guidance

## Purpose

CalleMilano is a family travel guide for guests at Casa de la Familia, starting with the nearby area and expanding later to Andalusia and Spain. Google Maps saved places are discovery inputs. Verify factual claims from appropriate sources before including them in editorial content.

## Scope and audience (owner decision 2026-10-05)

- **Primary area:** destinations within a one-way driving time of at most 30 minutes from Casa de la Familia, taken as Google Maps' main figure (owner decision 2026-10-29, superseding the earlier straight-line rule). Straight-line distance is not used for placement; places beyond 30 minutes belong to the excursion layers.
- **Origin coordinates:** Plus Code `8C8QG8PP+7W` = latitude 36.5356875, longitude -4.6626875 (WGS 84). Use these for distance calculations; `tools/places.py` holds the same constant.
- **Primary audience:** families with children who do not want long drives. **Secondary:** adults, seniors, and teenagers.
- **Places beyond the primary area** remain in `docs/places/` and the analytical datasets as an archive. Do not develop, fact-check, or recommend them in the current phase unless the editor-of-record says so. Do not delete them.
- Prioritize new intake, fact-checking, and recommendation testing inside the primary area.

## Excursion layer (owner decision 2026-10-15)

- A second layer, `excursions_4h`, is added beside the 30 km primary area: destinations reachable by a route-checked one-way drive of up to about 4 h (day trips and overnight stays). Layers are defined in `data/layers.csv`; membership is listed in `data/layer-membership.csv` (analytical, not a second source of truth for records).
- Target audience for this layer: young adults (nature and hiking, city life, culture and architecture, food, bars, cafés, wellness).
- This is the editor's instruction under the rule above that places beyond the primary area stay archive unless the editor says so: records in `excursions_4h` may be developed and fact-checked. Existing out-of-area records not listed in `data/layer-membership.csv` remain archive.
- Records in this layer follow the same schema, evidence and review rules. Driving time must still be route-checked, never estimated.
- Extension (owner decision 2026-10-16): layer `excursions_5h` covers route-checked one-way drives above about 4 h and up to about 5 h, for overnight routes. Portuguese places stay out of scope for now. Senior itineraries are in `docs/senior-itineraries.md`; see `docs/change-log.md`.
- Catalogue group `Tæt på` (owner decision 2026-11-02, decision 12 in `docs/owner-decisions-2026-11-02.md`): places in `excursions_4h` with a route-checked one-way drive of at most 60 minutes. Longer drives go in `Dagsture` or `Længere væk`.

## Beach selection rule: rocks (owner decision 2026-11-02)

- Exclude a beach that is purely a rock beach.
- Exclude a beach that can only be reached by climbing down over rocks.
- Rocks on a sand beach do not exclude it.

Check composition and access against official sources where available (see `docs/owner-decisions-2026-11-02.md`). This replaces the earlier working rule that any rocks excluded a beach.

## Approval rule (owner decision 2026-11-10)

- A place that has passed fact-check (`needs_editorial_review`) counts as approved for use in the app and in trip plans. The editor-of-record no longer signs off each record in advance. The formal `approved` status is no longer used as a step (owner decision 2026-11-11, see "Editor workflow").
- Approval after that is a running process driven by family feedback in the app: positive feedback can mark a place "Familien anbefaler" (green, the only green label); negative feedback (closed, wrong price, wrong hours) sends the record back to `needs_fact_check`.
- In the app, only places that are not fact-checked carry a warning label ("Ikke faktatjekket"). Statuses in the records are unchanged; only their meaning for display and trip plans changed. See `docs/change-log.md`.

## Editor workflow (owner decision 2026-11-11)

The editor-of-record sees only what needs editorial judgement or a formal decision; Claude does the rest and reports in `docs/change-log.md`. Full table and procedure: `docs/multi-agent-workflow.md`, section "Editor workflow".

- **Levels.** A: Claude alone (logged). B: Claude, editor informed in the weekly summary. C: the editor decides; the item goes on the editor list with Claude's recommendation and ready-made choices, and Claude changes nothing until answered. D: only the editor (category, taxonomy/schema, images and rights); never delegated, not even by a general permission. When in doubt, use the higher level.
- **Editor list.** At most once a week and only when there is something, one interactive list of all level C and D items (about 25 at most; the rest waits). Each item has: place, what to decide, why now, sources, Claude's recommendation (default), choices, note. Answers are stored in the list and written to the records as the editor's own judgement with date and link.
- **Claude decides alone (A):** hours, prices, contact and rules from official or own sources (quote, URL, date in the evidence ledger); driving times; `draft` → `needs_fact_check`; `needs_fact_check` → `needs_editorial_review` when there is official evidence for the core facts and no open blocking or `facts_not_checked` issue (the subagents still never set a status beyond `needs_fact_check`; the main session does the lift); back to `needs_fact_check` on negative app feedback or an overdue `next_review_at`; trip plans; catalogue, export, change-log and status file.
- **The editor decides (C):** source conflicts (price, hours, minimum age, access, safety; never closed in bulk); tags, family scores, energy and age groups (collected on a checklist; Claude writes only what the editor chose); accessibility, child safety and dog policy (official source or the editor's own knowledge, never a guess); new candidates; archiving.
- **Status `approved` is retired as a step.** `needs_editorial_review` is the end station for a fact-checked place and counts as approved for use; the app shows "Faktatjekket" for it. Existing `approved` records stay unchanged and are treated like `needs_editorial_review`. The editor's real approval of a place is his own review of tags and family ratings. No schema change.
- **Archiving.** If the facts for a place are too hard to obtain, it drops off the list; we already have enough places. Claude proposes archiving on the editor list (with what was tried) for drafts without a usable source after two attempts; archiving itself happens only after the editor says yes.
- **Issues.** `info` and `warning`: Claude closes them (a `warning` is retried twice, then closed as "not found", with the value left unknown and shown as "check before visiting"). `blocking` and all conflict issues go to the editor and are never closed in bulk to reach a status.
- **Push, PR, merge and import.** Standing permission for changes that consist only of level A/B work: Claude may push, open the PR (`gh`), merge and import into the app, and reports afterwards. Changes with level C/D content (archiving, categories, tags, conflicts, rules in this file) are merged only after the editor has answered. `main` changes only through a PR. After every import, check it: count of updated places, none skipped, a spot check of one place. The import runs without a browser login: `POST https://callemilano.dk/api/import-places` with the token in `~/.callemilano-import-token` (a dry run by default; `?apply=1` writes; see `docs/multi-agent-workflow.md`). The admin page `callemilano.dk/admin` stays as a fallback. The Facebook/Instagram and Google Maps checks still need Claude in Chrome open and signed in; GitHub work uses `gh`.
- **Freshness.** `next_review_at` follows volatility (hours, prices, access shorter than name and location); five months is the default for fact-checked places. Monthly, Claude sets overdue places back to `needs_fact_check` and reads the official sources again; only conflicts go to the editor.
- **Feedback from the app.** Negative feedback: Claude fixes it from a source and sets `needs_fact_check` until the correction is read from a source. Positive feedback may mark "Familien anbefaler"; no editor action. Feedback that disagrees with a source goes on the editor list.
- **Decisions.** Every editor decision gets a line in `docs/change-log.md` with date and source (list or chat); rules that apply going forward are also written here. No rule applies until it stands here; if something was only said in chat, Claude asks whether it should be written in.

## Language (owner decision 2026-11-11)

- Report to the editor-of-record in Danish: chat replies, reports, editor lists, weekly summaries, PR descriptions and status files.
- Code, file names, commands, schema values and the English texts in the records stay as they are.

## Agent pipeline (owner decision 2026-11-02)

Routine intake and fact-check work uses `tools/intake.py` and the subagents in `.claude/agents/` (`candidate-screener`, `source-reader`, `record-writer`) as described in `docs/agent-pipeline.md`. Subagents never approve, never change category/tags/family scores, and never set a status beyond `needs_fact_check`; the main session spot-checks their quotes before committing.

## Trip plans (owner decisions 2026-11-01 and 2026-11-02)

Trip plans work in two phases, described in `docs/trip-planner-agents.md`. Advance work (places, opening hours via Alpha, restaurants via Charlie) follows the pipeline rules above and ends in place records; restaurants are full place records and `data/restaurant-directory.csv` is only a lead list. The trip plan is `/turforslag`: `tools/trip.py plan` (weather, traffic, holidays and automatic checks; former agents Bravo and Delta) and the agent Ecco, who writes the Danish text and PDF. For between-stop Google Routes checks, use the current time as `departureTime`, not a standardized Saturday or the requested plan date (owner decision 2026-11-05). Trip working files and PDFs go to `trips/` and are not committed.

## Canonical project files

- Place records: `docs/places/` (canonical editable place data).
- Place schema and controlled vocabulary: `docs/place-schema.md`.
- Agent specifications and workflows: `docs/maps-import-agent-spec.md` and `docs/multi-agent-workflow.md`.
- Source/rights evidence for images: central asset-rights register at `data/image-rights.csv`.
- Place ID allocation: central ID register at `data/place-id-registry.csv`.
- Generated catalog index: `data/place-catalog.csv`; derive this from place records and never edit it as a second source of truth.
- Images: `images/`.

Do not store editable place records in `data/`; the Markdown files with YAML front matter in `docs/places/` are the only canonical record source.

The recommendation prototype datasets in `data/` (`personas.csv`, `demo-groups.csv`, `destination-*.csv`, `*-metadata.csv`) and `docs/enriched-place-metadata.csv` are analytical inputs, not place records. They contain editorial estimates and use a separate collection-tag vocabulary (`data/destination-tag-vocabulary.csv`) that is not interchangeable with the schema tags below. Never copy values from them into a place record as verified facts. Field definitions are in `docs/data-dictionary.md`.

Pages in `docs/published/` are hand-written gold-standard page drafts, not records produced through the lifecycle. They are not "published" in the schema sense until a matching record in `docs/places/` has passed validation and human approval.

Run `python3 tools/places.py validate` before handing a record to human review and `python3 tools/places.py catalog` after any record change.

## Categories and controlled labels

Every place has exactly one primary category: `Restaurants`, `Beaches`, `Excursions`, `Nature`, `City`, or `Family activities`. Use the exact enum spelling in `docs/place-schema.md`. Do not use `Cities` as a category.

Use only schema-controlled values for tags, age groups, family scores, energy, seasonality, booking, accessibility, parking, and cost. Age groups are `Small children (0-6)`, `Children (7-12)`, `Young adults`, `Seniors`; ratings are separate `family_score` values. Do not substitute informal groups such as “toddlers,” “teens,” or “all ages.”

Tags are: `Beach`, `Restaurant`, `Nature`, `Hiking`, `Viewpoint`, `Historic town`, `Museum`, `Adventure`, `Rainy day`, `Half day`, `Full day`, `Overnight`, `Free`, `Premium`. `Overnight` replaces `Full day` for a destination whose realistic one-way drive time makes a day trip impractical. Energy is exactly `Low`, `Medium`, or `High`. Seasons are `Spring`, `Summer`, `Autumn`, `Winter`, or `All year`.

Only the human editor-of-record may approve changes to categories, tags, enums, or the schema. Record approved changes in `docs/change-log.md` and update all relevant documentation and records together. Do not introduce synonyms or new values locally.

## Place record format and lifecycle

Each place record is a Markdown file with YAML front matter, named with a lowercase kebab-case slug, in `docs/places/`. The YAML front matter is the canonical data. Narrative Markdown may follow it but must not duplicate structured fields as a competing source.

Records declare `schema_version` and `status`. Valid statuses and transitions are defined in `docs/place-schema.md`. Unknown values are allowed only in draft workflow states and only in fields whose schema permits them. Never mark a record `approved` or `published` while publication-blocking facts, source evidence, validation errors, or review decisions remain unresolved.

Use stable IDs allocated through `data/place-id-registry.csv`; check the registry before creating a record. Do not derive a replacement ID when a name changes. A slug change requires a redirect entry according to the schema.

## Sources, evidence, and accuracy

Use official venue, government, tourism, transport, park, or heritage sources wherever available. Maps may establish identity, coordinates, and the source link, but not claims about safety, access, prices, facilities, opening, or family suitability. Record source URLs, supported claims/fields, dates checked, and checker in the record's evidence ledger. Apply the source-quality policy in the agent specifications.

Do not fabricate experience, reviews, amenities, prices, accessibility, child suitability, or travel time. If sources conflict or evidence is absent, retain an allowed unknown value and a review issue; do not guess. Preserve Spanish spelling and accents. Keep fact statements distinct from editorial judgments.

Driving time is an approximate one-way route from **Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain** to a named destination point. Record route source and check date. Do not estimate from memory.

Toll roads (owner decision 2026-11-11): use Google Maps' main figure, i.e. the fastest route it proposes, and do not avoid toll roads. The difference is a few minutes and is small next to local traffic. Earlier owner measurements with "toll roads avoided" are not re-done for that reason alone; where a record is re-checked, the new figure replaces the old one.

## Images and rights

Do not copy Google Maps images or user-uploaded material unless reuse permission is documented. Each image needs a stable asset ID, source, documented rights, required credit, role, dimensions when known, and useful context-specific alt text. Track rights and review status in `data/image-rights.csv`. Exclude assets with unclear or withdrawn rights. Alt text is for accessibility, not keyword insertion.

## Content and review

Write clear, useful, family-focused descriptions. Make suitability, energy, season, cost, and access claims evidence-aware and qualified. Accessibility and family ratings require human review under the evidence policy. Check volatile details according to the review intervals in `docs/multi-agent-workflow.md`.

The human editor-of-record owns final approval, source disputes, taxonomy, schema changes, correction escalation, and archival decisions. Agents prepare drafts and may not publish or deploy. Use the issue and handoff formats in the workflow for ambiguity, failures, corrections, and unresolved evidence.

## Validation

Before a record advances to human approval, validate YAML/front matter, schema version, required fields, enums, unique ID and slug, ID registry, duplicate place identity, URLs, evidence, and SEO uniqueness against the catalog. The validation gate is mandatory; a validation failure leaves the record in a draft/review status.
