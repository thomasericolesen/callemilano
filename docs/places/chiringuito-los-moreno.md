---
schema_version: 1.0.0
status: approved
id: ES-AND-MAL-CHIRINGUITO-LOS-MORENO-001
slug: chiringuito-los-moreno
name: Chiringuito Los Moreno
category: Restaurants
tags:
- Restaurant
- Beach
coordinates:
  latitude: 36.4995404
  longitude: -4.6837348
  purpose: venue
  label: Chiringuito Los Moreno, C. Butibamba, 14B, 29649 La Cala de Mijas (Google Places listing)
  source: Google Places API (New) searchText, place ChIJUZiWWzQecw0RzxsKypXrEbY, read 2026-11-01
  checked_at: '2026-11-01'
google_maps_url: https://maps.google.com/?cid=13119526218079280079
external_ids:
  google_place_id: ChIJUZiWWzQecw0RzxsKypXrEbY
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 15 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Chiringuito Los Moreno, C. Butibamba, 14B, 29649 La Cala de Mijas
  source: Google Routes API computeRoutes, run 2026-11-01 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.4995404,-4.6837348); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4995404%2C-4.6837348&travelmode=driving
  checked_at: '2026-11-01'
  note: 'Routes API figure: 15 min with predicted Saturday 10:00 traffic (15 min without traffic), 6.8 km via Arrabal Sector 13. One predicted sample, not the Google Maps app''s main figure.'
age_groups:
- Young adults
family_score:
  small_children: medium
  children: medium
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
  cost_basis: 'No own website; Tripadvisor price marking ''€€ - €€€'' read as the middle band. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-02'
links:
  official_website: null
  booking: null
  visitor_information: https://turismo.mijas.es/es/gastronomia/donde-comer/chiringuitos/chiringuito-los-moreno
  transport: null
  contact: tel:+34615673977
related_places:
- id: ES-AND-MAL-LA-BUTIBAMBA-001
  relationship: nearby
  note: Beach bar at La Butiplaya, the La Butibamba stretch of La Cala.
description_short: Beach bar (chiringuito) at La Butiplaya, La Cala de Mijas, listed by Turismo de Mijas; about 15 minutes by car from Casa de la Familia.
description_long: 'Chiringuito Los Moreno is a beach bar at C/ Butibamba 14B, La Butiplaya (La Cala, Mijas), listed in the beach-bar section of the official Mijas tourism site with phone 615 673 977. Its own Instagram profile describes Mediterranean food with fish on the espeto (skewer), sunbeds and live music (profile excerpt, not an independent check). Route check: about 15 minutes from Casa de la Familia (Saturday 10:00, predicted traffic). Opening hours, season, prices, children''s facilities and accessibility are not confirmed by an official source. Prices and seasonal opening are not confirmed; check with the restaurant before visiting.'
seo_title: Chiringuito Los Moreno, Mijas | CalleMilano
seo_description: 'Chiringuito Los Moreno (Mijas): beach restaurant near Casa de la Familia, with drive time, what is confirmed and what to check before visiting.'
images: []
evidence:
- field: name, municipality, food_available, links
  claim: Turismo de Mijas lists Chiringuito Los Moreno under beach bars at C/ Butibamba 14B, La Butiplaya (La Cala), phone 615 673 977, e-mail salvimoreno@hotmail.com.
  source_url: https://turismo.mijas.es/es/gastronomia/donde-comer/chiringuitos/chiringuito-los-moreno
  source_type: official_tourism
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: high
  notes: Read on 2026-11-01.
- field: coordinates, google_maps_url, external_ids
  claim: Google Places lists Chiringuito Los Moreno at C. Butibamba, 14B, 29649 La Cala de Mijas (36.4995404,-4.6837348), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=13119526218079280079
  source_type: maps_identity
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: medium
  notes: Google Places API (New) searchText on 2026-11-01. Maps establishes identity and position only, not hours, prices or facilities.
- field: driving_time_from_casa_de_la_familia
  claim: 'One-way drive from Casa de la Familia: 15 min, 6.8 km (Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4995404%2C-4.6837348&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: medium
  notes: Google Routes API computeRoutes; predicted-traffic estimate for one departure time.
- field: description_long (food, sunbeds, live music)
  claim: 'Own Instagram profile: Mediterranean food, speciality fish on the espeto, sunbeds, live music.'
  source_url: https://www.instagram.com/chiringuitolosmoreno/
  source_type: official_venue
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: low
  notes: Search-result excerpt of the venue's own profile on 2026-11-01; the page itself could not be read.
- field: seasonality, cost_level, visit_information
  claim: Restaurant prices and season stay unknown, shown with a "check before visiting" note.
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/decisions/approval-decisions-2026-11-01.md
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: high
  notes: Owner decision 7, 2026-11-01, given on the approval checklist and recorded in docs/decisions/approval-decisions-2026-11-01.md. This is an editor decision, not an external fact source; source_type is the nearest schema value. Venue-stated opening hours in visit_information remain dated facts.
- field: parking, transport_options, toilets_available, accessibility, dog_friendly, booking_required
  claim: Practical details for restaurants are deliberately left unknown, as for beaches.
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/decisions/approval-decisions-2026-11-01.md
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: high
  notes: Owner decision 8, 2026-11-01, given on the approval checklist and recorded in docs/decisions/approval-decisions-2026-11-01.md. This is an editor decision, not an external fact source; source_type is the nearest schema value. Replaces review issue practical_details_unverified.
- field: age_groups, family_score
  claim: 'Owner-approved family assessment: age groups Young adults; scores small_children medium, children medium, young_adults high, seniors medium.'
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/decisions/family-assessment-decisions-2026-11-02.md
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: high
  notes: 'Owner decisions 2/6: Claude proposed values (docs/decisions/family-assessment-proposal-2026-11-02.md); the owner corrected and approved them on the checklist page on 2026-11-02. Editorial judgment, not an external fact source; source_type is the nearest schema value. Scores are suitability guidance, not safety advice. '
- field: cost_level
  claim: '"Precio. €€ - €€€"'
  source_url: https://www.tripadvisor.es/Restaurant_Review-g1892987-d10475750-Reviews-or15-Chiringuito_Los_Moreno-La_Cala_de_Mijas_Mijas_Costa_del_Sol_Province_of_Ma.html
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band approved by owner 2026-11-02
  confidence: low
  notes: Tripadvisor price marking from search excerpt; no ratings recorded.
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
  notes: Approved by the owner on the approval page "CalleMilano godkendelse 8 poster" (saved 2026-11-02 07:08 UTC; recorded in docs/decisions/approval-decisions-2026-11-02.md). Owner confirmed energy_level Low and the family assessment of 2026-11-02. Practical details, prices and season stay unknown by owner decisions 7 and 8 (shown as "check before visiting"). SEO title and description had "draft record" removed at approval (wording only, no fact changed).
redirects: []
---
