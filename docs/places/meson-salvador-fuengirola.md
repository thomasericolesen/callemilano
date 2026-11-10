---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-MESON-SALVADOR-FUENGIROLA-001
slug: meson-salvador-fuengirola
name: Mesón Salvador
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.5544279
  longitude: -4.6140142
  purpose: venue
  label: Mesón Salvador, Av. de los Boliches, 97, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ7_eyIFDicg0RMY51FzkG8VA, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=5832449834697985585
external_ids:
  google_place_id: ChIJ7_eyIFDicg0RMY51FzkG8VA
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 15 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Mesón Salvador, Av. de los Boliches, 97, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5544279,-4.6140142); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5544279%2C-4.6140142&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 15 min, 6.6 km. One predicted sample.'
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
cost_level: Unknown
visit_information:
  schedule: Mon-Sat 8:30-23:00 (kitchen); closed Sunday. Taken from undated notices on the own Facebook page; not confirmed as current.
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: https://www.facebook.com/Meson-Salvador-Comida-Casera-1231393506981047/
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34952587494
related_places: []
description_short: 'Mesón Salvador: homely Spanish restaurant (''comida casera'') in Los Boliches, about 15 min by car from Casa de la Familia; open Monday to Saturday according to Facebook notices.'
description_long: 'Mesón Salvador (Facebook: ''Meson Salvador Comida Casera'') is a Spanish restaurant in Los Boliches, Fuengirola, about 15 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Its own Facebook page lists phone +34 952 58 74 94. Two photo notices on the page say that Sundays are closed and that the usual hours on other days are 8:30 to 23:00 (kitchen); a further notice gives shorter hours (8:30-17:00) for 6 to 11 October ''as every year''. The notices are undated, so the hours may be out of date. The page shows Christmas group menus (38, 45 and 55 EUR with drink, post of 30 October 2026) but no regular menu, so the price level is unknown. Check before visiting.'
seo_title: Mesón Salvador, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Mesón Salvador (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Mesón Salvador' at Av. de los Boliches, 97, 29640 Fuengirola, Málaga, España (36.5544279,-4.6140142), status OPERATIONAL, type restaurant.
  source_url: https://maps.google.com/?cid=5832449834697985585
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. Owner selected directory lead R-0107 on 2026-11-02 (checklist https://claude.ai/artifact/VCrXrv5vKsUhruvVk6R9ZT).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 15 min by car (6.6 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5544279%2C-4.6140142&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: links.contact; visit_information.schedule
  claim: '"Queridos clientes, Os informamos que, a partir de ahora, los Domingos permaneceremos cerrados por descanso del personal. El resto de días, mantendremos nuestro horario habitual de 8:30 a 23:00 (cocina)" ; "Como cada año nuestro horario del 6 al 11 de Octubre será de 8:30 a 17:00. El Domingo permanecemos cerrado."'
  source_url: https://www.facebook.com/profile.php?id=100063518890340
  source_type: official_venue
  checked_at: '2026-11-10'
  checked_by: Claude (main session), Claude in Chrome, logged-in read-only
  confidence: medium
  notes: Own Facebook page, read 2026-11-10. The notices are photos and undated in the grid (one of the newer ones), so confidence is medium at best. Phone +34 952 58 74 94; address field only '29640, Fuengirola, Spain'.
- field: cost_level (not set)
  claim: '"MENÚ 1 38€ / MENÚ 2 45€ / MENÚ 3 55€. Todos los menús incluyen bebida."'
  source_url: https://www.facebook.com/profile.php?id=100063518890340
  source_type: official_venue
  checked_at: '2026-11-10'
  checked_by: Claude (main session), Claude in Chrome, logged-in read-only
  confidence: low
  notes: 'Post of 30 Oct 2026: Christmas group menus only; not usable for the a la carte price rule. No regular carta found.'
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
- code: facts_partly_checked
  severity: warning
  fields:
  - cost_level
  - accessibility
  - parking
  description: 'Phone and hours from own Facebook notices (undated, 2026-11-10). Still open: current hours, regular menu and prices (cost_level Unknown), accessibility, parking.'
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-10'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
