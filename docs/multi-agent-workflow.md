# CalleMilano multi-agent workflow

## Purpose and authority

This workflow specifies how agents prepare and maintain place records. It does not authorize publication. `AGENTS.md` and the active `docs/place-schema.md` are authoritative.

Canonical editable records are Markdown files with YAML front matter in `docs/places/`. Reserve IDs in `data/place-id-registry.csv`; `data/place-catalog.csv` is generated and read-only. Images live in `images/`, with rights recorded centrally in `data/image-rights.csv`. Do not create competing copies of place data.

The human editor-of-record owns final approval, taxonomy and schema changes, source disputes, accessibility/suitability escalation, and archive/correction decisions. Agents never set `published` and never deploy.

## Implementation (2026-11-02)

The stages below are implemented as scripts and subagents described in `docs/agent-pipeline.md`: Maps Import = `tools/intake.py sweep/create`; Fact Check = subagents `source-reader` and `record-writer`; Editorial and approval stay with the main session and the editor-of-record. No SEO agent exists yet.

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

**Owner decision 2026-11-10:** a record that has passed fact-check (`needs_editorial_review`) counts as approved for use in the app and in trip plans. The editor-of-record does not sign off each record in advance; approval is a running process driven by family feedback from the app (positive feedback can mark a place "Familien anbefaler", negative feedback such as a closure or wrong price sends it back to `needs_fact_check`). The rules below still apply to the formal `approved` status, which is now optional.

Only the human editor-of-record can move `published` to `archived`; publication itself belongs to a separate process. (`approved` is no longer used as a step, see "Editor workflow"; the sentence "Only the editor can move `needs_editorial_review` to `approved`" is kept in effect for any record the editor chooses to approve formally.) Approval records reviewer, decision, date, and notes. Requested edits return to the stage responsible, and material factual edits after approval reset status to `needs_fact_check`.

Corrections and closure reports enter the same queue with issue type and source. The editor-of-record triages them, assigns fact check, and records the resolution. Reopened places return to fact check before publication. Set `next_review_at` by volatility class: fast-changing details such as hours, cost, booking, parking, and access need shorter intervals than stable location/name facts. A stale record becomes `needs_fact_check`; do not leave stale content appearing current.

## Editor workflow (owner decision 2026-11-11)

Goal: the editor-of-record sees only what needs editorial judgement or a formal decision. Claude does the rest and reports it in `docs/change-log.md`. This section replaces the editor sign-off per record described above; the summary rules are in `AGENTS.md`.

### Levels

| Level | Who | Meaning |
|---|---|---|
| A. Claude alone | Claude | Done without asking; logged in the change log; the editor can always ask for a rollback. |
| B. Claude, editor informed | Claude | Done and included in the weekly summary; no answer needed. |
| C. The editor decides | Editor | On the editor list with Claude's recommendation and ready-made choices; Claude changes nothing until answered. |
| D. Only the editor | Editor | Formal decisions reserved for the editor; never delegated, not even by a general permission. |

When in doubt, use the higher level.

### Who decides what

| # | Element | Level | Rule |
|---|---|---|---|
| 1 | Hours, prices, address, phone, rules from an official or own source | A | Claude updates with quote, URL, date and source in the evidence ledger. A conflict between two sources goes to row 9. |
| 2 | Driving time from Casa de la Familia | A | Google Maps' main figure (fastest route, toll roads allowed), measured in Chrome, with date and link. A change over 15 min or a move between `Tæt på` and `Dagsture` is reported (B). |
| 3 | New place proposed by the editor or the family | A, then C | Claude creates the draft and reads the sources; whether it is included is the editor's choice (Yes/Maybe/No on a checklist). |
| 4 | New candidates from sweeps | C | Claude screens them onto a checklist; the editor chooses. No candidate enters the app without a choice. |
| 5 | `draft` → `needs_fact_check` | A | When identity and coordinates are clear. |
| 6 | `needs_fact_check` → `needs_editorial_review` | A | When there is official evidence for the core facts and no open blocking or `facts_not_checked` issue. Subagents never set this; the main session does. Shown in the app as "Faktatjekket". |
| 7 | `approved` | none | Retired as a step. `needs_editorial_review` is the end station and counts as approved. Existing `approved` records stay unchanged. |
| 8 | `needs_editorial_review` (or older `approved`) → `needs_fact_check` | A | On negative app feedback (closed, wrong price, wrong hours) or when `next_review_at` is overdue; Claude sets it and corrects the facts. |
| 9 | Source conflict (price, hours, minimum age, access, safety) | C | Claude puts both sources with quotes on the list and recommends one. Conflicts are never closed in bulk. |
| 10 | Category | D | The editor; Claude proposes. |
| 11 | Tags, family score, energy, age groups | C | The editor's judgement, collected on a checklist; Claude proposes from evidence but writes only what the editor chose (also for adjustments). |
| 12 | Accessibility, child safety, dogs | C | Official source or the editor's own knowledge; never a guess. |
| 13 | Archiving | C | The editor. If the facts for a place are too hard to obtain, it drops off the list. Claude puts the proposal on the list with what was tried; drafts without a usable source after two attempts are proposed automatically. |
| 14 | Taxonomy, new tags, enums, schema changes | D | Only the editor. |
| 15 | Images and rights | D | Only the editor. |
| 16 | Issues | A or C | `info` and `warning`: Claude. `blocking` and all conflict issues: the editor. |
| 17 | Trip plans, restaurant checks, opening-hours jobs | A | As before (`docs/trip-planner-agents.md`). |
| 18 | Catalogue, export, change log, status file | A | Claude updates them with every change. |
| 19 | Push, PR, merge to `main`, import into the app | see below | Standing permission for A/B work. |

