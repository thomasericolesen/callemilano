---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-PLAYA-DE-SAN-FRANCISCO-001
slug: playa-de-san-francisco
name: Playa de San Francisco
category: Beaches
tags: []
coordinates:
  latitude: 36.5443693
  longitude: -4.6174365
  purpose: representative_point
  label: Playa de San Francisco, Playa de San Francisco, España (Google Places listing)
  source: Google Places API (New), place ChIJV34OUkLicg0Re40FhUruEe0, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=17082696865419726203
external_ids:
  google_place_id: ChIJV34OUkLicg0Re40FhUruEe0
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 15 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Playa de San Francisco, Playa de San Francisco, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5443693,-4.6174365); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5443693%2C-4.6174365&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 15 min, 6.2 km. One predicted sample.'
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
description_short: 'Playa de San Francisco: a beach, about 15 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Playa de San Francisco is a beach. About 15 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Other facts have not been checked yet.
seo_title: Playa de San Francisco, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Playa de San Francisco (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Playa de San Francisco' at Playa de San Francisco, España (36.5443693,-4.6174365), status OPERATIONAL, type beach.
  source_url: https://maps.google.com/?cid=17082696865419726203
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 15 min by car (6.2 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5443693%2C-4.6174365&travelmode=driving
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
created_at: '2026-11-15'
updated_at: '2026-11-15'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
