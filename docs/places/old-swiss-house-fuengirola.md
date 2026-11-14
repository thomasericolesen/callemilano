---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-OLD-SWISS-HOUSE-FUENGIROLA-001
slug: old-swiss-house-fuengirola
name: Old Swiss House
category: Restaurants
tags:
- Restaurant
- Rainy day
- Half day
- Premium
coordinates:
  latitude: 36.5337161
  longitude: -4.624188999999999
  purpose: venue
  label: Restaurante Old Swiss House, C. Marina Nacional, 26, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJM_I01Gzicg0Rm-e40hL_w8M, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=14106398914164352923
external_ids:
  google_place_id: ChIJM_I01Gzicg0Rm-e40hL_w8M
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 13 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante Old Swiss House, C. Marina Nacional, 26, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5337161,-4.624188999999999); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5337161%2C-4.624188999999999&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 13 min, 5.6 km. One predicted sample.'
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
booking_required: true
dog_friendly: unknown
toilets_available: unknown
food_available: 'yes'
cost_level: €€
visit_information:
  schedule: "Tuesday closed. The own website gives conflicting hours for the other days (Wednesday lunch, Sunday); check before visiting, tel. +34 952 472 606 (owner decision 2026-11-11)."
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own website: set menus 27-30 € per person (Chateaubriand menu 30 €); children''s menu 7,50 €. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-02'
links:
  official_website: https://www.oldswisshouse.com/
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34952472606
related_places: []
description_short: 'Old Swiss House: restaurant in Fuengirola with a Superman kids menu; booking in advance by phone advised (own website).'
description_long: 'According to the restaurant''s own website, Old Swiss House is at Calle Marina Nacional 28 in Fuengirola, and it is necessary to book in advance by phone (+34 952 472 606) or the booking form. Opening days: closed on Tuesday, dinner only on Wednesday, lunch and dinner on Monday and Thursday to Sunday. The website offers set menus such as a Chateaubriand menu (30 EUR) and a Steak Tartar menu (27 EUR per person), and a "Superman Menu for Kids" at 7,50 EUR per child.'
seo_title: Old Swiss House, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Old Swiss House (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Restaurante Old Swiss House' at C. Marina Nacional, 26, 29640 Fuengirola, Málaga, España (36.5337161,-4.624188999999999), status OPERATIONAL, type swiss_restaurant.
  source_url: https://maps.google.com/?cid=14106398914164352923
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. Owner selected directory lead R-0210 on 2026-11-02 (checklist https://claude.ai/artifact/VCrXrv5vKsUhruvVk6R9ZT).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 13 min by car (5.6 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5337161%2C-4.624188999999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: booking_required; description_long (menus, kids menu)
  claim: '"It is necessary to book in advance (phone)"; "+34 952 472 606"; "Chateaubriand Menu 30€"; "Steak Tartar Menu" "27€ /per person"; "Superman Menu for Kids" "7,50€/per child"; "C. Marina Nacional, 28, 29640 Fuengirola, Málaga"'
  source_url: https://www.oldswisshouse.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: medium
  notes: Prices shown for the two menus only, not per dish. Page also says '1 HOUR OF FREE PARKING UPON REQUEST FOR CLIENTS DURING LUNCH OR DINNER' (reader note). Page carries a stale holiday-closure line from 2023-24.
- field: visit_information.schedule (conflicting, not set)
  claim: '"Monday\n13:00 - 15:30 | 18:30 – 22:45"; "Tuesday\nCLOSED"; "Wednesday\n13:00 - 17:30 | 18:30 – 22:30"; "Tuesday closed, Wednesday open for dinner only, Monday, Thursday to Sunday lunch and dinner."; "SUNDAYS\nClosed"'
  source_url: https://www.oldswisshouse.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: medium
  notes: Page contradicts itself on Sunday and Wednesday; schedule deliberately not set.
- field: visit_information.schedule; address
  claim: '"OPENING TIMES Tuesday closed, Wednesday open for dinner only, Monday, Thursday to Sunday lunch and dinner." ; "952 47 26 06" ; "C. Marina Nacional, 28, 29640 Fuengirola, Málaga"'
  source_url: https://oldswisshouse.com/en/
  source_type: official_venue
  checked_at: '2026-11-08'
  checked_by: Eric Olesen (screenshot of the own website); recorded by Claude
  confidence: medium
  notes: 'Owner screenshot 2026-11-08 of the ''Opening times'' and contact block. Owner decision: this block is the valid one; it replaces the conflicting hours table (Sunday closed vs open) and confirms house number 28 (Google Places lists 26).'
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults high, seniors high; energy_level Low. Owner note (Danish): ''Klassiske schweizisk restaurant''.'
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
- field: visit_information.schedule (conflict)
  claim: "\"Tuesday closed, Wednesday open for dinner only, Monday, Thursday to Sunday lunch and dinner.\"; \"SUNDAYS\" \"Closed\"; table: \"Wednesday\" \"13:00 - 17:30 | 18:30 – 22:30\""
  source_url: https://oldswisshouse.com/en/
  source_type: official_venue
  checked_at: '2026-11-11'
  checked_by: Claude (main session); own site fetched with tools/intake.py fetch and Tavily extract
  confidence: high
  notes: "The same page contradicts itself: the opening-times sentence says Wednesday is dinner only, the table lists Wednesday lunch (13:00 - 17:30) and Sunday 13:00 – 16:00 | 19:00 – 23:00, and a separate block says Sundays closed. Hours stay unset; the conflict is on the editor list."
- field: visit_information.schedule
  claim: "Editor decision: write \"check before visiting\" and leave the hours unknown; only Tuesday closed is consistent on the own website."
  source_url: https://claude.ai/artifact/C1Lu1WExnpBw8YRw5K1Jrc
  source_type: secondary
  checked_at: '2026-11-11'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-11
  confidence: medium
  notes: "Decision made by the editor on the editor list (first list, 11 Nov 2026); the conflicting source is named in the record. Own judgement, not independently verified."
review_issues: []
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: null
next_review_at: 2027-02-14
review_decision: null
redirects: []
---
