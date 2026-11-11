---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-BENAHAVIS-001
slug: benahavis
name: Benahavís
category: City
tags:
- Nature
- Viewpoint
- Historic town
- Half day
- Free
coordinates:
  latitude: 36.5174193
  longitude: -5.0450107
  purpose: town_center
  label: Benahavís, 29679 Benahavís, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJFffGQ0fVcg0ReCGEqx44f6w, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=12429715200943595896
external_ids:
  google_place_id: ChIJFffGQ0fVcg0ReCGEqx44f6w
municipality: Benahavís
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 48 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Benahavís, 29679 Benahavís, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5174193,-5.0450107); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5174193%2C-5.0450107&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 48 min, 47.3 km. One predicted sample.'
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
  official_website: null
  booking: null
  visitor_information: https://www.andalucia.org/es/benahavis
  transport: null
  contact: null
related_places: []
description_short: 'Benahavís: white hill village in the most mountainous municipality of the western Costa del Sol.'
description_long: Benahavís is on the southern slope of the Serranía de Ronda, the most mountainous municipality of the western Costa del Sol, crossed by the Guadalmina, Guadaiza and Guadalmanza rivers. The village keeps traits of its Arab origin in the white-village style; the remains of the Castillo de Montemayor and a 16th-century palace are its listed monuments. Natural spots in the municipality include the Charco de las Mozas and the Embalse de la Leche (Andalusian tourist board). The Angosturas gorge on the Guadalmina is a separate candidate. About 48 minutes by car from Casa de la Familia.
seo_title: Benahavís, Benahavís | CalleMilano
seo_description: 'Benahavís (Benahavís): what to see and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Benahavís' at 29679 Benahavís, Málaga, España (36.5174193,-5.0450107), primary type None.
  source_url: https://maps.google.com/?cid=12429715200943595896
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 48 min by car (47.3 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5174193%2C-5.0450107&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long
  claim: 'Andalucía tourist board: ''el municipio más montañoso de la Costa del Sol occidental''; rivers Guadalmina, Guadaiza, Guadalmanza; ''el Charco de las Mozas y el embalse de la Leche''; ''el Castillo de Montemayor y un antiguo palacio del siglo XVI''.'
  source_url: https://www.andalucia.org/es/benahavis
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour towns fact check 2026-11-02)
  confidence: high
  notes: Read with Firecrawl (direct quotes) or directly on 2026-11-02. Supports the description of sights only; not opening hours, access or suitability.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults medium, seniors medium; energy_level Medium.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Nature, Viewpoint, Historic town, Half day, Free."
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
