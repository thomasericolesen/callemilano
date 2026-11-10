---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-ALORA-001
slug: alora
name: Álora
category: City
tags: []
coordinates:
  latitude: 36.819586799999996
  longitude: -4.704041699999999
  purpose: town_center
  label: Castillo de Álora, C. Ancha, s/n, 29500 Álora, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ36qTmPXqcg0Rm9iWJqc8780, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=14839145985813698715
external_ids:
  google_place_id: ChIJ36qTmPXqcg0Rm9iWJqc8780
municipality: Álora
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 50 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Castillo de Álora, C. Ancha, s/n, 29500 Álora, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.819586799999996,-4.704041699999999); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.819586799999996%2C-4.704041699999999&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 50 min, 46.0 km. One predicted sample.'
age_groups:
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: low
  children: medium
  young_adults: high
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
  official_website: http://www.alora.es/
  booking: null
  visitor_information: https://www.andalucia.org/es/alora
  transport: null
  contact: null
related_places: []
description_short: 'Álora: white town on a hill over the Guadalhorce valley, with steep streets up to its castle.'
description_long: Álora stands on a small hill commanding the Guadalhorce valley from the north. Its Arab-origin streets climb steeply to the castle, the town's symbol, which is unusual in being used as the cemetery; the Iglesia de la Encarnación is its main church. The Desfiladero de los Gaitanes (Caminito del Rey area) and the Sierra de Huma and Sierra de Aguas are in the surroundings (Andalusian tourist board). The record point is the castle; families should know it is a working cemetery. The streets are steep, so energy is set to Medium. About 50 minutes by car from Casa de la Familia.
seo_title: Álora, Álora | CalleMilano
seo_description: 'Álora (Álora): what to see and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Castillo de Álora' at C. Ancha, s/n, 29500 Álora, Málaga, España (36.819586799999996,-4.704041699999999), primary type castle.
  source_url: https://maps.google.com/?cid=14839145985813698715
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 50 min by car (46.0 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.819586799999996%2C-4.704041699999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long
  claim: 'Andalucía tourist board: ''situación sobre el Valle del Guadalhorce''; ''empinadas calles que conducen al castillo: símbolo del pueblo, y cuya originalidad radica en que es utilizado como cementerio''; ''el Desfiladero de los Gaitanes ... la sierra de Huma o la sierra de Aguas''; ''la Iglesia de la Encarnación''.'
  source_url: https://www.andalucia.org/es/alora
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour towns fact check 2026-11-02)
  confidence: high
  notes: Read with Firecrawl (direct quotes) or directly on 2026-11-02. Supports the description of sights only; not opening hours, access or suitability.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children unknown, children medium, young_adults high, seniors medium; energy_level Medium.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children low, children medium, young_adults high, seniors medium; energy_level Medium. Replaces the owner''s earlier answer on the same checklist.'
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
updated_at: '2026-11-10'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
