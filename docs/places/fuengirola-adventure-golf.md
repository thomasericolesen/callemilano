---
schema_version: 1.0.0
status: approved
id: ES-AND-MAL-FUENGIROLA-ADVENTURE-GOLF-001
slug: fuengirola-adventure-golf
name: Fuengirola Adventure Golf
category: Family activities
tags:
- Adventure
- Half day
- Premium
coordinates:
  latitude: 36.532201
  longitude: -4.632048999999999
  purpose: venue
  label: Fuengirola Adventure Golf, Parque Fluvial, 29640 Fuengirola, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJZ4JOQgzicg0RwGNz_8aaJxo, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=1884645148557796288
external_ids:
  google_place_id: ChIJZ4JOQgzicg0RwGNz_8aaJxo
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 9 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Fuengirola Adventure Golf, Parque Fluvial, 29640 Fuengirola, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.532201,-4.632048999999999); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.532201%2C-4.632048999999999&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 9 min, 4.5 km. One predicted sample, not the Google Maps app''s main figure.'
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
food_available: unknown
cost_level: Unknown
visit_information:
  schedule: null
  typical_duration: About 1 hour per game (own website)
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: http://www.fuengirolaadventuregolf.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Fuengirola Adventure Golf: mini golf course in the Parque Fluvial, about 9 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: Fuengirola Adventure Golf is a mini golf course in the Parque Fluvial at Parque Fluvial, 29640 Fuengirola, Málaga. From Casa de la Familia it is about 9 minutes by car (Google route check, Saturday 10:00). Its own website describes a 19-hole adventure mini golf course for all ages, with a bar and restaurant; a game takes about one hour. Opening hours and prices were not readable on the homepage.
seo_title: Fuengirola Adventure Golf, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Fuengirola Adventure Golf (Fuengirola): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Fuengirola Adventure Golf' at Parque Fluvial, 29640 Fuengirola, Málaga, España (36.532201,-4.632048999999999), business status OPERATIONAL, website http://www.fuengirolaadventuregolf.com/.
  source_url: https://maps.google.com/?cid=1884645148557796288
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 9 min by car (4.5 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.532201%2C-4.632048999999999&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: 'Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time removed 2026-11-02 (owner decision: walking times of 20 minutes or more are not shown).'
- field: visit_information.typical_duration, description_long
  claim: 'Own website (page metadata): "19 hole putting adventure for all ages and skills with bar and restaurant"; "A game of Adventure Golf takes approximately 1hr".'
  source_url: http://www.fuengirolaadventuregolf.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: medium
  notes: Read from the homepage description and social metadata via Firecrawl on 2026-11-02; body text not captured.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children high, children high, young_adults high, seniors high; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Adventure, Half day, Premium."
  source_url: https://claude.ai/artifact/DZv9cLLQ1BEcYs3NeewdEF
  source_type: secondary
  checked_at: '2026-11-11'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-11
  confidence: medium
  notes: Owner's own judgment on the tag checklist on 2026-11-11 (previous tags were estimates from import); not independently verified. source_type secondary is the nearest schema value.
review_issues: []
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: '2026-11-02'
last_reviewed_at: '2026-11-11'
next_review_at: '2027-04-11'
review_decision:
  decision: approved
  reviewer: Eric Olesen (editor-of-record)
  date: '2026-11-11'
  notes: "Approved by the owner on 2026-11-11 after his own review of the place on the family-rating checklist (2026-11-10) and the tag checklist (2026-11-11), on top of the agent fact-check. Practical details that are still unknown stay shown as 'check before visiting'."
redirects: []
---
