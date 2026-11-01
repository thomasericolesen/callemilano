---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-LOS-MARINOS-PACO-001
slug: los-marinos-paco
name: Los Marinos Paco
category: Restaurants
tags:
- Restaurant
- Beach
coordinates:
  latitude: 36.5708563
  longitude: -4.5909912
  purpose: venue
  label: Los Marinos Paco, Paseo Marítimo Rey de España 158, 29640 Fuengirola (Google Places listing)
  source: Google Places API (New) searchText, place ChIJ9YgpdRvjcg0RG8NVC6FEW0Y, read 2026-11-01
  checked_at: '2026-11-01'
google_maps_url: https://maps.google.com/?cid=5069721264006218523
external_ids:
  google_place_id: ChIJ9YgpdRvjcg0RG8NVC6FEW0Y
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 17 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Los Marinos Paco, Paseo Marítimo Rey de España 158, 29640 Fuengirola
  source: Google Routes API computeRoutes, run 2026-11-01 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5708563,-4.5909912); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5708563%2C-4.5909912&travelmode=driving
  checked_at: '2026-11-01'
  note: 'Routes API figure: 17 min with predicted Saturday 10:00 traffic (18 min without traffic), 9.0 km via Cam. de Campanales. One predicted sample, not the Google Maps app''s main figure.'
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
booking_required: false
dog_friendly: partial
toilets_available: unknown
food_available: 'yes'
cost_level: Unknown
visit_information:
  schedule: 'Closed Mondays. Summer: Tue-Sat 12:30-22:30, Sun 12:30-17:30. Winter: Tue-Sun 10:00-18:00 (own website, read 2026-11-01; summer/winter dates not stated).'
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: https://www.losmarinospaco.es/
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34952661320
related_places:
- id: ES-AND-MAL-CARVAJAL-001
  relationship: nearby
  note: Beach restaurant on Carvajal beach.
description_short: Family-run fish restaurant and beach bar on Carvajal beach, Fuengirola, with a children's menu and high chairs; about 17 minutes by car.
description_long: 'Los Marinos Paco is a family-run beach restaurant, now in its third generation, at Paseo Marítimo Rey de España 158 on Carvajal beach in Fuengirola. Its own website lists a children''s menu and high chairs, gluten-free dishes and dogs welcome on the terrace. It is closed on Mondays; in summer it opens Tuesday-Saturday 12:30-22:30 and Sunday 12:30-17:30, in winter Tuesday-Sunday 10:00-18:00 (the website does not give the switch-over dates). Bookings are by phone only (952 66 13 20) and are recommended at weekends, on holidays and from June to September. Route check: about 17 minutes from Casa de la Familia (Saturday 10:00, predicted traffic). Prices and accessibility are not confirmed.'
seo_title: Los Marinos Paco, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Los Marinos Paco (Fuengirola): location, drive from Casa de la Familia and what is confirmed so far.'
images: []
evidence:
- field: name, municipality, food_available, links
  claim: 'Own website: family-run beach restaurant (third generation) at Paseo Marítimo Rey de España 158 on Carvajal beach; closed Mondays; summer Tue-Sat 12:30-22:30 and Sun 12:30-17:30, winter Tue-Sun 10:00-18:00; bookings by phone only (952 66 13 20), recommended at weekends, holidays and June-September; children''s menu and high chairs; dogs welcome on the terrace; gluten-free dishes.'
  source_url: https://www.losmarinospaco.es/
  source_type: official_venue
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: high
  notes: Own website read on 2026-11-01.
- field: coordinates, google_maps_url, external_ids
  claim: Google Places lists Los Marinos Paco at Paseo Marítimo Rey de España 158, 29640 Fuengirola (36.5708563,-4.5909912), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=5069721264006218523
  source_type: maps_identity
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: medium
  notes: Google Places API (New) searchText on 2026-11-01. Maps establishes identity and position only, not hours, prices or facilities.
- field: driving_time_from_casa_de_la_familia
  claim: 'One-way drive from Casa de la Familia: 17 min, 9.0 km (Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5708563%2C-4.5909912&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: medium
  notes: Google Routes API computeRoutes; predicted-traffic estimate for one departure time.
- field: dog_friendly, booking_required, description_long (children, gluten-free)
  claim: 'Own website FAQ: children''s menu and high chairs; dogs welcome on the terrace (tell the restaurant when booking); booking recommended but by phone only; gluten-free dishes available.'
  source_url: https://www.losmarinospaco.es/
  source_type: official_venue
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: high
  notes: Own website read on 2026-11-01. 'partial' for dogs because only the terrace is mentioned.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  description: The venue's own website states a children's menu and high chairs (see evidence); age groups and family scores are still left for the editor, and energy_level Low is an editorial default.
  retryable: true
  owner: human_editor
- code: season_and_prices_unverified
  severity: warning
  fields:
  - seasonality
  - cost_level
  - visit_information
  description: Opening hours come from the venue's own website, but the dates when summer and winter hours switch, and prices, are not stated.
  retryable: true
  owner: fact_check
- code: practical_details_unverified
  severity: info
  fields:
  - parking
  - transport_options
  - toilets_available
  - accessibility
  description: Practical and accessibility details were not researched in the restaurant pilot.
  retryable: true
  owner: fact_check
created_at: 2026-11-01
updated_at: 2026-11-01
last_verified: 2026-11-01
last_reviewed_at: null
next_review_at: 2027-04-01
review_decision: null
redirects: []
---
