---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-DUNAS-DE-ARTOLA-001
slug: dunas-de-artola
name: Dunas de Artola
category: Nature
tags: []
coordinates:
  latitude: 36.485948
  longitude: -4.7487129
  purpose: venue
  label: Dunas de Artola, 29604 Marbella, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJm_krjjggcw0Rzkvi5-eJFBw, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=2023393761717013454
external_ids:
  google_place_id: ChIJm_krjjggcw0Rzkvi5-eJFBw
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 22 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Dunas de Artola, 29604 Marbella, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.485948,-4.7487129); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.485948%2C-4.7487129&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 22 min, 13.34 km. One predicted sample, not the Google Maps app''s main figure.'
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
  official_website: http://www.andalucia.org/es/espacios-naturales/monumento-natural/dunas-de-artola-o-cabopino/
  booking: null
  visitor_information: https://www.andalucia.org/listing/dunas-de-artola-o-cabopino/15533102/
  transport: null
  contact: null
related_places:
- id: ES-AND-MAL-CABOPINO-ARTOLA-001
  relationship: nearby
  note: Cabopino/Artola beach next to the dunes.
description_short: 'Dunas de Artola: a protected dune area next to Cabopino beach, about 22 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: 'Dunas de Artola is a protected dune area next to Cabopino beach (29604 Marbella, Málaga, España). From Casa de la Familia it is about 22 minutes by car (Google route check, Saturday 10:00). Andalusia''s official tourism site (checked 2026-11-02): a Natural Monument (declared 30 September 2003), the remnant of a dune belt that once ran some 20 km along this coast. Three kinds of dunes can be seen: moving dunes with ripples by the beach, inactive dunes covered with plants further in, and fossil dunes under dense pine forest. Plants include marram grass, sea holly and sea daffodils. Visitors should keep to the marked paths, because trampling damages the dunes. Nearby are the Torre de los Ladrones (a listed watchtower), Cabopino marina and Cabopino beach, part of which is nudist. Check conditions before setting out.'
seo_title: Dunas de Artola, Marbella | CalleMilano draft record
seo_description: 'Draft record for Dunas de Artola (Marbella): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Dunas de Artola' at 29604 Marbella, Málaga, España (36.485948,-4.7487129), business status OPERATIONAL, primary type nature_preserve.
  source_url: https://maps.google.com/?cid=2023393761717013454
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 22 min by car (13.34 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.485948%2C-4.7487129&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time over 20 minutes, so not shown (owner rule).
- field: description_long
  claim: 'andalucia.org ''Dunas de Artola o Cabopino'': Monumento Natural, declared 30/09/2003; former dune belt of about 20 km; three dune types (mobile with ripples, inactive vegetated, fossil under pine); barrón, cardo marítimo, narciso de mar, sabina caudada; ''pasear entre las dunas por alguno de los senderos habilitados, pues el pisoteo podría perjudicar su dinámica natural''; Torre de los Ladrones (Bien de Interés Cultural); Puerto de Cabopino and ''la playa nudista del mismo nombre'' nearby.'
  source_url: https://www.andalucia.org/listing/dunas-de-artola-o-cabopino/15533102/
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: high
  notes: Junta de Andalucía tourism portal, read via Firecrawl on 2026-11-02. Area field on the page reads '20' (unit unclear); not recorded.
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
  description: 'Category ''Nature'' was chosen by Claude from the schema definitions (routes and sights: Excursions; towns: City; natural areas: Nature; visitor attractions: Family activities). Confirm at editorial review.'
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
