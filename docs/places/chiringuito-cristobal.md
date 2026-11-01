---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-CHIRINGUITO-CRISTOBAL-001
slug: chiringuito-cristobal
name: Chiringuito Cristóbal
category: Restaurants
tags:
- Restaurant
- Beach
coordinates:
  latitude: 36.5003692
  longitude: -4.682398
  purpose: venue
  label: Chiringuito Cristóbal, C. Butibamba, 26, 29649 La Cala de Mijas (Google Places listing)
  source: Google Places API (New) searchText, place ChIJN9nfFDQecw0RNeKzx_ykrlw, read 2026-11-01
  checked_at: '2026-11-01'
google_maps_url: https://maps.google.com/?cid=6678456703026192949
external_ids:
  google_place_id: ChIJN9nfFDQecw0RNeKzx_ykrlw
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 15 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Chiringuito Cristóbal, C. Butibamba, 26, 29649 La Cala de Mijas
  source: Google Routes API computeRoutes, run 2026-11-01 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5003692,-4.682398); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5003692%2C-4.682398&travelmode=driving
  checked_at: '2026-11-01'
  note: 'Routes API figure: 15 min with predicted Saturday 10:00 traffic (15 min without traffic), 6.7 km via Arrabal Sector 13. One predicted sample, not the Google Maps app''s main figure.'
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
  official_website: null
  booking: null
  visitor_information: https://turismo.mijas.es/es/gastronomia/donde-comer/chiringuitos/chiringuito-cristobal
  transport: null
  contact: tel:+34692899163
related_places:
- id: ES-AND-MAL-LA-BUTIBAMBA-001
  relationship: nearby
  note: Beach bar on Playa La Butibamba.
description_short: Beach bar (chiringuito) on Playa La Butibamba in La Cala de Mijas, listed by Turismo de Mijas; about 15 minutes by car from Casa de la Familia.
description_long: 'Chiringuito Cristóbal is a beach bar on Playa La Butibamba (La Cala, Mijas), listed in the beach-bar section of the official Mijas tourism site with phone 692 899 163. Google lists it as Kiosko Cristóbal at C. Butibamba 26. Route check: about 15 minutes from Casa de la Familia (Saturday 10:00, predicted traffic). Opening hours, season, prices, menu, children''s facilities and accessibility are not confirmed by an official source; beach bars on this coast often reduce hours or close out of season, so check before going.'
seo_title: Chiringuito Cristóbal, Mijas | CalleMilano draft record
seo_description: 'Draft record for Chiringuito Cristóbal (Mijas): location, drive from Casa de la Familia and what is confirmed so far.'
images: []
evidence:
- field: name, municipality, food_available, links
  claim: Turismo de Mijas lists Chiringuito Cristóbal under beach bars at Playa La Butibamba (La Cala), phone 692 899 163, e-mail kioscocristobal@hotmail.com.
  source_url: https://turismo.mijas.es/es/gastronomia/donde-comer/chiringuitos/chiringuito-cristobal
  source_type: official_tourism
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: high
  notes: Read on 2026-11-01.
- field: coordinates, google_maps_url, external_ids
  claim: Google Places lists Chiringuito Cristóbal at C. Butibamba, 26, 29649 La Cala de Mijas (36.5003692,-4.682398), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=6678456703026192949
  source_type: maps_identity
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: medium
  notes: Google Places API (New) searchText on 2026-11-01. Maps establishes identity and position only, not hours, prices or facilities.
- field: driving_time_from_casa_de_la_familia
  claim: 'One-way drive from Casa de la Familia: 15 min, 6.7 km (Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5003692%2C-4.682398&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: medium
  notes: Google Routes API computeRoutes; predicted-traffic estimate for one departure time.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  description: No source on children's menu, high chairs, play area or family suitability was checked; age groups and family scores are left unknown/empty and energy_level Low is an editorial default for a restaurant visit. Needs editor assessment.
  retryable: true
  owner: human_editor
- code: season_and_prices_unverified
  severity: warning
  fields:
  - seasonality
  - cost_level
  - visit_information
  description: Season, opening hours (where not stated) and prices are not confirmed by an official source; beach bars often change hours out of season.
  retryable: true
  owner: fact_check
- code: practical_details_unverified
  severity: info
  fields:
  - parking
  - transport_options
  - dog_friendly
  - toilets_available
  - accessibility
  - booking_required
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
