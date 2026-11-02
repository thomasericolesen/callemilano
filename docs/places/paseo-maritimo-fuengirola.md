---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-PASEO-MARITIMO-FUENGIROLA-001
slug: paseo-maritimo-fuengirola
name: Paseo Marítimo de Fuengirola
category: Excursions
tags: []
coordinates:
  latitude: 36.5433212
  longitude: -4.618598599999999
  purpose: venue
  label: Paseo Marítimo de Fuengirola, Puerto Deportivo Fuengirola, Local 301, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJd4Szyorjcg0RISr3zRiA_GA, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=6988601565795265057
external_ids:
  google_place_id: ChIJd4Szyorjcg0RISr3zRiA_GA
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 16 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Paseo Marítimo de Fuengirola, Puerto Deportivo Fuengirola, Local 301, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5433212,-4.618598599999999); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5433212%2C-4.618598599999999&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 16 min, 6.61 km. One predicted sample, not the Google Maps app''s main figure.'
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
description_short: 'Paseo Marítimo de Fuengirola: Fuengirola''s seafront promenade, about 16 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: Paseo Marítimo de Fuengirola is Fuengirola's seafront promenade (Puerto Deportivo Fuengirola, Local 301, 29640 Fuengirola, Málaga, España). From Casa de la Familia it is about 16 minutes by car (Google route check, Saturday 10:00). Fuengirola council (2021) describes a cycle lane along the Los Boliches promenade, resurfaced that year. The promenade's total length and facilities were not found in an official source yet (secondary sources give about 7-8 km). Check conditions before setting out.
seo_title: Paseo Marítimo de Fuengirola, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Paseo Marítimo de Fuengirola (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Paseo Marítimo de Fuengirola' at Puerto Deportivo Fuengirola, Local 301, 29640 Fuengirola, Málaga, España (36.5433212,-4.618598599999999), business status OPERATIONAL, primary type tourist_attraction.
  source_url: https://maps.google.com/?cid=6988601565795265057
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 16 min by car (6.61 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5433212%2C-4.618598599999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time over 20 minutes, so not shown (owner rule).
- field: description_long
  claim: 'Fuengirola council, 25 Nov 2021: ''El Ayuntamiento de Fuengirola renueva el pavimento del carril bici del Paseo Marítimo de Los Boliches'' (about 1,500 m² resurfaced with synthetic resin, new road markings).'
  source_url: https://www.fuengirola.es/el-ayuntamiento-de-fuengirola-renueva-el-pavimento-del-carril-bici-del-paseo-maritimo-de-los-boliches/
  source_type: government
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: medium
  notes: Read via Firecrawl on 2026-11-02. Secondary length figures (Tripadvisor 'over 7 km', a Facebook post 'nearly 8 km') not recorded.
review_issues:
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
  description: 'Category ''Excursions'' was chosen by Claude from the schema definitions (routes and sights: Excursions; towns: City; natural areas: Nature; visitor attractions: Family activities). Confirm at editorial review.'
  retryable: true
  owner: human_editor
- code: promenade_facts_thin
  severity: warning
  fields:
  - description_long
  - accessibility
  - toilets_available
  description: Only the existence of a cycle lane is officially sourced. Length, sections, toilets and access need Fuengirola council or the tourism portal.
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: '2026-11-02'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
