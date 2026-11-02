---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-PLAYAMAR-001
slug: playamar
name: Playamar
category: Beaches
tags:
- Beach
coordinates:
  latitude: 36.6306
  longitude: -4.4887
  purpose: representative_point
  label: Google Maps marker 'Playamar' (owner-read); not a parking point
  source: Google Maps marker, read by Eric Olesen (owner) 2026-07-18; accepted as the record's place point by the owner on 2026-11-01 (decision 1). Not an official visitor point.
  checked_at: '2026-07-18'
google_maps_url: https://maps.google.com/?cid=13326802808353720739
external_ids:
  google_place_id: ChIJKQx4_ub7cg0Rowmat4tQ8rg
municipality: Torremolinos
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 27 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Playamar, Torremolinos, Málaga, Spain (Google Maps marker, not a parking point)
  source: Google Routes API computeRoutes, run 2026-11-01 from the project origin (36.5356875, -4.6626875); destination = record coordinates (36.6306,-4.4887); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6306%2C-4.4887&travelmode=driving
  checked_at: '2026-11-01'
  note: 'Routes API figure: 27 min with predicted Saturday 10:00 traffic (28 min without traffic), 24.0 km via AP-7; an avoid-tolls run gave 27 min. One predicted sample, not the Google Maps app''s main figure; traffic and season change the time. Previous value 28 min (2026-07-18): Google Maps, measured by Eric Olesen (owner). Batch: data/route-checks-2026-11-01-local.csv. Owner decision 2026-11-01: the owner-read marker is accepted as the place point, so this route check stands.'
age_groups:
- Small children (0-6)
family_score:
  small_children: medium
  children: unknown
  young_adults: unknown
  seniors: unknown
energy_level: Low
seasonality:
- Spring
- Summer
- Autumn
accessibility:
  overall: 'Torremolinos'' official tourism site (page updated 2026-05-11) states that its four main beaches, including Playamar, have extra-wide wooden walkways from the promenade to the bathing area, an assisted-bathing point staffed by specialised personnel with amphibious chairs and crutches (appointment by phone 697 61 04 60), and fully accessible toilets, showers and changing rooms plus shaded areas for people with disabilities. Bathing season: Easter week (Friday before Palm Sunday to Easter Monday) and 1 June-30 September. The per-beach accessibility map embedded on the page shows adapted toilets, accessible showers and reserved parking.'
  mobility:
    route: Extra-wide wooden walkways from the promenade to the bathing area (official tourism page).
    wheelchair_route: unknown
    facilities: Assisted-bathing point with amphibious chairs and crutches (by appointment, bathing season); accessible toilets, showers and changing rooms; shaded area for people with disabilities.
  sensory:
    notes: unknown
  accessible_toilets: 'yes'
  source: https://turismotorremolinos.es/es/descubre/playas/playas-accesibles/
  checked_at: '2026-11-01'
  confidence: medium
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
toilets_available: 'yes'
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
- id: ES-AND-MAL-MORROFINO-001
  relationship: nearby
  note: 'Place to eat: Morrofino.'
