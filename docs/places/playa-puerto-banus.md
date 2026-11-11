---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-PLAYA-PUERTO-BANUS-001
slug: playa-puerto-banus
name: Playa de Puerto Banús
category: Beaches
tags:
- Beach
- Half day
- Free
coordinates:
  latitude: 36.4898088
  longitude: -4.9490514
  purpose: representative_point
  label: Playa Puerto Banús, Playa Puerto Banús, España (Google Places listing); not a parking point
  source: Google Places API (New), place ChIJmV37XcYpcw0RSm-OCEyJ8eQ, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=16497117869688909642
external_ids:
  google_place_id: ChIJmV37XcYpcw0RSm-OCEyJ8eQ
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 36 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Playa Puerto Banús, Playa Puerto Banús, España (Google Places point, not a parking point)
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4898088,-4.9490514); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4898088%2C-4.9490514&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 36 min, 35.3 km. One predicted sample, not the Google Maps app''s main figure.'
age_groups:
- Young adults
- Seniors
family_score:
  small_children: unknown
  children: unknown
  young_adults: high
  seniors: high
energy_level: Low
seasonality:
- Spring
- Summer
- Autumn
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
description_short: 'Playa de Puerto Banús, Marbella: golden-sand beach next to the marina, with a long promenade.'
description_long: 'Playa de Puerto Banús lies next to the Puerto Banús marina. The Costa del Sol tourist board describes a semi-urban, golden-sand beach about 1,500 m long and 40 m wide, bordered by a long promenade (search excerpt; the page itself blocks automated reading). It is not on the 2026 Blue Flag list. Facilities and lifeguards are not checked. Rocks: the tourist board describes a sand beach with easy access on foot, so it meets the project''s beach rule (owner decision 2026-11-02). About 36 minutes by car from Casa de la Familia.'
seo_title: Playa de Puerto Banús, Marbella | CalleMilano
seo_description: 'Playa de Puerto Banús (Marbella): sand, facilities, Blue Flag status and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Playa Puerto Banús' at Playa Puerto Banús, España (36.4898088,-4.9490514), business status OPERATIONAL, primary type beach.
  source_url: https://maps.google.com/?cid=16497117869688909642
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Maps establishes identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 36 min by car (35.3 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4898088%2C-4.9490514&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour band intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL, Saturday 2026-11-07 10:00.
- field: description_long
  claim: 'Turismo Costa del Sol: ''playa semiurbana de arena dorada con 1.500 m de longitud y 40 m de anchura media, rodeada por un extenso paseo marítimo''.'
  source_url: https://www.visitacostadelsol.com/malaga-costa-del-sol/playas/playa-de-puerto-banus-p21761
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour beach fact check 2026-11-02)
  confidence: medium
  notes: Search excerpt only, 2026-11-02; the page returns a CAPTCHA to automated requests. Owner screenshot would raise confidence.
- field: description_long (Blue Flag 2026)
  claim: No beach named Puerto Banús appears under Marbella in ADEAC's 2026 list.
  source_url: https://www.banderaazul.org/sites/default/files/2026/Rueda-de-prensa-2026/Relaci%C3%B3n%20Playas%20Galardonadas%202026.pdf
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour beach fact check 2026-11-02)
  confidence: high
  notes: PDF read 2026-11-02.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children unknown, children unknown, young_adults high, seniors high; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Beach, Half day, Free."
  source_url: https://claude.ai/artifact/DZv9cLLQ1BEcYs3NeewdEF
  source_type: secondary
  checked_at: '2026-11-11'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-11
  confidence: medium
  notes: Owner's own judgment on the tag checklist on 2026-11-11 (previous tags were estimates from import); not independently verified. source_type secondary is the nearest schema value.
review_issues:
- code: lifeguard_season_unchecked
  severity: warning
  fields:
  - description_long
  - accessibility
  description: Lifeguard service and bathing-season dates for 2027 are not checked against the council's beach plan; check before publishing safety-related text.
  retryable: true
  owner: fact_check
- code: official_page_not_readable
  severity: warning
  fields:
  - description_long
  - toilets_available
  description: The tourist board page for this beach blocks automated reading; only a search excerpt was used. Facilities need the full page (owner screenshot) or Marbella council's beach information.
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
