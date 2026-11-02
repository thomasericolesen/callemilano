---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-MORROFINO-001
slug: morrofino
name: Morrofino
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.633802
  longitude: -4.4878468
  purpose: venue
  label: Morrofino, Paseo Marítimo 69, local 16, 29620 Torremolinos (Google Places listing)
  source: Google Places API (New) searchText, place ChIJ108ayAD7cg0R5c0rCMaYpTc, read 2026-11-01
  checked_at: '2026-11-01'
google_maps_url: https://maps.google.com/?cid=4009779019551329765
external_ids:
  google_place_id: ChIJ108ayAD7cg0R5c0rCMaYpTc
municipality: Torremolinos
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 29 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Morrofino, Paseo Marítimo 69, local 16, 29620 Torremolinos
  source: Google Routes API computeRoutes, run 2026-11-01 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.633802,-4.4878468); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.633802%2C-4.4878468&travelmode=driving
  checked_at: '2026-11-01'
  note: 'Routes API figure: 29 min with predicted Saturday 10:00 traffic (29 min without traffic), 24.3 km via AP-7. One predicted sample, not the Google Maps app''s main figure.'
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
  schedule: 12:00-24:00, closed Tuesday (own website, read 2026-11-01; no seasonal variation stated).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: https://morrofinoplayamar.com/
  booking: https://reservas.morrofinoplayamar.com/reservar/morrofino
  visitor_information: null
  transport: null
  contact: tel:+34952185597
related_places:
- id: ES-AND-MAL-PLAYAMAR-001
  relationship: nearby
  note: On the Paseo Marítimo at Playamar.
- id: ES-AND-MAL-LOS-ALAMOS-001
  relationship: nearby
  note: Short walk along the promenade to Los Álamos.
description_short: Mediterranean restaurant on the Paseo Marítimo at Playamar, Torremolinos, with gluten-free, vegan and vegetarian options; about 29 minutes by car.
description_long: 'Morrofino is a restaurant on the Paseo Marítimo in Playamar, Torremolinos (Paseo Marítimo 69, local 16). Its own website describes traditional and Mediterranean cooking with gluten-free, vegan and vegetarian options, opening hours 12:00-24:00 with Tuesday closed, and online table booking. Route check: about 29 minutes from Casa de la Familia (Saturday 10:00, predicted traffic), close to the 30-minute local-area limit. Prices, children''s menu, high chairs and accessibility are not confirmed by an official source. Prices and seasonal opening are not confirmed; check with the restaurant before visiting.'
seo_title: Morrofino, Torremolinos | CalleMilano draft record
seo_description: 'Draft record for Morrofino (Torremolinos): location, drive from Casa de la Familia and what is confirmed so far.'
images: []
evidence:
- field: name, municipality, food_available, links
  claim: 'Own website: Mediterranean and traditional cooking in Playamar, Torremolinos, facing the Paseo Marítimo; gluten-free, vegan and vegetarian options; hours 12:00-24:00, closed Tuesday; phone 952 18 55 97; online table booking.'
  source_url: https://morrofinoplayamar.com/
  source_type: official_venue
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: high
  notes: Read on 2026-11-01.
- field: coordinates, google_maps_url, external_ids
  claim: Google Places lists Morrofino at Paseo Marítimo 69, local 16, 29620 Torremolinos (36.633802,-4.4878468), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=4009779019551329765
  source_type: maps_identity
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: medium
  notes: Google Places API (New) searchText on 2026-11-01. Maps establishes identity and position only, not hours, prices or facilities.
- field: driving_time_from_casa_de_la_familia
  claim: 'One-way drive from Casa de la Familia: 29 min, 24.3 km (Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.633802%2C-4.4878468&travelmode=driving
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
- code: driving_time_near_local_limit
  severity: info
  fields:
  - driving_time_from_casa_de_la_familia
  description: Routes API gives 29 min (Saturday 10:00), just under the 30-min local_30km limit; the Google Maps app figure may differ.
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
