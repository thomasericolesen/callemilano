---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-PRISON-ISLAND-MALAGA-001
slug: prison-island-malaga
name: Prison Island Málaga
category: Family activities
tags: []
coordinates:
  latitude: 36.597178
  longitude: -4.514616999999999
  purpose: venue
  label: Prison Island Málaga, Plaza de la Goleta s/n C.C, Puerto Marina Shopping, Local L3, 29631 Benalmádena, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJubP79GT8cg0RatdRkjTslSI, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=2492157679356729194
external_ids:
  google_place_id: ChIJubP79GT8cg0RatdRkjTslSI
municipality: Benalmádena
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 27 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Prison Island Málaga, Plaza de la Goleta s/n C.C, Puerto Marina Shopping, Local L3, 29631 Benalmádena, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.597178,-4.514616999999999); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.597178%2C-4.514616999999999&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 27 min, 20.2 km. One predicted sample.'
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
cost_level: €€
visit_information:
  schedule: July-August 10:00-22:00; rest of the year 10:00-21:00 (own website, 2026-11-15).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own website 2026-11-15: 1 hour 18,50 € child / 25,50 € adult; 2 hours 21,50 € / 29 €.'
  cost_checked_at: '2026-11-15'
links:
  official_website: https://www.prisonislandmalaga.es/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Prison Island Málaga: team challenge rooms and laser tag at Puerto Marina, Benalmádena; all ages, under-15s with an adult, about 27 min by car.'
description_long: Prison Island Málaga at Puerto Marina, Benalmádena, has team challenge cells (teams of 3-5) and laser tag. All ages are allowed, but children under 15 must play with at least one adult per team. One hour costs 18,50 € per child and 25,50 € per adult; 2 hours cost 21,50 € and 29 €. Open 10:00-22:00 in July and August and 10:00-21:00 the rest of the year (own website, checked 2026-11-15). About 27 minutes by car from Casa de la Familia.
seo_title: Prison Island Málaga, Benalmádena | CalleMilano draft record
seo_description: 'Draft record for Prison Island Málaga (Benalmádena): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Prison Island Málaga' at Plaza de la Goleta s/n C.C, Puerto Marina Shopping, Local L3, 29631 Benalmádena, Málaga, España (36.597178,-4.514616999999999), status OPERATIONAL, type amusement_center.
  source_url: https://maps.google.com/?cid=2492157679356729194
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 27 min by car (20.2 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.597178%2C-4.514616999999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule, cost_level, age_groups (input)
  claim: '''Todas las edades están permitidas, pero los menores de 15 años deberan participar con al menos un adulto por equipo''; ''Niños: hasta 15 años''; ''1 Hora | Niño | 18,50€ | Adulto | 25,50€''; ''1,5 Horas | Niño | 20,00€ | Adulto | 27,50€''; ''2 Horas | Niño | 21,50€ | Adulto | 29,00€''; ''Julio y Agosto: 10:00 - 22:00 - Resto del año: 10:00 - 21:00''.'
  source_url: https://www.prisonislandmalaga.es/precios/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
  notes: Front page says '26 Celdas', price page 'nuestras 24 celdas' (minor).
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
created_at: '2026-11-15'
updated_at: '2026-11-15'
last_verified: '2026-11-15'
last_reviewed_at: '2026-11-15'
next_review_at: '2027-04-15'
review_decision: null
redirects: []
---
