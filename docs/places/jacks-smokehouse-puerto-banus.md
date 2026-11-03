---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-JACKS-SMOKEHOUSE-PUERTO-BANUS-001
slug: jacks-smokehouse-puerto-banus
name: Jacks Smokehouse (Puerto Banús)
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.4885233
  longitude: -4.9510252
  purpose: venue
  label: Jacks Smokehouse, de Ribera, C. Mlle. Salman, 22-24, Nueva Andalucía, 29660 Marbella, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ1bNMKcEpcw0RacCk-_v-U_o, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=18038041290761093225
external_ids:
  google_place_id: ChIJ1bNMKcEpcw0RacCk-_v-U_o
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 41 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Jacks Smokehouse, de Ribera, C. Mlle. Salman, 22-24, Nueva Andalucía, 29660 Marbella, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4885233,-4.9510252); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4885233%2C-4.9510252&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 41 min, 36.4 km. One predicted sample.'
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
  schedule: null
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'No prices on own site; Tripadvisor price marking "€€ - €€€" read as the middle band. Fallback source per docs/trip-planner-agents.md. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).N'
  cost_checked_at: '2026-11-02'
links:
  official_website: https://www.jacks-smokehouse.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- playa-puerto-banus
description_short: 'Jack''s Smokehouse, Puerto Banús: New York-style barbecue restaurant in the port.'
description_long: Jack's Smokehouse is a New York-style barbecue restaurant with branches in Puerto Marina (Benalmádena) and Puerto Banús (own website description). This record is the Puerto Banús branch. Opening hours, prices and booking were not readable on the site.
seo_title: Jacks Smokehouse (Puerto Banús), Marbella | CalleMilano
seo_description: 'Jacks Smokehouse (Puerto Banús) (Marbella): food, opening hours and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'Jacks Smokehouse' at de Ribera, C. Mlle. Salman, 22-24, Nueva Andalucía, 29660 Marbella, Málaga, España (36.4885233,-4.9510252), business status OPERATIONAL, primary type american_restaurant; about 227 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=18038041290761093225
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/one-hour-beach-restaurants-intake-2026-11-02.md, row rD04).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 41 min by car (36.4 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4885233%2C-4.9510252&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long, visit_information, food_available
  claim: 'Own site description: ''Jacks Smokehouse Restaurant in Puerto Marina, Benalmádena and Puerto Banús brings a New York feel ... authentic BBQ experience''.'
  source_url: https://www.jacks-smokehouse.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant fact check 2026-11-02)
  confidence: medium
  notes: Own website read with Firecrawl (direct quotes) on 2026-11-02. Only the page description was readable.
- field: cost_level
  claim: '"€€ - €€€"'
  source_url: https://www.tripadvisor.es/Restaurant_Review-g1207898-d792718-Reviews-Jacks_Smokehouse-Puerto_Banus_Marbella_Costa_del_Sol_Province_of_Malaga_Andalucia.html
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: low
  notes: Tripadvisor price marking only (search excerpt); no ratings or reviews recorded. Own-site prices preferred when available. Quote from search snippet of tripadvisor.es listing. Name and town match (Puerto Banús).
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
  - visit_information
  - cost_level
  - booking_required
  description: 'Own website checked 2026-11-02. Still open: visit_information, cost_level. Opening hours change by season; check before publishing.'
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
