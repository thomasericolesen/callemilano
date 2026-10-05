# CalleMilano destination record specification

## Purpose and authority

This document defines the editorial record needed to maintain a destination page over time. It brings together the shared guest-decision content in [content-types.md](content-types.md), the three knowledge layers in [knowledge-model.md](knowledge-model.md), and the evidence and page standards illustrated by [gold-standard-destination.md](gold-standard-destination.md) and [docs/published/](published/).

The record must let an editor answer four questions for every material statement:

1. Is it a verified fact, an editorial recommendation, or a guest observation?
2. Who owns it, and when was it last checked or experienced?
3. What source or reasoning supports it, and how much trust should a guest place in it?
4. What should happen if another source or visitor says something different?

The current [place schema](place-schema.md) remains canonical. This specification does not change it or approve new controlled fields. It defines the complete editorial information a destination record needs; any structural change needed to hold the additional governance details requires approval from the human editor-of-record and coordinated updates to the schema and related project documents.

## Record structure

A complete destination record has five connected parts:

1. **Destination identity and guest essentials:** what the place is, where the guest should go, and the current practical facts.
2. **Claim register:** each material verified fact, with source, scope, dates, owner, trust basis, and publication state.
3. **Editorial guidance:** reasoned recommendations linked to the facts and explicit assumptions they use.
4. **Guest observations:** moderated first-hand reports kept separate from facts and editorial conclusions.
5. **Conflict and review history:** unresolved differences, next action, accountable owner, decision, and correction history.

The public page is a readable summary of this record. It must preserve the distinction between its parts and must never present an unresolved claim as settled merely because it appears in polished prose.

## Update-frequency terms

Use the project’s approved volatility intervals in [multi-agent-workflow.md](multi-agent-workflow.md); the terms below describe the trigger, not a replacement calendar:

- **Stable / on change:** Recheck when the name, identity, location, boundaries, or official scope changes, or when a credible correction arrives.
- **Volatile / short interval:** Recheck at the approved short interval and after credible reports of a change. Applies to hours, admission, booking, parking, menus, facilities, and access.
- **Seasonal / before season:** Recheck before the relevant season or operating period and when a current notice or report indicates a change.
- **Live / date-specific:** Check for the guest’s planned date or visit day. Applies to warnings, closures, water quality, weather, and same-day services.
- **At each edit / review:** Update when the record changes and reconsider during its scheduled editorial review.
- **Per contribution:** Date and moderate each report when received; older observations lose prominence according to the approved freshness policy.

Do not make a fact seem current just because another field on the page was checked recently. Freshness attaches to the claim.

## Field specification: identity and lifecycle

These fields establish the destination’s identity and whether the record may move through review. Owners are responsible for proposing or preparing updates; approval authority remains with the human editor-of-record as specified below.

