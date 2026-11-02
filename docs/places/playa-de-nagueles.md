---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-PLAYA-DE-NAGUELES-001
slug: playa-de-nagueles
name: Playa de Nagüeles
category: Beaches
tags:
- Beach
coordinates:
  latitude: 36.5022476
  longitude: -4.9213001
  purpose: representative_point
  label: Playa de Nagüeles, Playa de Nagüeles, 29602 Marbella, España (Google Places listing); not a parking point
  source: Google Places API (New), place ChIJcQhxdSQocw0R5cB8JTUjRcU, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=14214806510034010341
external_ids:
  google_place_id: ChIJcQhxdSQocw0R5cB8JTUjRcU
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 36 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Playa de Nagüeles, Playa de Nagüeles, 29602 Marbella, España (Google Places point, not a parking point)
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5022476,-4.9213001); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5022476%2C-4.9213001&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 36 min, 32.0 km. One predicted sample, not the Google Maps app''s main figure.'
age_groups: []
family_score:
  small_children: unknown
  children: unknown
  young_adults: unknown
  seniors: unknown
energy_level: Low
seasonality:
- Spring
- Summer
- Autumn
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
  official_website: null
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Playa de Nagüeles, Marbella: golden-sand beach on the Golden Mile; Blue Flag 2026 (Nagüeles-Casablanca).'
description_long: 'Playa de Nagüeles lies on Marbella''s Golden Mile between the town and Puerto Banús. Spain.info (Turespaña) lists golden sand, moderate waves, about 1,600 m by 40 m, high occupancy, semi-urban, easy access on foot, and services including sunbed and parasol hire, water-sports hire and showers; toilets are not listed. Blue Flag 2026 under the name Nagüeles-Casablanca. Rocks: the official sources describe a sand beach with easy access on foot, so it meets the project''s beach rule (owner decision 2026-11-02). About 36 minutes by car from Casa de la Familia.'
seo_title: Playa de Nagüeles, Marbella | CalleMilano
seo_description: 'Playa de Nagüeles (Marbella): sand, facilities, Blue Flag status and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Playa de Nagüeles' at Playa de Nagüeles, 29602 Marbella, España (36.5022476,-4.9213001), business status OPERATIONAL, primary type beach.
  source_url: https://maps.google.com/?cid=14214806510034010341
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Maps establishes identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 36 min by car (32.0 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5022476%2C-4.9213001&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL, Saturday 2026-11-07 10:00.
- field: description_long
  claim: 'Spain.info: Nagüeles, sand (golden), moderate waves, 1,600 x 40 m, high occupancy, semi-urban, easy access on foot; services: parasol and sunbed hire, water-sports hire, showers, tourist office, bins, cleaning.'
  source_url: https://www.spain.info/es/playa/nagueles/
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour beach fact check 2026-11-02)
  confidence: medium
  notes: Turespaña beach page, undated, read 2026-11-02. Toilets not listed.
- field: description_long (Blue Flag 2026)
  claim: '''Nagüeles-Casablanca'' is listed under Marbella in ADEAC''s ''Relación Playas Galardonadas 2026''.'
  source_url: https://www.banderaazul.org/sites/default/files/2026/Rueda-de-prensa-2026/Relaci%C3%B3n%20Playas%20Galardonadas%202026.pdf
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour beach fact check 2026-11-02)
  confidence: high
  notes: PDF read 2026-11-02. The award names a stretch; whether the Places point lies inside it is not checked.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  description: Age groups and family scores are not assessed.
  retryable: true
  owner: human_editor
- code: lifeguard_season_unchecked
  severity: warning
  fields:
  - description_long
  - accessibility
  description: Lifeguard service and bathing-season dates for 2027 are not checked against the council's beach plan; check before publishing safety-related text.
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
