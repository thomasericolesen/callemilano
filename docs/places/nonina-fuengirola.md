---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-NONINA-FUENGIROLA-001
slug: nonina-fuengirola
name: Noniná
category: Restaurants
tags: []
coordinates:
  latitude: 36.5412292
  longitude: -4.619409999999999
  purpose: venue
  label: Noniná, C. Puerto, 29640 Fuengirola, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJNy0yLhHjcg0R0F7F3OklLwI, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=157386198342786768
external_ids:
  google_place_id: ChIJNy0yLhHjcg0R0F7F3OklLwI
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 15 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Noniná, C. Puerto, 29640 Fuengirola, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5412292,-4.619409999999999); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5412292%2C-4.619409999999999&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 15 min, 6.37 km. Daytime sample; evening traffic differs.'
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
description_short: 'Noniná: bar, about 15 min by car, taxi or Uber from Casa de la Familia. Draft; facts not yet checked.'
description_long: Noniná is a bar at C. Puerto, 29640 Fuengirola, Málaga. From Casa de la Familia it is about 15 minutes by car, taxi or Uber (Google route check, Saturday 10:00; evening traffic differs). Opening hours, prices, music and atmosphere have not been checked yet; check with the venue before visiting. If you plan to drink, take a taxi or Uber both ways. As in any bar, keep an eye on your drink.
seo_title: Noniná, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Noniná (Fuengirola): location and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Noniná' at C. Puerto, 29640 Fuengirola, Málaga, España (36.5412292,-4.619409999999999), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=157386198342786768
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (bars intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 15 min by car (6.37 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5412292%2C-4.619409999999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (bars intake 2026-11-02)
  confidence: medium
  notes: 'Google Routes API computeRoutes, DRIVE (TRAFFIC_AWARE_OPTIMAL, Saturday 2026-11-07 10:00), from the project origin. Walking time removed 2026-11-02 (owner decision: guests reach bars in town by taxi or Uber).'
- field: status (selection)
  claim: Selected by the owner for the guide on the bars selection page; passed a reputation screen on 2026-11-02.
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/bars-selection-2026-11-02.md
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: medium
  notes: 'Screen: Google rating and count, 5 Google reviews, and web/news searches for drink spiking; nothing was found for this venue. The owner does not know the bar personally. Not a guarantee.'
review_issues:
- code: facts_not_checked
  severity: warning
  fields:
  - visit_information
  - cost_level
  - accessibility
  - food_available
  description: Created from Google identity and route checks only. Hours, prices, music, food and accessibility need the venue's own sources.
  retryable: true
  owner: fact_check
- code: audience_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  description: Added for adults and seniors; age groups and scores are not assessed. energy_level Low is an editorial estimate.
  retryable: true
  owner: human_editor
- code: owner_has_not_visited
  severity: info
  fields:
  - description_long
  description: The owner does not know this bar personally (2026-11-02). Consider a visit or more sources before recommending it.
  retryable: true
  owner: human_editor
- code: no_official_source_found
  severity: warning
  fields:
  - visit_information
  - cost_level
  - links
  description: Search on 2026-11-02 found no own website or readable social page. Hours and prices need a direct check.
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
