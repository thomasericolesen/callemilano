---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-AQUAMIJAS-001
slug: aquamijas
name: Aquamijas
category: Family activities
tags: []
coordinates:
  latitude: 36.538292999999996
  longitude: -4.6330707
  purpose: venue
  label: Aquamijas, Carr. de Cádiz, Km. 1016, 29651 Las Lagunas de Mijas, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJs_TXeBficg0Re0eb1ulV3Uc, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=5178389609362179963
external_ids:
  google_place_id: ChIJs_TXeBficg0Re0eb1ulV3Uc
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 10 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Aquamijas, Carr. de Cádiz, Km. 1016, 29651 Las Lagunas de Mijas, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.538292999999996,-4.6330707); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.538292999999996%2C-4.6330707&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 10 min, 4.09 km. Walking (Routes API WALK, same day): 54 min, 3.98 km. One predicted sample, not the Google Maps app''s main figure.'
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
  official_website: https://aquamijas.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Aquamijas: seasonal water park, about 54 min on foot or 10 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: 'Aquamijas is a seasonal water park at Carr. de Cádiz, Km. 1016, 29651 Las Lagunas de Mijas, Málaga. From Casa de la Familia it is about 54 minutes on foot (3.98 km, Google''s walking route) or about 10 minutes by car (Google route check, Saturday 10:00). Owner''s own knowledge: Very family-friendly. The price is lower at off-peak times, but that must be checked. Its own website says the 2026 season opened on 1 May and the park closed from 14 September 2026. Opening hours, prices, age rules and facilities have not been checked yet; check with the venue before visiting.'
seo_title: Aquamijas, Mijas | CalleMilano draft record
seo_description: 'Draft record for Aquamijas (Mijas): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Aquamijas' at Carr. de Cádiz, Km. 1016, 29651 Las Lagunas de Mijas, Málaga, España (36.538292999999996,-4.6330707), business status CLOSED_TEMPORARILY, website https://aquamijas.com/.
  source_url: https://maps.google.com/?cid=5178389609362179963
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia, description_long (walking time)
  claim: 'From Casa de la Familia: 10 min by car (4.09 km, Saturday 10:00 predicted traffic) and 54 min on foot (3.98 km).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.538292999999996%2C-4.6330707&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00, and WALK (https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.538292999999996%2C-4.6330707&travelmode=walking). Google's walking route says nothing about pavements, crossings or whether it suits children.
- field: description_long (owner knowledge)
  claim: Very family-friendly. The price is lower at off-peak times, but that must be checked.
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/nearby-selection-2026-11-02.md
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: medium
  notes: Owner's own local knowledge, given on the nearby selection page on 2026-11-02; not independently verified.
- field: description_long (season)
  claim: 'Own website: the park stays closed from 14 September 2026; the 2026 season opened on 1 May 2026.'
  source_url: https://aquamijas.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Search excerpts of aquamijas.com and aquamijas.com/fecha-apertura-aquamijas-2026/ read 2026-11-02; pages not read in full. Google shows the park as temporarily closed (off-season).
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
  description: 'Age groups and family scores are not assessed; energy_level Medium is an editorial estimate from the type of place. Owner note: Very family-friendly. The price is lower at off-peak times, but that must be checked.'
  retryable: true
  owner: human_editor
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
