---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-AQUALAND-TORREMOLINOS-001
slug: aqualand-torremolinos
name: Aqualand Torremolinos
category: Family activities
tags: []
coordinates:
  latitude: 36.6259897
  longitude: -4.5082274
  purpose: venue
  label: Aqualand Torremolinos, C. Cuba, 10, 29620 Torremolinos, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJgwo4J5D7cg0Ry4aludNIl4k, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=9914473178869368523
external_ids:
  google_place_id: ChIJgwo4J5D7cg0Ry4aludNIl4k
municipality: Torremolinos
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 24 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Aqualand Torremolinos, C. Cuba, 10, 29620 Torremolinos, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.6259897,-4.5082274); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6259897%2C-4.5082274&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 24 min, 22.52 km. Walking (Routes API WALK, same day): 279 min, 20.07 km. One predicted sample, not the Google Maps app''s main figure.'
age_groups: []
family_score:
  small_children: unknown
  children: unknown
  young_adults: unknown
  seniors: unknown
energy_level: Medium
seasonality: []
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
  official_website: http://www.aqualand.es/torremolinos
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Aqualand Torremolinos: water park, about 279 min on foot or 24 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Aqualand Torremolinos is a water park at C. Cuba, 10, 29620 Torremolinos, Málaga. From Casa de la Familia it is about 279 minutes on foot (20.07 km, Google's walking route) or about 24 minutes by car (Google route check, Saturday 10:00). Opening hours, prices, age rules and facilities have not been checked yet; check with the venue before visiting.
seo_title: Aqualand Torremolinos, Torremolinos | CalleMilano draft record
seo_description: 'Draft record for Aqualand Torremolinos (Torremolinos): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Aqualand Torremolinos' at C. Cuba, 10, 29620 Torremolinos, Málaga, España (36.6259897,-4.5082274), business status OPERATIONAL, website http://www.aqualand.es/torremolinos.
  source_url: https://maps.google.com/?cid=9914473178869368523
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia, description_long (walking time)
  claim: 'From Casa de la Familia: 24 min by car (22.52 km, Saturday 10:00 predicted traffic) and 279 min on foot (20.07 km).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6259897%2C-4.5082274&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00, and WALK (https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6259897%2C-4.5082274&travelmode=walking). Google's walking route says nothing about pavements, crossings or whether it suits children.
review_issues:
- code: facts_not_checked
  severity: warning
  fields:
  - visit_information
  - cost_level
  - seasonality
  - accessibility
  - booking_required
  - food_available
  - toilets_available
  description: Created from Google Places identity and route checks only. Opening hours, season, prices, age rules, booking and facilities still need the venue's own or official sources.
  retryable: true
  owner: fact_check
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  description: Age groups and family scores are not assessed; energy_level Medium is an editorial estimate from the type of place.
  retryable: true
  owner: human_editor
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
