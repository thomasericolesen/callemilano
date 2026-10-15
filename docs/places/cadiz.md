---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-CAD-CADIZ-001
slug: cadiz
name: Cádiz
category: City
tags:
  - Beach
  - Historic town
  - Restaurant
  - Full day
coordinates:
  latitude: 36.5289521
  longitude: -6.2953183
  purpose: town_center
  label: "Catedral de Cádiz (Catedral de la Santa Cruz sobre el Mar), old town"
  source: https://www.openstreetmap.org/way/66648047
  checked_at: 2026-10-15
google_maps_url: https://maps.google.com/?q=C%C3%A1diz%2C+C%C3%A1diz%2C+Spain
external_ids: {}
municipality: Cádiz
province: Cádiz
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: "160 min"
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: "Catedral de Cádiz, Cádiz, Spain"
  source: "https://router.project-osrm.org/route/v1/driving/-4.6626875,36.5356875;-6.2953183,36.5289521?overview=false"
  checked_at: 2026-10-15
  note: "Route-checked one-way via OSRM (driving profile), ~213 km. Actual time varies with traffic; this is the longest drive among the Cádiz-province excursion candidates and is best treated as a long-day or overnight trip."
age_groups:
  - Small children (0-6)
  - Children (7-12)
  - Young adults
  - Seniors
family_score:
  small_children: medium
  children: high
  young_adults: high
  seniors: high
energy_level: Medium
seasonality:
  - Spring
  - Summer
  - Autumn
  - Winter
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
  schedule: "The cathedral's own site shows rolling visit-schedule notices rather than a clear stable annual timetable; current 2026 hours should be reconfirmed directly before publication."
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: "Not confirmed on the official page reached; secondary sources give conflicting figures (roughly €8-15 depending on ticket type, with student/senior discounts and under-12s often free). Do not treat as final; tickets are sold via shop.articketing.com per the cathedral's own site."
  cost_checked_at: 2026-10-15
links:
  official_website: "https://catedraldecadiz.com/"
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: "Cádiz, one of the oldest continuously inhabited cities in Western Europe, pairs its cathedral and old town with the sheltered Playa de la Caleta beach; around 2 hours 40 minutes' drive from Casa de la Familia, best treated as a long day or overnight trip."
description_long: "Cádiz is the provincial capital, about 2 hours 40 minutes' drive from Casa de la Familia (route-checked, ~213 km) — long enough that it is best planned as a long day trip or an overnight stay rather than a quick excursion. The Catedral de Cádiz (Catedral de la Santa Cruz sobre el Mar) anchors the old town; its own website shows visit information but with rolling, inconsistently dated notices rather than a clear stable schedule, so current hours and price are not published here and should be reconfirmed directly. The visit is described as including a climbable clock tower (Torre del Reloj) with city views, a crypt, a small museum gallery, and a virtual-reality element. Playa de la Caleta, a sheltered, Blue Flag cove beach flanked by two historic castles (San Sebastián and Santa Catalina) with full services, is a short walk from the old town and has been a boat-mooring point since Phoenician times according to secondary sources. Parking, accessibility and the exact cathedral price have not been confirmed from an official source."
seo_title: "Cádiz: Cathedral, Old Town and Playa de la Caleta"
seo_description: "Plan a long day trip or overnight stay in Cádiz: the cathedral, old town, and Playa de la Caleta beach. About 2h40 from Casa de la Familia."
images: []
evidence:
  - field: "coordinates"
    claim: "Catedral de Cádiz stands in the old town, overlooking the sea."
    source_url: https://www.openstreetmap.org/way/66648047
    source_type: maps_identity
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: high
    notes: "Cross-checked against an independent secondary (Wikipedia) coordinate within a few metres."
  - field: "visit_information, description_long"
    claim: "The cathedral visit includes a climbable clock tower (Torre del Reloj), a crypt, a small museum gallery (Casa de la Contaduría), and a virtual-reality element; tickets are sold via a linked third-party platform."
    source_url: "https://catedraldecadiz.com/"
    source_type: official_venue
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "Directly fetched, but the page's schedule notices carry inconsistent/undated references, so hours and price are not asserted as current fact."
  - field: "description_long"
    claim: "Playa de la Caleta is a sheltered, Blue Flag cove beach flanked by Castillo de San Sebastián and Castillo de Santa Catalina, with full visitor services."
    source_url: "https://andalucia.com/cadiz/beaches.htm"
    source_type: secondary
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "Consistent across several independent secondary sources (spain.info, idealista, Barceló); no official government beach-quality page was successfully fetched directly in this pass (cadizturismo.com returned HTTP 403)."
  - field: "driving_time_from_casa_de_la_familia"
    claim: "One-way driving route from Casa de la Familia to Catedral de Cádiz is approximately 160 minutes (213 km)."
    source_url: "https://router.project-osrm.org/route/v1/driving/-4.6626875,36.5356875;-6.2953183,36.5289521?overview=false"
    source_type: secondary
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "OSRM public routing engine, driving profile; traffic not modelled."
review_issues:
  - code: schedule_unverified
    severity: warning
    fields: [visit_information.schedule, cost_level]
    description: "The official cathedral site's schedule notices are not clearly dated for the current year; current 2026 hours and the exact ticket price need direct reconfirmation (e.g. via shop.articketing.com)."
    retryable: true
    owner: fact_check
  - code: excursion_layer_scope
    severity: warning
    fields: [status]
    description: "Included under the owner decision of 2026-10-15 to add an excursion layer (route-checked one-way drive up to about 4 h) beyond the 30 km primary area. Pending editor-of-record approval and change-log entry."
    retryable: true
    owner: editor
  - code: visitor_facilities_unverified
    severity: warning
    fields: [accessibility, wheelchair_friendly, parking, dog_friendly, toilets_available, food_available, booking_required]
    description: "Visitor facilities, access, parking and booking remain unverified for the cathedral."
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

Fact-checked 2026-10-15: coordinates and driving time resolved; cathedral hours/price and Playa de la Caleta described with sourced but partly secondary facts. Draft source notes (import): Created from the Danish excursion catalogue of 2026-10-15 (an inspiration document, not a source). The Maps link is a place lookup, not a saved-list link.
