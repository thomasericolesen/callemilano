---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-EL-OCEANO-BEACH-HOTEL-001
slug: el-oceano-beach-hotel
name: El Oceano Beach Hotel
category: Restaurants
tags: []
coordinates:
  latitude: 36.4907937
  longitude: -4.6946639
  purpose: venue
  label: El Oceano Beach Hotel, Km 1026, C. Cádiz - Torrenueva, 31, 29649 Las Lagunas de Mijas, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJlyUiMrcfcw0RGhWs6bOiHHU, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=8438798695388681498
external_ids:
  google_place_id: ChIJlyUiMrcfcw0RGhWs6bOiHHU
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 17 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: El Oceano Beach Hotel, Km 1026, C. Cádiz - Torrenueva, 31, 29649 Las Lagunas de Mijas, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.4907937,-4.6946639); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4907937%2C-4.6946639&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 17 min, 10.37 km. Daytime sample; evening traffic differs.'
age_groups:
- Young adults
- Seniors
family_score:
  small_children: low
  children: low
  young_adults: high
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
booking_required: unknown
dog_friendly: unknown
toilets_available: unknown
food_available: 'yes'
cost_level: €€
visit_information:
  schedule: null
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own à la carte menu: quoted mains 26, 28 and 32 € (median 28 €); drink prices not on the page, so main plus one drink is about 30 € or more, inside 20-50 €. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03). Sunday menu prices: check before visiting (the hotel''s own page states two different sets, 49/59 and 45/55 EUR; left unknown by the editor''s decision on 2026-11-13).'
  cost_checked_at: '2026-11-02'
