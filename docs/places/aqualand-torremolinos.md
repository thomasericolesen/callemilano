---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-AQUALAND-TORREMOLINOS-001
slug: aqualand-torremolinos
name: Aqualand Torremolinos
category: Family activities
tags: []
coordinates:
  latitude: 36.6259897
  longitude: -4.5082274
  purpose: venue
  label: Aqualand Torremolinos, C. Cuba, 10, 29620 Torremolinos, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJgwo4J5D7cg0Ry4aludNIl4k, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=9914473178869368523
external_ids:
  google_place_id: ChIJgwo4J5D7cg0Ry4aludNIl4k
municipality: Torremolinos
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 24 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Aqualand Torremolinos, C. Cuba, 10, 29620 Torremolinos, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.6259897,-4.5082274); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6259897%2C-4.5082274&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 24 min, 22.52 km. One predicted sample, not the Google Maps app''s main figure.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: high
  children: high
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
  official_website: http://www.aqualand.es/torremolinos
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Aqualand Torremolinos: water park, about 24 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: Aqualand Torremolinos is a water park at C. Cuba, 10, 29620 Torremolinos, Málaga. From Casa de la Familia it is about 24 minutes by car (Google route check, Saturday 10:00). Its own schedule page shows opening days in November 2026 with hours of 10:00-17:00 or 10:00-18:00 (the specific days were not captured); rides close 30 minutes before the park. The 2026 season began on 1 April (its own social posts). Prices, age rules and facilities were not checked.
seo_title: Aqualand Torremolinos, Torremolinos | CalleMilano draft record
seo_description: 'Draft record for Aqualand Torremolinos (Torremolinos): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Aqualand Torremolinos' at C. Cuba, 10, 29620 Torremolinos, Málaga, España (36.6259897,-4.5082274), business status OPERATIONAL, website http://www.aqualand.es/torremolinos.
  source_url: https://maps.google.com/?cid=9914473178869368523
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 24 min by car (22.52 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6259897%2C-4.5082274&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: 'Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time removed 2026-11-02 (owner decision: walking times of 20 minutes or more are not shown).'
- field: visit_information, description_long
  claim: 'Own schedule page: calendar for November 2026 shows opening days "Abierto: 10:00h-17:00h" and "Abierto: 10:00h-18:00h"; rides open until 30 minutes before park closing.'
  source_url: https://www.aqualand.es/torremolinos/horario/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: medium
  notes: Quoted via Firecrawl on 2026-11-02; the calendar day labels were not captured. Season start 1 April 2026 from the park's own Facebook/Instagram posts (search excerpts, 2026-11-02).
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children high, children high, young_adults high, seniors medium; energy_level Medium.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
review_issues:
- code: days_prices_age_rules_unchecked
  severity: warning
  fields:
  - visit_information
  - cost_level
  - age_groups
  description: Exact opening days, prices, height/age rules and facilities still need checking on aqualand.es.
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
