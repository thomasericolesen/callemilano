---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-CHIRINGUITO-RAFAEL-001
slug: chiringuito-rafael
name: Chiringuito Rafael
category: Restaurants
tags:
- Restaurant
- Beach
coordinates:
  latitude: 36.599392
  longitude: -4.5102398
  purpose: venue
  label: Chiringuito Rafael, Playa de la Salud, 29630 Benalmádena (Google Places listing)
  source: Google Places API (New) searchText, place ChIJhbPN5G_8cg0RQ0xpdwmEZLU, read 2026-11-01
  checked_at: '2026-11-01'
google_maps_url: https://maps.google.com/?cid=13070717194728983619
external_ids:
  google_place_id: ChIJhbPN5G_8cg0RQ0xpdwmEZLU
municipality: Benalmádena
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 28 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Chiringuito Rafael, Playa de la Salud, 29630 Benalmádena
  source: Google Routes API computeRoutes, run 2026-11-01 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.599392,-4.5102398); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.599392%2C-4.5102398&travelmode=driving
  checked_at: '2026-11-01'
  note: 'Routes API figure: 28 min with predicted Saturday 10:00 traffic (29 min without traffic), 20.3 km via AP-7. One predicted sample, not the Google Maps app''s main figure.'
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
  visitor_information: https://www.facebook.com/rafaelchiringuito/
  transport: null
  contact: null
related_places:
- id: ES-AND-MAL-FUENTE-DE-LA-SALUD-001
  relationship: nearby
  note: Beach bar on Playa de la Salud, by Puerto Marina.
description_short: Seasonal beach bar on Playa de la Salud (Fuente de la Salud), Benalmádena, near Puerto Marina; about 28 minutes by car.
description_long: 'Chiringuito Rafael is a beach bar on Playa de la Salud (Fuente de la Salud) in Benalmádena, on the promenade by Puerto Marina. Its own Facebook page announces each new season, so it is likely seasonal; the season dates were not found. Route check: about 28 minutes from Casa de la Familia (Saturday 10:00, predicted traffic), close to the 30-minute local-area limit. Opening hours, menu, prices, children''s facilities and accessibility are not confirmed by an official source. Prices and seasonal opening are not confirmed; check with the restaurant before visiting.'
seo_title: Chiringuito Rafael, Benalmádena | CalleMilano draft record
seo_description: 'Draft record for Chiringuito Rafael (Benalmádena): location, drive from Casa de la Familia and what is confirmed so far.'
images: []
evidence:
- field: name, municipality, food_available, links
  claim: The venue's own Facebook page (Chiringuito Rafael, Benalmádena) announces its return for another season.
  source_url: https://www.facebook.com/rafaelchiringuito/
  source_type: official_venue
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: low
  notes: Search-result excerpt of the venue's own page on 2026-11-01; the page itself was not read.
- field: coordinates, google_maps_url, external_ids
  claim: Google Places lists Chiringuito Rafael at Playa de la Salud, 29630 Benalmádena (36.599392,-4.5102398), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=13070717194728983619
  source_type: maps_identity
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: medium
  notes: Google Places API (New) searchText on 2026-11-01. Maps establishes identity and position only, not hours, prices or facilities.
- field: driving_time_from_casa_de_la_familia
  claim: 'One-way drive from Casa de la Familia: 28 min, 20.3 km (Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.599392%2C-4.5102398&travelmode=driving
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
- field: name, coordinates
  claim: 'Independent listings agree on the identity and place: Tripadvisor ''Chiringuito Rafael, Benalmádena'' on the Avenida del Puerto Deportivo (Paseo Marítimo) opposite Playa de la Salud; the venue''s Facebook page (search excerpt) ''Paseo Marítimo, S/N, Benalmádena, 29630''; minube phone +34 952 56 17 71.'
  source_url: https://www.tripadvisor.es/Restaurant_Review-g562812-d1929855-Reviews-Chiringuito_Rafael-Benalmadena_Costa_del_Sol_Province_of_Malaga_Andalucia.html
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (beach follow-up 2026-11-02)
  confidence: medium
  notes: Search excerpts read 2026-11-02; Facebook could not be fetched. Identity corroboration only; hours and reviews not recorded.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  description: 'No source on children''s menu, high chairs, play area or family suitability was checked; age groups and family scores are left unknown/empty and energy_level Low is an editorial default for a restaurant visit. Needs editor assessment. 2026-11-02: the owner did not approve the proposed values (see docs/family-assessment-decisions-2026-11-02.md); still open.'
  retryable: true
  owner: human_editor
- code: driving_time_near_local_limit
  severity: info
  fields:
  - driving_time_from_casa_de_la_familia
  description: Routes API gives 28 min (Saturday 10:00), close to the 30-min local_30km limit.
  retryable: true
  owner: human_editor
- code: weak_identity_source
  severity: info
  fields:
  - links
  - evidence
  description: Identity corroborated 2026-11-02 by several independent listings (Paseo Marítimo, opposite Playa de la Salud, Benalmádena). Current operation, season and hours still need the own Facebook page (owner screenshot) or a call.
  retryable: true
  owner: fact_check
created_at: 2026-11-01
updated_at: '2026-11-02'
last_verified: 2026-11-01
last_reviewed_at: null
next_review_at: 2027-04-01
review_decision: null
redirects: []
---
