# CalleMilano multi-agent workflow

## Purpose and authority

This workflow specifies how agents prepare and maintain place records. It does not authorize publication. `AGENTS.md` and the active `docs/place-schema.md` are authoritative.

Canonical editable records are Markdown files with YAML front matter in `docs/places/`. Reserve IDs in `data/place-id-registry.csv`; `data/place-catalog.csv` is generated and read-only. Images live in `images/`, with rights recorded centrally in `data/image-rights.csv`. Do not create competing copies of place data.

The human editor-of-record owns final approval, taxonomy and schema changes, source disputes, accessibility/suitability escalation, and archive/correction decisions. Agents never set `published` and never deploy.

## Intake and queue

Every individual or bulk Maps import is entered into `data/import-queue.csv` with a stable intake ID, input URL/name, processing state, retry count, duplicate candidates, clarification question if any, active stage/owner, and last update. Batch progress is tracked per place, so one ambiguous or failed entry does not block unrelated entries.

Before work, check the generated catalog and ID registry for existing identity, ID, and slug. A matching place becomes an update task; it does not create a parallel record.

## Stages

```text
Intake and duplicate check
          ↓
Maps Import Agent
          ↓
Fact Check Agent ── independent factual checks may run in parallel
          ↓
Editorial Agent
          ↓
SEO Agent
          ↓
Validation gate
          ↓
Human approval → separate publication process
```

The four roles are sequential at handoff boundaries. Within fact-checking, independent claims (for example official age rules and official parking details) can be researched in parallel, then consolidated into the evidence ledger. Low-risk edits to an existing, recently verified record may use a shortened path, but identity, source, accessibility, age restriction, price, booking, and driving-time changes always require fact check and human review.

### 1. Maps Import Agent

**Responsibilities:** Resolve place identity; capture original Maps URL, coordinates and pin purpose, canonical name and administrative location; check duplicate catalog entries; reserve stable ID and unique slug; create the complete draft front matter; add provisional taxonomy, family ratings, and candidate sources; log unknowns.

**Inputs:** URL or place name, optional disambiguating context, queue item, current schema, ID registry, catalog.

**Outputs:** Draft at `docs/places/{slug}.md`, queue state, source candidates, identity confidence, duplicate findings, open issues, and handoff summary.

**Handoff:** Proceed to fact check only if identity and intended coordinate point are clear. Otherwise save the clarification and candidate matches in the queue, set `waiting_for_clarification`, ask the user, then resume the same item. Never guess.

### 2. Fact Check Agent

**Responsibilities:** Verify identity, coordinates, administrative location, and each material claim against claim-specific official/authoritative sources. Verify volatile schedule, cost, booking, parking, facilities, dog policy, age limits, access, and seasonal facts. Check route time from the fixed Casa de la Familia origin to a named point. Populate the evidence ledger with claim, field, URL, source type, date, checker, confidence, and notes.

**Inputs:** Import draft and handoff, official/authoritative sources, active schema.

**Outputs:** Corrected record, complete evidence ledger for asserted facts, verification report, unresolved issues, and recommended next stage.

**Handoff:** Continue if identity and core facts are supported and any remaining unknowns are explicitly non-misleading draft values. Return fundamental identity/coordinate issues to Maps Import Agent. Conflicting or high-impact unsupported facts become blocking issues for the editor-of-record.

### 3. Editorial Agent

**Responsibilities:** Write concise, useful short and long descriptions from supported facts; preserve caveats; select one category and relevant controlled tags; assess family scores, age groups, energy, seasonality, and cost; make limitations clear. Keep claims distinguishable from editorial recommendation.

**Inputs:** Fact-checked record, verification report, style guidance, schema.

**Outputs:** Edited draft and editorial handoff note listing judgment calls and unresolved claims.

**Handoff:** Send unsupported or contradictory claims back to Fact Check Agent. Proceed to SEO only when content and classifications align with evidence.

