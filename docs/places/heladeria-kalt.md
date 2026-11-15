---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-HELADERIA-KALT-001
slug: heladeria-kalt
name: Heladería KALT
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.4933542
  longitude: -4.775796199999999
  purpose: venue
  label: Heladería KALT, Centro Comercial Contur, N-340, km 192, 29604 Marbella, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJrZ5AlF4hcw0R75U9H6n0WUg, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=5213467050868839919
external_ids:
  google_place_id: ChIJrZ5AlF4hcw0R75U9H6n0WUg
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 21 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Heladería KALT, Centro Comercial Contur, N-340, km 192, 29604 Marbella, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4933542,-4.775796199999999); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4933542%2C-4.775796199999999&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 21 min, 16.9 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: medium
  children: high
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
cost_level: Unknown
visit_information:
  schedule: 'Check before visiting: own Instagram gives Monday-Tuesday 13:30-19:00, Wednesday-Sunday 13:30-21:00, but signals a seasonal closing (2026-11-15).'
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: https://www.instagram.com/kalthelados?igsh=dTlwemw4ZDdocnVt&utm_source=qr
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Heladería KALT: handcrafted ice-cream shop at Centro Comercial Contur, Marbella, about 21 min by car. May close for the season.'
description_long: KALT is a handcrafted ice-cream shop at Centro Comercial Contur (N-340, km 192) in Marbella. Its own Instagram profile gives Monday-Tuesday 13:30-19:00 and Wednesday-Sunday 13:30-21:00, but it also has a 'Season closing' highlight, so it may close in winter (checked 2026-11-15); check before visiting. About 21 minutes by car from Casa de la Familia.
seo_title: Heladería KALT, Marbella | CalleMilano draft record
seo_description: 'Draft record for Heladería KALT (Marbella): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Heladería KALT' at Centro Comercial Contur, N-340, km 192, 29604 Marbella, Málaga, España (36.4933542,-4.775796199999999), status OPERATIONAL, type ice_cream_shop.
  source_url: https://maps.google.com/?cid=5213467050868839919
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 21 min by car (16.9 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4933542%2C-4.775796199999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule, description_long
  claim: 'Instagram bio: ''Handcrafted Ice Cream | We are Open | Monday -Tuesday | 13:30-19:00 | Wednesday-Sunday | 13:30-21:00''; ''Centro Commercial Contur N-340, km 192, Marbella''.'
  source_url: https://www.instagram.com/kalthelados
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: low
  notes: Highlight 'Season closing' suggests a seasonal closure; bio hours may be summer hours.
- field: tags, age_groups, family_score, energy_level
  claim: 'Editor decision 2026-11-15 on the tags list: tags = Restaurant; age_groups = Small children (0-6), Children (7-12), Young adults, Seniors; family_score = small_children medium, children high, young_adults medium, seniors medium; energy_level = Low.'
  source_url: https://claude.ai/artifact/VoHiKgGvqiiP3YA66KP3s5
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-15
  confidence: high
  notes: The editor's own judgement; answers stored in collection tags_2026_11_15.
review_issues:
- code: facts_not_checked
  severity: warning
  fields:
  - description_long
  - visit_information
  - cost_level
  - accessibility
  - parking
  description: Created from Google Places identity and a route check only; needs official or own sources.
  retryable: true
  owner: fact_check
- code: seasonal_closure_unclear
  severity: warning
  fields:
  - visit_information.schedule
  - seasonality
  description: Instagram highlight 'Season closing' suggests a winter closure; season dates not found. Check at the next review.
  retryable: true
  owner: fact_check
created_at: '2026-11-15'
updated_at: '2026-11-15'
last_verified: '2026-11-15'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
