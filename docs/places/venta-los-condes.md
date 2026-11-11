---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-VENTA-LOS-CONDES-001
slug: venta-los-condes
name: Venta los Condes
category: Restaurants
tags:
- Restaurant
- Rainy day
- Half day
- Premium
coordinates:
  latitude: 36.6027124
  longitude: -4.674296399999999
  purpose: venue
  label: Venta los Condes, Lugar Sierra Blanca, 9, 29650 Mijas, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJgSUqt-Ljcg0Rp3ZGau3rOiI, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=2466543150861547175
external_ids:
  google_place_id: ChIJgSUqt-Ljcg0Rp3ZGau3rOiI
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 25 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Venta los Condes, Lugar Sierra Blanca, 9, 29650 Mijas, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.6027124,-4.674296399999999); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6027124%2C-4.674296399999999&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 25 min, 15.1 km. One predicted sample.'
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
energy_level: Medium
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
  schedule: Tuesday-Sunday 13:00-22:00, kitchen 13:00-16:00 and 18:00-21:00; closed Monday (own website, read 2026-11-08).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own menu PDF (dated 31.03.26): grilled mains 21-59 € (median about 31 €: burger 21, ribs 28, pork fillet 28, pork belly 28, duck 30, entrecôte 400 g 32, lamb 33, lamb shanks 33, fillet steak 34, rib eye 500 g 59); kids'' menu 9 € incl. a soft drink and a scoop of ice cream. Main plus one drink is well inside 20-50 €. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-08'
links:
  official_website: https://ventaloscondes.com/
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34951744179
related_places: []
description_short: 'Venta los Condes: a grill restaurant in the hills above Mijas, about 25 min by car from Casa de la Familia. Partly fact-checked.'
description_long: 'Venta los Condes is a grill restaurant in the hills above Mijas (Lugar Sierra Blanca 9), open Tuesday to Sunday 13:00-22:00 with the kitchen open 13:00-16:00 and 18:00-21:00, closed on Monday (own website). Grilled meat mains cost about 21-59 €, and there is a kids'' menu at 9 € including a drink and ice cream. Book by phone (+34 951 744 179) or WhatsApp (+34 633 329 808). About 25 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Owner''s recommendation (callemilano.dk): Tasty, always beautifully presented food; meat is cooked over an open grill. A little expensive, but good.'
seo_title: Venta los Condes, Mijas | CalleMilano draft record
seo_description: 'Draft record for Venta los Condes (Mijas): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Venta los Condes' at Lugar Sierra Blanca, 9, 29650 Mijas, Málaga, España (36.6027124,-4.674296399999999), status OPERATIONAL, type restaurant.
  source_url: https://maps.google.com/?cid=2466543150861547175
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. From the owner's recommendations on callemilano.dk (Lovable app 'Vores Spanske Hjem', table recommendations), read 2026-11-02.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 25 min by car (15.1 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6027124%2C-4.674296399999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long (owner knowledge)
  claim: Lækker mad, altid smukt anrettet. Kød bliver tilberedt over åben grill. Værten bærer en læder kilt - men er ikke skotte. Lidt dyrt, men godt
  source_url: https://callemilano.dk/
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: medium
  notes: 'Owner''s own recommendation (kind ''anbefaling'') on callemilano.dk, read from the Lovable app database 2026-11-02; site tags: aftensmad, steak. Personal experience, not independently verified.'
- field: visit_information.schedule; links.contact; address; booking
  claim: '"MONDAY" "CLOSED" ; "TUESDAY - SUNDAY" "13:00 - 22:00" ; "kitchen" "13:00 - 16:00" "18:00 - 21:00" ; "Lugar Sierra Blanca, 9, Mijas, Málaga 29650 Mijas, Spain." ; "+34 951 744 179" ; "+34 633 329 808" ; "CALL OR TEXT US ON WHATSAPP TO BOOK YOUR TABLE TODAY!"'
  source_url: https://ventaloscondes.com/
  source_type: official_venue
  checked_at: '2026-11-08'
  checked_by: source-reader agent
  confidence: medium
  notes: 'Method: curl.'
- field: cost_level; children
  claim: '"Char Grilled Entrecôte (400gr) With Natural Jus & Fries 32 €" ; "Jimmy’s Famous BBQ Ribs with BBQ or Asian Sauce & French Fries 28 €" ; "Grilled Duck Breast with a Sweet Malaga Wine Sauce, Vegetables & Gratin Potatoes 30€" ; "Char Grilled Fillet Steak (300gr) with Fried Onion, Natural Jus & Fries 34 €" ; "Slow Braised Lamb Shanks ... 33 €" ; "Char Grilled Iberian Pork Fillet ... 28 €" ; "Char Grilled Lamb Chops ... 33 €" ; "Rib Eye Steak (500gr) For One or Two People ... 59 €" ; "Slow Coal Roasted Pork Belly ... 28 €" ; "Burger With Smoked Bacon, Cheese, The Secret “Los Condes” Sauce & Fries 21 €" ; "MENÚ INFANTIL 9 € KIDS MENU" ; "Bebida y Bola de Helado a Elegir A Soft Drink & a Ball Of Ice Cream of Choice"'
  source_url: https://ventaloscondes.com/wp-content/uploads/2026/04/Venta-Los-Condes-Menu.pdf
  source_type: official_venue
  checked_at: '2026-11-08'
  checked_by: source-reader agent (Firecrawl)
  confidence: low
  notes: Image PDF (no text layer); read via Firecrawl query mode, not checked character by character. 10 of the menu's mains quoted. Kids' menu from the separate kids' menu PDF on the same site. Band €€ holds for any plausible reading.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults high, seniors high; energy_level Medium.'
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
review_issues:
- code: facts_partly_checked
  severity: warning
  fields:
  - accessibility
  - seasonality
  - parking
  description: 'Own website and menus read 2026-11-08. Still open: accessibility, season, parking, high chairs; menu prices read by machine from an image PDF.'
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
