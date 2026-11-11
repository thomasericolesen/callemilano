---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-PLAYA-DE-SAN-PEDRO-ALCANTARA-001
slug: playa-de-san-pedro-alcantara
name: Playa de San Pedro de Alcántara
category: Beaches
tags:
- Beach
coordinates:
  latitude: 36.472585699999996
  longitude: -4.9862369
  purpose: representative_point
  label: Playa de San Pedro de Alcántara, Playa de San Pedro de Alcántara, Marbella, España (Google Places listing); not a parking point
  source: Google Places API (New), place ChIJTzbx0jEqcw0Rou3kgMstejI, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=3637270001119194530
external_ids:
  google_place_id: ChIJTzbx0jEqcw0Rou3kgMstejI
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 41 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Playa de San Pedro de Alcántara, Playa de San Pedro de Alcántara, Marbella, España (Google Places point, not a parking point)
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.472585699999996,-4.9862369); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.472585699999996%2C-4.9862369&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 41 min, 39.7 km. One predicted sample, not the Google Maps app''s main figure.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: high
  children: high
  young_adults: high
  seniors: high
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
toilets_available: 'yes'
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
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Playa de San Pedro de Alcántara, Marbella: sand-and-gravel beach with a promenade and beach restaurants.'
description_long: 'Playa de San Pedro de Alcántara lies in front of San Pedro, west of Puerto Banús. Spain.info (Turespaña) lists sand and gravel (dark), moderate waves, about 1,400 m by 35 m, high occupancy, semi-urban, easy access on foot, several restaurants and beach bars, a promenade, and services including toilets and showers. The 2026 Blue Flag list names ''San Pedro de Alcántara (Guadalmina)''; whether that covers the stretch at this point is not confirmed. Rocks: the official sources describe a sand-and-gravel beach with easy access on foot, so it meets the project''s beach rule (owner decision 2026-11-02). About 41 minutes by car from Casa de la Familia; the Roman remains at Las Bóvedas and Vega del Mar are nearby.'
seo_title: Playa de San Pedro de Alcántara, Marbella | CalleMilano
seo_description: 'Playa de San Pedro de Alcántara (Marbella): sand, facilities, Blue Flag status and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Playa de San Pedro de Alcántara' at Playa de San Pedro de Alcántara, Marbella, España (36.472585699999996,-4.9862369), business status OPERATIONAL, primary type beach.
  source_url: https://maps.google.com/?cid=3637270001119194530
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Maps establishes identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 41 min by car (39.7 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.472585699999996%2C-4.9862369&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL, Saturday 2026-11-07 10:00.
- field: description_long, toilets_available, food_available
  claim: 'Spain.info: San Pedro de Alcántara, sand and gravel (dark), moderate waves, 1,400 x 35 m, high occupancy, semi-urban, easy access on foot; ''cuenta con varios restaurantes y chiringuitos''; services include toilets and showers.'
  source_url: https://www.spain.info/es/playa/san-pedro-alcantara/
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour beach fact check 2026-11-02)
  confidence: medium
  notes: Turespaña beach page, undated, read 2026-11-02.
- field: description_long (Blue Flag 2026)
  claim: '''San Pedro de Alcántara (Guadalmina)'' is listed under Marbella in ADEAC''s 2026 list.'
  source_url: https://www.banderaazul.org/sites/default/files/2026/Rueda-de-prensa-2026/Relaci%C3%B3n%20Playas%20Galardonadas%202026.pdf
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour beach fact check 2026-11-02)
  confidence: high
  notes: PDF read 2026-11-02. Guadalmina is the western stretch; the award may not cover the Places point.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children high, children high, young_adults high, seniors high; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Beach."
  source_url: https://claude.ai/artifact/DZv9cLLQ1BEcYs3NeewdEF
  source_type: secondary
  checked_at: '2026-11-11'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-11
  confidence: medium
  notes: Owner's own judgment on the tag checklist on 2026-11-11 (previous tags were estimates from import); not independently verified. source_type secondary is the nearest schema value.
review_issues:
- code: lifeguard_season_unchecked
  severity: warning
  fields:
  - description_long
  - accessibility
  description: Lifeguard service and bathing-season dates for 2027 are not checked against the council's beach plan; check before publishing safety-related text.
  retryable: true
  owner: fact_check
- code: blue_flag_stretch_unclear
  severity: info
  fields:
  - description_long
  description: The Blue Flag is listed for 'San Pedro de Alcántara (Guadalmina)'. Confirm whether the record point is inside the awarded stretch before stating it as a Blue Flag beach.
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
