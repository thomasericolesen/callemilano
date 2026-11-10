---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-JARDIN-BOTANICO-LA-CONCEPCION-001
slug: jardin-botanico-la-concepcion
name: Jardín Botánico Histórico La Concepción
category: Nature
tags: []
coordinates:
  latitude: 36.7601029
  longitude: -4.4262669
  purpose: venue
  label: Jardín Botánico Histórico La Concepción, Cam. del Jardin Botanico, 3, Cdad. Jardín, 29014 Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJBeoOtEP2cg0RAui-vP66EyM, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=2527569419136067586
external_ids:
  google_place_id: ChIJBeoOtEP2cg0RAui-vP66EyM
municipality: Málaga
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 36 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Jardín Botánico Histórico La Concepción, Cam. del Jardin Botanico, 3, Cdad. Jardín, 29014 Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.7601029,-4.4262669); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.7601029%2C-4.4262669&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 36 min, 39.1 km. One predicted sample.'
age_groups:
- Young adults
- Seniors
family_score:
  small_children: low
  children: low
  young_adults: high
  seniors: high
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
food_available: 'yes'
cost_level: Unknown
visit_information:
  schedule: Tuesday to Sunday. April to September 09:30-20:30; October to March 09:30-17:30. Closed 25 December and 1 January. Seasonal (own website, checked 2026-11-02).
  typical_duration: null
  booking_lead_time: null
  valid_from: '2026-11-02'
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: http://laconcepcion.malaga.eu/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: Historic subtropical botanical garden north of Málaga, open Tuesday to Sunday; about 36 min by car from Casa de la Familia.
description_long: 'Jardín Botánico Histórico La Concepción is described on its own website as a natural oasis in the city and the best-preserved landscape-style subtropical garden in Europe. It is a Bien de Interés Cultural created in 1855, with more than fifty thousand plants and three thousand species, varieties and cultivars. About 36 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). According to the garden''s website it is open Tuesday to Sunday: April to September 09:30-20:30 and October to March 09:30-17:30, closed on 25 December and 1 January. The site says the garden can be visited freely and that a kiosk cafeteria stands next to the entrance. Ticket prices are only linked to a tariff list, and toilets, accessibility and parking are not stated on the page.'
seo_title: Jardín Botánico Histórico La Concepción, Málaga | CalleMilano draft record
seo_description: 'Draft record for Jardín Botánico Histórico La Concepción (Málaga): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Jardín Botánico Histórico La Concepción' at Cam. del Jardin Botanico, 3, Cdad. Jardín, 29014 Málaga, España (36.7601029,-4.4262669), status OPERATIONAL, type botanical_garden.
  source_url: https://maps.google.com/?cid=2527569419136067586
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Places API (New). Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 36 min by car (39.1 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.7601029%2C-4.4262669&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long
  claim: '"Un oasis natural en la ciudad. El jardín subtropical de estilo paisajista mejor conservado de Europa." / "Bien de Interés Cultural creado en 1855, con más de cincuenta mil plantas, tres mil especies, variedades y cultivares tropicales, subtropicales, autóctonas, endemismos y agrícolas."'
  source_url: http://laconcepcion.malaga.eu/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: high
  notes: null
- field: visit_information.schedule
  claim: '"Horario (Martes a domingos)" / "Abril a sept.:  09:30 - 20:30 h -  Oct. a marzo: 09:30 - 17:30 h" / "Cerrado 25 de diciembre y 1 de enero."'
  source_url: http://laconcepcion.malaga.eu/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: high
  notes: Seasonal timetable.
- field: food_available
  claim: '"Servicio de cafetería en un quiosco junto a la entrada"'
  source_url: http://laconcepcion.malaga.eu/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: high
  notes: null
- field: description_long (access)
  claim: '"El Jardín se puede visitar de forma libre." / "Consulta las diferentes tarifas que tenemos"'
  source_url: http://laconcepcion.malaga.eu/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: medium
  notes: Page does not state whether entry is free; amounts are only linked. Ticket price left unknown.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children low, children low, young_adults high, seniors high; energy_level Medium.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
review_issues:
- code: facts_partly_checked
  severity: warning
  fields:
  - cost_level
  - accessibility
  - parking
  - toilets_available
  description: Ticket amounts, toilets, accessibility and parking are not stated on the garden's page; the 'visitar de forma libre' wording does not say whether entry is free. Family suitability not covered by a quote (the only family item is an autumn 2026 event listing).
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
