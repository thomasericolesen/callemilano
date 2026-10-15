---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-ANTEQUERA-001
slug: antequera
name: Antequera
category: City
tags:
  - Historic town
  - Museum
  - Restaurant
  - Full day
coordinates:
  latitude: 37.0144361
  longitude: -4.5577719
  purpose: venue
  label: "Alcazaba de Antequera (hilltop fortress)"
  source: https://www.openstreetmap.org/way/495226025
  checked_at: 2026-10-15
google_maps_url: https://maps.google.com/?q=Antequera%2C+M%C3%A1laga%2C+Spain
external_ids: {}
municipality: Antequera
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: "65 min"
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: "Alcazaba de Antequera, Antequera, Málaga, Spain"
  source: "https://router.project-osrm.org/route/v1/driving/-4.6626875,36.5356875;-4.5577719,37.0144361?overview=false"
  checked_at: 2026-10-15
  note: "Route-checked one-way via OSRM (driving profile), ~80.9 km. Actual time varies with traffic."
age_groups:
  - Young adults
family_score:
  small_children: unknown
  children: unknown
  young_adults: high
  seniors: unknown
energy_level: Medium
seasonality:
  - Spring
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
description_short: "Antequera is a historic Málaga-province town built around its hilltop Alcazaba, with the UNESCO-listed Dolmens of Antequera nearby; opening hours and prices still need official confirmation."
description_long: "Antequera is a historic town in Málaga province, about 65 minutes' drive from Casa de la Familia (route-checked). Its hilltop Alcazaba fortress is the town's best-known landmark; a government geodetic survey point and independent map data place it on the hill near the Arco de los Gigantes. The Dolmens of Antequera (Menga, Viera and El Romeral), a UNESCO World Heritage prehistoric site, are nearby and were running guided visits in 2023 (Tue–Sun for Menga/Viera, weekends for El Romeral), though that schedule is three years old and must be reconfirmed before publication. Secondary sources (not independently confirmed against an official page) suggest a combined Alcazaba/Real Colegiata ticket around €6 with free entry on some Tuesday afternoons — this has not been verified from antequera.es, turismo.antequera.es, or another official source, which could not be reached in this research pass, so no price or opening hours are published here yet. El Torcal de Antequera, a separate nearby nature reserve, is recorded in its own place entry and linked here once fact-checked."
seo_title: "Antequera, Málaga: Historic Town and Alcazaba"
seo_description: "Plan a visit to Antequera, Málaga province: the hilltop Alcazaba and nearby Dolmens of Antequera. Opening hours and prices pending official confirmation."
images: []
evidence:
  - field: "coordinates"
    claim: "The Alcazaba de Antequera is a hilltop fortress in Antequera; coordinates resolved via OpenStreetMap, cross-checked against a Spanish national geodetic survey benchmark inside the Alcazaba grounds (37.01525, -4.55667, within ~100 m)."
    source_url: https://www.openstreetmap.org/way/495226025
    source_type: maps_identity
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: high
    notes: "Cross-check source: Instituto Geográfico Nacional (IGN) geodetic benchmark sheet, https://datos-geodesia.ign.es/REDNAP/Lin00584/584062.pdf (government)."
  - field: "description_long"
    claim: "Antequera was designated a 'Municipio Turístico de Andalucía' by the Junta de Andalucía in 2020."
    source_url: "https://cdn.juntadeandalucia.es/boja/2020/40/BOJA20-040-00003-2984-01_00170421.pdf"
    source_type: government
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: high
    notes: "Official regional gazette (BOJA); background context only, not a visitor-facing fact."
  - field: "description_long"
    claim: "The Dolmens of Antequera ran guided visits in 2023 on a published schedule (Menga/Viera Tue–Sun 10:30–12:00, El Romeral weekends/holidays 12:00–14:00)."
    source_url: "https://juntadeandalucia.es/sites/default/files/inline-files/2023/07/MENGASTONE_2023_web.pdf"
    source_type: government
    checked_at: 2026-10-15
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "Three-year-old document; current schedule must be reconfirmed before publication."
review_issues:
  - code: official_links_unverified
    severity: blocking
    fields: [links, visit_information]
    description: "No official Antequera municipal or tourism-office page (antequera.es / turismo.antequera.es) could be reached in this research pass. Alcazaba opening hours and ticket price are therefore unknown and unpublished; a secondary, unverified figure (~€6, possible Tuesday free entry) was found but is not cited as fact. Needs a direct follow-up fetch."
    retryable: true
    owner: fact_check
  - code: overlap_torcal
    severity: warning
    fields: [related_places]
    description: "Combined with El Torcal in the catalogue; keep as two records and link via related_places after both are fact-checked."
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
    fields: [accessibility, wheelchair_friendly, parking, dog_friendly, toilets_available, cost_level, booking_required]
    description: "Visitor facilities, access, parking, booking and cost remain unverified; no official Antequera source was reachable this round."
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

Fact-checked 2026-10-15: coordinates and driving time resolved; Alcazaba opening hours/price and official town links remain unresolved (antequera.es/turismo.antequera.es unreachable this round) — flagged as a blocking fact-check issue rather than guessed. Draft source notes (import): Created from the Danish excursion catalogue of 2026-10-15 (an inspiration document, not a source). The Maps link is a place lookup, not a saved-list link.
