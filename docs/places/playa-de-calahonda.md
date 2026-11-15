---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-PLAYA-DE-CALAHONDA-001
slug: playa-de-calahonda
name: Playa de Calahonda
category: Beaches
tags: []
coordinates:
  latitude: 36.4853674
  longitude: -4.738263
  purpose: representative_point
  label: Playa de Calahonda, Playa de Calahonda, España (Google Places listing)
  source: Google Places API (New), place ChIJpX3uuiUgcw0R832ZxF1iweg, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=16771794642174311923
external_ids:
  google_place_id: ChIJpX3uuiUgcw0R832ZxF1iweg
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 20 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Playa de Calahonda, Playa de Calahonda, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4853674,-4.738263); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4853674%2C-4.738263&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 20 min, 14.1 km. One predicted sample.'
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
description_short: 'Playa de Calahonda: long sand beach with some rocks in Mijas Costa, easy access, about 20 min by car.'
description_long: Playa de Calahonda is a 4,4 km beach of sand with some rocks in Mijas Costa, with easy access on foot and by car (Spain's official tourism site, checked 2026-11-15). Rocks on a sand beach do not exclude it from the guide. About 20 minutes by car from Casa de la Familia.
seo_title: Playa de Calahonda, Mijas | CalleMilano draft record
seo_description: 'Draft record for Playa de Calahonda (Mijas): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Playa de Calahonda' at Playa de Calahonda, España (36.4853674,-4.738263), status OPERATIONAL, type beach.
  source_url: https://maps.google.com/?cid=16771794642174311923
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 20 min by car (14.1 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4853674%2C-4.738263&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long (composition, access)
  claim: '''Composición: arena, roca''; ''Longitud: 4400 m''; ''Forma de acceso: A pie fácil,Coche''.'
  source_url: https://www.spain.info/es/playa/calahonda-mijas
  source_type: official_tourism
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
- field: status
  claim: 'Lifted needs_fact_check -> needs_editorial_review: official or own-venue evidence for the core facts, no blocking or facts_not_checked issue (editor workflow, level A).'
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/AGENTS.md
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (main session)
  confidence: high
review_issues:
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
last_verified: '2026-11-15'
last_reviewed_at: '2026-11-15'
next_review_at: '2027-04-15'
review_decision: null
redirects: []
---
