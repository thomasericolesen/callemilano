---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-SOLLO-FUENGIROLA-001
slug: sollo-fuengirola
name: Sollo Restaurante
category: Restaurants
tags:
- Restaurant
- Rainy day
- Half day
- Premium
coordinates:
  latitude: 36.5799411
  longitude: -4.5953257
  purpose: venue
  label: Sollo, Urbanización Reserva del Higuerón, Av. del Higuerón, 48, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJezXuFzx2LxURgLw_P3n5zLo, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=13460407685451070592
external_ids:
  google_place_id: ChIJezXuFzx2LxURgLw_P3n5zLo
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 17 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Sollo, Urbanización Reserva del Higuerón, Av. del Higuerón, 48, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5799411,-4.5953257); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5799411%2C-4.5953257&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 17 min, 11.7 km. One predicted sample.'
age_groups:
- Young adults
- Seniors
family_score:
  small_children: unknown
  children: unknown
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
cost_level: €€€€
visit_information:
  schedule: null
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own site: tasting menu Menú degustación "Caminho 2026" 180 € per person (the menu page shows only this menu, plus separate pages for pairings and caviar). No à la carte prices read.'
  cost_checked_at: '2026-11-11'
links:
  official_website: https://www.sollo.es/es/
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34692425385
related_places: []
description_short: 'Sollo: restaurant on Av. del Higuerón, Fuengirola; own website has a menu page and online booking.'
description_long: Sollo's own website gives its address as Av. del Higuerón, 48, 29640 Fuengirola, and has a "RESERVA AHORA" booking button and a phone number (+34 692 425 385). The menu page we read showed no dish prices, opening hours or children's information, so these are not confirmed.
seo_title: Sollo Restaurante, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Sollo Restaurante (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Sollo' at Urbanización Reserva del Higuerón, Av. del Higuerón, 48, 29640 Fuengirola, Málaga, España (36.5799411,-4.5953257), status OPERATIONAL, type fine_dining_restaurant.
  source_url: https://maps.google.com/?cid=13460407685451070592
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. Owner selected directory lead R-0304 on 2026-11-02 (checklist https://claude.ai/artifact/VCrXrv5vKsUhruvVk6R9ZT).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 17 min by car (11.7 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5799411%2C-4.5953257&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: links.contact; address; booking
  claim: '"+34 692 425 385"; "RESERVA AHORA"; "Av. del Higuerón, 48. 29640 Fuengirola"; "Málaga. España."'
  source_url: https://www.sollo.es/es/menu-sollo/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: medium
  notes: Menu page navigation only; no prices, hours or kids info in fetched text. Booking button does not state whether booking is required.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children unknown, children unknown, young_adults high, seniors high; energy_level Low. Owner note (Danish): ''Gourmet restaurant dyr''.'
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
- field: cost_level; links.contact
  claim: "\"Menú degustación \\\"Caminho 2026\\\"\"; \"180€\"; \"+34 692 425 385\"; \"Av. del Higuerón, 48. 29640 Fuengirola\""
  source_url: https://www.sollo.es/es/menu-sollo/menu-caminho/
  source_type: official_venue
  checked_at: '2026-11-11'
  checked_by: Claude (main session); own site fetched with tools/intake.py fetch and Tavily extract
  confidence: high
  notes: "Own site (Tavily extract). One tasting menu at 180 € per person; the menu's courses use caviar and sturgeon. Opening hours, kids facilities and drink or pairing prices were not read."
review_issues: []
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
