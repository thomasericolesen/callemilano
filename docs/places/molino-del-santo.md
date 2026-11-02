---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-MOLINO-DEL-SANTO-001
slug: molino-del-santo
name: Restaurante El Molino del Santo
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.7127664
  longitude: -5.2498472000000005
  purpose: venue
  label: Molino Del Santo, Bda Estacion, s/n, 29370 Benaoján, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJfdT65lw6DQ0RwXR4kg5IvpA, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=10429853014460757185
external_ids:
  google_place_id: ChIJfdT65lw6DQ0RwXR4kg5IvpA
municipality: Benaoján
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 105 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Molino Del Santo, Bda Estacion, s/n, 29370 Benaoján, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.7127664,-5.2498472000000005); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.7127664%2C-5.2498472000000005&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 105 min, 100.9 km. One predicted sample.'
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
  official_website: http://www.molinodelsanto.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- id: ES-AND-MAL-RONDA-001
  relationship: nearby
  note: Benaoján lies in the Serranía de Ronda.
description_short: 'Restaurante El Molino del Santo: the restaurant of a mill hotel by Benaoján station in the Serranía de Ronda, about 105 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: 'Restaurante El Molino del Santo is the restaurant of a mill hotel by Benaoján station in the Serranía de Ronda. About 105 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Other facts have not been checked yet. Owner''s note (2026-11-02): this is a hotel that is worth the trip for its restaurant; its other facilities are for hotel guests only, so it is not listed as a standalone excursion.'
seo_title: Restaurante El Molino del Santo, Benaoján | CalleMilano draft record
seo_description: 'Draft record for Restaurante El Molino del Santo (Benaoján): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Molino Del Santo' at Bda Estacion, s/n, 29370 Benaoján, Málaga, España (36.7127664,-5.2498472000000005), status OPERATIONAL, type hotel.
  source_url: https://maps.google.com/?cid=10429853014460757185
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner decision 2026-11-02: the hotel is not a standalone excursion; it is visited for its restaurant, and its other facilities are for hotel guests only. Source of the lead: owner''s ''inspiration'' entry on callemilano.dk.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 105 min by car (100.9 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.7127664%2C-5.2498472000000005&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long (owner knowledge), category
  claim: 'Owner 2026-11-02: ''Hotellerne Almagruz, Castillo de Monda og Molino del Santo skal ikke være selvstændige udflugtsmål - de besøges for restauranterne og faciliteterne som ikke kan tilgås uden at være gæst''. Site entry (inspiration): "Ca. 1 time 30 min · Region: Benaoján (Málaga)"'
  source_url: https://callemilano.dk/
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: medium
  notes: Owner instruction in chat plus the owner's inspiration entry on callemilano.dk (Lovable table recommendations). Drive time in the site text is the owner's estimate; the record uses the Routes API figure.
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
- code: guest_only_facilities
  severity: info
  fields:
  - description_long
  - accessibility
  description: Hotel facilities other than the restaurant are for guests only (owner). Check whether the restaurant takes non-resident diners and needs booking.
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
