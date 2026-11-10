---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-MARISQUERIA-EL-ANCLA-SAN-PEDRO-001
slug: marisqueria-el-ancla-san-pedro
name: Marisquería El Ancla (San Pedro)
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.4701216
  longitude: -4.990124499999999
  purpose: venue
  label: Marisquería El Ancla, Av. Carmen Sevilla, s/n, 29670 Marbella, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJgwVAszAqcw0R0TkPQ62h-Lo, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=13472696050805324241
external_ids:
  google_place_id: ChIJgwVAszAqcw0R0TkPQ62h-Lo
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 41 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Marisquería El Ancla, Av. Carmen Sevilla, s/n, 29670 Marbella, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4701216,-4.990124499999999); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4701216%2C-4.990124499999999&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 41 min, 40.7 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: medium
  children: medium
  young_adults: high
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
  schedule: Restaurant 13:00-23:00 in summer (closed Monday except public holidays) and in winter (no closing day stated); own contact page, undated (page last modified 2021), read 2026-11-08.
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own carta PDF (Last-Modified August 2022): 19 portion-priced meat, tuna, fish, pasta and rice dishes 18-45 € (median 25 €; per-kg fish and shellfish left out); no drink prices in the carta, so main plus one drink is about 27 € or more, inside 20-50 €. Bread 2 € extra. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-05'
links:
  official_website: https://www.elanclarestaurante.com/
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34952787496
related_places:
- playa-de-san-pedro-alcantara
description_short: 'El Ancla: seafood restaurant on the seafront at San Pedro de Alcántara.'
description_long: El Ancla is a seafood restaurant that describes itself as 'located in a privileged spot on the shore of the Mediterranean' at San Pedro de Alcántara, with a saltwater pool and hammock service (own website). The contact page gives restaurant hours of 13:00-23:00, with Monday closed in summer except on public holidays; the page is undated, so check before going. Bookings by phone only (952 787 496 or 952 789 328).
seo_title: Marisquería El Ancla (San Pedro), Marbella | CalleMilano
seo_description: 'Marisquería El Ancla (San Pedro) (Marbella): food, opening hours and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'Marisquería El Ancla' at Av. Carmen Sevilla, s/n, 29670 Marbella, Málaga, España (36.4701216,-4.990124499999999), business status OPERATIONAL, primary type seafood_restaurant; about 443 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=13472696050805324241
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/one-hour-beach-restaurants-intake-2026-11-02.md, row rE03).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 41 min by car (40.7 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4701216%2C-4.990124499999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long, visit_information, food_available
  claim: 'Own site description: ''Ubicado en un lugar privilegiado a orillas del Mar Mediterráneo'' (page meta description).'
  source_url: https://www.elanclarestaurante.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant fact check 2026-11-02)
  confidence: medium
  notes: Own website read with Firecrawl (direct quotes) on 2026-11-02. Only the page description was readable.
- field: cost_level
  claim: '"€€ - €€€"'
  source_url: https://www.tripadvisor.es/Restaurant_Review-g652103-d2521008-Reviews-El_Ancla_Restaurante-San_Pedro_de_Alcantara_Marbella_Costa_del_Sol_Province_of_Ma.html
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: low
  notes: Tripadvisor price marking only (search excerpt); no ratings or reviews recorded. Own-site prices preferred when available. Listing is titled 'EL ANCLA RESTAURANTE, San Pedro de Alcántara'. Key says 'Marisquería El Ancla San Pedro Marbella'. Matched on name and locality. Name variant to confirm.
- field: cost_level
  claim: '"49 Filetes de lomo a la plancha 18€" ; "50 San Jacobo 19€" ; "51 Rabo de toro 24€" ; "52 Solomillo de ternera, plancha o a la pimienta 32€" ; "55 Lomo de atún encebollado 25€" ; "56 Lomo de atún a la plancha 25€" ; "57 Huevo roto con atún 25€" ; "58 Tataki de atún con salsa nikkey 25€" ; "38 Rosada frita con patatas 18€" ; "39 Merluza a la plancha o a la romana 23€" ; "40 Brocheta de rape 28€" ; "41 Rape frito o a la plancha 28€" ; "42 Salmón a la plancha 28€" ; "73 Raviolis rellenos de setas con salsa de trufa 26€" ; "74 Lingüini con almejas 29€" ; "75 Lingüini con carabineros 45€" ; "35 Caldoso de marisco (mínimo 2 personas) (p/p) 25€" ; "36 Paella de pollo y verduras (mínimo 2 personas) (p/p) 25€" ; "Paella negra de gambas y calamar (mínimo 2 personas) (p/p) 28€" ; "76 Nuggets de pollo con patatas fritas 13€" ; "Servicio de pan 2€ / 10% IVA incluido"'
  source_url: https://www.elanclarestaurante.com/wp-content/uploads/2021/03/CartaESP_SP.pdf
  source_type: official_venue
  checked_at: '2026-11-05'
  checked_by: Claude (main session)
  confidence: medium
  notes: 'Method: pdf (pdftotext), linked as ''CARTA EN PDF'' from the home page. Server Last-Modified 8 Aug 2022, so prices may have risen; the band would stay €€ unless they rose by about 100 %. Children''s dishes (PLATOS INFANTILES 13-18 €) not counted. The linked POOL BAR MENU PDF has no drink prices either.'
- field: visit_information.schedule
  claim: '"HORARIO DE VERANO RESTAURANTE 13:00 a 23:00 Lunes cerrado (excepto festivos)" ; "HORARIO DE INVIERNO 13:00h a 23.00h"'
  source_url: https://www.elanclarestaurante.com/contacto/
  source_type: official_venue
  checked_at: '2026-11-08'
  checked_by: source-reader agent; spot-checked by Claude (main session)
  confidence: medium
  notes: 'Method: curl. Page schema dateModified 2021-07-20, so the hours may be old. The winter block names no closing day.'
- field: links.contact
  claim: '"TELÉFONOS 952 787 496 / 952 789 328" ; "No admitimos reservas por email , las reservas deben realizarse únicamente por teléfono, gracias."'
  source_url: https://www.elanclarestaurante.com/contacto/
  source_type: official_venue
  checked_at: '2026-11-08'
  checked_by: source-reader agent; spot-checked by Claude (main session)
  confidence: medium
  notes: 'Method: curl. Other numbers on the page are for the pool/hammocks and a shop.'
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults high, seniors high; energy_level Low. Owner note (Danish): ''Eksklusiv, hyggelig og romantisk fiskerestaurant''.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
review_issues:
- code: menu_possibly_outdated
  severity: info
  fields:
  - cost_level
  description: The own carta PDF was last modified in August 2022; prices on site may be higher. The band (€€) is unlikely to change.
  retryable: true
  owner: fact_check
- code: facts_partly_checked
  severity: warning
  fields:
  - booking_required
  description: 'Own website checked 2026-11-02 and 2026-11-08 (prices, hours, phone). Still open: booking_required. Hours page is undated; check before publishing.'
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
