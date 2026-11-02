---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-EQUESTRIAN-CENTRE-CHAPARRAL-001
slug: equestrian-centre-chaparral
name: Equestrian Centre
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.5400742
  longitude: -4.6594660999999995
  purpose: venue
  label: Equestrian Centre, Diseminado Chaparral, 231, 29649 Las Lagunas de Mijas, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJ16vvKZPhcg0RnMcLZGUrxOU, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=16556405844590970780
external_ids:
  google_place_id: ChIJ16vvKZPhcg0RnMcLZGUrxOU
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 4 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Equestrian Centre, Diseminado Chaparral, 231, 29649 Las Lagunas de Mijas, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5400742,-4.6594660999999995); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5400742%2C-4.6594660999999995&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 4 min, 1.3 km. Walking (Routes API WALK, same day): 16 min, 1.22 km. One predicted sample, not the Google Maps app''s main figure.'
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
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Equestrian Centre: venue listed by Google as a restaurant; the name suggests a riding centre, about 16 min on foot or 4 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Equestrian Centre is a venue listed by Google as a restaurant; the name suggests a riding centre at Diseminado Chaparral, 231, 29649 Las Lagunas de Mijas, Málaga. From Casa de la Familia it is about 16 minutes on foot (1.22 km, Google's walking route) or about 4 minutes by car (Google route check, Saturday 10:00). Opening hours, prices, age rules and facilities have not been checked yet; check with the venue before visiting.
seo_title: Equestrian Centre, Mijas | CalleMilano draft record
seo_description: 'Draft record for Equestrian Centre (Mijas): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, food_available
  claim: Google Places lists 'Equestrian Centre' at Diseminado Chaparral, 231, 29649 Las Lagunas de Mijas, Málaga, España (36.5400742,-4.6594660999999995), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=16556405844590970780
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia, description_long (walking time)
  claim: 'From Casa de la Familia: 4 min by car (1.3 km, Saturday 10:00 predicted traffic) and 16 min on foot (1.22 km).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5400742%2C-4.6594660999999995&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00, and WALK (https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5400742%2C-4.6594660999999995&travelmode=walking). Google's walking route says nothing about pavements, crossings or whether it suits children.
review_issues:
- code: facts_not_checked
  severity: warning
  fields:
  - visit_information
  - cost_level
  - seasonality
  - accessibility
  - booking_required
  - food_available
  - toilets_available
  description: Created from Google Places identity and route checks only. Opening hours, season, prices, age rules, booking and facilities still need the venue's own or official sources.
  retryable: true
  owner: fact_check
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  description: Age groups and family scores are not assessed; energy_level Low is an editorial estimate from the type of place.
  retryable: true
  owner: human_editor
- code: no_official_website
  severity: info
  fields:
  - links
  description: Google lists no website; facts may have to come from a social page or a direct contact.
  retryable: true
  owner: fact_check
- code: identity_unclear
  severity: warning
  fields:
  - name
  - category
  - description_long
  description: 'Search on 2026-11-02 found nothing about an "Equestrian Centre" at Diseminado Chaparral 231. Google types it as a restaurant; it may be a riding centre with a bar. Owner to confirm what it is, or drop it. 2026-11-02: the owner does not know the place either; needs a visit or a direct contact before it can go further.'
  retryable: true
  owner: human_editor
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
