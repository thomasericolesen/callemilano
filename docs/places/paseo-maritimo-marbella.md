---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-PASEO-MARITIMO-MARBELLA-001
slug: paseo-maritimo-marbella
name: Paseo Marítimo de Marbella
category: Excursions
tags: []
coordinates:
  latitude: 36.507252799999996
  longitude: -4.8971162
  purpose: representative_point
  label: Paseo Maritimo De Marbella, P.º Marítimo, 2, 29602 Marbella, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ22WccAAocw0RnQKI29MdqCI, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=2497278789135368861
external_ids:
  google_place_id: ChIJ22WccAAocw0RnQKI29MdqCI
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 37 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Paseo Maritimo De Marbella, P.º Marítimo, 2, 29602 Marbella, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.507252799999996,-4.8971162); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.507252799999996%2C-4.8971162&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 37 min, 27.4 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: high
  children: high
  young_adults: high
  seniors: high
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
related_places:
- marbella-old-town
- playa-de-nagueles
description_short: 'Paseo Marítimo de Marbella: Marbella''s seafront promenade, about 37 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Paseo Marítimo de Marbella is Marbella's seafront promenade. About 37 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Other facts have not been checked yet.
seo_title: Paseo Marítimo de Marbella, Marbella | CalleMilano draft record
seo_description: 'Draft record for Paseo Marítimo de Marbella (Marbella): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Paseo Maritimo De Marbella' at P.º Marítimo, 2, 29602 Marbella, Málaga, España (36.507252799999996,-4.8971162), status OPERATIONAL, type scenic_spot.
  source_url: https://maps.google.com/?cid=2497278789135368861
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Places API (New). Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 37 min by car (27.4 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.507252799999996%2C-4.8971162&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children high, children high, young_adults high, seniors high; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
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
- code: source_covers_other_section
  severity: info
  fields:
  - description_long
  description: The Turismo Marbella page found (https://turismo.marbella.es/servicios/ruta-fotografica-de-marbella/paseo-maritimo-de-san-pedro-alcantara.html) covers the San Pedro Alcántara section, not the Marbella town section at this record's point. Find the town-section page before writing the description.
  retryable: true
  owner: fact_check
- code: second_source_attempt_failed
  severity: warning
  fields:
  - description_long
  - visit_information
  description: 'Second source attempt 2026-11-13: no official page covering this section found; guides disagree on length (about 5 vs 6 km) and are not recorded. No facts added. Proposed for the editor list (archive, or the owner decides which section the record covers).'
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
