---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-SAN-PEDRO-ALCANTARA-001
slug: san-pedro-alcantara
name: San Pedro Alcántara
category: City
tags: []
coordinates:
  latitude: 36.4820717
  longitude: -4.9888911
  purpose: town_center
  label: Bulevar San Pedro Alcántara (WEB), Avenida Luis Braille, s/n Avenida Norberto Goizueta Díaz, s/n, 29670 San Pedro Alcántara, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJk6y_sj0qcw0R1wTH3JO56wU, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=426638634432005335
external_ids:
  google_place_id: ChIJk6y_sj0qcw0R1wTH3JO56wU
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 39 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Bulevar San Pedro Alcántara (WEB), Avenida Luis Braille, s/n Avenida Norberto Goizueta Díaz, s/n, 29670 San Pedro Alcántara, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4820717,-4.9888911); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4820717%2C-4.9888911&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 39 min, 38.7 km. One predicted sample.'
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
  official_website: http://www.bulevarsanpedro.es/
  booking: null
  visitor_information: https://www.spain.info/es/destino/marbella/
  transport: null
  contact: null
related_places:
- playa-de-san-pedro-alcantara
description_short: 'San Pedro Alcántara: town in the municipality of Marbella, with a boulevard park in its centre.'
description_long: San Pedro Alcántara is a town within the municipality of Marbella, west of Puerto Banús; its patron saint's fiestas are held in October (Spain.info). The record point is the boulevard park in the town centre; a local news site reports that its children's play areas were ranked among the best in Spain by a website (secondary source, not verified). The beach, the Roman remains at Las Bóvedas and Vega del Mar, and beach restaurants are close by. About 39 minutes by car from Casa de la Familia.
seo_title: San Pedro Alcántara, Marbella | CalleMilano
seo_description: 'San Pedro Alcántara (Marbella): what to see and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Bulevar San Pedro Alcántara (WEB)' at Avenida Luis Braille, s/n Avenida Norberto Goizueta Díaz, s/n, 29670 San Pedro Alcántara, Málaga, España (36.4820717,-4.9888911), primary type tourist_attraction.
  source_url: https://maps.google.com/?cid=426638634432005335
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 39 min by car (38.7 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4820717%2C-4.9888911&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long
  claim: 'Spain.info (Turespaña) Marbella page: ''las fiestas patronales de San Pedro de Alcántara, que tienen lugar en octubre''.'
  source_url: https://www.spain.info/es/destino/marbella/
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour towns fact check 2026-11-02)
  confidence: high
  notes: Read with Firecrawl (direct quotes) or directly on 2026-11-02. Supports the description of sights only; not opening hours, access or suitability.
- field: description_long (play areas)
  claim: 'Local news: ''Las zonas de juegos para niños que hay en el bulevar de San Pedro Alcántara se encuentran entre los mejores a nivel nacional'', according to a website.'
  source_url: https://www.marbella24horas.es/local/la-zona-infantil-del-bulevar-entre-las-mejores-de-espana-segun-una-web-13632
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour towns fact check 2026-11-02)
  confidence: low
  notes: Search excerpt only; undated. Needs Marbella council confirmation before it is stated as fact.
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
