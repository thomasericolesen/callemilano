---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-RESTAURANTE-LA-REJA-001
slug: restaurante-la-reja
name: Restaurante La Reja
category: Restaurants
tags: []
coordinates:
  latitude: 36.595349399999996
  longitude: -4.6381157
  purpose: venue
  label: Restaurante La Reja. Steak House & Traditional Spanish Restaurant with Panoramic Views, C. de los Caños, 9, 29650 Mijas, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJSVxmMfvjcg0Rjbng0mplliE, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=2420233359237101965
external_ids:
  google_place_id: ChIJSVxmMfvjcg0Rjbng0mplliE
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 22 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante La Reja. Steak House & Traditional Spanish Restaurant with Panoramic Views, C. de los Caños, 9, 29650 Mijas, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.595349399999996,-4.6381157); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.595349399999996%2C-4.6381157&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 22 min, 11.5 km. One predicted sample.'
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
  official_website: https://restaurantelareja.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Restaurante La Reja: a restaurant, about 22 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Restaurante La Reja is a restaurant. About 22 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Other facts have not been checked yet.
seo_title: Restaurante La Reja, Mijas | CalleMilano draft record
seo_description: 'Draft record for Restaurante La Reja (Mijas): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Restaurante La Reja. Steak House & Traditional Spanish Restaurant with Panoramic Views' at C. de los Caños, 9, 29650 Mijas, Málaga, España (36.595349399999996,-4.6381157), status OPERATIONAL, type restaurant.
  source_url: https://maps.google.com/?cid=2420233359237101965
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes. Editor: own site has conflicting hours (''Tuesday Closed'' and ''Monday-Sunday''); show ''check before visiting'', hours unknown.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 22 min by car (11.5 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.595349399999996%2C-4.6381157&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
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
created_at: '2026-11-15'
updated_at: '2026-11-15'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
