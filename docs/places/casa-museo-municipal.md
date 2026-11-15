---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-CASA-MUSEO-MUNICIPAL-001
slug: casa-museo-municipal
name: Casa Museo Municipal
category: City
tags: []
coordinates:
  latitude: 36.5952307
  longitude: -4.6385622
  purpose: venue
  label: Casa Museo Municipal, Pl. de la Libertad, 2, 29650 Mijas, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJiXT5Nfvjcg0RvzD1cwrZIgE, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=81866382164439231
external_ids:
  google_place_id: ChIJiXT5Nfvjcg0RvzD1cwrZIgE
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 21 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Casa Museo Municipal, Pl. de la Libertad, 2, 29650 Mijas, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5952307,-4.6385622); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5952307%2C-4.6385622&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 21 min, 11.4 km. One predicted sample.'
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
  schedule: Monday-Sunday 10:00-14:00 and 15:00-19:00 (Turismo Mijas, 2026-11-15).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Turismo Mijas 2026-11-15: entry 1 €.'
  cost_checked_at: '2026-11-15'
links:
  official_website: null
  booking: null
  visitor_information: null
  transport: null
  contact: 952 59 03 80
related_places: []
description_short: 'Casa Museo (Museo Histórico-Etnológico) in Mijas Pueblo: local history museum, entry 1 €, about 21 min by car.'
description_long: The Casa Museo, Mijas' municipal history and ethnology museum, is on Plaza de la Libertad in Mijas Pueblo. Mijas' official tourism site gives Monday-Sunday 10:00-14:00 and 15:00-19:00, entry 1 €, phone 952 59 03 80 (checked 2026-11-15). About 21 minutes by car from Casa de la Familia.
seo_title: Casa Museo Municipal, Mijas | CalleMilano draft record
seo_description: 'Draft record for Casa Museo Municipal (Mijas): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Casa Museo Municipal' at Pl. de la Libertad, 2, 29650 Mijas, Málaga, España (36.5952307,-4.6385622), status OPERATIONAL, type museum.
  source_url: https://maps.google.com/?cid=81866382164439231
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes. Editor: Casa Museo Municipal and Museo Histórico-Etnológico are the same museum; keep this record only.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 21 min by car (11.4 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5952307%2C-4.6385622&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule, cost_level, links.contact
  claim: '''Museo histórico-etnológico - Casa Museo''; ''Horario: Lunes a Domingo, de 10:00H a 14:00H - de 15:00H a 19:00H''; ''Dirección: Plaza de la Libertad, Mijas''; ''Entrada: 1 €''; ''Contacto: 952 59 03 80''.'
  source_url: https://turismo.mijas.es/es/cultura/museos/museo-historico-y-etnologico
  source_type: official_tourism
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
created_at: '2026-11-15'
updated_at: '2026-11-15'
last_verified: '2026-11-15'
last_reviewed_at: '2026-11-15'
next_review_at: '2027-04-15'
review_decision: null
redirects: []
---
