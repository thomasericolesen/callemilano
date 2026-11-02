---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-ZERO-LATENCY-MIRAMAR-001
slug: zero-latency-miramar
name: Zero Latency Miramar
category: Family activities
tags:
- Rainy day
coordinates:
  latitude: 36.528642999999995
  longitude: -4.6320191
  purpose: venue
  label: Zero Latency Miramar, Av. de la Encarnación, s/n, 29640 Fuengirola, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJncyQDNPjcg0R65KB7DHmwIY, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=9710013898706490091
external_ids:
  google_place_id: ChIJncyQDNPjcg0R65KB7DHmwIY
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 9 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Zero Latency Miramar, Av. de la Encarnación, s/n, 29640 Fuengirola, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.528642999999995,-4.6320191); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.528642999999995%2C-4.6320191&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 9 min, 4.24 km. One predicted sample, not the Google Maps app''s main figure.'
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
  official_website: http://www.zerolatencyvr.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Zero Latency Miramar: free-roam virtual-reality arena at the Miramar shopping centre, about 9 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: 'Zero Latency Miramar is a free-roam virtual-reality arena at the Miramar shopping centre at Av. de la Encarnación, s/n, 29640 Fuengirola, Málaga. From Casa de la Familia it is about 9 minutes by car (Google route check, Saturday 10:00). The operator''s pages (checked 2026-11-02): an arena of more than 200 m² where up to eight players move freely without cables; standard hours Monday-Thursday 15:00-22:00, Friday 13:00-23:00, Saturday 12:00-23:00 and Sunday 12:00-22:00 (the operator notes these may differ on the day). Games last 15-30 minutes, with packages of 45-60 minutes. The age rule is unclear: the Málaga page says there is no fixed minimum age but each game has a minimum height, while the operator''s general FAQ says players must be 13 or older. The FAQ also says the games are generally not suitable for pregnant players, people who need mobility assistance, who are deaf or blind, or who have heart conditions, and that VR can trigger seizures. Prices were not readable. Check with the venue before visiting.'
seo_title: Zero Latency Miramar, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Zero Latency Miramar (Fuengirola): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Zero Latency Miramar' at Av. de la Encarnación, s/n, 29640 Fuengirola, Málaga, España (36.528642999999995,-4.6320191), business status OPERATIONAL, website http://www.zerolatencyvr.com/.
  source_url: https://maps.google.com/?cid=9710013898706490091
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 9 min by car (4.24 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.528642999999995%2C-4.6320191&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: 'Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time removed 2026-11-02 (owner decision: walking times of 20 minutes or more are not shown).'
- field: description_long, visit_information, links
  claim: 'Málaga location page: CC Miramar, Avd. de la Encarnación s/n, 29640 Fuengirola; phone +34 951811105; standard hours Sun 12-22, Mon-Thu 15-22, Fri 13-23, Sat 12-23, ''may differ on the day''.'
  source_url: https://zerolatencyvr.com/es/locations/malaga
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: high
  notes: Read via Firecrawl on 2026-11-02.
- field: description_long, age_groups
  claim: 'Málaga page: arena over 200 m², up to eight players at once without cables or backpacks; ''No existe una edad mínima establecida, aunque los jugadores deben cumplir la altura mínima requerida para cada experiencia''.'
  source_url: https://zerolatencyvr.com/es/malaga
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: medium
  notes: Read via Firecrawl on 2026-11-02. Conflicts with the general FAQ (13+).
- field: description_long, accessibility, age_groups
  claim: 'General FAQ: players must be 13 or older (recommended minimum, some venues differ); experiences last 15-30 min, packages 45-60 min; generally not suitable for pregnant players, people needing mobility assistance, deaf or blind players, or heart conditions; seizure warning; small-frame glasses usually fit.'
  source_url: https://zerolatencyvr.com/es/faqs
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: medium
  notes: Read via Firecrawl on 2026-11-02. Chain-wide rules; the Málaga venue may differ.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  description: Age groups and family scores are not assessed; energy_level Medium is an editorial estimate from the type of place.
  retryable: true
  owner: human_editor
- code: minimum_age_conflict
  severity: warning
  fields:
  - age_groups
  - family_score
  description: The Málaga page says no fixed minimum age (minimum height per game); the chain FAQ says 13+. Confirm with the venue (+34 951811105) before any child suitability claim.
  retryable: true
  owner: fact_check
- code: prices_not_readable
  severity: warning
  fields:
  - cost_level
  description: Prices are only shown in the booking flow, which was not readable. An Instagram excerpt mentioned a Tuesday price of €19.95 (date unknown); not recorded.
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
