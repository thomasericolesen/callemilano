---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-PARQUE-LA-CANTERA-001
slug: parque-la-cantera
name: Parque La Cantera
category: Nature
tags: []
coordinates:
  latitude: 36.5657639
  longitude: -4.6188943
  purpose: representative_point
  label: Parque La Cantera, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJMxizfrPjcg0ROjLo0soXQlU, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=6143499001576043066
external_ids:
  google_place_id: ChIJMxizfrPjcg0ROjLo0soXQlU
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 13 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Parque La Cantera, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5657639,-4.6188943); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5657639%2C-4.6188943&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 13 min, 7.0 km. One predicted sample.'
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
description_short: 'Parque La Cantera: a park, about 13 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Parque La Cantera is a park. About 13 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Other facts have not been checked yet.
seo_title: Parque La Cantera, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Parque La Cantera (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Parque La Cantera' at 29640 Fuengirola, Málaga, España (36.5657639,-4.6188943), status OPERATIONAL, type park.
  source_url: https://maps.google.com/?cid=6143499001576043066
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 13 min by car (7.0 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5657639%2C-4.6188943&travelmode=driving
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
