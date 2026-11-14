---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-EL-HIGUERON-FUENGIROLA-001
slug: el-higueron-fuengirola
name: Restaurante El Higuerón
category: Restaurants
tags:
- Restaurant
- Rainy day
- Half day
- Premium
coordinates:
  latitude: 36.5870167
  longitude: -4.5996649
  purpose: venue
  label: Restaurante El Higuerón, Autovia Costa del Sol, Salida 1008 Carretera Benalmadena Mijas Km 3, 1, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJq2VBvnTjcg0Rptt-17hGjmU, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=7317864204226976678
external_ids:
  google_place_id: ChIJq2VBvnTjcg0Rptt-17hGjmU
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 16 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante El Higuerón, Autovia Costa del Sol, Salida 1008 Carretera Benalmadena Mijas Km 3, 1, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5870167,-4.5996649); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5870167%2C-4.5996649&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 16 min, 11.7 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: medium
  children: medium
  young_adults: medium
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
  availability: 'yes'
  location_type: onsite
  cost: unknown
  restrictions: unknown
  walk_distance: unknown
  source: Own website (elhigueron.com), read 2026-11-02
  checked_at: '2026-11-02'
transport_options: []
booking_required: unknown
dog_friendly: unknown
toilets_available: unknown
food_available: 'yes'
cost_level: €€
visit_information:
  schedule: 'Monday closed; Tuesday-Saturday 12:30-00:00; Sunday 12:30-18:00 (own website footer, read 2026-11-11). Kitchen hours on the site: breakfast 09:00-12:00, bar with non-stop kitchen 13:00-16:00, lunch 13:00-16:00.'
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own carta (restaurant page, partial text read): mains 21-43 €, median about 31 € (e.g. Fabada Asturiana 26, Presa Ibérica de Bellota 29, Solomillo 35, Lubina Salvaje 35); no drink prices read. Band rule: median main + one drink; precedent Venta Los Condes (median about 31 €) = €€. Borderline.'
  cost_checked_at: '2026-11-11'
links:
  official_website: http://elhigueron.com/
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34952119163
related_places: []
description_short: 'El Higueron: restaurant on the slopes of the Sierra de Mijas with breakfast, lunch and dinner service and private parking (own website).'
description_long: According to its own website, El Higueron lies on the foothills of the Sierra de Mijas and has private parking with more than 100 spaces. The website lists breakfast 09:00-12:00, a bar with non-stop kitchen and lunch 13:00-16:00, closing to the public at 17:00 and dinner from 20:30. Days of the week are not stated in the text we read. Prices, booking and children's facilities were not found.
seo_title: Restaurante El Higuerón, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Restaurante El Higuerón (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Restaurante El Higuerón' at Autovia Costa del Sol, Salida 1008 Carretera Benalmadena Mijas Km 3, 1, 29640 Fuengirola, Málaga, España (36.5870167,-4.5996649), status OPERATIONAL, type restaurant.
  source_url: https://maps.google.com/?cid=7317864204226976678
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. Owner selected directory lead R-0305 on 2026-11-02 (checklist https://claude.ai/artifact/VCrXrv5vKsUhruvVk6R9ZT).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 16 min by car (11.7 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5870167%2C-4.5996649&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule
  claim: '"Desayunos (Breakfast) 09:00 – 12:00"; "Bar (Cocina non-Stop) 13:00 – 16:00"; "Almuerzo (Lunch) 13:00 – 16:00"; "Cierre al público 17:00h"; "Cena (Dinner) 20:30h"'
  source_url: http://elhigueron.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: medium
  notes: Read via Firecrawl query after curl 503. No days of week; no street address on page.
- field: parking.availability, parking.location_type
  claim: '"Además, contamos con parking privado con más de 100 plazas"; "Nos situamos en las faldas de la Sierra de Mijas"'
  source_url: http://elhigueron.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: medium
  notes: Parking quote taken from reader notes, not from a quote entry; cost and restrictions unknown.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults medium, seniors medium; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Restaurant, Rainy day, Half day, Premium."
  source_url: https://claude.ai/artifact/DZv9cLLQ1BEcYs3NeewdEF
  source_type: secondary
  checked_at: '2026-11-11'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-11
  confidence: medium
  notes: Owner's own judgment on the tag checklist on 2026-11-11 (previous tags were estimates from import); not independently verified. source_type secondary is the nearest schema value.
- field: visit_information.schedule; links.contact
  claim: "\"Horario:\"; \"Lunes cerrado\"; \"Martes a Sábado 12:30 a 00:00\"; \"Domingo 12:30 a 18:00\"; \"Telf (+34) 952 11 91 63\"; \"Email. reservas@elhigueron.com\""
  source_url: http://elhigueron.com/
  source_type: official_venue
  checked_at: '2026-11-11'
  checked_by: Claude (main session); own site fetched with tools/intake.py fetch and Tavily extract
  confidence: high
  notes: "Footer of the own home page. The earlier schedule text (09:00-12:00 breakfast, closed 17:00, dinner 20:30) came from the 24 and 31 December notices on the page and is replaced by the regular hours. The site's menu navigation has an \"Infantil\" (children's) section that was not read."
- field: cost_level (menu prices)
  claim: "\"Fabada Asturiana ... 26\"; \"Presa Ibérica de Bellota 29\"; \"Solomillo ... 35\"; \"Lubina Salvaje ... 35\"; \"Solomillo Asturiano ... 68\" (for two)"
  source_url: http://elhigueron.com/restaurante/
  source_type: official_venue
  checked_at: '2026-11-11'
  checked_by: Claude (main session); own site fetched with tools/intake.py fetch and Tavily extract
  confidence: medium
  notes: "Partial text of the restaurant carta (Tavily extract); mains 21-43 €, median about 31 €. No drink prices read. Menu date not stated."
review_issues:
- code: cost_level_borderline
  severity: info
  fields:
  - cost_level
  description: "Median main about 31 € plus a drink is at the upper edge of the €€ band (rule of 2026-11-03); only part of the carta text was read and no drink prices."
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: null
next_review_at: 2027-02-14
review_decision: null
redirects: []
---
