---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-TOMILLO-LIMON-001
slug: tomillo-limon
name: Tomillo Limón
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.597366199999996
  longitude: -4.6366591999999995
  purpose: venue
  label: Tomillo Limón, Av. Virgen de la Peña, 11, 29650 Mijas, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ-YYs-vrjcg0RBbmYTbTCo4U, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=9629754507900008709
external_ids:
  google_place_id: ChIJ-YYs-vrjcg0RBbmYTbTCo4U
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 20 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Tomillo Limón, Av. Virgen de la Peña, 11, 29650 Mijas, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.597366199999996,-4.6366591999999995); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.597366199999996%2C-4.6366591999999995&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 20 min, 11.1 km. One predicted sample.'
age_groups:
- Young adults
- Seniors
family_score:
  small_children: low
  children: medium
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
  schedule: Tuesday-Saturday 12:00-00:00; kitchen 12:30-16:00 and 19:00-22:00. Closed Sunday and Monday (own website, 2026-11-15).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Carta 2026: dishes 6-24 €, desserts 6,50-8 €, bread 1,50 € per person.'
  cost_checked_at: '2026-11-15'
links:
  official_website: https://www.tomillolimon.es/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Tomillo Limón: restaurant with modern Spanish cooking in Mijas Pueblo, about 20 min by car.'
description_long: Tomillo Limón is a restaurant in Mijas Pueblo (Avenida Virgen de la Peña, 11) serving traditional Spanish cooking with a modern touch; its own site calls it a place for 'una comida familiar memorable'. Open Tuesday to Saturday 12:00-00:00, closed Sunday and Monday; the kitchen serves 12:30-16:00 and 19:00-22:00 (own website, checked 2026-11-15). Dishes on the 2026 menu cost 6-24 €, desserts 6,50-8 €, and bread 1,50 € per person. The menu has no children's menu. About 20 minutes by car from Casa de la Familia.
seo_title: Tomillo Limón, Mijas | CalleMilano draft record
seo_description: 'Draft record for Tomillo Limón (Mijas): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Tomillo Limón' at Av. Virgen de la Peña, 11, 29650 Mijas, Málaga, España (36.597366199999996,-4.6366591999999995), status OPERATIONAL, type restaurant.
  source_url: https://maps.google.com/?cid=9629754507900008709
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 20 min by car (11.1 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.597366199999996%2C-4.6366591999999995&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule
  claim: '''Domingo Cerrado'' / ''Lunes Cerrado'' / ''Martes – Sábado 12:00 – 00:00'' / ''Cocina abierta de 12:30 a 16:00 y de 19:00 a 22:00.'''
  source_url: https://www.tomillolimon.es/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
- field: description_long (type)
  claim: '''Restaurante en Mijas Pueblo''; ''cocina tradicional española se reinterpreta ... toque de autor''; ''el lugar perfecto para una cena romántica o una comida familiar memorable.'''
  source_url: https://www.tomillolimon.es/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
- field: cost_level, visit_information.cost_basis
  claim: 'Carta 2026 (PDF): ''Mini chapata de carrillada ... 6€'', ''Bravas ... 9€'', ''Nuestra burger de carrillada ... 16€'', ''Tabla de entrecote a la parrilla ... 24€''; ''Servicio Pan por persona 1,50€''. No children''s menu.'
  source_url: https://drive.google.com/file/d/1G8Vxqezy3C1scSCJP551l36UkS0677hD/view
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
  notes: Linked from the own website.
- field: status
  claim: 'Lifted needs_fact_check -> needs_editorial_review: official or own-venue evidence for the core facts, no blocking or facts_not_checked issue (editor workflow, level A).'
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/AGENTS.md
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (main session)
  confidence: high
- field: tags, age_groups, family_score, energy_level
  claim: 'Editor decision 2026-11-15 on the tags list: tags = Restaurant; age_groups = Young adults, Seniors; family_score = small_children low, children medium, young_adults medium, seniors high; energy_level = Low.'
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
