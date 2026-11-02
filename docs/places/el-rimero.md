---
schema_version: 1.0.0
status: archived
id: ES-AND-MAL-EL-RIMERO-001
slug: el-rimero
name: El Rimero
category: Restaurants
tags: []
coordinates:
  latitude: 36.5322871
  longitude: -4.6447012999999995
  purpose: venue
  label: El Rimero, C. Archidona, 81, 29651 Las Lagunas de Mijas, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJwe81eR3icg0RNyj5oJqegnI, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=8251331854259005495
external_ids:
  google_place_id: ChIJwe81eR3icg0RNyj5oJqegnI
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 8 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: El Rimero, C. Archidona, 81, 29651 Las Lagunas de Mijas, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5322871,-4.6447012999999995); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5322871%2C-4.6447012999999995&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 8 min, 3.39 km. Daytime sample; evening traffic differs.'
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
  contact: https://www.facebook.com/elrimero
related_places: []
description_short: 'El Rimero: wine bar, about 8 min by car, taxi or Uber from Casa de la Familia. Draft; facts not yet checked.'
description_long: El Rimero ('El Rimero. Tu Vinoteca particular') is listed at C. Archidona, 81, 29651 Las Lagunas de Mijas, Málaga, about 8 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Its own Facebook page describes it as a private wine shop, on- and offline, in the retail category - not as a bar. The latest visible posts are from 2020 (a closure for the COVID-19 state of alarm in March 2020 and a wine tasting in May 2020), and its website elrimero.com no longer exists. It is not recommended as a bar.
seo_title: El Rimero, Mijas | CalleMilano draft record
seo_description: 'Draft record for El Rimero (Mijas): location and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'El Rimero' at C. Archidona, 81, 29651 Las Lagunas de Mijas, Málaga, España (36.5322871,-4.6447012999999995), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=8251331854259005495
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (bars intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 8 min by car (3.39 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5322871%2C-4.6447012999999995&travelmode=driving
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
- field: description_long, category
  claim: 'Own Facebook page ''El Rimero. Tu Vinoteca particular'': ''El Rimero. Tu Vinoteca particular. On/Off Line.''; category ''Shopping og detailhandel'' (shopping and retail); Archidona, 81, Mijas 29651; phone +34 952 46 59 65; info@elrimero.com; posts 21 March 2020 (closed due to the COVID-19 state of alarm) and 13 May 2020 (''Cata Martín Códax'').'
  source_url: https://www.facebook.com/elrimero
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (bar fact check 2026-11-02)
  confidence: medium
  notes: Owner screenshot of the page (supplied 2026-11-02). Review and follower counts not recorded. elrimero.com did not resolve (DNS failure) on 2026-11-02.
review_issues:
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
- code: not_a_bar_possibly_closed
  severity: blocking
  fields:
  - category
  - status
  - description_long
  description: 'Own page describes a wine shop (retail, on/offline), not a bar, with no visible activity since 2020 and a dead website. Owner decision: archive, or confirm that it serves drinks on site and is open.'
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
  notes: 'Owner decision 2026-11-02: remove El Rimero from the guide (own page describes a wine shop, not a bar; no activity since 2020 and website gone). Kept as archive; the ID stays allocated and must not be reused.'
redirects: []
---
