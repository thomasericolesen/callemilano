---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-MARBELLA-OLD-TOWN-001
slug: marbella-old-town
name: Marbella Old Town
category: City
tags:
  - Historic town
  - Museum
  - Restaurant
  - Half day
coordinates:
  latitude: 36.5101033
  longitude: -4.8849716
  purpose: town_center
  label: Plaza de los Naranjos
  source: https://www.juntadeandalucia.es/cultura/agendaculturaldeandalucia/espacios/marbella-casco-antiguo
  checked_at: 2026-10-03
google_maps_url: https://maps.google.com/?q=Marbella+Old+Town%2C+M%C3%A1laga%2C+Spain
external_ids: {}
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: null
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Plaza de los Naranjos, Marbella, Málaga, Spain
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
  seniors: medium
energy_level: Medium
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
food_available: "yes"
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
  official_website: https://turismo.marbella.es/
  booking: null
  visitor_information: https://turismo.marbella.es/vive/cultura/patrimonio-historico/casco-historico.html
  transport: null
  contact: null
related_places: []
description_short: "Walk Marbella's historic center, with heritage streets, plazas, museums, and places to eat."
description_long: "Marbella's municipal tourism site describes the historic center's Roman, Arab, and Christian heritage, including the old walls, museums, chapels, plazas, restaurants, and traditional shops. Plaza de los Naranjos is used as the representative central point. This is a walk-through urban visit; step-free routes, public parking, toilets, and current museum schedules or admission details have not been checked."
seo_title: "Marbella Old Town: Historic Center and Plazas"
seo_description: "Explore Marbella Old Town's historic streets, plazas, museums, and restaurants. Check current access, parking, and museum details before visiting."
images: []
evidence:
  - field: "coordinates"
    claim: "Plaza de los Naranjos is the representative center point for Marbella's old town."
    source_url: https://www.juntadeandalucia.es/cultura/agendaculturaldeandalucia/espacios/marbella-casco-antiguo
    source_type: government
    checked_at: 2026-10-03
    checked_by: maps-import-agent
    confidence: high
    notes: "Official regional cultural listing locates the old town at Plaza de los Naranjos."
  - field: "description_long, tags, food_available"
    claim: "Marbella's historic center contains historic heritage, museums, plazas, restaurants, and shops."
    source_url: https://turismo.marbella.es/vive/cultura/patrimonio-historico/casco-historico.html
    source_type: official_tourism
    checked_at: 2026-10-03
    checked_by: maps-import-agent
    confidence: high
    notes: null
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
    description: "Audience ratings, energy, and visit-duration tag are provisional editorial estimates for an urban walking visit; assess route demands and typical visit time before approval."
    retryable: true
    owner: editorial
  - code: visitor_facilities_unverified
    severity: warning
    fields: [accessibility, wheelchair_friendly, parking, dog_friendly, toilets_available, cost_level]
    description: "Visitor facilities, access, parking, and cost remain unverified."
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

Draft source notes: Marbella municipal tourism and regional cultural listing checked on 2026-10-03. No user-provided saved-place URL was supplied; the Maps search link is a place lookup, not a saved-list link.