| Field | Purpose | Owner | Update frequency | Publication rules |
|---|---|---|---|---|
| `schema_version` | Identifies the approved record contract. | Human editor-of-record owns schema approval; record editor applies it. | On approved schema change. | Must match the active approved schema; never change it locally to accommodate an unapproved field. |
| `status` | Shows the record’s review state. | Human editor-of-record controls approval, publication, and archival transitions. | At each workflow handoff or decision. | Use only allowed transitions. Unresolved publication blockers, failed validation, or absent human approval keep it out of `approved`/`published`. |
| `id` | Stable identity across edits and name changes. | Intake editor reserves it through the project register; human owner resolves identity disputes. | Once at creation; never replaced. | Must be unique and registered. Do not invent, recycle, or change an ID to fix a duplicate. |
| `slug` | Stable public page identifier. | Editorial/validation owner checks uniqueness; human owner approves material identity changes. | At creation; on approved rename only. | Lowercase kebab-case, unique; a changed slug must preserve a redirect. |
| `name` | Correct, recognizable public name. | Fact-check editor, based on venue/authority and local-language evidence. | Stable / on change. | Preserve Spanish spelling and accents; resolve ambiguous or duplicate identities before publication. |
| `category` | Assigns one approved primary category. | Human editor-of-record. | On initial classification or approved reclassification. | Exactly one controlled category; taxonomy changes need owner approval and coordinated documentation. |
| `tags` | Gives useful secondary discovery labels. | Editorial author proposes; human editor approves controlled-value changes. | At creation and when the documented experience changes. | Use only approved controlled tags; do not use tags to imply an unsupported property. |
| `coordinates` | Identifies the precise entrance, start, or representative visitor point. | Intake/fact-check editor. | Stable / on change; recheck on pin or access changes. | Include point purpose, label, source, and check date. A broad town coordinate must not imply the location of every attraction. |
| `google_maps_url` | Preserves a supplied discovery/listing reference. | Intake editor. | On intake or link correction. | May identify a listing or route lead; it is not evidence for price, safety, opening, facilities, access, or suitability. |
| `external_ids` | Records known official or external identity references. | Intake/fact-check editor. | On identity change or newly verified identifier. | Use only when the identifier matches the destination; empty is preferable to a guessed identifier. |
| `municipality` | Names the administrative municipality. | Fact-check editor. | Stable / on boundary or correction. | Use an authoritative administrative name, not a nearby locality as a substitute. |
| `province` | Records the province. | Fact-check editor. | Stable / on correction. | Use the official province name. |
| `autonomous_community` | Records the autonomous community. | Fact-check editor. | Stable / on correction. | Use the official name. |
| `country` | States the country in guest-readable form. | Fact-check editor. | Stable / on correction. | Use `Spain` for destinations in Spain. |
| `created_at` | Preserves when the record began. | Record editor. | Once at creation. | Do not reset it during later edits. |
| `updated_at` | Shows when any record content last changed. | Current record editor. | At each saved substantive edit. | A prose-only edit must not be represented as a new fact-check date. |
| `last_verified` | Summarizes the latest completed factual review. | Fact-check editor records; reviewer checks. | After fact-check work. | Does not replace dates on individual claims or sources; do not advance it when only one unrelated claim was checked. |
| `last_reviewed_at` | Records the latest editorial review. | Independent reviewer or human editor. | At each substantive content review. | Keep distinct from factual verification. |
| `next_review_at` | Tells the team when another review is due. | Fact-check owner sets by volatility; human editor oversees overdue work. | After each review or volatility change. | Follow approved project intervals; overdue volatile information must not continue to appear current without recheck. |
| `review_decision` | Records the human decision and rationale. | Human editor-of-record. | On each approval/return decision. | Only the human editor-of-record can approve; record date, reviewer, decision, and material notes. |
| `redirects` | Preserves access to former slugs. | Record editor proposes; validation/release owner checks. | On approved slug change. | Include every prior public slug requiring redirection; do not reuse it for another destination. |

## Field specification: verified facts and evidence

Layer 1 facts describe what an appropriate source establishes. Every material public factual claim must have a matching evidence entry, even when the page groups several claims in one paragraph.

