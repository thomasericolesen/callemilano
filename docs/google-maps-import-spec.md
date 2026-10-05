# Google Maps import specification

## Purpose and scope

This specification governs intake of a Google Maps saved-place list exported from the CalleMilano Spain project. Maps is a discovery and identity source. It is not evidence for a destination’s opening status, price, safety, facilities, access, or family suitability.

Apply this document with the staged [maps import workflow](maps-import-workflow.md), [destination record specification](destination-record-spec.md), and [knowledge model](knowledge-model.md). The human editor-of-record retains final decisions on identity disputes, category assignment, taxonomy changes, source conflicts, suitability, approval, and publication. The current place schema remains canonical; this document does not change it.

## Import item and batch identity

Every row in an imported batch represents one saved-list entry, not necessarily one new destination record. Preserve a traceable relationship between the raw list entry and its eventual disposition: new record, update to existing record, duplicate/merge, clarification, hold, or exclusion.

Batch-level context should identify:

- The source list as named in Google Maps and its source/project context (Spain project).
- Import date and batch identifier.
- The guest audience or purpose supplied by the project owner; do not infer intent from a saved place alone.
- The person or role responsible for intake and the reviewer responsible for final triage.

## Required import fields

These are required to preserve and review each raw list entry. If a value is missing from the export, record it as missing rather than inventing it.

| Field | Rule |
|---|---|
| Batch identifier and item number | Unique within the batch; retain through all review stages and dispositions. |
| Raw saved-place name | Preserve the displayed name as supplied, including Spanish accents and spelling. Do not overwrite it with an AI-normalized name. |
| Google Maps URL | Preserve the original listing URL. If absent or unusable, flag the issue and keep the item traceable by batch/item number. |
| Source-list name/context | Record the source list and Spain-project context so later reviewers can trace where the item came from. |
| Import date | Date the item entered CalleMilano intake. |
| Intake disposition/state | Use the approved intake or editorial queue state; do not treat an imported item as a place record or publication approval. |

The user-facing template in [import-batch-template.md](import-batch-template.md) adds triage fields needed to turn these raw entries into reviewable candidates.

## Optional import fields

Retain these only when present in the export or supplied as project context. They are clues for identity resolution, never substitute evidence for visitor claims.

| Field | Use and limits |
|---|---|
| Google Maps Place ID or other listing identifier | Helps match a listing; does not by itself prove a unique real-world venue identity. |
| Coordinates / pin | Helps identify and geolocate the saved point. Confirm the point purpose (entrance, business, town centre, trailhead, or representative point) before using it in a destination record. |
| Displayed address or locality | A matching clue to check against official or authoritative sources. Do not treat it as the official visitor address without verification. |
| Displayed business/site name | A discovery clue; confirm canonical spelling and current identity with an appropriate source. |
| List grouping or saved label | Preserve if useful to understand the imported list, but do not infer a recommendation or user intent from the group name. |
| User-provided notes | Keep only notes relevant to the import decision. Separate owner-provided notes from guest feedback and verified facts. |
| Existing catalog/record candidate | Record the possible match and reason; human review confirms whether it is an update, duplicate, or distinct destination. |

Do not import Maps reviews, review text, photos, ratings, personal profile information, or implied image permissions into CalleMilano content. Popularity is not evidence of quality, suitability, trust, or launch priority.

## Duplicate handling

Compare a candidate against the current catalog and place ID registry before creating a new canonical record. Use several identity clues together:

- Canonical and alternate names, with accents and common spelling variations.
- Address, coordinates, and the purpose of the saved pin.
- Official website, phone or venue identity where available.
- Municipality/locality and the exact visitor experience represented.
- Existing record name, stable ID, and scope.

Assign a **proposed match disposition**:

1. **Same place / existing record:** route as an update to the existing record owner; retain the imported URL and batch reference. Do not create a second record or allocate a replacement ID.
2. **Same place / multiple list entries:** retain all source entries in the batch history but select one canonical candidate for human confirmation. Preserve distinct source links as references; do not erase provenance.
3. **Distinct place:** keep separate only when the visitor identity, branch, entrance, experience, or guest decision is meaningfully distinct.
4. **Uncertain match:** send for manual review or clarification. Do not merge, split, or allocate an ID based on name similarity alone.

Do not merge two branches solely because they share a chain name. Do not merge a beach with a beach club, trail, town, or nearby attraction because a pin is close. For towns and broad areas, confirm the intended visitor scope and named arrival point. Human review confirms every uncertain match and any merge that would change an existing record’s identity or scope.

## Category and content-type assignment rules

Category and editorial content type are separate decisions. Assign exactly one approved primary category; separately recommend one of the existing content templates.

### Approved primary categories

- `Restaurants` — restaurants, cafés, and food/drink venues.
- `Beaches` — beaches, coves, and coastal bathing areas.
- `Excursions` — organized outings, routes, and destination-led trips not better represented by another category.
- `Nature` — natural areas/features such as parks, reserves, rivers, or caves when not primarily a hike.
- `City` — a city, town, or village recommended as a destination.
- `Family activities` — attractions or activities centered on a visitor activity.

### Editorial content templates

