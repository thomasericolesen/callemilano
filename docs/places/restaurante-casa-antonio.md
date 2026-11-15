---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-RESTAURANTE-CASA-ANTONIO-001
slug: restaurante-casa-antonio
name: Restaurante Casa Antonio
category: Restaurants
tags: []
coordinates:
  latitude: 36.5354868
  longitude: -4.6282267
  purpose: venue
  label: Restaurante Casa Antonio, Cam. Condesa, 3, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ0Q_gJyHjcg0RdydZ-FmwYnM, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=8314401762544527223
external_ids:
  google_place_id: ChIJ0Q_gJyHjcg0RdydZ-FmwYnM
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 12 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante Casa Antonio, Cam. Condesa, 3, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5354868,-4.6282267); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5354868%2C-4.6282267&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 12 min, 4.8 km. One predicted sample.'
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
  schedule: Tuesday-Thursday 13:00-16:30 and 19:30-22:30; Friday-Saturday 13:00-16:30 and 19:30-23:00; Sunday 13:00-17:00; closed Monday (own Instagram, 2026-11-15).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: http://www.instagram.com/casa_antonio_restaurante
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Restaurante Casa Antonio: Mediterranean restaurant in Fuengirola with a fully gluten-free kitchen, about 12 min by car.'
description_long: 'Restaurante Casa Antonio is a Mediterranean restaurant at Camino Condesa 3 in Fuengirola; its own Instagram profile says the whole kitchen is gluten-free (''100% SIN GLUTEN''). Hours on the profile (checked 2026-11-15): Tuesday-Thursday 13:00-16:30 and 19:30-22:30, Friday-Saturday 13:00-16:30 and 19:30-23:00, Sunday 13:00-17:00, closed Monday. The profile mentions one hour of parking. Prices and children''s facilities were not confirmed from text. About 12 minutes by car from Casa de la Familia.'
seo_title: Restaurante Casa Antonio, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Restaurante Casa Antonio (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Restaurante Casa Antonio' at Cam. Condesa, 3, 29640 Fuengirola, Málaga, España (36.5354868,-4.6282267), status OPERATIONAL, type restaurant.
  source_url: https://maps.google.com/?cid=8314401762544527223
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 12 min by car (4.8 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5354868%2C-4.6282267&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule, description_long
  claim: 'Instagram bio: ''Cocina Mediterránea • 100% SIN GLUTEN''; ''M–J 13–16:30 | 19:30–22:30 | V–S 13–16:30 | 19:30–23:00 | D 13–17 | L ❌''; ''C/ Camino Condesa, 3, Fuengirola 29640''; ''🚗 1h parking''.'
  source_url: https://www.instagram.com/casa_antonio_restaurante
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
  notes: Read in Claude in Chrome, signed in. Highlight 'Rincón infantil' exists but was not opened. Menu PDF (15 pages) could not be read without poppler.
- field: status
  claim: 'Lifted needs_fact_check -> needs_editorial_review: official or own-venue evidence for the core facts, no blocking or facts_not_checked issue (editor workflow, level A).'
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/AGENTS.md
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (main session)
  confidence: high
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
- code: not_found_first_attempt
  severity: warning
  fields:
  - cost_level
  - visit_information.cost_basis
  description: 'First source attempt 2026-11-15 found no official answer for: prices (menu PDF unreadable; retry with poppler) and the ''Rincón infantil'' highlight. Value left unknown; check before visiting.'
  retryable: true
  owner: fact_check
created_at: '2026-11-15'
updated_at: '2026-11-15'
last_verified: '2026-11-15'
last_reviewed_at: '2026-11-15'
next_review_at: '2027-04-15'
review_decision: null
redirects: []
---
