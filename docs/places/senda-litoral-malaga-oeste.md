---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-SENDA-LITORAL-MALAGA-OESTE-001
slug: senda-litoral-malaga-oeste
name: Senda Litoral (Málaga west)
category: Excursions
tags: []
coordinates:
  latitude: 36.689676
  longitude: -4.4423341999999995
  purpose: representative_point
  label: Senda Litoral de Malaga, Paseo Marítimo Antonio Banderas, 28, Carretera de Cádiz, 29004, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJfSHnarD5cg0RA3PSb5XNtJo, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=11147761019358704387
external_ids:
  google_place_id: ChIJfSHnarD5cg0RA3PSb5XNtJo
municipality: Málaga
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 30 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Senda Litoral de Malaga, Paseo Marítimo Antonio Banderas, 28, Carretera de Cádiz, 29004, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.689676,-4.4423341999999995); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.689676%2C-4.4423341999999995&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 30 min, 31.5 km. One predicted sample.'
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
  contact: null
related_places: []
description_short: 'Senda Litoral (Málaga west): the coastal path along Málaga''s western seafront, about 30 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Senda Litoral (Málaga west) is the coastal path along Málaga's western seafront. About 30 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Other facts have not been checked yet.
seo_title: Senda Litoral (Málaga west), Málaga | CalleMilano draft record
seo_description: 'Draft record for Senda Litoral (Málaga west) (Málaga): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Senda Litoral de Malaga' at Paseo Marítimo Antonio Banderas, 28, Carretera de Cádiz, 29004, Málaga, España (36.689676,-4.4423341999999995), status OPERATIONAL, type hiking_area.
  source_url: https://maps.google.com/?cid=11147761019358704387
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Places API (New). Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 30 min by car (31.5 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.689676%2C-4.4423341999999995&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
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
- code: source_covers_other_section
  severity: info
  fields:
  - description_long
  description: The Málaga council page found (Paseo Litoral, El Candado-La Araña) is the eastern seafront, not the western Senda Litoral at this record's point; it also gives conflicting lengths (2,500 m vs 4 km). Find a page for the western section.
  retryable: true
  owner: fact_check
- code: second_source_attempt_failed
  severity: warning
  fields:
  - description_long
  - visit_information
  description: 'Second source attempt 2026-11-13: only commercial guides and a 2014 PDF found, no current official page for the western section. No facts added. Proposed for the editor list (archive, or the owner confirms the section).'
  retryable: false
  owner: editor
created_at: '2026-11-02'
updated_at: '2026-11-13'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
