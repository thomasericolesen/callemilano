---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-GRA-LAS-ALPUJARRAS-001
slug: las-alpujarras
name: Las Alpujarras
category: Nature
tags:
  - Nature
  - Hiking
  - Historic town
  - Full day
coordinates:
  latitude: 36.9613562
  longitude: -3.3585582
  purpose: representative_point
  label: "Capileira, highest of the Poqueira-gorge villages — chosen as an anchor point for this region record, not a final single-point decision"
  source: https://www.openstreetmap.org/node/33350836
  checked_at: 2026-10-15
google_maps_url: https://maps.google.com/?q=Las+Alpujarras%2C+Granada%2C+Spain
external_ids: {}
municipality: Capileira
province: Granada
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: "150 min"
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: "Capileira, Granada, Spain"
  source: "https://router.project-osrm.org/route/v1/driving/-4.6626875,36.5356875;-3.3585582,36.9613562?overview=false"
  checked_at: 2026-10-15
  note: "Route-checked one-way via OSRM (driving profile), ~171 km, via the Poqueira gorge mountain road (narrow and winding in its final stretch). Actual time varies with traffic and road conditions."
age_groups:
  - Young adults
family_score:
  small_children: unknown
  children: unknown
  young_adults: high
  seniors: unknown
energy_level: High
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
booking_required: false
dog_friendly: unknown
toilets_available: unknown
food_available: unknown
cost_level: Free
visit_information:
  schedule: null
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: "Walking the village is free; the Museo Pedro Antonio de Alarcón has an admission fee not confirmed in this research."
  cost_checked_at: null
links:
  official_website: null
  booking: null
  visitor_information: "https://www.spain.info/en/destination/capileira"
  transport: null
  contact: null
related_places: []
description_short: "Las Alpujarras is a mountain region of white villages south of Sierra Nevada; this record anchors on Capileira, the highest Poqueira-gorge village and a common hiking trailhead, though the single-point choice for this region is still open for editorial decision."
description_long: "Las Alpujarras is a region of white villages in the valleys south of Sierra Nevada, not a single point — this fact-check anchors the record on Capileira (altitude 1,436 m, population around 590), the highest of the three well-known Poqueira-gorge villages, reached via a narrow, winding mountain road about 2 hours 30 minutes' drive from Casa de la Familia (route-checked). Capileira has cubic, flat-roofed houses reflecting Moorish heritage, the Museo Pedro Antonio de Alarcón (an ethnological museum), and the 18th-century Iglesia de Santa María la Mayor. It is a commonly used trailhead area for hiking: the long-distance GR-7 passes nearby with a roughly 6 km stretch to Pampaneira and an 11.5 km, 3.5-hour stretch from Busquístar, and the GR-240 (Sulayr) ring trail includes a Capileira-Trevélez stage, though the full Sulayr circuit is considered demanding and sources recommend day-walk segments rather than the whole route for casual visitors. Two claims should NOT be assumed for Capileira specifically: the region's famous cured-ham (jamón) tradition is tied to Trevélez, not Capileira, and craft-shop streets are more specifically associated with nearby Pampaneira. Whether Mulhacén hiking routes start precisely at Capileira was not confirmed. Pampaneira itself (lower, easier access, more commercial infrastructure) is a defensible alternative anchor point and remains an open editorial choice."
seo_title: "Las Alpujarras: Capileira and the Poqueira Gorge"
seo_description: "Explore Las Alpujarras from Capileira: hiking trails, white villages, and the drive from Casa de la Familia. Region anchor point still under editorial review."
images: []
evidence:
  - field: "coordinates"
    claim: "Capileira is a village in the Poqueira gorge, Las Alpujarras, at about 1,436 m altitude."
    source_url: https://www.openstreetmap.org/node/33350836
    source_type: maps_identity
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "OpenStreetMap village-level point, within about 1.5 km of an independent secondary (Wikipedia) coordinate for Capileira."
  - field: "description_long"
    claim: "Capileira has cubic flat-roofed houses reflecting Moorish heritage, the Museo Pedro Antonio de Alarcón, and the 18th-century Iglesia de Santa María la Mayor."
    source_url: "https://www.spain.info/en/destination/capileira"
    source_type: official_tourism
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: high
    notes: "Spain's official national tourism board site."
  - field: "description_long"
    claim: "The GR-7 passes near Capileira (about 6 km to Pampaneira; 11.5 km / ~3.5 h from Busquístar); the GR-240 (Sulayr) includes a Capileira-Trevélez stage, and the full Sulayr circuit is considered demanding for casual hikers."
    source_url: "https://treksierranevada.com"
    source_type: secondary
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "Jamón fame and craft-shop streets are specifically attributed to Trevélez and Pampaneira respectively in these sources, not Capileira — recorded here to prevent a misattributed claim."
  - field: "driving_time_from_casa_de_la_familia"
    claim: "One-way driving route from Casa de la Familia to Capileira is approximately 150 minutes (171 km)."
    source_url: "https://router.project-osrm.org/route/v1/driving/-4.6626875,36.5356875;-3.3585582,36.9613562?overview=false"
    source_type: secondary
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "OSRM public routing engine, driving profile; traffic and the mountain road's winding final stretch are not separately modelled."
review_issues:
  - code: area_pin_open
    severity: blocking
    fields: [coordinates, municipality]
    description: "Region (villages and sierra), not a point. This fact-check anchors on Capileira as the most defensible single point for a nature/hiking-focused young-adult audience, with Pampaneira flagged as a credible alternative; the editor must approve the final choice (and whether Sierra Nevada itself becomes a separate record)."
    retryable: true
    owner: editor
  - code: excursion_layer_scope
    severity: warning
    fields: [status]
    description: "Included under the owner decision of 2026-10-15 to add an excursion layer (route-checked one-way drive up to about 4 h) beyond the 30 km primary area. Pending editor-of-record approval and change-log entry."
    retryable: true
    owner: editor
  - code: family_ratings_estimated
    severity: warning
    fields: [age_groups, family_score, energy_level, seasonality, tags]
    description: "Audience ratings, energy, season and duration tag are provisional editorial estimates for young adults; other age groups left unknown. Assess before approval."
    retryable: true
    owner: editorial
  - code: visitor_facilities_unverified
    severity: warning
    fields: [accessibility, wheelchair_friendly, parking, dog_friendly, toilets_available, food_available]
    description: "Visitor facilities, access, parking, dog policy and on-site food remain unverified."
    retryable: true
    owner: fact_check
created_at: 2026-10-15
updated_at: 2026-10-15
last_verified: 2026-10-15
last_reviewed_at: null
next_review_at: 2027-01-15
review_decision: null
redirects: []
---

Fact-checked 2026-10-15: Capileira used as a sourced anchor point with driving time established; the region's structural area-pin decision remains open for the editor, and several facts (Mulhacén trailhead claim, visitor facilities) are explicitly flagged rather than guessed. Draft source notes (import): Created from the Danish excursion catalogue of 2026-10-15 (an inspiration document, not a source). The Maps link is a place lookup, not a saved-list link.
