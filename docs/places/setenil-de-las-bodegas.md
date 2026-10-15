---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-CAD-SETENIL-DE-LAS-BODEGAS-001
slug: setenil-de-las-bodegas
name: Setenil de las Bodegas
category: City
tags:
  - Historic town
  - Restaurant
  - Half day
coordinates:
  latitude: 36.8638359
  longitude: -5.1811411
  purpose: town_center
  label: "Plaza de Andalucía, upper town square next to the old Ayuntamiento/Torreón and tourist office"
  source: https://www.openstreetmap.org/way/548232862
  checked_at: 2026-10-15
google_maps_url: https://maps.google.com/?q=Setenil+de+las+Bodegas%2C+C%C3%A1diz%2C+Spain
external_ids: {}
municipality: Setenil de las Bodegas
province: Cádiz
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: "121 min"
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: "Plaza de Andalucía, Setenil de las Bodegas, Cádiz, Spain"
  source: "https://router.project-osrm.org/route/v1/driving/-4.6626875,36.5356875;-5.1811411,36.8638359?overview=false"
  checked_at: 2026-10-15
  note: "Route-checked one-way via OSRM (driving profile), ~115.6 km. Actual time varies with traffic."
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
  - Spring
  - Summer
  - Autumn
  - Winter
accessibility:
  overall: unknown
  mobility:
    route: "Streets wind through town on a slope beside the Río Trejo/Guadalporcún gorge; cobbled, sometimes steep. No official accessibility assessment found."
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
  schedule: "Open town; no entrance fee. Tourist office reportedly 10:00-14:00 (unverified directly, relayed via search snippet only)."
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: "Free to walk the streets; individual bars/restaurants charge separately (not itemised here)."
  cost_checked_at: 2026-10-15
links:
  official_website: null
  booking: null
  visitor_information: "https://andalucia.org/en/setenil-de-las-bodegas-information-services-setenil-de-las-bodegas"
  transport: null
  contact: null
related_places: []
description_short: "Setenil de las Bodegas is famous for houses built directly into rock overhangs above a river gorge; a free-to-walk historic town, about 2 hours' drive from Casa de la Familia, often combined with nearby Ronda."
description_long: "Setenil de las Bodegas is a small Cádiz-province town (population roughly 2,600) known for houses and bars built directly under and into overhanging rock above a river through the town centre (sources disagree on whether it is the Río Trejo or Guadalporcún). The streets around Plaza de Andalucía, where the old town hall and tourist office sit, are free to walk, with cave-set bars and restaurants lining the main cobbled streets; the Junta de Andalucía formally recognised the town as a 'Municipio Turístico' in a late-2023 agreement. It is about 2 hours' drive from Casa de la Familia (route-checked) and is commonly visited together with Ronda, a short distance away, though the Setenil-Ronda leg itself has not been route-checked for this record. Tourist-office hours, parking, and accessibility (the town is built on a slope) have not been confirmed from an official source."
seo_title: "Setenil de las Bodegas: Cave Houses and Historic Centre"
seo_description: "Visit Setenil de las Bodegas, Cádiz: cave-set houses and bars above a river gorge, often paired with Ronda. Free to walk; drive time from Casa de la Familia."
images: []
evidence:
  - field: "coordinates"
    claim: "Plaza de Andalucía is the upper town square in Setenil de las Bodegas, next to the old town hall/Torreón and the tourist office."
    source_url: https://www.openstreetmap.org/way/548232862
    source_type: maps_identity
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: null
  - field: "description_long"
    claim: "Setenil de las Bodegas is known for houses built into rock overhangs above a river running through the town; population approximately 2,600."
    source_url: "https://en.wikipedia.org/wiki/Setenil_de_las_Bodegas"
    source_type: secondary
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "Encyclopedia entry; the river's exact name is given inconsistently across sources (Río Trejo vs Guadalporcún) and is flagged as unresolved rather than asserted."
  - field: "description_long"
    claim: "The Junta de Andalucía formally designated Setenil a 'Municipio Turístico' in a late-2023 administrative agreement following a December 2022 application."
    source_url: "https://juntadeandalucia.es"
    source_type: government
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "Relayed via search result of an official regional gazette entry; not independently re-fetched as a direct PDF in this pass."
  - field: "driving_time_from_casa_de_la_familia"
    claim: "One-way driving route from Casa de la Familia to Plaza de Andalucía, Setenil de las Bodegas, is approximately 121 minutes (115.6 km)."
    source_url: "https://router.project-osrm.org/route/v1/driving/-4.6626875,36.5356875;-5.1811411,36.8638359?overview=false"
    source_type: secondary
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "OSRM public routing engine, driving profile; traffic not modelled."
review_issues:
  - code: overlap_ronda
    severity: warning
    fields: [related_places]
    description: "Usually combined with Ronda (docs/places/ronda.md). Add related_places link after both records confirm identity; the Setenil-Ronda driving leg has not itself been route-checked."
    retryable: true
    owner: editorial
  - code: excursion_layer_scope
    severity: warning
    fields: [status]
    description: "Included under the owner decision of 2026-10-15 to add an excursion layer (route-checked one-way drive up to about 4 h) beyond the 30 km primary area. Pending editor-of-record approval and change-log entry."
    retryable: true
    owner: editor
  - code: visitor_facilities_unverified
    severity: warning
    fields: [accessibility, wheelchair_friendly, parking, dog_friendly, toilets_available, food_available]
    description: "Parking, accessibility (sloped/cobbled streets), dog policy, toilets and on-site food have not been confirmed from an official source."
    retryable: true
    owner: fact_check
created_at: 2026-10-15
updated_at: 2026-10-15
last_verified: 2026-10-15
last_reviewed_at: 2026-10-15
next_review_at: 2027-04-15
review_decision: null
redirects: []
---

Fact-checked 2026-10-15: visitor point, driving time and core identity facts established; tourist-office hours, parking and accessibility remain unverified and are flagged. Draft source notes (import): Created from the Danish excursion catalogue of 2026-10-15 (an inspiration document, not a source). The Maps link is a place lookup, not a saved-list link.
