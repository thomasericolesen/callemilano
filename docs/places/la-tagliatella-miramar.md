---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-LA-TAGLIATELLA-MIRAMAR-001
slug: la-tagliatella-miramar
name: La Tagliatella (C.C. Miramar)
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.528461899999996
  longitude: -4.6317998
  purpose: venue
  label: Restaurante La Tagliatella | Fuengirola, CC Miramar, Av. de la Encarnación, s/n, Planta 1, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJHzgiD37jcg0ROY-ZzB1cFE8, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=5698280711586942777
external_ids:
  google_place_id: ChIJHzgiD37jcg0ROY-ZzB1cFE8
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 8 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante La Tagliatella | Fuengirola, CC Miramar, Av. de la Encarnación, s/n, Planta 1, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.528461899999996,-4.6317998); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.528461899999996%2C-4.6317998&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 8 min, 4.2 km. One predicted sample.'
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
  official_website: https://www.latagliatella.es/restaurantes/malaga/cc-miramar-fuengirola?utm_source=gmb&utm_medium=organic&utm_campaign=gmb&utm_content=web
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'La Tagliatella (C.C. Miramar): an Italian restaurant chain at the Miramar shopping centre, about 8 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: La Tagliatella (C.C. Miramar) is an Italian restaurant chain at the Miramar shopping centre. About 8 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Other facts have not been checked yet.
seo_title: La Tagliatella (C.C. Miramar), Fuengirola | CalleMilano draft record
seo_description: 'Draft record for La Tagliatella (C.C. Miramar) (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Restaurante La Tagliatella | Fuengirola' at CC Miramar, Av. de la Encarnación, s/n, Planta 1, 29640 Fuengirola, Málaga, España (36.528461899999996,-4.6317998), status OPERATIONAL, type italian_restaurant.
  source_url: https://maps.google.com/?cid=5698280711586942777
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. Owner selected directory lead R-0207 on 2026-11-02 (checklist https://claude.ai/artifact/VCrXrv5vKsUhruvVk6R9ZT).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 8 min by car (4.2 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.528461899999996%2C-4.6317998&travelmode=driving
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
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
