---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-KOCO-BISTRO-001
slug: koco-bistro
name: Koco Bistró
category: Restaurants
tags: []
coordinates:
  latitude: 36.596716199999996
  longitude: -4.6374007
  purpose: venue
  label: Koco Bistró, Pl. Virgen de la Peña, 3, 29650 Mijas, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJbxPHHfvjcg0R7fOIqa7ZEZ0, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=11318066682750628845
external_ids:
  google_place_id: ChIJbxPHHfvjcg0R7fOIqa7ZEZ0
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 20 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Koco Bistró, Pl. Virgen de la Peña, 3, 29650 Mijas, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.596716199999996,-4.6374007); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.596716199999996%2C-4.6374007&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 20 min, 11.2 km. One predicted sample.'
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
  cost_basis: 'Own menu 2026-11-15: tapas 3,50-9,90 €, mains 17,90-34,90 €; a main plus a drink is over 20 €.'
  cost_checked_at: '2026-11-15'
links:
  official_website: https://go.nordqr.com/koco-bistro/
  booking: null
  visitor_information: null
  transport: null
  contact: +34 95286152
related_places: []
description_short: 'Koco Bistró: tapas bistro in Mijas Pueblo, about 20 min by car from Casa de la Familia.'
description_long: Koco Bistró is a tapas bistro on Avenida Virgen de la Peña in Mijas Pueblo; its own digital menu calls it a 'Lugar de tapas en mijas'. Menu prices (checked 2026-11-15) run from 3,50 € for small tapas to 34,90 € for a 220 g beef sirloin; most mains are 17-35 €. The menu lists no children's menu. Opening hours are not published on the menu; check before visiting. About 20 minutes by car from Casa de la Familia.
seo_title: Koco Bistró, Mijas | CalleMilano draft record
seo_description: 'Draft record for Koco Bistró (Mijas): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Koco Bistró' at Pl. Virgen de la Peña, 3, 29650 Mijas, Málaga, España (36.596716199999996,-4.6374007), status OPERATIONAL, type restaurant.
  source_url: https://maps.google.com/?cid=11318066682750628845
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes. Editor: keep as restaurant, mention tapas in the text.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 20 min by car (11.2 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.596716199999996%2C-4.6374007&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long, category (type)
  claim: 'Own menu: ''Lugar de tapas en mijas''; logo ''Koco Bistró Tapas''; address ''Avenida Virgen de la Peña, 3, Mijas''.'
  source_url: https://go.nordqr.com/koco-bistro/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
- field: cost_level, visit_information.cost_basis
  claim: 'Menu: ''Camembert frito'' 3.50 €, ''Calamar en tempura'' 6.50 €, ''Pollo al curry verde'' 17.90 €, ''Solomillo de Ternera (220gr)'' 34.90 €; 61 prices from 3,50 to 34,90 €. No children''s menu (searched infantil/niño/kids).'
  source_url: https://go.nordqr.com/koco-bistro/
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
  description: 'First source attempt 2026-11-15 found no official answer for: opening hours and closing days. Value left unknown; check before visiting.'
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
