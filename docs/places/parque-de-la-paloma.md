---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-PARQUE-DE-LA-PALOMA-001
slug: parque-de-la-paloma
name: Parque de la Paloma
category: Family activities
tags: []
coordinates:
  latitude: 36.5935284
  longitude: -4.5293123
  purpose: venue
  label: Parque de la Paloma, Av. Federico García Lorca, s/n, 29630 Benalmádena, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJq2BnI4z8cg0RpE_1LeHQrfI, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=17486862593706774436
external_ids:
  google_place_id: ChIJq2BnI4z8cg0RpE_1LeHQrfI
municipality: Benalmádena
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 25 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Parque de la Paloma, Av. Federico García Lorca, s/n, 29630 Benalmádena, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5935284,-4.5293123); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5935284%2C-4.5293123&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 25 min, 19.03 km. One predicted sample, not the Google Maps app''s main figure.'
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
  official_website: http://www.andalucia.org/es/turismo-cultural/visitas/malaga/otras-visitas/parque-de-la-paloma/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Parque de la Paloma: a large park with animals and a lake, about 25 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Parque de la Paloma is a large park with animals and a lake (Av. Federico García Lorca, s/n, 29630 Benalmádena, Málaga, España). From Casa de la Familia it is about 25 minutes by car (Google route check, Saturday 10:00). Opening hours, prices, access and suitability have not been checked yet; check before visiting.
seo_title: Parque de la Paloma, Benalmádena | CalleMilano draft record
seo_description: 'Draft record for Parque de la Paloma (Benalmádena): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Parque de la Paloma' at Av. Federico García Lorca, s/n, 29630 Benalmádena, Málaga, España (36.5935284,-4.5293123), business status OPERATIONAL, primary type park.
  source_url: https://maps.google.com/?cid=17486862593706774436
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 25 min by car (19.03 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5935284%2C-4.5293123&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time over 20 minutes, so not shown (owner rule).
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
  description: Created from Google Places identity and route checks only. Opening hours, season, prices, access and facilities still need official or own sources.
  retryable: true
  owner: fact_check
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  - tags
  description: Age groups, family scores and tags are not assessed; energy_level Low is an editorial estimate from the type of place.
  retryable: true
  owner: human_editor
- code: category_editorial_choice
  severity: info
  fields:
  - category
  description: 'Category ''Family activities'' was chosen by Claude from the schema definitions (routes and sights: Excursions; towns: City; natural areas: Nature; visitor attractions: Family activities). Confirm at editorial review.'
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
