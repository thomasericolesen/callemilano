# Google Maps list import workflow

## Goal

Turn a list of 200 or more saved Google Maps places into a smaller, evidence-aware editorial backlog that can be produced and maintained. Maps is a **discovery source**: it helps identify a place and the original listing, but it does not establish visitor facts such as hours, safety, access, facilities, cost, or family suitability.

This workflow applies the [destination record specification](destination-record-spec.md), the three-layer [knowledge model](knowledge-model.md), the stage budgets in the [content production system](content-production-system.md), and the prioritization approach in the [launch backlog](launch-backlog.md). Canonical place records are created only after identity and scope are resolved. AI may propose and prepare work; the human editor-of-record retains approval, taxonomy decisions, conflict resolution, and publication authority.

## Operating principles

- Process the full list for identity, duplicates, basic classification proposals, missing-information flags, and initial prioritization. Do **not** fully research all 200 places by default.
- Spend deeper research effort only after a human has confirmed the place is distinct, useful to the Casa de la Familia audience, and clear enough to scope.
- Keep **guest value**, **verification readiness**, and **editorial effort** as separate measures. A high-value but poorly documented place may deserve research priority; weak evidence must not be mistaken for low guest value.
- Preserve unknown, not searched, not applicable, and conflicting as distinct states.
- Never turn Maps ratings, reviews, photos, or descriptions into verified CalleMilano facts or guest contributions.
- Do not create duplicate records, silently discard source URLs, or allocate IDs before identity resolution.
- Use only the six approved place categories and five editorial content types. AI suggestions are not taxonomy approval.

## End-to-end stages

Effort ranges below are planning estimates for a batch of 200 and per-place estimates where useful. They describe active human or AI work, not elapsed time waiting for a source or an editor. Actual effort should be measured during the first batch and adjusted.

| Stage | Inputs | Outputs | Human effort | AI effort | Quality gates |
|---|---|---|---:|---:|---|
| 1. Raw import | Google Maps list or saved-place URLs/names; list title and owner-provided context; current catalog and ID registry for comparison. | Preserved intake item per listing; source URL/name; available identity clues; import exceptions; no new canonical record yet. | About 1–2 hours per 200-place batch for access, spot checks, and import exceptions; additional time only for malformed/ambiguous inputs. | About 1–3 minutes per listing to normalize the supplied name, retain the Maps URL, and identify missing/unclear intake values. | Every input has a traceable intake reference and original link; no review text or image is copied; private or unrelated data is excluded; duplicates are not discarded at intake. |
| 2. AI triage | Raw intake; current catalog; approved categories, tags, and content types; guest needs and launch priorities; source-quality rules. | Duplicate candidates; proposed identity/scope; proposed category and content type; preliminary launch score; evidence-readiness assessment; missing-information list; estimated verification effort; triage disposition. | About 1–2 hours to audit a representative sample per 200 and review high-risk/low-confidence items. | About 4–8 minutes per listing for identity matching, classification proposal, template-gap scan, candidate scoring, and concise rationale. | AI labels all values as proposals; likely duplicates and category uncertainty are explicit; preliminary trust reflects sources checked, not Maps content; no unsupported family/access/safety assertions are created. |
| 3. Human review | AI triage results; duplicate groups; candidate scores/rationales; current place records and controlled vocabulary. | Confirmed merge/update/new-place decisions; human-confirmed scope, category, content type, shortlist, exclusions/holds; resolved questions; authorized candidate set for fact checking. | Roughly 2–4 minutes per ordinary item reviewed; 5–15 minutes for ambiguous identity/scope or taxonomy decisions. For all 200, plan 7–15 hours, reduced when clear duplicates are reviewed as groups. | About 1–2 minutes per reviewed item to summarize matches, show evidence/rationale, and prepare the decision queue. | Human confirms primary category and scope; distinct branches remain distinct; an existing record becomes an update; uncertain identities wait for clarification; no ID or canonical draft is created before resolution. |
| 4. Fact checking and draft creation | Human-confirmed shortlist; exact visitor point; chosen content type; official/authoritative sources; project schema and registry; missing-information list. | Claim-level source packet; per-claim confidence and conflict flags; completed missing-information status; dated route estimate; draft record for selected candidates; unresolved issues with owner/next action; revised readiness and effort estimates. | Approximately 5–15 minutes per place for review/escalation and high-impact checks, plus human judgment on access, suitability, and source disputes. | Approximately 15–35 minutes per shortlisted place for official-source research, evidence organization, route checking, and draft field preparation. | Maps supports identity only. Material claims cite claim-specific sources/check dates. Unknowns and conflicts remain visible. Required category-template questions are covered or explicitly unresolved. Drafts validate against the active schema; no record is approved or published by AI. |
| 5. Editorial / publication queue | Fact-checked drafts; launch-value scores; trust-readiness summaries; effort estimates; blockers; independent review and validation results. | Ranked production backlog with batch, priority, owner, next action, blockers, confidence coverage, and estimate; separate ready-for-editorial-review, held, and replacement pools. | About 1–2 hours per batch of 30–50 for ordering, assigning owners, and confirming first-wave choices; human editor-of-record separately handles approval decisions. | About 1–2 minutes per candidate to update scores, summarize remaining blockers, and produce a ranked handoff. | Queue order cannot override evidence or publication gates; a high score does not mean publishable; unresolved blockers stay out of the approval-ready queue; humans control final approval and publication. |

