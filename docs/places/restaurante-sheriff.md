---
schema_version: 1.0.0
status: archived
id: ES-AND-MAL-RESTAURANTE-SHERIFF-001
slug: restaurante-sheriff
name: Restaurante Sheriff
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.504587
  longitude: -4.6686863999999995
  purpose: venue
  label: Restaurante Sheriff, Calle Playa del Chaparral, 4, 29649 Las Lagunas de Mijas, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJYVv2Vjwecw0RP4Ct1pXJH9g, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=15573387681859469375
external_ids:
  google_place_id: ChIJYVv2Vjwecw0RP4Ct1pXJH9g
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 12 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante Sheriff, Calle Playa del Chaparral, 4, 29649 Las Lagunas de Mijas, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.504587,-4.6686863999999995); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.504587%2C-4.6686863999999995&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 12 min, 6.6 km. One predicted sample.'
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
  cost_basis: 'Own carta (la_carta.cfm): 12 quoted mains 12,00-26,20 € (median 16,70 €); no drink prices, so the band is € only if a drink costs at most 3,30 €. Owner decision 2026-11-03: stays Unknown until the restaurant is confirmed open and a drink price is known. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-03'
links:
  official_website: http://www.elsheriff.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Restaurante Sheriff: a beachfront restaurant at Playa del Chaparral, about 12 min by car from Casa de la Familia. Draft; facts not yet checked.'
description_long: Restaurante Sheriff is a beachfront restaurant at Playa del Chaparral. About 12 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Other facts have not been checked yet.
seo_title: Restaurante Sheriff, Mijas | CalleMilano draft record
seo_description: 'Draft record for Restaurante Sheriff (Mijas): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Restaurante Sheriff' at Calle Playa del Chaparral, 4, 29649 Las Lagunas de Mijas, Málaga, España (36.504587,-4.6686863999999995), status CLOSED_TEMPORARILY, type mediterranean_restaurant.
  source_url: https://maps.google.com/?cid=15573387681859469375
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. From the owner's recommendations on callemilano.dk (Lovable app 'Vores Spanske Hjem', table recommendations), read 2026-11-02.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 12 min by car (6.6 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.504587%2C-4.6686863999999995&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: status (operating)
  claim: Google Places businessStatus CLOSED_TEMPORARILY for 'Restaurante Sheriff', Calle Playa del Chaparral, 4.
  source_url: https://maps.google.com/?cid=15573387681859469375
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Listed on callemilano.dk as inspiration (published-restaurante-sheriff). Hand-written gold page in docs/published/ is not a record.
- field: cost_level
  claim: '"Pollo asado 14,20 €" ; "Pollo al ajillo 15,30 €" ; "Pollo al curry 17,90 €" ; "Chuletas de cerdo 14,70 €" ; "Hamburguesa adulto 14,00 €" ; "Solomillo de cerdo 23,60 €" ; "Entrecot plancha 26,20 €" ; "Pizza sheriff 30 cm 16,50 €" ; "Spaguetti bolognese 12,00 €" ; "Lenguado plancha 20,10 €" ; "Salmón a la plancha 22,20 €" ; "Rosada a la plancha 16,90 €"'
  source_url: http://www.elsheriff.com/la_carta.cfm
  source_type: official_venue
  checked_at: '2026-11-03'
  checked_by: record-writer agent
  confidence: high
  notes: 'Method: curl. Followed La Carta (curl). In the source each dish name and price sit on separate lines; joined here with a space and the leading item number removed. Carta has no drink prices. Address on page: Calle Playa del Chaparral 4, Mijas Costa (La Cala); name matches ''Restaurante Sheriff La Cala Tranquila''. Home page itself has no prices.'
- field: status
  claim: 'Owner (editor-of-record) 2026-11-08: Sheriff is apparently closed, and not because of seasonal variation ("Sheriff er tilsyneladende lukket - ikke på grund af sæsonvariation").'
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/change-log.md
  source_type: secondary
  checked_at: '2026-11-08'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-08
  confidence: medium
  notes: Owner statement in session 2026-11-08 after the phone check listed in docs/faktatjek-liste-2026-11-08.md.
review_issues:
- code: facts_not_checked
  severity: warning
  fields:
  - description_long
  - visit_information
  - cost_level
  - accessibility
  - parking
  description: Created from Google Places identity and a route check only; needs official or own sources.
  retryable: true
  owner: fact_check
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  - tags
  description: Age groups, family scores and tags are not assessed; energy_level is an editorial estimate.
  retryable: true
  owner: human_editor
- code: closed_permanently
  severity: info
  fields:
  - status
  description: 'Owner decision 2026-11-08: the restaurant is closed, not a seasonal closure (Google CLOSED_TEMPORARILY 2026-11-02; Mijas Tourism note "Cerrado desde el 28 de febrero"). Archived; ID kept. Reopen as a new check if it reopens.'
  retryable: false
  owner: human_editor
created_at: '2026-11-02'
updated_at: '2026-11-08'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
