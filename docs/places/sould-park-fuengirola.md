---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-SOULD-PARK-FUENGIROLA-001
slug: sould-park-fuengirola
name: Sould Park Fuengirola
category: Family activities
tags: []
coordinates:
  latitude: 36.5434149
  longitude: -4.6182096999999995
  purpose: venue
  label: Sould Park Fuengirola, Puerto Deportivo, P.º Marítimo Rey de España, s/n, 29640 Fuengirola, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJpXWjQA3icg0RkfKr1oVzPnY, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=8520374563700994705
external_ids:
  google_place_id: ChIJpXWjQA3icg0RkfKr1oVzPnY
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 18 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Sould Park Fuengirola, Puerto Deportivo, P.º Marítimo Rey de España, s/n, 29640 Fuengirola, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5434149,-4.6182096999999995); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5434149%2C-4.6182096999999995&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 18 min, 6.71 km. One predicted sample, not the Google Maps app''s main figure.'
age_groups: []
family_score:
  small_children: unknown
  children: unknown
  young_adults: unknown
  seniors: unknown
energy_level: Medium
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
  official_website: http://souldpark.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Sould Park Fuengirola: children''s amusement park at the Fuengirola marina, about 18 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Sould Park Fuengirola is a children's amusement park at the Fuengirola marina at Puerto Deportivo, P.º Marítimo Rey de España, s/n, 29640 Fuengirola, Málaga. From Casa de la Familia it is about 18 minutes by car (Google route check, Saturday 10:00). Opening hours, prices, age rules and facilities have not been checked yet; check with the venue before visiting.
seo_title: Sould Park Fuengirola, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Sould Park Fuengirola (Fuengirola): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Sould Park Fuengirola - Parque infantil y Atracciones' at Puerto Deportivo, P.º Marítimo Rey de España, s/n, 29640 Fuengirola, Málaga, España (36.5434149,-4.6182096999999995), business status OPERATIONAL, website http://souldpark.com/.
  source_url: https://maps.google.com/?cid=8520374563700994705
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 18 min by car (6.71 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5434149%2C-4.6182096999999995&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: 'Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time removed 2026-11-02 (owner decision: walking times of 20 minutes or more are not shown).'
- field: name, municipality
  claim: Operator's amusement-park page lists 'Fuengirola' among its Sould Park parks (link to a Google Maps entry only), separately from CC Miramar.
  source_url: https://www.souldpark.com/ocio/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: low
  notes: Read via Firecrawl on 2026-11-02. Confirms the operator lists a Fuengirola park; no attractions, ages, prices, hours or season given.
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
  description: Age groups and family scores are not assessed; energy_level Medium is an editorial estimate from the type of place.
  retryable: true
  owner: human_editor
- code: details_not_readable
  severity: warning
  fields:
  - visit_information
  - cost_level
  - age_groups
  description: 'Rechecked 2026-11-02: the operator''s site only lists Fuengirola with a map link; no attractions, age limits, prices, hours or season. Needs the operator''s social pages (owner screenshot), a visit or a call (622 60 89 91). 2026-11-02: the chain''s Facebook page ''Sould Park España'' (owner screenshot) lists Fuengirola and Marbella among its locations, price range ''cheap'', phone 622 60 89 91 and WhatsApp 633 89 37 61, but nothing specific to this venue.'
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
