---
schema_version: 1.0.0
status: approved
id: ES-AND-MAL-TASCA-LASKA-MALAGUETA-001
slug: tasca-laska-malagueta
name: Tasca Láska Malagueta
category: Restaurants
tags:
- Restaurant
- Rainy day
- Full day
coordinates:
  latitude: 36.7193155
  longitude: -4.4091223
  purpose: venue
  label: Tasca láska Malagueta, C. Fernando Camino, 15, Málaga-Este, 29016 Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJxbuuQof3cg0R2aBBQ7v6bw4, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=1040325721140076761
external_ids:
  google_place_id: ChIJxbuuQof3cg0R2aBBQ7v6bw4
municipality: Málaga
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 43 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Tasca láska Malagueta, C. Fernando Camino, 15, Málaga-Este, 29016 Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.7193155,-4.4091223); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.7193155%2C-4.4091223&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 43 min, 37.3 km. One predicted sample.'
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
  schedule: Mon, Thu-Sun 12:00-00:00 (kitchen 12:00-23:00); closed Tue-Wed (own site, read 2026-11-02).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own digital menu for the Malagueta branch (tascalaska.es/QR/Malagueta): 17 rice (per person), meat and fish mains 13,00-32,00 € (median 18,00 €) plus the cheapest glass of wine 3,80 € (wine list September 2025) gives about 21,80 € per adult. Bread 1,50 € and olives 0,50 € extra. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-05'
links:
  official_website: https://tascalaska.es/es/tasca-laska-malagueta/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- playa-la-malagueta
description_short: 'Tasca Láska Malagueta: rice dishes and tapas about 150 m from Malagueta beach.'
description_long: Tasca Láska Malagueta serves paellas and rice dishes, creative tapas and wine, at Calle Fernando Camino 15 by the bullring, about 150 m from Malagueta beach and 5 minutes' walk from Muelle Uno (own website). Open Monday and Thursday-Sunday 12:00-00:00, kitchen 12:00-23:00; closed Tuesday and Wednesday. Online booking. The restaurant lists a baby-changing table and short-stay parking around it.
seo_title: Tasca Láska Malagueta, Málaga | CalleMilano
seo_description: 'Tasca Láska Malagueta (Málaga): food, opening hours and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'Tasca láska Malagueta' at C. Fernando Camino, 15, Málaga-Este, 29016 Málaga, España (36.7193155,-4.4091223), business status OPERATIONAL, primary type restaurant; about 272 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=1040325721140076761
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/decisions/one-hour-beach-restaurants-intake-2026-11-02.md, row rA03).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 43 min by car (37.3 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.7193155%2C-4.4091223&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long, visit_information, food_available
  claim: 'Own site: ''a solo 150 metros de la playa de la Malagueta''; Fernando Camino 15, 29016 Málaga; open lunes, jueves, viernes, sábado y domingo 12:00-0:00, martes y miércoles cerrado, cocina 12:00-23:00; reserva online; ''Cambiador para bebés''; parking de corta duración alrededor. Site title: tapas, paellas.'
  source_url: https://tascalaska.es/es/tasca-laska-malagueta/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant fact check 2026-11-02)
  confidence: high
  notes: Own website read with Firecrawl (direct quotes) on 2026-11-02.
- field: cost_level
  claim: '"Precio medio: 24 €"; "€€ - €€€"'
  source_url: https://www.thefork.es/restaurante/tasca-laska-malagueta-r842451
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: low
  notes: 'TheFork price marking only (search excerpt); no ratings or reviews recorded. Own-site prices preferred when available. Two URLs used. The first quote is from the entry URL (thefork.es, search snippet ''Restaurante Tasca Láska Malagueta en Málaga''). The second quote is from a different URL: https://www.tripadvisor.es/Re'
- field: cost_level
  claim: '"Arroz de verduras 13.00€ Precio por persona." ; "Arroz de pollo 16.00€" ; "Arroz de ibéricos 19.00€" ; "Arroz mixto 17.00€" ; "Arroz de mariscos 18.00€" ; "Arroz negro 19.00€" ; "Arroz de costillas glaseadas con shiitake 21.00€" ; "Arroz con pulpo y gambas peladas 21.00€" ; "Arroz meloso con pulpo y gambas 23.00€" ; "Arroz meloso con pulpo, langostinos y bogavante 32.00€" ; "Codillo a baja temperatura con patatas baby 19.00€" ; "Secreto ibérico con patatas fritas y pimientos asados 17.00€" ; "Pechuga de pollo con coleslaw 14.00€" ; "Magret de pato 15.00€" ; "Pulpo flor a la plancha 24.00€" ; "Buchones de rosada con patatas fritas 14.00€" ; "Lubina a la plancha 17.00€"'
  source_url: https://tascalaska.es/QR/Malagueta/web.php?lang=es
  source_type: official_venue
  checked_at: '2026-11-05'
  checked_by: Claude (main session)
  confidence: medium
  notes: 'Method: curl. The PDF menu ''MENU-ES-220926'' linked on the branch page carries the QR link /QR/Avenida and ''Visítanos también en Tasca láska Malagueta'', so it is the other branch''s menu; its main-course prices are the same. Rice dishes are for at least two people. Starters (tiradito 17,00 €, carpaccio 13,00 €) not counted.'
- field: cost_level
  claim: '"COPA 3.8€ 19€ Cortijo la Fuente A.S." ; "COPA 3.8€ 19€ Acappela"'
  source_url: https://tascalaska.es/wp-content/uploads/2025/09/TASKA-LASKA-Vinos-sept-2025.pdf
  source_type: official_venue
  checked_at: '2026-11-05'
  checked_by: Claude (main session)
  confidence: medium
  notes: 'Method: pdf (pdftotext). Wine list September 2025 (Last-Modified 22 Sep 2025), linked from the home page; not stated per branch. Beer and soft-drink prices not found on the site. Column layout: the 3.8 € glass price is printed above the wine name.'
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults medium, seniors medium; energy_level Low. Owner note (Danish): ''Tirsdag og onsdag lukket''.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Restaurant, Rainy day, Full day."
  source_url: https://claude.ai/artifact/DZv9cLLQ1BEcYs3NeewdEF
  source_type: secondary
  checked_at: '2026-11-11'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-11
  confidence: medium
  notes: Owner's own judgment on the tag checklist on 2026-11-11 (previous tags were estimates from import); not independently verified. source_type secondary is the nearest schema value.
review_issues: []
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: '2026-11-11'
next_review_at: '2027-04-11'
review_decision:
  decision: approved
  reviewer: Eric Olesen (editor-of-record)
  date: '2026-11-11'
  notes: "Approved by the owner on 2026-11-11 after his own review of the place on the family-rating checklist (2026-11-10) and the tag checklist (2026-11-11), on top of the agent fact-check. Practical details that are still unknown stay shown as 'check before visiting'."
redirects: []
---
