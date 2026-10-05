---
schema_version: 1.0.0
status: needs_fact_check
id: ES-VAL-CAS-LA-VALL-DUIXO-001
slug: la-vall-duixo
name: La Vall d'Uixó
category: City
tags: []
coordinates:
  latitude:  null
  longitude:  null
  purpose: representative_point
  label: Unknown; exact visitor point not established
  source:  null
  checked_at:  null
google_maps_url: https://maps.app.goo.gl/4cZJ8eRQH47aHH146
external_ids: {}
municipality: Unknown
province: Unknown
autonomous_community: Unknown
country: Unknown
driving_time_from_casa_de_la_familia:
  duration:  null
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas,
    Málaga, Spain
  destination: Unknown; named visitor point not established
  source:  null
  checked_at:  null
  note: Route not checked; do not estimate from memory.
age_groups:
  - Children (7-12)
  - Teenagers (13-17)
  - Adults
  - Seniors
family_score:
  small_children: low
  children: high
  teenagers: high
  adults: high
  seniors: medium
energy_level: Low
seasonality:
  - All year
accessibility:
  overall: unknown
  mobility:
    route: unknown
    wheelchair_route: unknown
    facilities: unknown
  sensory:
    notes: unknown
  accessible_toilets: unknown
  source:  null
  checked_at:  null
  confidence: unknown
wheelchair_friendly: unknown
parking:
  availability: unknown
  location_type: unknown
  cost: unknown
  restrictions: unknown
  walk_distance: unknown
  source:  null
  checked_at:  null
transport_options: []
booking_required: true
dog_friendly: unknown
toilets_available: unknown
food_available: unknown
cost_level: Unknown
visit_information:
  schedule:  null
  typical_duration: "Half day for the caves and immediate area (editorial planning estimate)"
  booking_lead_time:  null
  valid_from:  null
  valid_until:  null
  cost_basis:  null
  cost_checked_at:  null
links:
  official_website:  null
  booking:  null
  visitor_information:  null
  transport:  null
  contact:  null
related_places: []
description_short: "Town in Castellón best known to visitors for the Coves de Sant Josep underground river and cave complex."
description_long: "Why interesting: The caves offer a distinctive underground landscape and boat visit; the town also has walking routes and other local attractions. Treat the cave as a separate, specific experience from the town record. Editorial suitability by audience (low / medium / high): Small children (0-6) low, Children (7-12) high, Teenagers (13-17) high, Adults high, Seniors medium. These are estimates for planning, not guarantees or safety advice. Estimated duration: Half day for the caves and immediate area (editorial planning estimate). Seasonality: All year. Weather and practical notes: The local tourism office provides a ticket-purchase link for the caves; confirm current tour availability and any visitor restrictions. A town visit alone does not require booking. No cave access or sensory suitability assumptions are made here. Booking: true."
seo_title: La Vall d'Uixó | CalleMilano destination record
seo_description: Draft destination record for La Vall d'Uixó. Visitor facts and practical
  details are under verification.
images: []
evidence:
- field: name, province, country, google_maps_url
  claim: The owner-supplied list capture displays “La Vall d’Uixó” with Province of
    Castellón, Spain.
  source_url: https://maps.app.goo.gl/4cZJ8eRQH47aHH146
  source_type: maps_identity
  checked_at: '2026-10-04'
  checked_by: maps-import-agent
  confidence: medium
  notes: User-provided visible list capture. The list link is identity provenance
    only; it does not verify visitor facts, and an individual place URL was not supplied.
- field: description_short, description_long, booking_required
  claim: "La Vall d’Uixó tourism describes Coves de Sant Josep and links to ticket purchase; municipal visitor page describes local access and attractions."
  source_url: https://turismolavallduixo.es/coves-de-sant-josep/
  source_type: official_tourism
  checked_at: 2026-10-04
  checked_by: fact-check-agent
  confidence: high
  notes: "Supports the stated claim only; any editorial planning estimate is identified as such."
- field: description_long
  claim: "Municipal tourism identifies the caves as the town’s main tourist attraction and notes transport limitations, routes, and other activities."
  source_url: https://turismolavallduixo.es/venir/informacion-practica/
  source_type: official_tourism
  checked_at: 2026-10-04
  checked_by: fact-check-agent
  confidence: high
  notes: "Supports the stated claim only; any editorial planning estimate is identified as such."
review_issues:
- code: editorial_suitability_requires_human_review
  severity: warning
  fields:
  description: Audience ratings and effort level are editorial estimates requested for this draft; human editor must review them before approval.
  retryable: false
  owner: human_editor
- code: record_incomplete
  severity: warning
  fields:
  - coordinates
  - driving_time_from_casa_de_la_familia
  - accessibility
  - parking
  - visit_information
  description: These facts or editorial assessments were not established from the
    supplied list or checked sources. Explicit unknown values remain in this draft;
    complete claim-specific research and editorial review before advancement.
  retryable: true
  owner: fact_check
- code: identity_scope_unresolved
  severity: blocking
  fields:
  - name
  - coordinates
  - municipality
  - province
  - google_maps_url
  description: The imported name/pin does not establish an unambiguous visitor destination
    or exact point; confirm the intended identity before this draft advances.
  retryable: false
  owner: human_editor
- code: schema_blocking_unknowns
  severity: blocking
  fields:
  - coordinates.latitude
  - coordinates.longitude
  description: The active schema does not define unknown values for all required fields.
    This draft leaves unsupported values explicit; resolve them with evidence or obtain
    an approved schema-compatible representation before validation or human approval.
  retryable: true
  owner: fact_check
- code: category_and_tags_need_human_review
  severity: warning
  fields:
  - category
  - tags
  description: Primary category and controlled tags are provisional intake recommendations;
    human editor-of-record must confirm before editorial advancement.
  retryable: false
  owner: human_editor
created_at: '2026-10-04'
updated_at: '2026-10-04'
last_verified:  null
last_reviewed_at:  null
next_review_at:  null
review_decision:  null
redirects: []
---