Use only: **Attraction, Town, Beach, Restaurant, Nature/Hiking**. Examples: a ticketed museum can be `Family activities` + Attraction; a town walk can be `City` + Town; a defined coastal walk can be `Nature` + Nature/Hiking; a restaurant is `Restaurants` + Restaurant.

The AI or intake reviewer may propose one category and one template with a short rationale and confidence. The human editor-of-record confirms the category and resolves borderline classification. Do not use `Cities`, informal synonyms, or newly invented tags/categories. If the candidate does not fit the approved vocabulary, flag it for human taxonomy review rather than stretching a label.

## Launch-priority scoring rules

Use the provisional **0–100 candidate-priority score** to order human attention and research, not to predict publication quality or guest satisfaction. Record criterion scores, rationale, input confidence, and the reviewer’s adjustment reason.

| Criterion | Weight | Scoring question |
|---|---:|---|
| Guest decision value | 35 | Does this place answer a meaningful choice about what to do, where to eat, or how to spend time? |
| Relevance to Casa guests | 25 | Is it practically useful to guests staying in Cerros del Águila, considering distance, visit duration, party needs, and outing scale? |
| Collection contribution | 15 | Does it add a distinct useful choice or address an actual coverage gap rather than duplicate a stronger option? |
| Evidence feasibility | 15 | Are a clear visitor point and responsible sources likely to be available for the claims the page needs? This is research feasibility, not trust. |
| Effort to publish | 10 | Is the remaining verification and editorial effort proportionate to its guest value? Lower effort earns more points, but cannot outweigh guest value. |

Starting bands for a 25-place batch:

- **75–100:** first-pass research candidates.
- **55–74:** reserve and compare against category/guest-need gaps.
- **Below 55:** defer unless it serves a distinctive need or fills a material gap.

These bands are provisional and must be recalibrated after the first batch. They are not automatic inclusion/exclusion rules. Show guest value, effort, and trust readiness as separate views; a high value/low evidence candidate may deserve research, but cannot skip fact checking. Never use Maps save counts, reviews, rating, or photo volume as a score input.

## Trust-scoring rules

Trust is claim-specific. The batch-level score is an **evidence-coverage/readiness measure**, not a trust rating of the venue or destination.

> **Evidence coverage = applicable material guest questions with current, relevant, claim-specific support ÷ all applicable material guest questions × 100.**

For each question/claim, record one of these states:

- **High:** a current, direct or authoritative source supports this precise claim and scope.
- **Medium:** credible evidence supports the claim but has a meaningful limit in scope or directness and remains applicable.
- **Low:** weak, ambiguous, indirect, or insufficiently specific support.
- **Unsearched:** no claim-specific source search has been made.
- **Not found:** appropriate sources were checked but the answer was not established.
- **Conflict:** suitable sources materially disagree; preserve both claims and open a review issue.
- **Not applicable:** with a destination-specific reason.

Only supported High/Medium claims count toward coverage. Low, Unsearched, Not found, and Conflict do not count. Exclude justified Not applicable items from the denominator. Display the number of unresolved conflicts beside the percentage. At raw import, Maps alone ordinarily supports **0% visitor-fact coverage**; it can support identity/location leads only. No aggregate score clears an unresolved publication blocker, especially identity, current operation, access, safety, booking, or material cost.

## Manual-review triggers

Require human review before creating or advancing a candidate when any of the following applies:

- Likely duplicate, similar name, chain branch, adjacent attraction, ambiguous visitor point, or existing-record update.
- Unclear municipality/country, implausible coordinates, broad town/route area, or a pin that may not be the visitor entrance.
- Proposed category/template is borderline, uncertain, or outside the approved list; any proposal would change taxonomy or controlled values.
- A destination appears closed, renamed, moved, seasonal, or inconsistent across official sources.
- A high-priority score depends on guessed audience fit, travel burden, or value not supplied by evidence.
- Any safety, access, wheelchair, child-suitability, nudism, water-quality, route-difficulty, or seasonal-restriction question affects whether a family should go.
- A credible source or guest observation conflicts with a current official claim.
- Sources are absent, stale, secondary-only where an official source should exist, or do not support the exact claim.
- The place is a broad excursion concept without a defined operator/product or clear guest-facing scope.
- The import contains non-place material, personal data, reviews, or images that should not enter the destination record.
- A new ID, slug, canonical record, or category decision is needed.

An AI proposal remains provisional until resolved. Record the manual-review decision, owner, date, and rationale. Ambiguous identity waits for clarification; it is not resolved by a guessed record.

## Disposition and handoff

Every imported item must leave the first-batch process with one explicit recommendation:

- **Research selected** — human-approved identity/scope and worth an initial official-source fact-check.
- **Update existing record** — send to that record’s owner with the source link and proposed changes.
- **Merge as duplicate** — keep source provenance and point to the confirmed canonical identity.
- **Clarify** — name the exact identity/scope question and owner.
- **Hold / reserve** — potentially useful but lower priority or blocked on a future source/need.
- **Exclude for this batch** — give a brief reason; this is not a permanent judgment of destination quality.

Only after a human confirms a distinct candidate should an ID be reserved and a draft place record created in the canonical place-record location. AI and agents may prepare evidence and drafts but may not approve or publish.