### 4. SEO Agent

**Responsibilities:** Generate unique, accurate SEO title and description from approved editorial copy and verified facts. Avoid keyword stuffing and implied claims. Check proposed slug and metadata against the catalog. Do not use alt text as an SEO keyword field.

**Inputs:** Editorially stable draft, evidence ledger, catalog, current schema.

**Outputs:** SEO fields, duplicate check result, and SEO handoff note.

**Handoff:** If SEO wording changes factual meaning, send it back to Fact Check and Editorial. Otherwise send record to validation gate. No SEO Agent may approve or publish.

## Handoff contract and file ownership

Each handoff includes stable ID, path, schema version, status, requested action, sources/evidence, open issues, field changes, and any duplicate/slug findings. Only one agent owns a record file at a time. The receiver must confirm the expected revision before editing; save changes as a version-checked patch. On a conflict, stop and reconcile against the latest file rather than overwriting. Preserve human edits and explain material removals.

## Validation gate

Before human approval, validate:

- YAML front matter syntax and active `schema_version`.
- Required fields, field types, allowed unknown representation, and status transition.
- Category, tags, age groups, family-score keys, and every enum against the schema.
- Unique registered ID, unique slug, coordinates and coordinate purpose.
- Evidence coverage for factual claims, source URLs, check dates, and blocking review issues.
- Links' syntax/availability, no duplicate place identity, and no duplicate SEO title/description.
- Image asset IDs and current approved rights state.
- Draft or approval requirements applicable to the requested transition.

A validation failure creates a structured issue and keeps the record in a draft/review state. Validation should be implemented as an automated check before the workflow is relied on at scale; until then, a named reviewer must perform the same checklist manually and record the result.

## Issue, retry, and disagreement rules

All issues use `code`, `severity` (`blocking`, `warning`, `info`), `fields`, `description`, `retryable`, and `owner`. Retry transient source/validation failures up to two times, then escalate. Do not retry unresolved identity without a user answer. The editor-of-record decides irreconcilable source conflicts, category/taxonomy disputes, and evidence exceptions; the decision and rationale go in the evidence/review record.

## Approval, changes, and maintenance

Only the human editor-of-record can move `needs_editorial_review` to `approved`, or `published` to `archived`; publication itself belongs to a separate process. Approval records reviewer, decision, date, and notes. Requested edits return to the stage responsible, and material factual edits after approval reset status to `needs_fact_check`.

Corrections and closure reports enter the same queue with issue type and source. The editor-of-record triages them, assigns fact check, and records the resolution. Reopened places return to fact check before publication. Set `next_review_at` by volatility class: fast-changing details such as hours, cost, booking, parking, and access need shorter intervals than stable location/name facts. A stale record becomes `needs_fact_check`; do not leave stale content appearing current.

## Image rights workflow

Only approved assets with documented reuse permission may enter a place record. Register asset ID, source, permission evidence, attribution, rights review date, and state in `data/image-rights.csv`. The rights owner/reviewer controls approval or withdrawal. If rights are pending or withdrawn, remove the asset from publishable output and use `images: []` when no approved replacement exists.

## Registry, catalog, and taxonomy operations

- Allocate IDs through a single collision-checked `data/place-id-registry.csv`; never recycle an ID. If a name changes, preserve the ID.
- Check slug uniqueness in the generated catalog. A slug rename adds a redirect entry to the record.
- Generate `data/place-catalog.csv` from canonical front matter; never edit it directly.
- The editor-of-record approves taxonomy proposals. Record category/tag changes and rationale in `docs/change-log.md`, then update schema, agents, and records as one coordinated migration.

## Batch completion

A batch may contain successful, waiting, and blocked items. Report counts by state and list each affected intake ID. A place import is complete for editorial review when its record exists at the canonical path, matches the current schema, passes draft validation, and all unknowns/conflicts are explicit. It is not approved or published until the human review decision and separate publication gate are complete.
