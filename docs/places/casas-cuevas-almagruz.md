---
schema_version: 1.0.0
status: archived
id: ES-AND-GRA-CASAS-CUEVAS-ALMAGRUZ-001
slug: casas-cuevas-almagruz
name: Casas Cuevas Almagruz
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 37.3335548
  longitude: -3.2253194
  purpose: venue
  label: Casas Cuevas Almagruz y Centro de Interpretación Hábitat Troglodita Almagruz, Purullena, Granada, España (Google Places listing)
  source: Google Places API (New), place ChIJaY4kRmgpbg0RYoCnYCF9Qzo, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=4198336859948417122
external_ids:
  google_place_id: ChIJaY4kRmgpbg0RYoCnYCF9Qzo
municipality: Purullena
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 120 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Casas Cuevas Almagruz y Centro de Interpretación Hábitat Troglodita Almagruz, Purullena, Granada, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (37.3335548,-3.2253194); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=37.3335548%2C-3.2253194&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 120 min, 198.5 km. One predicted sample.'
age_groups: []
family_score:
  small_children: unknown
  children: unknown
  young_adults: unknown
  seniors: unknown
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
  official_website: http://www.cuevasalmagruz.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Casas Cuevas Almagruz: a cave-house hotel with restaurant in Purullena near Guadix, about 120 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: 'Casas Cuevas Almagruz is a cave-house hotel with restaurant in Purullena near Guadix. About 120 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Other facts have not been checked yet. Owner''s note (2026-11-02): this is a hotel that is worth the trip for its restaurant; its other facilities are for hotel guests only, so it is not listed as a standalone excursion.'
seo_title: Casas Cuevas Almagruz, Purullena | CalleMilano draft record
seo_description: 'Draft record for Casas Cuevas Almagruz (Purullena): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Casas Cuevas Almagruz y Centro de Interpretación Hábitat Troglodita Almagruz' at Purullena, Granada, España (37.3335548,-3.2253194), status OPERATIONAL, type hotel.
  source_url: https://maps.google.com/?cid=4198336859948417122
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner decision 2026-11-02: the hotel is not a standalone excursion; it is visited for its restaurant, and its other facilities are for hotel guests only. Source of the lead: owner''s ''inspiration'' entry on callemilano.dk.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 120 min by car (198.5 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=37.3335548%2C-3.2253194&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long (owner knowledge), category
  claim: 'Owner 2026-11-02: ''Hotellerne Almagruz, Castillo de Monda og Molino del Santo skal ikke være selvstændige udflugtsmål - de besøges for restauranterne og faciliteterne som ikke kan tilgås uden at være gæst''. Site entry (inspiration): "Ca. 2 timer · Region: Granada"'
  source_url: https://callemilano.dk/
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: medium
  notes: Owner instruction in chat plus the owner's inspiration entry on callemilano.dk (Lovable table recommendations). Drive time in the site text is the owner's estimate; the record uses the Routes API figure.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children unknown, children unknown, young_adults unknown, seniors unknown; energy_level Medium. Owner note (Danish): ''Hotel hugget ud i klipperne med restaurant''.'
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
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - tags
  description: 'Owner answered ''Ved ikke'' (or left blank) on the 2026-11-10 checklist for: small_children, children, young_adults, seniors. Energy level set by owner. Tags not assessed.'
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
  notes: 'Owner decision 2026-11-11: too much effort to get usable facts (draft with no verified facts, 2 h drive away and owner answered "Ved ikke" on family suitability); we already have enough restaurants. Kept as archive; the ID stays allocated and must not be reused.'
redirects: []
---