### Editor list

At most once a week and only when there is something, one interactive list of all level C and D items, about 25 at most; the rest waits. Fields per item: place (name, category, area, drive time); what to decide (one sentence); why now (conflict, request, assessment, archiving); sources (links, short quotes); Claude's recommendation (one choice, the default); choices (2 to 4 checkboxes); note (optional).

Fixed choices by type: conflict: use source A, use source B, write "check before visiting" and leave the value unknown. Archiving: archive, keep and retry (say what), ask the family. New place: yes, maybe, no. Assessment (tags and family): the controlled values from the schema, preselected with the current ones; "don't know" means leave unchanged and is not an open issue.

Answers are stored in the list. Claude reads them and writes them to the records with evidence (the editor's own judgement, date, link to the list). The list and all choices are kept as history.

### Weekly summary (level B)

A short summary in the change log, shown when the editor opens a session: places updated, lifted, sent back to fact-check and archived by Claude; driving times that changed much; places with negative feedback and what was done; what was dropped as "too hard" and why. It needs no answer.

### Issues

| Severity | Closed by | How |
|---|---|---|
| `info` | Claude | When clarified or irrelevant for the whole; noted in the evidence. |
| `warning` | Claude | The source is tried twice. If it works: closed with evidence. Otherwise closed as "not found"; the value stays unknown and is shown as "check before visiting". |
| `blocking` | Editor | On the editor list. |
| Conflict (price, time, age, access, safety) | Editor | Always the editor list; never closed in bulk. |

Issues are closed by these rules and never in bulk to reach a status.

### Statuses and what the app shows

| Status | Meaning | App label |
|---|---|---|
| `draft` | Created, not checked. Not in the app. | none |
| `needs_fact_check` | To be checked, or has an open `facts_not_checked`. | "Ikke faktatjekket" |
| `needs_editorial_review` | Fact-checked; counts as approved for use; end station. | "Faktatjekket" |
| `approved` | Retired as a step; old records are kept and treated like `needs_editorial_review`. | "Faktatjekket" |
| `archived` | Out of the guide; the record is kept. | none |

### Push, PR, merge and import

Standing permission for changes that consist only of level A/B work: Claude may push, open the PR with `gh`, merge and import into the app, and reports afterwards. Changes with level C/D content (archiving, categories, tags, conflicts, rule changes in `AGENTS.md`) are merged only after the editor has answered. `main` changes only through a PR. After every import, check it: count of updated places, none skipped, a spot check of one place. GitHub work uses `gh` (logged in as `thomasericolesen`); the import (`callemilano.dk/admin`), the Facebook/Instagram checks and Google Maps checks need Claude in Chrome open and signed in.

### When the family uses the app

Negative feedback (closed, wrong price, wrong hours): Claude fixes it from a source and sets `needs_fact_check` until the correction is read from a source (level A). Positive feedback may mark "Familien anbefaler" (green); no editor action. Feedback that disagrees with a source goes on the editor list.

### Freshness

`next_review_at` follows volatility (hours, prices and access shorter than name and location); five months is the default for fact-checked places. Monthly, Claude sets overdue places back to `needs_fact_check` and reads the official sources again. Only conflicts go to the editor.

### Recording decisions

Every editor decision gets a line in `docs/change-log.md` with date and source (list or chat). Rules that apply going forward are also written in `AGENTS.md`. No rule applies until it stands there; if something was only said in chat, Claude asks whether it should be written in.

Open item from the review of 2026-11-11: the editor said that some elements are missing from the table above but has not yet named them; add them as new rows when known.

## Image rights workflow

Only approved assets with documented reuse permission may enter a place record. Register asset ID, source, permission evidence, attribution, rights review date, and state in `data/image-rights.csv`. The rights owner/reviewer controls approval or withdrawal. If rights are pending or withdrawn, remove the asset from publishable output and use `images: []` when no approved replacement exists.

## Registry, catalog, and taxonomy operations

- Allocate IDs through a single collision-checked `data/place-id-registry.csv`; never recycle an ID. If a name changes, preserve the ID.
- Check slug uniqueness in the generated catalog. A slug rename adds a redirect entry to the record.
- Generate `data/place-catalog.csv` from canonical front matter; never edit it directly.
- The editor-of-record approves taxonomy proposals. Record category/tag changes and rationale in `docs/change-log.md`, then update schema, agents, and records as one coordinated migration.

## Batch completion

A batch may contain successful, waiting, and blocked items. Report counts by state and list each affected intake ID. A place import is complete for editorial review when its record exists at the canonical path, matches the current schema, passes draft validation, and all unknowns/conflicts are explicit. It is not approved or published until the human review decision and separate publication gate are complete.
