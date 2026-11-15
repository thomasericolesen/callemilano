---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-FERRUM-RESTAURANTE-001
slug: ferrum-restaurante
name: Ferrum Restaurante
category: Restaurants
tags: []
coordinates:
  latitude: 36.539007999999995
  longitude: -4.6211379
  purpose: venue
  label: Ferrum Restaurante, C. Moncayo, 20, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJy_huOTzjcg0RLKBDDXA2-58, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=11527867526071689260
external_ids:
  google_place_id: ChIJy_huOTzjcg0RLKBDDXA2-58
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 17 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Ferrum Restaurante, C. Moncayo, 20, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.539007999999995,-4.6211379); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.539007999999995%2C-4.6211379&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 17 min, 6.7 km. One predicted sample.'
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
  official_website: https://www.instagram.com/ferrumfuengirola/
  booking: null
  visitor_information: null
  transport: null
  contact: +34 604299443
related_places: []
description_short: 'Ferrum Restaurante: restaurant in Fuengirola, about 17 min by car. Hours and prices not yet found.'
description_long: Ferrum is a restaurant at Calle Moncayo 20 in Fuengirola, according to its own Instagram profile, which takes bookings on +34 604 299 443. Opening hours, prices and children's facilities were not found (checked 2026-11-15); check before visiting. About 17 minutes by car from Casa de la Familia.
seo_title: Ferrum Restaurante, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Ferrum Restaurante (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Ferrum Restaurante' at C. Moncayo, 20, 29640 Fuengirola, Málaga, España (36.539007999999995,-4.6211379), status OPERATIONAL, type mediterranean_restaurant.
  source_url: https://maps.google.com/?cid=11527867526071689260
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 17 min by car (6.7 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.539007999999995%2C-4.6211379&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long, links.contact
  claim: 'Instagram bio: ''Restaurant'' / ''Disfruta de la excelencia culinaria en Fuengirola.'' / ''Reservas/Booking: +34 604299443'' / ''Calle Moncayo 20, Fuengirola 29640''.'
  source_url: https://www.instagram.com/ferrumfuengirola/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: low
  notes: Highlight 'Horarios' not opened (Mac session).
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
  description: 'First source attempt 2026-11-15 found no official answer for: opening hours (Instagram highlight ''Horarios'' not opened), prices, children''s facilities. Value left unknown; check before visiting.'
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
