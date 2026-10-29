---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-PLAYAMAR-001
slug: playamar
name: Playamar
category: Beaches
tags:
- Beach
coordinates:
  latitude: null
  longitude: null
  purpose: representative_point
  label: Unknown; exact visitor point not established
  source: null
  checked_at: null
google_maps_url: null
external_ids: {}
municipality: Torremolinos
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: null
  origin: Casa de la Familia (Calle Milano 35, 29649 Las Lagunas de Mijas, Málaga, Spain)
  destination: Unknown; named visitor point not established
  source: null
  checked_at: null
  note: Not checked. The owner's own figure is about 30 min (Google Maps, Saturday 10:00); coordinates and times have not yet been read from the Maps link. The figure is not recorded as a measured duration. Do not estimate.
age_groups:
- Small children (0-6)
family_score:
  small_children: medium
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
description_short: 'Playamar, Torremolinos: Blue Flag 2026. Character (subjective): Developed (Danish: Tilrettelagt). Draft from a dated secondary-source snapshot; not fact-checked.'
description_long: 'Playamar (Torremolinos). Blue Flag 2026 (used as proxy for water quality). Fine, dark sand. Often recommended for children. Eating places named in tourist sources (opening hours not checked; many beach bars close out of season): Wide choice of beach bars and restaurants. Nearby: Paseo Maritimo. Rocks: not mentioned in the sources reviewed (absence of mention, not a confirmed absence). Character: Developed (Danish: Tilrettelagt) - subjective assessment from the sources'' description of urbanisation, not an official category. Family suitability and energy level are subjective estimates and not safety advice.'
seo_title: Playamar, Torremolinos | CalleMilano draft record
seo_description: Draft record for Playamar beach (Torremolinos). Based on a dated secondary-source snapshot; facts are under verification.
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
- field: description_long (sand, size, waves, occupancy)
  claim: Fine, dark sand.
  source_url: null
  source_type: secondary
  checked_at: '2026-10-15'
  checked_by: strandoversigt-snapshot (Eric/Claude)
  confidence: low
  notes: '[unverified] Source per snapshot: per-beach source not recorded in snapshot (snapshot lists Barcelo, ''Torremolinos med børn'', among its sources). URL not recorded in the snapshot. Not rechecked 2026-10-29.'
- field: description_long (children, facilities, restaurants, experiences)
  claim: Often recommended for children. | Wide choice of beach bars and restaurants. | Paseo Maritimo.
  source_url: null
  source_type: secondary
  checked_at: '2026-10-15'
  checked_by: strandoversigt-snapshot (Eric/Claude)
  confidence: low
  notes: '[unverified] Hotel-chain and tourist-site guides (Hoteles.net, Barcelo, Cargest, Mijas tourism and others), not independent. Opening hours and child-friendliness not checked.'
- field: description_long (rocks)
  claim: The sources reviewed do not mention rocks.
  source_url: null
  source_type: secondary
  checked_at: '2026-10-15'
  checked_by: strandoversigt-snapshot (Eric/Claude)
  confidence: low
  notes: '[unverified] Absence of a mention is not confirmation that there are no rocks.'
review_issues:
- code: coordinates_missing
  severity: blocking
  fields:
  - coordinates.latitude
  - coordinates.longitude
  description: Coordinates not yet read from the owner's Maps link; not guessed. Needed for the radius filter.
  retryable: true
  owner: fact_check
- code: driving_time_unverified
  severity: blocking
  fields:
  - driving_time_from_casa_de_la_familia
  description: Not checked. The owner's own figure is about 30 min but the Maps link has not been read; nothing recorded as measured. Do not estimate.
  retryable: true
  owner: fact_check
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
  description: Facilities, child-related statements and restaurant names come from tourist-site and hotel-chain guides (not independent). Opening hours not checked; many beach bars close out of season.
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
  description: Absence of any mention of rocks is not confirmation. The project criterion excludes beaches with rocks; a visit or an independent source is needed.
  retryable: true
  owner: fact_check
- code: seasonality_unknown
  severity: warning
  fields:
  - seasonality
  description: The snapshot gives no seasonal information; left empty rather than guessed.
  retryable: true
  owner: fact_check
- code: practical_details_out_of_scope
  severity: info
  fields:
  - parking
  - transport_options
  - dog_friendly
  - cost_level
  - booking_required
  - food_available
  - visit_information
  description: 'Parking and other practical details are intentionally left unknown (owner decision: adults look these up themselves).'
  retryable: false
  owner: human_editor
- code: name_confusion_playamarina
  severity: info
  fields:
  - name
  - slug
  description: Not the same place as 'El Charcón-Playamarina' in Mijas (docs/launch-candidates.md). This record is Playamar in Torremolinos.
  retryable: false
  owner: human_editor
created_at: '2026-10-29'
updated_at: '2026-10-29'
last_verified: '2026-10-29'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
