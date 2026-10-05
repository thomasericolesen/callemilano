---
schema_version: 1.0.0
status: draft
id:  null
slug: miradouro-da-serpente-do-medal
name: Miradouro da Serpente do Medal
category: Nature
tags:
- Viewpoint
- Hiking
coordinates:
  latitude:  null
  longitude:  null
  purpose: representative_point
  label: Unknown; exact visitor point not established
  source:  null
  checked_at:  null
google_maps_url: https://maps.app.goo.gl/4cZJ8eRQH47aHH146
external_ids: {}
municipality: Mogadouro
province: Unknown
autonomous_community: Not applicable
country: Portugal
driving_time_from_casa_de_la_familia:
  duration:  null
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas,
    Málaga, Spain
  destination: Unknown; named visitor point not established
  source:  null
  checked_at:  null
  note: Route not checked; do not estimate from memory.
age_groups: []
family_score:
  small_children: unknown
  children: unknown
  teenagers: unknown
  adults: unknown
  seniors: unknown
energy_level:  null
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
  source:  null
  checked_at:  null
  confidence: unknown
wheelchair_friendly: unknown
parking:
  availability: unknown
  location_type: unknown
  cost: unknown
  restrictions: unknown
  walk_distance: unknown
  source:  null
  checked_at:  null
transport_options: []
booking_required: unknown
dog_friendly: unknown
toilets_available: unknown
food_available: unknown
cost_level: Unknown
visit_information:
  schedule:  null
  typical_duration:  null
  booking_lead_time:  null
  valid_from:  null
  valid_until:  null
  cost_basis:  null
  cost_checked_at:  null
links:
  official_website:  null
  booking:  null
  visitor_information: https://www.mogadouro.pt/cmmogadouro/uploads/document/file/3001/demonstracoes_financeiras.pdf
  transport:  null
  contact:  null
related_places: []
description_short: Imported destination candidate; visitor point and practical visitor
  information are not yet fully verified.
description_long: |-
  Official facts (see evidence ledger): Mogadouro municipal documentation refers to the Miradouro da Serpente do Medal project in the municipality.
  Editorial interpretation (low confidence): This imported candidate may fit the owner’s interests in nature, viewpoints, or hiking; the exact visitor experience, route, and suitability remain unassessed.
  Guest observations: None were supplied in the imported list material reviewed.
seo_title: Miradouro da Serpente do Medal | CalleMilano destination record
seo_description: Draft destination record for Miradouro da Serpente do Medal. Visitor
  facts and practical details are under verification.
images: []
evidence:
- field: name, google_maps_url
  claim: The owner-supplied Projekt Spanien Google Maps list contains a saved-place
    entry displayed as “Miradouro da Serpente do Medal”.
  source_url: https://maps.app.goo.gl/4cZJ8eRQH47aHH146
  source_type: maps_identity
  checked_at: '2026-10-04'
  checked_by: maps-import-agent
  confidence: medium
  notes: User-provided visible list capture. The list link is identity provenance
    only; it does not verify visitor facts, and an individual place URL was not supplied.
- field: description_long
  claim: Mogadouro municipal documentation refers to the Miradouro da Serpente do
    Medal project in the municipality.
  source_url: https://www.mogadouro.pt/cmmogadouro/uploads/document/file/3001/demonstracoes_financeiras.pdf
  source_type: government
  checked_at: '2026-10-04'
  checked_by: fact-check-agent
  confidence: medium
  notes: Supports only the stated claim; do not generalize to unverified facilities
    or suitability.
review_issues:
- code: needs_clarification
  severity: blocking
  fields:
  - name
  - coordinates
  description: Identity remains unresolved; retained as a clarification hold. No further identity research was performed in this task.
  retryable: false
  owner: human_editor
- code: record_incomplete
  severity: warning
  fields:
  - coordinates
  - driving_time_from_casa_de_la_familia
  - age_groups
  - family_score
  - energy_level
  - seasonality
  - accessibility
  - parking
  - visit_information
  - guest_observations
  description: These facts or editorial assessments were not established from the
    supplied list or checked sources. Explicit unknown values remain in this draft;
    complete claim-specific research and editorial review before advancement.
  retryable: true
  owner: fact_check
- code: outside_spain_id_namespace
  severity: blocking
  fields:
  - id
  - country
  - autonomous_community
  description: The destination is in Portugal, while the active schema requires ES-prefixed
    Spanish place IDs. This draft uses the project namespace provisionally; human
    editor must resolve out-of-country ID handling before advancement.
  retryable: false
  owner: human_editor
- code: schema_blocking_unknowns
  severity: blocking
  fields:
  - coordinates.latitude
  - coordinates.longitude
  - energy_level
  - seasonality
  description: The active schema does not define unknown values for all required fields.
    This draft leaves unsupported values explicit; resolve them with evidence or obtain
    an approved schema-compatible representation before validation or human approval.
  retryable: true
  owner: fact_check
- code: stable_id_not_allocated
  severity: blocking
  fields:
  - id
  - name
  - coordinates
  - country
  description: Stable ID allocation is withheld because the saved identity/scope is
    unresolved or the destination is outside the Spanish ES ID namespace. Resolve
    identity/scope or the applicable ID policy before reserving an ID.
  retryable: false
  owner: human_editor
- code: category_and_tags_need_human_review
  severity: warning
  fields:
  - category
  - tags
  description: Primary category and controlled tags are provisional intake recommendations;
    human editor-of-record must confirm before editorial advancement.
  retryable: false
  owner: human_editor
created_at: '2026-10-04'
updated_at: '2026-10-04'
last_verified:  null
last_reviewed_at:  null
next_review_at:  null
review_decision:  null
redirects: []
---
