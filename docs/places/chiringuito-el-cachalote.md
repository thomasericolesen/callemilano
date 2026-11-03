---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-CHIRINGUITO-EL-CACHALOTE-001
slug: chiringuito-el-cachalote
name: Chiringuito El Cachalote
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.719982699999996
  longitude: -4.405285699999999
  purpose: venue
  label: Chiringuito El Cachalote, P.º Marítimo Pablo Ruiz Picasso, s/n, Málaga-Este, 29016, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJVdtypuf3cg0RFNC3gERp8Co, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=3094088686941753364
external_ids:
  google_place_id: ChIJVdtypuf3cg0RFNC3gERp8Co
municipality: Málaga
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 39 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Chiringuito El Cachalote, P.º Marítimo Pablo Ruiz Picasso, s/n, Málaga-Este, 29016, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.719982699999996,-4.405285699999999); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.719982699999996%2C-4.405285699999999&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 39 min, 37.1 km. One predicted sample.'
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
cost_level: €€
visit_information:
  schedule: Wed-Sun 11:30-19:00 (kitchen); closed Mon-Tue (own site, undated, read 2026-11-02).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'No prices on own site; Tripadvisor price marking "€€ - €€€" read as the middle band. Fallback source per docs/trip-planner-agents.md. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).N'
  cost_checked_at: '2026-11-02'
links:
  official_website: http://www.chiringuitoelcachalote.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- playa-la-malagueta
description_short: 'Chiringuito El Cachalote: family-run fish beach restaurant on Malagueta beach since 1980, with sardine espetos.'
description_long: 'Chiringuito El Cachalote is a family business on the Paseo Marítimo Pablo Ruiz Picasso by Calle Gutemberg, on Malagueta beach, serving Málaga-style fried fish (''pescaíto''), seafood and grilled sardine espetos since 1980 (own website). Opening hours on the site: Wednesday-Sunday 11:30-19:00 (kitchen); closed Monday and Tuesday. The hours are not dated, so check before going, especially outside summer.'
seo_title: Chiringuito El Cachalote, Málaga | CalleMilano
seo_description: 'Chiringuito El Cachalote (Málaga): food, opening hours and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'Chiringuito El Cachalote' at P.º Marítimo Pablo Ruiz Picasso, s/n, Málaga-Este, 29016, Málaga, España (36.719982699999996,-4.405285699999999), business status OPERATIONAL, primary type bar; about 552 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=3094088686941753364
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/one-hour-beach-restaurants-intake-2026-11-02.md, row rA04).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 39 min by car (37.1 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.719982699999996%2C-4.405285699999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long, visit_information, food_available
  claim: 'Own site: ''Desde 1980, esta empresa familiar ... pescaito ... espetos de sardinas a la brasa''; Paseo Marítimo Pablo Ruiz Picasso s/n (junto a Calle Gutemberg); horario miércoles a domingo 11:30-19:00 cocina; lunes y martes cerrado.'
  source_url: http://www.chiringuitoelcachalote.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant fact check 2026-11-02)
  confidence: high
  notes: Own website read with Firecrawl (direct quotes) on 2026-11-02.
- field: cost_level
  claim: '"€€ - €€€"'
  source_url: https://www.tripadvisor.es/Restaurant_Review-g187438-d4788282-Reviews-Chiringuito_El_Cachalote-Malaga_Costa_del_Sol_Province_of_Malaga_Andalucia.html
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: low
  notes: Tripadvisor price marking only (search excerpt); no ratings or reviews recorded. Own-site prices preferred when available. Quote from search snippet of tripadvisor.es listing. Name and town match (Málaga).
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
  - booking_required
  description: 'Own website checked 2026-11-02. Still open: cost_level. Opening hours change by season; check before publishing.'
  retryable: true
  owner: fact_check
- code: cost_level_secondary_source
  severity: info
  fields:
  - cost_level
  description: cost_level is based on the Tripadvisor price marking, not the own menu; replace when an own menu with prices is found.
  retryable: true
  owner: human_editor
created_at: '2026-11-02'
updated_at: '2026-11-03'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
