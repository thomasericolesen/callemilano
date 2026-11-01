---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-MARBELLA-OLD-TOWN-001
slug: marbella-old-town
name: Marbella Old Town
category: City
tags:
  - Historic town
  - Museum
  - Restaurant
  - Half day
coordinates:
  latitude: 36.5101033
  longitude: -4.8849716
  purpose: town_center
  label: Plaza de los Naranjos
  source: https://www.juntadeandalucia.es/cultura/agendaculturaldeandalucia/espacios/marbella-casco-antiguo
  checked_at: 2026-10-03
google_maps_url: https://maps.google.com/?q=Marbella+Old+Town%2C+M%C3%A1laga%2C+Spain
external_ids: {}
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 35 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Old Town Marbella parking, Av. del Mar 14, 29602 Marbella, Málaga, Spain (a car park, not Plaza de los Naranjos)
  source: Google Routes API computeRoutes, run 2026-11-01 from the project origin (36.5356875, -4.6626875); destination = record coordinates (36.5101033,-4.8849716); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5101033%2C-4.8849716&travelmode=driving
  checked_at: '2026-11-01'
  note: 'Routes API figure: 35 min with predicted Saturday 10:00 traffic (35 min without traffic), 28.9 km via A-7; an avoid-tolls run gave 35 min. One predicted sample, not the Google Maps app''s main figure; traffic and season change the time. Previous value 36 min (2026-10-29): Google Maps, measured by the owner (Eric Olesen) on 2026-10-29 from Calle Milano. Batch: data/route-checks-2026-11-01-local.csv.'
age_groups:
  - Small children (0-6)
  - Children (7-12)
  - Young adults
  - Seniors
family_score:
  small_children: medium
  children: high
  young_adults: high
  seniors: medium
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
  availability: "Google Maps lists a car park 'Old Town Marbella parking' at Av. del Mar 14; price, hours, capacity and the walk to Plaza de los Naranjos are not verified."
  location_type: nearby
  cost: unknown
  restrictions: unknown
  walk_distance: unknown
  source: https://maps.app.goo.gl/GXxtiiSjGwB5qGdZ6
  checked_at: 2026-10-29
transport_options: []
booking_required: false
dog_friendly: unknown
toilets_available: unknown
food_available: "yes"
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
  official_website: https://turismo.marbella.es/
  booking: null
  visitor_information: https://turismo.marbella.es/vive/cultura/patrimonio-historico/casco-historico.html
  transport: null
  contact: null
related_places: []
description_short: "Walk Marbella's historic center, with heritage streets, plazas, museums, and places to eat."
description_long: "Marbella's municipal tourism site describes the historic center's Roman, Arab, and Christian heritage, including the old walls, museums, chapels, plazas, restaurants, and traditional shops. Plaza de los Naranjos is used as the representative central point. The drive to the old-town car park at Av. del Mar 14 is about 36 minutes (Google Maps, toll roads avoided, owner-measured 2026-10-29, live traffic). This is a walk-through urban visit; step-free routes, public parking, toilets, and current museum schedules or admission details have not been checked."
seo_title: "Marbella Old Town: Historic Center and Plazas"
seo_description: "Explore Marbella Old Town's historic streets, plazas, museums, and restaurants. Check current access, parking, and museum details before visiting."
images: []
evidence:
  - field: "coordinates"
    claim: "Plaza de los Naranjos is the representative center point for Marbella's old town."
    source_url: https://www.juntadeandalucia.es/cultura/agendaculturaldeandalucia/espacios/marbella-casco-antiguo
    source_type: government
    checked_at: 2026-10-03
    checked_by: maps-import-agent
    confidence: high
    notes: "Official regional cultural listing locates the old town at Plaza de los Naranjos."
  - field: "description_long, tags, food_available"
    claim: "Marbella's historic center contains historic heritage, museums, plazas, restaurants, and shops."
    source_url: https://turismo.marbella.es/vive/cultura/patrimonio-historico/casco-historico.html
    source_type: official_tourism
    checked_at: 2026-10-03
    checked_by: maps-import-agent
    confidence: high
    notes: null
  - field: "driving_time_from_casa_de_la_familia, parking"
    claim: "Google Maps drive time from Calle Milano 35 to 'Old Town Marbella parking' (Av. del Mar 14) is 36 min (27.3 km via A-7)."
    source_url: https://maps.app.goo.gl/GXxtiiSjGwB5qGdZ6
    source_type: maps_identity
    checked_at: 2026-10-29
    checked_by: "fact-check-agent"
    confidence: medium
    notes: "Measured by the owner, toll roads avoided, Thursday 2026-10-29 around 15:00 with live traffic. One sample. The official municipal tourism page (turismo.marbella.es, re-read 2026-10-29) lists the sights of the old town but gives no opening hours, parking or access details."
  - field: driving_time_from_casa_de_la_familia
    claim: 'One-way drive from Casa de la Familia to Old Town Marbella parking, Av. del Mar 14, 29602 Marbella, Málaga, Spain (a car park, not Plaza de los Naranjos): 35 min, 28.9 km (Saturday 10:00 predicted traffic).'
    source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5101033%2C-4.8849716&travelmode=driving
    source_type: secondary
    checked_at: '2026-11-01'
    checked_by: Claude (Routes API batch 2026-11-01)
    confidence: medium
    notes: Google Routes API computeRoutes; destination = record coordinates (36.5101033,-4.8849716). Predicted-traffic estimate for one departure time; the local_30km rule uses the Google Maps app's main figure.
review_issues:
  - code: family_ratings_estimated
    severity: warning
    fields: [age_groups, family_score, energy_level, tags.Half day]
    description: "Audience ratings, energy, and visit-duration tag are provisional editorial estimates for an urban walking visit; assess route demands and typical visit time before approval."
    retryable: true
    owner: editorial
  - code: visitor_facilities_unverified
    severity: warning
    fields: [accessibility, wheelchair_friendly, parking, dog_friendly, toilets_available, cost_level]
    description: "Visitor facilities, access, parking, and cost remain unverified."
    retryable: true
    owner: fact_check
created_at: 2026-10-03
updated_at: 2026-10-29
last_verified: 2026-10-29
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---

Draft source notes: Marbella municipal tourism and regional cultural listing checked on 2026-10-03. No user-provided saved-place URL was supplied; the Maps search link is a place lookup, not a saved-list link.
