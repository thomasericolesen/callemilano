---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-RESTAURANTE-CASA-FERNANDO-SAN-PEDRO-001
slug: restaurante-casa-fernando-san-pedro
name: Restaurante Casa Fernando (San Pedro)
category: Restaurants
tags:
- Restaurant
- Rainy day
- Full day
- Premium
coordinates:
  latitude: 36.476132199999995
  longitude: -4.9879999999999995
  purpose: venue
  label: Restaurante Casa Fernando, Av. del Mediterráneo, 48, 29670 San Pedro Alcántara, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJkRhFLzsqcw0RBpdnNOmq_60, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=12537927806206056198
external_ids:
  google_place_id: ChIJkRhFLzsqcw0RBpdnNOmq_60
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 40 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante Casa Fernando, Av. del Mediterráneo, 48, 29670 San Pedro Alcántara, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.476132199999995,-4.9879999999999995); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.476132199999995%2C-4.9879999999999995&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 40 min, 39.4 km. One predicted sample.'
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
cost_level: €€
visit_information:
  schedule: Tue-Sat 13:30-00:00; closed Sun-Mon (own site, read 2026-11-02).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own menu: quoted mains 26,00 and 29,50 € (median about 27,75 €); drink prices not on the page, so main plus one drink is about 30 € or more, inside 20-50 €. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-02'
links:
  official_website: https://www.casafernandos.com/en/eng-home/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- playa-de-san-pedro-alcantara
description_short: 'Casa Fernando: family-founded Spanish restaurant with fish and seafood, San Pedro de Alcántara.'
description_long: Casa Fernando serves Spanish food with fresh fish and seafood; the restaurant was founded in 1977 in Marbella by a married couple (own website). Open Tuesday-Saturday 13:30-00:00, closed Sunday and Monday; phone +34 952 85 33 44.
seo_title: Restaurante Casa Fernando (San Pedro), Marbella | CalleMilano
seo_description: 'Restaurante Casa Fernando (San Pedro) (Marbella): food, opening hours and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'Restaurante Casa Fernando' at Av. del Mediterráneo, 48, 29670 San Pedro Alcántara, Málaga, España (36.476132199999995,-4.9879999999999995), business status OPERATIONAL, primary type seafood_restaurant; about 425 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=12537927806206056198
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/one-hour-beach-restaurants-intake-2026-11-02.md, row rE02).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 40 min by car (39.4 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.476132199999995%2C-4.9879999999999995&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long, visit_information, food_available
  claim: 'Own site: ''Authentic Spanish flavors in a familiar and cozy atmosphere, where the freshness of the sea and tradition are found in every dish''; ''founded in 1977 in Marbella by a married couple''; Tuesday to Saturday 13:30-00:00, Sunday and Monday closed; (+34) 952 85 33 44.'
  source_url: https://www.casafernandos.com/en/eng-home/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant fact check 2026-11-02)
  confidence: medium
  notes: Own website read with Firecrawl (direct quotes) on 2026-11-02.
- field: cost_level
  claim: '"Entrecote 29.50€"; "Sea bass 65.00€/kg"; "Seafood Paella 26.00€"'
  source_url: https://www.casafernandos.com/en/eng-menu/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: high
  notes: Menu lines quoted verbatim; name and price on adjacent lines joined with a space.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children high, children high, young_adults high, seniors high; energy_level Low. Owner note (Danish): ''Familiedrevet fiskerestaurant. Anbefaling i Michelin-guiden''.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Restaurant, Rainy day, Full day, Premium."
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
  - cost_level
  - booking_required
  description: 'Own website checked 2026-11-02. Still open: cost_level. Opening hours change by season; check before publishing. The site''s address was not read; that it is the same Casa Fernando as the Google listing on Av. del Mediterráneo 48, San Pedro, rests on the website link in the Google listing.'
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
