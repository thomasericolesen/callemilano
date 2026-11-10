---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-PARQUE-DE-LA-PALOMA-001
slug: parque-de-la-paloma
name: Parque de la Paloma
category: Family activities
tags: []
coordinates:
  latitude: 36.5935284
  longitude: -4.5293123
  purpose: venue
  label: Parque de la Paloma, Av. Federico García Lorca, s/n, 29630 Benalmádena, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJq2BnI4z8cg0RpE_1LeHQrfI, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=17486862593706774436
external_ids:
  google_place_id: ChIJq2BnI4z8cg0RpE_1LeHQrfI
municipality: Benalmádena
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 25 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Parque de la Paloma, Av. Federico García Lorca, s/n, 29630 Benalmádena, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5935284,-4.5293123); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5935284%2C-4.5293123&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 25 min, 19.03 km. One predicted sample, not the Google Maps app''s main figure.'
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
  official_website: http://www.andalucia.org/es/turismo-cultural/visitas/malaga/otras-visitas/parque-de-la-paloma/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Parque de la Paloma: a large park with animals and a lake, about 25 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: 'Parque de la Paloma is a large park with animals and a lake (Av. Federico García Lorca, s/n, 29630 Benalmádena, Málaga, España). From Casa de la Familia it is about 25 minutes by car (Google route check, Saturday 10:00). Andalusia''s official tourism site (checked 2026-11-02): Benalmádena''s main urban green space, over 200,000 m², with marked walking paths, an artificial lake, two modern playgrounds, trails, animals and places to eat; listed hours 09:00-23:00 for 2026. Whether entry is free is not stated in that source. Check before visiting.'
seo_title: Parque de la Paloma, Benalmádena | CalleMilano draft record
seo_description: 'Draft record for Parque de la Paloma (Benalmádena): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Parque de la Paloma' at Av. Federico García Lorca, s/n, 29630 Benalmádena, Málaga, España (36.5935284,-4.5293123), business status OPERATIONAL, primary type park.
  source_url: https://maps.google.com/?cid=17486862593706774436
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 25 min by car (19.03 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5935284%2C-4.5293123&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time over 20 minutes, so not shown (owner rule).
- field: description_long, visit_information
  claim: 'andalucia.org listing ''Parque de la Paloma'': Avenida Federico García Lorca s/n, 29631 Benalmádena; más de 200.000 m² de áreas verdes, zonas de paseo balizadas, un lago artificial, dos modernos parques infantiles, senderos, animales y zonas de restauración; fechas 1 Jan-31 Dec 2026, 09:00-23:00.'
  source_url: https://www.andalucia.org/listing/parque-de-la-paloma/16577102/
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: high
  notes: Junta de Andalucía tourism portal, read via Firecrawl on 2026-11-02.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults medium, seniors medium; energy_level Low.'
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
  description: 'Category ''Family activities'' was chosen by Claude from the schema definitions (routes and sights: Excursions; towns: City; natural areas: Nature; visitor attractions: Family activities). Confirm at editorial review.'
  retryable: true
  owner: human_editor
- code: entry_and_facilities_to_confirm
  severity: warning
  fields:
  - cost_level
  - toilets_available
  - accessibility
  description: Free entry, toilets and accessibility are not stated by the official source; check with Benalmádena council.
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
