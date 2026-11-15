---
schema_version: 1.0.0
status: archived
id: ES-AND-MAL-HELADERIA-SAN-MIGUEL-DESAYUNOS-001
slug: heladeria-san-miguel-desayunos
name: Heladería San Miguel Desayunos
category: Restaurants
tags: []
coordinates:
  latitude: 36.6096704
  longitude: -4.5038556
  purpose: venue
  label: Heladería San Miguel Desayunos, Costa de la Carihuela, 87, 29620 Torremolinos, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJPcvXSf79cg0RSK7OwyLtry8, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=3436225774276750920
external_ids:
  google_place_id: ChIJPcvXSf79cg0RSK7OwyLtry8
municipality: Torremolinos
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 30 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Heladería San Miguel Desayunos, Costa de la Carihuela, 87, 29620 Torremolinos, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.6096704,-4.5038556); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6096704%2C-4.5038556&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 30 min, 21.0 km. One predicted sample.'
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
description_short: 'Heladería San Miguel Desayunos: an ice-cream shop, about 30 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Heladería San Miguel Desayunos is an ice-cream shop. About 30 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Other facts have not been checked yet.
seo_title: Heladería San Miguel Desayunos, Torremolinos | CalleMilano draft record
seo_description: 'Draft record for Heladería San Miguel Desayunos (Torremolinos): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Heladería San Miguel Desayunos' at Costa de la Carihuela, 87, 29620 Torremolinos, Málaga, España (36.6096704,-4.5038556), status OPERATIONAL, type ice_cream_shop.
  source_url: https://maps.google.com/?cid=3436225774276750920
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 30 min by car (21.0 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6096704%2C-4.5038556&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
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
- code: no_readable_own_source
  severity: warning
  fields:
  - visit_information.schedule
  - cost_level
  - description_long
  description: 'First source attempt 2026-11-15: Google Maps lists no website or social media and no official source was found. Only identity and drive time are known.'
  retryable: true
  owner: fact_check
created_at: '2026-11-15'
updated_at: '2026-11-15'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision:
  decision: archived
  reviewer: Eric Olesen (editor-of-record)
  date: '2026-11-15'
  notes: 'Owner decision 2026-11-15 (chat): make a second attempt on the six drafts without a source and archive those that still fail. Second attempt 2026-11-15: web search found only third-party listings (two different addresses); the only Facebook page named ''Heladeria San Miguel'' sells soft ice cream and ice lollies elsewhere and is not this café; no Instagram found. Kept as archive; the ID stays allocated and must not be reused.'
redirects: []
---
