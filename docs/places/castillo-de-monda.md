---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-CASTILLO-DE-MONDA-001
slug: castillo-de-monda
name: Hotel-Restaurante Castillo de Monda
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.6307591
  longitude: -4.835406
  purpose: venue
  label: Hotel - Restaurante Castillo De Monda, C. Castillo, s/n, 29110 Monda, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJO0OZS5jbcg0Rosmsqojo4SE, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=2441488146688166306
external_ids:
  google_place_id: ChIJO0OZS5jbcg0Rosmsqojo4SE
municipality: Monda
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 35 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Hotel - Restaurante Castillo De Monda, C. Castillo, s/n, 29110 Monda, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.6307591,-4.835406); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6307591%2C-4.835406&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 35 min, 29.5 km. One predicted sample.'
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
  availability: Private hotel car park (not guarded, security cameras) and free parking on the side of the road up to the hotel; the private car park may get busy in summer.
  location_type: onsite
  cost: Roadside parking free; private car park cost not stated.
  restrictions: 'The access road is steep (own site: drive up in first gear); the route through the village is narrow and not recommended for large cars.'
  walk_distance: unknown
  source: https://castillodemonda.com/contact/
  checked_at: '2026-11-14'
transport_options: []
booking_required: unknown
dog_friendly: unknown
toilets_available: unknown
food_available: 'yes'
cost_level: €€
visit_information:
  schedule: 'Restaurant Albacar open daily: breakfast 8:30-10:30, lunch 13:00-16:00, dinner 19:00-22:00. Bar Albacar open daily 9:00-23:00. (Own site, contact page, read 2026-11-14; not stated as seasonal.)'
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own menu (Restaurant Albacar): charcoal-grill mains 26-36 EUR (median 36 EUR); wine by the glass from 4.50 EUR. Median main plus one drink is about 40-45 EUR, inside 20-50 EUR.'
  cost_checked_at: '2026-11-14'
links:
  official_website: http://www.castillodemonda.com/
  booking: null
  visitor_information: https://castillodemonda.com/contact/
  transport: null
  contact: tel:+34952459836
related_places:
- id: ES-AND-MAL-MONDA-001
  relationship: nearby
  note: Castle hotel above the village.
