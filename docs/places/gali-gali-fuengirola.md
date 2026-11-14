---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-GALI-GALI-FUENGIROLA-001
slug: gali-gali-fuengirola
name: Gali Gali Beach Club
category: Restaurants
tags:
- Beach
- Restaurant
- Full day
- Premium
coordinates:
  latitude: 36.5323365
  longitude: -4.6239951
  purpose: venue
  label: Restaurante Chiringuito Gali Gali, frente Hotel Occidental (Las Pirámides, P.º Marítimo Rey de España, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJYSu88enjcg0Rn30b7Gx25v0, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=18295440746428988831
external_ids:
  google_place_id: ChIJYSu88enjcg0Rn30b7Gx25v0
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 12 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante Chiringuito Gali Gali, frente Hotel Occidental (Las Pirámides, P.º Marítimo Rey de España, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5323365,-4.6239951); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5323365%2C-4.6239951&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 12 min, 5.6 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: high
  children: high
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
  schedule: Monday to Saturday 12:00-24:00 (kitchen 12:00-23:00); Sunday 12:00-19:00 (kitchen 12:00-18:00); open every day depending on weather conditions (own website; weather-dependent, not a seasonal timetable)
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own carta: quoted mains 14,00, 17,50 and 20,00 € (median 17,50 €); drink prices not on the page, so main plus one drink is about 20 € (borderline € / €€). Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-02'
links:
  official_website: http://galigali.es/
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34682199629
related_places: []
description_short: 'Gali Gali: beachfront chiringuito on the Paseo Maritimo of Fuengirola, open daily, weather permitting (own website).'
description_long: 'Gali Gali describes itself on its own website as a chiringuito on the Paseo Maritimo Rey de Espana in Fuengirola, with the line "Quiero mi mesa junto al mar". It is open every day depending on weather conditions: Monday to Saturday 12:00-24:00 (kitchen 12:00-23:00) and Sunday 12:00-19:00 (kitchen 12:00-18:00). The carta shows dishes such as grilled sole (17.50 EUR), grilled Iberian pork (20.00 EUR) and spaghetti bolognese (14.00 EUR). The page offers table or sunbed reservation, but does not state whether booking is required. A children''s menu is not stated.'
seo_title: Gali Gali Beach Club, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Gali Gali Beach Club (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Restaurante Chiringuito Gali Gali' at frente Hotel Occidental (Las Pirámides, P.º Marítimo Rey de España, 29640 Fuengirola, Málaga, España (36.5323365,-4.6239951), status OPERATIONAL, type restaurant.
  source_url: https://maps.google.com/?cid=18295440746428988831
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. Owner selected directory lead R-0209 on 2026-11-02 (checklist https://claude.ai/artifact/VCrXrv5vKsUhruvVk6R9ZT).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 12 min by car (5.6 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5323365%2C-4.6239951&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule
  claim: '"Lunes a Sábado de 12:00-24:00, cocina de 12:00-23:00"; "Domingo  12:00-19:00, cocina de 12:00-18:00"; "Abierto todos los días (según condiciones meteorológicas)"'
  source_url: https://galigali.es/nuestra-carta
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: high
  notes: Own carta page read via curl. Seasonality not stated.
- field: cost_level (menu prices)
  claim: '"Lenguado a la plancha con patatas baby y tomates cherry" "17.50€"; "Pluma ibérica a la plancha con ensalada o patatas" "20,00€"; "Espaguetis boloñesa" "14.00€"'
  source_url: https://galigali.es/nuestra-carta
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: high
  notes: Dish and price were on separate lines. No drink prices. Price band left to orchestrator.
- field: links.contact; address; booking
  claim: '"Teléfono: 682 199 629"; "Dirección: Paseo Marítimo Rey de España, Fuengirola"; "Quiero mi mesa junto al mar"'
  source_url: https://galigali.es/nuestra-carta
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: high
  notes: Page has 'Reserva fácil, sin complicaciones.' and 'Reservar Mesa o Hamaca' but no statement that booking is required. The carta lists chicken burger and fingers under 'Pasta' with no kids-menu label; not recorded as a kids menu.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children high, children high, young_adults high, seniors high; energy_level Low. Owner note (Danish): ''Strandstole. Gode cocktails. Kvindeejet! hunde velkomne''.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Beach, Restaurant, Full day, Premium."
  source_url: https://claude.ai/artifact/DZv9cLLQ1BEcYs3NeewdEF
  source_type: secondary
  checked_at: '2026-11-11'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-11
  confidence: medium
  notes: Owner's own judgment on the tag checklist on 2026-11-11 (previous tags were estimates from import); not independently verified. source_type secondary is the nearest schema value.
- field: visit_information.schedule; cost_level
  claim: "\"Lunes a Sábado de 12:00-24:00, cocina de 12:00-23:00\"; \"Domingo  12:00-19:00, cocina de 12:00-18:00\"; \"Teléfono: 682 199 629\"; a dish price \"17.50€\""
  source_url: https://galigali.es/nuestra-carta
  source_type: official_venue
  checked_at: '2026-11-11'
  checked_by: Claude (main session); own site fetched with tools/intake.py fetch and Tavily extract
  confidence: high
  notes: "Page read again on 2026-11-11 with tools/intake.py fetch; hours, phone and prices unchanged from the 2026-11 reading. Drink prices, kids menu and booking requirement are not stated."
review_issues: []
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: null
next_review_at: 2027-02-14
review_decision: null
redirects: []
---
