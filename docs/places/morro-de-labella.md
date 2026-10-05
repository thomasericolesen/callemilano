---
schema_version: 1.0.0
status: needs_fact_check
id: ES-CAT-BAR-MORRO-DE-LABELLA-001
slug: morro-de-labella
name: Morro de l'Abella
category: Nature
tags:
- Viewpoint
- Nature
coordinates:
  latitude:  null
  longitude:  null
  purpose: representative_point
  label: Unknown; exact visitor point not established
  source:  null
  checked_at:  null
google_maps_url: https://maps.app.goo.gl/4cZJ8eRQH47aHH146
external_ids: {}
municipality: Tavertet
province: Barcelona
autonomous_community: Catalonia
country: Spain
driving_time_from_casa_de_la_familia:
  duration:  null
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas,
    Málaga, Spain
  destination: Unknown; named visitor point not established
  source:  null
  checked_at:  null
  note: Route not checked; do not estimate from memory.
age_groups: []
family_score:
  small_children: unknown
  children: unknown
  teenagers: unknown
  adults: unknown
  seniors: unknown
energy_level: High
seasonality:
  - Spring
  - Summer
  - Autumn
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
booking_required: unknown
dog_friendly: unknown
toilets_available: unknown
food_available: unknown
cost_level: Unknown
visit_information:
  schedule:  null
  typical_duration: "Unknown; no visit duration assigned while access status is unresolved"
  booking_lead_time:  null
  valid_from:  null
  valid_until:  null
  cost_basis:  null
  cost_checked_at:  null
links:
  official_website:  null
  booking:  null
  visitor_information: https://www.tavertet.cat/turisme/llocs-dinteres/el-morro-de-labella.html
  transport:  null
  contact:  null
related_places: []
description_short: "A natural viewpoint in Tavertet, currently subject to access restrictions."
description_long: "Why interesting: Its appeal is the cliffside landscape and elevated views. Do not plan a visit until Tavertet confirms that access is open: the municipality says the viewpoint is on private land and has published closure notices. Editorial suitability by audience is unknown because current access status has not been verified. Estimated duration: Unknown; no visit duration assigned while access status is unresolved. Seasonality: Spring; Summer; Autumn. Weather and practical notes: Weather, ice and cliff exposure are relevant. Verify current opening/access directly with Tavertet; do not enter private land or approach cliff edges. Source status is an older official notice, so current access remains unknown. Booking: unknown."
seo_title: Morro de l'Abella | CalleMilano destination record
seo_description: Draft destination record for Morro de l'Abella. Visitor facts and
  practical details are under verification.
images: []
evidence:
- field: name, google_maps_url
  claim: The owner-supplied Projekt Spanien Google Maps list contains a saved-place
    entry displayed as “Morro de l'Abella”.
  source_url: https://maps.app.goo.gl/4cZJ8eRQH47aHH146
  source_type: maps_identity
  checked_at: '2026-10-04'
  checked_by: maps-import-agent
  confidence: high
  notes: User-provided visible list capture. The list link is identity provenance
    only; it does not verify visitor facts, and an individual place URL was not supplied.
- field: description_long
  claim: The municipality identifies El Morro de l’Abella as a viewpoint on private
    land and states it is closed; page updated 2025-03-18.
  source_url: https://www.tavertet.cat/turisme/llocs-dinteres/el-morro-de-labella.html
  source_type: government
  checked_at: '2026-10-04'
  checked_by: fact-check-agent
  confidence: high
  notes: Supports only the stated claim; do not generalize to unverified facilities
    or suitability.
- field: description_long
  claim: "Tavertet says the viewpoint is on private property and was closed until further notice due to seasonal danger; current status must be checked."
  source_url: https://www.tavertet.cat/actualitat/noticies/el-morro-de-labella-tancat-fins-nou-avis.html
  source_type: government
  checked_at: 2026-10-04
  checked_by: fact-check-agent
  confidence: medium
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
- code: site_closed_private_property
  severity: blocking
  fields:
  - description_long
  - status
  description: Tavertet municipality states that the viewpoint is on private land
    and closed (page updated 2025-03-18); human editor must decide whether to retain
    as a closed/avoid candidate or exclude.
  retryable: true
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
