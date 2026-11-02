---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-BIGFOOT-BUGGY-TOURS-001
slug: bigfoot-buggy-tours
name: Bigfoot Buggy Tours
category: Family activities
tags:
- Adventure
coordinates:
  latitude: 36.540579199999996
  longitude: -4.658856699999999
  purpose: venue
  label: Bigfoot Buggy Tours, Diseminado el Chapparal, C. la Higuera, 6, 29651 Las Lagunas de Mijas, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJmTvBvyTicg0RdM2SPrpX2Wk, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=7627223901353987444
external_ids:
  google_place_id: ChIJmTvBvyTicg0RdM2SPrpX2Wk
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 4 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Bigfoot Buggy Tours, Diseminado el Chapparal, C. la Higuera, 6, 29651 Las Lagunas de Mijas, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.540579199999996,-4.658856699999999); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.540579199999996%2C-4.658856699999999&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 4 min, 1.38 km. Walking (Routes API WALK, same day): 17 min, 1.3 km. One predicted sample, not the Google Maps app''s main figure.'
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
  official_website: http://www.bigfootbuggytours.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Bigfoot Buggy Tours: buggy tour operator, about 17 min on foot or 4 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: 'Bigfoot Buggy Tours is a buggy tour operator at Diseminado el Chapparal, C. la Higuera, 6, 29651 Las Lagunas de Mijas, Málaga. From Casa de la Familia it is about 17 minutes on foot (1.3 km, Google''s walking route) or about 4 minutes by car (Google route check, Saturday 10:00). Owner''s own knowledge: For adventurous adults with petrol in their blood. Opening hours, prices, age rules and facilities have not been checked yet; check with the venue before visiting.'
seo_title: Bigfoot Buggy Tours, Mijas | CalleMilano draft record
seo_description: 'Draft record for Bigfoot Buggy Tours (Mijas): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Bigfoot Buggy Tours Costa Del Sol' at Diseminado el Chapparal, C. la Higuera, 6, 29651 Las Lagunas de Mijas, Málaga, España (36.540579199999996,-4.658856699999999), business status OPERATIONAL, website http://www.bigfootbuggytours.com/.
  source_url: https://maps.google.com/?cid=7627223901353987444
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia, description_long (walking time)
  claim: 'From Casa de la Familia: 4 min by car (1.38 km, Saturday 10:00 predicted traffic) and 17 min on foot (1.3 km).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.540579199999996%2C-4.658856699999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00, and WALK (https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.540579199999996%2C-4.658856699999999&travelmode=walking). Google's walking route says nothing about pavements, crossings or whether it suits children.
- field: description_long (owner knowledge)
  claim: For adventurous adults with petrol in their blood.
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
  description: 'Age groups and family scores are not assessed; energy_level Medium is an editorial estimate from the type of place. Owner note: For adventurous adults with petrol in their blood.'
  retryable: true
  owner: human_editor
- code: age_and_licence_rules_unknown
  severity: warning
  fields:
  - age_groups
  - family_score
  - description_long
  description: Minimum age for drivers and passengers, driving-licence rules and safety equipment must come from the operator before any family rating.
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
