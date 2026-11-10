---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-NORTE-PUERTO-BANUS-001
slug: norte-puerto-banus
name: Norte Puerto Banús
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.4906174
  longitude: -4.9514172
  purpose: venue
  label: NORTE - Puerto Banús, C. Ramón Areces, Nueva Andalucía, 29660 Marbella, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ63tlFhspcw0RkD0jLu-51Qg, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=636619359265176976
external_ids:
  google_place_id: ChIJ63tlFhspcw0RkD0jLu-51Qg
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 37 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: NORTE - Puerto Banús, C. Ramón Areces, Nueva Andalucía, 29660 Marbella, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4906174,-4.9514172); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4906174%2C-4.9514172&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 37 min, 36.3 km. One predicted sample.'
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
  cost_basis: 'No prices on own site; Tripadvisor price marking "$$ - $$$" read as the middle band. Fallback source per docs/trip-planner-agents.md. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).N'
  cost_checked_at: '2026-11-02'
links:
  official_website: null
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- playa-puerto-banus
description_short: 'Norte Puerto Banús: restaurant near the beach (Marbella). Draft; facts not yet checked.'
description_long: Norte Puerto Banús is listed by Google at C. Ramón Areces, Nueva Andalucía, 29660 Marbella, Málaga, España, about 230 m in a straight line from the beach point of the related beach record. About 37 minutes by car from Casa de la Familia. Menu, opening hours, prices and child-friendliness have not been checked yet.
seo_title: Norte Puerto Banús, Marbella | CalleMilano draft record
seo_description: 'Draft record for Norte Puerto Banús (Marbella): location near the beach and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'NORTE - Puerto Banús' at C. Ramón Areces, Nueva Andalucía, 29660 Marbella, Málaga, España (36.4906174,-4.9514172), business status OPERATIONAL, primary type restaurant; about 230 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=636619359265176976
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/one-hour-beach-restaurants-intake-2026-11-02.md, row rD03).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 37 min by car (36.3 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4906174%2C-4.9514172&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: cost_level
  claim: '"$$ - $$$"'
  source_url: https://www.tripadvisor.com/Restaurant_Review-g1207898-d23587297-Reviews-or30-Norte-Puerto_Banus_Marbella_Costa_del_Sol_Province_of_Malaga_Andalucia.html
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: low
  notes: Tripadvisor price marking only (search excerpt); no ratings or reviews recorded. Own-site prices preferred when available. Quote from search snippet of the tripadvisor.com listing 'NORTE, Puerto Banus'. The .com site shows the marking with '$' symbols. Name and town match.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults high, seniors high; energy_level Low. Owner note (Danish): ''Pintxos restaurant, moderate priser for Puerto Banús''.'
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
updated_at: '2026-11-10'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
