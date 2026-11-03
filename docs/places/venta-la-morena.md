---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-VENTA-LA-MORENA-001
slug: venta-la-morena
name: Venta La Morena
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.54382100000001
  longitude: -4.6565385
  purpose: venue
  label: Venta La Morena, Camino Viejo de Coín, Km. 2, 5, 29651 Las Lagunas de Mijas, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJAy9bGRXicg0RJWcr01Der7Q, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=13019869486472980261
external_ids:
  google_place_id: ChIJAy9bGRXicg0RJWcr01Der7Q
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 4 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Venta La Morena, Camino Viejo de Coín, Km. 2, 5, 29651 Las Lagunas de Mijas, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.54382100000001,-4.6565385); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.54382100000001%2C-4.6565385&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 4 min, 1.76 km. One predicted sample, not the Google Maps app''s main figure.'
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
cost_level: €€
visit_information:
  schedule: null
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'No prices on own site; Tripadvisor price marking "Precio. €€ - €€€." read as the middle band. Fallback source per docs/trip-planner-agents.md. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).N'
  cost_checked_at: '2026-11-02'
links:
  official_website: https://www.facebook.com/ventalamorena/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Venta La Morena: venta (roadside restaurant) with grill on the Camino Viejo de Coín, about 4 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: 'Venta La Morena is a venta (roadside restaurant) with grill on the Camino Viejo de Coín at Camino Viejo de Coín, Km. 2, 5, 29651 Las Lagunas de Mijas, Málaga. From Casa de la Familia it is about 4 minutes by car (Google route check, Saturday 10:00). Owner''s own knowledge: Well visited and a good place; the lamb is very good. Its own Facebook page exists, but opening hours, prices, children''s facilities and accessibility could not be read from it; check with the venue before visiting.'
seo_title: Venta La Morena, Mijas | CalleMilano draft record
seo_description: 'Draft record for Venta La Morena (Mijas): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, food_available
  claim: Google Places lists 'Venta La Morena' at Camino Viejo de Coín, Km. 2, 5, 29651 Las Lagunas de Mijas, Málaga, España (36.54382100000001,-4.6565385), business status OPERATIONAL, website https://gmaps.top/venta-la-morena.
  source_url: https://maps.google.com/?cid=13019869486472980261
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 4 min by car (1.76 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.54382100000001%2C-4.6565385&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: 'Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time removed 2026-11-02 (owner decision: walking times of 20 minutes or more are not shown).'
- field: description_long (owner knowledge)
  claim: Well visited and a good place; the lamb is very good.
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/nearby-selection-2026-11-02.md
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: medium
  notes: Owner's own local knowledge, given on the nearby selection page on 2026-11-02; not independently verified.
- field: links.official_website
  claim: The venue has its own Facebook page (@ventalamorena) giving Camino Viejo de Coín, Mijas.
  source_url: https://www.facebook.com/ventalamorena/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: low
  notes: Search excerpt read 2026-11-02; the page content (hours, menu) was not read. Google's listed website is a directory page (gmaps.top), not the venue's own.
- field: cost_level
  claim: '"Precio. €€ - €€€."'
  source_url: https://www.tripadvisor.es/Restaurant_Review-g580271-d3699293-Reviews-or75-Venta_La_Morena-Mijas_Costa_del_Sol_Province_of_Malaga_Andalucia.html
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: low
  notes: Tripadvisor price marking only (search excerpt); no ratings or reviews recorded. Own-site prices preferred when available. Quote from search snippet of tripadvisor.es listing 'VENTA LA MORENA, Mijas'. Name and town match.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  description: 'Age groups and family scores are not assessed; energy_level Low is an editorial estimate from the type of place. Owner note: Well visited and a good place; the lamb is very good.'
  retryable: true
  owner: human_editor
- code: hours_and_prices_unverified
  severity: warning
  fields:
  - visit_information
  - cost_level
  - accessibility
  description: Only the own Facebook page was found and its content was not read. Hours, menu and prices still need checking.
  retryable: true
  owner: fact_check
- code: cost_level_secondary_source
  severity: info
  fields:
  - cost_level
  description: cost_level is based on the Tripadvisor price marking, not the own menu; replace when an own menu with prices is found.
  retryable: true
  owner: human_editor
created_at: '2026-11-02'
updated_at: '2026-11-03'
last_verified: '2026-11-02'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
