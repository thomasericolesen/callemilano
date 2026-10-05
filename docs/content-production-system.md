# Content production system

**Goal:** Produce and maintain 50 decision-ready destination pages for guests staying at Casa de la Familia in Cerros del Águila.

This process applies the five page types in [content-types.md](content-types.md), the gates in [editorial-checklist.md](editorial-checklist.md), and the candidate shortlist in [launch-candidates.md](launch-candidates.md). The ten-destination production test estimates **150–200 active editorial hours** for 50 destinations, before waiting for venue replies. The process below targets roughly three hours of work per destination on average; complex or poorly documented places will take longer.

Agents prepare drafts and evidence. The human editor-of-record resolves high-impact disputes, approves eligible content, and controls publication. No score or automated check overrides a publication blocker.

## Production workflow

Times are **active effort per destination**, not elapsed calendar time. Independent evidence searches can run in parallel. The average budget below is about three hours per place; allow **150–200 hours total** for the 50-place pilot, replacements, and correction cycles.

| Step | Owner | Expected time | Inputs | Outputs | Quality gate |
|---|---|---:|---|---|---|
| 1. Intake and prioritization | Maps/import agent; editor sets batch order | 0.15 h | Candidate list, category mix, destination rationale, known pilot notes | Queue item, proposed content type, initial source leads, priority | Candidate serves a guest decision; no padding to hit category counts; unresolved generic excursions go to scope review. |
| 2. Resolve identity and scope | Maps/import agent | 0.20 h | Candidate name, Maps/tourism leads, current schema, generated catalog, place ID registry | Canonical identity, exact intended visit scope, named visitor point, duplicate/redirect findings, registered ID and unique slug | Identity and visitor point are distinct and navigable. Ambiguity or duplicates stop the record here; never allocate a replacement for an existing identity. |
| 3. Gather claim-specific sources | Research/fact-check agent; independent searches may be delegated to subagents | 1.05 h | Scoped destination, category template, official venue/authority sources, source policy | Evidence ledger: claim, source URL/type, check date, checker, confidence; source links for live visitor details | Prefer official/authoritative sources. Each material claim is supported; source conflicts and stale sources are flagged. Maps support identity/location only, not visitor claims. |
| 4. Verify plan-critical facts | Fact-check agent; human owner handles escalations | 0.40 h | Evidence ledger, route provider, operator/authority sources, exact visitor point | Dated one-way drive estimate from Casa; visit duration; current schedule, costs, booking, restrictions, access, and arrival findings | Drive estimate matches the named visitor point. Critical unknowns are resolved or marked blocking. Do not infer family fit, access, or live availability. |
| 5. Draft the guest page | Editorial agent | 0.50 h | Fact-checked findings, selected content type, guest needs and MVP priorities | Concise, decision-focused page; facts separated from editorial recommendations; explicit caveats | Correct template; answers time, cost, fit, access, and next steps; no unsupported claims or empty promotional prose. |
| 6. Search copy and mechanical validation | SEO agent plus automated checks; manual reviewer until tools exist | 0.15 h | Stable draft, evidence links, current controlled values, generated catalog | Accurate unique page/search title and description, link/section report, uniqueness/enum checks, canonical place record | No factual meaning introduced by search copy. Required sections, links, dates, registered IDs/slugs, and controlled values pass checks. Editable records stay in `docs/places/`; generated catalog output is never edited as a second source. Failure returns to the responsible stage. |
| 7. Independent content review | Reviewer who did not draft the page | 0.30 h | Draft, evidence ledger, checklist, validation report | Review decision, defects ranked blocking/warning, corrections routed to owner | Independently sample-check high-impact claims and check every blocker in the editorial checklist. A broad source link is not evidence for a specific claim. |
| 8. Human owner decision | Human editor-of-record | 0.25 h average | Draft, evidence, reviewer findings, issue list, validation result | Approved, returned for correction, or held; decision and rationale recorded | Human resolves taxonomy/scope disputes, suitability/access judgments, conflicting sources, and evidence exceptions. Only eligible records are approved. |
| 9. Release and maintenance setup | Human publication owner; reviewer sets follow-up dates | 0.10 h | Approved record, rights-cleared assets if any, volatility of facts | Publication handoff, review owner, next review date, correction route | Agents do not publish/deploy. Hours, prices, booking, parking, transport, and access get review dates based on their volatility; stale content returns to fact check. |

**Planning note:** The row estimates total about **3.1 hours per destination**. For 50 records, the straight-line estimate is 155 hours. Keep the production-test range of **150–200 hours** to account for difficult evidence, replacements, and corrections. Waiting for responses is calendar delay, not active editorial time.

## Batch operation

1. **Prepare a screened queue:** Start with the 50 launch candidates, but keep a replacement pool. Preserve the approved category targets as a guide; reject weak candidates rather than lowering the evidence bar.
2. **Run a five-page calibration batch:** Include at least one destination of each content type. Confirm that reviewers interpret blockers consistently and that required route estimates can be produced.
3. **Process in batches of ten:** Keep an independent queue state, owner, evidence, blockers, and next action for each destination. Do not let one missing response block unrelated pages.
4. **Hold a batch gate:** Before beginning the next ten, review blocker frequency, repeated source gaps, category balance, duplicate/scope issues, reviewer rework, and active time per page. Update candidate choices or instructions if a recurring defect appears.
5. **Finish the 30/20 waves:** Deliver the first 30 and remaining 20 as separate review batches. Report counts as ready for human review, returned, held, replaced, and approved. A batch is complete only when each record's state is explicit.
6. **Do not treat approval as publication:** Human approval and the separate publication process remain distinct. Any failed validation or unresolved blocking fact stays in draft/review.

