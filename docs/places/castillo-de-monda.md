---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-CASTILLO-DE-MONDA-001
slug: castillo-de-monda
name: Hotel-Restaurante Castillo de Monda
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.6307591
  longitude: -4.835406
  purpose: venue
  label: Hotel - Restaurante Castillo De Monda, C. Castillo, s/n, 29110 Monda, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJO0OZS5jbcg0Rosmsqojo4SE, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=2441488146688166306
external_ids:
  google_place_id: ChIJO0OZS5jbcg0Rosmsqojo4SE
municipality: Monda
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 35 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Hotel - Restaurante Castillo De Monda, C. Castillo, s/n, 29110 Monda, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.6307591,-4.835406); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6307591%2C-4.835406&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 35 min, 29.5 km. One predicted sample.'
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
energy_level: Medium
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
  official_website: http://www.castillodemonda.com/
  booking: null
  visitor_information: https://castillodemonda.com/restaurant-near-marbella/
  transport: null
  contact: null
related_places:
- id: ES-AND-MAL-MONDA-001
  relationship: nearby
  note: Castle hotel above the village.
description_short: 'Hotel-Restaurante Castillo de Monda: the restaurant of a castle hotel above the village of Monda, about 35 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: 'Hotel-Restaurante Castillo de Monda is the restaurant of a castle hotel above the village of Monda. About 35 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Other facts have not been checked yet. Owner''s note (2026-11-02): this is a hotel that is worth the trip for its restaurant; its other facilities are for hotel guests only, so it is not listed as a standalone excursion.'
seo_title: Hotel-Restaurante Castillo de Monda, Monda | CalleMilano draft record
seo_description: 'Draft record for Hotel-Restaurante Castillo de Monda (Monda): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Hotel - Restaurante Castillo De Monda' at C. Castillo, s/n, 29110 Monda, Málaga, España (36.6307591,-4.835406), status OPERATIONAL, type hotel.
  source_url: https://maps.google.com/?cid=2441488146688166306
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner decision 2026-11-02: the hotel is not a standalone excursion; it is visited for its restaurant, and its other facilities are for hotel guests only. Source of the lead: owner''s ''inspiration'' entry on callemilano.dk.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 35 min by car (29.5 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6307591%2C-4.835406&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long (owner knowledge), category
  claim: 'Owner 2026-11-02: ''Hotellerne Almagruz, Castillo de Monda og Molino del Santo skal ikke være selvstændige udflugtsmål - de besøges for restauranterne og faciliteterne som ikke kan tilgås uden at være gæst''. Site entry (inspiration): "Historisk slot ombygget til hotel og restaurant. Vejen op er stejl, men udsigten er turen værd.\n\nFamilie-tip: Kombinér med Mijas eller Marbella.\n\nKøretid fra huset: ca. 45 min."'
  source_url: https://callemilano.dk/
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: medium
  notes: Owner instruction in chat plus the owner's inspiration entry on callemilano.dk (Lovable table recommendations). Drive time in the site text is the owner's estimate; the record uses the Routes API figure.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults high, seniors high; energy_level Medium.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: description_long (restaurant)
  claim: '"Perched on the 6th floor of Castillo de Monda, Albacar Restaurante offers an extraordinary dining experience high above the Andalusian countryside."; "BOOK A TABLE"; "Bar Albacar ... light meals and snacks"'
  source_url: https://castillodemonda.com/restaurant-near-marbella/
  source_type: official_venue
  checked_at: '2026-11-13'
  checked_by: Claude (main session, Claude in Chrome)
  confidence: medium
  notes: Own site read in Claude in Chrome on 2026-11-13. It describes the Albacar restaurant (6th floor), Bar Albacar and a rooftop garden and offers table booking, but gives no opening hours, prices or rule for diners who are not hotel guests. The menu page linked from it was the wine list.
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
- code: guest_only_facilities
  severity: info
  fields:
  - description_long
  - accessibility
  description: Hotel facilities other than the restaurant are for guests only (owner). Check whether the restaurant takes non-resident diners and needs booking.
  retryable: true
  owner: fact_check
- code: second_source_attempt_failed
  severity: warning
  fields:
  - description_long
  - visit_information
  description: 'Second source attempt 2026-11-13: the hotel''s own site (castillodemonda.com) was read; it only shows a ''Book your table'' button on the menus page. No hours, prices, non-resident rule or access found; the restaurant page URLs tried returned 404. Proposed for the editor list (archive or keep as a lead).'
  retryable: false
  owner: editor
created_at: '2026-11-02'
updated_at: '2026-11-13'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
