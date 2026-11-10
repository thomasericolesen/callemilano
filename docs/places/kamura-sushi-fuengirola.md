---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-KAMURA-SUSHI-FUENGIROLA-001
slug: kamura-sushi-fuengirola
name: Kamura Sushi
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.5548332
  longitude: -4.6134485
  purpose: venue
  label: Restaurante Kamura Sushi, Av. de los Boliches, 108, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJF01fJVDicg0REeH6Zp_vJMs, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=14638088156767510801
external_ids:
  google_place_id: ChIJF01fJVDicg0REeH6Zp_vJMs
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 15 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante Kamura Sushi, Av. de los Boliches, 108, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5548332,-4.6134485); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5548332%2C-4.6134485&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 15 min, 6.4 km. One predicted sample.'
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
  schedule: Tue 13:00-16:00 (bento boxes only); Wed-Sat 13:00-16:00 and 20:00-23:00; no hours listed for Sun and Mon (closed implied). Not stated as seasonal (own website, undated).
  typical_duration: null
  booking_lead_time: Booking recommended; two dinner sittings at weekends or busy days (20:00-21:30 or 21:30-23:00).
  valid_from: null
  valid_until: null
  cost_basis: 'Own carta (image, undated): sushi sets (bandejas) takara 16,00; sakura 19,00; kiku 21,00; maki 24,50; salmon dake 32,00 EUR, median 21 EUR, plus one drink. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-10'
links:
  official_website: http://kamurasushi.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Kamura Sushi: small sushi restaurant in Los Boliches with takeaway pick-up and a few tables, open Tuesday to Saturday; booking recommended.'
description_long: Kamura Sushi is a sushi restaurant in Los Boliches, about 15 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). According to its own website it is open Tuesday 13:00-16:00 (bento boxes only) and Wednesday to Saturday 13:00-16:00 and 20:00-23:00; no hours are given for Sunday and Monday. The site recommends booking and says there are two dinner sittings at weekends or busy days (20:00-21:30 or 21:30-23:00). Orders are picked up at the restaurant (no home delivery) and can be eaten there on the terrace or inside. The own carta (an undated image) lists sushi sets at 16 to 32 EUR (median 21 EUR), so about 24 EUR per person with a drink. Check the hours and prices before going.
seo_title: Kamura Sushi, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Kamura Sushi (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Restaurante Kamura Sushi' at Av. de los Boliches, 108, 29640 Fuengirola, Málaga, España (36.5548332,-4.6134485), status OPERATIONAL, type sushi_restaurant.
  source_url: https://maps.google.com/?cid=14638088156767510801
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. Owner selected directory lead R-0105 on 2026-11-02 (checklist https://claude.ai/artifact/VCrXrv5vKsUhruvVk6R9ZT).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 15 min by car (6.4 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5548332%2C-4.6134485&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule; booking
  claim: '"SE RECOMIENDA RESERVAR, TENEMOS DOBLE TURNO PARA LAS CENAS EN FIN DE SEMANA O DÍAS CONCURRIDOS: (20:00-21:30 o 21:30-23:00)" ; "Martes 13:00 - 16:00 sólo cajas Bento" ; "Miércoles a sábado 13:00 - 16:00 y 20:00 - 23:00" ; "para recogida de encargos en local y comer allí (terraza o dentro)."'
  source_url: http://www.kamurasushi.com/horario/
  source_type: official_venue
  checked_at: '2026-11-10'
  checked_by: Claude (main session), Claude in Chrome, logged-in read-only
  confidence: high
  notes: 'Own website, read in a real browser 2026-11-10; undated. Home page: ''sólo recoger en local, no a domicilio''. Sunday and Monday not listed (closed implied, not stated). Booking is recommended, not required, so booking_required stays unknown.'
- field: cost_level
  claim: 'Bandejas: takara 16,00; sakura 19,00; kiku 21,00; maki 24,50; salmon dake 32,00. Usuzukuri 16-19; sashimi 10-18,50; uramaki 7,80-15,50.'
  source_url: http://www.kamurasushi.com/app/download/11389959/Carta+Kamura+Sushi.png
  source_type: official_venue
  checked_at: '2026-11-10'
  checked_by: Claude (main session), Claude in Chrome, logged-in read-only
  confidence: medium
  notes: Own carta image, undated, read 2026-11-10. Median set 21 EUR plus one drink (about 24 EUR) gives €€.
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
  - accessibility
  - parking
  - booking_required
  description: 'Hours, booking advice and carta prices from own website (2026-11-10). Still open: accessibility, parking, whether booking is mandatory, child facilities.'
  retryable: true
  owner: fact_check
- code: cost_menu_undated
  severity: info
  fields:
  - cost_level
  description: The carta image is undated; prices may have changed.
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
