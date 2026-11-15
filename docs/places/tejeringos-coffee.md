---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-TEJERINGOS-COFFEE-001
slug: tejeringos-coffee
name: Tejeringo's Coffee
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.5410751
  longitude: -4.6247877
  purpose: venue
  label: Tejeringo's Coffee, P.º Jesús Santos Rein, 1, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJlf2GfiXjcg0RYnpanTAve8c, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=14374134521527958114
external_ids:
  google_place_id: ChIJlf2GfiXjcg0RYnpanTAve8c
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 13 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Tejeringo's Coffee, P.º Jesús Santos Rein, 1, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5410751,-4.6247877); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5410751%2C-4.6247877&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 13 min, 5.0 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: high
  children: high
  young_adults: medium
  seniors: high
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
  schedule: Every day 08:00-13:00 and 17:00-21:00 (own website, 2026-11-15).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: http://www.tejeringoscoffee.es/
  booking: null
  visitor_information: null
  transport: null
  contact: 951 10 02 53
related_places: []
description_short: 'Tejeringo''s Coffee Fuengirola: churrería and café for churros and chocolate, about 13 min by car; closed 13:00-17:00.'
description_long: Tejeringo's Coffee is a churrería-café chain run by three generations of churro makers. The Fuengirola venue at Av. Jesús Santos Rein 1 is open every day 08:00-13:00 and 17:00-21:00, closed in the middle of the day; phone 951 10 02 53 (own website, checked 2026-11-15). Prices are not published. About 13 minutes by car from Casa de la Familia.
seo_title: Tejeringo's Coffee, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Tejeringo''s Coffee (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Tejeringo's Coffee' at P.º Jesús Santos Rein, 1, 29640 Fuengirola, Málaga, España (36.5410751,-4.6247877), status OPERATIONAL, type coffee_shop.
  source_url: https://maps.google.com/?cid=14374134521527958114
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes. Editor: keep under cafés (churrería).'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 13 min by car (5.0 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5410751%2C-4.6247877&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long
  claim: '''TRES GENERACIONES DE CHURREROS ARTESANOS''.'
  source_url: http://www.tejeringoscoffee.es/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
- field: visit_information.schedule, links.contact
  claim: '''Av. Jesús Santos Rein nº 1, 29640, Fuengirola'': ''Lunes - Viernes: 08:00 - 13:00 y 17:00 - 21:00'' / ''Sábado y Domingo: 08:00 - 13:00 y 17:00 - 21:00''; ''Telf: 951 10 02 53''.'
  source_url: https://www.tejeringoscoffee.es/locales/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
  notes: 'Editor decision 2026-11-15: keep under cafés.'
- field: status
  claim: 'Lifted needs_fact_check -> needs_editorial_review: official or own-venue evidence for the core facts, no blocking or facts_not_checked issue (editor workflow, level A).'
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/AGENTS.md
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (main session)
  confidence: high
- field: tags, age_groups, family_score, energy_level
  claim: 'Editor decision 2026-11-15 on the tags list: tags = Restaurant; age_groups = Small children (0-6), Children (7-12), Young adults, Seniors; family_score = small_children high, children high, young_adults medium, seniors high; energy_level = Low.'
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
  description: 'First source attempt 2026-11-15 found no official answer for: prices. Value left unknown; check before visiting.'
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
