---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-COSMOZONE-LASERTAG-001
slug: cosmozone-lasertag
name: Cosmozone Lasertag
category: Family activities
tags: []
coordinates:
  latitude: 36.534731
  longitude: -4.6353832
  purpose: venue
  label: Cosmozone Lasertag, Av. de Andalucía, 15, 29651 Las Lagunas de Mijas, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJZZP-Oi7jcg0RmgSo05MhLzI, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=3616145944596710554
external_ids:
  google_place_id: ChIJZZP-Oi7jcg0RmgSo05MhLzI
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 8 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Cosmozone Lasertag, Av. de Andalucía, 15, 29651 Las Lagunas de Mijas, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.534731,-4.6353832); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.534731%2C-4.6353832&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 8 min, 3.98 km. One predicted sample, not the Google Maps app''s main figure.'
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
  official_website: http://www.cosmozone.es/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Cosmozone Lasertag: laser tag venue, about 8 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Cosmozone Lasertag is a laser tag venue at Av. de Andalucía, 15, 29651 Las Lagunas de Mijas, Málaga. From Casa de la Familia it is about 8 minutes by car (Google route check, Saturday 10:00). Opening hours, prices, age rules and facilities have not been checked yet; check with the venue before visiting.
seo_title: Cosmozone Lasertag, Mijas | CalleMilano draft record
seo_description: 'Draft record for Cosmozone Lasertag (Mijas): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Cosmozone Lasertag' at Av. de Andalucía, 15, 29651 Las Lagunas de Mijas, Málaga, España (36.534731,-4.6353832), business status OPERATIONAL, website http://www.cosmozone.es/.
  source_url: https://maps.google.com/?cid=3616145944596710554
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 8 min by car (3.98 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.534731%2C-4.6353832&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: 'Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time removed 2026-11-02 (owner decision: walking times of 20 minutes or more are not shown).'
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
  description: 'Checked 2026-11-02: The website (cosmozone.es) calls itself "the most technologically advanced laser tag in Spain", but hours, prices and minimum age were not readable. Needs another source or a direct check.'
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
