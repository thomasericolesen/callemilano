# Destination metadata roadmap

## Basis and assumptions

This roadmap uses the 30 destinations in `data/destination-metadata.csv` and the field coverage and confidence notes in `docs/enriched-place-metadata.csv`, interpreted alongside `docs/v2-vs-v3-analysis.md`. The automation percentages are planning estimates for this current mixed set of destinations, not measured completion rates. They mean “could be populated automatically from a sufficiently clear source and then pass a basic evidence check”; they do not mean publication-ready without review.

“Recommendation impact” ranks each attribute’s likely ability to change which destinations suit different groups. “Ease” ranks how readily reliable evidence is available across these destination types. “Automation” ranks the share likely to be collected and normalized with limited human research. Effort estimates cover an initial collection and quality-control capability for all 30 places; they exclude schema approval and extensive source-access negotiations.

Google Maps can help resolve identity and locate candidate information, but under project source rules it cannot establish accessibility, safety, facilities, opening, or family suitability. Tripadvisor is a secondary lead only; material claims require confirmation from an official or otherwise responsible source. Where no reliable source exists, retain unknown and route the field to review.

## Ranked fields

| Field | Recommendation impact rank | Ease of reliable data rank | Automation rank | Estimated automatically populated | Likely sources | Initial implementation effort |
|---|---:|---:|---:|---:|---|---|
| Mobility access profile: step-free route, surface, gradients, stairs, and distance | 1 | 8 | 8 | 20% | Official venue access pages; municipal accessibility guides; park or transport authority pages; manual review | High — 8–12 working days |
| Age-group suitability with evidence-based reasons | 2 | 10 | 10 | 5% | Official age restrictions and activity descriptions; park or attraction guidance; manual editorial review | High — 10–15 working days |
| Physical effort and route difficulty: distance, elevation, surface, and duration | 3 | 4 | 4 | 40% | Official route guides, park authorities, municipal hiking pages, published GPX/route notes; manual review | Medium — 5–8 working days |
| Stroller suitability: steps, surface, ramps, narrow sections, and route continuity | 4 | 9 | 9 | 15% | Official access information; venue visitor guidance; municipal route guides; manual review | High — 7–10 working days |
| Weather exposure and protection: outdoor exposure, shelter, heat or wind sensitivity, and closures | 5 | 6 | 5 | 35% | Park and venue notices; official visitor guidance; municipal beach/route pages; manual review | Medium — 4–7 working days |
| Toilets: availability, accessible facilities, and baby changing | 6 | 2 | 2 | 55% | Official venue facilities pages; municipal or park facility listings; manual confirmation | Low–medium — 3–5 working days |
| Shade and heat relief: reliable shade on the visitor route or activity area | 7 | 10 | 7 | 20% | Official venue/park descriptions where explicit; manual site or route review | Medium — 4–7 working days |
| Parking difficulty and entrance distance: location, restrictions, capacity cues, and accessible spaces | 8 | 5 | 6 | 35% | Municipal parking pages; venue directions; park authority notices; manual review. Maps may identify candidate lots, not establish access or availability | Medium — 4–7 working days |
| On-site food and drink: whether available at the destination, visitor area, or not at all | 9 | 3 | 3 | 50% | Official venue, market, park, or municipal pages; venue menus; manual check for “on-site” versus merely nearby | Low–medium — 3–5 working days |
| Booking and access constraints: advance booking, timed entry, age limits, seasonal closure, or restricted access | 10 | 1 | 1 | 65% | Official booking pages; venue notices; park and heritage authority access rules | Low — 2–4 working days |

Rank 1 is the highest impact, easiest reliable sourcing, or greatest automation opportunity, respectively. Ease and automation ranks are not the same: booking rules are often easy to find and automate, while age suitability has high recommendation value but requires judgement.

## Why these fields rank this way

- The V2/V3 run changed the top recommendation for 13 of 20 groups, but most changes clustered around a few destinations with more populated metadata. That indicates evidence coverage is currently driving some ranking changes.
- Mobility, age suitability, route effort, and stroller access can rule a destination in or out for a meaningful subset of groups. They have high decision impact but are difficult to infer safely from general listings.
- Booking constraints, toilets, and food are relatively easy to find on official pages. They improve practical recommendations, though they are less likely on their own to distinguish personas.
- Shade, parking difficulty, and weather exposure often require route-specific or place-specific interpretation. A generic listing rarely supports a dependable answer.
- Existing `destination-metadata.csv` already has coarse cohort scores, energy, duration, drive time, season, and weather dependence. New collection should add evidence and detail to those concepts rather than create duplicate versions of the same values.

## Recommended first three fields

1. **Booking and access constraints.** Start here because official sources commonly publish these details, the current destination mix includes ticketed attractions and controlled-access natural sites, and the result is straightforward to verify. Capture timed entry, advance reservation, age limits, seasonal access, and closures as distinct facts.
2. **Toilets and key visitor facilities.** Collect toilet availability, accessible toilets, and baby changing separately. The enriched file currently has confirmed toilet information for only 5 of 30 destinations; official amenity pages often make this a practical, low-effort improvement.
3. **Physical effort and route difficulty.** Add route distance, elevation, surface, stairs, and stated difficulty where applicable. This is more useful than a single generic energy label for families, active groups, and seniors, and official trail authorities frequently publish the necessary measurements.

Begin mobility and age-suitability research in parallel as a high-priority manual review stream. Their recommendation impact is high, but automating them before there is consistent source coverage and editorial criteria would create unjustified confidence. Use Google Maps and Tripadvisor only to find leads; do not use them as final evidence for these fields.

## Automation guardrails

- Store source URL, supported field, check date, and confidence with each populated value.
- Preserve “unknown” when an official or responsible source does not answer the question.
- Do not infer wheelchair or stroller suitability from a destination type, photograph, or generic “accessible” label.
- Treat seasonal services, booking rules, closures, and opening arrangements as volatile and recheck them on the project review schedule.
- Keep editorial suitability judgements separate from official facts and require human review before they are used as strong recommendation signals.