## Stage 1: Raw import

Capture the list as supplied before normalizing it. Keep the source listing URL and supplied place name together so a later researcher can return to the same discovery item. Preserve optional list grouping or the guest context provided by the owner, but do not infer why a place was saved.

At this stage:

- Normalize whitespace and obvious encoding issues without replacing local spelling or accents.
- Retain alternative names as clues, not canonical names.
- Record missing links, inaccessible entries, and entries that resolve to a broad area rather than a specific destination.
- Compare against the current catalog and ID register as a lookup, not as permission to create an ID.

**Gate:** all inputs are accounted for as imported, failed, or awaiting clarification. Nothing is silently dropped because it looks like a duplicate.

## Stage 2: AI triage

AI triage should reduce review burden by assembling evidence and surfacing decisions, not by making irreversible choices.

### Duplicate detection

Use multiple clues together: canonical and alternate names, coordinates/place point, address, official site, supplied Maps URL, municipality, and the existing catalog. Return likely groups with a match rationale and confidence:

- **Likely same place:** same visitor identity despite spelling/name variation; recommend merging into the existing record or one new candidate.
- **Likely distinct:** separate branch, access point, venue, or experience; keep as separate candidates and explain why.
- **Uncertain:** similar names or nearby pins without enough evidence; send to human review.

Never merge merely because two entries share a chain name, beach, town, park, or broad map area. One saved-place entry may represent a business inside another destination; identify whether guests make one combined decision or need distinct records.

### Category and content-type proposal

AI proposes exactly one existing primary category: `Restaurants`, `Beaches`, `Excursions`, `Nature`, `City`, or `Family activities`. It separately proposes one of the five editorial templates: Attraction, Town, Beach, Restaurant, or Nature/Hiking. The proposal includes a one-sentence rationale and an uncertainty flag. A type/template does not change the controlled category. The human editor confirms the category and resolves borderline cases; AI must not introduce new labels or synonyms.

### Preliminary launch-suitability score

Use a **0–100 candidate-priority score** to sort human attention, not to decide publication. Score only what is known at triage and mark the result provisional:

| Criterion | Weight | Question |
|---|---:|---|
| Guest decision value | 35 | Does this place answer a meaningful choice about what to do, where to eat, or how to spend time? |
| Relevance to Casa guests | 25 | Is it realistically reachable and useful to guests staying in Cerros del Águila, considering time, party needs, and the outing’s scale? |
| Collection contribution | 15 | Does it add a useful option or fill a real category/experience gap without duplicating stronger coverage? |
| Evidence feasibility | 15 | Are responsible official sources and a clear visitor point likely to be available? This is research feasibility, not factual truth. |
| Effort to publish | 10 | Is the likely fact-check and editorial workload proportionate to the expected guest value? Lower effort earns more points, but cannot outweigh guest value. |

Show the component scores, one-line rationale, and confidence in the input. Do not reward a place just because it has many Maps saves/reviews, and do not penalize a high-value place solely because it needs research. Human review may change its rank with a recorded reason.

Use provisional bands to organize the review, not as automatic acceptance rules: **75–100** first-pass research candidates; **55–74** reserve/compare against category gaps; **below 55** defer unless it fills a distinctive guest need. Recalibrate after the first 25–50 entries and compare each band with human decisions.

### Trust / evidence-readiness score

Trust is claim-specific under the [knowledge model](knowledge-model.md); it is not a rating of whether the destination or its owner is trustworthy. For queue comparison, report a **0–100 evidence-coverage score** over the applicable material guest questions in that content type:

> **Evidence coverage = applicable material questions with current, relevant, claim-specific support ÷ all applicable material questions × 100.**

