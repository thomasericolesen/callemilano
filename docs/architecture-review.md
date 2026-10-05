# CalleMilano architecture review

## Scope

This review covers `AGENTS.md`, `docs/place-schema.md`, `docs/maps-import-agent-spec.md`, and `docs/multi-agent-workflow.md`. It assesses their consistency and readiness to support a growing family travel guide. No source documents were changed as part of this review.

## Summary

The architecture has a useful editorial foundation: a controlled vocabulary, explicit Google Maps sourcing limits, source verification expectations, family-oriented fields, and a human review boundary. Its main weaknesses are inconsistent instructions between documents, incomplete lifecycle and provenance data, and a multi-agent process that describes handoffs but does not yet provide operational controls for many records.

The issues below should be resolved before automating or importing records at scale.

## 1. Missing fields

### High priority

- **Record lifecycle:** The workflow and import spec require draft status, but `place-schema.md` has no `status` field. Add a defined lifecycle enum such as `draft`, `needs_fact_check`, `needs_editorial_review`, `approved`, `published`, `archived`, with clear transitions and permitted values.
- **Provenance and audit trail:** The schema has one `last_verified` date and some nested source fields, but no record-level creation/update dates, per-claim source references, verification owner, or change history. Distinguish source facts from editorial judgments in a machine-readable way.
- **Place identity and administration:** `municipality` and `province` exist, but the schema lacks region/autonomous community and country fields even though the ID embeds region and the guide covers all Spain. Define standardized administrative names and codes where useful.
- **Contact and visit links:** No canonical official website, booking URL, phone, public transport guidance, or visitor-information link is modeled. These are useful family planning data and valuable provenance links.
- **Opening and visit planning:** Seasonality is broad, but there is no optional hours/schedule field, typical visit duration, reservation lead time, or visit date/season of validity. Avoid requiring volatile details when unavailable, but give them a defined structure.
- **Accessibility detail:** A summary and details object plus `wheelchair_friendly` are redundant and underdefined. The schema should separately describe route/access, mobility features, sensory access, accessible toilets, and confidence/source, or explicitly scope these fields.
- **Parking and transport:** A generic parking summary omits location, type, capacity, cost, restrictions, and walking distance. There is no transit or walking alternative even though some destinations may be better reached without driving.
- **Cost semantics:** `cost_level` is a broad euro-symbol estimate without a defined party size, date, included items, or basis. Add a price range or basis and check date, or make clear that the symbols are qualitative and not comparable across place types.
- **Image role:** Image metadata lacks an explicit role (cover/gallery/map), focal subject, and source asset identifier. Alt text is present, but image provenance and rights may change independently of the place record.
- **Record status for uncertainty:** The phrase “complete schema-compliant record” conflicts with examples that use `null`, `Not yet verified`, or unverified values. Define which fields may be unresolved and which block draft creation versus publication.

### Additional useful fields

- Stable external place identifiers beyond the Maps URL, such as an official venue ID or Maps Place ID when available and appropriate.
- `canonical_slug` or an explicit rule connecting the stable ID to the web URL.
- Coordinates' pin target/type and verification source; destination-level towns need a consistent representative-point policy.
- Optional nearby places or itinerary relationships, modeled as IDs rather than copied data.
- Last review date and next review date for volatile records.

## 2. Missing workflows

- **Intake and queue management:** The import spec accepts a single place but does not define bulk Google Maps saved-list exports, deduplication before research, batch progress, retries, or a queue of unresolved links.
- **Clarification loop:** Ambiguous places may trigger a user question, but there is no defined waiting, timeout, or resume behavior, nor a standard way to record the clarification in the record.
- **Field-level verification:** Agents are told to source claims, but there is no claim-to-source matrix or required evidence format. “Source notes” at the bottom may not identify which source supports which field.
- **Review and approval:** The workflow ends with a human reviewer but does not define reviewer roles, approval criteria, sign-off recording, or how requested changes re-enter the pipeline.
- **Publication and update lifecycle:** Publishing is out of scope, but there is no separate documented handoff to a publishing process, no archive/closure process, and no cadence for rechecking stale facts.
- **Regression validation:** No workflow checks controlled values, required keys, duplicate IDs, YAML validity, broken links, or duplicates in SEO fields before handing off.
- **Image intake and rights review:** The workflow can omit images, but lacks a process for receiving approved assets, documenting permissions, maintaining credits, and revisiting expired or withdrawn rights.
- **Agent disagreement resolution:** Handoff rules return issues to a prior agent, but do not set a final authority for disputed classifications, confidence thresholds, or irreconcilable sources.
- **Failure reporting:** The import spec and agent workflow describe errors independently; standard result codes, issue severity, retry behavior, and human escalation are missing.

## 3. Scalability issues

