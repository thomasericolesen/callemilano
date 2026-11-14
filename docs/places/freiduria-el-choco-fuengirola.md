---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-FREIDURIA-EL-CHOCO-FUENGIROLA-001
slug: freiduria-el-choco-fuengirola
name: Pulpería Freiduría El Choco
category: Restaurants
tags:
- Restaurant
- Rainy day
- Half day
- Premium
coordinates:
  latitude: 36.5509163
  longitude: -4.6153718999999995
  purpose: venue
  label: Pulperia Freiduria El Choco, C. Francisco Cano, 13, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJmXdIPkXicg0R6gdJJVRwONM, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=15220038447403698154
external_ids:
  google_place_id: ChIJmXdIPkXicg0R6gdJJVRwONM
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 14 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Pulperia Freiduria El Choco, C. Francisco Cano, 13, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5509163,-4.6153718999999995); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5509163%2C-4.6153718999999995&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 14 min, 6.2 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: medium
  children: medium
  young_adults: medium
  seniors: medium
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
food_available: 'yes'
cost_level: Unknown
visit_information:
  schedule: 'Monday closed; Tuesday to Sunday 13:00-16:00 and 20:00-23:00 (own website, read 2026-11-11). No reservations.'
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: https://freiduriaelchoco.es/
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34952468169
related_places: []
description_short: 'Freiduria El Choco: fried-fish restaurant in Fuengirola; closed Mondays, no reservations (own website).'
description_long: Freiduria El Choco is on Calle Francisco Cano in Fuengirola, as given on its own website. The website lists Monday as closed and two service periods on the other days (13:00-16:00 and 20:00-23:00). It states that it does not take reservations, so families should expect to wait for a table at busy times. The website text we read gave no menu, prices or children's facilities, so these are not confirmed.
seo_title: Pulpería Freiduría El Choco, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Pulpería Freiduría El Choco (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Pulperia Freiduria El Choco' at C. Francisco Cano, 13, 29640 Fuengirola, Málaga, España (36.5509163,-4.6153718999999995), status OPERATIONAL, type restaurant.
  source_url: https://maps.google.com/?cid=15220038447403698154
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. Owner selected directory lead R-0108 on 2026-11-02 (checklist https://claude.ai/artifact/VCrXrv5vKsUhruvVk6R9ZT).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 14 min by car (6.2 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5509163%2C-4.6153718999999995&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule; booking_required
  claim: '"Monday\n\nClosed"; "Tuesday\n\n13:00 - 16:0020:00 - 23:00"; "Please note that we do not take reservations."'
  source_url: https://freiduriaelchoco.es/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: medium
  notes: Read via Firecrawl query, not full page. Wednesday to Sunday same hours as Tuesday per reader notes only (not quoted). No seasonality stated.
- field: links.contact; address
  claim: '"952 46 81 69"; "Calle Francisco Cano, 13, 29640 Fuengirlola, Málaga."'
  source_url: https://freiduriaelchoco.es/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: record-writer agent
  confidence: medium
  notes: Address spelled 'Fuengirlola' on the page, quoted as printed.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults medium, seniors medium; energy_level Low. Owner note (Danish): ''Klassisk fiskerestaurant Ingen bordreservation - ventetid''.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Restaurant, Rainy day, Half day, Premium."
  source_url: https://claude.ai/artifact/DZv9cLLQ1BEcYs3NeewdEF
  source_type: secondary
  checked_at: '2026-11-11'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-11
  confidence: medium
  notes: Owner's own judgment on the tag checklist on 2026-11-11 (previous tags were estimates from import); not independently verified. source_type secondary is the nearest schema value.
- field: visit_information.schedule
  claim: "\"13:00 - 16:00 20:00 - 23:00\" for each of the six open days; the first day in the list is marked closed"
  source_url: https://freiduriaelchoco.es/
  source_type: official_venue
  checked_at: '2026-11-11'
  checked_by: Claude (main session); own site fetched with tools/intake.py fetch and Tavily extract
  confidence: medium
  notes: "Own website (Tavily extract; the page is built with JavaScript and curl returns almost nothing). The days appear as numbered entries in the order Monday to Sunday; the earlier Firecrawl read of 2026-11-02 labelled the first entry Monday (closed) and the second Tuesday, which fits this order. Menu and prices are not in the page text."
review_issues: []
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: null
next_review_at: 2027-02-14
review_decision: null
redirects: []
---
