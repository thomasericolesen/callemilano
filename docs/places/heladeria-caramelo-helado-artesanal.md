---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-HELADERIA-CARAMELO-HELADO-ARTESANAL-001
slug: heladeria-caramelo-helado-artesanal
name: Heladería Caramelo Helado Artesanal
category: Restaurants
tags: []
coordinates:
  latitude: 36.5433832
  longitude: -4.6285495
  purpose: venue
  label: Heladería Caramelo Helado Artesanal, Calle Miguel Bueno, 2, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJqfz6j_fjcg0RBvTAP5rr-kw, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=5547004938787288070
external_ids:
  google_place_id: ChIJqfz6j_fjcg0RBvTAP5rr-kw
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 11 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Heladería Caramelo Helado Artesanal, Calle Miguel Bueno, 2, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5433832,-4.6285495); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5433832%2C-4.6285495&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 11 min, 4.6 km. One predicted sample.'
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
  schedule: Monday-Thursday 14:00-01:00; Friday-Sunday 11:00-01:30 (own website, 2026-11-15).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: https://www.heladeriacaramelo.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Heladería Caramelo: artisan ice-cream shop with savoury snacks in Fuengirola, open until late, about 11 min by car.'
description_long: Heladería Caramelo is an artisan ice-cream shop at Calle Miguel Bueno 2 in Fuengirola that also serves savoury snacks and takes table bookings. Open Monday-Thursday 14:00-01:00 and Friday-Sunday 11:00-01:30 (own website, checked 2026-11-15). Prices are not published. About 11 minutes by car from Casa de la Familia.
seo_title: Heladería Caramelo Helado Artesanal, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Heladería Caramelo Helado Artesanal (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Heladería Caramelo Helado Artesanal' at Calle Miguel Bueno, 2, 29640 Fuengirola, Málaga, España (36.5433832,-4.6285495), status OPERATIONAL, type ice_cream_shop.
  source_url: https://maps.google.com/?cid=5547004938787288070
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 11 min by car (4.6 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5433832%2C-4.6285495&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule, description_long
  claim: '''Heladería Artesanal en Fuengirola''; ''Bocados Salados''; ''Lunes a Jueves 14h-1h / Viernes, sábado y domingo 11h-1:30h''; ''Calle Miguel Bueno 2, Fuengirola 29640''.'
  source_url: https://www.heladeriacaramelo.com/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
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
  description: 'First source attempt 2026-11-15 found no official answer for: prices. Value left unknown; check before visiting.'
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
