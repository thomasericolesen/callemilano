---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-PUERTO-MARINA-BENALMADENA-001
slug: puerto-marina-benalmadena
name: Puerto Marina Benalmádena
category: Excursions
tags: []
coordinates:
  latitude: 36.5979187
  longitude: -4.5122478
  purpose: venue
  label: Puerto Marina Benalmadena Oficial, Calle la Fragata, A11, 29630 Benalmádena, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ330SE2X8cg0R2koQwZJV0Fk, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=6471766753324059354
external_ids:
  google_place_id: ChIJ330SE2X8cg0R2koQwZJV0Fk
municipality: Benalmádena
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 28 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Puerto Marina Benalmadena Oficial, Calle la Fragata, A11, 29630 Benalmádena, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5979187,-4.5122478); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5979187%2C-4.5122478&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 28 min, 20.15 km. One predicted sample, not the Google Maps app''s main figure.'
age_groups: []
family_score:
  small_children: unknown
  children: unknown
  young_adults: unknown
  seniors: unknown
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
  official_website: https://puertobenalmadena.es/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Puerto Marina Benalmádena: Benalmádena''s marina with shops and restaurants, about 28 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: 'Puerto Marina Benalmádena is Benalmádena''s marina with shops and restaurants (Calle la Fragata, A11, 29630 Benalmádena, Málaga, España). From Casa de la Familia it is about 28 minutes by car (Google route check, Saturday 10:00). Andalusia''s official tourism site (checked 2026-11-02): one of the most important marinas on the Andalusian coast, noted for its design and architecture and its wide range of leisure; 1,140 moorings, Blue Flag, with restaurants, bars, toilets, facilities for disabled visitors, boat hire, a nautical club and parking. The marina is run by a municipal company. The Sea Life aquarium is on the marina (see its own record). Check before visiting.'
seo_title: Puerto Marina Benalmádena, Benalmádena | CalleMilano draft record
seo_description: 'Draft record for Puerto Marina Benalmádena (Benalmádena): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Puerto Marina Benalmadena Oficial' at Calle la Fragata, A11, 29630 Benalmádena, Málaga, España (36.5979187,-4.5122478), business status OPERATIONAL, primary type marina.
  source_url: https://maps.google.com/?cid=6471766753324059354
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 28 min by car (20.15 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5979187%2C-4.5122478&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time over 20 minutes, so not shown (owner rule).
- field: description_long, toilets_available, parking
  claim: 'andalucia.org listing ''Puerto Deportivo de Benalmádena Puerto Marina'': ''uno de los más importantes del litoral andaluz, por la belleza de su diseño y de su arquitectura interior, por el número de atraques, por la amplísima oferta alternativa de ocio y diversión''; services: restaurante, servicios para discapacitados, academia, alquiler de embarcaciones, aseos, bar, club náutico, parking, WIFI; amarres 1.140; Bandera Azul. puertobenalmadena.es: managed by Benalmádena Town Hall, a municipal company since July 1996; Edificio Capitanía, Av. Juan Sebastián Elcano s/n; +34 952 57 70 22.'
  source_url: https://www.andalucia.org/listing/puerto-deportivo-de-benalm%C3%A1dena-puerto-marina/9860102/
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: high
  notes: Read via Firecrawl on 2026-11-02.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  - tags
  description: Age groups, family scores and tags are not assessed; energy_level Low is an editorial estimate from the type of place.
  retryable: true
  owner: human_editor
- code: category_editorial_choice
  severity: info
  fields:
  - category
  description: 'Category ''Excursions'' was chosen by Claude from the schema definitions (routes and sights: Excursions; towns: City; natural areas: Nature; visitor attractions: Family activities). Confirm at editorial review.'
  retryable: true
  owner: human_editor
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: '2026-11-02'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
