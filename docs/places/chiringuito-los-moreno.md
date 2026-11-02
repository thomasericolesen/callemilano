---
schema_version: 1.0.0
status: needs_fact_check
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
age_groups: []
family_score:
  small_children: unknown
  children: unknown
  young_adults: unknown
  seniors: unknown
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
cost_level: Unknown
visit_information:
  schedule: null
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
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
seo_title: Chiringuito Los Moreno, Mijas | CalleMilano draft record
seo_description: 'Draft record for Chiringuito Los Moreno (Mijas): location, drive from Casa de la Familia and what is confirmed so far.'
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
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  description: No source on children's menu, high chairs, play area or family suitability was checked; age groups and family scores are left unknown/empty and energy_level Low is an editorial default for a restaurant visit. Needs editor assessment.
  retryable: true
  owner: human_editor
created_at: 2026-11-01
updated_at: '2026-11-02'
last_verified: 2026-11-01
last_reviewed_at: null
next_review_at: 2027-04-01
review_decision: null
redirects: []
---