| Field | Purpose | Owner | Update frequency | Publication rules |
|---|---|---|---|---|
| `driving_time_from_casa_de_la_familia` | Gives a one-way estimate to a named visitor point. | Fact-check editor. | Volatile / short interval; recheck after route, access, or origin changes. | Name the exact destination point, route source, and date. State it as approximate. Drafts may remain unknown; public pages must not invent a time. |
| `age_groups` | Indicates which controlled age groups may be relevant to the activity. | Editorial author proposes from facts; reviewer and human editor assess. | At each review or when rules/route/experience change. | Use only controlled labels. Do not imply safety or guaranteed enjoyment. |
| `family_score` | Gives structured suitability guidance by audience group. | Editorial author proposes; independent reviewer and human editor review. | At each material experience, restriction, access, or audience change. | Keep as a reasoned assessment grounded in evidence; `unknown` is preferable to false precision. |
| `energy_level` | Summarizes the physical effort. | Editorial author proposes; reviewer checks against route/activity facts. | When route, activity, or access changes; review on schedule. | Use only approved values and explain the basis in guest-facing guidance where material. |
| `seasonality` | Summarizes the seasons relevant to the experience. | Fact-check editor for operation; editorial author for practical fit. | Seasonal / before season and after operating changes. | Do not use `All year` to conceal seasonal facilities or dates. State separate opening/service seasons. |
| `accessibility` | Describes mobility, sensory, route, and facility facts. | Fact-check editor gathers evidence; accessibility/suitability decisions escalated to human editor. | Volatile / short interval; event-triggered after a reported barrier or alteration. | Scope claims to exact entrance/route/facility. A general “accessible” label is not enough to assert every route or toilet works. Unknowns remain explicit. |
| `wheelchair_friendly` | Provides a derived summary of wheelchair suitability. | Editorial author proposes; reviewer/human editor confirm consistency with access details. | Whenever `accessibility` changes. | Must not overstate or conflict with the detailed access account; use unknown/partial when evidence is limited. |
| `parking` | Records availability, location, cost, restrictions, and walk distance. | Fact-check editor checks official venue/authority/parking sources. | Volatile / short interval; seasonal / before season if applicable. | Separate destination parking from nearby parking; give source/date and do not turn one visitor’s full-lot report into a general fact. |
| `transport_options` | Lists verified arrival alternatives and relevant stops. | Fact-check editor. | Volatile / short interval; recheck when services/timetables change. | Identify access point and current timetable source. Do not imply transport from Casa is practical without checking the full journey and last mile. |
| `booking_required` | States whether advance booking is required. | Fact-check editor checks current terms; human editor decides unresolved blocker status. | Volatile / short interval; before peak/seasonal periods where relevant. | Distinguish required, recommended, and optional booking. If requirement is unknown, do not guess “walk-ins welcome.” |
| `dog_friendly` | States formal dog access rules. | Fact-check editor checks current operator/authority policy. | Volatile / short interval and after rule changes. | Distinguish all areas from restricted areas and assistance animals; cite the applicable rule. |
| `toilets_available` | States whether toilets are available at the destination. | Fact-check editor. | Volatile / short interval; event-triggered for closures or renovation. | Distinguish on-site from nearby and accessible from general provision. Unknown is not “no.” |
| `food_available` | States whether food or drink is available on site. | Fact-check editor checks venue/authority. | Volatile / short interval; seasonal / before season when relevant. | Nearby restaurants do not satisfy “on-site.” State seasonal limits and distinguish a venue from nearby options. |
| `cost_level` | Gives an approved qualitative price tier for the core experience. | Fact-check editor supplies cost basis; editorial author proposes tier; human reviewer approves. | Volatile / short interval after price change. | Include the basis and date; separate core ticket/meal from parking, transport, food, and equipment. |
| `visit_information` | Holds factual opening, duration, booking lead time, validity, and cost-basis details. | Fact-check editor; editorial author labels any planning estimate separately. | Each subclaim follows its own volatility; hours/prices short interval, seasonal periods before season. | Separate operator-stated durations from editorial allowances. Add applicable dates; do not let one current subfield imply all others were checked. |
| `links` | Provides official site, booking, information, transport, and contact destinations. | Fact-check/record editor. | Check links during each scheduled review and after a reported change. | Use the responsible official link where available. A working URL does not prove its contents are current or that booking is mandatory. |
| `related_places` | Connects a guest to genuinely useful nearby or itinerary-related destinations. | Editorial author proposes; record/validation editor checks identity and relationship. | On nearby-place or itinerary change; reconsider at editorial review. | Use existing, verified place identities and an accurate relationship. Do not create an implied partnership, route, or inclusion. |
| `evidence` | Connects each fact to its supporting source and review history. | Fact-check editor; independent reviewer samples consequential claims. | Per claim, source check, or correction. | Record claim/field, source, source type, date checked, checker, confidence, and limits. Source confidence applies to that claim, not every claim from that source. |
| `review_issues` | Keeps unresolved facts, conflicts, and quality blockers visible with next action. | Current issue owner; human editor-of-record resolves high-impact disputes. | Create on discovery; update at every handoff; close only when resolved. | State severity, affected claims, responsible owner, and next action. Never remove an unresolved blocker merely to make the record appear complete. |
| `images` | Supplies destination imagery with rights, credit, and accessibility context. | Image contributor supplies source/permission details; rights reviewer owns rights approval; editor checks relevance and alt text. | On asset addition, permission change, withdrawal, or periodic rights review. | Publish only assets with approved documented rights. Use accurate, useful alt text; never treat an image as evidence of access, safety, facilities, or current conditions. |

### Nested field rules

The parent-field rule above applies to each nested field below. These details are called out separately because they carry distinct evidence, freshness, or publication implications.

