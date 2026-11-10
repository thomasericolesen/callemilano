---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-FUNNY-HILL-KARTING-001
slug: funny-hill-karting
name: Funny Hill Karting
category: Family activities
tags: []
coordinates:
  latitude: 36.5431404
  longitude: -4.8651938
  purpose: venue
  label: Funny Hill Karting, Carretera antigua de Ojén-Marbella, Poligono 1, parcela 493 Cañada de Murta, 29610 Ojén, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJt4Lv8T7Zcg0Rflv-j9_NYiI, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=2477769105084406654
external_ids:
  google_place_id: ChIJt4Lv8T7Zcg0Rflv-j9_NYiI
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 34 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Funny Hill Karting, Carretera antigua de Ojén-Marbella, Poligono 1, parcela 493 Cañada de Murta, 29610 Ojén, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5431404,-4.8651938); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5431404%2C-4.8651938&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 34 min, 31.1 km. One predicted sample.'
age_groups:
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: low
  children: medium
  young_adults: high
  seniors: medium
energy_level: High
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
  schedule: Monday to Friday 15:00-21:00; Saturdays, Sundays and public holidays 12:00-21:00. Whether this is seasonal is not stated (own website, checked 2026-11-02).
  typical_duration: null
  booking_lead_time: null
  valid_from: '2026-11-02'
  valid_until: null
  cost_basis: EUR 20 per child, EUR 25 per adult, EUR 30 per kart, each 8 minutes (own website)
  cost_checked_at: '2026-11-02'
links:
  official_website: https://funnyhill.es/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: Go-kart track with children's rides on the old Ojén road above Marbella; about 34 min by car from Casa de la Familia.
description_long: 'Funny Hill Karting describes itself on its own website as a karting track with children''s attractions and hospitality. It lists bumper cars, a super jump, trampolines and more, and says the karts are safe and adaptable, so children can share the activity. About 34 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Own website opening hours: Monday to Friday 15:00-21:00; Saturdays, Sundays and public holidays 12:00-21:00. Prices listed: EUR 20 per child, EUR 25 per adult, EUR 30 per kart, each for 8 minutes. The page gives no minimum age or height for the karts. Address on the site: Carretera antigua de Ojén, Polígono 1, parcela 493, Cañada de Murta, 29610 Ojén-Marbella.'
seo_title: Funny Hill Karting, Marbella | CalleMilano draft record
seo_description: 'Draft record for Funny Hill Karting (Marbella): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Funny Hill Karting' at Carretera antigua de Ojén-Marbella, Poligono 1, parcela 493 Cañada de Murta, 29610 Ojén, Málaga, España (36.5431404,-4.8651938), status OPERATIONAL, type go_karting_venue.
  source_url: https://maps.google.com/?cid=2477769105084406654
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Places API (New). Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 34 min by car (31.1 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5431404%2C-4.8651938&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long
  claim: '"Pista de karting, atracciones infantiles, hostelería y mucho más" / "Disponemos de todo tipo de atracciones infantiles como coches de choque, súper salto, camas elásticas y más." / "Comparte con tus amigos una carrera inolvidable en unos karts super seguros, adaptables y divertidos."'
  source_url: https://funnyhill.es/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: high
  notes: null
- field: visit_information.schedule
  claim: '"De lunes a viernes de 15 a 21hs." / "Sábados, domingos y festivos de 12 a 21hs."'
  source_url: https://funnyhill.es/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: high
  notes: Seasonality not stated.
- field: visit_information.cost_basis
  claim: '"Precio: 20 € por niño - 8 minutos." / "Precio: 25 € por adulto - 8 minutos." / "Precio: 30 € por kart - 8 minutos."'
  source_url: https://funnyhill.es/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: high
  notes: null
- field: description_long (address)
  claim: '"Dirección: Carretera antigua de Ojén, Poligono 1, parcela 493 Cañada de Murta, 29610 Ojén-Marbella ."'
  source_url: https://funnyhill.es/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: high
  notes: null
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children low, children medium, young_adults high, seniors medium; energy_level High.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
review_issues:
- code: facts_partly_checked
  severity: warning
  fields:
  - age_groups
  - cost_level
  - accessibility
  - parking
  - toilets_available
  - food_available
  - booking_required
  description: Minimum age or height for karts is not stated on the page ('Para que también puedas compartir con los peques' only); ask the venue. Accessibility, parking, toilets, food details and booking not covered. 'hostelería' is mentioned but not described, so food_available left unknown.
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
