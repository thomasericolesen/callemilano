---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-LORENA-CAFE-ARROYO-DE-LA-MIEL-001
slug: lorena-cafe-arroyo-de-la-miel
name: Lorena Café Arroyo de la Miel
category: Restaurants
tags: []
coordinates:
  latitude: 36.5997951
  longitude: -4.5313682
  purpose: venue
  label: Lorena Café Arroyo de la Miel, Av. de la Constitución, 12, Loc 20, 29631 Arroyo de La Miel, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJTauPSiT9cg0RRy96oB_wm0g, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=5232039410747977543
external_ids:
  google_place_id: ChIJTauPSiT9cg0RRy96oB_wm0g
municipality: Benalmádena
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 22 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Lorena Café Arroyo de la Miel, Av. de la Constitución, 12, Loc 20, 29631 Arroyo de La Miel, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5997951,-4.5313682); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5997951%2C-4.5313682&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 22 min, 18.2 km. One predicted sample.'
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
cost_level: €
visit_information:
  schedule: Kitchen until 23:00, café until 00:00; opening time not stated (own website, 2026-11-15).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own carta 2026-11-15: dishes about 6,95-15 €.'
  cost_checked_at: '2026-11-15'
links:
  official_website: https://www.lorenacafe.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Lorena Café Arroyo de la Miel: café for breakfast, sandwiches, burgers and bowls in Benalmádena, about 22 min by car.'
description_long: Lorena Café Arroyo de la Miel is one of four Lorena Café venues, serving breakfasts, sandwiches, burgers, bowls and juices from the same menu in all four (Av. de la Constitución, 12, Local 20, 29631 Arroyo de la Miel). The kitchen is open until 23:00 and the café until 00:00; the opening time is not stated. Dishes cost about 6,95-15 € (own website, checked 2026-11-15). About 22 minutes by car from Casa de la Familia.
seo_title: Lorena Café Arroyo de la Miel, Benalmádena | CalleMilano draft record
seo_description: 'Draft record for Lorena Café Arroyo de la Miel (Benalmádena): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Lorena Café Arroyo de la Miel' at Av. de la Constitución, 12, Loc 20, 29631 Arroyo de La Miel, Málaga, España (36.5997951,-4.5313682), status OPERATIONAL, type coffee_shop.
  source_url: https://maps.google.com/?cid=5232039410747977543
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 22 min by car (18.2 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5997951%2C-4.5313682&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule, cost_level, description_long
  claim: '''desayunos, bocadillos, burgers, bowls y zumos ... Misma carta en los cuatro locales''; address ''Av. de la Constitución, 12, Local 20, 29631 Arroyo de la Miel''; ''Cocina abierta hasta las 23:00'' / ''Local abierto hasta las 0:00''; carta dishes about 6,95-15,00 €.'
  source_url: http://lorenacafe.com/locales
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
- field: status
  claim: 'Lifted needs_fact_check -> needs_editorial_review: official or own-venue evidence for the core facts, no blocking or facts_not_checked issue (editor workflow, level A).'
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/AGENTS.md
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (main session)
  confidence: high
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  - tags
  description: Age groups, family scores and tags are not assessed; energy_level is an editorial estimate.
  retryable: true
  owner: human_editor
- code: not_found_first_attempt
  severity: warning
  fields:
  - visit_information.schedule
  description: 'First source attempt 2026-11-15 found no official answer for: opening time in the morning. Value left unknown; check before visiting.'
  retryable: true
  owner: fact_check
created_at: '2026-11-15'
updated_at: '2026-11-15'
last_verified: '2026-11-15'
last_reviewed_at: '2026-11-15'
next_review_at: '2027-04-15'
review_decision: null
redirects: []
---
