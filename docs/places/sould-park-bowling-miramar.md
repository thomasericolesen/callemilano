---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-SOULD-PARK-BOWLING-MIRAMAR-001
slug: sould-park-bowling-miramar
name: Sould Park Bowling Miramar
category: Family activities
tags:
- Rainy day
coordinates:
  latitude: 36.5287161
  longitude: -4.6323609
  purpose: venue
  label: Sould Park Bowling Miramar, Av. de la Encarnación, s/n, 29640 Fuengirola, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJ0Z5xKdHjcg0Rk-5vStw8r98, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=16118168508221615763
external_ids:
  google_place_id: ChIJ0Z5xKdHjcg0Rk-5vStw8r98
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 9 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Sould Park Bowling Miramar, Av. de la Encarnación, s/n, 29640 Fuengirola, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5287161,-4.6323609); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5287161%2C-4.6323609&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 9 min, 4.27 km. Walking (Routes API WALK, same day): 51 min, 3.77 km. One predicted sample, not the Google Maps app''s main figure.'
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
  official_website: https://www.souldpark.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Sould Park Bowling Miramar: bowling alley and arcade at the Miramar shopping centre, about 51 min on foot or 9 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Sould Park Bowling Miramar is a bowling alley and arcade at the Miramar shopping centre at Av. de la Encarnación, s/n, 29640 Fuengirola, Málaga. From Casa de la Familia it is about 51 minutes on foot (3.77 km, Google's walking route) or about 9 minutes by car (Google route check, Saturday 10:00). Opening hours, prices, age rules and facilities have not been checked yet; check with the venue before visiting.
seo_title: Sould Park Bowling Miramar, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Sould Park Bowling Miramar (Fuengirola): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Sould Park Bowling CC Miramar - Bolera y Arcade' at Av. de la Encarnación, s/n, 29640 Fuengirola, Málaga, España (36.5287161,-4.6323609), business status OPERATIONAL, website https://www.souldpark.com/.
  source_url: https://maps.google.com/?cid=16118168508221615763
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia, description_long (walking time)
  claim: 'From Casa de la Familia: 9 min by car (4.27 km, Saturday 10:00 predicted traffic) and 51 min on foot (3.77 km).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5287161%2C-4.6323609&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00, and WALK (https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5287161%2C-4.6323609&travelmode=walking). Google's walking route says nothing about pavements, crossings or whether it suits children.
review_issues:
- code: facts_not_checked
  severity: warning
  fields:
  - visit_information
  - cost_level
  - seasonality
  - accessibility
  - booking_required
  - food_available
  - toilets_available
  description: Created from Google Places identity and route checks only. Opening hours, season, prices, age rules, booking and facilities still need the venue's own or official sources.
  retryable: true
  owner: fact_check
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  description: Age groups and family scores are not assessed; energy_level Low is an editorial estimate from the type of place.
  retryable: true
  owner: human_editor
- code: details_not_readable
  severity: warning
  fields:
  - visit_information
  - cost_level
  - age_groups
  description: 'Checked 2026-11-02: The chain website (souldpark.com) gives no readable details for the Miramar bowling. Needs another source or a direct check.'
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
