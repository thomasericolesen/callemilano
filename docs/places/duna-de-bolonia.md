---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-CAD-DUNA-DE-BOLONIA-001
slug: duna-de-bolonia
name: Duna de Bolonia
category: Beaches
tags:
- Beach
- Nature
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
municipality: Unknown
province: Cádiz
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration:  null
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas,
    Málaga, Spain
  destination: Unknown; named visitor point not established
  source:  null
  checked_at:  null
  note: Route not checked; do not estimate from memory.
age_groups:
  - Children (7-12)
  - Teenagers (13-17)
  - Adults
family_score:
  small_children: low
  children: medium
  teenagers: high
  adults: high
  seniors: low
energy_level: Medium
seasonality:
  - Spring
  - Summer
  - Autumn
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
booking_required: false
dog_friendly: unknown
toilets_available: unknown
food_available: unknown
cost_level: Unknown
visit_information:
  schedule:  null
  typical_duration: "About 30–60 minutes for the official short trail; longer if combined with the beach (official route duration plus editorial allowance)"
  booking_lead_time:  null
  valid_from:  null
  valid_until:  null
  cost_basis:  null
  cost_checked_at:  null
links:
  official_website:  null
  booking:  null
  visitor_information: https://www.juntadeandalucia.es/medioambiente/portal/areas-tematicas/espacios-protegidos/legislacion-autonomica-nacional/monumentos-naturales/monumento-natural-duna-bolonia
  transport:  null
  contact:  null
related_places: []
description_short: "Active coastal dune and protected natural monument beside Bolonia beach in Tarifa."
description_long: "Why interesting: The dune is a striking wind-shaped landform and an outdoor landscape visit. The experience is primarily scenic; visitors should respect protected-area limits and avoid climbing restricted vegetation or unstable slopes. Editorial suitability by audience (low / medium / high): Small children (0-6) low, Children (7-12) medium, Teenagers (13-17) high, Adults high, Seniors low. These are estimates for planning, not guarantees or safety advice. Estimated duration: About 30–60 minutes for the official short trail; longer if combined with the beach (official route duration plus editorial allowance). Seasonality: Spring; Summer; Autumn. Weather and practical notes: Strong Levante wind, sand, heat and sun exposure affect comfort. The official visitor page reported a temporary closure of the trail and viewpoint in May 2026; check that current closure has ended before visiting. Do not assume the dune itself is open for climbing. Booking: false."
seo_title: Duna de Bolonia | CalleMilano destination record
seo_description: Draft destination record for Duna de Bolonia. Visitor facts and practical
  details are under verification.
images: []
evidence:
- field: name, google_maps_url
  claim: The owner-supplied Projekt Spanien Google Maps list contains a saved-place
    entry displayed as “Duna de Bolonia”.
  source_url: https://maps.app.goo.gl/4cZJ8eRQH47aHH146
  source_type: maps_identity
  checked_at: '2026-10-04'
  checked_by: maps-import-agent
  confidence: high
  notes: User-provided visible list capture. The list link is identity provenance
    only; it does not verify visitor facts, and an individual place URL was not supplied.
- field: description_long
  claim: The Junta identifies Duna de Bolonia as a natural monument near Baelo Claudia
    and notes its exposure to Levante winds.
  source_url: https://www.juntadeandalucia.es/medioambiente/portal/areas-tematicas/espacios-protegidos/legislacion-autonomica-nacional/monumentos-naturales/monumento-natural-duna-bolonia
  source_type: government
  checked_at: '2026-10-04'
  checked_by: fact-check-agent
  confidence: high
  notes: Supports only the stated claim; do not generalize to unverified facilities
    or suitability.
- field: description_short, description_long, seasonality
  claim: "Andalusia environment portal identifies the active 30 m dune, protected designation, Tarifa location and exposure to Levante winds."
  source_url: https://www.juntadeandalucia.es/medioambiente/portal/areas-tematicas/espacios-protegidos/legislacion-autonomica-nacional/monumentos-naturales/monumento-natural-duna-bolonia
  source_type: government
  checked_at: 2026-10-04
  checked_by: fact-check-agent
  confidence: high
  notes: "Supports the stated claim only; any editorial planning estimate is identified as such."
- field: visit_information.typical_duration, description_long
  claim: "Andalusia visitor portal describes the short dune trail and lists a temporary closure notice dated 8 May 2026."
  source_url: https://www.juntadeandalucia.es/medioambiente/portal/web/ventanadelvisitante/detalle-buscador-mapa/-/asset_publisher/Jlbxh2qB3NwR/content/duna-de-bolonia/
  source_type: government
  checked_at: 2026-10-04
  checked_by: fact-check-agent
  confidence: high
  notes: "Supports the stated claim only; any editorial planning estimate is identified as such."
review_issues:
- code: editorial_suitability_requires_human_review
  severity: warning
  fields:
  description: Audience ratings and effort level are editorial estimates requested for this draft; human editor must review them before approval.
  retryable: false
  owner: human_editor
- code: record_incomplete
  severity: warning
  fields:
  - coordinates
  - driving_time_from_casa_de_la_familia
  - accessibility
  - parking
  - visit_information
  description: These facts or editorial assessments were not established from the
    supplied list or checked sources. Explicit unknown values remain in this draft;
    complete claim-specific research and editorial review before advancement.
  retryable: true
  owner: fact_check
- code: schema_blocking_unknowns
  severity: blocking
  fields:
  - coordinates.latitude
  - coordinates.longitude
  description: The active schema does not define unknown values for all required fields.
    This draft leaves unsupported values explicit; resolve them with evidence or obtain
    an approved schema-compatible representation before validation or human approval.
  retryable: true
  owner: fact_check
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
