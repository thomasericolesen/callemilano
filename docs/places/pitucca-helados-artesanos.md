---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-PITUCCA-HELADOS-ARTESANOS-001
slug: pitucca-helados-artesanos
name: Pitucca Helados Artesanos
category: Restaurants
tags: []
coordinates:
  latitude: 36.538078399999996
  longitude: -4.6213681
  purpose: venue
  label: Pitucca Helados Artesanos, P.º Marítimo Rey de España, 28, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ80qBpGvicg0Rtm1b2fjOaQM, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=245955222862261686
external_ids:
  google_place_id: ChIJ80qBpGvicg0Rtm1b2fjOaQM
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 15 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Pitucca Helados Artesanos, P.º Marítimo Rey de España, 28, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.538078399999996,-4.6213681); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.538078399999996%2C-4.6213681&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 15 min, 6.3 km. One predicted sample.'
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
food_available: 'yes'
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
  official_website: http://facebook.com/pituccahelados
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Pitucca Helados Artesanos: artisan ice-cream shop on the Fuengirola promenade, about 15 min by car. Hours not yet found.'
description_long: Pitucca is an artisan ice-cream and sweets shop at Paseo Marítimo Rey de España 28 in Fuengirola, according to its own Facebook page. Hours and prices were not visible (checked 2026-11-15); check before visiting. About 15 minutes by car from Casa de la Familia.
seo_title: Pitucca Helados Artesanos, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Pitucca Helados Artesanos (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Pitucca Helados Artesanos' at P.º Marítimo Rey de España, 28, 29640 Fuengirola, Málaga, España (36.538078399999996,-4.6213681), status OPERATIONAL, type ice_cream_shop.
  source_url: https://maps.google.com/?cid=245955222862261686
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 15 min by car (6.3 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.538078399999996%2C-4.6213681&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long
  claim: 'Facebook: ''Heladería Artesanal - Dulces Artesanos'', ''Paseo Maritimo Rey de España Nº 28, Fuengirola''.'
  source_url: http://facebook.com/pituccahelados
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: low
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
- code: not_found_first_attempt
  severity: warning
  fields:
  - visit_information.schedule
  - cost_level
  description: 'First source attempt 2026-11-15 found no official answer for: opening hours and prices. Value left unknown; check before visiting.'
  retryable: true
  owner: fact_check
created_at: '2026-11-15'
updated_at: '2026-11-15'
last_verified: '2026-11-15'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
