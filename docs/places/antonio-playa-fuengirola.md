---
schema_version: 1.0.0
status: archived
id: ES-AND-MAL-ANTONIO-PLAYA-FUENGIROLA-001
slug: antonio-playa-fuengirola
name: Restaurante Antonio Playa
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.5280257
  longitude: -4.6260498
  purpose: venue
  label: Restaurante Antonio Playa, C. Alberto Morgenstern, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJwwQE4gzicg0RJH6I7tX58b8, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=13831110627856776740
external_ids:
  google_place_id: ChIJwwQE4gzicg0RJH6I7tX58b8
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 10 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante Antonio Playa, C. Alberto Morgenstern, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5280257,-4.6260498); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5280257%2C-4.6260498&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 10 min, 5.1 km. One predicted sample.'
age_groups: []
family_score:
  small_children: unknown
  children: unknown
  young_adults: unknown
  seniors: unknown
energy_level: Low
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
  official_website: null
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Restaurante Antonio Playa: a beachside restaurant, about 10 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Restaurante Antonio Playa is a beachside restaurant. About 10 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Other facts have not been checked yet.
seo_title: Restaurante Antonio Playa, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Restaurante Antonio Playa (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Restaurante Antonio Playa' at C. Alberto Morgenstern, 29640 Fuengirola, Málaga, España (36.5280257,-4.6260498), status OPERATIONAL, type bar_and_grill.
  source_url: https://maps.google.com/?cid=13831110627856776740
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. Owner selected directory lead R-0208 on 2026-11-02 (checklist https://claude.ai/artifact/VCrXrv5vKsUhruvVk6R9ZT).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 10 min by car (5.1 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5280257%2C-4.6260498&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
review_issues:
- code: facts_not_checked
  severity: warning
  fields:
  - description_long
  - visit_information
  - cost_level
  - accessibility
  - parking
  description: Created from Google Places identity and a route check only; needs official or own sources.
  retryable: true
  owner: fact_check
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  - tags
  description: Age groups, family scores and tags are not assessed; energy_level is an editorial estimate.
  retryable: true
  owner: human_editor
- code: no_readable_own_source
  severity: warning
  fields:
  - description_long
  - visit_information
  - cost_level
  description: '2026-11-10: no Facebook page found when searching Facebook for ''Antonio Playa Fuengirola''; Instagram keyword search returned no readable text. No own website either, so no readable own source.'
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision:
  decision: archived
  reviewer: Eric Olesen (editor-of-record)
  date: '2026-11-11'
  notes: 'Owner decision 2026-11-11: too much effort to get usable facts (no Facebook page or readable own source found); we already have enough restaurants. Kept as archive; the ID stays allocated and must not be reused.'
redirects: []
---
