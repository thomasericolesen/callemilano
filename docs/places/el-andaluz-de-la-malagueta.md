---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-EL-ANDALUZ-DE-LA-MALAGUETA-001
slug: el-andaluz-de-la-malagueta
name: El Andaluz de la Malagueta
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.7190896
  longitude: -4.4093101
  purpose: venue
  label: El Andaluz de la Malagueta, C. Fernando Camino, 18, Málaga-Este, 29016 Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJB8KQ9Oj3cg0RE5_C9nK0byc, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=2841688295753293587
external_ids:
  google_place_id: ChIJB8KQ9Oj3cg0RE5_C9nK0byc
municipality: Málaga
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 43 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: El Andaluz de la Malagueta, C. Fernando Camino, 18, Málaga-Este, 29016 Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.7190896,-4.4093101); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.7190896%2C-4.4093101&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 43 min, 37.3 km. One predicted sample.'
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
related_places:
- playa-la-malagueta
description_short: 'El Andaluz de la Malagueta: andalusisk køkken near the beach (Málaga). Draft; facts not yet checked.'
description_long: El Andaluz de la Malagueta is listed by Google at C. Fernando Camino, 18, Málaga-Este, 29016 Málaga, España, about 243 m in a straight line from the beach point of the related beach record. About 43 minutes by car from Casa de la Familia. Menu, opening hours, prices and child-friendliness have not been checked yet.
seo_title: El Andaluz de la Malagueta, Málaga | CalleMilano draft record
seo_description: 'Draft record for El Andaluz de la Malagueta (Málaga): location near the beach and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'El Andaluz de la Malagueta' at C. Fernando Camino, 18, Málaga-Este, 29016 Málaga, España (36.7190896,-4.4093101), business status OPERATIONAL, primary type restaurant; about 243 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=2841688295753293587
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/one-hour-beach-restaurants-intake-2026-11-02.md, row rA02).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 43 min by car (37.3 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.7190896%2C-4.4093101&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
review_issues:
- code: facts_not_checked
  severity: warning
  fields:
  - visit_information
  - cost_level
  - food_available
  - booking_required
  - description_long
  description: Created from Google Places identity and a route check. Cuisine, opening hours, season, prices and booking need the restaurant's own source.
  retryable: true
  owner: fact_check
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  description: Age groups and family scores are not assessed.
  retryable: true
  owner: human_editor
- code: no_readable_own_source
  severity: warning
  fields:
  - description_long
  - visit_information
  description: No own website (or only a Facebook page) in the Google listing. Needs the owner's screenshots of the venue's own page or menu, or a visit.
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
