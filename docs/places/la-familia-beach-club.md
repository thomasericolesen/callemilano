---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-LA-FAMILIA-BEACH-CLUB-001
slug: la-familia-beach-club
name: La Familia Beach Club
category: Restaurants
tags: []
coordinates:
  latitude: 36.494167999999995
  longitude: -4.6901515
  purpose: venue
  label: La Familia Beach Club, Playa del Bombo Urbanización Torrenueva, 20, 29649 Mijas, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJOXNSv7Ufcw0R9PBU2RKjed8, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=16103081243990880500
external_ids:
  google_place_id: ChIJOXNSv7Ufcw0R9PBU2RKjed8
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 14 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: La Familia Beach Club, Playa del Bombo Urbanización Torrenueva, 20, 29649 Mijas, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.494167999999995,-4.6901515); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.494167999999995%2C-4.6901515&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 14 min, 8.5 km. One predicted sample.'
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
cost_level: €€
visit_information:
  schedule: Daily 10:00-20:00 September-May; 10:00-22:00 June-August (own website, 2026-11-15). No closing days stated.
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Menu 2026: mains about 15-29 €; bread and butter 1,80 €.'
  cost_checked_at: '2026-11-15'
links:
  official_website: http://www.lafamilia-beachclub.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'La Familia Beach Club: beach restaurant on Playa del Bombo, Mijas Costa, about 14 min by car.'
description_long: La Familia Beach Club is a beach restaurant on Playa del Bombo (Urbanización Torrenueva) in Mijas Costa, serving fish, seafood and espetos. Open daily 10:00-20:00 from September to May and 10:00-22:00 in June, July and August (own website, checked 2026-11-15). The 2026 menu has mains at about 15-29 €, rice from 18,50 € per person (min. 2), and simple dishes such as chicken strips (9,50 €) and spaghetti bolognese (15,50 €), though there is no children's menu as such. About 14 minutes by car from Casa de la Familia.
seo_title: La Familia Beach Club, Mijas | CalleMilano draft record
seo_description: 'Draft record for La Familia Beach Club (Mijas): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'La Familia Beach Club' at Playa del Bombo Urbanización Torrenueva, 20, 29649 Mijas, Málaga, España (36.494167999999995,-4.6901515), status OPERATIONAL, type mediterranean_restaurant.
  source_url: https://maps.google.com/?cid=16103081243990880500
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 14 min by car (8.5 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.494167999999995%2C-4.6901515&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule, description_long
  claim: '''Un restaurante situado en Mijas Costa, en la Playa del Bombo''; ''De Septiembre a Mayo: 10h00 – 20h00'' / ''Junio, Julio y Agosto : 10h00 – 22h00''; ''Urbanización Torrenueva Playa del Bombo, s.n. 29649 Mijas''.'
  source_url: http://www.lafamilia-beachclub.com/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
- field: cost_level, visit_information.cost_basis
  claim: 'Menu 2026: ''Patatas Fritas 4,5€'', ''Palitos de Pollo 9,5€'', ''Spaghetti Boloñesa 15,5€'', ''Arroz Mixto (min. 2 personas) 18,5€'', ''Dorada al Espeto o a la Plancha 27€'', ''Lenguado a la Plancha 28,5€''; ''Servicio de Pan y Mantequilla 1.80€''. No children''s menu.'
  source_url: https://lafamilia-beachclub.com/wp-content/uploads/2026/06/180526_LF_Menu2026-langostinos.pdf
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
created_at: '2026-11-15'
updated_at: '2026-11-15'
last_verified: '2026-11-15'
last_reviewed_at: '2026-11-15'
next_review_at: '2027-04-15'
review_decision: null
redirects: []
---
