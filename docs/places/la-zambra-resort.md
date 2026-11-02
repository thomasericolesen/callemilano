---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-LA-ZAMBRA-RESORT-001
slug: la-zambra-resort
name: La Zambra Resort
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.5529094
  longitude: -4.6667533
  purpose: venue
  label: La Zambra Resort, Av. de Louison Bobet, 9, 29650 Málaga (Google Places listing)
  source: Google Places API (New), place ChIJrYNyj6bhcg0RJxTIGH2EJng, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=8657753006487901223
external_ids:
  google_place_id: ChIJrYNyj6bhcg0RJxTIGH2EJng
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 7 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: La Zambra Resort, Av. de Louison Bobet, 9, 29650 Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5529094,-4.6667533); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5529094%2C-4.6667533&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 7 min, 3.44 km. Walking (Routes API WALK, same day): 45 min, 3.29 km. One predicted sample, not the Google Maps app''s main figure.'
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
  official_website: https://www.hyatt.com/unbound-collection/en-US/agpub-la-zambra-resort
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34951311234
related_places: []
description_short: 'La Zambra Resort: resort hotel (The Unbound Collection by Hyatt) with restaurant and spa, about 45 min on foot or 7 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: 'La Zambra Resort is a resort hotel (The Unbound Collection by Hyatt) with restaurant and spa at Av. de Louison Bobet, 9, 29650 Málaga. From Casa de la Familia it is about 45 minutes on foot (3.29 km, Google''s walking route) or about 7 minutes by car (Google route check, Saturday 10:00). Owner''s own knowledge: Restaurant and spa area (added by the owner). Its own website: a five-star resort on the site of the former Hotel Byblos (opened 1986, reopened as La Zambra in 2022), with four restaurants (Palmito from breakfast to late dinner, Picador for tapas with more than ninety wines by the glass, Bamboleo for sunset dining, La Bartola by the pool) plus Sarao for the night, and Mood Spa, described as one of the largest spas on the Costa del Sol, with Turkish baths and an indoor pool. It also runs two kids'' clubs (6 months-3 years and 4-10 years) daily 10:00-18:00 for hotel guests. The site does not say whether non-guests can use the restaurants or spa; check before visiting.'
seo_title: La Zambra Resort, Mijas | CalleMilano draft record
seo_description: 'Draft record for La Zambra Resort (Mijas): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, food_available
  claim: Google Places lists 'La Zambra Resort Mijas - Marbella - The Unbound Collection by Hyatt' at Av. de Louison Bobet, 9, 29650 Málaga, España (36.5529094,-4.6667533), business status OPERATIONAL, website https://www.hyatt.com/unbound-collection/en-US/agpub-la-zambra-resort.
  source_url: https://maps.google.com/?cid=8657753006487901223
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia, description_long (walking time)
  claim: 'From Casa de la Familia: 7 min by car (3.44 km, Saturday 10:00 predicted traffic) and 45 min on foot (3.29 km).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5529094%2C-4.6667533&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00, and WALK (https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5529094%2C-4.6667533&travelmode=walking). Google's walking route says nothing about pavements, crossings or whether it suits children.
- field: description_long (owner knowledge)
  claim: Restaurant and spa area (added by the owner).
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/nearby-selection-2026-11-02.md
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: medium
  notes: Owner's own local knowledge, given on the nearby selection page on 2026-11-02; not independently verified.
- field: description_long, links
  claim: 'Own page: former Hotel Byblos (1986), reopened 2022; four restaurants (Palmito, Picador, Bamboleo, La Bartola) and Sarao; Mood Spa with Turkish baths and indoor pool, yoga and Pilates daily; kids clubs 6 m-3 y and 4-10 y, daily 10:00-18:00; address Avenida Louison Bobet 9, 29650 Mijas; phone +34 951 31 12 34.'
  source_url: https://www.hyatt.com/unbound-collection/en-US/agpub-la-zambra-resort
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: high
  notes: Read in full via Firecrawl on 2026-11-02. Access for non-guests is not stated.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  description: 'Age groups and family scores are not assessed; energy_level Low is an editorial estimate from the type of place. Owner note: Restaurant and spa area (added by the owner).'
  retryable: true
  owner: human_editor
- code: non_guest_access_unknown
  severity: warning
  fields:
  - description_long
  - booking_required
  - cost_level
  description: The resort site does not say whether non-guests can eat in the restaurants or use the spa, or at what price. Confirm with the resort before recommending it to guests of Casa de la Familia.
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
