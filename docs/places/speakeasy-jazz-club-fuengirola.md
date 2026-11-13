---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-SPEAKEASY-JAZZ-CLUB-FUENGIROLA-001
slug: speakeasy-jazz-club-fuengirola
name: Speakeasy Jazz Club & Cocktails
category: Restaurants
tags: []
coordinates:
  latitude: 36.5405146
  longitude: -4.6217781
  purpose: venue
  label: Speakeasy Jazz Club & Cocktails, Pje. de las Rampas, 10, 29640 Fuengirola, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJaaO9YGricg0RNKwi4iSWO3Y, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=8519568205258337332
external_ids:
  google_place_id: ChIJaaO9YGricg0RNKwi4iSWO3Y
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 16 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Speakeasy Jazz Club & Cocktails, Pje. de las Rampas, 10, 29640 Fuengirola, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5405146,-4.6217781); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5405146%2C-4.6217781&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 16 min, 6.67 km. Daytime sample; evening traffic differs.'
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
  official_website: https://speakeasy-jazz-club.sumupstore.com/productos
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Speakeasy Jazz Club & Cocktails: jazz club and cocktail bar, about 16 min by car, taxi or Uber from Casa de la Familia. Draft; partly fact-checked.'
description_long: Speakeasy Jazz Club & Cocktails is a jazz club and cocktail bar at Pje. de las Rampas, 10, 29640 Fuengirola, Málaga. From Casa de la Familia it is about 16 minutes by car, taxi or Uber (Google route check, Saturday 10:00; evening traffic differs). Its own online shop sells tickets for live concerts at 23:30 on many nights in October 2026 (jazz, blues and soul), at €56 or €84 per listed option; what each option includes (for example a table for two or drinks) is not stated in the listing. Regular opening hours were not checked. If you plan to drink, take a taxi or Uber both ways. As in any bar, keep an eye on your drink.
seo_title: Speakeasy Jazz Club & Cocktails, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Speakeasy Jazz Club & Cocktails (Fuengirola): location and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Speakeasy Jazz Club & Cocktails' at Pje. de las Rampas, 10, 29640 Fuengirola, Málaga, España (36.5405146,-4.6217781), business status OPERATIONAL, website https://speakeasy-jazz-club.sumupstore.com/productos.
  source_url: https://maps.google.com/?cid=8519568205258337332
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (bars intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 16 min by car (6.67 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5405146%2C-4.6217781&travelmode=driving
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
- field: description_long
  claim: 'Own SumUp shop (Speakeasy Cocktail Bar): concert tickets for October 2026 dates, all at 23:30 (e.g. Nasho Hot Blues 2/10, Phil Wilkinson Quartet 3/10, Sandie Ann Nielsen Trio 30/10), priced €56 or €84 with "more variants available".'
  source_url: https://speakeasy-jazz-club.sumupstore.com/productos
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (bars fact check 2026-11-02)
  confidence: medium
  notes: Shop listing quoted via Firecrawl on 2026-11-02; ticket contents not stated.
review_issues:
- code: audience_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  description: Added for adults and seniors; age groups and scores are not assessed. energy_level Low is an editorial estimate.
  retryable: true
  owner: human_editor
- code: owner_has_not_visited
  severity: info
  fields:
  - description_long
  description: The owner does not know this bar personally (2026-11-02). Consider a visit or more sources before recommending it.
  retryable: true
  owner: human_editor
- code: hours_and_ticket_terms_unknown
  severity: warning
  fields:
  - visit_information
  - cost_level
  description: Regular opening hours, whether entry without a ticket is possible, and what the €56/€84 options include need checking.
  retryable: true
  owner: fact_check
- code: source_attempt_not_found
  severity: info
  fields:
  - visit_information
  description: "Source attempt 2026-11-13 found nothing usable (blocked). curl returned HTTP 403. The Tavily extract step could not be run: no Tavily tool is available in this session. Not read; needs a Tavily extract or Mac session. Retry once more, then close the open facts as not found (value unknown, shown as check before visiting)."
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-13'
last_verified: '2026-11-02'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
