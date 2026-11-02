---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-FUENGIROLA-ADVENTURE-GOLF-001
slug: fuengirola-adventure-golf
name: Fuengirola Adventure Golf
category: Family activities
tags: []
coordinates:
  latitude: 36.532201
  longitude: -4.632048999999999
  purpose: venue
  label: Fuengirola Adventure Golf, Parque Fluvial, 29640 Fuengirola, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJZ4JOQgzicg0RwGNz_8aaJxo, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=1884645148557796288
external_ids:
  google_place_id: ChIJZ4JOQgzicg0RwGNz_8aaJxo
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 9 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Fuengirola Adventure Golf, Parque Fluvial, 29640 Fuengirola, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.532201,-4.632048999999999); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.532201%2C-4.632048999999999&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 9 min, 4.5 km. Walking (Routes API WALK, same day): 50 min, 3.67 km. One predicted sample, not the Google Maps app''s main figure.'
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
  typical_duration: About 1 hour per game (own website)
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: http://www.fuengirolaadventuregolf.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Fuengirola Adventure Golf: mini golf course in the Parque Fluvial, about 50 min on foot or 9 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: Fuengirola Adventure Golf is a mini golf course in the Parque Fluvial at Parque Fluvial, 29640 Fuengirola, Málaga. From Casa de la Familia it is about 50 minutes on foot (3.67 km, Google's walking route) or about 9 minutes by car (Google route check, Saturday 10:00). Its own website describes a 19-hole adventure mini golf course for all ages, with a bar and restaurant; a game takes about one hour. Opening hours and prices were not readable on the homepage.
seo_title: Fuengirola Adventure Golf, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Fuengirola Adventure Golf (Fuengirola): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Fuengirola Adventure Golf' at Parque Fluvial, 29640 Fuengirola, Málaga, España (36.532201,-4.632048999999999), business status OPERATIONAL, website http://www.fuengirolaadventuregolf.com/.
  source_url: https://maps.google.com/?cid=1884645148557796288
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia, description_long (walking time)
  claim: 'From Casa de la Familia: 9 min by car (4.5 km, Saturday 10:00 predicted traffic) and 50 min on foot (3.67 km).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.532201%2C-4.632048999999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00, and WALK (https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.532201%2C-4.632048999999999&travelmode=walking). Google's walking route says nothing about pavements, crossings or whether it suits children.
- field: visit_information.typical_duration, description_long
  claim: 'Own website (page metadata): "19 hole putting adventure for all ages and skills with bar and restaurant"; "A game of Adventure Golf takes approximately 1hr".'
  source_url: http://www.fuengirolaadventuregolf.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: medium
  notes: Read from the homepage description and social metadata via Firecrawl on 2026-11-02; body text not captured.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  description: Age groups and family scores are not assessed; energy_level Low is an editorial estimate from the type of place.
  retryable: true
  owner: human_editor
- code: hours_and_prices_unknown
  severity: warning
  fields:
  - visit_information
  - cost_level
  description: Opening hours and prices still need checking.
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: '2026-11-02'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
