---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-EL-GRAN-PARQUE-DE-MIJAS-001
slug: el-gran-parque-de-mijas
name: El Gran Parque de Mijas
category: Family activities
tags: []
coordinates:
  latitude: 36.539559499999996
  longitude: -4.656531
  purpose: venue
  label: El Gran Parque de Mijas, Cl. Buitre, 29651 Las Lagunas de Mijas, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJETGGUwDhcg0RCUl3V52-r-8, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=17271232678975719689
external_ids:
  google_place_id: ChIJETGGUwDhcg0RCUl3V52-r-8
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 3 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: El Gran Parque de Mijas, Cl. Buitre, 29651 Las Lagunas de Mijas, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.539559499999996,-4.656531); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.539559499999996%2C-4.656531&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 3 min, 1.08 km. Walking (Routes API WALK, same day): 13 min, 1.01 km. One predicted sample, not the Google Maps app''s main figure.'
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
description_short: 'El Gran Parque de Mijas: large public park in Las Lagunas de Mijas, about 13 min on foot or 3 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: 'El Gran Parque de Mijas is a large public park in Las Lagunas de Mijas at Cl. Buitre, 29651 Las Lagunas de Mijas, Málaga. From Casa de la Familia it is about 13 minutes on foot (1.01 km, Google''s walking route) or about 3 minutes by car (Google route check, Saturday 10:00). Owner''s own knowledge: Suitable for children, with water and play areas. Opening hours, prices, age rules and facilities have not been checked yet; check with the venue before visiting.'
seo_title: El Gran Parque de Mijas, Mijas | CalleMilano draft record
seo_description: 'Draft record for El Gran Parque de Mijas (Mijas): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'El Gran Parque de Mijas' at Cl. Buitre, 29651 Las Lagunas de Mijas, Málaga, España (36.539559499999996,-4.656531), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=17271232678975719689
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia, description_long (walking time)
  claim: 'From Casa de la Familia: 3 min by car (1.08 km, Saturday 10:00 predicted traffic) and 13 min on foot (1.01 km).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.539559499999996%2C-4.656531&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00, and WALK (https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.539559499999996%2C-4.656531&travelmode=walking). Google's walking route says nothing about pavements, crossings or whether it suits children.
- field: description_long (owner knowledge)
  claim: Suitable for children, with water and play areas.
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/nearby-selection-2026-11-02.md
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: medium
  notes: Owner's own local knowledge, given on the nearby selection page on 2026-11-02; not independently verified.
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
  description: 'Age groups and family scores are not assessed; energy_level Low is an editorial estimate from the type of place. Owner note: Suitable for children, with water and play areas.'
  retryable: true
  owner: human_editor
- code: no_official_website
  severity: info
  fields:
  - links
  description: Google lists no website; facts may have to come from a social page or a direct contact.
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
