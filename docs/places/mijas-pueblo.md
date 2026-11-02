---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-MIJAS-PUEBLO-001
slug: mijas-pueblo
name: Mijas Pueblo
category: City
tags: []
coordinates:
  latitude: 36.5967755
  longitude: -4.6323067
  purpose: town_center
  label: Mijas, 29650 Mijas, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJOTfyvvzjcg0RDdSq9b2T98M, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=14120917600723194893
external_ids:
  google_place_id: ChIJOTfyvvzjcg0RDdSq9b2T98M
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 17 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Mijas, 29650 Mijas, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5967755,-4.6323067); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5967755%2C-4.6323067&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 17 min, 10.16 km. One predicted sample, not the Google Maps app''s main figure.'
age_groups: []
family_score:
  small_children: unknown
  children: unknown
  young_adults: unknown
  seniors: unknown
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
  official_website: https://turismo.mijas.es/es/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Mijas Pueblo: the white village of Mijas on the mountainside, about 17 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: 'Mijas Pueblo is the white village of Mijas on the mountainside (29650 Mijas, Málaga, España). From Casa de la Familia it is about 17 minutes by car (Google route check, Saturday 10:00). Andalusia''s official tourism site (checked 2026-11-02): a village of Moorish layout spread along the slope of the Sierra de Mijas like a balcony, white houses against green pines, one of the most attractive views on the coast. Sights include the Santuario de la Virgen de la Peña, the bullring, and the group formed by the Iglesia de la Concepción, the auditorium and its gardens. Beside the Virgen de la Peña hermitage, built into the rock on Avenida del Compás, is the Mirador del Compás (also called Mirador Virgen de la Peña), a viewpoint with wide views over the Costa del Sol. Parking, donkey taxis and accessibility were not checked. Check before visiting.'
seo_title: Mijas Pueblo, Mijas | CalleMilano draft record
seo_description: 'Draft record for Mijas Pueblo (Mijas): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Mijas' at 29650 Mijas, Málaga, España (36.5967755,-4.6323067), business status None, primary type None.
  source_url: https://maps.google.com/?cid=14120917600723194893
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 17 min by car (10.16 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5967755%2C-4.6323067&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time over 20 minutes, so not shown (owner rule).
- field: description_long
  claim: 'andalucia.org listing ''Mijas'': ''El pueblo, con una fisonomía típica de la época árabe, se extiende a través de la ladera de la sierra como si de un balcón se tratase, con sus casas blancas en vivo contraste con el verde de los pinos''; ''lugares de especial interés, como el Santuario de la Virgen de la Peña, la Plaza de Toros, o el conjunto que forman la Iglesia de la Concepción, el Auditorio y los Jardines anexos''; history summary.'
  source_url: https://www.andalucia.org/listing/mijas/19913102/
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: high
  notes: Read via Firecrawl on 2026-11-02.
- field: description_long (Mirador del Compás)
  claim: 'Google Places: ''Ermita de la Virgen de la Peña'', Av. del Compás 7, 29650 Mijas (36.5955369,-4.6356259), about 30 m from the ''Mirador del Compás'' point (36.5953395,-4.6358648); ''Santuario de la Virgen de la Peña'', Av. del Compás 8.'
  source_url: https://maps.google.com/?cid=9334915565214010936
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: high
  notes: Places API text search 2026-11-02; shows the viewpoint is in Mijas Pueblo, not on a mountain trail.
- field: description_long (Mirador del Compás)
  claim: '''El Mirador Virgen de la Peña es también conocido como Mirador del Compás. Se encuentra junto a la Ermita de la Virgen de la Peña. Este mirador deja unas vistas impresionantes de la Costa del Sol.'' Ermita: ''La imagen de la virgen está tallada en madera y fue descubierta en el año 1586.'''
  source_url: https://www.allincarhire.com/es/mijas-mirador.php
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: medium
  notes: Owner screenshot (supplied 2026-11-02) of a car-hire company's travel page; secondary. The two names agree with Google's positions.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  - tags
  description: Age groups, family scores and tags are not assessed; energy_level Medium is an editorial estimate from the type of place.
  retryable: true
  owner: human_editor
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
  description: Parking, bus links from Las Lagunas, steepness of the streets and the donkey taxis (and any welfare questions) were not checked. Turismo de Mijas (turismo.mijas.es) is the source to use.
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: '2026-11-02'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
