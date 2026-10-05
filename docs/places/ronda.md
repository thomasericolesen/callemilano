---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-RONDA-001
slug: ronda
name: Ronda
category: City
tags:
  - Historic town
  - Viewpoint
  - Nature
  - Full day
coordinates:
  latitude: 36.741564
  longitude: -5.165708
  purpose: town_center
  label: Plaza de España / Puente Nuevo approach
  source: https://spainfilmcommission.com/localizaciones/puente-nuevo-y-plaza-de-espana/
  checked_at: 2026-10-03
google_maps_url: https://maps.google.com/?q=Ronda%2C+M%C3%A1laga%2C+Spain
external_ids: {}
municipality: Ronda
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: null
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Plaza de España, Ronda, Málaga, Spain
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
  official_website: https://info.turismoderonda.es/
  booking: null
  visitor_information: https://info.turismoderonda.es/patrimonio-cultural/puente-nuevo-sobre-el-tajo/
  transport: null
  contact: null
related_places: []
description_short: "Discover Ronda's historic center, Puente Nuevo, and views over the Tajo gorge."
description_long: "Ronda's official tourism information identifies Puente Nuevo as a defining city landmark and describes the bridge's connection between the old and newer parts of the city, with views over the Tajo gorge. This record uses Plaza de España as a representative central point. Expect a walking visit across different parts of town; step-free routing, parking, facilities, and current monument access have not been verified."
seo_title: "Ronda, Málaga: Historic Center and Puente Nuevo"
seo_description: "Explore Ronda's historic center and Puente Nuevo above the Tajo gorge. Check current monument access, parking, and facilities before your family visit."
images: []
evidence:
  - field: "coordinates"
    claim: "Plaza de España is a central point in Ronda near the Puente Nuevo approach."
    source_url: https://spainfilmcommission.com/localizaciones/puente-nuevo-y-plaza-de-espana/
    source_type: secondary
    checked_at: 2026-10-03
    checked_by: maps-import-agent
    confidence: medium
    notes: "Coordinates from Spain Film Commission; verify against the municipality's current map before approval."
  - field: "description_long, tags"
    claim: "Puente Nuevo is a defining landmark connecting parts of Ronda and overlooking the Tajo gorge."
    source_url: https://info.turismoderonda.es/patrimonio-cultural/puente-nuevo-sobre-el-tajo/
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
    fields: [age_groups, family_score, energy_level, tags.Full day]
    description: "Audience ratings, energy, and visit-duration tag are provisional editorial estimates for a town visit involving walking; check route demands, typical visit time, and suitability before approval."
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

Draft source notes: Ronda tourism and Spain Film Commission pages checked on 2026-10-03. No user-provided saved-place URL was supplied; the Maps search link is a place lookup, not a saved-list link.
