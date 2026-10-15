---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-CAD-VEJER-DE-LA-FRONTERA-001
slug: vejer-de-la-frontera
name: Vejer de la Frontera
category: City
tags:
  - Historic town
  - Viewpoint
  - Restaurant
  - Overnight
coordinates:
  latitude: 36.2527948
  longitude: -5.9635372
  purpose: venue
  label: "Castillo de Vejer, hilltop old town"
  source: https://www.openstreetmap.org/relation/14594695
  checked_at: 2026-10-15
google_maps_url: https://maps.google.com/?q=Vejer+de+la+Frontera%2C+C%C3%A1diz%2C+Spain
external_ids: {}
municipality: Vejer de la Frontera
province: Cádiz
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: "153 min"
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: "Castillo de Vejer, Vejer de la Frontera, Cádiz, Spain"
  source: "https://router.project-osrm.org/route/v1/driving/-4.6626875,36.5356875;-5.9635372,36.2527948?overview=false"
  checked_at: 2026-10-15
  note: "Route-checked one-way via OSRM (driving profile), ~187.3 km. Actual time varies with traffic."
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
energy_level: Low
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
description_short: "Vejer de la Frontera is a white hill town in Cádiz province topped by a 10th-11th century castle once home to the Dukes of Medina Sidonia; opening hours and prices are unconfirmed and conflict across the sources found."
description_long: "Vejer de la Frontera is a hilltop white town in Cádiz province, about 2 hours 33 minutes' drive from Casa de la Familia (route-checked). Its Castillo de Vejer dates to the 10th-11th century, was once home to the Dukes of Medina Sidonia, and was declared a Historic-Artistic Monument (Bien de Interés Cultural) in 1931. Sources on the castle's current opening hours and admission price actively conflict: one account describes opening hours as historically 'erratic' with visitors advised to ask the tourist office; another claims a specific seasonal schedule and a small entrance fee; others describe free admission. None of these could be confirmed against an official ayuntamiento or tourist-office source in this research pass, so no hours or price are published here. The town's general character (narrow hilltop streets, views over the surrounding countryside toward the coast) is well attested across sources but has not been itemised into specific sourced facts yet."
seo_title: "Vejer de la Frontera: Hilltop Castle and White Town"
seo_description: "Visit Vejer de la Frontera's hilltop castle and old town in Cádiz province. Opening hours and prices pending official confirmation."
images: []
evidence:
  - field: "coordinates"
    claim: "Castillo de Vejer stands at the top of the old town in Vejer de la Frontera."
    source_url: https://www.openstreetmap.org/relation/14594695
    source_type: maps_identity
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: null
  - field: "description_long"
    claim: "The castle dates to the 10th-11th century, was once home to the Dukes of Medina Sidonia, and was declared a Bien de Interés Cultural (Historic-Artistic Monument) in 1931."
    source_url: "https://www.lonelyplanet.com"
    source_type: secondary
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "Corroborated across more than one independent secondary source for the historical claims, though no official heritage-register page was reached directly."
  - field: "driving_time_from_casa_de_la_familia"
    claim: "One-way driving route from Casa de la Familia to Castillo de Vejer is approximately 153 minutes (187.3 km)."
    source_url: "https://router.project-osrm.org/route/v1/driving/-4.6626875,36.5356875;-5.9635372,36.2527948?overview=false"
    source_type: secondary
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "OSRM public routing engine, driving profile; traffic not modelled."
review_issues:
  - code: hours_price_conflict
    severity: blocking
    fields: [visit_information, cost_level]
    description: "Sources conflict on the castle's opening hours (erratic/unscheduled vs. a specific seasonal timetable) and whether there is an admission fee. No official ayuntamiento or tourist-office source was reached. Do not publish a schedule or price until confirmed directly (e.g. by phone or a live official page)."
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
    description: "Visitor facilities, access, parking and booking remain unverified."
    retryable: true
    owner: fact_check
created_at: 2026-10-15
updated_at: 2026-10-15
last_verified: 2026-10-15
last_reviewed_at: 2026-10-15
next_review_at: 2027-01-15
review_decision: null
redirects: []
---

Fact-checked 2026-10-15: coordinates and driving time resolved; castle hours and admission price actively conflict across sources with no official source reached, so neither is published — flagged as a blocking fact-check issue. Draft source notes (import): Created from the Danish excursion catalogue of 2026-10-15 (an inspiration document, not a source). The Maps link is a place lookup, not a saved-list link.