| Field | Purpose | Owner | Update frequency | Publication rules |
|---|---|---|---|---|
| `coordinates.latitude`, `coordinates.longitude` | Place the selected visitor point on a map. | Intake/fact-check editor. | Stable / on point or access change. | WGS 84 coordinates must match the named point and purpose; retain source and check date. |
| `coordinates.purpose`, `coordinates.label` | Explain whether coordinates mark an entrance, trailhead, town centre, or representative point. | Intake/fact-check editor. | When selected point/scope changes. | State the point plainly; do not imply a representative town point is an entrance. |
| `coordinates.source`, `coordinates.checked_at` | Show how and when the coordinate was established. | Fact-check editor. | Whenever coordinates are rechecked or changed. | Identity/map sources may support location only, not visitor claims. |
| `accessibility.overall` | Summarizes known access information. | Fact-check editor; human editor reviews consequential statements. | Volatile / short interval and after access reports. | Must not be broader than the supporting details; use unknown when the route/facility is not established. |
| `accessibility.mobility.route` | Describes route surface, slope, steps, and relevant distance. | Fact-check editor. | Volatile / short interval; event-triggered. | Tie details to the exact route/area and evidence; never infer whole-site access from an entrance. |
| `accessibility.mobility.wheelchair_route` | Records whether a specific route is usable, not a general venue label. | Fact-check editor; human accessibility review. | Volatile / short interval and after reports/changes. | Use only the approved values; explain partial or unknown scope in the page. |
| `accessibility.mobility.facilities` | Records relevant mobility facilities such as lifts or adapted bathing equipment. | Fact-check editor. | Seasonal / before service season; after reported change. | State location and operating period; distinguish equipment availability from guaranteed use. |
| `accessibility.sensory.notes` | Identifies documented sensory conditions that affect planning. | Fact-check editor gathers; editorial author explains relevance. | On venue/experience change or credible report. | Avoid unsupported diagnoses or assumptions; keep advice specific and optional. |
| `accessibility.accessible_toilets` | States whether accessible toilets are verified. | Fact-check editor. | Volatile / short interval; on facility change. | Do not infer from general accessibility claims or an unlabeled toilet symbol. |
| `accessibility.source`, `accessibility.checked_at`, `accessibility.confidence` | Shows basis, freshness, and claim-specific certainty for access. | Fact-check editor; reviewer checks consequential evidence. | With each access claim/source check. | Confidence expresses evidence quality, not degree of accessibility. Apply only to the described scope. |
| `parking.availability`, `parking.location_type` | Identifies whether parking exists and whether it is onsite, nearby, street-based, absent, or unknown. | Fact-check editor. | Volatile / short interval; seasonal / before season if relevant. | Distinguish destination parking from nearby options; do not treat a guest report as universal availability. |
| `parking.cost` | States parking charge or discount. | Fact-check editor. | Volatile / short interval. | Give the current basis and date; if no reliable current price exists, say so rather than estimating. |
| `parking.restrictions`, `parking.walk_distance` | Helps guests assess vehicle limits and last-mile effort. | Fact-check editor. | Volatile / short interval and after access/route changes. | Identify which lot/point the restriction or distance describes; do not imply an accessible route unless checked. |
| `parking.source`, `parking.checked_at` | Supports the parking claim and records freshness. | Fact-check editor. | Every parking review. | Source must support the specific lot, rule, price, or walk—not just destination identity. |
| `transport_options.mode`, `stop/access_point`, `source`, `checked_at` | Describes a usable non-driving option and how current it is. | Fact-check editor. | Volatile / short interval; when route or timetable changes. | Identify the relevant stop and last mile. Link to current operator/authority timetable; check an entire Casa-to-place journey before recommending it. |
| `visit_information.schedule`, `valid_from`, `valid_until` | States opening/service schedule and the period it applies to. | Fact-check editor. | Volatile / short interval; seasonal / before season. | Distinguish opening hours from kitchen, lifeguard, bathing-assistance, or facility hours. Show exceptions and validity. |
| `visit_information.typical_duration` | Records an operator-stated visit average or duration where one exists. | Fact-check editor records sourced duration; editorial author records advice separately. | When experience/schedule changes or source is reviewed. | Attribute official averages; label planning allowances as editorial estimates. |
| `visit_information.booking_lead_time` | Records any published advance-booking window. | Fact-check editor. | Volatile / short interval. | Do not confuse a discount window with a booking requirement. |
| `visit_information.cost_basis`, `cost_checked_at` | Explains which price supports the cost tier and when it was checked. | Fact-check editor; editorial author confirms examples. | After any price/menu change. | State currency, ticket/order assumptions, party ages where relevant, and excluded extras. |
| `links.official_website`, `visitor_information`, `booking`, `transport`, `contact` | Directs guests to the appropriate current source or action. | Fact-check/record editor. | Check at each scheduled review and after reported failures. | Use null when unavailable; a booking URL does not establish that booking is compulsory. |
| `evidence.field`, `evidence.claim` | Names the record field and exact statement supported. | Fact-check editor. | Per claim or claim revision. | One entry must not silently support unrelated statements. Split claims when source scope differs. |
| `evidence.source_url`, `source_type` | Identifies the source and its role. | Fact-check editor. | Per new or changed source. | Classify accurately as official venue, government, official tourism, official transport, secondary, or maps identity; maps support identity/location only. |
| `evidence.checked_at`, `checked_by` | Establishes when and by whom the source was checked. | Fact-check editor. | Every source check. | Record actual check dates and checker; never backdate. |
| `evidence.confidence`, `notes` | Records evidence strength and limits for that precise claim. | Fact-check editor; reviewer challenges material uncertainty. | With each evidence assessment. | Use approved confidence values. Notes must disclose conflict, stale source, narrow scope, or interpretation limits. |
| `review_issues.code`, `severity`, `fields` | Classifies an issue and identifies affected claims. | Issue owner; human editor oversees blockers. | At issue creation and when severity/scope changes. | Use approved issue format and severity; a blocking issue cannot be hidden in narrative. |
| `review_issues.description`, `retryable`, `owner` | Explains the problem, whether another check may help, and who acts next. | Assigned issue owner; human editor assigns/escalates. | At each handoff/retry. | Include a concrete next action and named role/person; do not leave material conflicts ownerless. |
| `review_decision.reviewer`, `decision`, `date`, `notes` | Preserves accountable human approval or return reasoning. | Human editor-of-record. | At each formal review decision. | Record only a real human decision; agents cannot populate an approval to bypass the gate. |
| `images.asset_id`, `role`, `src` | Identifies the image asset, its page role, and location. | Rights/image owner; editor verifies fit. | On asset change or withdrawal. | Each asset must be uniquely identifiable and relevant to the destination. |
| `images.alt`, `caption` | Makes imagery understandable and accessible. | Editorial/image owner. | When image or context changes. | Alt text describes what matters in the image; do not add unshown amenities or search terms. |
| `images.source`, `rights`, `credit`, `rights_status` | Records origin, permission, attribution, and use eligibility. | Rights owner/reviewer. | At intake and on any rights/permission change or review. | Only approved rights may be used; pending/withdrawn assets are excluded. Credit as required by permission. |
| `images.width`, `height` | Records dimensions when known for the asset. | Image/editorial owner. | On asset replacement or when dimensions are established. | Record only known values; dimensions do not establish rights or image accuracy. |
| `related_places.id`, `relationship` | Points to another destination and explains its connection. | Editorial author proposes; validation editor confirms. | On destination or itinerary changes. | Reference a valid identity and approved relationship; do not imply an official partnership. |

