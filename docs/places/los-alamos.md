---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-LOS-ALAMOS-001
slug: los-alamos
name: Los Álamos
category: Beaches
tags:
- Beach
coordinates:
  latitude: 36.6349
  longitude: -4.4856
  purpose: representative_point
  label: Google Maps marker 'Playa de los Álamos' (owner-read); not a parking point
  source: Google Maps marker, read by Eric Olesen (owner) 2026-07-18; accepted as the record's place point by the owner on 2026-11-01 (decision 1). Not an official visitor point.
  checked_at: '2026-07-18'
google_maps_url: null
external_ids: {}
municipality: Torremolinos
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 28 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Los Álamos, Torremolinos, Málaga, Spain (Google Maps marker, not a parking point)
  source: Google Routes API computeRoutes, run 2026-11-01 from the project origin (36.5356875, -4.6626875); destination = record coordinates (36.6349,-4.4856); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6349%2C-4.4856&travelmode=driving
  checked_at: '2026-11-01'
  note: 'Routes API figure: 28 min with predicted Saturday 10:00 traffic (29 min without traffic), 24.8 km via AP-7; an avoid-tolls run gave 28 min. One predicted sample, not the Google Maps app''s main figure; traffic and season change the time. Previous value 30 min (2026-07-18): Google Maps, measured by Eric Olesen (owner). Batch: data/route-checks-2026-11-01-local.csv. Owner decision 2026-11-01: the owner-read marker is accepted as the place point, so this route check stands.'
age_groups: []
family_score:
  small_children: unknown
  children: unknown
  young_adults: unknown
  seniors: unknown
