---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-TABERNA-MAR-DE-ALBORAN-ESTEPONA-001
slug: taberna-mar-de-alboran-estepona
name: Taberna Mar de Alborán (Estepona)
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.4159394
  longitude: -5.1588487999999995
  purpose: venue
  label: Taberna Mar de Alboran, Av. Luis Braille, 17, 29680 Estepona, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJJUz8cLTWDA0RbUpbt6--f_M, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=17545952335163509357
external_ids:
  google_place_id: ChIJJUz8cLTWDA0RbUpbt6--f_M
municipality: Estepona
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 52 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Taberna Mar de Alboran, Av. Luis Braille, 17, 29680 Estepona, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4159394,-5.1588487999999995); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4159394%2C-5.1588487999999995&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 52 min, 59.4 km. One predicted sample.'
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
  official_website: https://es-es.facebook.com/taberna.mardealboran.1
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- playa-de-la-rada-estepona
description_short: 'Taberna Mar de Alborán (Estepona): taverna near the beach (Estepona). Draft; facts not yet checked.'
description_long: Taberna Mar de Alborán (Estepona) is listed by Google at Av. Luis Braille, 17, 29680 Estepona, Málaga, España, about 676 m in a straight line from the beach point of the related beach record. About 52 minutes by car from Casa de la Familia. Menu, opening hours, prices and child-friendliness have not been checked yet.
seo_title: Taberna Mar de Alborán (Estepona), Estepona | CalleMilano draft record
seo_description: 'Draft record for Taberna Mar de Alborán (Estepona) (Estepona): location near the beach and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'Taberna Mar de Alboran' at Av. Luis Braille, 17, 29680 Estepona, Málaga, España (36.4159394,-5.1588487999999995), business status OPERATIONAL, primary type restaurant; about 676 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=17545952335163509357
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/one-hour-beach-restaurants-intake-2026-11-02.md, row rF04).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 52 min by car (59.4 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4159394%2C-5.1588487999999995&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
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
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
