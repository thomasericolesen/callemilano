---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-MEETING-POINT-CAFE-001
slug: meeting-point-cafe
name: Meeting Point Cafe
category: Restaurants
tags: []
coordinates:
  latitude: 36.589715999999996
  longitude: -4.533528
  purpose: venue
  label: Meeting Point Cafe, Av. las Palmeras, 17, Bq. 4 Local 7, 29630 Benalmádena, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJt5_y5ZL8cg0R7lWzOrJN1IU, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=9643418129991423470
external_ids:
  google_place_id: ChIJt5_y5ZL8cg0R7lWzOrJN1IU
municipality: Benalmádena
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 24 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Meeting Point Cafe, Av. las Palmeras, 17, Bq. 4 Local 7, 29630 Benalmádena, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.589715999999996,-4.533528); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.589715999999996%2C-4.533528&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 24 min, 19.2 km. One predicted sample.'
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
  schedule: Monday-Sunday 7:00-22:30 (own Instagram, 2026-11-15).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: https://instagram.com/meetingpointcafe_?igshid=MTIyMzRjYmRlZg==
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Meeting Point Cafe: pet-friendly brunch café in Benalmádena, open daily 7:00-22:30, about 24 min by car.'
description_long: Meeting Point Cafe in Benalmádena is a pet-friendly café for breakfast, brunch, cakes and desserts, and also pizza. Its own Instagram profile gives daily hours of 7:00-22:30 (checked 2026-11-15). Prices are not published. About 24 minutes by car from Casa de la Familia.
seo_title: Meeting Point Cafe, Benalmádena | CalleMilano draft record
seo_description: 'Draft record for Meeting Point Cafe (Benalmádena): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Meeting Point Cafe' at Av. las Palmeras, 17, Bq. 4 Local 7, 29630 Benalmádena, Málaga, España (36.589715999999996,-4.533528), status OPERATIONAL, type coffee_shop.
  source_url: https://maps.google.com/?cid=9643418129991423470
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 24 min by car (19.2 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.589715999999996%2C-4.533528&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule, description_long
  claim: 'Instagram bio: ''Café | #Chillcoffe #Petfriendly | #Desayunos, #Brunch, #Tartas, #Postres ... #pizza'' / ''⏰L~D: 7:00-22:30''.'
  source_url: https://instagram.com/meetingpointcafe_
  source_type: official_venue
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
- code: not_found_first_attempt
  severity: warning
  fields:
  - cost_level
  description: 'First source attempt 2026-11-15 found no official answer for: prices. Value left unknown; check before visiting.'
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
