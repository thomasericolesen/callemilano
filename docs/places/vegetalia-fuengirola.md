---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-VEGETALIA-FUENGIROLA-001
slug: vegetalia-fuengirola
name: Restaurante Vegetalia
category: Restaurants
tags:
- Restaurant
- Half day
coordinates:
  latitude: 36.5529963
  longitude: -4.617451
  purpose: venue
  label: Restaurante Vegetalia, C. Sta. Isabel, 8, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ3SAuZE_icg0R3oY_Vln9aQM, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=246006214809323230
external_ids:
  google_place_id: ChIJ3SAuZE_icg0R3oY_Vln9aQM
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 16 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante Vegetalia, C. Sta. Isabel, 8, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5529963,-4.617451); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5529963%2C-4.617451&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 16 min, 6.7 km. One predicted sample.'
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
  contact: tel:+34952586031
related_places: []
description_short: 'Restaurante Vegetalia: vegetarian restaurant with an ovo-lacto-vegetarian buffet in central Fuengirola, about 16 min by car from Casa de la Familia.'
description_long: Restaurante Vegetalia is a vegetarian restaurant at Calle Santa Isabel 8, 29640 Fuengirola, about 16 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Its own Facebook page describes a 'buffet ovo-lacto-vegetariano' (eggs and dairy, no meat or fish) and lists phone +34 952 58 60 31. The page posts a daily dish, the latest on 9 November 2026 for Tuesday 10 November, so the restaurant appears active. Opening days and hours are not stated, and the buffet price was not found; check before going.
seo_title: Restaurante Vegetalia, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Restaurante Vegetalia (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Restaurante Vegetalia' at C. Sta. Isabel, 8, 29640 Fuengirola, Málaga, España (36.5529963,-4.617451), status OPERATIONAL, type vegetarian_restaurant.
  source_url: https://maps.google.com/?cid=246006214809323230
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. Owner selected directory lead R-0110 on 2026-11-02 (checklist https://claude.ai/artifact/VCrXrv5vKsUhruvVk6R9ZT).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 16 min by car (6.7 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5529963%2C-4.617451&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long; address; links.contact
  claim: '"buffet ovo-lacto-vegetariano"; address "Calle Santa Isabel, 8, Fuengirola, Spain, 29640"; phone "+34 952 58 60 31"'
  source_url: https://www.facebook.com/vegetaliafuengirola
  source_type: official_venue
  checked_at: '2026-11-10'
  checked_by: Claude (main session), Claude in Chrome, logged-in read-only
  confidence: medium
  notes: Own Facebook page, read 2026-11-10. Daily dish posts (latest 9 Nov 2026 for Tue 10.11.; also 3-7 Nov) show activity; open days appear to be Tuesday to Saturday but this is inferred, not stated, so no schedule is set. Facebook label 'Moderat' is not a menu price. Buffet price not found.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults medium, seniors medium; energy_level Low. Owner note (Danish): ''Vegetar og vegansk restaurant''.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Restaurant, Half day."
  source_url: https://claude.ai/artifact/DZv9cLLQ1BEcYs3NeewdEF
  source_type: secondary
  checked_at: '2026-11-11'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-11
  confidence: medium
  notes: Owner's own judgment on the tag checklist on 2026-11-11 (previous tags were estimates from import); not independently verified. source_type secondary is the nearest schema value.
review_issues: []
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