### Claim-level governance details

The current evidence and issue fields do not by themselves distinguish the three knowledge layers or hold a full guest observation. The following governance details are required for any material statement or contribution used in the destination record. They are **content requirements**, not approved new schema fields.

| Claim detail | Purpose | Owner | Update frequency | Publication rules |
|---|---|---|---|---|
| Knowledge layer | Identifies whether the item is a verified fact, editorial recommendation, or guest observation. | Fact-check/editorial owner assigns; reviewer checks. | At creation and whenever its meaning changes. | One item belongs to one primary layer. Do not label an opinion as a fact or a guest report as an editor recommendation. |
| Exact statement | Preserves the claim or report in precise, reviewable language. | Fact-checker records facts; author records advice; guest supplies their observation. | Whenever claim is corrected or narrowed. | Split statements that need different sources, dates, scopes, or trust assessments. |
| Scope / applicability | Says which entrance, route segment, facility, date, season, party, or conditions the claim concerns. | Claim owner; fact-checker confirms factual scope. | Whenever source or applicability changes. | Do not generalize from one site area, day, visitor, or season to the whole destination. |
| Source or provenance | Connects a fact to its evidence, a recommendation to its rationale, or an observation to its contributor/context. | Fact-check/editorial owner; guest for original report. | Per source/contribution and on correction. | Preserve source URL/type and direct/secondhand status. Protect private contributor details. |
| Checked/observed date and validity | Shows when the information was verified or experienced and how long it may apply. | Fact-checker for check date; guest for observation date; editor sets validity/review date. | Each check or contribution; revise on new evidence. | Do not let record-level `last_verified` refresh an unchecked claim. Expired facts and old observations must be rechecked, marked historical, or removed from current prominence. |
| Claim owner | Identifies who is responsible for the next check or editorial decision. | Human editor-of-record assigns accountable role/person. | At assignment, handoff, or ownership change. | Every open material issue has one accountable owner; contributors are not made responsible for CalleMilano verification. |
| Trust basis | Explains why a claim merits its stated confidence or remains uncertain. | Fact-check/editorial reviewer. | At assessment and when evidence changes. | Assess responsibility, firsthand status, specificity, recency, and corroboration for this claim; do not assign trust by popularity or source label alone. |
| Publication treatment | Determines whether the item is stated, qualified, shown only as a report, held, historical, or excluded. | Human editor-of-record for material or disputed items; moderator for routine contribution moderation under policy. | At review and after each material conflict/correction. | The treatment must follow evidence and risk. Unresolved safety, operation, access, or suitability issues can block approval. |
| Conflict link and next action | Connects a disputed item to related claims and states what will resolve it. | Fact-checker creates; human editor owns high-impact resolution. | On conflict discovery and every investigation step. | Preserve all sides, record the next action and owner, and close only with a documented resolution or approved warning. |

