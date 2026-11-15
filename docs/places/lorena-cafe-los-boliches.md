---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-LORENA-CAFE-LOS-BOLICHES-001
slug: lorena-cafe-los-boliches
name: Lorena Café Los Boliches
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.5472603
  longitude: -4.6183022
  purpose: venue
  label: Lorena Café Los Boliches, Av. Ramón y Cajal, 48, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ04fOCUTicg0RXAvvVrhNUxo, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=1896945322180938588
external_ids:
  google_place_id: ChIJ04fOCUTicg0RXAvvVrhNUxo
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 15 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Lorena Café Los Boliches, Av. Ramón y Cajal, 48, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5472603,-4.6183022); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5472603%2C-4.6183022&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 15 min, 6.3 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: medium
  children: high
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
  official_website: http://lorenacafe.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Lorena Café Los Boliches: café for breakfast, sandwiches, burgers and bowls in Fuengirola, about 15 min by car.'
description_long: Lorena Café Los Boliches is one of four Lorena Café venues, serving breakfasts, sandwiches, burgers, bowls and juices from the same menu in all four (Av. Ramón y Cajal, 48, 29640 Fuengirola). The kitchen is open until 23:00 and the café until 00:00; the opening time is not stated. Dishes cost about 6,95-15 € (own website, checked 2026-11-15). About 15 minutes by car from Casa de la Familia.
seo_title: Lorena Café Los Boliches, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Lorena Café Los Boliches (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Lorena Café Los Boliches' at Av. Ramón y Cajal, 48, 29640 Fuengirola, Málaga, España (36.5472603,-4.6183022), status OPERATIONAL, type cafeteria.
  source_url: https://maps.google.com/?cid=1896945322180938588
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 15 min by car (6.3 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5472603%2C-4.6183022&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule, cost_level, description_long
  claim: '''desayunos, bocadillos, burgers, bowls y zumos ... Misma carta en los cuatro locales''; address ''Av. Ramón y Cajal, 48, 29640 Fuengirola''; ''Cocina abierta hasta las 23:00'' / ''Local abierto hasta las 0:00''; carta dishes about 6,95-15,00 €.'
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
- field: tags, age_groups, family_score, energy_level
  claim: 'Editor decision 2026-11-15 on the tags list: tags = Restaurant; age_groups = Small children (0-6), Children (7-12), Young adults, Seniors; family_score = small_children medium, children high, young_adults high, seniors medium; energy_level = Low.'
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
