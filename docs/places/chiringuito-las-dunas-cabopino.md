---
schema_version: 1.0.0
status: needs_editorial_review
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
age_groups:
- Children (7-12)
- Young adults
family_score:
  small_children: medium
  children: medium
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
  cost_basis: 'No prices on own site; Tripadvisor price marking "€€ - €€€" read as the middle band. Fallback source per docs/trip-planner-agents.md. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).N'
  cost_checked_at: '2026-11-02'
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
  claim: 'Owner-approved family assessment: age groups Children (7-12), Young adults; scores small_children medium, children medium, young_adults medium, seniors medium.'
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/decisions/family-assessment-decisions-2026-11-02.md
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: high
  notes: 'Owner decisions 2/6: Claude proposed values (docs/decisions/family-assessment-proposal-2026-11-02.md); the owner corrected and approved them on the checklist page on 2026-11-02. Editorial judgment, not an external fact source; source_type is the nearest schema value. Scores are suitability guidance, not safety advice. '
- field: cost_level
  claim: '"€€ - €€€"'
  source_url: https://www.tripadvisor.es/Restaurant_Review-g187439-d3294578-Reviews-Chiringuito_Las_Dunas-Marbella_Costa_del_Sol_Province_of_Malaga_Andalucia.html
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: low
  notes: Tripadvisor price marking only (search excerpt); no ratings or reviews recorded. Own-site prices preferred when available. Quote from search snippet of tripadvisor.es listing 'CHIRINGUITO LAS DUNAS, Marbella' (Cabopino). Matched on name and locality; the key says 'Cabopino', the listing does not repeat that word in its ti
review_issues:
- code: winter_opening_unclear
  severity: warning
  fields:
  - seasonality
  - visit_information
  description: Own Instagram says the regular season ends 1 November but announces staying this year; winter days and hours are unknown. Confirm before recommending a visit between November and spring.
  retryable: true
  owner: fact_check
- code: energy_level_editorial_estimate
  severity: info
  fields:
  - energy_level
  description: energy_level Low is an editorial default for a restaurant visit; confirm it at editorial review.
  retryable: false
  owner: human_editor
- code: cost_level_secondary_source
  severity: info
  fields:
  - cost_level
  description: cost_level is based on the Tripadvisor price marking, not the own menu; replace when an own menu with prices is found.
  retryable: true
  owner: human_editor
created_at: 2026-11-01
updated_at: '2026-11-11'
last_verified: 2026-11-01
last_reviewed_at: null
next_review_at: 2027-04-01
review_decision: null
redirects: []
---
