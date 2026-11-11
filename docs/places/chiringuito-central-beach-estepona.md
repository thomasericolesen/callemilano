---
schema_version: 1.0.0
status: archived
id: ES-AND-MAL-CHIRINGUITO-CENTRAL-BEACH-ESTEPONA-001
slug: chiringuito-central-beach-estepona
name: Chiringuito Central Beach (Estepona)
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.4228141
  longitude: -5.1471539
  purpose: venue
  label: Chiringuito Central Beach, Glorieta Juan Carlos I, S/N, 29680 Estepona, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJhYwK8h7UDA0RwtF1odozYUQ, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=4927276481424773570
external_ids:
  google_place_id: ChIJhYwK8h7UDA0RwtF1odozYUQ
municipality: Estepona
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 53 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Chiringuito Central Beach, Glorieta Juan Carlos I, S/N, 29680 Estepona, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4228141,-5.1471539); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4228141%2C-5.1471539&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 53 min, 59.1 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: medium
  children: high
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
  cost_basis: 'No prices on own site; Tripadvisor price marking "€€ - €€€" read as the middle band. Fallback source per docs/trip-planner-agents.md. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).N'
  cost_checked_at: '2026-11-02'
links:
  official_website: null
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- playa-de-la-rada-estepona
description_short: 'Chiringuito Central Beach (Estepona): strandrestaurant (chiringuito) near the beach (Estepona). Draft; facts not yet checked.'
description_long: Chiringuito Central Beach (Estepona) is listed by Google at Glorieta Juan Carlos I, S/N, 29680 Estepona, Málaga, España, about 636 m in a straight line from the beach point of the related beach record. About 53 minutes by car from Casa de la Familia. Menu, opening hours, prices and child-friendliness have not been checked yet.
seo_title: Chiringuito Central Beach (Estepona), Estepona | CalleMilano draft record
seo_description: 'Draft record for Chiringuito Central Beach (Estepona) (Estepona): location near the beach and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'Chiringuito Central Beach' at Glorieta Juan Carlos I, S/N, 29680 Estepona, Málaga, España (36.4228141,-5.1471539), business status OPERATIONAL, primary type bar; about 636 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=4927276481424773570
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/one-hour-beach-restaurants-intake-2026-11-02.md, row rF03).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 53 min by car (59.1 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4228141%2C-5.1471539&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: cost_level
  claim: '"€€ - €€€"'
  source_url: https://www.tripadvisor.es/Restaurant_Review-g187437-d7950104-Reviews-Chiringuito_Central_Beach-Estepona_Costa_del_Sol_Province_of_Malaga_Andalucia.html
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: low
  notes: Tripadvisor price marking only (search excerpt); no ratings or reviews recorded. Own-site prices preferred when available. Quote from search snippet of tripadvisor.es listing. Name and town match (Estepona). A TheFork page for 'La Central' in Estepona appeared but is a different restaurant and was not used.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children unknown, children high, young_adults high, seniors high; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children high, young_adults high, seniors high; energy_level Low. Replaces the owner''s earlier answer on the same checklist.'
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
  description: cost_level is based on the Tripadvisor price marking, not the own menu; replace when an own menu with prices is found.
  retryable: true
  owner: human_editor
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision:
  decision: archived
  reviewer: Eric Olesen (editor-of-record)
  date: '2026-11-11'
  notes: 'Owner decision 2026-11-11 on the editor list (https://claude.ai/artifact/C1Lu1WExnpBw8YRw5K1Jrc): archive (no readable own source, price only from a secondary source); we already have enough places. Kept as archive; the ID stays allocated and must not be reused.'
redirects: []
---
