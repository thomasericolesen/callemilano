---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-CHIRINGUITO-LAS-DUNAS-CABOPINO-001
slug: chiringuito-las-dunas-cabopino
name: Chiringuito Las Dunas
category: Restaurants
tags:
- Restaurant
- Beach
coordinates:
  latitude: 36.4860513
  longitude: -4.7356401
  purpose: venue
  label: Chiringuito Las Dunas, Urb. Cabopino, calle de la playa, 29604 Marbella (Google Places listing)
  source: Google Places API (New) searchText, place ChIJYWXF_yQgcw0RZL80by3DvYU, read 2026-11-01
  checked_at: '2026-11-01'
google_maps_url: https://maps.google.com/?cid=9637073377549401956
external_ids:
  google_place_id: ChIJYWXF_yQgcw0RZL80by3DvYU
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 22 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Chiringuito Las Dunas, Urb. Cabopino, calle de la playa, 29604 Marbella
  source: Google Routes API computeRoutes, run 2026-11-01 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.4860513,-4.7356401); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4860513%2C-4.7356401&travelmode=driving
  checked_at: '2026-11-01'
  note: 'Routes API figure: 22 min with predicted Saturday 10:00 traffic (22 min without traffic), 13.6 km via A-7. One predicted sample, not the Google Maps app''s main figure.'
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
  visitor_information: https://www.facebook.com/chiringuitolasdunasdecabopino/
  transport: null
  contact: null
related_places:
- id: ES-AND-MAL-CABOPINO-ARTOLA-001
  relationship: nearby
  note: Beach bar at Cabopino beach.
description_short: Beach bar (chiringuito) at Cabopino beach, Marbella; seasonal, about 22 minutes by car from Casa de la Familia.
description_long: 'Chiringuito Las Dunas is a beach bar at Cabopino beach in Marbella (urb. Cabopino, calle de la playa, per its own Facebook page). Its own Instagram profile says its regular season ends on 1 November, with an announcement about staying open in some form this winter; the details were not confirmed. Route check: about 22 minutes from Casa de la Familia (Saturday 10:00, predicted traffic). Menu, prices, children''s facilities and accessibility are not confirmed by an official source. Prices and seasonal opening are not confirmed; check with the restaurant before visiting.'
seo_title: Chiringuito Las Dunas, Marbella | CalleMilano draft record
seo_description: 'Draft record for Chiringuito Las Dunas (Marbella): location, drive from Casa de la Familia and what is confirmed so far.'
images: []
evidence:
- field: name, municipality, food_available, links
  claim: The venue's own Facebook page gives the address urb. Cabopino, c/ de la playa, 29604 Marbella.
  source_url: https://www.facebook.com/chiringuitolasdunasdecabopino/
  source_type: official_venue
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: medium
  notes: Search-result excerpt of the venue's own page on 2026-11-01; the page itself was not read.
- field: coordinates, google_maps_url, external_ids
  claim: Google Places lists Chiringuito Las Dunas at Urb. Cabopino, calle de la playa, 29604 Marbella (36.4860513,-4.7356401), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=9637073377549401956
  source_type: maps_identity
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: medium
  notes: Google Places API (New) searchText on 2026-11-01. Maps establishes identity and position only, not hours, prices or facilities.
- field: driving_time_from_casa_de_la_familia
  claim: 'One-way drive from Casa de la Familia: 22 min, 13.6 km (Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4860513%2C-4.7356401&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: medium
  notes: Google Routes API computeRoutes; predicted-traffic estimate for one departure time.
- field: seasonality, description_long (season)
  claim: 'Own Instagram profile: regular season ends 1 November; an announcement that the team stays this year (details not stated in the excerpt).'
  source_url: https://www.instagram.com/chiringuitolasdunas/
  source_type: official_venue
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: low
  notes: Search-result excerpt only on 2026-11-01; the profile page could not be read (site not supported by the scraper).
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
- code: winter_opening_unclear
  severity: warning
  fields:
  - seasonality
  - visit_information
  description: Own Instagram says the regular season ends 1 November but announces staying this year; winter days and hours are unknown. Confirm before recommending a visit between November and spring.
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
