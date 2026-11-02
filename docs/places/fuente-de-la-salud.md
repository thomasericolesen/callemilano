---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-FUENTE-DE-LA-SALUD-001
slug: fuente-de-la-salud
name: Fuente de la Salud
category: Beaches
tags:
- Beach
coordinates:
  latitude: 36.5986
  longitude: -4.5102
  purpose: representative_point
  label: Google Maps marker (owner-read); not a parking point
  source: Google Maps marker, read by Eric Olesen (owner) 2026-07-18; accepted as the record's place point by the owner on 2026-11-01 (decision 1). Not an official visitor point.
  checked_at: '2026-07-18'
google_maps_url: https://maps.google.com/?cid=14195859727461052171
external_ids:
  google_place_id: ChIJ8WWL6G_8cg0RC--WkDXTAcU
municipality: Benalmádena
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 30 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Fuente de la Salud, Benalmádena, Málaga, Spain (Google Maps marker, not a parking point)
  source: Google Routes API computeRoutes, run 2026-11-01 from the project origin (36.5356875, -4.6626875); destination = record coordinates (36.5986,-4.5102); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5986%2C-4.5102&travelmode=driving
  checked_at: '2026-11-01'
  note: 'Routes API figure: 30 min with predicted Saturday 10:00 traffic (30 min without traffic), 20.5 km via AP-7; an avoid-tolls run gave 30 min. One predicted sample, not the Google Maps app''s main figure; traffic and season change the time. Previous value 30 min (2026-07-18): Google Maps, measured by Eric Olesen (owner). Batch: data/route-checks-2026-11-01-local.csv. Owner decision 2026-11-01: the owner-read marker is accepted as the place point, so this route check stands.'
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
  overall: Benalmádena lists Fuente de la Salud as one of four accessibility points / adapted beaches in 2026 (with Malapesquera, Arroyo de la Miel and Carvajal). The facilities at the point, the route and accessible toilets are not specified in the source.
  mobility:
    route: unknown
    wheelchair_route: unknown
    facilities: Accessibility point / adapted beach (2026, municipal); equipment not specified.
  sensory:
    notes: unknown
  accessible_toilets: unknown
  source: https://www.benalmadena.es/noticias/N13457/El-Ayuntamiento-refuerza-la-seguridad-y-la-accesibilidad-de-las-playas-con-un-amplio-dispositivo-de-vigilancia-y-salvamento.html
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
- id: ES-AND-MAL-CHIRINGUITO-RAFAEL-001
  relationship: nearby
  note: 'Place to eat: Chiringuito Rafael.'
