---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-KARTING-EXPERIENCE-MIJAS-001
slug: karting-experience-mijas
name: Karting Experience Mijas
category: Family activities
tags:
- Adventure
coordinates:
  latitude: 36.567079899999996
  longitude: -4.621423
  purpose: venue
  label: Karting Experience Mijas, Lugar Diseminado Arroyo Pajares, Poligono, 4 Parcela 127, 29650 Las Lagunas de Mijas, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJZ_F5Uzfjcg0RuLcz3VaMGfQ, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=17589244124378412984
external_ids:
  google_place_id: ChIJZ_F5Uzfjcg0RuLcz3VaMGfQ
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 13 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Karting Experience Mijas, Lugar Diseminado Arroyo Pajares, Poligono, 4 Parcela 127, 29650 Las Lagunas de Mijas, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.567079899999996,-4.621423); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.567079899999996%2C-4.621423&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 13 min, 7.11 km. One predicted sample, not the Google Maps app''s main figure.'
age_groups:
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: low
  children: medium
  young_adults: high
  seniors: medium
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
  official_website: https://kartingexperience.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Karting Experience Mijas: outdoor karting track, about 13 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: 'Karting Experience Mijas is a outdoor karting track at Lugar Diseminado Arroyo Pajares, Poligono, 4 Parcela 127, 29650 Las Lagunas de Mijas, Málaga. From Casa de la Familia it is about 13 minutes by car (Google route check, Saturday 10:00). The operator''s website: Karting Mijas is a 900 m outdoor circuit in a natural setting, with long straights and technical bends, and a bar-café terrace overlooking the track. The page shows kart prices from €12 to €30 per session but does not clearly tie each price list to this track; age rules and opening hours were not checked.'
seo_title: Karting Experience Mijas, Mijas | CalleMilano draft record
seo_description: 'Draft record for Karting Experience Mijas (Mijas): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Karting Experience Mijas' at Lugar Diseminado Arroyo Pajares, Poligono, 4 Parcela 127, 29650 Las Lagunas de Mijas, Málaga, España (36.567079899999996,-4.621423), business status OPERATIONAL, website https://kartingexperience.com/.
  source_url: https://maps.google.com/?cid=17589244124378412984
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 13 min by car (7.11 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.567079899999996%2C-4.621423&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: 'Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time removed 2026-11-02 (owner decision: walking times of 20 minutes or more are not shown).'
- field: description_long
  claim: 'Operator website: Karting Mijas, 900 m circuit in a natural setting, long straights and technical curves, bar-café terrace overlooking the races; link to its own tariff page (kartingexperience.com/tarifas/).'
  source_url: https://kartingexperience.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: medium
  notes: Homepage quoted via Firecrawl on 2026-11-02.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children low, children medium, young_adults high, seniors medium; energy_level Medium.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
review_issues:
- code: prices_and_hours_by_track_unclear
  severity: warning
  fields:
  - cost_level
  - visit_information
  - age_groups
  description: Read kartingexperience.com/tarifas/ to tie prices and age rules to this track; opening hours not checked.
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-10'
last_verified: '2026-11-02'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
