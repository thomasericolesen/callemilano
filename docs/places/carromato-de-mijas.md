---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-CARROMATO-DE-MIJAS-001
slug: carromato-de-mijas
name: Carromato de Mijas
category: City
tags:
- Museum
- Rainy day
coordinates:
  latitude: 36.595234999999995
  longitude: -4.637379
  purpose: venue
  label: Carromato de Mijas, Av. del Compás, 22, 29650 Mijas, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJZ3iizfrjcg0RUczpzkIGrho, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=1922480974942817361
external_ids:
  google_place_id: ChIJZ3iizfrjcg0RUczpzkIGrho
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 23 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Carromato de Mijas, Av. del Compás, 22, 29650 Mijas, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.595234999999995,-4.637379); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.595234999999995%2C-4.637379&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 23 min, 11.6 km. One predicted sample.'
age_groups:
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: medium
  children: high
  young_adults: low
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
food_available: unknown
cost_level: Unknown
visit_information:
  schedule: Jan-Mar, Nov-Dec 10:00-18:00; Apr-Jun, Oct 10:00-20:00; Jul-Sep 10:00-21:00 (own website, 2026-11-15). No closing days stated.
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: http://www.carromatodemijas.org/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Carromato de Mijas: museum of miniatures in Mijas Pueblo, about 23 min by car.'
description_long: 'Carromato de Mijas is a museum of miniatures on Avenida del Compás in Mijas Pueblo. Its own site gives opening hours by season: 10:00-18:00 in January-March, November and December; 10:00-20:00 in April-June and October; 10:00-21:00 in July-September (checked 2026-11-15). No closing days, prices or children''s information are given. About 23 minutes by car from Casa de la Familia.'
seo_title: Carromato de Mijas, Mijas | CalleMilano draft record
seo_description: 'Draft record for Carromato de Mijas (Mijas): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Carromato de Mijas' at Av. del Compás, 22, 29650 Mijas, Málaga, España (36.595234999999995,-4.637379), status OPERATIONAL, type art_museum.
  source_url: https://maps.google.com/?cid=1922480974942817361
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 23 min by car (11.6 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.595234999999995%2C-4.637379&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule, description_long
  claim: '''Museo de miniaturas en Mijas''; ''ENERO, FEBRERO, MARZO, NOVIEMBRE Y DICIEMBRE: 10:00H A 18:00H'' / ''ABRIL, MAYO, JUNIO Y OCTUBRE: 10:00H A 20:00H'' / ''JULIO, AGOSTO Y SEPTIEMBRE: 10:00H A 21:00H''; ''Avenida del Compás, s/n 29650 Mijas-Pueblo''.'
  source_url: http://www.carromatodemijas.org/
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
- field: tags, age_groups, family_score, energy_level
  claim: 'Editor decision 2026-11-15 on the tags list: tags = Museum, Rainy day; age_groups = Children (7-12), Young adults, Seniors; family_score = small_children medium, children high, young_adults low, seniors medium; energy_level = Low.'
  source_url: https://claude.ai/artifact/VoHiKgGvqiiP3YA66KP3s5
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-15
  confidence: high
  notes: The editor's own judgement; answers stored in collection tags_2026_11_15.
review_issues:
- code: not_found_first_attempt
  severity: warning
  fields:
  - cost_level
  description: 'First source attempt 2026-11-15 found no official answer for: entry price. Value left unknown; check before visiting.'
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
