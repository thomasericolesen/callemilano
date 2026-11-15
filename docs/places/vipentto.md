---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-VIPENTTO-001
slug: vipentto
name: Vipentto
category: Restaurants
tags: []
coordinates:
  latitude: 36.5378167
  longitude: -4.6237207
  purpose: venue
  label: Vipentto, C. Troncón, 9, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJPeQAuXfjcg0RbhDD_6HOvaU, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=11942928982032453742
external_ids:
  google_place_id: ChIJPeQAuXfjcg0RbhDD_6HOvaU
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 13 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Vipentto, C. Troncón, 9, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5378167,-4.6237207); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5378167%2C-4.6237207&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 13 min, 5.9 km. One predicted sample.'
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
  schedule: Monday-Sunday 15:00-01:00 (own Instagram, 2026-11-15).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: https://vipentto.com/home/
  booking: null
  visitor_information: null
  transport: null
  contact: https://www.instagram.com/vipentto.es/
related_places: []
description_short: 'Vipentto: Argentine artisan ice-cream shop in Fuengirola, open daily 15:00-01:00, about 13 min by car.'
description_long: Vipentto is an Argentine artisan ice-cream shop on Calle Troncón 9 in Fuengirola, made with natural Italian ingredients and pet-friendly, according to its own Instagram profile. Open every day 15:00-01:00 (checked 2026-11-15). Prices are not published. About 13 minutes by car from Casa de la Familia.
seo_title: Vipentto, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Vipentto (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Vipentto' at C. Troncón, 9, 29640 Fuengirola, Málaga, España (36.5378167,-4.6237207), status OPERATIONAL, type ice_cream_shop.
  source_url: https://maps.google.com/?cid=11942928982032453742
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 13 min by car (5.9 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5378167%2C-4.6237207&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule, description_long, links.contact
  claim: 'Instagram bio: ''🍦Helado artesanal argentino hecho con ingredientes naturales italianos🌿'' / ''🗓Lun-Dom🕐15:00 - 1:00'' / ''#petfriendly'' / ''Troncon 9, Fuengirola 29640''.'
  source_url: https://www.instagram.com/vipentto.es/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (second source attempt 2026-11-15, Claude in Chrome)
  confidence: medium
  notes: Address matches the Google listing. The cloud reader's earlier '13:00 a 01:00' from vipentto.com is superseded; that site did not load. Not the Argentine account @vipentto (La Plata).
- field: status
  claim: 'Lifted needs_fact_check -> needs_editorial_review: own-venue evidence for type, address and hours; no blocking or facts_not_checked issue (editor workflow, level A).'
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
- code: not_found_after_two_attempts
  severity: info
  fields:
  - cost_level
  retryable: true
  owner: fact_check
  description: 'Two source attempts (2026-11-15) found no official answer for: prices. Value left unknown; check before visiting. Retry at the next freshness review.'
created_at: '2026-11-15'
updated_at: '2026-11-15'
last_verified: '2026-11-15'
last_reviewed_at: '2026-11-15'
next_review_at: '2027-04-15'
review_decision: null
redirects: []
---
