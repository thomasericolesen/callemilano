---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-LA-MAR-SALA-001
slug: la-mar-sala
name: La Mar Salá
category: Restaurants
tags:
- Restaurant
- Beach
coordinates:
  latitude: 36.5576685
  longitude: -4.6093624
  purpose: venue
  label: La Mar Salá, Paseo Marítimo Rey de España 95, 29640 Fuengirola (Google Places listing)
  source: Google Places API (New) searchText, place ChIJJe2zUVHicg0RAObVo27GiMo, read 2026-11-01
  checked_at: '2026-11-01'
google_maps_url: https://maps.google.com/?cid=14594132770991498752
external_ids:
  google_place_id: ChIJJe2zUVHicg0RAObVo27GiMo
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 17 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: La Mar Salá, Paseo Marítimo Rey de España 95, 29640 Fuengirola
  source: Google Routes API computeRoutes, run 2026-11-01 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5576685,-4.6093624); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5576685%2C-4.6093624&travelmode=driving
  checked_at: '2026-11-01'
  note: 'Routes API figure: 17 min with predicted Saturday 10:00 traffic (17 min without traffic), 7.0 km via Cam. de Campanales. One predicted sample, not the Google Maps app''s main figure.'
age_groups:
- Children (7-12)
- Young adults
- Seniors
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
cost_level: Unknown
visit_information:
  schedule: Every day 12:00-00:00 (own website, page modified 2026-10-29; no seasonal variation stated).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: https://www.chiringuitolamarsala.es/
  booking: https://www.chiringuitolamarsala.es/contacto-2/
  visitor_information: null
  transport: null
  contact: tel:+34951312241
related_places:
- id: ES-AND-MAL-BOLICHES-GAVIOTAS-001
  relationship: nearby
  note: Beach bar on the Los Boliches stretch of the Fuengirola promenade.
description_short: Beach bar with a serviced sunbed area on the Los Boliches promenade, Fuengirola, open daily 12:00-midnight; about 17 minutes by car.
description_long: 'La Mar Salá is a beach bar on the Paseo Marítimo Rey de España (number 95) at Playa de los Boliches in Fuengirola. Its own website gives daily opening hours of 12:00 to midnight, a sunbed lounge area with food and drink service, and booking through its contact page (phone 951 31 22 41). Google places it at the boundary between the Los Boliches and Fuengirola centre stretches. Route check: about 17 minutes from Casa de la Familia (Saturday 10:00, predicted traffic). Children''s facilities, prices and accessibility are not confirmed. Prices and seasonal opening are not confirmed; check with the restaurant before visiting.'
seo_title: La Mar Salá, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for La Mar Salá (Fuengirola): location, drive from Casa de la Familia and what is confirmed so far.'
images: []
evidence:
- field: name, municipality, food_available, links
  claim: 'Own website (modified 2026-10-29): beach bar on the Paseo Marítimo of Fuengirola, Playa de los Boliches, at Paseo Marítimo Rey de España 95; open every day 12:00-00:00; phone 951 31 22 41; sunbed lounge area with service; table and sunbed booking via the contact page.'
  source_url: https://www.chiringuitolamarsala.es/
  source_type: official_venue
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: high
  notes: Own website read on 2026-11-01.
- field: coordinates, google_maps_url, external_ids
  claim: Google Places lists La Mar Salá at Paseo Marítimo Rey de España 95, 29640 Fuengirola (36.5576685,-4.6093624), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=14594132770991498752
  source_type: maps_identity
  checked_at: '2026-11-01'
  checked_by: Claude (restaurant pilot 2026-11-01)
  confidence: medium
  notes: Google Places API (New) searchText on 2026-11-01. Maps establishes identity and position only, not hours, prices or facilities.
- field: driving_time_from_casa_de_la_familia
  claim: 'One-way drive from Casa de la Familia: 17 min, 7.0 km (Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5576685%2C-4.6093624&travelmode=driving
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
  claim: 'Owner-approved family assessment: age groups Children (7-12), Young adults, Seniors; scores small_children medium, children medium, young_adults high, seniors medium.'
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/family-assessment-decisions-2026-11-02.md
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: high
  notes: 'Owner decisions 2/6: Claude proposed values (docs/family-assessment-proposal-2026-11-02.md); the owner corrected and approved them on the checklist page on 2026-11-02. Editorial judgment, not an external fact source; source_type is the nearest schema value. Scores are suitability guidance, not safety advice. '
review_issues:
- code: energy_level_editorial_estimate
  severity: info
  fields:
  - energy_level
  description: energy_level Low is an editorial default for a restaurant visit; confirm it at editorial review.
  retryable: false
  owner: human_editor
created_at: 2026-11-01
updated_at: '2026-11-02'
last_verified: 2026-11-01
last_reviewed_at: null
next_review_at: 2027-04-01
review_decision: null
redirects: []
---
