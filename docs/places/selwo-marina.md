---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-SELWO-MARINA-001
slug: selwo-marina
name: Selwo Marina
category: Family activities
tags: []
coordinates:
  latitude: 36.592469
  longitude: -4.532156
  purpose: venue
  label: Selwo Marina, Parque de la Paloma s/n, 29630 Benalmádena, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ4XVoW8v8cg0RBJXVuZ9VtFc, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=6319770321613591812
external_ids:
  google_place_id: ChIJ4XVoW8v8cg0RBJXVuZ9VtFc
municipality: Benalmádena
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 24 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Selwo Marina, Parque de la Paloma s/n, 29630 Benalmádena, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.592469,-4.532156); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.592469%2C-4.532156&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 24 min, 19.01 km. One predicted sample, not the Google Maps app''s main figure.'
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
  official_website: https://www.selwomarina.es/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Selwo Marina: a marine animal park, about 24 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: 'Selwo Marina is a marine animal park (Parque de la Paloma s/n, 29630 Benalmádena, Málaga, España). From Casa de la Familia it is about 24 minutes by car (Google route check, Saturday 10:00). Its own website (checked 2026-11-02): a marine animal park with penguins, exotic birds and other species, educational presentations and keeper talks, and bookable animal encounters (penguins, squirrel monkeys). Tickets (dynamic pricing): general (ages 8-64) from €15.90 online / €17.90 at the gate; reduced (children from age 3 or 1 m tall up to 7, seniors 65+, large families) from €13.90; children under 3 and under 1 m free. It opens to a seasonal calendar; the 2026 Halloween season ran to 2 November, and winter opening was not confirmed. Check before visiting.'
seo_title: Selwo Marina, Benalmádena | CalleMilano draft record
seo_description: 'Draft record for Selwo Marina (Benalmádena): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Selwo Marina' at Parque de la Paloma s/n, 29630 Benalmádena, Málaga, España (36.592469,-4.532156), business status OPERATIONAL, primary type zoo.
  source_url: https://maps.google.com/?cid=6319770321613591812
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 24 min by car (19.01 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.592469%2C-4.532156&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time over 20 minutes, so not shown (owner rule).
- field: description_long, cost_level
  claim: 'Own price page: Entrada General (8-64) online from 15,90€, gate from 17,90€; Entrada Reducida (infantil 3 años o 1 m hasta 7, senior 65+, discapacidad + acompañante gratis, familias numerosas) from 13,90€; menores de 3 años y 1 m gratis; open-date ticket 23,90€; dynamic pricing; visits any day until end of season per the park''s opening calendar.'
  source_url: https://www.selwomarina.es/horarios-y-precios/precios
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: high
  notes: Read via Firecrawl on 2026-11-02. Prices are dynamic or volatile; recheck before publication.
- field: description_long
  claim: 'Own homepage: penguin and squirrel-monkey encounters (new 2026), educational exotic-bird presentation, keeper talks; Halloween season page: 19 October-2 November 2026.'
  source_url: https://www.selwomarina.es/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: medium
  notes: Read via Firecrawl on 2026-11-02. Prices are dynamic or volatile; recheck before publication.
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
  description: 'Category ''Family activities'' was chosen by Claude from the schema definitions (routes and sights: Excursions; towns: City; natural areas: Nature; visitor attractions: Family activities). Confirm at editorial review.'
  retryable: true
  owner: human_editor
- code: season_calendar_unconfirmed
  severity: warning
  fields:
  - seasonality
  - visit_information
  description: The park opens to a seasonal calendar that Firecrawl could not read day by day; winter 2026-27 opening is unconfirmed. Check the calendar (selwomarina.es/horarios-y-precios/horarios) before recommending a visit.
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
