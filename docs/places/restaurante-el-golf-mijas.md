---
schema_version: 1.0.0
status: archived
id: ES-AND-MAL-RESTAURANTE-EL-GOLF-MIJAS-001
slug: restaurante-el-golf-mijas
name: Restaurante El Golf
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.5461604
  longitude: -4.6586579
  purpose: venue
  label: Restaurante El Golf, Av. Suiza, 1, 29651 Las Lagunas de Mijas, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJX4jMbhHicg0RnDykh7D9XAI, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=170289820564995228
external_ids:
  google_place_id: ChIJX4jMbhHicg0RnDykh7D9XAI
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 5 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante El Golf, Av. Suiza, 1, 29651 Las Lagunas de Mijas, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5461604,-4.6586579); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5461604%2C-4.6586579&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 5 min, 2.13 km. One predicted sample, not the Google Maps app''s main figure.'
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
cost_level: €€
visit_information:
  schedule: null
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'No prices on own site; TheFork average price ("Average price€26"; "€€ - €€€") is inside the 20-50 € band. Fallback source per docs/trip-planner-agents.md. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).N'
  cost_checked_at: '2026-11-02'
links:
  official_website: null
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Restaurante El Golf: restaurant on Avenida Suiza (Mijas Golf), about 5 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Restaurante El Golf is a restaurant on Avenida Suiza (Mijas Golf) at Av. Suiza, 1, 29651 Las Lagunas de Mijas, Málaga. From Casa de la Familia it is about 5 minutes by car (Google route check, Saturday 10:00). Opening hours, prices, age rules and facilities have not been checked yet; check with the venue before visiting.
seo_title: Restaurante El Golf, Mijas | CalleMilano draft record
seo_description: 'Draft record for Restaurante El Golf (Mijas): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, food_available
  claim: Google Places lists 'Restaurante El Golf' at Av. Suiza, 1, 29651 Las Lagunas de Mijas, Málaga, España (36.5461604,-4.6586579), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=170289820564995228
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 5 min by car (2.13 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5461604%2C-4.6586579&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: 'Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time removed 2026-11-02 (owner decision: walking times of 20 minutes or more are not shown).'
- field: cost_level
  claim: '"Average price€26"; "€€ - €€€"'
  source_url: https://www.thefork.com/restaurant/restaurante-el-golf-r857436
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: low
  notes: 'TheFork price marking only (search excerpt); no ratings or reviews recorded. Own-site prices preferred when available. Two URLs used. The first quote (TheFork, ''Average price€26'', from the search snippet of thefork.com r857436) is on the entry URL. The second quote is from a different URL: https://www.tripadvisor.es/R'
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
- code: no_official_website
  severity: info
  fields:
  - links
  description: Google lists no website; facts may have to come from a social page or a direct contact.
  retryable: true
  owner: fact_check
- code: cost_level_secondary_source
  severity: info
  fields:
  - cost_level
  description: cost_level is based on the TheFork price marking, not the own menu; replace when an own menu with prices is found.
  retryable: true
  owner: human_editor
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision:
  decision: archived
  reviewer: Eric Olesen (editor-of-record)
  date: '2026-11-11'
  notes: 'Owner decision 2026-11-11 on the editor list (https://claude.ai/artifact/C1Lu1WExnpBw8YRw5K1Jrc): archive (no own website, price only from a secondary source); we already have enough places. Kept as archive; the ID stays allocated and must not be reused.'
redirects: []
---