## Maintenance workflow

- Track a named owner, check date, source, and next review date for every volatile detail. Follow the volatility classes and status transitions in the project workflow; do not invent a single refresh interval for all facts.
- Use automated due-date reminders and link checks to create a fact-check queue. A working link does not prove its content is current or accurate.
- Recheck fast-changing hours, prices, booking, parking, access, and transport at shorter intervals than stable names and locations. On closures, corrections, and guest reports, return the affected claims to fact check before restoring the recommendation.
- Re-run the same content-type checklist after material edits. Independent review and human approval are required again when an edit affects identity, route, price, booking, suitability, access, or other plan-critical details.
- Agents may prepare revisions and summarize changes. The human editor-of-record owns source disputes, correction escalation, archival decisions, approval, and publication.

## Automation opportunities

### Automate

- Queue creation, stage/owner tracking, due-date reminders, batch status counts, and blocked-item reports.
- Page skeleton generation from the five content types and presence checks for required sections.
- YAML/front-matter and controlled-value validation, registered ID and slug uniqueness, duplicate candidate flags, required-source/date presence, link syntax, and SEO uniqueness.
- Arithmetic checks for stated party-price examples; stale-date alerts; broken-link detection; comparison of review dates against volatility classes.
- Repetitive handoff summaries and checklist reports.

These checks improve consistency but do not prove a claim. Link checking cannot certify a price or opening hour, and a required-section check cannot judge whether the content answers the guest's question. Where project validation tooling is not yet available, keep the checklist manual and have a named reviewer record the result before relying on it at scale.

### Keep under human judgment

- Whether two names or pins describe the same place, and whether a town, trail, beach, or excursion is scoped clearly enough to recommend.
- Whether sources support the exact claim, which source should prevail in a conflict, and whether a fact is too volatile or consequential to publish.
- Family/age suitability, effort, accessibility interpretation, stroller/wheelchair limitations, cost examples, and whether an unknown could make the outing unsuitable.
- Whether a replacement is genuinely useful, whether categories or editorial choices need owner approval, and the final decision to approve, publish, correct, or archive.
- Whether prose is clear, balanced, and useful without exaggeration. AI scores or ratings cannot replace evidence or editor review.

## Where subagents help most

- **Parallel claim research:** Split independent claims for one place—opening/prices/booking, access/parking/facilities, and transport/route—among research subagents. The fact-check lead consolidates claims into one evidence ledger and resolves conflicts.
- **Parallel destination batches:** Assign groups of destinations by category or geography so source familiarity and local context can be reused. Keep one file owner per destination and use version-checked handoffs.
- **Independent challenge review:** Ask a reviewer who did not draft the page to check its most consequential claims and identify missing guest questions. This is most valuable for access, formal restrictions, cost, and visitor-point scope.
- **Do not delegate approval:** No subagent changes categories/enums, accepts weak evidence, clears a blocker, approves a record, or publishes it. Escalate these to the human editor-of-record.

### Expected hours saved

The following are planning estimates, not measured results. Compare against a single editor doing the same 50 pages serially:

- **Research subagents:** Shift roughly **25–40 hours of first-pass source gathering and claim organization** away from the lead editor. This is human-editor capacity recovered, not research work eliminated; agents still perform the searches, and the lead/reviewer must inspect the evidence.
- **Automation:** After setup, save about **10–15 hours** across the batch on repetitive page creation, presence/format/uniqueness checks, arithmetic, due dates, and status reporting. Expect **5–8 hours of initial tool setup** if these checks do not exist yet, so net savings in the first 50 are modest; the benefit compounds during maintenance.
- **Batching/reuse:** Reuse of category-specific source packs and page patterns may save another **5–10 hours** of context switching and repeated setup, provided destination-specific evidence is still checked.

Overall, plan for roughly **40–60 editor hours of capacity recovered** across the 50-place launch, while retaining the same claim verification and human sign-off. Parallel work is expected to shorten the calendar path most during research; it does not justify reducing independent review.

## Recommended multi-agent architecture

Use the project's four staged agent roles, with one human editor-of-record:

1. **Maps Intake Agent:** Identity, scope, duplicates, visitor point, queue entry, and draft record preparation.
2. **Fact Check Agent:** Official-source research, dated drive estimate, evidence ledger, volatile details, and blocking issues. This role may delegate independent claims or destination batches to short-lived research subagents, then consolidates their evidence.
3. **Editorial Agent:** Applies the correct content type and writes the guest-facing page from verified facts, keeping judgments and caveats explicit.
4. **SEO/Validation Agent:** Checks unique accurate search copy, performs the independent checklist review, and runs or records validation results. Returns defects to the responsible stage; never approves or publishes.
5. **Human editor-of-record:** Resolves disputes and editorial judgments, approves eligible content, and authorizes the separate publication process.

Four agent roles are the minimum efficient configuration for this project because they preserve identity, fact-check, writing, and final-review handoffs without giving one agent unchecked control over the whole record. The same agent instance can cover more than one role sequentially when throughput is low, but **the final reviewer must not be the page's drafter**. For the 50-page push, run at least two research subagents in parallel under the Fact Check Agent; scale their count to workload, not to a fixed per-place formula. Maintain the canonical place record as the single editable source, and keep human approval as the publication gate.