description_short: 'Fuente de la Salud, Benalmádena: Blue Flag 2026. Character (subjective): Developed (Danish: Tilrettelagt). Draft; facts being checked against official sources.'
description_long: 'Fuente de la Salud (Benalmádena). Blue Flag 2026 (used as proxy for water quality). Official regional tourism listing (andalucia.org, Junta de Andalucía; undated, read 2026-11-02): Benalmádena''s easternmost beach, next to the marina (Puerto Deportivo) and bordering Torremolinos, fine sand, about 150 m long, with adapted toilets. Places to eat: see the linked record for Chiringuito Rafael. Rocks: not confirmed either way (not mentioned in the sources reviewed, and not known to the owner). Municipal source (Benalmádena, 2026-06-05, checked 2026-11-01): a lifeguard point and an accessibility point / adapted beach at Fuente de la Salud; intensive lifeguard season 15 May-15 October, plus Easter week and the following weekends. A play area is not confirmed by an official source. Character: Developed (Danish: Tilrettelagt) - subjective assessment from the sources'' description of urbanisation, not an official category. Family suitability and energy level are subjective estimates and not safety advice.'
seo_title: Fuente de la Salud, Benalmádena | CalleMilano draft record
seo_description: Draft record for Fuente de la Salud beach (Benalmádena). Facts are being checked against official sources.
images: []
evidence:
- field: description_long (Blue Flag 2026)
  claim: '''Fuente de la Salud'' is on the ADEAC, ''Relación Playas Galardonadas 2026''.'
  source_url: https://www.banderaazul.org/sites/default/files/2026/Rueda-de-prensa-2026/Relaci%C3%B3n%20Playas%20Galardonadas%202026.pdf
  source_type: official_tourism
  checked_at: '2026-10-29'
  checked_by: claude-sonnet-5-5 (draft 2026-10-29)
  confidence: high
  notes: '[verified] Checked against ADEAC''s official list (edition 2026-2027) on 2026-10-29, read via a WebFetch summary (PDF not read page by page). Matches the snapshot check of 2026-10-15. Municipality grouping read directly from the list. Awards are conditional on continued compliance and verification during 2027 (list footnote). source_type is the nearest schema value: ADEAC is the national Blue Flag operator and the schema has no certification source type (editor decision).'
- field: description_long (Blue Flag 2026)
  claim: El Español's 2026 Blue Flag article lists the beach under Benalmádena. Article lists 'Fuente de la Salud' under Benalmádena.
  source_url: https://www.elespanol.com/malaga/20260505/malaga-vuelve-tenir-azul-costa-playas-provincia-cuentan-bandera-sello-calidad/1003744233872_0.html
  source_type: secondary
  checked_at: '2026-10-29'
  checked_by: claude-sonnet-5-5 (draft 2026-10-29)
  confidence: medium
  notes: '[partial] Corroborating source, read via a WebFetch summary on 2026-10-29 (article not read in full). Supports the ADEAC check; does not replace it.'
- field: driving_time_from_casa_de_la_familia
  claim: 'One-way drive from Casa de la Familia to Fuente de la Salud, Benalmádena, Málaga, Spain (Google Maps marker, not a parking point): 30 min, 20.5 km (Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5986%2C-4.5102&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Claude (Routes API batch 2026-11-01)
  confidence: medium
  notes: Google Routes API computeRoutes; destination = record coordinates (36.5986,-4.5102). Predicted-traffic estimate for one departure time; the local_30km rule uses the Google Maps app's main figure.
- field: accessibility, description_long (lifeguard post)
  claim: Fuente de la Salud is one of nine lifeguard points and one of four accessibility points / adapted beaches in Benalmádena's 2026 beach service; bathing season Easter week and following weekends, intensive season 15 May-15 October.
  source_url: https://www.benalmadena.es/noticias/N13457/El-Ayuntamiento-refuerza-la-seguridad-y-la-accesibilidad-de-las-playas-con-un-amplio-dispositivo-de-vigilancia-y-salvamento.html
  source_type: government
  checked_at: '2026-11-01'
  checked_by: Claude (beach fact check 2026-11-01)
  confidence: high
  notes: Ayuntamiento de Benalmádena, Delegación de Playas news item 2026-06-05, read 2026-11-01. Toilets and play area are not mentioned.
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
  claim: Google Places lists 'Playa de Fuente de la Salud' (29630 Benalmádena, Málaga, España), place ID ChIJ8WWL6G_8cg0RC--WkDXTAcU, about 5 m from the record coordinates.
  source_url: https://maps.google.com/?cid=14195859727461052171
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (Places API lookup 2026-11-02)
  confidence: high
  notes: Google Places API (New) searchText/searchNearby on 2026-11-02. Maps establishes identity and position only, not facilities or suitability.
- field: description_long (sand, size, waves, occupancy, services), toilets_available
  claim: 'Fuente de la Salud: easternmost beach of Benalmádena, next to the Puerto Deportivo, bordering Torremolinos; fine sand; 150 m long; central, with all services; adapted toilets.'
  source_url: https://www.andalucia.org/listing/playa-fuente-de-la-salud/18944102/
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (official beach data 2026-11-02)
  confidence: medium
  notes: Junta de Andalucía official tourism portal; undated listing. Read via Firecrawl on 2026-11-02. Replaces the unsourced snapshot entries for sand, size, children, facilities and restaurants, which were removed together with their unsourced claims in the description.
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
created_at: '2026-10-29'
updated_at: '2026-11-02'
last_verified: '2026-10-29'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