## Field specification: editorial recommendations

Editorial recommendations are judgments in Layer 2, supported by but not interchangeable with Layer 1. Their owner must be visible in the handoff/review history, and their rationale should be understandable from the public page.

| Field or section | Purpose | Owner | Update frequency | Publication rules |
|---|---|---|---|---|
| `description_short` | Gives a concise, accurate guest-facing summary. | Editorial author; independent reviewer checks. | At each material content review or fact change. | Keep factual statements supported; avoid promotional claims; preserve the main suitability caveat. |
| `description_long` | Explains experience, limits, and practical decision details. | Editorial author; reviewer; human editor owns final judgment. | At each material fact, access, audience, or seasonal change. | Separate facts from advice in wording; do not duplicate structured facts inconsistently. |
| Quick verdict | States who may benefit, time commitment, and the main caveat. | Editorial author; reviewer challenges it. | Revisit whenever a supporting fact or recommendation changes. | Advice must be conditional and reasoned, not a guarantee or a general “family-friendly” badge. |
| Why visit / experience | Explains the actual activity or meal. | Fact-checker supplies facts; editorial author frames guest value. | On experience change; otherwise scheduled review. | Claims about what is offered require evidence; recommendations about why it may suit a guest are labeled as advice. |
| Who may enjoy it / choose something else | Helps guests compare the destination with their own party and constraints. | Editorial author; human reviewer reviews suitability. | On activity, rules, access, effort, or season change. | Use concrete attributes and controlled audience groups in structured data. Avoid guarantees, stereotypes, or safety assurances. |
| Editorial visit-time allowance | Helps a guest plan beyond an operator’s average or minimum. | Editorial author, reviewed independently. | When route, activity, or service pattern changes. | Label it as an editorial estimate and state what it includes; do not overwrite an operator-stated duration. |
| Party-cost example | Makes a likely spend understandable. | Fact-checker verifies item prices; editorial author chooses explicit order assumptions. | After any price/menu change. | Show party composition, selected items, arithmetic, exclusions, and checked date. Never call an incomplete subtotal a complete meal price. |
| Weather/season advice | Turns verified exposure and seasonal facts into practical planning guidance. | Editorial author based on verified climate/season rules; reviewer checks. | Seasonal / before season and after warnings or operating change. | Date-specific alerts remain linked to live authorities; no generic advice may override an active closure or warning. |
| `seo_title` | Gives the page a unique, accurate search title. | Editorial/validation owner. | When public name/scope changes; uniqueness check at each release. | Must not add unsupported claims or imply a wider scope than the page covers. |
| `seo_description` | Summarizes the destination accurately for discovery. | Editorial/validation owner. | With meaningful page changes; uniqueness check at each release. | Must preserve caveats where their omission would mislead; no unsupported superlatives. |

Content-type-specific sections are added only when relevant: attraction rules, town scope and route, beach conditions and services, restaurant menu/booking/access, or nature-route distance/effort/closures. Each section follows the same fact/recommendation separation.

## Field specification: guest contributions and trust

Guest contributions add lived experience without becoming an unofficial source of permanent policy. The current schema does not define a dedicated contribution section; this specification therefore treats the following as required **governance information** for any report considered for public use, not as an approved schema change.

