---
schema_version: 1.0.0
status: draft
id: ES-AND-GRA-GRANADA-001
slug: granada
name: Granada
category: City
tags:
  - Historic town
  - Museum
  - Restaurant
  - Full day
coordinates:
  latitude: null
  longitude: null
  purpose: town_center
  label: Unknown; exact visitor point not established
  source: null
  checked_at: null
google_maps_url: https://maps.google.com/?q=Granada%2C+Granada%2C+Spain
external_ids: {}
municipality: Granada
province: Granada
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: null
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Unknown; named visitor point not established
  source: null
  checked_at: null
  note: Route not checked; do not estimate from memory.
age_groups:
  - Teenagers (13-17)
  - Adults
family_score:
  small_children: unknown
  children: unknown
  teenagers: high
  adults: high
  seniors: unknown
energy_level: Medium
seasonality:
  - Spring
  - Autumn
  - Winter
accessibility:
  overall: unknown
  mobility:
    route: unknown
    wheelchair_route: unknown
    facilities: unknown
  sensory:
    notes: unknown
  accessible_toilets: unknown
  source: null
  checked_at: null
  confidence: unknown
wheelchair_friendly: unknown
parking:
  availability: unknown
  location_type: unknown
  cost: unknown
  restrictions: unknown
  walk_distance: unknown
  source: null
  checked_at: null
transport_options: []
booking_required: unknown
dog_friendly: unknown
toilets_available: unknown
food_available: unknown
cost_level: Unknown
visit_information:
  schedule: null
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: null
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: "Granada is a candidate destination for longer excursions from Casa de la Familia; content is pending fact check."
description_long: "Granada (Granada) is proposed for the excursion layer aimed at young adults. This record is an identity-level placeholder: no sourced facts about sights, food and drink, access or prices have been collected yet."
seo_title: "Granada: Excursion from Casa de la Familia (Draft)"
seo_description: "Draft page for Granada. Content, access and travel time are not yet verified."
images: []
evidence: []
review_issues:
  - code: driving_time_unverified
    severity: blocking
    fields: [driving_time_from_casa_de_la_familia]
    description: "Verify one-way drive time from Casa de la Familia with a route source and record the check date. Do not estimate."
    retryable: true
    owner: fact_check
  - code: coordinates_missing
    severity: blocking
    fields: [coordinates]
    description: "Coordinates not yet established from a source; choose and record the named visitor point."
    retryable: true
    owner: fact_check
  - code: no_sources_yet
    severity: blocking
    fields: [description_long, evidence]
    description: "No source evidence collected. Descriptions are identity-level placeholders; write content only from official sources."
    retryable: true
    owner: fact_check
  - code: alhambra_in_granada
    severity: warning
    fields: [description_long, coordinates, booking_required]
    description: "Owner decision 2026-10-15: the Alhambra is part of this record, not a separate one. Its ticketing and booking rules must be checked from the official site and recorded here."
    retryable: true
    owner: editorial
  - code: excursion_layer_scope
    severity: warning
    fields: [status]
    description: "Included under the owner decision of 2026-10-15 to add an excursion layer (route-checked one-way drive up to about 4 h) beyond the 30 km primary area. Pending editor-of-record approval and change-log entry."
    retryable: true
    owner: editor
  - code: family_ratings_estimated
    severity: warning
    fields: [age_groups, family_score, energy_level, seasonality, tags]
    description: "Audience ratings, energy, season and duration tag are provisional editorial estimates for young adults; other age groups left unknown. Assess before approval."
    retryable: true
    owner: editorial
  - code: visitor_facilities_unverified
    severity: warning
    fields: [accessibility, wheelchair_friendly, parking, dog_friendly, toilets_available, cost_level, booking_required]
    description: "Visitor facilities, access, parking, booking and cost remain unverified."
    retryable: true
    owner: fact_check
created_at: 2026-10-15
updated_at: 2026-10-15
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---

Draft source notes: none. Created from the Danish excursion catalogue of 2026-10-15 (an inspiration document, not a source). The Maps link is a place lookup, not a saved-list link.
