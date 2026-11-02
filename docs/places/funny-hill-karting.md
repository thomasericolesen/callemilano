---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-FUNNY-HILL-KARTING-001
slug: funny-hill-karting
name: Funny Hill Karting
category: Family activities
tags: []
coordinates:
  latitude: 36.5431404
  longitude: -4.8651938
  purpose: venue
  label: Funny Hill Karting, Carretera antigua de Ojén-Marbella, Poligono 1, parcela 493 Cañada de Murta, 29610 Ojén, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJt4Lv8T7Zcg0Rflv-j9_NYiI, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=2477769105084406654
external_ids:
  google_place_id: ChIJt4Lv8T7Zcg0Rflv-j9_NYiI
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 34 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Funny Hill Karting, Carretera antigua de Ojén-Marbella, Poligono 1, parcela 493 Cañada de Murta, 29610 Ojén, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5431404,-4.8651938); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5431404%2C-4.8651938&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 34 min, 31.1 km. One predicted sample.'
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
  official_website: https://funnyhill.es/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Funny Hill Karting: a go-kart track on the old Ojén road above Marbella, about 34 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Funny Hill Karting is a go-kart track on the old Ojén road above Marbella. About 34 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Other facts have not been checked yet.
seo_title: Funny Hill Karting, Marbella | CalleMilano draft record
seo_description: 'Draft record for Funny Hill Karting (Marbella): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Funny Hill Karting' at Carretera antigua de Ojén-Marbella, Poligono 1, parcela 493 Cañada de Murta, 29610 Ojén, Málaga, España (36.5431404,-4.8651938), status OPERATIONAL, type go_karting_venue.
  source_url: https://maps.google.com/?cid=2477769105084406654
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Places API (New). Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 34 min by car (31.1 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5431404%2C-4.8651938&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
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
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
