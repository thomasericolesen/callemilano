---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-MUSEO-AERONAUTICO-MALAGA-001
slug: museo-aeronautico-malaga
name: Museo Aeronáutico de Málaga
category: Family activities
tags: []
coordinates:
  latitude: 36.669914399999996
  longitude: -4.4811323
  purpose: venue
  label: Museo Aeronáutico de Málaga, Plaza Pierre-Georges Latécoère s/n, Churriana, 29004 Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJHzVwcyH6cg0RhFmuwAv0SHk, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=8739503408226916740
external_ids:
  google_place_id: ChIJHzVwcyH6cg0RhFmuwAv0SHk
municipality: Málaga
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 28 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Museo Aeronáutico de Málaga, Plaza Pierre-Georges Latécoère s/n, Churriana, 29004 Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.669914399999996,-4.4811323); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.669914399999996%2C-4.4811323&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 28 min, 28.1 km. One predicted sample.'
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
  cost: Free (own website)
  restrictions: unknown
  walk_distance: unknown
  source: https://www.aeromuseo.org/
  checked_at: '2026-11-02'
transport_options: []
booking_required: unknown
dog_friendly: unknown
toilets_available: unknown
food_available: unknown
cost_level: Free
visit_information:
  schedule: Tuesday 10:00-20:00; Wednesday to Sunday 10:00-14:00; closed Mondays. Seasonality not stated (own website, checked 2026-11-02).
  typical_duration: null
  booking_lead_time: null
  valid_from: '2026-11-02'
  valid_until: null
  cost_basis: Entry stated as completely free (own website)
  cost_checked_at: '2026-11-02'
links:
  official_website: https://www.aeromuseo.org/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: Aviation museum by Málaga airport with free entry and free parking, per its website; about 28 min by car from Casa de la Familia.
description_long: 'The Museo Aeronáutico de Málaga (Aeromuseo) describes itself on its own website as a place to explore, learn and have fun, with more than 5,000 square metres of aeronautical history. About 28 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). The website says entry and parking are completely free. Opening hours listed: Tuesday 10:00-20:00; Wednesday to Sunday 10:00-14:00; closed to the public on Mondays. The site says children will be entertained and offers guided school visits where children can touch and explore. Whether the hours change by season is not stated, and the address was not found in the fetched text.'
seo_title: Museo Aeronáutico de Málaga, Málaga | CalleMilano draft record
seo_description: 'Draft record for Museo Aeronáutico de Málaga (Málaga): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Museo Aeronáutico de Málaga' at Plaza Pierre-Georges Latécoère s/n, Churriana, 29004 Málaga, España (36.669914399999996,-4.4811323), status OPERATIONAL, type museum.
  source_url: https://maps.google.com/?cid=8739503408226916740
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Places API (New). Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 28 min by car (28.1 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.669914399999996%2C-4.4811323&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long
  claim: '"El Museo aeronáutico de Málaga Aeromuseo, es el lugar perfecto para explorar, aprender y divertirse." / "En el Aeromuseo, te sumergirás en más de 5000 metros cuadrados de pura historia aeronáutica ."'
  source_url: https://www.aeromuseo.org/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: high
  notes: null
- field: visit_information.schedule
  claim: '"Martes : de 10:00 a 20:00" / "Miércoles a domingo : de 10:00 a 14:00" / "Los lunes cerramos al público para darle un descanso a los aviones"'
  source_url: https://www.aeromuseo.org/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: high
  notes: null
- field: cost_level, parking.cost
  claim: '"¡Buenas noticias! La entrada y el parking en el Aeromuseo, son completamente gratuitos ."'
  source_url: https://www.aeromuseo.org/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: high
  notes: null
- field: description_long (children)
  claim: '"Así que trae a toda la familia, los niños estarán entretenidos" / "Ofrecemos visitas escolares guiadas donde los niños no solo escuchan, ¡también tocan y exploran!"'
  source_url: https://www.aeromuseo.org/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: medium
  notes: Marketing statement; not an assessment of age suitability.
review_issues:
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
- code: facts_partly_checked
  severity: warning
  fields:
  - accessibility
  - toilets_available
  - food_available
  - parking
  - visit_information
  description: Address, accessibility, toilets, food, parking capacity/location and seasonal changes to hours are not on the fetched page. Age suitability not assessed beyond the site's own claim.
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
