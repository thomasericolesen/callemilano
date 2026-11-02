---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-ATV-ADVENTURES-MIJAS-001
slug: atv-adventures-mijas
name: ATV Adventures
category: Family activities
tags:
- Adventure
coordinates:
  latitude: 36.5410031
  longitude: -4.6583355
  purpose: venue
  label: ATV Adventures, C. la Higuera, 26, 29651 Las Lagunas de Mijas, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJr1XX5U0fcw0RQaGm8AoMoPg, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=17915332558806491457
external_ids:
  google_place_id: ChIJr1XX5U0fcw0RQaGm8AoMoPg
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 4 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: ATV Adventures, C. la Higuera, 26, 29651 Las Lagunas de Mijas, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5410031,-4.6583355); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5410031%2C-4.6583355&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 4 min, 1.44 km. Walking (Routes API WALK, same day): 18 min, 1.37 km. One predicted sample, not the Google Maps app''s main figure.'
age_groups: []
family_score:
  small_children: unknown
  children: unknown
  young_adults: unknown
  seniors: unknown
energy_level: Medium
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
booking_required: true
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
  official_website: https://atvadventurescostadelsol.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'ATV Adventures: quad and buggy tour operator, about 18 min on foot or 4 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: 'ATV Adventures is a quad and buggy tour operator at C. la Higuera, 26, 29651 Las Lagunas de Mijas, Málaga. From Casa de la Familia it is about 18 minutes on foot (1.37 km, Google''s walking route) or about 4 minutes by car (Google route check, Saturday 10:00). Its own website (FAQ, in Spanish): a valid type-B car licence is needed to drive a quad or buggy; passengers need no licence. Children can ride as passengers: in buggies from 4 years, on quads from 6 years. All quads and buggies are two-seaters. Tours of 1, 2 and 3 hours plus a sunset tour; the site title says from €80. Closed-toe shoes are compulsory for driver and passenger. Advance online booking is required.'
seo_title: ATV Adventures, Mijas | CalleMilano draft record
seo_description: 'Draft record for ATV Adventures (Mijas): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'ATV Adventures | Rutas en Quad y Buggy en Málaga' at C. la Higuera, 26, 29651 Las Lagunas de Mijas, Málaga, España (36.5410031,-4.6583355), business status OPERATIONAL, website https://atvadventurescostadelsol.com/.
  source_url: https://maps.google.com/?cid=17915332558806491457
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia, description_long (walking time)
  claim: 'From Casa de la Familia: 4 min by car (1.44 km, Saturday 10:00 predicted traffic) and 18 min on foot (1.37 km).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5410031%2C-4.6583355&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00, and WALK (https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5410031%2C-4.6583355&travelmode=walking). Google's walking route says nothing about pavements, crossings or whether it suits children.
- field: booking_required, description_long, age rules
  claim: 'Own FAQ: type-B licence to drive; passengers need none; children as passengers from 4 in buggies and from 6 on quads; all vehicles two-seaters; tours 1, 2, 3 h and sunset; closed footwear for driver and passenger; advance booking required. Page title: "Desde 80 €".'
  source_url: https://atvadventurescostadelsol.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: high
  notes: Homepage FAQ quoted via Firecrawl (direct-quote mode) on 2026-11-02 (page modified 2026-10-25). The "from €80" figure is from the page title only.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  description: Age groups and family scores are not assessed; energy_level Medium is an editorial estimate from the type of place.
  retryable: true
  owner: human_editor
- code: prices_not_detailed
  severity: info
  fields:
  - cost_level
  - visit_information
  description: Only a "from €80" headline price was seen; per-tour prices were not checked.
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: '2026-11-02'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
