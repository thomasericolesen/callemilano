---
schema_version: 1.0.0
status: archived
id: ES-AND-MAL-RIO-GRANDE-COIN-001
slug: rio-grande-coin
name: Río Grande (Coín)
category: Nature
tags: []
coordinates:
  latitude: 36.688942
  longitude: -4.787760899999999
  purpose: representative_point
  label: Río grande, 29100 Coín, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJKxFW0M3dcg0Rlfe0zExsH4M, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=9448389620354316181
external_ids:
  google_place_id: ChIJKxFW0M3dcg0Rlfe0zExsH4M
municipality: Coín
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 40 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Río grande, 29100 Coín, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.688942,-4.787760899999999); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.688942%2C-4.787760899999999&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 40 min, 31.8 km. One predicted sample.'
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
description_short: 'Río Grande (Coín): a river path near Coín, about 40 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Río Grande (Coín) is a river path near Coín. About 40 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Other facts have not been checked yet.
seo_title: Río Grande (Coín), Coín | CalleMilano draft record
seo_description: 'Draft record for Río Grande (Coín) (Coín): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Río grande' at 29100 Coín, Málaga, España (36.688942,-4.787760899999999), status OPERATIONAL, type hiking_area.
  source_url: https://maps.google.com/?cid=9448389620354316181
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Places API (New). Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 40 min by car (31.8 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.688942%2C-4.787760899999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children high, children high, young_adults high, seniors high; energy_level Medium. Owner note (Danish): ''Visse stier er svært fremkommelige med klapvogn''.'
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
- code: no_official_source
  severity: warning
  fields:
  - description_long
  - visit_information
  description: No official page (Coín council, Junta de Andalucía) found for the Río Grande path on 2026-11-02. Bathing spots and safety stay undescribed until a source is found.
  retryable: true
  owner: fact_check
- code: second_source_attempt_failed
  severity: warning
  fields:
  - description_long
  - visit_information
  description: 'Second source attempt 2026-11-13: no official page for this path found; the only matches were the PR-A 496 Coín-Guadalhorce route and the Guadalhorce footbridge, which may be different places. No facts added. Proposed for the editor list (archive, or the owner confirms the exact path).'
  retryable: false
  owner: editor
created_at: '2026-11-02'
updated_at: '2026-11-13'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision:
  decision: archived
  reviewer: Eric Olesen (editor-of-record)
  date: '2026-11-13'
  notes: 'Owner decision 2026-11-13 on the editor list (https://claude.ai/artifact/EpwDTtUv1wLvgu1u5Yy5Jn): archive (no official page for the path found after two source attempts); we already have enough places. Kept as archive; the ID stays allocated and must not be reused.'
redirects: []
---
