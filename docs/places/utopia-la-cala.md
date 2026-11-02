---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-UTOPIA-LA-CALA-001
slug: utopia-la-cala
name: UTOPÍA
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.500232
  longitude: -4.6852730000000005
  purpose: venue
  label: UTOPÍA, C. Fuengirola, S/N, LOCAL 8, 29649 La Cala de Mijas, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJY5UFvzQecw0RCx13LV8o47Y, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=13178421323865988363
external_ids:
  google_place_id: ChIJY5UFvzQecw0RCx13LV8o47Y
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 14 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: UTOPÍA, C. Fuengirola, S/N, LOCAL 8, 29649 La Cala de Mijas, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.500232,-4.6852730000000005); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.500232%2C-4.6852730000000005&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 14 min, 6.8 km. One predicted sample.'
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
  official_website: https://utopialacala.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'UTOPÍA: a burger, hot-dog and nachos restaurant in La Cala de Mijas, about 14 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: 'UTOPÍA is a burger, hot-dog and nachos restaurant in La Cala de Mijas. About 14 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Other facts have not been checked yet. Owner''s recommendation (callemilano.dk): A pleasant restaurant with a simple menu of burgers, hot dogs and nachos; nice atmosphere, fine with children, and tasty chili con carne.'
seo_title: UTOPÍA, Mijas | CalleMilano draft record
seo_description: 'Draft record for UTOPÍA (Mijas): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'UTOPÍA' at C. Fuengirola, S/N, LOCAL 8, 29649 La Cala de Mijas, Málaga, España (36.500232,-4.6852730000000005), status OPERATIONAL, type bar_and_grill.
  source_url: https://maps.google.com/?cid=13178421323865988363
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. From the owner's recommendations on callemilano.dk (Lovable app 'Vores Spanske Hjem', table recommendations), read 2026-11-02.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 14 min by car (6.8 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.500232%2C-4.6852730000000005&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long (owner knowledge)
  claim: Dejlig restaurant, simpelt menukort - burgere, hotdogs og nachos. Dejlig stemning og fint med børn. Og lækker chili con carne.
  source_url: https://callemilano.dk/
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: medium
  notes: 'Owner''s own recommendation (kind ''anbefaling'') on callemilano.dk, read from the Lovable app database 2026-11-02; site tags: børn, burger, hotdogs, aftensmad. Personal experience, not independently verified.'
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
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
