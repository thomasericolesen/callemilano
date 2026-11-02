---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-PUERTO-COLORADO-SIERRA-DE-MIJAS-001
slug: puerto-colorado-sierra-de-mijas
name: Puerto Colorado (Sierra de Mijas)
category: Excursions
tags: []
coordinates:
  latitude: 36.597363699999995
  longitude: -4.6620145
  purpose: venue
  label: Puerto Colorado, 29650 Mijas, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJbdNgaQPhcg0RBmQsr7fP8Kg, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=12173458180607337478
external_ids:
  google_place_id: ChIJbdNgaQPhcg0RBmQsr7fP8Kg
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 23 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Puerto Colorado, 29650 Mijas, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.597363699999995,-4.6620145); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.597363699999995%2C-4.6620145&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 23 min, 13.71 km. One predicted sample, not the Google Maps app''s main figure.'
age_groups: []
family_score:
  small_children: unknown
  children: unknown
  young_adults: unknown
  seniors: unknown
energy_level: High
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
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Puerto Colorado (Sierra de Mijas): a trail area in the Sierra de Mijas, about 23 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: Puerto Colorado (Sierra de Mijas) is a trail area in the Sierra de Mijas (29650 Mijas, Málaga, España). From Casa de la Familia it is about 23 minutes by car (Google route check, Saturday 10:00). Puerto Colorado is the end point of a family stage of the Málaga provincial council's Gran Senda network (Sendero 07, Mijas - Puerto Colorado), which starts in Mijas village and passes the Ermita del Calvario. A 2018 Mijas council walking programme gives the route from the Via Crucis to Puerto Colorado as 7.5 km with 500 m of climb. Trail details were not yet read from the official page. Check conditions before setting out.
seo_title: Puerto Colorado (Sierra de Mijas), Mijas | CalleMilano draft record
seo_description: 'Draft record for Puerto Colorado (Sierra de Mijas) (Mijas): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Puerto Colorado' at 29650 Mijas, Málaga, España (36.597363699999995,-4.6620145), business status OPERATIONAL, primary type hiking_area.
  source_url: https://maps.google.com/?cid=12173458180607337478
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 23 min by car (13.71 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.597363699999995%2C-4.6620145&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time over 20 minutes, so not shown (owner rule).
- field: description_long
  claim: 'Gran Senda de Málaga (Diputación de Málaga), ''Sendero 07. Mijas - Puerto Colorado (Familia)'': ''La etapa parte del casco urbano de Mijas en busca de la Ermita del Calvario por el Via Crucis, que cuenta con 14 estaciones y la parada final ...''.'
  source_url: https://www.gransendademalaga.es/es/etapas/lis_cd-9508/sendero-07-mijas-puerto-colorado-familia
  source_type: government
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: medium
  notes: Search excerpt read 2026-11-02; the page itself blocked automated reading. Distance, time and difficulty not yet read.
- field: description_long
  claim: 'Turismo de Mijas guided-walk programme (December 2018): ''Via Crucis hasta la Ermita del Calvario, proseguiremos hasta Puerto Colorado ... Distancia: 7,5 Kms. Desnivel: 500 mts.'''
  source_url: https://turismo.mijas.es/images/ocio/agenda/Programas%20de%20senderos/DICIEMBRE%20SENDERISMO%20EN%20MIJAS%20Diciembre%202018.pdf
  source_type: government
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: low
  notes: Search excerpt of a 2018 municipal guided-walk programme; figures describe that organised walk, not necessarily the signed trail.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  - tags
  description: Age groups, family scores and tags are not assessed; energy_level High is an editorial estimate from the type of place.
  retryable: true
  owner: human_editor
- code: category_editorial_choice
  severity: info
  fields:
  - category
  description: 'Category ''Excursions'' was chosen by Claude from the schema definitions (routes and sights: Excursions; towns: City; natural areas: Nature; visitor attractions: Family activities). Confirm at editorial review.'
  retryable: true
  owner: human_editor
- code: trail_data_unread
  severity: warning
  fields:
  - description_long
  - energy_level
  - accessibility
  description: Official trail data were not read (Gran Senda page blocked automated reading). Needs an owner screenshot or Turismo de Mijas; parking and trailhead also to confirm.
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
