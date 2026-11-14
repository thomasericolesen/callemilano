---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-MIAS-PIZZORANTE-FUENGIROLA-001
slug: mias-pizzorante-fuengirola
name: Mia's Pizzorante
category: Restaurants
tags:
- Restaurant
- Rainy day
- Half day
- Free
coordinates:
  latitude: 36.5680051
  longitude: -4.5954396
  purpose: venue
  label: Mia's Pizzorante Gourmet, Local 2, P.º Marítimo Rey de España, 141, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJDzV4DgPjcg0Rzr0dMZGZo0k, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=5306253634845916622
external_ids:
  google_place_id: ChIJDzV4DgPjcg0Rzr0dMZGZo0k
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 17 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Mia's Pizzorante Gourmet, Local 2, P.º Marítimo Rey de España, 141, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5680051,-4.5954396); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5680051%2C-4.5954396&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 17 min, 8.5 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: high
  children: high
  young_adults: high
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
  cost_basis: 'Own carta: quoted mains 18,00, 18,50 and 21,00 € (median 18,50 €) plus wine glass 4,50 € gives about 23 € per adult. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-02'
links:
  official_website: https://miaspizzorante.com/
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34951903240
related_places: []
description_short: 'Mia''s Pizzorante: Italian restaurant on Playa de Carvajal, Fuengirola, facing the Mediterranean (own website).'
description_long: Mia's Pizzorante says on its own website that it is at Playa de Carvajal, Fuengirola, facing the Mediterranean. The online carta lists pasta dishes such as pappardelle with beef fillet and porcini (21,00 EUR), garganelli alla Mia's (18,00 EUR) and tagliolini alla Norcina (18,50 EUR), and take-away is offered. The site has a button to reserve a table online. Opening hours, a children's menu and a street address were not found on the page.
seo_title: Mia's Pizzorante, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Mia''s Pizzorante (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Mia's Pizzorante Gourmet' at Local 2, P.º Marítimo Rey de España, 141, 29640 Fuengirola, Málaga, España (36.5680051,-4.5954396), status OPERATIONAL, type italian_restaurant.
  source_url: https://maps.google.com/?cid=5306253634845916622
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. Owner selected directory lead R-0303 on 2026-11-02 (checklist https://claude.ai/artifact/VCrXrv5vKsUhruvVk6R9ZT).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 17 min by car (8.5 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5680051%2C-4.5954396&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: cost_level (menu prices); description_long
  claim: '"PAPPARDELLE AL FILLETO DI MANZO CON PORCINI" "21,00 €"; "GARGANELLI ALLA MIA''S" "18,00 €"; "TAGLIOLINI ALLA NORCINA" "18,50 €"; "PINOT GRIGIO BLUSH I.G.T VAJA" "4,50 € / 21,90 €"; "Reserva aquí tu mesa"; "Estamos en Playa de Carvajal, Fuengirola , frente al Mediterráneo."'
  source_url: https://miaspizzorante.com/nuestra-carta/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: high
  notes: Own carta page read via curl. Wine prices have no printed glass/bottle label. No phone number, hours or street address. Booking button only; no statement that booking is required. Price band left to orchestrator.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children high, children high, young_adults high, seniors medium; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Restaurant, Rainy day, Half day, Free."
  source_url: https://claude.ai/artifact/DZv9cLLQ1BEcYs3NeewdEF
  source_type: secondary
  checked_at: '2026-11-11'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-11
  confidence: medium
  notes: Owner's own judgment on the tag checklist on 2026-11-11 (previous tags were estimates from import); not independently verified. source_type secondary is the nearest schema value.
- field: links.contact; booking
  claim: "\"+34 951 90 32 40\"; \"reservation@miaspizzorante.com\"; \"Reserva tu mesa y descubre Mia’s Pizzorante.\""
  source_url: https://miaspizzorante.com/
  source_type: official_venue
  checked_at: '2026-11-11'
  checked_by: Claude (main session); own site fetched with tools/intake.py fetch and Tavily extract
  confidence: high
  notes: "Home and contact pages read on 2026-11-11. Opening hours and a kids menu were not found on the site; the carta page has a take-away section."
review_issues: []
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: null
next_review_at: 2027-02-14
review_decision: null
redirects: []
---
