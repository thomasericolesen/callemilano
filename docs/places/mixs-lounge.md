---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-MIXS-LOUNGE-001
slug: mixs-lounge
name: Mixs Lounge
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.5345521
  longitude: -4.6598372999999995
  purpose: venue
  label: Mixs Lounge, Edificio colina park, Cl. Buitre, 45, 29649 Las Lagunas de Mijas, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJN-Yokn7hcg0RIwuySIjMK8E, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=13919443959025896227
external_ids:
  google_place_id: ChIJN-Yokn7hcg0RIwuySIjMK8E
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 2 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Mixs Lounge, Edificio colina park, Cl. Buitre, 45, 29649 Las Lagunas de Mijas, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5345521,-4.6598372999999995); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5345521%2C-4.6598372999999995&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 2 min, 0.79 km. Walking (Routes API WALK, same day): 5 min, 0.35 km. One predicted sample, not the Google Maps app''s main figure.'
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
description_short: 'Mixs Lounge: Indian restaurant (Google lists it as "Mixs longe"), about 5 min on foot or 2 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Mixs Lounge is a Indian restaurant (Google lists it as "Mixs longe") at Edificio colina park, Cl. Buitre, 45, 29649 Las Lagunas de Mijas, Málaga. From Casa de la Familia it is about 5 minutes on foot (0.35 km, Google's walking route) or about 2 minutes by car (Google route check, Saturday 10:00). Opening hours, prices, age rules and facilities have not been checked yet; check with the venue before visiting.
seo_title: Mixs Lounge, Mijas | CalleMilano draft record
seo_description: 'Draft record for Mixs Lounge (Mijas): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, food_available
  claim: Google Places lists 'Mixs longe' at Edificio colina park, Cl. Buitre, 45, 29649 Las Lagunas de Mijas, Málaga, España (36.5345521,-4.6598372999999995), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=13919443959025896227
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia, description_long (walking time)
  claim: 'From Casa de la Familia: 2 min by car (0.79 km, Saturday 10:00 predicted traffic) and 5 min on foot (0.35 km).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5345521%2C-4.6598372999999995&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00, and WALK (https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5345521%2C-4.6598372999999995&travelmode=walking). Google's walking route says nothing about pavements, crossings or whether it suits children.
- field: name
  claim: A Just Eat delivery listing names "Mixs Longe Restaurante" at Calle Buitre 45, 29649 Las Lagunas de Mijas; an Uber Eats listing names "Mixs Curry & Pizza" on Calle Buitre in Cerros del Águila.
  source_url: https://www.just-eat.es/restaurants-mixs-longe-restaurante-29649/menu
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: low
  notes: Search excerpts read 2026-11-02. The venue's own name and spelling are unconfirmed ("Lounge", "Longe" or "Curry & Pizza").
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
- code: name_unconfirmed
  severity: warning
  fields:
  - name
  - slug
  description: Google and Just Eat spell it "Mixs longe"; Uber Eats lists "Mixs Curry & Pizza" on the same street. Confirm the venue's own name before review; a name change keeps the ID.
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