links:
  official_website: https://www.oceanohotel.com/
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34952587550
related_places: []
description_short: 'El Oceano Beach Hotel: beachfront hotel with restaurant and bar, about 17 min by car, taxi or Uber from Casa de la Familia. Draft; partly fact-checked.'
description_long: 'El Oceano Beach Hotel is a beachfront hotel with restaurant and bar at Km 1026, C. Cádiz - Torrenueva, 31, 29649 Las Lagunas de Mijas, Málaga. From Casa de la Familia it is about 17 minutes by car, taxi or Uber (Google route check, Saturday 10:00; evening traffic differs). Its own website: a beachfront hotel at Calle Cádiz de Torrenueva 31 (km 1026), Mijas Costa, with a restaurant that hosts live music almost every evening through the season, from piano sets to party nights, a lighter lunch menu and a pool bar at its Polynesian pool. Phone 952 587 550. Whether non-guests can use the pool bar, and prices, were not checked. If you plan to drink, take a taxi or Uber both ways. As in any bar, keep an eye on your drink.'
seo_title: El Oceano Beach Hotel, Mijas | CalleMilano draft record
seo_description: 'Draft record for El Oceano Beach Hotel (Mijas): location and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'El Oceano Beach Hotel & Restaurant' at Km 1026, C. Cádiz - Torrenueva, 31, 29649 Las Lagunas de Mijas, Málaga, España (36.4907937,-4.6946639), business status OPERATIONAL, website https://www.oceanohotel.com/.
  source_url: https://maps.google.com/?cid=8438798695388681498
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (bars intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 17 min by car (10.37 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4907937%2C-4.6946639&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (bars intake 2026-11-02)
  confidence: medium
  notes: 'Google Routes API computeRoutes, DRIVE (TRAFFIC_AWARE_OPTIMAL, Saturday 2026-11-07 10:00), from the project origin. Walking time removed 2026-11-02 (owner decision: guests reach bars in town by taxi or Uber).'
- field: status (selection)
  claim: Selected by the owner for the guide on the bars selection page; passed a reputation screen on 2026-11-02.
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/decisions/bars-selection-2026-11-02.md
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: medium
  notes: 'Screen: Google rating and count, 5 Google reviews, and web/news searches for drink spiking; nothing was found for this venue. The owner does not know the bar personally. Not a guarantee.'
- field: food_available, links, description_long
  claim: 'Own website: restaurant with live music almost every evening (UK and Spanish acts, e.g. piano sets by Johnny Baker, party nights) through the season; lite-bites lunch menu; pool bar at the Polynesian pool; address Km 1026, Calle Cádiz de Torrenueva 31, Mijas Costa 29649; phone +34 952 587 550.'
  source_url: https://www.oceanohotel.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (bars fact check 2026-11-02)
  confidence: high
  notes: Homepage quoted via Firecrawl on 2026-11-02 (page modified 2026-10-25). The site calls its restaurant "award-winning"; that claim is not repeated as fact.
- field: cost_level
  claim: '"Fillet of Seabass 32 €"; "Thai Scented Chicken 28 €"; "Fish ‘n’ Chips 26 €"'
  source_url: https://oceanohotel.com/restaurant/menus/a-la-carte
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: high
  notes: Menu lines quoted verbatim; name and price on adjacent lines joined with a space.
- field: visit_information.cost_basis (Sunday menu)
  claim: '"2 Courses 49€, 3 Courses 59€." ; "Two courses are priced at €45. Three courses at €55."'
  source_url: https://oceanohotel.com/restaurant/menus/sunday-menu
  source_type: official_venue
  checked_at: '2026-11-13'
  checked_by: record-writer agent
  confidence: medium
  notes: 'CONFLICT within the same page: both price sets quoted, not resolved.'
- field: visit_information.cost_basis (menus)
  claim: '"Creative Soup 11 €" ; "Fillet Steak 38 €"'
  source_url: https://oceanohotel.com/restaurant/menus/a-la-carte
  source_type: official_venue
  checked_at: '2026-11-13'
  checked_by: record-writer agent
  confidence: medium
  notes: Existing cost_basis cites mains 26, 28, 32 EUR; this fetch shows Fillet Steak 38 EUR, which may be outside that list. Editor to check with the conflict.
- field: visit_information.cost_basis (lunch menu)
  claim: '"Peking Duck Spring Rolls 12.50 €" ; "An optional 10% service charge will be added to your bill."'
  source_url: https://oceanohotel.com/restaurant/menus/lunch
  source_type: official_venue
  checked_at: '2026-11-13'
  checked_by: record-writer agent
  confidence: medium
  notes: null
- field: non-guest access, booking, children
  claim: '"As a lunchtime guest, you have full access to the terrace and pool area." ; "Please note: Children are very welcome in the restaurant, however the hotel and pool area are recommended for adults only. Thank you for your understanding." ; "Bookings can be made directly through the reservation system on this website, which is always the most reliable way to secure your table." ; "It is strongly recommended that you book as early as you can."'
  source_url: https://www.oceanohotel.com/
  source_type: official_venue
  checked_at: '2026-11-13'
  checked_by: record-writer agent
  confidence: medium
  notes: 'Pool access wording is from the lunch page, booking wording from the Sunday-menu page; whether non-hotel-guests may use the Polynesian pool/pool bar is still not stated. Dinner-with-music booking rule not found. Phone: "Telephone  (+34) 952 587 550".'
- field: visit_information.cost_basis (Sunday menu)
  claim: 'Editor decision 2026-11-13 on the editor list: write ''check before visiting'' and leave the Sunday menu prices unknown.'
  source_url: https://claude.ai/artifact/EpwDTtUv1wLvgu1u5Yy5Jn
  source_type: secondary
  checked_at: '2026-11-13'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-13
  confidence: medium
  notes: Resolves the source_conflict opened 2026-11-13; the a la carte Fillet Steak 38 EUR is noted in the evidence only.
- field: review_issues
  claim: 'Editor decision 2026-11-14 on editor list (2): close owner_has_not_visited; family feedback in the app replaces it (approval rule 2026-11-10).'
  source_url: https://claude.ai/artifact/2HgGANPzRn8pRQqqdGcur1
  source_type: secondary
  checked_at: '2026-11-14'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-14
  confidence: high
  notes: The editor's own judgement; answers stored in collection editorlist-2026-11-14b.
- field: age_groups, family_score, energy_level
  claim: 'Editor decision 2026-11-14 on editor list (2), same values for all 13 bars: age_groups = Young adults, Seniors; energy_level = Low; family_score.children = low; family_score.seniors = medium; family_score.small_children = low; family_score.young_adults = high.'
  source_url: https://claude.ai/artifact/2HgGANPzRn8pRQqqdGcur1
  source_type: secondary
  checked_at: '2026-11-14'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-14
  confidence: high
  notes: The editor's own judgement; answers stored in collection editorlist-2026-11-14b.
review_issues:
- code: not_found_after_two_attempts
  severity: info
  owner: fact_check
  fields:
  - booking_required
  - cost_level
  retryable: true
  description: 'Two source attempts (latest 2026-11-14) found no official answer for: whether non-guests can use the pool and pool bar, and their prices (the own site only offers table booking). Value left as it is; check before visiting. Retry at the next freshness review.'
created_at: '2026-11-02'
updated_at: '2026-11-14'
last_verified: '2026-11-02'
last_reviewed_at: '2026-11-14'
next_review_at: 2027-02-14
review_decision: null
redirects: []
---
