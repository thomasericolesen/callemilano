---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-PALMERAL-DE-LAS-SORPRESAS-001
slug: palmeral-de-las-sorpresas
name: Palmeral de Las Sorpresas
category: City
tags: []
coordinates:
  latitude:  null
  longitude:  null
  purpose: representative_point
  label: Unknown; exact visitor point not established
  source:  null
  checked_at:  null
google_maps_url: https://maps.app.goo.gl/4cZJ8eRQH47aHH146
external_ids: {}
municipality: Málaga
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: "40 min"
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Palmeral de Las Sorpresas, Málaga
  source: "Google Maps (web), main figure (fastest route shown, toll roads not avoided), read by Claude in Chrome on 2026-11-11 from the project origin (36.5356875,-4.6626875); live traffic about 09:51 Wednesday 2026-11-11 - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=Palmeral+de+las+Sorpresas%2C+P%C2%BA+del+Muelle+Uno%2C+29015+M%C3%A1laga%2C+Spain&travelmode=driving"
  checked_at: 2026-11-11
  note: "38.6 km via AP-7 (route has tolls). Replaces 37 min from the earlier check of 2026-11-01 (Routes API); its method is in the git history."
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
seasonality:
  - All year
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
  typical_duration: "30–90 minutes (editorial planning estimate, depending on route)"
  booking_lead_time:  null
  valid_from:  null
  valid_until:  null
  cost_basis:  null
  cost_checked_at:  null
links:
  official_website:  null
  booking:  null
  visitor_information:  null
  transport:  null
  contact:  null
related_places: []
description_short: "Pedestrian waterfront public space beside Málaga port, linking the city centre with the harbour area."
description_long: "Why interesting: Useful for an easy outdoor stroll or as a connecting segment between central Málaga and Muelle Uno. Its value is the seafront setting and walkability, rather than a ticketed attraction. Editorial suitability by audience (low / medium / high): Small children (0-6) high, Children (7-12) high, Teenagers (13-17) medium, Adults high, Seniors high. These are estimates for planning, not guarantees or safety advice. Estimated duration: 30–90 minutes (editorial planning estimate, depending on route). Seasonality: All year. Weather and practical notes: Sun and heat exposure are likely on the open waterfront; bring shade and water in hot weather. Exact route surface, toilets and facilities have not been independently confirmed. Booking: false."
seo_title: Palmeral de Las Sorpresas | CalleMilano destination record
seo_description: Draft destination record for Palmeral de Las Sorpresas. Visitor facts
  and practical details are under verification.
images: []
evidence:
- field: name, google_maps_url
  claim: The owner-supplied Projekt Spanien Google Maps list contains a saved-place
    entry displayed as “Palmeral de Las Sorpresas”.
  source_url: https://maps.app.goo.gl/4cZJ8eRQH47aHH146
  source_type: maps_identity
  checked_at: '2026-10-04'
  checked_by: maps-import-agent
  confidence: medium
  notes: User-provided visible list capture. The list link is identity provenance
    only; it does not verify visitor facts, and an individual place URL was not supplied.
- field: description_short, description_long
  claim: "Málaga waterfront planning document describes the Palmeral as a pedestrian connection between the city, port and Muelle Uno."
  source_url: https://planmalagalitoral.malaga.eu/export/sites/planlitoral/.galleries/Documentos-actuaciones/Espacios-publicos/ECOSISTEMA-LITORAL_Memoria.pdf
  source_type: government
  checked_at: 2026-10-04
  checked_by: fact-check-agent
  confidence: medium
  notes: "Supports the stated claim only; any editorial planning estimate is identified as such."
- field: driving_time_from_casa_de_la_familia
  claim: 'One-way drive from Casa de la Familia to Palmeral de Las Sorpresas, Málaga: 37 min, 35.9 km (Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=Palmeral+de+Las+Sorpresas%2C+M%C3%A1laga%2C+Spain&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Claude (Routes API batch 2026-11-01)
  confidence: medium
  notes: Google Routes API computeRoutes; destination geocoded by Google from the record's destination text (the record has no coordinates). Predicted-traffic estimate for one departure time; the local_30km rule uses the Google Maps app's main figure.
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
updated_at: '2026-11-11'
last_verified:  null
last_reviewed_at:  null
next_review_at:  null
review_decision:  null
redirects: []
---
