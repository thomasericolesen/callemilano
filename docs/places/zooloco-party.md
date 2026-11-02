---
schema_version: 1.0.0
status: archived
id: ES-AND-MAL-ZOOLOCO-PARTY-001
slug: zooloco-party
name: Zooloco Party
category: Family activities
tags: []
coordinates:
  latitude: 36.5394839
  longitude: -4.641249999999999
  purpose: venue
  label: Zooloco Party, C. Río Almanzora, 15, 29651 Las Lagunas de Mijas, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJOe9yFR_icg0RjoVAGLc4NVM, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=5995760837950735758
external_ids:
  google_place_id: ChIJOe9yFR_icg0RjoVAGLc4NVM
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 8 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Zooloco Party, C. Río Almanzora, 15, 29651 Las Lagunas de Mijas, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5394839,-4.641249999999999); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5394839%2C-4.641249999999999&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 8 min, 3.25 km. One predicted sample, not the Google Maps app''s main figure.'
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
  official_website: http://www.zoolocoparty.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Zooloco Party: indoor play and party centre, about 8 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: Zooloco Party is a indoor play and party centre at C. Río Almanzora, 15, 29651 Las Lagunas de Mijas, Málaga. From Casa de la Familia it is about 8 minutes by car (Google route check, Saturday 10:00). Its own website describes a private children's party room rented by the day for birthdays, class parties or family gatherings (adults and children), 200 m² with a bouncy castle, trampolines, a ball pit and a small football pitch, suited to children up to 12. It does not describe open play for drop-in visitors.
seo_title: Zooloco Party, Mijas | CalleMilano draft record
seo_description: 'Draft record for Zooloco Party (Mijas): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Zooloco Party' at C. Río Almanzora, 15, 29651 Las Lagunas de Mijas, Málaga, España (36.5394839,-4.641249999999999), business status OPERATIONAL, website http://www.zoolocoparty.com/.
  source_url: https://maps.google.com/?cid=5995760837950735758
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 8 min by car (3.25 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5394839%2C-4.641249999999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: 'Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time removed 2026-11-02 (owner decision: walking times of 20 minutes or more are not shown).'
- field: description_long
  claim: 'Own website: "Sala privada de ocio infantil" - room rented per day for children''s birthdays, class parties or family gatherings; 200 m2 with bouncy castle, trampolines, ball pit, football pitch; for children up to 12; Calle Río Almanzora 15, Las Lagunas.'
  source_url: http://www.zoolocoparty.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: high
  notes: Homepage quoted via Firecrawl on 2026-11-02.
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
- code: private_hire_only
  severity: warning
  fields:
  - category
  - description_long
  description: The venue is a private party room for hire by the day, not a drop-in attraction. Owner to decide whether it belongs in the guide (it may suit longer family stays with a birthday).
  retryable: true
  owner: human_editor
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: '2026-11-02'
last_reviewed_at: null
next_review_at: null
review_decision:
  decision: archived
  reviewer: Eric Olesen (editor-of-record)
  date: '2026-11-02'
  notes: 'Owner decision 2026-11-02: remove Zooloco Party from the guide (it is a private party room for hire, not a drop-in attraction). Kept as archive; the ID stays allocated and must not be reused.'
redirects: []
---