energy_level: Low
seasonality:
- Spring
- Summer
- Autumn
accessibility:
  overall: 'Torremolinos'' official tourism site (page updated 2026-05-11) states that its four main beaches, including Los Álamos, have extra-wide wooden walkways from the promenade to the bathing area, an assisted-bathing point staffed by specialised personnel with amphibious chairs and crutches (appointment by phone 697 61 04 60), and fully accessible toilets, showers and changing rooms plus shaded areas for people with disabilities. Bathing season: Easter week (Friday before Palm Sunday to Easter Monday) and 1 June-30 September. The per-beach accessibility map embedded on the page shows adapted toilets, accessible showers and reserved parking.'
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
description_short: 'Los Álamos, Torremolinos: Blue Flag 2026. Character (subjective): Developed (Danish: Tilrettelagt). Draft from a dated secondary-source snapshot; not fact-checked.'
description_long: 'Los Álamos (Torremolinos). Blue Flag 2026 (used as proxy for water quality). Fine sand (sources disagree on the length). Described as a younger, livelier atmosphere. Eating places named in tourist sources (opening hours not checked; many beach bars close out of season): Beach bars and restaurants. Nearby: Paseo Maritimo. Rocks: not confirmed either way (not mentioned in the sources reviewed, and not known to the owner). Official tourism source (checked 2026-11-01): accessible walkways, a staffed assisted-bathing point and accessible toilets; bathing season Easter week and 1 June-30 September. Character: Developed (Danish: Tilrettelagt) - subjective assessment from the sources'' description of urbanisation, not an official category. Family suitability and energy level are subjective estimates and not safety advice.'
seo_title: Los Álamos, Torremolinos | CalleMilano draft record
seo_description: Draft record for Los Álamos beach (Torremolinos). Based on a dated secondary-source snapshot; facts are under verification.
images: []
evidence:
- field: description_long (Blue Flag 2026)
  claim: '''Los Álamos'' is on the ADEAC, ''Relación Playas Galardonadas 2026''.'
  source_url: https://www.banderaazul.org/sites/default/files/2026/Rueda-de-prensa-2026/Relaci%C3%B3n%20Playas%20Galardonadas%202026.pdf
  source_type: official_tourism
  checked_at: '2026-10-29'
  checked_by: claude-sonnet-5-5 (draft 2026-10-29)
  confidence: high
  notes: '[verified] Checked against ADEAC''s official list (edition 2026-2027) on 2026-10-29, read via a WebFetch summary (PDF not read page by page). Matches the snapshot check of 2026-10-15. Municipality grouping read directly from the list. Awards are conditional on continued compliance and verification during 2027 (list footnote). source_type is the nearest schema value: ADEAC is the national Blue Flag operator and the schema has no certification source type (editor decision).'
- field: description_long (Blue Flag 2026)
  claim: El Español's 2026 Blue Flag article lists the beach under Torremolinos. Article lists 'Los Álamos' under Torremolinos.
  source_url: https://www.elespanol.com/malaga/20260505/malaga-vuelve-tenir-azul-costa-playas-provincia-cuentan-bandera-sello-calidad/1003744233872_0.html
  source_type: secondary
  checked_at: '2026-10-29'
  checked_by: claude-sonnet-5-5 (draft 2026-10-29)
  confidence: medium
  notes: '[partial] Corroborating source, read via a WebFetch summary on 2026-10-29 (article not read in full). Supports the ADEAC check; does not replace it.'
- field: description_long (sand, size, waves, occupancy)
  claim: Fine sand (sources disagree on the length).
  source_url: null
  source_type: secondary
  checked_at: '2026-10-15'
  checked_by: strandoversigt-snapshot (Eric/Claude)
  confidence: low
  notes: '[unverified] Source per snapshot: per-beach source not recorded in snapshot. URL not recorded in the snapshot. Not rechecked 2026-10-29.'
- field: description_long (children, facilities, restaurants, experiences)
  claim: Described as a younger, livelier atmosphere. | Beach bars and restaurants. | Paseo Maritimo.
  source_url: null
  source_type: secondary
  checked_at: '2026-10-15'
  checked_by: strandoversigt-snapshot (Eric/Claude)
  confidence: low
  notes: '[unverified] Hotel-chain and tourist-site guides (Hoteles.net, Barcelo, Cargest, Mijas tourism and others), not independent. Opening hours and child-friendliness not checked.'
- field: driving_time_from_casa_de_la_familia
  claim: 'One-way drive from Casa de la Familia to Los Álamos, Torremolinos, Málaga, Spain (Google Maps marker, not a parking point): 28 min, 24.8 km (Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6349%2C-4.4856&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Claude (Routes API batch 2026-11-01)
  confidence: medium
  notes: Google Routes API computeRoutes; destination = record coordinates (36.6349,-4.4856). Predicted-traffic estimate for one departure time; the local_30km rule uses the Google Maps app's main figure.
- field: toilets_available, accessibility
  claim: Los Álamos has wide walkways to the shore, a staffed assisted-bathing point with amphibious chairs, and accessible toilets, showers and changing rooms; bathing season Easter week and 1 June-30 September.
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
review_issues:
- code: google_maps_url_missing
  severity: info
  fields:
  - google_maps_url
  description: No Maps link recorded on this draft.
  retryable: true
  owner: fact_check
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
- code: secondary_sources_unverified
  severity: warning
  fields:
  - description_long
  - toilets_available
  - accessibility
  - evidence
  description: 'Facilities, child-related statements and restaurant names come from tourist-site and hotel-chain guides (not independent). Opening hours not checked; many beach bars close out of season. Fact check 2026-11-01: lifeguard, toilet and accessibility claims checked against municipal/official sources where available (see evidence); beach-bar names, sand, depth and child-friendliness remain secondary.'
  retryable: true
  owner: fact_check
- code: source_urls_missing
  severity: warning
  fields:
  - evidence
  description: The snapshot records source names, not URLs, for beach facts. Add URLs before fact check.
  retryable: true
  owner: fact_check
- code: rocks_not_verified
  severity: warning
  fields:
  - description_long
  description: Absence of any mention of rocks is not confirmation, and the owner does not know (decision 4, 2026-11-01). The project criterion excludes beaches with rocks; a visit or an independent source is needed.
  retryable: true
  owner: fact_check
- code: lively_atmosphere_not_rated
  severity: info
  fields:
  - family_score
  description: Snapshot describes a younger, livelier environment; possibly less suited to small children. Not rated either way.
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
