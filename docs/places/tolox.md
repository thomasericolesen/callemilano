---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-TOLOX-001
slug: tolox
name: Tolox
category: Excursions
tags:
  - Historic town
  - Nature
  - Half day
coordinates:
  latitude: 36.6850627
  longitude: -4.9114074
  purpose: venue
  label: "Balneario de Tolox (Fuente Amargosa), access road area"
  source: https://www.openstreetmap.org/way/56157662
  checked_at: 2026-10-15
google_maps_url: https://maps.google.com/?q=Tolox%2C+M%C3%A1laga%2C+Spain
external_ids: {}
municipality: Tolox
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: "56 min"
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: "Balneario de Tolox (Fuente Amargosa), Tolox, Málaga, Spain"
  source: "https://router.project-osrm.org/route/v1/driving/-4.6626875,36.5356875;-4.9114074,36.6850627?overview=false"
  checked_at: 2026-10-15
  note: "Route-checked one-way via OSRM (driving profile), ~43.7 km. Actual time varies with traffic."
age_groups:
  - Young adults
family_score:
  small_children: unknown
  children: unknown
  young_adults: high
  seniors: unknown
energy_level: Low
seasonality:
  - Summer
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
  schedule: "The spa's own site states it is open 1 June–16 October only; it is NOT open year-round. Today's date (2026-10-15) falls right at the edge of that stated season and could not be confirmed as currently open or closed from this research."
  typical_duration: null
  booking_lead_time: null
  valid_from: "2026-06-01"
  valid_until: "2026-10-16"
  cost_basis: null
  cost_checked_at: null
links:
  official_website: https://www.balneariodetolox.es/
  booking: null
  visitor_information: "https://andalucia.org/en/tolox-health-and-beauty-balneario-de-tolox-2"
  transport: null
  contact: "tel:+34952487091"
related_places: []
description_short: "Tolox is a small white-village spa town in Málaga province; its historic Balneario de Tolox (Fuente Amargosa) thermal spa is real and documented, but only operates seasonally (1 June–16 October), not year-round."
description_long: "Tolox sits at the foot of the Sierra de las Nieves, about 56 minutes' drive from Casa de la Familia (route-checked). The town's wellness draw is the Balneario de Tolox, also known as Fuente Amargosa: a thermal spa whose hypothermal, naturally gas-bearing waters were discovered in 1867 and have been used since 1869 for respiratory-condition treatments taken by inhalation; the current building dates to 1930, rebuilt after a major 1906 flood destroyed the original. Its own website states it is open only from 1 June to 16 October each year, not year-round — this directly resolves the open editorial question about Tolox's wellness offering, but also means any visit must be timed to that window; today's date (15 October) is right at the edge of the stated season, so current same-week opening could not be confirmed. Daily hours, current treatment prices, whether day visitors (not staying at the spa) can use the facilities, and the historic town centre's own sights have not yet been confirmed from an official source."
seo_title: "Tolox, Málaga: Seasonal Thermal Spa and Village"
seo_description: "Tolox's Balneario de Tolox thermal spa is seasonal (June-October), not year-round. Plan around the season and the drive from Casa de la Familia."
images: []
evidence:
  - field: "coordinates"
    claim: "Balneario de Tolox (Fuente Amargosa) sits on the Carretera del Balneario, the access road into the spa from Tolox village."
    source_url: https://www.openstreetmap.org/way/56157662
    source_type: maps_identity
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "This is the access road, not a confirmed point for the spa building itself; the spa's exact street address is reported inconsistently across secondary sources (Calle Extramuros s/n vs Calle Balneario s/n) and should be confirmed directly with the venue."
  - field: "visit_information.schedule, visit_information.valid_from, visit_information.valid_until, description_long, category"
    claim: "The Balneario de Tolox (Fuente Amargosa) is a real, operating thermal spa, open seasonally from 1 June to 16 October, specializing in inhalation treatments for respiratory conditions."
    source_url: https://www.balneariodetolox.es/
    source_type: official_venue
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: high
    notes: "Directly fetched from the spa's own site; resolves the open 'category_open' review issue about whether Tolox actually has a wellness offering."
  - field: "description_long"
    claim: "History of the spa: waters discovered 1867, spa opened 1869, rebuilt 1930 after a 1906 flood; waters are hypothermal and gas-bearing, taken by inhalation."
    source_url: "https://andalucia.org/en/tolox-health-and-beauty-balneario-de-tolox-2"
    source_type: official_tourism
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "Corroborated by secondary local-tourism sources; dates and flood year not independently cross-verified against a government archive."
  - field: "driving_time_from_casa_de_la_familia"
    claim: "One-way driving route from Casa de la Familia to the Balneario de Tolox area is approximately 56 minutes (43.7 km)."
    source_url: "https://router.project-osrm.org/route/v1/driving/-4.6626875,36.5356875;-4.9114074,36.6850627?overview=false"
    source_type: secondary
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "OSRM public routing engine, driving profile; traffic not modelled."
review_issues:
  - code: seasonal_opening_unconfirmed_this_week
    severity: blocking
    fields: [visit_information.schedule]
    description: "The spa's official season is stated as 1 June-16 October; today (2026-10-15) is within days of the season's stated end and current/same-week opening status was not confirmed by phone or a live booking page. Confirm directly before recommending a visit."
    retryable: true
    owner: fact_check
  - code: category_open
    severity: warning
    fields: [category, tags]
    description: "Resolved by this fact-check: Tolox's wellness offering is a real, named thermal spa (Balneario de Tolox / Fuente Amargosa) per its own official site, but it is seasonal (June-October), not year-round. Editor to confirm category/tags reflect the seasonal nature."
    retryable: false
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
    description: "Audience ratings, energy, season and duration tag are provisional editorial estimates for young adults; seasonality should be narrowed to reflect the spa's June-October operating window."
    retryable: true
    owner: editorial
  - code: visitor_facilities_unverified
    severity: warning
    fields: [accessibility, wheelchair_friendly, parking, dog_friendly, toilets_available, cost_level, booking_required]
    description: "Daily hours, current treatment prices, day-visitor access, parking and accessibility remain unverified."
    retryable: true
    owner: fact_check
  - code: layer_boundary_open
    severity: warning
    fields: [driving_time_from_casa_de_la_familia]
    description: "Tolox is within the 30 km primary-area straight-line radius (27.7 km per the generated catalog) with a route-checked one-way drive of only 56 minutes; editor to decide whether this record should move to the primary layer rather than excursions_4h."
    retryable: false
    owner: editorial
created_at: 2026-10-15
updated_at: 2026-10-15
last_verified: 2026-10-15
last_reviewed_at: null
next_review_at: 2027-04-01
review_decision: null
redirects: []
---

Fact-checked 2026-10-15: confirmed the Balneario de Tolox is real but seasonal (1 Jun-16 Oct), resolving the open category question; exact address, daily hours, prices and current same-week opening status remain unverified and are flagged, not guessed. Draft source notes (import): Created from the Danish excursion catalogue of 2026-10-15 (an inspiration document, not a source). The Maps link is a place lookup, not a saved-list link.
