---
schema_version: 1.0.0
status: approved
id: ES-AND-MAL-SANTA-ANA-DENIS-001
slug: santa-ana-denis
name: Restaurante Santa Ana Denis
category: Restaurants
tags:
- Restaurant
- Beach
coordinates:
  latitude: 36.5908659
  longitude: -4.52638
  purpose: venue
  label: Restaurante Santa Ana Denis, Playa de Santa Ana, local 4, 29630 Benalmádena (Google Places listing)
  source: Google Places API (New) searchText, place ChIJlZTX_GH8cg0RvQde5l7lnfA, read 2026-11-01
  checked_at: '2026-11-01'
google_maps_url: https://maps.google.com/?cid=17338266336200886205
external_ids:
  google_place_id: ChIJlZTX_GH8cg0RvQde5l7lnfA
municipality: Benalmádena
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 27 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante Santa Ana Denis, Playa de Santa Ana, local 4, 29630 Benalmádena
  source: Google Routes API computeRoutes, run 2026-11-01 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5908659,-4.52638); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5908659%2C-4.52638&travelmode=driving
  checked_at: '2026-11-01'
  note: 'Routes API figure: 27 min with predicted Saturday 10:00 traffic (27 min without traffic), 20.1 km via AP-7. One predicted sample, not the Google Maps app''s main figure.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: medium
  children: high
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
  cost_basis: 'Own menu: quoted mains 18,50, 18,50 and 26,00 € (median 18,50 €) plus beer 3,50 € gives about 22 € per adult. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-02'
links:
  official_website: https://www.restaurantesantaanadenis.com/
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34952564382
related_places:
- id: ES-AND-MAL-SANTA-ANA-BENALMADENA-001
  relationship: nearby
  note: Beachfront restaurant on Playa de Santa Ana.
description_short: Beachfront restaurant on Playa de Santa Ana, Benalmádena Costa, serving paellas, seafood and espetos; about 27 minutes by car.
description_long: 'Restaurante Santa Ana Denis is a beachfront restaurant on the Benalmádena Costa promenade at Playa de Santa Ana (local 4). Its own website lists paellas, seafood, grilled meat and fish on the espeto, phone 952 56 43 82, and describes the atmosphere as ideal for families and groups (the venue''s own wording, not an independent assessment). Route check: about 27 minutes from Casa de la Familia (Saturday 10:00, predicted traffic). Opening hours, season, prices, children''s facilities and accessibility are not confirmed. Prices and seasonal opening are not confirmed; check with the restaurant before visiting.'
seo_title: Restaurante Santa Ana Denis, Benalmádena | CalleMilano
seo_description: 'Restaurante Santa Ana Denis (Benalmádena): beach restaurant near Casa de la Familia, with drive time, what is confirmed and what to check before visiting.'
images: []
evidence:
- field: name, municipality, food_available, links
  claim: 'Own website: beachfront restaurant on the Benalmádena Costa promenade at Playa de Santa Ana, local 4; paellas, seafood, grilled meat and fish on the espeto; phone 952 56 43 82; describes itself as ideal for families and groups.'
  source_url: https://www.restaurantesantaanadenis.com/
  source_type: official_venue
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: high
  notes: Own website read on 2026-11-01.
- field: coordinates, google_maps_url, external_ids
  claim: Google Places lists Restaurante Santa Ana Denis at Playa de Santa Ana, local 4, 29630 Benalmádena (36.5908659,-4.52638), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=17338266336200886205
  source_type: maps_identity
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: medium
  notes: Google Places API (New) searchText on 2026-11-01. Maps establishes identity and position only, not hours, prices or facilities.
- field: driving_time_from_casa_de_la_familia
  claim: 'One-way drive from Casa de la Familia: 27 min, 20.1 km (Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5908659%2C-4.52638&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: medium
  notes: Google Routes API computeRoutes; predicted-traffic estimate for one departure time.
- field: seasonality, cost_level, visit_information
  claim: Restaurant prices and season stay unknown, shown with a "check before visiting" note.
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/approval-decisions-2026-11-01.md
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: high
  notes: Owner decision 7, 2026-11-01, given on the approval checklist and recorded in docs/approval-decisions-2026-11-01.md. This is an editor decision, not an external fact source; source_type is the nearest schema value. Venue-stated opening hours in visit_information remain dated facts.
- field: parking, transport_options, toilets_available, accessibility, dog_friendly, booking_required
  claim: Practical details for restaurants are deliberately left unknown, as for beaches.
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/approval-decisions-2026-11-01.md
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: high
  notes: Owner decision 8, 2026-11-01, given on the approval checklist and recorded in docs/approval-decisions-2026-11-01.md. This is an editor decision, not an external fact source; source_type is the nearest schema value. Replaces review issue practical_details_unverified.
- field: age_groups, family_score
  claim: 'Owner-approved family assessment: age groups Small children (0-6), Children (7-12), Young adults, Seniors; scores small_children medium, children high, young_adults medium, seniors medium.'
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/family-assessment-decisions-2026-11-02.md
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: high
  notes: 'Owner decisions 2/6: Claude proposed values (docs/family-assessment-proposal-2026-11-02.md); the owner corrected and approved them on the checklist page on 2026-11-02. Editorial judgment, not an external fact source; source_type is the nearest schema value. Scores are suitability guidance, not safety advice. '
- field: cost_level
  claim: '"Merluza a la plancha / Grilled hake / 18,50 €"; "Pez espada a la plancha / Grilled sword fish / 18,50 €"; "Gambas a la plancha de Málaga / Grilled prawns / 26,00 €"; "Copa de vino de la casa / 4,00 €"; "Botella de cerveza / 3,50 €"'
  source_url: https://www.restaurantesantaanadenis.com/carta
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band approved by owner 2026-11-02
  confidence: high
  notes: Own carta; name, translation and price joined with ' / '.
review_issues: []
created_at: 2026-11-01
updated_at: '2026-11-03'
last_verified: 2026-11-01
last_reviewed_at: 2026-11-02
next_review_at: 2027-04-01
review_decision:
  decision: approved
  reviewer: Eric Olesen (editor-of-record)
  date: '2026-11-02'
  notes: Approved by the owner on the approval page "CalleMilano godkendelse 8 poster" (saved 2026-11-02 07:08 UTC; recorded in docs/approval-decisions-2026-11-02.md). Owner confirmed energy_level Low and the family assessment of 2026-11-02. Practical details, prices and season stay unknown by owner decisions 7 and 8 (shown as "check before visiting"). SEO title and description had "draft record" removed at approval (wording only, no fact changed).
redirects: []
---
