---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-PARQUE-LA-CANTERA-001
slug: parque-la-cantera
name: Parque La Cantera
category: Nature
tags:
- Nature
- Free
coordinates:
  latitude: 36.5657639
  longitude: -4.6188943
  purpose: representative_point
  label: Parque La Cantera, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJMxizfrPjcg0ROjLo0soXQlU, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=6143499001576043066
external_ids:
  google_place_id: ChIJMxizfrPjcg0ROjLo0soXQlU
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 13 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Parque La Cantera, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5657639,-4.6188943); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5657639%2C-4.6188943&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 13 min, 7.0 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Seniors
family_score:
  small_children: high
  children: high
  young_adults: low
  seniors: medium
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
description_short: 'Parque La Cantera: park in Fuengirola for a walk, exercise or time outdoors as a family, about 13 min by car.'
description_long: Parque La Cantera is a park in Fuengirola. Fuengirola's official map of parks describes it as having everything needed for a walk, exercise or time outdoors as a family (checked 2026-11-15). No playground or opening hours are stated there. About 13 minutes by car from Casa de la Familia.
seo_title: Parque La Cantera, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Parque La Cantera (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Parque La Cantera' at 29640 Fuengirola, Málaga, España (36.5657639,-4.6188943), status OPERATIONAL, type park.
  source_url: https://maps.google.com/?cid=6143499001576043066
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 13 min by car (7.0 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5657639%2C-4.6188943&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long
  claim: '''Este parque contiene todos los elementos necesarios para disfrutar de un paseo, hacer ejercicio o disfrutar en familia al aire libre.'''
  source_url: https://mapas.fuengirola.es/es/parques-y-plazas/resource/r/parque-de-la-cantera
  source_type: government
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
- field: tags, age_groups, family_score, energy_level
  claim: 'Editor decision 2026-11-15 on the tags list: tags = Nature, Free; age_groups = Small children (0-6), Children (7-12), Seniors; family_score = small_children high, children high, young_adults low, seniors medium; energy_level = Low.'
  source_url: https://claude.ai/artifact/VoHiKgGvqiiP3YA66KP3s5
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-15
  confidence: high
  notes: The editor's own judgement; answers stored in collection tags_2026_11_15.
review_issues:
- code: not_found_first_attempt
  severity: warning
  fields:
  - visit_information.schedule
  - toilets_available
  description: 'First source attempt 2026-11-15 found no official answer for: opening hours, playground and toilets. Value left unknown; check before visiting.'
  retryable: true
  owner: fact_check
created_at: '2026-11-15'
updated_at: '2026-11-15'
last_verified: '2026-11-15'
last_reviewed_at: '2026-11-15'
next_review_at: '2027-04-15'
review_decision: null
redirects: []
---
