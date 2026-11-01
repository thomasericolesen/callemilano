---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-CHIRINGUITO-RAFAEL-001
slug: chiringuito-rafael
name: Chiringuito Rafael
category: Restaurants
tags:
- Restaurant
- Beach
coordinates:
  latitude: 36.599392
  longitude: -4.5102398
  purpose: venue
  label: Chiringuito Rafael, Playa de la Salud, 29630 Benalmádena (Google Places listing)
  source: Google Places API (New) searchText, place ChIJhbPN5G_8cg0RQ0xpdwmEZLU, read 2026-11-01
  checked_at: '2026-11-01'
google_maps_url: https://maps.google.com/?cid=13070717194728983619
external_ids:
  google_place_id: ChIJhbPN5G_8cg0RQ0xpdwmEZLU
municipality: Benalmádena
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 28 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Chiringuito Rafael, Playa de la Salud, 29630 Benalmádena
  source: Google Routes API computeRoutes, run 2026-11-01 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.599392,-4.5102398); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.599392%2C-4.5102398&travelmode=driving
  checked_at: '2026-11-01'
  note: 'Routes API figure: 28 min with predicted Saturday 10:00 traffic (29 min without traffic), 20.3 km via AP-7. One predicted sample, not the Google Maps app''s main figure.'
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
  visitor_information: https://www.facebook.com/rafaelchiringuito/
  transport: null
  contact: null
related_places:
- id: ES-AND-MAL-FUENTE-DE-LA-SALUD-001
  relationship: nearby
  note: Beach bar on Playa de la Salud, by Puerto Marina.
description_short: Seasonal beach bar on Playa de la Salud (Fuente de la Salud), Benalmádena, near Puerto Marina; about 28 minutes by car.
description_long: 'Chiringuito Rafael is a beach bar on Playa de la Salud (Fuente de la Salud) in Benalmádena, on the promenade by Puerto Marina. Its own Facebook page announces each new season, so it is likely seasonal; the season dates were not found. Route check: about 28 minutes from Casa de la Familia (Saturday 10:00, predicted traffic), close to the 30-minute local-area limit. Opening hours, menu, prices, children''s facilities and accessibility are not confirmed by an official source.'
seo_title: Chiringuito Rafael, Benalmádena | CalleMilano draft record
seo_description: 'Draft record for Chiringuito Rafael (Benalmádena): location, drive from Casa de la Familia and what is confirmed so far.'
images: []
evidence:
- field: name, municipality, food_available, links
  claim: The venue's own Facebook page (Chiringuito Rafael, Benalmádena) announces its return for another season.
  source_url: https://www.facebook.com/rafaelchiringuito/
  source_type: official_venue
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: low
  notes: Search-result excerpt of the venue's own page on 2026-11-01; the page itself was not read.
- field: coordinates, google_maps_url, external_ids
  claim: Google Places lists Chiringuito Rafael at Playa de la Salud, 29630 Benalmádena (36.599392,-4.5102398), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=13070717194728983619
  source_type: maps_identity
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: medium
  notes: Google Places API (New) searchText on 2026-11-01. Maps establishes identity and position only, not hours, prices or facilities.
- field: driving_time_from_casa_de_la_familia
  claim: 'One-way drive from Casa de la Familia: 28 min, 20.3 km (Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.599392%2C-4.5102398&travelmode=driving
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
- code: driving_time_near_local_limit
  severity: info
  fields:
  - driving_time_from_casa_de_la_familia
  description: Routes API gives 28 min (Saturday 10:00), close to the 30-min local_30km limit.
  retryable: true
  owner: human_editor
- code: weak_identity_source
  severity: warning
  fields:
  - links
  - evidence
  description: Only the venue's own Facebook page (search excerpt) and Google Places confirm identity; no website or official tourism listing found. Confirm current operation and season before recommending.
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
