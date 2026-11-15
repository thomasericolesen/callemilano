---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-RESTAURANTE-LA-REJA-001
slug: restaurante-la-reja
name: Restaurante La Reja
category: Restaurants
tags:
- Restaurant
- Viewpoint
coordinates:
  latitude: 36.595349399999996
  longitude: -4.6381157
  purpose: venue
  label: Restaurante La Reja. Steak House & Traditional Spanish Restaurant with Panoramic Views, C. de los Caños, 9, 29650 Mijas, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJSVxmMfvjcg0Rjbng0mplliE, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=2420233359237101965
external_ids:
  google_place_id: ChIJSVxmMfvjcg0Rjbng0mplliE
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 22 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante La Reja. Steak House & Traditional Spanish Restaurant with Panoramic Views, C. de los Caños, 9, 29650 Mijas, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.595349399999996,-4.6381157); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.595349399999996%2C-4.6381157&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 22 min, 11.5 km. One predicted sample.'
age_groups:
- Young adults
- Seniors
family_score:
  small_children: low
  children: low
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
cost_level: €€
visit_information:
  schedule: 'Check before visiting: the own website says both ''Tuesday: Closed'' and ''Monday - Sunday 12:00-22:30'' (2026-11-15).'
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own website 2026-11-15: starters from 9 €, mains 18-29 €, paella 18 € per person (min. 2).'
  cost_checked_at: '2026-11-15'
links:
  official_website: https://restaurantelareja.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Restaurante La Reja: steakhouse and Spanish restaurant with a panoramic terrace in Mijas Pueblo, about 22 min by car.'
description_long: 'Restaurante La Reja is a steakhouse and Spanish restaurant at Calle de Los Caños 9 in Mijas Pueblo, with panoramic views. Prices on its own site (checked 2026-11-15) run from 9 € for porra antequerana to 28-29 € for steaks; paella is 18 € per person for at least two. The site''s opening hours contradict themselves (''Tuesday: Closed'' and ''Monday - Sunday: 12:00 - 22:30''), so check before visiting. No children''s menu is mentioned. About 22 minutes by car from Casa de la Familia.'
seo_title: Restaurante La Reja, Mijas | CalleMilano draft record
seo_description: 'Draft record for Restaurante La Reja (Mijas): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Restaurante La Reja. Steak House & Traditional Spanish Restaurant with Panoramic Views' at C. de los Caños, 9, 29650 Mijas, Málaga, España (36.595349399999996,-4.6381157), status OPERATIONAL, type restaurant.
  source_url: https://maps.google.com/?cid=2420233359237101965
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes. Editor: own site has conflicting hours (''Tuesday Closed'' and ''Monday-Sunday''); show ''check before visiting'', hours unknown.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 22 min by car (11.5 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.595349399999996%2C-4.6381157&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long (type), cost_level
  claim: '''Steak House & Spanish Fine Cousine Restaurant''; ''Porras Antequeranas 9,00€'', ''Hungarian Goulash 18,00€'', ''Grilled Fillet Steak 28,00€'', ''Steak Al-Andalus 29,00€''; paella ''18,00€'' (''Minimum for two people, price per person''). Address ''Calle de Los Caños 9 29650 Mijas Pueblo''.'
  source_url: https://restaurantelareja.com/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
- field: visit_information.schedule
  claim: 'EN ''Tuesday : Closed / Monday – Sunday : 12:00 – 22:30''; ES ''Martes: Cerrado | Lunes – Domingo: 12:00 – 22:30'' (same on /es/ and /contact/).'
  source_url: https://restaurantelareja.com/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: low
  notes: 'Contradictory wording. Editor decision 2026-11-15 on the owner checklist (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): show ''check before visiting'' and leave the hours unknown.'
- field: status
  claim: 'Lifted needs_fact_check -> needs_editorial_review: official or own-venue evidence for the core facts, no blocking or facts_not_checked issue (editor workflow, level A).'
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/AGENTS.md
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (main session)
  confidence: high
- field: tags, age_groups, family_score, energy_level
  claim: 'Editor decision 2026-11-15 on the tags list: tags = Restaurant, Viewpoint; age_groups = Young adults, Seniors; family_score = small_children low, children low, young_adults medium, seniors high; energy_level = Low.'
  source_url: https://claude.ai/artifact/VoHiKgGvqiiP3YA66KP3s5
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-15
  confidence: high
  notes: The editor's own judgement; answers stored in collection tags_2026_11_15.
review_issues: []
created_at: '2026-11-15'
updated_at: '2026-11-15'
last_verified: '2026-11-15'
last_reviewed_at: '2026-11-15'
next_review_at: '2027-04-15'
review_decision: null
redirects: []
---
