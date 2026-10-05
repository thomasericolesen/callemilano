---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-FRIGILIANA-001
slug: frigiliana
name: Frigiliana
category: City
tags:
  - Historic town
  - Viewpoint
  - Half day
coordinates:
  latitude: 36.7908751
  longitude: -3.8947061
  purpose: town_center
  label: Plaza de las Tres Culturas
  source: https://www.juntadeandalucia.es/cultura/agendaculturaldeandalucia/espacios/plaza-tres-culturas
  checked_at: 2026-10-03
google_maps_url: https://maps.google.com/?q=Frigiliana%2C+M%C3%A1laga%2C+Spain
external_ids: {}
municipality: Frigiliana
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: null
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Plaza de las Tres Culturas, Frigiliana, Málaga, Spain
  source: null
  checked_at: null
  note: One-way route duration not verified; check a current routing source.
age_groups:
  - Small children (0-6)
  - Children (7-12)
  - Teenagers (13-17)
  - Adults
  - Seniors
family_score:
  small_children: medium
  children: high
  teenagers: high
  adults: high
  seniors: low
energy_level: High
seasonality:
  - Spring
  - Summer
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
booking_required: false
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
  official_website: https://frigiliana.es/
  booking: null
  visitor_information: https://frigiliana.es/la-concejalia-de-turismo-pone-en-valor-nuestro-casco-historico/
  transport: null
  contact: null
related_places: []
description_short: "Explore Frigiliana's historic quarter and viewpoints in an Andalusian mountain town."
description_long: "Frigiliana's municipal tourism office describes guided visits that introduce the town's historic quarter and architectural heritage. Plaza de las Tres Culturas is used here as the representative town-center pin. This is a walking-focused visit; route gradients, step-free access, parking, facilities, and current tour arrangements have not been verified."
seo_title: "Frigiliana, Málaga: Historic Quarter and Viewpoints"
seo_description: "Plan a family visit to Frigiliana, with its historic quarter and viewpoints. Check current route access, parking, and visitor services before travelling."
images: []
evidence:
  - field: "coordinates"
    claim: "Plaza de las Tres Culturas is the representative town-center point."
    source_url: https://www.juntadeandalucia.es/cultura/agendaculturaldeandalucia/espacios/plaza-tres-culturas
    source_type: government
    checked_at: 2026-10-03
    checked_by: maps-import-agent
    confidence: high
    notes: "Coordinates listed for the public square; represents the town-center arrival point, not every attraction."
  - field: "description_long, tags"
    claim: "The municipal tourism office promotes visits to Frigiliana's historic quarter and cultural/architectural heritage."
    source_url: https://frigiliana.es/la-concejalia-de-turismo-pone-en-valor-nuestro-casco-historico/
    source_type: government
    checked_at: 2026-10-03
    checked_by: maps-import-agent
    confidence: high
    notes: null
  - field: "tags.Viewpoint"
    claim: "The town's historic quarter includes viewpoints with views from its upper streets."
    source_url: https://frigiliana.es/frigiliana-localizacion-destacada-en-el-ultimo-anuncio-de-coca-cola/
    source_type: government
    checked_at: 2026-10-03
    checked_by: maps-import-agent
    confidence: high
    notes: "Municipal tourism article; exact viewpoint route and current access remain unverified."
review_issues:
  - code: driving_time_unverified
    severity: blocking
    fields: [driving_time_from_casa_de_la_familia]
    description: "Verify one-way drive time from Casa de la Familia and record route source and check date."
    retryable: true
    owner: fact_check
  - code: family_ratings_estimated
    severity: warning
    fields: [age_groups, family_score, energy_level, tags.Half day]
    description: "Audience ratings, energy, and visit-duration tag are provisional editorial estimates for a walking-focused historic town; check terrain, duration, and suitability before approval."
    retryable: true
    owner: editorial
  - code: visitor_facilities_unverified
    severity: warning
    fields: [accessibility, wheelchair_friendly, parking, dog_friendly, toilets_available, food_available, cost_level]
    description: "Visitor facilities, access, and cost remain unverified."
    retryable: true
    owner: fact_check
created_at: 2026-10-03
updated_at: 2026-10-03
last_verified: 2026-10-03
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---

Draft source notes: official municipality and regional cultural listing checked on 2026-10-03. No user-provided saved-place URL was supplied; the Maps search link is a place lookup, not a saved-list link.
