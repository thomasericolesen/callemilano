---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-EL-GRAN-PARQUE-DE-MIJAS-001
slug: el-gran-parque-de-mijas
name: El Gran Parque de Mijas
category: Family activities
tags:
- Nature
- Adventure
- Half day
- Free
coordinates:
  latitude: 36.539559499999996
  longitude: -4.656531
  purpose: venue
  label: El Gran Parque de Mijas, Cl. Buitre, 29651 Las Lagunas de Mijas, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJETGGUwDhcg0RCUl3V52-r-8, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=17271232678975719689
external_ids:
  google_place_id: ChIJETGGUwDhcg0RCUl3V52-r-8
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 3 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: El Gran Parque de Mijas, Cl. Buitre, 29651 Las Lagunas de Mijas, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.539559499999996,-4.656531); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.539559499999996%2C-4.656531&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 3 min, 1.08 km. Walking (Routes API WALK, same day): 13 min, 1.01 km. One predicted sample, not the Google Maps app''s main figure.'
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
seasonality: []
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
description_short: 'El Gran Parque de Mijas: large public park in Las Lagunas de Mijas, about 13 min on foot or 3 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: 'El Gran Parque de Mijas is a large public park in Las Lagunas de Mijas at Cl. Buitre, 29651 Las Lagunas de Mijas, Málaga. From Casa de la Familia it is about 13 minutes on foot (1.01 km, Google''s walking route) or about 3 minutes by car (Google route check, Saturday 10:00). Owner''s own knowledge: Suitable for children, with water and play areas. Mijas Town Hall opened a splash park in the Gran Parque on 12 June 2026: 430 m², 41 interactive water features, open daily 10:00-22:00 in its season, room for 65 children, with three age zones (1-3, 4-9 and 10-11 years); children under 8 must be with an adult and babies must wear swim nappies; no balls, bikes or similar. Municipal media later reported that the water games closed for the season (date not confirmed). The rest of the park''s facilities and opening hours have not been checked.'
seo_title: El Gran Parque de Mijas, Mijas | CalleMilano draft record
seo_description: 'Draft record for El Gran Parque de Mijas (Mijas): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'El Gran Parque de Mijas' at Cl. Buitre, 29651 Las Lagunas de Mijas, Málaga, España (36.539559499999996,-4.656531), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=17271232678975719689
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia, description_long (walking time)
  claim: 'From Casa de la Familia: 3 min by car (1.08 km, Saturday 10:00 predicted traffic) and 13 min on foot (1.01 km).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.539559499999996%2C-4.656531&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00, and WALK (https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.539559499999996%2C-4.656531&travelmode=walking). Google's walking route says nothing about pavements, crossings or whether it suits children.
- field: description_long (owner knowledge)
  claim: Suitable for children, with water and play areas.
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/nearby-selection-2026-11-02.md
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: medium
  notes: Owner's own local knowledge, given on the nearby selection page on 2026-11-02; not independently verified.
- field: description_long (splash park)
  claim: 'Mijas Town Hall, 12 June 2026: splash park in the Gran Parque opened that day; 430 m2, 41 interactive elements; daily 10:00-22:00; max 65 children; zones baby 1-3, kids 4-9, teen 10-11; under-8s accompanied by an adult; swim nappies compulsory for babies; no balloons, balls, motor vehicles or bicycles; closed, recycled water circuit.'
  source_url: https://www.mijas.es/portal/el-ayuntamiento-de-mijas-abre-el-splash-park-del-gran-parque-una-zona-infantil-acuatica-con-41-elementos-interactivos/
  source_type: government
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: high
  notes: Read in full via Firecrawl on 2026-11-02.
- field: description_long (season end)
  claim: Municipal media (Mijas Comunicación) report that the Gran Parque water games have closed their season.
  source_url: https://x.com/MijasCom/status/2107018132921430263
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: low
  notes: Search excerpt only, read 2026-11-02; closing date not stated in the excerpt.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children high, children high, young_adults high, seniors high; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Nature, Adventure, Half day, Free."
  source_url: https://claude.ai/artifact/DZv9cLLQ1BEcYs3NeewdEF
  source_type: secondary
  checked_at: '2026-11-11'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-11
  confidence: medium
  notes: Owner's own judgment on the tag checklist on 2026-11-11 (previous tags were estimates from import); not independently verified. source_type secondary is the nearest schema value.
review_issues:
- code: no_official_website
  severity: info
  fields:
  - links
  description: Google lists no website; facts may have to come from a social page or a direct contact.
  retryable: true
  owner: fact_check
- code: park_facilities_and_hours_unknown
  severity: warning
  fields:
  - visit_information
  - toilets_available
  - parking
  - accessibility
  description: Only the splash park is sourced. Park opening hours, playgrounds, toilets and parking need a municipal source; the 2027 splash-park season is not announced.
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: '2026-11-02'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
