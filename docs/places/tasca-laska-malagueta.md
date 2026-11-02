---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-TASCA-LASKA-MALAGUETA-001
slug: tasca-laska-malagueta
name: Tasca Láska Malagueta
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.7193155
  longitude: -4.4091223
  purpose: venue
  label: Tasca láska Malagueta, C. Fernando Camino, 15, Málaga-Este, 29016 Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJxbuuQof3cg0R2aBBQ7v6bw4, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=1040325721140076761
external_ids:
  google_place_id: ChIJxbuuQof3cg0R2aBBQ7v6bw4
municipality: Málaga
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 43 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Tasca láska Malagueta, C. Fernando Camino, 15, Málaga-Este, 29016 Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.7193155,-4.4091223); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.7193155%2C-4.4091223&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 43 min, 37.3 km. One predicted sample.'
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
cost_level: Unknown
visit_information:
  schedule: Mon, Thu-Sun 12:00-00:00 (kitchen 12:00-23:00); closed Tue-Wed (own site, read 2026-11-02).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: https://tascalaska.es/es/tasca-laska-malagueta/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- playa-la-malagueta
description_short: 'Tasca Láska Malagueta: rice dishes and tapas about 150 m from Malagueta beach.'
description_long: Tasca Láska Malagueta serves paellas and rice dishes, creative tapas and wine, at Calle Fernando Camino 15 by the bullring, about 150 m from Malagueta beach and 5 minutes' walk from Muelle Uno (own website). Open Monday and Thursday-Sunday 12:00-00:00, kitchen 12:00-23:00; closed Tuesday and Wednesday. Online booking. The restaurant lists a baby-changing table and short-stay parking around it.
seo_title: Tasca Láska Malagueta, Málaga | CalleMilano
seo_description: 'Tasca Láska Malagueta (Málaga): food, opening hours and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'Tasca láska Malagueta' at C. Fernando Camino, 15, Málaga-Este, 29016 Málaga, España (36.7193155,-4.4091223), business status OPERATIONAL, primary type restaurant; about 272 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=1040325721140076761
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/one-hour-beach-restaurants-intake-2026-11-02.md, row rA03).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 43 min by car (37.3 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.7193155%2C-4.4091223&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long, visit_information, food_available
  claim: 'Own site: ''a solo 150 metros de la playa de la Malagueta''; Fernando Camino 15, 29016 Málaga; open lunes, jueves, viernes, sábado y domingo 12:00-0:00, martes y miércoles cerrado, cocina 12:00-23:00; reserva online; ''Cambiador para bebés''; parking de corta duración alrededor. Site title: tapas, paellas.'
  source_url: https://tascalaska.es/es/tasca-laska-malagueta/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant fact check 2026-11-02)
  confidence: high
  notes: Own website read with Firecrawl (direct quotes) on 2026-11-02.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  description: Age groups and family scores are not assessed.
  retryable: true
  owner: human_editor
- code: facts_partly_checked
  severity: warning
  fields:
  - cost_level
  description: 'Own website checked 2026-11-02. Still open: cost_level. Opening hours change by season; check before publishing.'
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