description_short: Albacar, the restaurant on the 6th floor of the Castillo de Monda hotel above the village of Monda, with countryside views; about 35 min by car from Casa de la Familia.
description_long: 'Restaurant Albacar is on the 6th floor of the Castillo de Monda hotel, above the white village of Monda; its own site describes views over the hills and villages below. About 35 minutes by car from Casa de la Familia (Google route check). The own site gives daily opening times for breakfast (8:30-10:30), lunch (13:00-16:00) and dinner (19:00-22:00), and Bar Albacar, with light meals and a terrace, is open daily 9:00-23:00. Charcoal-grill mains on the own menu cost 26-36 EUR. Tables can be booked through the own site or reception (+34 952 45 98 36). The road up to the castle is steep; the own site advises first gear and warns that the route through the village is too narrow for large cars. There is a private car park and free parking along the access road. Owner''s note (2026-11-02): the hotel is worth the trip for its restaurant; its other facilities are for hotel guests only. The own site does not state a rule for non-resident diners, so check when booking.'
seo_title: Hotel-Restaurante Castillo de Monda, Monda | CalleMilano draft record
seo_description: 'Draft record for Hotel-Restaurante Castillo de Monda (Monda): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Hotel - Restaurante Castillo De Monda' at C. Castillo, s/n, 29110 Monda, Málaga, España (36.6307591,-4.835406), status OPERATIONAL, type hotel.
  source_url: https://maps.google.com/?cid=2441488146688166306
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner decision 2026-11-02: the hotel is not a standalone excursion; it is visited for its restaurant, and its other facilities are for hotel guests only. Source of the lead: owner''s ''inspiration'' entry on callemilano.dk.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 35 min by car (29.5 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6307591%2C-4.835406&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long (owner knowledge), category
  claim: 'Owner 2026-11-02: ''Hotellerne Almagruz, Castillo de Monda og Molino del Santo skal ikke være selvstændige udflugtsmål - de besøges for restauranterne og faciliteterne som ikke kan tilgås uden at være gæst''. Site entry (inspiration): "Historisk slot ombygget til hotel og restaurant. Vejen op er stejl, men udsigten er turen værd.\n\nFamilie-tip: Kombinér med Mijas eller Marbella.\n\nKøretid fra huset: ca. 45 min."'
  source_url: https://callemilano.dk/
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: medium
  notes: Owner instruction in chat plus the owner's inspiration entry on callemilano.dk (Lovable table recommendations). Drive time in the site text is the owner's estimate; the record uses the Routes API figure.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults high, seniors high; energy_level Medium.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: description_long (restaurant)
  claim: '"Perched on the 6th floor of Castillo de Monda, Albacar Restaurante offers an extraordinary dining experience high above the Andalusian countryside."; "BOOK A TABLE"; "Bar Albacar ... light meals and snacks"'
  source_url: https://castillodemonda.com/restaurant-near-marbella/
  source_type: official_venue
  checked_at: '2026-11-13'
  checked_by: Claude (main session, Claude in Chrome)
  confidence: medium
  notes: Own site read in Claude in Chrome on 2026-11-13. It describes the Albacar restaurant (6th floor), Bar Albacar and a rooftop garden and offers table booking, but gives no opening hours, prices or rule for diners who are not hotel guests. The menu page linked from it was the wine list.
- field: visit_information.schedule
  claim: '"RESTAURANT ALBACAR - Open Daily" "Breakfast | 8:30 - 10:30" "Lunch | 13:00 - 16:00" "Dinner | 19:00 - 22:00" "BAR ALBACAR - Open Daily" "9:00 - 23:00"'
  source_url: https://castillodemonda.com/contact/
  source_type: official_venue
  checked_at: '2026-11-14'
  checked_by: Claude (main session), read in Claude in Chrome
  confidence: high
  notes: null
- field: parking
  claim: '"There is plenty of parking around the castle." "In the summer our private parking may get busy, but you can park free of charge on the side of the road that leads up to the hotel." "The private Castle parking area is not guarded but we do have security cameras in this area."'
  source_url: https://castillodemonda.com/contact/
  source_type: official_venue
  checked_at: '2026-11-14'
  checked_by: Claude (main session), read in Claude in Chrome
  confidence: high
  notes: null
- field: parking.restrictions
  claim: '"Drive in first gear as the way up is a little steep but wide enough to arrive safe" and "We don''t recommend you take this route with large cars".'
  source_url: https://castillodemonda.com/contact/
  source_type: official_venue
  checked_at: '2026-11-14'
  checked_by: Claude (main session), read in Claude in Chrome
  confidence: high
  notes: null
- field: links.contact
  claim: Reception "+34 952 45 98 36", Calle Castillo 29110 Monda.
  source_url: https://castillodemonda.com/contact/
  source_type: official_venue
  checked_at: '2026-11-14'
  checked_by: Claude (main session), read in Claude in Chrome
  confidence: high
  notes: null
- field: cost_level, visit_information.cost_basis
  claim: 'Carbón & Leña: "Entrecôte madurado ... 36", "Solomillo de ternera ... 36", "Lomo alto cuberol ... 36", "Secreto ibérico ... 30", "Picantón piri-piri ... 26"; wine by the glass from 4.50.'
  source_url: https://castillodemonda.com/menus/
  source_type: official_venue
  checked_at: '2026-11-14'
  checked_by: Claude (main session), read in Claude in Chrome
  confidence: high
  notes: 'Band rule: median main plus one drink, about 40-45 EUR = EUR EUR.'
review_issues:
- code: guest_only_facilities
  severity: info
  fields:
  - description_long
  - accessibility
  description: Hotel facilities other than the restaurant are for guests only (owner). The own site markets Albacar as a "Restaurant Near Marbella" with a public "Book a table" form, but states no rule for non-resident diners (read 2026-11-14). Check when booking.
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-14'
last_verified: '2026-11-14'
last_reviewed_at: null
next_review_at: '2027-02-14'
review_decision: null
redirects: []
---