| Contribution field | Purpose | Owner | Update frequency | Publication rules |
|---|---|---|---|---|
| Observation | Records what the visitor personally saw or experienced. | Contributing guest; moderator checks clarity. | Per contribution. | Keep first person, specific, and limited to the reported event. Distinguish firsthand from hearsay. |
| Observed date/time | Establishes when the report applied. | Contributing guest; moderator requests clarification if material. | Per contribution. | Required for operational, access, safety, crowding, or seasonal reports. Do not present an undated report as recent. |
| Place/route scope | Identifies the exact entrance, beach section, facility, or trail segment. | Contributing guest; moderator verifies understandable scope. | Per contribution. | Narrow scope; do not turn a report about one point into a whole-destination claim. |
| Visit context | Adds optional relevant context such as season, party needs, weather, or visit type. | Guest chooses what to share; moderator limits collection to useful context. | Per contribution. | Ask only for information that helps interpret the report; do not require sensitive personal details. |
| First-hand status | Distinguishes direct experience from hearsay. | Guest declares; moderator labels uncertainty. | Per contribution. | Do not present hearsay as a firsthand observation or verified fact. |
| Attribution/consent | Establishes whether and how the contribution may be displayed. | Guest grants the requested consent; moderator safeguards it. | Per contribution; revise/remove on valid request. | Avoid unnecessary identity details. Publish names only with clear permission and a guest benefit. |
| Moderation state | Shows whether a report is pending, accepted as a report, needs clarification, or rejected. | Editorial moderator. | At submission and moderation changes. | A moderated report is not thereby fact-verified. Explain removal/limits consistently and do not publish abuse or private information. |
| Contribution freshness | Prevents old reports appearing current. | Editorial moderator. | Reassess per project freshness policy and when a newer report arrives. | Show the date. Mark historical reports as such; do not let old praise or warnings imply current conditions. |
| Report trust note | Explains the report’s evidential limits. | Moderator/fact-check editor. | When accepted, clarified, or checked against another source. | Trust attaches to what one visitor experienced, not to a general policy or all future visits. Popularity/likes do not raise evidential confidence. |

Do not invent community reports for an example, seed a place with fabricated praise, or conceal material negative observations. Where contribution volume is small, say so rather than implying consensus.

## Field specification: conflict and decision history

Conflict information preserves disagreement until it is resolved and prevents one layer from silently overwriting another.

| Conflict field | Purpose | Owner | Update frequency | Publication rules |
|---|---|---|---|---|
| Conflicting claims | States the exact incompatible statements. | Fact-check editor creates; human editor accountable for resolution. | On each new source/report; update at each investigation step. | Preserve each statement with its source or reporter and date; do not blend them into a false average. |
| Conflict scope | Identifies differences in venue, access point, date, season, policy, or actual observation. | Fact-check editor. | During initial triage and whenever scope is clarified. | Resolve apparent conflicts of scope before treating them as direct contradictions. |
| Trust assessment | Records relevance, responsibility, recency, specificity, and evidence limits for each claim. | Fact-check editor; human editor reviews high-impact differences. | During each substantive check. | Do not assign a global source ranking; judge sources for the specific claim. |
| Guest-facing uncertainty | Gives guests the precise caveat and next step. | Editorial author drafts; human editor approves material warnings. | While conflict is open; revise as facts change. | Say what each side reports and what is unknown. Make safety/wasted-trip implications prominent and proportionate. |
| Interim recommendation | States whether the page is still recommendable while the conflict is open. | Editorial author proposes; human editor decides. | At conflict triage and each new finding. | Pause or qualify the recommendation where uncertainty could make the visit unsafe, unavailable, or materially unsuitable. |
| Next action and owner | Makes clear who will contact/check what. | Assigned issue owner; human editor owns escalation. | At every handoff or retry. | No unresolved material conflict may be left without a named owner and next action. |
| Resolution and rationale | Records what settled the conflict and why one claim was accepted, narrowed, or rejected. | Human editor-of-record for material disputes; fact-checker documents sources. | Once resolved and whenever reopened. | Preserve the decision and evidence. Reopen if a new credible contradiction appears. |

## Trust labels and public language

Use the knowledge model’s distinctions consistently:

- **Verified fact:** “The venue’s current visitor page lists…” Include the source and check date when the claim can change.
- **Editorial recommendation:** “We recommend…” or “This may suit…” Give the concrete reason and caveat.
- **Guest observation:** “A visitor reported on [date]…” Keep it attributed, time-bound, and scoped.
- **Verification required:** Use only when a material point remains genuinely unsettled. State the missing confirmation and a practical next step.
- **Unknown / not listed / not applicable:** Keep these meanings distinct. The absence of a claim is not evidence that a facility, rule, or problem does not exist.

Trust is qualitative and claim-specific. “Official,” “recent,” or “many guests said” must not be used as a substitute for claim-level reasoning. Community volume can prioritize a check, but does not convert opinions into facts.

## Record-level publication gate

A record may be considered for human approval only when:

