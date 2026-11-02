---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-SEA-LIFE-BENALMADENA-001
slug: sea-life-benalmadena
name: Sea Life Benalmádena
category: Family activities
tags: []
coordinates:
  latitude: 36.59664
  longitude: -4.5152
  purpose: venue
  label: Sea Life Benalmádena, Av. del Puerto Deportivo, s/n, 29630 Benalmádena, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJV2-CZGT8cg0RtuBfkTYPR4w, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=10108064615697998006
external_ids:
  google_place_id: ChIJV2-CZGT8cg0RtuBfkTYPR4w
municipality: Benalmádena
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 27 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Sea Life Benalmádena, Av. del Puerto Deportivo, s/n, 29630 Benalmádena, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.59664,-4.5152); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.59664%2C-4.5152&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 27 min, 20.1 km. One predicted sample, not the Google Maps app''s main figure.'
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
  official_website: https://www.visitsealife.com/benalmadena/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Sea Life Benalmádena: an aquarium at Puerto Marina, about 27 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: 'Sea Life Benalmádena is an aquarium at Puerto Marina (Av. del Puerto Deportivo, s/n, 29630 Benalmádena, Málaga, España). From Casa de la Familia it is about 27 minutes by car (Google route check, Saturday 10:00). Its own website (checked 2026-11-02): an aquarium at Puerto Marina with marine habitats (sharks, a large green turtle, otters), open seven days a week with timed entry slots. Standard ticket: adults (15+) €18.50 online or €21 at the door; children €11.50 (the age band was not shown). Online tickets need a time slot and are not sold for the same day. Check before visiting.'
seo_title: Sea Life Benalmádena, Benalmádena | CalleMilano draft record
seo_description: 'Draft record for Sea Life Benalmádena (Benalmádena): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Sea Life Benalmádena' at Av. del Puerto Deportivo, s/n, 29630 Benalmádena, Málaga, España (36.59664,-4.5152), business status OPERATIONAL, primary type tourist_attraction.
  source_url: https://maps.google.com/?cid=10108064615697998006
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 27 min by car (20.1 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.59664%2C-4.5152&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time over 20 minutes, so not shown (owner rule).
- field: description_long, cost_level, booking_required
  claim: 'Own tariffs page: Entrada Standard online 18,50€ por adulto (+15 años), taquilla 21€; 11,50€ por niño. Homepage: ''Abierto los 7 días de la semana''; online tickets need a time slot, up to 10% off, not for same-day purchase; VR combo +5€. Explora page: habitats with sharks and ''Yellow'', a green turtle over 100 kg; otters.'
  source_url: https://www.visitsealife.com/benalmadena/tarifas/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: high
  notes: Read via Firecrawl on 2026-11-02. Prices are dynamic or volatile; recheck before publication.
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
  description: 'Category ''Family activities'' was chosen by Claude from the schema definitions (routes and sights: Excursions; towns: City; natural areas: Nature; visitor attractions: Family activities). Confirm at editorial review.'
  retryable: true
  owner: human_editor
- code: hours_and_child_ages_unconfirmed
  severity: warning
  fields:
  - visit_information
  - cost_level
  description: Daily opening hours and the child age band were not readable; check the hours page (visitsealife.com/benalmadena/prepara-tu-visita/antes-de-tu-visita/horario/).
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