- **Conflicting storage conventions:** `AGENTS.md` says structured place records belong in `data/`; the import spec and multi-agent workflow direct records to `docs/places/`. Choose one canonical data location and make examples, prompts, and workflow agree.
- **Category vocabulary mismatch:** `AGENTS.md` uses `Cities`; `place-schema.md` uses `City`. This can create invalid filters and inconsistent records.
- **Unversioned schema:** The workflow asks agents to acknowledge the schema version, but the schema has no version or migration policy. Changes to fields and enums could silently invalidate older records.
- **Unstable ID allocation:** The ID pattern includes a place name and a number, but no registry, number-assignment rule, collision policy, or rename policy is defined. Parallel imports can produce duplicate IDs.
- **Markdown as both content and data:** YAML inside Markdown is workable for a small project but requires parsing and validation conventions. Decide whether Markdown is canonical or generated from structured data; do not let both become competing sources of truth.
- **No index or query model:** There is no canonical place index/catalog for finding existing records, checking duplicate IDs, managing category/tag counts, or generating website feeds.
- **Serial handoffs multiply latency:** Four strictly sequential agents create a long path for simple places. Define which fact checks can run in parallel and which items merit all four agents, with risk-based review for low-risk records.
- **No freshness prioritization:** `last_verified` alone does not enable a scalable review queue. Opening hours, access, prices, and seasonal operations change at different rates.
- **Shared-file concurrency:** All agents are expected to edit the same draft in place. There is no lock, patch ownership, version check, or conflict resolution when agents run concurrently.
- **Taxonomy growth is unmanaged:** Tags and categories are controlled, but there is no owner, proposal process, deprecation/alias policy, or mechanism to avoid near-duplicate tags.

## 4. SEO issues

- **No technical SEO contract:** The schema has title and description but omits canonical URL, slug, indexability/robots, Open Graph/social metadata, structured-data mapping, and redirect rules when a place URL changes.
- **No duplicate-target policy:** The agent is told to make metadata unique, but there is no site-wide check for duplicate titles/descriptions, duplicate destinations, or overlapping town/place pages.
- **No localization strategy:** The project includes Spanish place names but does not define publication language, localized fields, translated slugs, `hreflang`, or whether there will be Spanish and English pages.
- **No measurable editorial guidance:** Title and description length are intentionally flexible; add recommended ranges and display previews while allowing search engines to truncate them. Define whether the place name, municipality, and province should appear consistently.
- **Search intent and page scope:** No rules distinguish a destination guide from a specific venue page. Broad city pages can compete with separate pages for beaches, restaurants, or attractions unless internal relationships and canonical strategy are defined.
- **Image search metadata:** Alt text is addressed, but no image filename, dimensions/responsive variants, caption policy, or performance requirements are defined. Alt text should remain accessibility-first and should not be treated as a ranking field.
- **No internal linking model:** There are no related-place, nearby-place, category landing page, or itinerary links to support navigation and topical structure.
- **No structured data governance:** Define whether and when to emit appropriate schema.org types (such as TouristAttraction, Restaurant, or Place), and ensure markup only reflects visible, verified page content.

## 5. Content governance issues

- **Contradictory audience definitions:** `AGENTS.md` examples mention toddlers, children, teens, or all ages, while the schema defines fixed age bands and separate family scores. Make the schema vocabulary authoritative everywhere.
- **Status and authority are undefined:** There is no named owner for taxonomy, final editorial approval, factual dispute resolution, schema changes, or emergency corrections.
- **Unverified examples may be mistaken for facts:** The Nerja and other example records contain ratings, prices, amenities, or values marked unknown without a consistent example-only/draft status in the schema. Explicitly label examples as non-publishable and avoid assigning unsupported values as if researched.
- **Evidence standard is vague:** “Official and authoritative” is a useful principle, but no minimum source quality, evidence granularity, confidence level, or acceptable exception policy exists.
- **Source rights and retention:** Maps content reuse is restricted in principle, but the project lacks a written source-data policy covering attribution, image licensing, link retention, personal data, and terms of use.
- **Review cadence is missing:** Define recheck intervals by field volatility and a workflow for corrections, closures, seasonal reopening, and stale data.
- **Accessibility and suitability claims need tighter review:** `wheelchair_friendly` and family scores are consequential, but there is no minimum evidence standard, qualified reviewer expectation, or rule for phrasing uncertain conditions.
- **No correction channel:** Readers or place owners need a defined way to report inaccurate details, and the project needs an owner and response target for those reports.
- **Language and tone governance:** Clear natural language is requested, but there is no defined voice, spelling convention, units/date style, translation review, or policy for local names and Catalan/Andalusian variants.

## Recommended order of work

1. Reconcile storage paths and controlled vocabulary across `AGENTS.md`, schema, examples, and agent documents.
2. Define schema lifecycle/status, provenance, timestamps, and which missing values are allowed at each status.
3. Add schema and content validation plus ID allocation and duplicate detection.
4. Establish review ownership, evidence standards, accessibility review, and freshness/maintenance rules.
5. Define SEO URL, localization, canonical, structured-data, and internal-link policies.
6. Decide whether Markdown/YAML remains the source of truth and document bulk intake and concurrent editing behavior.

## Overall assessment

The current design is suitable as an editorial prototype and for a small set of manually reviewed examples. It is not yet operationally consistent or sufficiently governed for bulk imports, automated publication, or a large multi-language catalog. Resolving the storage, taxonomy, status, provenance, and review gaps will provide the strongest foundation for growth.