1. Identity, scope, category, and named visitor point are clear.
2. Material public facts have appropriate evidence, a source date, and an accountable owner.
3. Recommendations are distinguishable from facts and supported by their stated rationale.
4. Guest observations are dated, scoped, moderated, and clearly attributed; unverified reports are not passed off as settled facts.
5. Material conflicts are resolved or presented with an approved, proportionate interim warning; conflicts affecting safety, access, operation, or whether the visit is worthwhile remain blockers when unresolved.
6. Required content-type sections and checklist gates are complete, validation passes, and the human editor-of-record records a decision.

Publication is not a claim that every fact is permanent. It means the record is accurate to its stated sources, scope, and review date, and that uncertainty is disclosed at the point where it affects a guest’s decision.

## Example: BIOPARC Fuengirola

The current [BIOPARC guest page](published/bioparc-fuengirola.md) illustrates a record with facts, advice, and remaining detail questions. The examples below show how those statements should be maintained; the hypothetical guest observation is not an actual report.

| Layer | Example record content | Treatment |
|---|---|---|
| Verified fact | BIOPARC’s visitor information says it opens daily at 10:00, closing varies by season, and average visits last about three hours. It lists ticket rates and says the park is fully accessible. | Separate evidence entries for opening, duration, price, and the venue’s general accessibility statement; each with official source and check date. Do not let the broad access statement imply that every route or toilet was specifically checked. |
| Editorial recommendation | “A good half-day choice for families interested in animals; allow breaks, and do not plan around a guaranteed sighting of a particular animal.” | Tie the advice to the stated visit duration and official note that animals may be out of view; keep it framed as guidance. |
| Guest observation (hypothetical) | “On [visit date], our wheelchair user could use the entrance but found the route to [named area] too steep.” | Attribute to the visitor, retain the exact date/area and their firsthand scope, and request the venue’s current route details. Do not generalize this to the entire park or immediately replace the official general statement. |
| Possible conflict | General operator statement “fully accessible” versus a specific dated report about a steep route. | Preserve both; explain that the statement is broad and the report is route-specific. Ask BIOPARC about the named route and access alternative. Keep route-level accessibility unresolved until checked. |

## Example: Restaurante Sheriff

The current [Restaurante Sheriff guest page](published/restaurante-sheriff.md) contains an actual source conflict as checked on 4 October 2026.

| Layer | Example record content | Treatment |
|---|---|---|
| Verified fact | The restaurant’s own site lists Tuesday–Sunday service and kitchen hours; Mijas Tourism’s listing says “Cerrado desde el 28 de febrero.” | Store these as two separate sourced claims with dates and source roles. The restaurant controls its current service schedule, while the municipal listing is a contradictory current directory notice. Neither statement should be silently deleted. |
| Verified fact | The operator’s menu lists item prices and children’s dishes; an example of two adult and two child hamburgers totals €47.60 before drinks/extras. | Preserve the checked menu prices and the explicit order assumptions. Recalculate after any menu update; do not describe the subtotal as a full family meal cost. |
| Editorial recommendation | “A potentially useful family meal for groups wanting a broad menu, but call before setting out until current operation is confirmed.” | Link the family fit to the menu facts; make the unresolved operating status prominent because an incorrect assumption could waste the trip. |
| Guest observation (hypothetical) | A guest later reports eating there on a named date, despite the municipal closure notice. | Treat it as evidence of one visit on that date, not proof of regular current hours. Ask the venue and municipal tourism office to reconcile their information. |
| Current decision | Whether the restaurant is operating now remains unresolved. | Keep **Verification required** prominent and do not describe the venue as definitively open. The page should not receive approval until the human editor-of-record accepts a current operating confirmation or decides, with rationale, that the qualified page is safe and useful to publish. |

## Long-term maintenance principles

- Maintain facts, advice, observations, and conflicts as separate knowledge, even when they concern the same topic.
- Prefer precise, low-maintenance claims over broad statements that are difficult to verify.
- Reuse the approved five content types, but let the destination’s real decision needs determine which optional sections appear.
- Treat every contribution as both community knowledge and a possible fact-check lead; never make contributors responsible for final verification.
- Recheck volatile claims on the project’s approved schedule and after credible reports. A record-level “last verified” date does not refresh every claim automatically.
- Keep the reason for material editorial decisions and corrections so future editors can understand why a statement or warning exists.
- Protect guest privacy and source attribution; retain only contribution context needed to assess usefulness and trust.
- Remove, narrow, or qualify content when its evidence expires. A smaller trustworthy guide is more useful than a larger catalogue of stale assertions.