description_short: 'Playamar, Torremolinos: Blue Flag 2026. Character (subjective): Developed (Danish: Tilrettelagt). Draft; facts being checked against official sources.'
description_long: 'Playamar (Torremolinos). Blue Flag 2026 (used as proxy for water quality). Official tourism data (spain.info, Turespaña; undated, read 2026-11-02): dark sand, moderate waves, about 1,000 x 50 m, high occupancy, urban; toilets, showers and parasol/sunbed hire are listed. Places to eat: see the linked record for Morrofino. Rocks: not confirmed either way (not mentioned in the sources reviewed, and not known to the owner). Official tourism source (checked 2026-11-01): accessible walkways, a staffed assisted-bathing point and accessible toilets; bathing season Easter week and 1 June-30 September. Character: Developed (Danish: Tilrettelagt) - subjective assessment from the sources'' description of urbanisation, not an official category. Family suitability and energy level are subjective estimates and not safety advice.'
seo_title: Playamar, Torremolinos | CalleMilano draft record
seo_description: Draft record for Playamar beach (Torremolinos). Facts are being checked against official sources.
images: []
evidence:
- field: description_long (Blue Flag 2026)
  claim: '''Playamar'' is on the ADEAC, ''Relación Playas Galardonadas 2026''.'
  source_url: https://www.banderaazul.org/sites/default/files/2026/Rueda-de-prensa-2026/Relaci%C3%B3n%20Playas%20Galardonadas%202026.pdf
  source_type: official_tourism
  checked_at: '2026-10-29'
  checked_by: claude-sonnet-5-5 (draft 2026-10-29)
  confidence: high
  notes: '[verified] Checked against ADEAC''s official list (edition 2026-2027) on 2026-10-29, read via a WebFetch summary (PDF not read page by page). Matches the snapshot check of 2026-10-15. Municipality grouping read directly from the list. Awards are conditional on continued compliance and verification during 2027 (list footnote). source_type is the nearest schema value: ADEAC is the national Blue Flag operator and the schema has no certification source type (editor decision).'
- field: description_long (Blue Flag 2026)
  claim: El Español's 2026 Blue Flag article lists the beach under Torremolinos. Article lists 'Playamar' under Torremolinos.
  source_url: https://www.elespanol.com/malaga/20260505/malaga-vuelve-tenir-azul-costa-playas-provincia-cuentan-bandera-sello-calidad/1003744233872_0.html
  source_type: secondary
  checked_at: '2026-10-29'
  checked_by: claude-sonnet-5-5 (draft 2026-10-29)
  confidence: medium
  notes: '[partial] Corroborating source, read via a WebFetch summary on 2026-10-29 (article not read in full). Supports the ADEAC check; does not replace it.'
- field: driving_time_from_casa_de_la_familia
  claim: 'One-way drive from Casa de la Familia to Playamar, Torremolinos, Málaga, Spain (Google Maps marker, not a parking point): 27 min, 24.0 km (Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6306%2C-4.4887&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Claude (Routes API batch 2026-11-01)
  confidence: medium
  notes: Google Routes API computeRoutes; destination = record coordinates (36.6306,-4.4887). Predicted-traffic estimate for one departure time; the local_30km rule uses the Google Maps app's main figure.
- field: toilets_available, accessibility
  claim: Playamar has wide walkways to the shore, a staffed assisted-bathing point with amphibious chairs, and accessible toilets, showers and changing rooms; bathing season Easter week and 1 June-30 September.
  source_url: https://turismotorremolinos.es/es/descubre/playas/playas-accesibles/
  source_type: official_tourism
  checked_at: '2026-11-01'
  checked_by: Claude (beach fact check 2026-11-01)
  confidence: medium
  notes: Turismo de Torremolinos, 'Playas Accesibles', modified 2026-05-11, read 2026-11-01. The four-beach statement is general; the per-beach Google My Maps embedded on the page (published 2019-2021) show adapted toilets at this beach. Confidence medium because the per-beach maps are older than the season.
- field: coordinates
  claim: The owner accepts the Google Maps marker coordinates read on 2026-07-18 as this beach's place point.
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/approval-decisions-2026-11-01.md
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: high
  notes: Owner decision 1, 2026-11-01, given on the approval checklist and recorded in docs/approval-decisions-2026-11-01.md. This is an editor decision, not an external fact source; source_type is the nearest schema value.
- field: seasonality
  claim: Beach seasonality is Spring, Summer and Autumn (same for all local beaches).
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/approval-decisions-2026-11-01.md
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: high
  notes: Owner decision 3, 2026-11-01, given on the approval checklist and recorded in docs/approval-decisions-2026-11-01.md. This is an editor decision, not an external fact source; source_type is the nearest schema value. Editorial judgment of the bathing season; lifeguard periods in the description are the dated facts.
- field: parking, transport_options, dog_friendly, cost_level, booking_required, food_available, visit_information
  claim: 'Parking, transport, dogs, cost, booking and food are deliberately left unknown for beaches: adults look these up themselves.'
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/approval-decisions-2026-11-01.md
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: high
  notes: Owner decision 5, 2026-11-01, given on the approval checklist and recorded in docs/approval-decisions-2026-11-01.md. This is an editor decision, not an external fact source; source_type is the nearest schema value. Replaces review issue practical_details_out_of_scope (owner decision of 2026-11-01 on the beach fact check, confirmed as decision 5).
- field: google_maps_url, external_ids
  claim: Google Places lists 'Playamar' (Playamar, España), place ID ChIJKQx4_ub7cg0Rowmat4tQ8rg, about 4 m from the record coordinates.
  source_url: https://maps.google.com/?cid=13326802808353720739
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (Places API lookup 2026-11-02)
  confidence: high
  notes: Google Places API (New) searchText/searchNearby on 2026-11-02. Maps establishes identity and position only, not facilities or suitability.
- field: description_long (sand, size, waves, occupancy, services)
  claim: 'Playamar: sand, dark, moderate waves, 1000 x 50 m, high occupancy, urban; services: parasol/sunbed/water-craft hire, toilets, showers, footwash, tourist office.'
  source_url: https://www.spain.info/es/playa/playamar/
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (official beach data 2026-11-02)
  confidence: medium
  notes: Turespaña's official tourism portal; beach data based on the national beach guide, undated. Read via Firecrawl on 2026-11-02. Replaces the unsourced snapshot entries for sand, size, children, facilities and restaurants, which were removed together with their unsourced claims in the description.
review_issues:
- code: subjective_assessments_need_human_review
  severity: warning
  fields:
  - family_score
  - age_groups
  - energy_level
  - description_long
  description: 'Character (Natural/Mixed/Developed) and family suitability are subjective. Rule used (confirmed by the owner 2026-10-29): small_children=medium only where the snapshot has an explicit child or family statement, otherwise unknown; no other audience rated. energy_level is an editorial estimate for a required field.'
  retryable: false
  owner: human_editor
- code: rocks_not_verified
  severity: warning
  fields:
  - description_long
  description: Absence of any mention of rocks is not confirmation, and the owner does not know (decision 4, 2026-11-01). The project criterion excludes beaches with rocks; a visit or an independent source is needed.
  retryable: true
  owner: fact_check
- code: name_confusion_playamarina
  severity: info
  fields:
  - name
  - slug
  description: Not the same place as 'El Charcón-Playamarina' in Mijas (docs/launch-candidates.md). This record is Playamar in Torremolinos.
  retryable: false
  owner: human_editor
created_at: '2026-10-29'
updated_at: '2026-11-02'
last_verified: '2026-10-29'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
