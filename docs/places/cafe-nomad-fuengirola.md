---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-CAFE-NOMAD-FUENGIROLA-001
slug: cafe-nomad-fuengirola
name: Café NOMAD
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.5299519
  longitude: -4.625333599999999
  purpose: venue
  label: Café NOMAD, P.º Marítimo Rey de España, 3, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJORomslricg0RFrnrOUwmN8c, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=14354984446097864982
external_ids:
  google_place_id: ChIJORomslricg0RFrnrOUwmN8c
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 10 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Café NOMAD, P.º Marítimo Rey de España, 3, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5299519,-4.625333599999999); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5299519%2C-4.625333599999999&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 10 min, 5.1 km. One predicted sample.'
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
booking_required: false
dog_friendly: unknown
toilets_available: unknown
food_available: unknown
cost_level: €
visit_information:
  schedule: Daily 9:00-15:00 (own website); season not stated.
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own website: 4 quoted favourites 10,90-14,20 € (median 13,20 €); drink prices not quoted, so main plus one drink stays under 20 € unless the drink costs more than 6,80 €. Owner decision 2026-11-03: €. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-03'
links:
  official_website: https://cafenomadfuengirola.com/
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34951536411
related_places: []
description_short: 'Café NOMAD: sea-facing café for breakfast, brunch and lunch on the Paseo Marítimo in Fuengirola, about 10 min by car from Casa de la Familia.'
description_long: 'Café NOMAD is a café at Paseo Marítimo Rey de España 3 in Fuengirola. Its own website describes breakfast, brunch and lunch facing the sea, with glass doors folded back onto the promenade, parasols on the sand and "sandy feet welcome". It is open daily 9:00-15:00 according to the own website, which does not say whether this changes by season. The own website says walk-ins are always welcome; booking just means a table is waiting, which matters most at weekends and for groups. About 10 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Favourites on the own website cost about 10,90-14,20 € (price check, 2026-11-03). Nothing about children''s facilities or accessibility was found. Owner''s recommendation (callemilano.dk): Very good for breakfast.'
seo_title: Café NOMAD, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Café NOMAD (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Café NOMAD' at P.º Marítimo Rey de España, 3, 29640 Fuengirola, Málaga, España (36.5299519,-4.625333599999999), status OPERATIONAL, type cafe.
  source_url: https://maps.google.com/?cid=14354984446097864982
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. From the owner's recommendations on callemilano.dk (Lovable app 'Vores Spanske Hjem', table recommendations), read 2026-11-02.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 10 min by car (5.1 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5299519%2C-4.625333599999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long (owner knowledge)
  claim: Virkelig lækkert til morgenmad.
  source_url: https://callemilano.dk/
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: medium
  notes: 'Owner''s own recommendation (kind ''anbefaling'') on callemilano.dk, read from the Lovable app database 2026-11-02; site tags: børn, morgenmad. Personal experience, not independently verified.'
- field: cost_level
  claim: '"So-fish-ticated 12.90 €" ; "Avoholic 10.90 €" ; "Nomad poké bowl 14.20 €" ; "Green Ocean 13.50 €"'
  source_url: https://cafenomadfuengirola.com/
  source_type: official_venue
  checked_at: '2026-11-03'
  checked_by: record-writer agent
  confidence: medium
  notes: 'Method: curl. Home page has 4 prices in the ''The favourites'' section (name line and price line in source, joined here). Home already has prices, so the menu page was not followed per the rule. The full menu is https://cafenomadfuengirola.com/menu.html (link text ''See the menu''); it may give more main-course lines if the orchestrator asks for it. No drink prices on home.'
- field: description_long
  claim: '"Breakfast, brunch and lunch, facing the sea" ; "Glass doors folded back onto the promenade, parasols on the sand, sandy feet welcome."'
  source_url: https://cafenomadfuengirola.com/
  source_type: official_venue
  checked_at: '2026-11-03'
  checked_by: record-writer agent
  confidence: high
  notes: Home page, /contact and /menu.html read via curl 2026-11-03.
- field: visit_information.schedule
  claim: '"Monday — Friday 9.00 — 15.00" ; "Saturday 9.00 — 15.00" ; "Sunday 9.00 — 15.00"'
  source_url: https://cafenomadfuengirola.com/contact
  source_type: official_venue
  checked_at: '2026-11-03'
  checked_by: record-writer agent
  confidence: high
  notes: Seasonal status not stated.
- field: booking_required
  claim: '"Walk-ins are always welcome — booking just means a table is waiting, which matters most at weekends and for groups." ; "A booking is only held once we have answered you. We reply by phone or email."'
  source_url: https://cafenomadfuengirola.com/contact
  source_type: official_venue
  checked_at: '2026-11-03'
  checked_by: record-writer agent
  confidence: high
  notes: Booking is optional, so booking_required is false.
- field: links.contact
  claim: '"+34 951 53 64 11"'
  source_url: https://cafenomadfuengirola.com/contact
  source_type: official_venue
  checked_at: '2026-11-03'
  checked_by: record-writer agent
  confidence: high
  notes: ''
- field: address
  claim: '"Paseo Marítimo Rey de España 3" ; "29640 Fuengirola, Málaga"'
  source_url: https://cafenomadfuengirola.com/contact
  source_type: official_venue
  checked_at: '2026-11-03'
  checked_by: record-writer agent
  confidence: high
  notes: Matches the Google Places identity.
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
- code: cost_level_borderline
  severity: info
  description: No drink price quoted; € assumes a drink under 6,80 € (owner decision 2026-11-03). Full menu at https://cafenomadfuengirola.com/menu.html not read.
  fields:
  - cost_level
  retryable: true
  owner: human_editor
- code: facts_partly_checked
  severity: warning
  fields:
  - visit_information
  - accessibility
  - parking
  description: 'Own website read. Still open: whether hours change by season, children''s menu/high chairs, accessibility, parking, full menu prices (see cost_level_borderline).'
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-03'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
