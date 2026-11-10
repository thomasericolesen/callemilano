---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-BENALMADENA-PUEBLO-001
slug: benalmadena-pueblo
name: Benalmádena Pueblo
category: City
tags: []
coordinates:
  latitude: 36.5964743
  longitude: -4.5197688
  purpose: town_center
  label: Benalmádena, Benalmádena, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJP-IFYLf8cg0RGlDfOjxP8gw, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=932895192923459610
external_ids:
  google_place_id: ChIJP-IFYLf8cg0RGlDfOjxP8gw
municipality: Benalmádena
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 25 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Benalmádena, Benalmádena, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5964743,-4.5197688); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5964743%2C-4.5197688&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 25 min, 19.5 km. One predicted sample, not the Google Maps app''s main figure.'
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
energy_level: Medium
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
  official_website: https://www.thisisbenalmadena.travel/descubre/las-3-benalmadenas/benalmadena-pueblo/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Benalmádena Pueblo: the old village of Benalmádena, about 25 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: 'Benalmádena Pueblo is the old village of Benalmádena (Benalmádena, Málaga, España). From Casa de la Familia it is about 25 minutes by car (Google route check, Saturday 10:00). Benalmádena''s official tourism site (This is Benalmádena, checked 2026-11-02): the original old village, about 300 m up the mountainside with the Mediterranean as backdrop; narrow cobbled streets, whitewashed façades with flower pots and quiet squares. Sights include Plaza de España, the Iglesia de Santo Domingo de Guzmán, the Jardines del Muro (gardens along the line of the medieval wall) and La Niña de Benalmádena, a sculpture by Jaime Pimentel. Check before visiting.'
seo_title: Benalmádena Pueblo, Benalmádena | CalleMilano draft record
seo_description: 'Draft record for Benalmádena Pueblo (Benalmádena): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Benalmádena' at Benalmádena, Málaga, España (36.5964743,-4.5197688), business status None, primary type None.
  source_url: https://maps.google.com/?cid=932895192923459610
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 25 min by car (19.5 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5964743%2C-4.5197688&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time over 20 minutes, so not shown (owner rule).
- field: description_long
  claim: 'thisisbenalmadena.travel ''Benalmádena Pueblo'': ''Encaramado en la ladera de la sierra y con el Mediterráneo como telón de fondo''; ''calles estrechas y empedradas, sus fachadas encaladas adornadas con macetas''; Iglesia de Santo Domingo de Guzmán, Jardines del Muro (siguen el trazado de la muralla medieval), escultura La Niña (Jaime Pimentel); Plaza de España: casco antiguo ''a unos 300 metros de altitud''.'
  source_url: https://www.thisisbenalmadena.travel/descubre/las-3-benalmadenas/benalmadena-pueblo/
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: high
  notes: Read via Firecrawl on 2026-11-02. Site of Benalmádena's tourism department (assumed from content; publisher not stated on the pages read).
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults medium, seniors medium; energy_level Medium. Owner note (Danish): ''Hvid by men mange seværdigheder''.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
review_issues:
- code: category_editorial_choice
  severity: info
  fields:
  - category
  description: 'Category ''City'' was chosen by Claude from the schema definitions (routes and sights: Excursions; towns: City; natural areas: Nature; visitor attractions: Family activities). Confirm at editorial review.'
  retryable: true
  owner: human_editor
- code: visit_practicalities_unchecked
  severity: warning
  fields:
  - parking
  - accessibility
  - transport_options
  description: Parking, buses and accessibility were not checked.
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-10'
last_verified: '2026-11-02'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