Each question still receives its own trust label: **high** (current and direct/authoritative support for the precise claim), **medium** (credible support with limited scope or indirectness that remains applicable to the claim), **low** (weak/ambiguous evidence), **unsearched**, **not found**, **not applicable with reason**, or **conflict**. A stale source that no longer supports a current claim is not medium evidence; it remains unverified. Unsearched, not found, and conflict do not count as supported coverage. Show the count of unresolved conflicts beside the percentage. A high evidence-coverage score cannot clear a single high-impact unresolved opening, safety, access, identity, or cost blocker.

At raw triage, if only Maps has been seen, the evidence-coverage score should normally be **0** for visitor claims. Maps can support identity/location leads, but never family suitability, opening, price, access, facilities, or safety.

### Missing-information scan

Compare known evidence with the required sections for the proposed content type and shared core in [content-types.md](content-types.md). For each requirement distinguish:

- **Not yet researched** — no source search has been made.
- **Searched, not found** — sources were checked but did not answer it.
- **Conflicting** — suitable sources disagree.
- **Not applicable** — with a reason tied to the place type.
- **Supported** — evidence covers the claim at the required scope and freshness.

AI may identify the question and likely source lead. It cannot mark a fact as absent from the real world just because search results did not show it.

## Stage 3: Human review

Review is a decision gate, not a rubber stamp. Present candidates in compact groups: likely duplicates, high-value candidates, low-evidence/high-risk candidates, category conflicts, and likely exclusions. Do not require the editor to reread every Maps card if the original source remains accessible and the triage record is clear.

The human reviewer decides:

- Whether candidates are the same identity, distinct places, or updates to existing records.
- The named visitor scope and point a future guest page would actually recommend.
- The primary category and editorial content type.
- Whether the candidate serves a guest decision and merits more research.
- Whether uncertainty means clarify, hold, exclude, or proceed to fact checking.
- Whether a list is overrepresented by near-identical options and which alternatives add more value.

Do not allocate a new stable ID to ambiguous or duplicate candidates. Confirmed new identities proceed for ID reservation and draft creation under the canonical workflow. A place can be held without being deleted; retain the reason so it can be reconsidered if evidence or launch needs change.

**Gate:** every reviewed candidate has an explicit disposition, accountable owner where work remains, and a recorded category/scope decision or clarification question.

## Stage 4: Fact checking and draft creation

Fact-check only human-confirmed candidates selected for the active research wave. First establish identity, exact arrival/visitor point, and current operation. Then research the highest-value claims required by the selected content type and the guest decision.

The source packet should:

- Prefer the venue or authority responsible for the specific claim; use secondary material only for clearly labeled gaps when a suitable official source is unavailable.
- Record each claim, supporting URL, source type, date checked, checker, confidence, applicable scope, and any limits in the evidence ledger.
- Record contrary sources and guest reports as separate items. Do not average them or silently choose one.
- Check volatile facts—operation, hours, prices, booking, parking, access, facilities—at the approved interval and for their valid season/date.
- Identify the exact visitor point and check a one-way route from Casa de la Familia to that point. Never estimate from memory.
- Keep recommendations separate from fact claims. Accessibility, safety, and family-suitability judgments receive human review.
- Create a draft canonical record only after identity is resolved and an ID is reserved. Do not create competing editable records in the import queue or generated catalog.

The initial fact-check is a **selection-quality pass**, not necessarily a finished destination page. It should be sufficient to decide whether full production is worthwhile and to expose blockers honestly. Candidates that pass this pass receive a revised launch score, evidence-coverage score, remaining-effort estimate, and next action.

**Gate:** source coverage is appropriate to the destination type; critical missing facts and conflicts are explicit; the record passes draft validation; no AI or agent assigns approval/publication status.

## Stage 5: Editorial and publication queue

Maintain two visibly separate queues:

1. **Production backlog:** human-selected places awaiting full page drafting, source follow-up, or review.
2. **Approval/publication queue:** complete drafts that have passed fact check, independent review, and validation and are awaiting the human editor-of-record’s decision or a separate release process.

Suggested candidate states:

- `triage_proposed`
- `human_review`
- `waiting_for_clarification`
- `hold`
- `exclude_or_merge`
- `research_selected`
- `needs_fact_check`
- `needs_editorial_review`
- `ready_for_human_decision`

The list above describes editorial queue dispositions only. Record lifecycle state remains governed by the canonical place schema; only the human editor-of-record can approve a record, and publication follows the separate authorized process.

Each production-backlog item should show:

- Candidate and confirmed scope/category/content type.
- Launch-priority score and its component rationale.
- Evidence-coverage percentage, per-claim trust labels, and unresolved-conflict count.
- Missing material information, blockers, and source-contact needs.
- Estimated remaining human/AI effort and expected guest value.
- Owner, next action, batch, and date last updated.

Rank the first wave by **guest value subject to feasible completion**, not simply by lowest effort or highest evidence score. Include a low-cost local choice alongside a few standout paid or full-day options when the catalog needs balance. Retain replacements in the research backlog so one difficult venue does not stall the whole batch.

**Gate:** only complete, validated drafts with no blocking issues enter the approval queue; only the human editor-of-record can approve, and publication follows the separate authorized publication process.

## Prioritization and selection rules

Use three views together:

1. **Highest guest value:** which choices most help Casa guests decide, especially for common needs and local outings.
2. **Fastest to complete:** where source material is already strong and remaining verification is limited.
3. **Lowest verification effort/risk:** where identity, current operation, access, cost, and arrival details can be established without unresolved high-impact uncertainty.

The launch order should not collapse these into one opaque score. Display the views separately and explain trade-offs. Use the launch score to create an initial queue, then let human review choose a practical batch. Re-rank when source replies arrive, a place closes, guest needs change, or a new candidate fills a stronger gap.

Exclude or hold when:

- The place is a duplicate or its identity/visitor scope cannot be resolved.
- It is outside the audience’s practical needs and adds little distinctive decision value.
- Current operation or an essential access/safety claim cannot be responsibly established.
- Its only support is Maps popularity, reviews, photos, or user-written listing claims.
- The place is a broad trip idea rather than a defined destination or bookable experience.

An exclusion is a current prioritization decision, not a claim that the destination is poor or permanently unsuitable.

## Batch sizing and planning envelope

Process the entire list through raw import and AI triage in manageable batches (for example, 25–50 inputs at a time) so errors and category patterns can be corrected early. Human review can then group duplicates and resolve exceptions. Avoid fact-checking 200 candidates to publication depth before choosing which ones matter.

For planning, a 200-item list may yield roughly:

- 200 traceable intake items;
- a smaller set after confirmed duplicate merges and non-destination exclusions;
- a human-selected research set of perhaps 30–60 places;
- a near-term production backlog of about 10–20, with a replacement pool;
- a separate approval queue containing only complete, validated drafts.

These are workload envelopes, not predicted outcomes or quotas. Use actual batch results to reset them. If the selected set still requires the ten-destination effort seen in [launch-backlog.md](launch-backlog.md), reserve approximately three active editorial hours per publication-ready place on average, with more time for source conflicts, inaccessible evidence, or access-sensitive destinations. Do not claim scale savings by reducing evidence or review requirements.

## Effort summary for 200 inputs

Using the ranges above, the first-pass raw import, AI triage, and human disposition review will typically require approximately **9–20 human hours** and **17–39 AI active hours**, depending on ambiguity and how much of the list needs individual review. A subsequent fact-check pass for 30–60 selected candidates adds approximately **2.5–15 human hours** and **7.5–35 AI hours**; full destination production is budgeted separately under the content production system. These ranges should be replaced with measured throughput after the first 25–50 entries.

Human effort is concentrated in identity resolution, taxonomy, guest value, suitability, conflicts, and approval. AI effort is concentrated in normalization, grouping candidate duplicates, source discovery, field-gap comparison, evidence summarization, and preparing concise review decisions. AI speed does not reduce the human owner’s accountability.

## Batch quality review

After the first 25–50 items and at each subsequent batch boundary, review:

- Duplicate precision: how often proposed matches were true same-place identities versus distinct branches/areas.
- Category agreement: how often humans accepted AI’s proposed approved category and template.
- Missing-field quality: whether triage found the questions that later blocked publication.
- Evidence quality: proportion of material claims with specific, current, responsible sources; common unresolved conflicts.
- Priority usefulness: whether high-ranked candidates served more guest decisions than low-ranked ones.
- Effort calibration: triage/research/editor time per item and how well estimates predicted actual work.
- Fairness and coverage: whether the shortlist overweights one category, geography, or well-marketed businesses at the expense of useful local options.

Correct systematic errors in the next batch instructions and rerun affected triage decisions. Do not retroactively change canonical records without normal review, source evidence, and approval.

## Completion definition

The Maps import is complete when every supplied list item is traceable and has a disposition, confirmed duplicates route to the existing identity, selected candidates have clear scope/category and a research owner, and the production backlog is ranked with evidence gaps and effort visible. This completes **backlog preparation**, not destination publication. Each place must still pass its own content-type checks, evidence validation, independent review, and human approval.
