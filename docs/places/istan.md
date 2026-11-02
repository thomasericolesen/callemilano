---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-ISTAN-001
slug: istan
name: Istán
category: City
tags: []
coordinates:
  latitude: 36.58209850000001
  longitude: -4.9497007
  purpose: town_center
  label: Istán, 29611 Istán, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJN_sC7sXWcg0RQ6vfWn40HbI, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=12834472230370913091
external_ids:
  google_place_id: ChIJN_sC7sXWcg0RQ6vfWn40HbI
municipality: Istán
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 57 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Istán, 29611 Istán, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.58209850000001,-4.9497007); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.58209850000001%2C-4.9497007&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 57 min, 45.4 km. One predicted sample.'
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
  visitor_information: https://www.andalucia.org/es/istan
  transport: null
  contact: null
related_places: []
description_short: 'Istán: small white village with steep Andalusí streets in the Sierra de las Nieves.'
description_long: 'Istán keeps the layout of its Andalusí past: narrow, steep streets with whitewashed houses and Arab-tile roofs, best seen in the upper village, where part of a tower of the old Arab fortress walls survives. The municipality is part of the Sierra de las Nieves natural area, a UNESCO Biosphere Reserve (Andalusian tourist board). About 57 minutes by car from Casa de la Familia, at the upper end of the one-hour band.'
seo_title: Istán, Istán | CalleMilano
seo_description: 'Istán (Istán): what to see and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Istán' at 29611 Istán, Málaga, España (36.58209850000001,-4.9497007), primary type None.
  source_url: https://maps.google.com/?cid=12834472230370913091
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 57 min by car (45.4 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.58209850000001%2C-4.9497007&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long
  claim: 'Andalucía tourist board: ''calles estrechas y empinadas con casas de fachadas encaladas ... en la parte alta del pueblo, donde aún se conserva parte de una torre de las murallas de la antigua fortaleza árabe''; ''Su término municipal forma parte del Parque Natural de la Sierra de Las Nieves, declarado por la Unesco Reserva de la Biosfera''.'
  source_url: https://www.andalucia.org/es/istan
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour towns fact check 2026-11-02)
  confidence: high
  notes: Read with Firecrawl (direct quotes) or directly on 2026-11-02. Supports the description of sights only; not opening hours, access or suitability.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  - tags
  description: Age groups, family scores and tags not assessed; energy_level Low is an editorial estimate.
  retryable: true
  owner: human_editor
- code: category_editorial_choice
  severity: info
  fields:
  - category
  description: 'Category ''City'' chosen by Claude (towns: City; marinas and sights: Excursions). Confirm at editorial review.'
  retryable: true
  owner: human_editor
- code: facts_partly_checked
  severity: warning
  fields:
  - parking
  - accessibility
  - visit_information
  description: Description checked against official tourism sources 2026-11-02. Parking, accessibility and practical visit information are still open.
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
