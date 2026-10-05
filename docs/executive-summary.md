# Executive summary: guest-focused schema gaps

**Audience:** Guests staying at Casa de la Familia in Cerros del Águila.  
**Basis:** `docs/schema-gap-analysis.md`, reviewed against schema version 1.0.0. This summary does not change the schema.

## Top 10 critical findings

The gap analysis labels eight guest needs Critical. The list below gives ten concrete findings by separating compound cost and mobility gaps; it does not reclassify Important needs.

1. **Visit duration is missing or unclear.** A guest cannot plan the day when typical on-site time is unknown. Duration tags duplicate `typical_duration` and can mislead when that field is empty.
2. **Drive time and destination point need verification.** All pilot driving durations are null; the estimate must refer to the same labeled point guests navigate to.
3. **Opening information needs dated, current evidence.** Schedule, seasonal exceptions, and the dates those hours apply determine whether a chosen-day visit is possible.
4. **Published admission prices are not a family budget.** The per-person cost tier does not show adult/child prices or family tickets.
5. **Likely add-on costs are easy to miss.** Parking, transport, and other required charges can change the outing’s actual cost; a generic tier cannot convey them.
6. **Booking policy is not date availability.** A booking link or “required” flag cannot establish whether a family can still reserve the desired date or slot.
7. **Wheelchair access needs route-level detail.** The summary must match the documented entrance, route, and relevant facilities; current pilots leave access unresolved.
8. **Stroller suitability is not explicit.** Wheelchair information does not automatically answer whether a stroller can manage the surface, steps, and gradients.
9. **Parking needs usable arrival detail.** Guests need a verified fee, restrictions, and walking distance to the actual visitor entrance, not merely a nearby parking label.
10. **Formal restrictions need separation from suitability ratings.** Age, height, supervision, and activity restrictions can prevent participation; `age_groups` and family scores do not substitute for those rules.

## Top 10 important findings

1. **Suitability needs reasons and caveats.** Distinguish eligible audiences, degree of fit, and physical effort; do not leave family scores unexplained.
2. **Season suitability and opening dates are different.** `seasonality` should not be used as an operating calendar.
3. **Facility location matters.** State whether toilets and food are on-site or nearby and where they are relative to the visit.
4. **Non-driving options need a practical last-mile picture.** Current stop, schedule, and walking effort matter more than a transport-mode label alone.
5. **Dog policy needs material conditions.** Keep the quick yes/no/partial summary, with sourced restrictions where applicable.
6. **Place scope and pin need a plain explanation.** Guests should know whether a record describes a town, route, venue, or specific entrance.
7. **Weather exposure may affect comfort.** Shade, shelter, outdoor exposure, and water conditions can matter more than a broad season label.
8. **Food presence does not answer dietary needs.** Menus, child options, allergens, and outside-food rules should be linked or described when verified.
9. **Route constraints can add time or cost.** Mention material tolls, restricted roads, or last-mile conditions when verified; avoid turn-by-turn duplication.
10. **Freshness must be clear.** Define `last_verified` and associate evidence dates with volatile hours, prices, booking, access, and transport claims.

## Schema changes actually necessary

Keep the change set small and tied to guest decisions:

- **Add optional structured price details** for ticket type/age band, amount, conditions, and checked date. Calculate a total only for a stated party composition; do not store a generic “family price.” Keep `cost_level` as a coarse comparison aid.
- **Add an optional structured restrictions list** for age/height, supervision, and activity-specific rules, with the affected activity/audience and evidence. Keep formal restrictions separate from editorial suitability.
- **Clarify existing field semantics:** define the scope/basis of `typical_duration`; make duration tags derived from it or remove them; distinguish seasonal suitability from opening schedules; define `last_verified`; and specify how `wheelchair_friendly` derives from detailed access. These are schema guidance/validation changes, not necessarily new fields.
- **Do not add stroller fields automatically.** First standardize verified stroller route information in the mobility description. Add a dedicated field only if guests need it consistently and evidence can support it.

## Missing information better handled in content or links

Use concise, sourced copy or an official live link for site-specific weather exposure, facility location, dietary/menu details, outside-food policies, parking approach, tolls, road notes, and live booking capacity. These facts vary by venue or date and would create maintenance burden as mandatory structured fields. Use links for current schedules, fares, menus, and availability; keep the record’s own summary and check evidence current.

## Existing fields with little direct guest decision value

Operational fields such as `id`, `schema_version`, `status`, `created_at`, `updated_at`, `review_decision`, `redirects`, `external_ids`, evidence checker identity, review issue ownership, image-rights state, and validation outcomes support governance and reliable publishing, but are not guest answers. SEO fields support discovery rather than the on-page decision. Administrative geography (`province`, `autonomous_community`, `country`) and coordinates help identify or navigate to a place but rarely explain whether to go. Retain these for their operational purpose; avoid giving them prominence over suitability, time, cost, access, and current conditions.
