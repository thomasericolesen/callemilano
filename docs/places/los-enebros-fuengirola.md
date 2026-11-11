---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-LOS-ENEBROS-FUENGIROLA-001
slug: los-enebros-fuengirola
name: Restaurante Los Enebros
category: Restaurants
tags:
- Restaurant
- Half day
- Premium
coordinates:
  latitude: 36.5530316
  longitude: -4.6162512
  purpose: venue
  label: Restaurante Los Enebros, Av. Nuestro Padre Jesús Cautivo, 19, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJJ3ce1U_icg0RofPFwPmoxl0, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=6757274081550529441
external_ids:
  google_place_id: ChIJJ3ce1U_icg0RofPFwPmoxl0
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 15 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante Los Enebros, Av. Nuestro Padre Jesús Cautivo, 19, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5530316,-4.6162512); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5530316%2C-4.6162512&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 15 min, 6.6 km. One predicted sample.'
age_groups:
- Young adults
- Seniors
family_score:
  small_children: low
  children: low
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
  cost_basis: 'Own carta: quoted mains 15,00, 19,00 and 32,00 € (median 19,00 €); drink prices not on the page, so main plus one drink is just over 20 €. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-02'
links:
  official_website: https://restaurantelosenebros.com/
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34952665550
related_places: []
description_short: 'Restaurante Los Enebros: Mediterranean restaurant in Los Boliches with a food menu on its own website; closed Mondays.'
description_long: Restaurante Los Enebros is in Los Boliches, Fuengirola, about 15 minutes by car from Casa de la Familia (Google route check). According to its own website, it is closed on Mondays and open in the evening on Tuesday (19:00-22:30), with lunch and dinner on Saturday and Sunday. The website's carta lists main dishes such as Black Angus entrecote (32.00 EUR), grilled fresh salmon loin (19.00 EUR) and spaghetti bolognese (15.00 EUR). The website does not say anything about a children's menu, high chairs or a play area, so child facilities are not confirmed.
seo_title: Restaurante Los Enebros, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Restaurante Los Enebros (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Restaurante Los Enebros' at Av. Nuestro Padre Jesús Cautivo, 19, 29640 Fuengirola, Málaga, España (36.5530316,-4.6162512), status OPERATIONAL, type mediterranean_restaurant.
  source_url: https://maps.google.com/?cid=6757274081550529441
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. Owner selected directory lead R-0101 on 2026-11-02 (checklist https://claude.ai/artifact/VCrXrv5vKsUhruvVk6R9ZT).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 15 min by car (6.6 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5530316%2C-4.6162512&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information (hours, partial); description_long
  claim: '"Martes: 19:00 – 22:30"; "Sábado: 13:00 – 15:30 / 19:00 – 22:30"; "Domingo: 13:00 – 15:30 / 19:00 – 22:00"; "Lunes: Cerrado"'
  source_url: https://www.restaurantelosenebros.com/carta/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: medium
  notes: Only four days quoted; Wednesday to Friday not captured, so no schedule set.
- field: cost_level (menu prices); description_long
  claim: '"Entrecot de Black Angus americano 32.00 €"; "Lomo de salmón fresco a la plancha 19.00 €"; "Spaghetti con salsa boloñesa 15.00 €"'
  source_url: https://www.restaurantelosenebros.com/carta/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: medium
  notes: Carta page has food and dessert prices only, no drinks. Price band left to orchestrator.
- field: links.contact; address
  claim: '"952 665 550"; "Avenida Nuestro Padre Jesús Cautivo, 19"'
  source_url: https://www.restaurantelosenebros.com/carta/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: medium
  notes: Phone printed under 'Teléfono'. The 'Reservas' item is only a navigation link; no booking statement.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children low, children low, young_adults medium, seniors medium; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Restaurant, Half day, Premium."
  source_url: https://claude.ai/artifact/DZv9cLLQ1BEcYs3NeewdEF
  source_type: secondary
  checked_at: '2026-11-11'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-11
  confidence: medium
  notes: Owner's own judgment on the tag checklist on 2026-11-11 (previous tags were estimates from import); not independently verified. source_type secondary is the nearest schema value.
review_issues:
- code: facts_not_checked
  severity: warning
  fields:
  - description_long
  - visit_information
  - cost_level
  - accessibility
  - parking
  description: Created from Google Places identity and a route check only; needs official or own sources.
  retryable: true
  owner: fact_check
- code: facts_partly_checked
  severity: warning
  fields:
  - visit_information
  - cost_level
  - booking_required
  - accessibility
  - parking
  description: 'Own carta read: partial hours (Wed-Fri missing), main-dish prices, phone. No drink prices, no kids facilities, no booking statement.'
  retryable: true
  owner: fact_check
- code: cost_level_borderline
  severity: info
  fields:
  - cost_level
  description: Median quoted main 19 € plus a drink is just over 20 €; drink prices are not on the page, so the band is €€ at its lower edge.
  retryable: true
  owner: human_editor
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
