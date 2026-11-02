---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-SOLO-BEACH-MARBELLA-001
slug: solo-beach-marbella
name: Solo Beach Marbella
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.4754104
  longitude: -4.9822923999999995
  purpose: venue
  label: Solo Beach Marbella, Av. Carlos Cano, 29670 Marbella, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ66dm7Pwrcw0RgbV8HvrKl2Y, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=7392600488954082689
external_ids:
  google_place_id: ChIJ66dm7Pwrcw0RgbV8HvrKl2Y
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 40 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Solo Beach Marbella, Av. Carlos Cano, 29670 Marbella, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4754104,-4.9822923999999995); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4754104%2C-4.9822923999999995&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 40 min, 39.4 km. One predicted sample.'
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
  schedule: Daily 09:00-21:00 (own site, read 2026-11-02).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: https://solobeachmarbella.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- playa-de-san-pedro-alcantara
description_short: 'Solo Beach: Mediterranean beach restaurant and sunbeds on the sand at San Pedro de Alcántara.'
description_long: Solo Beach is a beach restaurant and beach club on the sand at San Pedro de Alcántara, serving Mediterranean food, poke and cocktails (own website). The site lists daily opening 09:00-21:00, sunbed hire ('Solo Hamaca', 10 €) and table booking on request; phone +34 621 35 09 97.
seo_title: Solo Beach Marbella, Marbella | CalleMilano
seo_description: 'Solo Beach Marbella (Marbella): food, opening hours and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'Solo Beach Marbella' at Av. Carlos Cano, 29670 Marbella, Málaga, España (36.4754104,-4.9822923999999995), business status OPERATIONAL, primary type bar_and_grill; about 472 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=7392600488954082689
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/one-hour-beach-restaurants-intake-2026-11-02.md, row rE01).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 40 min by car (39.4 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4754104%2C-4.9822923999999995&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long, visit_information, food_available
  claim: 'Own site: ''Solo Beach nace en la arena de San Pedro de Alcántara''; cocina mediterránea, poke, cócteles; ''Lunes – Domingo 09:00 – 21:00''; ''Solo Hamaca 10 €''; Solicitar reserva; +34 621 35 09 97.'
  source_url: https://solobeachmarbella.com/
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
