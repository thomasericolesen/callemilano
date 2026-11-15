---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-CAC-MIJAS-CENTRO-DE-ARTE-CONTEMPORANEO-001
slug: cac-mijas-centro-de-arte-contemporaneo
name: CAC Mijas (Centro de Arte Contemporáneo)
category: City
tags: []
coordinates:
  latitude: 36.596326999999995
  longitude: -4.638059999999999
  purpose: venue
  label: CAC Mijas (Centro de Arte Contemporáneo), C. Málaga, 28, 29650 Mijas, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJoSv6Pfvjcg0RbhpiHn-aoI4, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=10277384220420741742
external_ids:
  google_place_id: ChIJoSv6Pfvjcg0RbhpiHn-aoI4
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 21 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: CAC Mijas (Centro de Arte Contemporáneo), C. Málaga, 28, 29650 Mijas, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.596326999999995,-4.638059999999999); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.596326999999995%2C-4.638059999999999&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 21 min, 11.3 km. One predicted sample.'
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
cost_level: €
visit_information:
  schedule: Monday-Saturday 10:30-14:00; Sunday closed (own website, footer dated 2019; confirm before visiting).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own website: entry 3 €; under 5 free (page footer dated 2019).'
  cost_checked_at: '2026-11-15'
links:
  official_website: http://cacmijas.info/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'CAC Mijas: contemporary art centre in Mijas Pueblo with works by Picasso and Dalí, about 21 min by car.'
description_long: CAC Mijas (Centro de Arte Contemporáneo) on Calle Málaga 28 in Mijas Pueblo shows works by Picasso and Dalí. Its own site gives Monday-Saturday 10:30-14:00, closed Sundays, entry 3 €, and free entry for children under 5; it also mentions children's workshops. The site footer is dated 2019, so hours and price should be confirmed before visiting (checked 2026-11-15). About 21 minutes by car from Casa de la Familia.
seo_title: CAC Mijas (Centro de Arte Contemporáneo), Mijas | CalleMilano draft record
seo_description: 'Draft record for CAC Mijas (Centro de Arte Contemporáneo) (Mijas): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'CAC Mijas (Centro de Arte Contemporáneo)' at C. Málaga, 28, 29650 Mijas, Málaga, España (36.596326999999995,-4.638059999999999), status OPERATIONAL, type art_museum.
  source_url: https://maps.google.com/?cid=10277384220420741742
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 21 min by car (11.3 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.596326999999995%2C-4.638059999999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule, cost_level
  claim: '''Centro de Arte Contemporáneo''; ''Obras de Picasso y Dalí''; ''C/ Málaga, 28. Mijas''; ''Lunes a Sábado. 10:30h a 14:00h'' / ''Domingos CERRADO.''; ''Entrada 3,00 €'' / ''Menores de 5 años gratis''; ''talleres infantiles''.'
  source_url: http://cacmijas.info/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: low
  notes: 'Footer ''© 2019'': the page may be old.'
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
- code: source_may_be_outdated
  severity: warning
  fields:
  - visit_information.schedule
  - cost_level
  description: Own website footer is dated 2019; confirm hours and price at the next review.
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
