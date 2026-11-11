---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-MONDA-001
slug: monda
name: Monda
category: City
tags:
- Restaurant
- Viewpoint
- Historic town
- Full day
- Premium
coordinates:
  latitude: 36.6306259
  longitude: -4.835327899999999
  purpose: town_center
  label: Castillo de la Villeta (Hotel Castillo de Monda), C. Castillo, 29110 Monda, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJCylSNqPbcg0RA9mEPCApF1M, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=5987299448043395331
external_ids:
  google_place_id: ChIJCylSNqPbcg0RA9mEPCApF1M
municipality: Monda
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 35 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Castillo de la Villeta (Hotel Castillo de Monda), C. Castillo, 29110 Monda, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.6306259,-4.835327899999999); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6306259%2C-4.835327899999999&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 35 min, 29.5 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: medium
  children: medium
  young_adults: medium
  seniors: medium
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
  official_website: http://www.castillodemonda.com/
  booking: null
  visitor_information: https://www.andalucia.org/es/monda
  transport: null
  contact: null
related_places: []
description_short: 'Monda: whitewashed village below a rebuilt castle, now a hotel, on the edge of the Sierra de las Nieves.'
description_long: Monda sits in the foothills of the Sierra de las Nieves, whose natural area includes part of the municipality. Its narrow, steep streets of whitewashed houses are overlooked by the castle, rebuilt on the ruins of the Arab fortress and now used as a hotel (Andalusian tourist board). The record point is the castle hotel. About 35 minutes by car from Casa de la Familia.
seo_title: Monda, Monda | CalleMilano
seo_description: 'Monda (Monda): what to see and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Castillo de la Villeta (Hotel Castillo de Monda)' at C. Castillo, 29110 Monda, Málaga, España (36.6306259,-4.835327899999999), primary type castle.
  source_url: https://maps.google.com/?cid=5987299448043395331
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 35 min by car (29.5 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6306259%2C-4.835327899999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long
  claim: 'Andalucía tourist board: ''se asienta en las estribaciones de la Sierra de las Nieves''; ''calles estrechas y empinadas con casas de fachadas encaladas sobre las que domina la silueta del castillo, levantado sobre ruinas de la antigua fortaleza árabe y recuperado para uso turístico''; ''su interior se ha convertido en hotel''.'
  source_url: https://www.andalucia.org/es/monda
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour towns fact check 2026-11-02)
  confidence: high
  notes: Read with Firecrawl (direct quotes) or directly on 2026-11-02. Supports the description of sights only; not opening hours, access or suitability.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults medium, seniors medium; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Restaurant, Viewpoint, Historic town, Full day, Premium."
  source_url: https://claude.ai/artifact/DZv9cLLQ1BEcYs3NeewdEF
  source_type: secondary
  checked_at: '2026-11-11'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-11
  confidence: medium
  notes: Owner's own judgment on the tag checklist on 2026-11-11 (previous tags were estimates from import); not independently verified. source_type secondary is the nearest schema value.
review_issues:
- code: category_editorial_choice
  severity: info
  fields:
  - category
  description: 'Category ''City'' chosen by Claude (towns: City; marinas and sights: Excursions). Confirm at editorial review.'
  retryable: true
  owner: human_editor
- code: facts_partly_checked
  severity: warning
  fields:
  - parking
  - accessibility
  - visit_information
  description: Description checked against official tourism sources 2026-11-02. Parking, accessibility and practical visit information are still open.
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
