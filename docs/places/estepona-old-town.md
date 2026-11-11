---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-ESTEPONA-OLD-TOWN-001
slug: estepona-old-town
name: Estepona old town
category: City
tags:
- Historic town
- Half day
- Free
coordinates:
  latitude: 36.4257878
  longitude: -5.145206
  purpose: town_center
  label: Plaza de las Flores, Plaza de las Flores, 29680 Estepona, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJnbmPqafWDA0RhcX3ivZG014, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=6832883084358567301
external_ids:
  google_place_id: ChIJnbmPqafWDA0RhcX3ivZG014
municipality: Estepona
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 53 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Plaza de las Flores, Plaza de las Flores, 29680 Estepona, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4257878,-5.145206); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4257878%2C-5.145206&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 53 min, 59.3 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: medium
  children: medium
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
  visitor_information: https://www.spain.info/es/destino/estepona/
  transport: null
  contact: null
related_places:
- playa-de-la-rada-estepona
description_short: 'Estepona old town: white streets full of flower pots, Plaza de las Flores and an open-air mural route.'
description_long: 'Estepona''s old town is known for whitewashed streets decorated with flower-filled pots around the Plaza de las Flores. The town has art routes: the Ruta de Murales with more than 40 works, a sculpture route with more than 30 pieces and a poetry route. Monuments include the Torre del Reloj, the 18th-century Iglesia de los Remedios and the remains of the Castillo de San Luis; the Casa del Aljibe (archaeological museum) and the Parque Botánico y Orquidario are also in town (Spain.info). The mural route is folded into this record (owner note on the selection checklist). About 53 minutes by car from Casa de la Familia; Playa de la Rada is nearby.'
seo_title: Estepona old town, Estepona | CalleMilano
seo_description: 'Estepona old town (Estepona): what to see and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Plaza de las Flores' at Plaza de las Flores, 29680 Estepona, Málaga, España (36.4257878,-5.145206), primary type None.
  source_url: https://maps.google.com/?cid=6832883084358567301
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 53 min by car (59.3 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4257878%2C-5.145206&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long
  claim: 'Spain.info (Turespaña): ''calles con casas de fachada blanca y cargadas de macetas con flores''; ''la Ruta de Murales, con más de 40 obras de arte, la Ruta de Esculturas, con más de 30 piezas ... la Ruta de Poesía''; ''la Torre del Reloj, la Iglesia de los Remedios, del siglo XVIII, y lo que fuera el Castillo de San Luis''; ''la plaza de las Flores, la Casa del Aljibe (con el Museo Arqueológico) y el Parque Botánico y Orquidario''.'
  source_url: https://www.spain.info/es/destino/estepona/
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour towns fact check 2026-11-02)
  confidence: high
  notes: Read with Firecrawl (direct quotes) or directly on 2026-11-02. Supports the description of sights only; not opening hours, access or suitability.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults high, seniors high; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Historic town, Half day, Free."
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
