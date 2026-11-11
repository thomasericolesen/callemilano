# Pilot review: five place records

**Scope:** Frigiliana, Ronda, Marbella Old Town, Selwo Aventura, and Zahara de la Sierra, reviewed against `docs/place-schema.md` version 1.0.0. This is a content and schema review of the current drafts; it does not independently re-verify destination facts.

## Summary

No clear hard schema violations were found in the five records. Their core fields and controlled values follow the schema, and unresolved values are generally marked as unknown or null with review issues. They are appropriately marked `needs_fact_check`.

The main pilot weaknesses are inconsistent interpretation of tags and SEO, uncertainty about the scope of place-level fields, and subjective values that are difficult to support consistently. The records should remain drafts until their open fact-check issues—especially driving times, visit duration, facilities, and family ratings—are resolved.

## Schema and evidence

- **No obvious field-name or enum violations.** The category, energy, season, accessibility, and other controlled values appear to use the schema’s allowed values. The records include the required core content and source references.
- **Open values are mostly handled as drafts should handle them.** Driving time is null in every record; several facilities and accessibility values are unknown. These are surfaced in review issues rather than presented as verified facts.
- **Evidence coverage is uneven.** Some sources support destination identity or one attraction but are also used to justify broad tags, seasonality, facilities, or suitability. Review each claim against a source that directly supports that field; explicitly label editorial estimates as estimates.
- **The Maps input is not consistently an imported saved-place URL.** The records use Maps lookup links and note the limitation. Confirm the exact saved place and representative pin before treating coordinates or routing as final, particularly for large or multi-site destinations.
- **`last_verified` needs a clearer meaning.** It is populated while records are still `needs_fact_check` and contain unresolved claims. Distinguish the date a source was checked from the date the complete record was verified, or define explicitly that this date can represent partial checks.
- **Draft-state fields are not violations.** Null review decision/review dates and empty image arrays are acceptable for drafts under the current schema. No image metadata can be reviewed until images are added.

## Tag consistency

- **Duration tags are not backed by a consistent duration field.** Frigiliana and Marbella Old Town have `Half day`; Ronda and Selwo Aventura have `Full day`. `typical_duration` is null in all four, and the tags are called provisional. Define the visit scope and populate a duration range before using these tags as filters.
- **`Nature` has an unclear inclusion rule.** It appears for Ronda, Selwo Aventura, and Zahara de la Sierra, but not for the mountain setting of Frigiliana. Specify whether this tag means a natural attraction is a core visit, rather than merely describing the surrounding landscape.
- **`Museum` coverage may depend on inconsistent place scope.** It appears on Marbella Old Town, but not on the broader Ronda or Frigiliana city records. Decide whether a tag describes a core feature of the named place or any attraction within its municipality; apply that rule consistently.
- **`Viewpoint` use is plausible but needs a threshold.** It is used for Frigiliana, Ronda, and Zahara de la Sierra, but not Marbella Old Town. State whether a viewpoint must be a named/primary attraction to qualify.
- **`Restaurant` on Marbella Old Town may describe amenities rather than the core experience.** Clarify whether this tag means the place itself is a restaurant or that visitors can find restaurants there. The latter could be more useful as a separate amenity/filter concept.
- **Seasonal tags and seasonality fields can be confused.** Make clear whether tags such as `Summer` describe the best season, operating availability, or weather suitability. Zahara omits summer while the other towns list all seasons; Selwo omits winter. Record a consistent rationale for each.

## SEO consistency

- **Titles use different patterns.** Frigiliana includes “Andalusia”; Ronda includes “Málaga”; Marbella Old Town has no province; Selwo uses “Estepona”; Zahara omits “Cádiz.” Adopt a title convention such as place name plus province and one verified distinguishing feature, with exceptions for recognizable brands.
- **Descriptions repeat a generic planning warning.** Several ask visitors to check access, parking, or facilities. Replace boilerplate with specific, verified visitor value and use a warning only where a current uncertainty materially affects planning.
- **Family intent is uneven.** Frigiliana, Ronda, and Selwo explicitly mention families, while Marbella Old Town and Zahara do not. Set a consistent editorial rule for family language and avoid implying suitability beyond the evidence.
- **Some title and description wording is broad or duplicative.** Selwo’s “Family Animal and Adventure Park” repeats the adventure idea in its name; other records repeat the same landmark list across the title and description. Give each field a distinct purpose: title for concise identification/search intent, description for a useful reason to visit.
- **SEO constraints are unspecified.** The schema does not set length targets, truncation guidance, or a rule for uniqueness across records. Define these in the SEO guidance and review titles/descriptions together once the full place set exists. The five current titles are not exact duplicates.

## Duplicated concepts and scope overlap

- **Duration is represented twice.** `Half day`/`Full day` tags overlap `visit_information.typical_duration`. Make duration a structured value and derive its display/filter tag from that value.
- **Wheelchair suitability is represented twice.** The top-level `wheelchair_friendly` value overlaps detailed mobility/accessibility information. Treat the summary as derived from the detailed accessibility record, with a documented mapping, so the two cannot drift.
- **Age groups and family ratings can be mistaken for the same measure.** Define age groups as the audiences for whom a visit is broadly suitable, and ratings as degree of suitability. Avoid inferring suitability from ticket-price age bands.
- **Evidence is repeated across fields.** Coordinates, source ledgers, source notes, and place links can point to the same URLs. Keep one canonical source record and refer to it elsewhere where the format permits; otherwise establish which copy is authoritative.
- **Place and attraction scopes differ.** A town record can include many museums, restaurants, routes, or access conditions. State whether amenities and tags cover the named core place, the selected Maps pin, or the wider municipality.

## Fields that are difficult to populate reliably

- **Driving time from Casa de la Familia:** currently null in every record. A reproducible value needs a destination pin, route mode, routing source, and a policy for traffic/date variability. Consider storing an approximate range and the check date rather than presenting one duration as stable.
- **Accessibility and facilities:** wheelchair route, accessible toilets, parking, toilets, food, and dog policy can differ by entrance, attraction, or operator and change over time. Record the scope, source, and verification date; retain `unknown` when the evidence is insufficient.
- **Town-level `cost_level`:** “free” can describe entry to public streets while museums, transport, food, or attractions cost money. Define a representative core visit or use a more precise cost breakdown. Selwo’s price tier also needs an as-of date and a rule for dynamic “from” prices.
- **Age suitability, family ratings, energy, and best season:** these are partly editorial judgments. Provide rating criteria and evidence expectations, distinguish physical effort from visit length, and label estimates until reviewed. The pilot records themselves note these values as provisional.
- **Representative coordinates:** a single coordinate for a town or large park may point to a square, entrance, or unrelated access point. Define the pin-selection rule and preserve the original Maps place identity separately where possible.
- **Verification dates:** a single `last_verified` date is difficult to maintain when fields are checked at different times. A per-source or per-field checked date is more actionable for volatile claims such as opening schedules, prices, transport, and access.

## Recommended follow-up order

1. Define place scope and representative-pin rules, plus what amenity fields mean for town-scale records.
2. Define duration and tag rules; resolve the provisional duration and seasonal tags in these drafts.
3. Set evidence and review criteria for subjective ratings and volatile facilities, routing, and prices.
4. Clarify verification-date semantics and the relationship between summary fields and detailed accessibility data.
5. Standardize SEO title/description guidance and revise the five records together after fact-checking.
