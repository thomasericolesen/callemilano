---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-RESTAURANTE-LA-ESCOLLERA-ESTEPONA-001
slug: restaurante-la-escollera-estepona
name: Restaurante La Escollera (Estepona)
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.4163478
  longitude: -5.1546519
  purpose: venue
  label: Restaurante La Escollera, C. Puerto Pesquero, 10, 29680 Estepona, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJx9tsD7LWDA0RBs11I1lyVmk, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=7590379949152128262
external_ids:
  google_place_id: ChIJx9tsD7LWDA0RBs11I1lyVmk
municipality: Estepona
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 53 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante La Escollera, C. Puerto Pesquero, 10, 29680 Estepona, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4163478,-5.1546519); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4163478%2C-5.1546519&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 53 min, 59.6 km. One predicted sample.'
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
cost_level: €€
visit_information:
  schedule: null
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'No prices on own site; Tripadvisor price marking "$$ - $$$" read as the middle band. Fallback source per docs/trip-planner-agents.md. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).N'
  cost_checked_at: '2026-11-02'
links:
  official_website: https://m.facebook.com/Restaurante-La-Escollera-Estepona-183448945056268/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- playa-de-la-rada-estepona
description_short: 'Restaurante La Escollera (Estepona): fisk ved fiskerihavnen near the beach (Estepona). Draft; facts not yet checked.'
description_long: Restaurante La Escollera (Estepona) is listed by Google at C. Puerto Pesquero, 10, 29680 Estepona, Málaga, España, about 348 m in a straight line from the beach point of the related beach record. About 53 minutes by car from Casa de la Familia. Menu, opening hours, prices and child-friendliness have not been checked yet.
seo_title: Restaurante La Escollera (Estepona), Estepona | CalleMilano draft record
seo_description: 'Draft record for Restaurante La Escollera (Estepona) (Estepona): location near the beach and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'Restaurante La Escollera' at C. Puerto Pesquero, 10, 29680 Estepona, Málaga, España (36.4163478,-5.1546519), business status OPERATIONAL, primary type seafood_restaurant; about 348 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=7590379949152128262
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/one-hour-beach-restaurants-intake-2026-11-02.md, row rF01).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 53 min by car (59.6 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4163478%2C-5.1546519&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: cost_level
  claim: '"$$ - $$$"'
  source_url: https://www.tripadvisor.com/Restaurant_Review-g187438-d2388981-Reviews-or330-Restaurante_La_Escollera-Estepona_Costa_del_Sol_Province_of_Malaga_Andaluci.html
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: low
  notes: Tripadvisor price marking only (search excerpt); no ratings or reviews recorded. Own-site prices preferred when available. Quote from search snippet of tripadvisor.com listing 'RESTAURANTE LA ESCOLLERA, Estepona'. The .com site shows '$' symbols. Name and town match.
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
- code: cost_level_secondary_source
  severity: info
  fields:
  - cost_level
  description: cost_level is based on the Tripadvisor price marking, not the own menu; replace when an own menu with prices is found.
  retryable: true
  owner: human_editor
created_at: '2026-11-02'
updated_at: '2026-11-03'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
