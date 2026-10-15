---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-CAD-TARIFA-001
slug: tarifa
name: Tarifa
category: City
tags:
  - Beach
  - Restaurant
  - Full day
coordinates:
  latitude: 36.0116776
  longitude: -5.6028099
  purpose: venue
  label: "Castillo de Guzmán el Bueno, old town, near the port"
  source: https://www.openstreetmap.org/way/79620499
  checked_at: 2026-10-15
google_maps_url: https://maps.google.com/?q=Tarifa%2C+C%C3%A1diz%2C+Spain
external_ids: {}
municipality: Tarifa
province: Cádiz
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: "116 min"
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: "Castillo de Guzmán el Bueno, Tarifa, Cádiz, Spain"
  source: "https://router.project-osrm.org/route/v1/driving/-4.6626875,36.5356875;-5.6028099,36.0116776?overview=false"
  checked_at: 2026-10-15
  note: "Route-checked one-way via OSRM (driving profile), ~138.1 km. Actual time varies with traffic."
age_groups:
  - Teenagers (13-17)
  - Adults
family_score:
  small_children: unknown
  children: unknown
  teenagers: high
  adults: high
  seniors: unknown
energy_level: Medium
seasonality:
  - Spring
  - Summer
  - Autumn
accessibility:
  overall: unknown
  mobility:
    route: "Castle involves stairs and uneven ground per a tour operator's description; no official accessibility statement found."
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
description_short: "Tarifa, Spain's southernmost mainland town, pairs a Caliphate-era castle and old town with a strong year-round wind that makes it a major kitesurf and windsurf destination; official opening hours and prices for the castle are not yet confirmed."
description_long: "Tarifa sits at Spain's southern tip facing the Strait of Gibraltar, about 1 hour 56 minutes' drive from Casa de la Familia (route-checked). Its Castillo de Guzmán el Bueno, a 10th-century fortress built under Caliph Abderramán III of Córdoba, overlooks the port and the strait toward Morocco; secondary sources describe free entry with no advance booking, but this has not been confirmed from an official heritage or municipal source, so no hours or price are published here yet. The old town has three notable churches built partly over former mosques (San Mateo, San Francisco de Asís, Santa María). The town is consistently described across independent sources as a major kitesurfing and windsurfing destination because of the strong, near-constant 'levante' wind. Tarifa neighbours Duna de Bolonia and Baelo Claudia, both separate existing records, along the coast road toward Cádiz. Castle opening hours, admission price, and accessibility have not been confirmed from an official source."
seo_title: "Tarifa, Cádiz: Castle, Old Town and Wind Sports"
seo_description: "Visit Tarifa's historic castle and old town, known for kitesurfing and windsurfing. Hours and prices pending official confirmation; drive time from Casa de la Familia."
images: []
evidence:
  - field: "coordinates"
    claim: "Castillo de Guzmán el Bueno stands in Tarifa's old town near the port."
    source_url: https://www.openstreetmap.org/way/79620499
    source_type: maps_identity
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: high
    notes: "Cross-checked against an independent secondary (Wikipedia) coordinate within a few metres."
  - field: "description_long"
    claim: "The castle is a 10th-century Caliphate-era fortress built under Abderramán III of Córdoba, overlooking the Strait of Gibraltar."
    source_url: "https://en.wikipedia.org/wiki/Castle_of_Tarifa"
    source_type: secondary
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "Seen via search snippet; recommend a direct re-check of the live Wikipedia infobox and an official heritage source."
  - field: "description_long, tags"
    claim: "Tarifa is a major kitesurfing/windsurfing destination due to the strong, near-constant 'levante' wind."
    source_url: "https://www.barcelo.com"
    source_type: secondary
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "Consistent across multiple independent secondary travel sources."
  - field: "driving_time_from_casa_de_la_familia"
    claim: "One-way driving route from Casa de la Familia to Castillo de Guzmán el Bueno, Tarifa, is approximately 116 minutes (138.1 km)."
    source_url: "https://router.project-osrm.org/route/v1/driving/-4.6626875,36.5356875;-5.6028099,36.0116776?overview=false"
    source_type: secondary
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "OSRM public routing engine, driving profile; traffic not modelled."
review_issues:
  - code: official_source_needed
    severity: blocking
    fields: [visit_information, cost_level, links]
    description: "No official heritage-authority or ayuntamiento page for the Castillo de Guzmán el Bueno was reached; opening hours and admission price are unconfirmed and unpublished. A candidate official site (aytotarifa.com or turismodetarifa.es) was found but not independently verified live."
    retryable: true
    owner: fact_check
  - code: overlap_bolonia
    severity: warning
    fields: [related_places]
    description: "Neighbours Duna de Bolonia and Baelo Claudia (both already in docs/places/); link via related_places after fact check."
    retryable: true
    owner: editorial
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
    fields: [accessibility, wheelchair_friendly, parking, dog_friendly, toilets_available, food_available, booking_required]
    description: "Visitor facilities, access, parking and booking remain unverified."
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

Fact-checked 2026-10-15: coordinates and driving time resolved; castle opening hours/price could not be confirmed from an official source this round and are flagged as a blocking fact-check issue rather than estimated. Draft source notes (import): Created from the Danish excursion catalogue of 2026-10-15 (an inspiration document, not a source). The Maps link is a place lookup, not a saved-list link.
