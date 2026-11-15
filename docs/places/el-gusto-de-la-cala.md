---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-EL-GUSTO-DE-LA-CALA-001
slug: el-gusto-de-la-cala
name: El Gusto de la Cala
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.5045307
  longitude: -4.6803498999999995
  purpose: venue
  label: El Gusto de la Cala, Blvd. de la Cala, 3, 29649 La Cala de Mijas, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJAfk4nDEecw0R1rawPp9RUXE, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=8165397343792838358
external_ids:
  google_place_id: ChIJAfk4nDEecw0R1rawPp9RUXE
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 11 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: El Gusto de la Cala, Blvd. de la Cala, 3, 29649 La Cala de Mijas, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5045307,-4.6803498999999995); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5045307%2C-4.6803498999999995&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 11 min, 6.0 km. One predicted sample.'
age_groups:
- Young adults
- Seniors
family_score:
  small_children: low
  children: low
  young_adults: high
  seniors: medium
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
  schedule: 'Check before visiting: the own website shows ''open every day 16:00-00:00'' and a brunch menu 11:00-17:00; Sunday roast from October, Sundays 13:00-19:00 (2026-11-15).'
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own website 2026-11-15: Sunday roast 19,50 € per person; menu shown as images, not read.'
  cost_checked_at: '2026-11-15'
links:
  official_website: http://www.elgustodelacala.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'El Gusto de la Cala: brasserie and steakhouse with live music and cocktails in La Cala de Mijas, about 11 min by car.'
description_long: El Gusto de la Cala is a brasserie and steakhouse on Boulevard de la Cala in La Cala de Mijas, open since 2003, with live music and signature cocktails. Its own site gives 'open every day 16:00-00:00' next to the cocktail section and a brunch menu 11:00-17:00, so it is unclear which hours apply to the restaurant; check before visiting. From October there is a Sunday roast every Sunday 13:00-19:00 at 19,50 € per person (checked 2026-11-15). About 11 minutes by car from Casa de la Familia.
seo_title: El Gusto de la Cala, Mijas | CalleMilano draft record
seo_description: 'Draft record for El Gusto de la Cala (Mijas): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'El Gusto de la Cala' at Blvd. de la Cala, 3, 29649 La Cala de Mijas, Málaga, España (36.5045307,-4.6803498999999995), status OPERATIONAL, type restaurant.
  source_url: https://maps.google.com/?cid=8165397343792838358
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes. Editor: keep as restaurant; own sources give conflicting hours (16-24 vs brunch 11-17); show ''check before visiting''.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 11 min by car (6.0 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5045307%2C-4.6803498999999995&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long (type)
  claim: '''BRASSERIE & STEAKHOUSE''; ''ACTUACIONES''; ''CÓCTEL DE AUTOR''; ''Desde 2003''; ''Blvd. de la Cala, 3, 29649 La Cala de Mijas''.'
  source_url: https://www.elgustodelacala.com/es.html
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
- field: visit_information.schedule
  claim: '''ABIERTO TODOS LOS DIAS · 16:00 — 00:00'' (cocktail block) and ''Carta de Brunch | De 11:00 a 17:00''.'
  source_url: https://www.elgustodelacala.com/es.html
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: low
  notes: 'Unclear which hours apply. Editor decision 2026-11-15 on the owner checklist (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): show ''check before visiting''.'
- field: visit_information.cost_basis
  claim: '''Sunday Roast | Todos los domingos a partir de Octubre de 13:00 a 19:00 · 19,50 € por persona.'''
  source_url: https://www.elgustodelacala.com/es.html
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
- field: tags, age_groups, family_score, energy_level
  claim: 'Editor decision 2026-11-15 on the tags list: tags = Restaurant; age_groups = Young adults, Seniors; family_score = small_children low, children low, young_adults high, seniors medium; energy_level = Low.'
  source_url: https://claude.ai/artifact/VoHiKgGvqiiP3YA66KP3s5
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-15
  confidence: high
  notes: The editor's own judgement; answers stored in collection tags_2026_11_15.
review_issues:
- code: not_found_first_attempt
  severity: warning
  fields:
  - cost_level
  description: 'First source attempt 2026-11-15 found no official answer for: menu prices (menu shown as images). Value left unknown; check before visiting.'
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
