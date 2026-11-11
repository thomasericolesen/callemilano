---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-PUERTO-DEPORTIVO-ESTEPONA-001
slug: puerto-deportivo-estepona
name: Puerto Deportivo de Estepona
category: Excursions
tags:
- Restaurant
- Viewpoint
- Historic town
- Half day
- Premium
coordinates:
  latitude: 36.4148347
  longitude: -5.1571843
  purpose: venue
  label: Puerto Deportivo Marina de Estepona, Puerto Deportivo de Estepona, Torre de Control, 29680 Estepona, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ2WZb67PWDA0R2YUuFiiGweQ, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=16483603617881687513
external_ids:
  google_place_id: ChIJ2WZb67PWDA0R2YUuFiiGweQ
municipality: Estepona
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 54 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Puerto Deportivo Marina de Estepona, Puerto Deportivo de Estepona, Torre de Control, 29680 Estepona, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4148347,-5.1571843); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4148347%2C-5.1571843&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 54 min, 59.9 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: high
  children: high
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
food_available: 'yes'
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
  official_website: https://www.marinasmediterraneo.com/estepona
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- estepona-old-town
- playa-de-la-rada-estepona
description_short: Estepona's marina with restaurants and leisure venues and a Sunday-morning craft market; about 54 min by car from Casa de la Familia.
description_long: 'According to the operator''s website, the Puerto Deportivo de Estepona has 447 berths, the third largest capacity in the province. It describes the food and leisure offer inside the port as high level and a regular meeting point, and mentions a traditional craft market every Sunday morning. A news item on the page says the port has 45 businesses. About 54 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Address on the site: Torre de Control, 29680 Estepona. Parking, toilets, accessibility and costs are not stated on the page.'
seo_title: Puerto Deportivo de Estepona, Estepona | CalleMilano draft record
seo_description: 'Draft record for Puerto Deportivo de Estepona (Estepona): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Puerto Deportivo Marina de Estepona' at Puerto Deportivo de Estepona, Torre de Control, 29680 Estepona, Málaga, España (36.4148347,-5.1571843), status OPERATIONAL, type marina.
  source_url: https://maps.google.com/?cid=16483603617881687513
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Places API (New). Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 54 min by car (59.9 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4148347%2C-5.1571843&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long
  claim: '"El Puerto Deportivo de Estepona, con 447 atraques , es el tercer puerto de la provincia en capacidad ." / "Mención aparte merece el tradicional mercadillo de artesanías que se desarrolla cada domingo por la mañana." / "mantiene su actividad comercial con 45 negocios en sus instalaciones"'
  source_url: https://www.marinasmediterraneo.com/estepona
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: medium
  notes: Operator (Marinas del Mediterráneo) page; 45-businesses figure comes from a news item.
- field: food_available
  claim: '"Dentro del propio recinto portuario la oferta gastronómica y lúdica es de alto nivel , siendo punto de encuentro habitual de propios y extraños."'
  source_url: https://www.marinasmediterraneo.com/estepona
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: medium
  notes: Marketing wording; no individual venues named.
- field: description_long (address)
  claim: '"Torre de Control 29680 Estepona"'
  source_url: https://www.marinasmediterraneo.com/estepona
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: medium
  notes: null
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children high, children high, young_adults high, seniors high; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Restaurant, Viewpoint, Historic town, Half day, Premium."
  source_url: https://claude.ai/artifact/DZv9cLLQ1BEcYs3NeewdEF
  source_type: secondary
  checked_at: '2026-11-11'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-11
  confidence: medium
  notes: Owner's own judgment on the tag checklist on 2026-11-11 (previous tags were estimates from import); not independently verified. source_type secondary is the nearest schema value.
review_issues:
- code: facts_partly_checked
  severity: warning
  fields:
  - parking
  - toilets_available
  - accessibility
  - cost_level
  - visit_information
  - age_groups
  description: Page covers marina facts only. Parking, toilets, accessibility, market hours and family suitability not found; no children-specific content quoted.
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
