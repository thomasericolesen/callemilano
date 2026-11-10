---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-JUANITO-JUAN-001
slug: juanito-juan
name: Juanito Juan
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.719518099999995
  longitude: -4.3619905999999995
  purpose: venue
  label: Juanito Juan, Av. Salvador Allende, 26, Málaga-Este, 29017 Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJESBYzLFZcg0Rruh_909V9SE, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=2446955774488864942
external_ids:
  google_place_id: ChIJESBYzLFZcg0Rruh_909V9SE
municipality: Málaga
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 42 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Juanito Juan, Av. Salvador Allende, 26, Málaga-Este, 29017 Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.719518099999995,-4.3619905999999995); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.719518099999995%2C-4.3619905999999995&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 42 min, 46.6 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: medium
  children: medium
  young_adults: high
  seniors: high
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
  cost_basis: 'No own website. Tripadvisor price marking ''€€ - €€€'' (listing ''Restaurante Juanito'', same address) read as the middle band. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03). Fallback source per docs/trip-planner-agents.md.'
  cost_checked_at: '2026-11-02'
links:
  official_website: null
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- playas-del-palo
description_short: 'Juanito Juan: restaurant near the beach (Málaga). Draft; facts not yet checked.'
description_long: Juanito Juan is listed by Google at Av. Salvador Allende, 26, Málaga-Este, 29017 Málaga, España, about 208 m in a straight line from the beach point of the related beach record. About 42 minutes by car from Casa de la Familia. Menu, opening hours, prices and child-friendliness have not been checked yet.
seo_title: Juanito Juan, Málaga | CalleMilano draft record
seo_description: 'Draft record for Juanito Juan (Málaga): location near the beach and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'Juanito Juan' at Av. Salvador Allende, 26, Málaga-Este, 29017 Málaga, España (36.719518099999995,-4.3619905999999995), business status OPERATIONAL, primary type restaurant; about 208 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=2446955774488864942
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/one-hour-beach-restaurants-intake-2026-11-02.md, row rB02).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 42 min by car (46.6 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.719518099999995%2C-4.3619905999999995&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: cost_level, name (identity)
  claim: 'Tripadvisor listing ''RESTAURANTE JUANITO, Málaga'': "€€ - €€€"; photo pages of the same listing (d2715918): "Avenida de Salvador Allende 26, 29017 Malaga Spain".'
  source_url: https://www.tripadvisor.es/Restaurant_Review-g187438-d2715918-Reviews-Restaurante_Juanito-Malaga_Costa_del_Sol_Province_of_Malaga_Andalucia.html
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (main session); source-reader agent
  confidence: low
  notes: Search excerpts only; no ratings or reviews recorded. Identity confirmed by address match with the Google listing 'Juanito Juan, Av. Salvador Allende, 26' (owner screenshot of Google Maps 2026-11-02, which also shows a user-reported 20-30 € per person; Google is not used as price source under AGENTS.md).
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults high, seniors high; energy_level Low. Owner note (Danish): ''Klassisk spansk. Kendt for Grand Marnier - soufflé''.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
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
  description: cost_level is based on the Tripadvisor price marking, not an own menu; no own website exists. Replace if a menu with prices is found.
  retryable: true
  owner: human_editor
created_at: '2026-11-02'
updated_at: '2026-11-10'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
