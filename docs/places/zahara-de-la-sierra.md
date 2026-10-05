---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-CAD-ZAHARA-DE-LA-SIERRA-001
slug: zahara-de-la-sierra
name: Zahara de la Sierra
category: City
tags:
  - Historic town
  - Viewpoint
  - Nature
coordinates:
  latitude: 36.840068
  longitude: -5.388687
  purpose: representative_point
  label: Municipal tourism office, C/ Camino Nazarí
  source: https://www.zaharadelasierra.es/turismo-zahara
  checked_at: 2026-10-03
google_maps_url: https://maps.google.com/?q=Zahara+de+la+Sierra%2C+C%C3%A1diz%2C+Spain
external_ids: {}
municipality: Zahara de la Sierra
province: Cádiz
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: null
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Municipal tourism office, C/ Camino Nazarí, Zahara de la Sierra, Cádiz, Spain
  source: null
  checked_at: null
  note: One-way route duration not verified; check a current routing source.
age_groups:
  - Small children (0-6)
  - Children (7-12)
  - Teenagers (13-17)
  - Adults
  - Seniors
family_score:
  small_children: low
  children: medium
  teenagers: high
  adults: high
  seniors: low
energy_level: High
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
booking_required: false
dog_friendly: unknown
toilets_available: unknown
food_available: unknown
cost_level: Unknown
visit_information:
  schedule: "Town walk is not a scheduled attraction; opening schedules for monuments and visitor services are unverified."
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: https://www.zaharadelasierra.es/
  booking: null
  visitor_information: https://www.zaharadelasierra.es/turismo-zahara
  transport: null
  contact: https://www.zaharadelasierra.es/turismo-zahara
related_places: []
description_short: "A hilltop village in Cádiz with a historic center, viewpoints, and a castle above the town."
description_long: "Zahara de la Sierra's municipal tourism site highlights its historic heritage, viewpoints, and the Torre del Homenaje at the castle's highest point. The municipal tourism office is used as the representative arrival pin. Reaching elevated viewpoints involves walking uphill; exact route gradients, step-free access, parking, facilities, monument schedules, and summer suitability have not been verified. The town's tourism office notes that guided visits pause during the hottest part of summer, so check current conditions before planning."
seo_title: "Zahara de la Sierra: Historic Village and Castle Views"
seo_description: "Discover Zahara de la Sierra in Cádiz, with a historic center, viewpoints, and its hilltop castle. Check current access and visitor information before travelling."
images: []
evidence:
  - field: "coordinates"
    claim: "The municipal tourism site links its visitor office location to a Google Maps point at these coordinates."
    source_url: https://www.zaharadelasierra.es/turismo-zahara
    source_type: government
    checked_at: 2026-10-03
    checked_by: maps-import-agent
    confidence: high
    notes: "Coordinate represents the visitor-office arrival point, not the castle or whole town."
  - field: "description_short, description_long, tags"
    claim: "Municipal tourism information highlights the town's heritage, viewpoints, and Torre del Homenaje at the castle."
    source_url: https://www.zaharadelasierra.es/turismo-zahara
    source_type: government
    checked_at: 2026-10-03
    checked_by: maps-import-agent
    confidence: high
    notes: null
  - field: "description_long, seasonality"
    claim: "The municipal tourism site says guided visits pause during hot summer conditions."
    source_url: https://www.zaharadelasierra.es/turismo-zahara
    source_type: government
    checked_at: 2026-10-03
    checked_by: maps-import-agent
    confidence: high
    notes: "Check again before travel; schedule is time-sensitive."
review_issues:
  - code: driving_time_unverified
    severity: blocking
    fields: [driving_time_from_casa_de_la_familia]
    description: "Verify one-way drive time from Casa de la Familia and record route source and check date."
    retryable: true
    owner: fact_check
  - code: family_ratings_estimated
    severity: warning
    fields: [age_groups, family_score, energy_level, seasonality]
    description: "Audience ratings, energy, and suitable seasons are provisional editorial estimates; confirm hill access, heat exposure, and route demands."
    retryable: true
    owner: editorial
  - code: visitor_facilities_unverified
    severity: warning
    fields: [accessibility, wheelchair_friendly, parking, dog_friendly, toilets_available, food_available, cost_level]
    description: "Access, parking, facilities, dog policy, and costs remain unverified."
    retryable: true
    owner: fact_check
created_at: 2026-10-03
updated_at: 2026-10-03
last_verified: 2026-10-03
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---

Draft source notes: Zahara de la Sierra municipal tourism pages checked on 2026-10-03. The municipality's map link was used for the visitor-office representative pin. No user-provided saved-place URL was supplied; the Maps search link is a place lookup, not a saved-list link.
