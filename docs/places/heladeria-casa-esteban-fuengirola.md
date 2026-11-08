---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-HELADERIA-CASA-ESTEBAN-FUENGIROLA-001
slug: heladeria-casa-esteban-fuengirola
name: Heladería Casa Esteban
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.53738
  longitude: -4.622
  purpose: venue
  label: Heladería casa Esteban, P.º Marítimo Rey de España, 26, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJxcDPWADjcg0RzAbeG1NeKCI, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=2461320907400808140
external_ids:
  google_place_id: ChIJxcDPWADjcg0RzAbeG1NeKCI
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 15 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Heladería casa Esteban, P.º Marítimo Rey de España, 26, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.53738,-4.622); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.53738%2C-4.622&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 15 min, 5.1 km. One predicted sample.'
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
food_available: unknown
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
  visitor_information: null
  transport: null
  contact: tel:+34952192942
related_places: []
description_short: 'Heladería Casa Esteban: artisan ice-cream parlour on the Paseo Marítimo in Fuengirola (one of three shops), about 15 min by car from Casa de la Familia. Partly fact-checked.'
description_long: 'Heladería Casa Esteban is an artisan ice-cream parlour with three shops (Mijas Pueblo, La Cala de Mijas and Fuengirola); this record is the Fuengirola shop at Paseo Marítimo Rey de España 26 (phone 952 19 29 42), according to the shop''s own Instagram and Facebook pages. Opening hours and prices are not published there; check before going. About 15 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Family recommendation (Christian, callemilano.dk): Good ice cream.'
seo_title: Heladería Casa Esteban, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Heladería Casa Esteban (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Heladería casa Esteban' at P.º Marítimo Rey de España, 26, 29640 Fuengirola, Málaga, España (36.53738,-4.622), status OPERATIONAL, type ice_cream_shop.
  source_url: https://maps.google.com/?cid=2461320907400808140
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. From the owner's recommendations on callemilano.dk (Lovable app 'Vores Spanske Hjem', table recommendations), read 2026-11-02.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 15 min by car (5.1 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.53738%2C-4.622&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long (owner knowledge)
  claim: Gode is 🍧🍨🍦
  source_url: https://callemilano.dk/
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Christian (family member, per Eric 2026-11-08); recorded by Claude 2026-11-02
  confidence: medium
  notes: 'Family recommendation by Christian (corrected 2026-11-08; first recorded as the owner''s) (kind ''anbefaling'') on callemilano.dk, read from the Lovable app database 2026-11-02; site tags: børn, is. Personal experience, not independently verified.'
- field: address; links.contact
  claim: '"Mijas Pueblo: Pasaje Esteban Moreno 1 952485216 La Cala de Mijas: Calle Marbella 3 952493549 Fuengirola: Paseo Marítimo Rey de España 26 952192942." ; "Nos encontramos en calle Marbella n3, La Cala de Mijas, Paseo Marítimo Rey de España n26, Fuengirola y pasaje Esteban Moreno n1, Mijas pueblo."'
  source_url: https://www.instagram.com/heladeriacasaesteban
  source_type: official_venue
  checked_at: '2026-11-08'
  checked_by: Claude (main session), Tavily search excerpts
  confidence: medium
  notes: Search excerpts of the shop's own Instagram profile and Facebook page (https://www.facebook.com/heladeriacasaesteban); the pages themselves are behind a login wall. Matches the Google Places point on the Paseo Marítimo in Fuengirola.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  - tags
  description: Age groups, family scores and tags are not assessed; energy_level is an editorial estimate.
  retryable: true
  owner: human_editor
- code: facts_partly_checked
  severity: warning
  fields:
  - visit_information
  - cost_level
  - seasonality
  description: 'Address and phone from the shop''s own social pages (search excerpts, 2026-11-08). Still open: opening hours, season, prices; no own website.'
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-08'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
