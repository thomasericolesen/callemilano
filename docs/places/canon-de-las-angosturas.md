---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-CANON-DE-LAS-ANGOSTURAS-001
slug: canon-de-las-angosturas
name: Cañón de las Angosturas (Benahavís)
category: Nature
tags: []
coordinates:
  latitude: 36.5172039
  longitude: -5.0399199999999995
  purpose: representative_point
  label: Cañón de las Angosturas, 29679 Benahavís, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJAwc6ZULVcg0R1eGXfZrigOs, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=16969812549091975637
external_ids:
  google_place_id: ChIJAwc6ZULVcg0R1eGXfZrigOs
municipality: Benahavís
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 46 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Cañón de las Angosturas, 29679 Benahavís, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5172039,-5.0399199999999995); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5172039%2C-5.0399199999999995&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 46 min, 46.7 km. One predicted sample.'
age_groups:
- Young adults
- Seniors
family_score:
  small_children: low
  children: low
  young_adults: high
  seniors: medium
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
dog_friendly: 'no'
toilets_available: unknown
food_available: unknown
cost_level: Unknown
visit_information:
  schedule: 'Access to the Río Guadalmina: 10:00-20:00; last departure down the canyon 19:00 (Benahavís council page dated 14 June 2021, read 2026-11-13; not stated whether this is seasonal or still current).'
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: http://andaluciarustica.com/canon-de-las-angosturas-del-rio-guadalmina-benahavis.htm
  booking: null
  visitor_information: https://www.benahavis.es/120/com1_md3_cd-62478/rio-guadalmina
  transport: null
  contact: null
related_places: []
description_short: 'Cañón de las Angosturas (Benahavís): a gorge on the Río Guadalmina near Benahavís, about 46 min by car from Casa de la Familia. Hours and rules from the council page (2021); other facts not yet checked.'
description_long: Cañón de las Angosturas (Benahavís) is a gorge on the Río Guadalmina near Benahavís. About 46 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). The Benahavís council page on the Río Guadalmina (dated 14 June 2021) gives access hours of 10:00-20:00 with the last descent at 19:00, describes the canyon as a level 1 canyoning area where protective equipment is recommended, requires children aged 14 and under to be accompanied by an adult, and bans pets, inflatables, glass, soap and music. Prices, duration, parking and accessibility have not been checked.
seo_title: Cañón de las Angosturas (Benahavís), Benahavís | CalleMilano draft record
seo_description: 'Draft record for Cañón de las Angosturas (Benahavís) (Benahavís): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Cañón de las Angosturas' at 29679 Benahavís, Málaga, España (36.5172039,-5.0399199999999995), status OPERATIONAL, type hiking_area.
  source_url: https://maps.google.com/?cid=16969812549091975637
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Places API (New). Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 46 min by car (46.7 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5172039%2C-5.0399199999999995&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children low, children low, young_adults high, seniors medium; energy_level High.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: visit_information.schedule, dog_friendly, description_long
  claim: '"Horario: 10:00h- 20:00h"; "Última salida para hacer la bajada del cañón de Las Angosturas: 19:00h"; "Los menores de 14 años (inclusive) deberán estar siempre acompañados de un adulto responsable."; "Prohibida la entrada de animales domésticos."; "Se trata de una zona de Barranquismo nivel 1"'
  source_url: https://www.benahavis.es/120/com1_md3_cd-62478/rio-guadalmina
  source_type: official_tourism
  checked_at: '2026-11-13'
  checked_by: Claude (main session, Claude in Chrome)
  confidence: medium
  notes: Ayuntamiento de Benahavís news item dated 14 June 2021, read in Claude in Chrome on 2026-11-13 (the page blocks automated reading). The rules may have changed since 2021; the page also carries a Covid-19 clause.
review_issues:
- code: facts_partly_checked
  severity: warning
  fields:
  - visit_information
  - accessibility
  - parking
  - cost_level
  description: Hours, children rule and pet ban come from a council page dated 2021; entry price, duration, parking, accessibility and current opening still need a source.
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-13'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
