---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-DELIS-HELADOS-ARTESANALES-001
slug: delis-helados-artesanales
name: DELIS HELADOS ARTESANALES
category: Restaurants
tags: []
coordinates:
  latitude: 36.5990501
  longitude: -4.5337667
  purpose: venue
  label: DELIS HELADOS ARTESANALES, Av. de la Constitución, 10, 29631 Arroyo de La Miel, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJARRzN2_9cg0Rnpce0cKPi9I, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=15171377836622518174
external_ids:
  google_place_id: ChIJARRzN2_9cg0Rnpce0cKPi9I
municipality: Benalmádena
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 23 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: DELIS HELADOS ARTESANALES, Av. de la Constitución, 10, 29631 Arroyo de La Miel, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5990501,-4.5337667); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5990501%2C-4.5337667&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 23 min, 18.4 km. One predicted sample.'
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
  contact: https://www.instagram.com/delishelados/
related_places: []
description_short: 'Delis Helados: Argentine-style artisan ice-cream shop with café in Arroyo de la Miel, Benalmádena, about 23 min by car. Hours not yet found.'
description_long: Delis Helados is an Argentine-style artisan ice-cream shop on Avenida de la Constitución in Arroyo de la Miel, Benalmádena, which also serves coffee, according to its own Instagram profile (phone +34 669 96 49 69). Opening hours and prices were not found (checked 2026-11-15); check before visiting. About 23 minutes by car from Casa de la Familia.
seo_title: DELIS HELADOS ARTESANALES, Benalmádena | CalleMilano draft record
seo_description: 'Draft record for DELIS HELADOS ARTESANALES (Benalmádena): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'DELIS HELADOS ARTESANALES' at Av. de la Constitución, 10, 29631 Arroyo de La Miel, Málaga, España (36.5990501,-4.5337667), status OPERATIONAL, type ice_cream_shop.
  source_url: https://maps.google.com/?cid=15171377836622518174
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 23 min by car (18.4 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5990501%2C-4.5337667&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long, links.contact
  claim: 'Instagram bio: ''🇦🇷 Heladería artesanal 🇦🇷'' / ''VOLVIO EL MEJOR HELADO DE MALAGA🍨🍦'' / ''+34 669 96 49 69''; highlights ''Menú 🥐'', ''Cafetería ☕️''.'
  source_url: https://www.instagram.com/delishelados/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (second source attempt 2026-11-15, Claude in Chrome)
  confidence: medium
  notes: 'Identity: the phone on the profile matches the Google Maps listing for DELIS HELADOS ARTESANALES, Av. de la Constitución 10 (checked 2026-11-15). The profile shows no address.'
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
- code: not_found_after_two_attempts
  severity: info
  fields:
  - visit_information.schedule
  - cost_level
  retryable: true
  owner: fact_check
  description: 'Two source attempts (2026-11-15) found no official answer for: opening hours and prices. Value left unknown; check before visiting. Retry at the next freshness review.'
created_at: '2026-11-15'
updated_at: '2026-11-15'
last_verified: '2026-11-15'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
