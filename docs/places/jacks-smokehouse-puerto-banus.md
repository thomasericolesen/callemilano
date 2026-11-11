---
schema_version: 1.0.0
status: approved
id: ES-AND-MAL-JACKS-SMOKEHOUSE-PUERTO-BANUS-001
slug: jacks-smokehouse-puerto-banus
name: Jacks Smokehouse (Puerto Banús)
category: Restaurants
tags:
- Restaurant
- Rainy day
- Half day
- Premium
coordinates:
  latitude: 36.4885233
  longitude: -4.9510252
  purpose: venue
  label: Jacks Smokehouse, de Ribera, C. Mlle. Salman, 22-24, Nueva Andalucía, 29660 Marbella, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ1bNMKcEpcw0RacCk-_v-U_o, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=18038041290761093225
external_ids:
  google_place_id: ChIJ1bNMKcEpcw0RacCk-_v-U_o
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 41 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Jacks Smokehouse, de Ribera, C. Mlle. Salman, 22-24, Nueva Andalucía, 29660 Marbella, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4885233,-4.9510252); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4885233%2C-4.9510252&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 41 min, 36.4 km. One predicted sample.'
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
food_available: 'yes'
cost_level: €€
visit_information:
  schedule: null
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'No prices on own site; Tripadvisor price marking "€€ - €€€" read as the middle band. Fallback source per docs/trip-planner-agents.md. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).N'
  cost_checked_at: '2026-11-02'
links:
  official_website: https://www.jacks-smokehouse.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- playa-puerto-banus
description_short: 'Jack''s Smokehouse, Puerto Banús: New York-style barbecue restaurant in the port.'
description_long: Jack's Smokehouse is a New York-style barbecue restaurant with branches in Puerto Marina (Benalmádena) and Puerto Banús (own website description). This record is the Puerto Banús branch. Opening hours, prices and booking were not readable on the site.
seo_title: Jacks Smokehouse (Puerto Banús), Marbella | CalleMilano
seo_description: 'Jacks Smokehouse (Puerto Banús) (Marbella): food, opening hours and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'Jacks Smokehouse' at de Ribera, C. Mlle. Salman, 22-24, Nueva Andalucía, 29660 Marbella, Málaga, España (36.4885233,-4.9510252), business status OPERATIONAL, primary type american_restaurant; about 227 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=18038041290761093225
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/one-hour-beach-restaurants-intake-2026-11-02.md, row rD04).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 41 min by car (36.4 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4885233%2C-4.9510252&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long, visit_information, food_available
  claim: 'Own site description: ''Jacks Smokehouse Restaurant in Puerto Marina, Benalmádena and Puerto Banús brings a New York feel ... authentic BBQ experience''.'
  source_url: https://www.jacks-smokehouse.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant fact check 2026-11-02)
  confidence: medium
  notes: Own website read with Firecrawl (direct quotes) on 2026-11-02. Only the page description was readable.
- field: cost_level
  claim: '"€€ - €€€"'
  source_url: https://www.tripadvisor.es/Restaurant_Review-g1207898-d792718-Reviews-Jacks_Smokehouse-Puerto_Banus_Marbella_Costa_del_Sol_Province_of_Malaga_Andalucia.html
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: low
  notes: Tripadvisor price marking only (search excerpt); no ratings or reviews recorded. Own-site prices preferred when available. Quote from search snippet of tripadvisor.es listing. Name and town match (Puerto Banús).
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children high, children high, young_adults high, seniors high; energy_level Low. Owner note (Danish): ''Amerikansk restaurant, mest BBQ men også vegetar''.'
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
review_issues: []
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: '2026-11-11'
next_review_at: '2027-04-11'
review_decision:
  decision: approved
  reviewer: Eric Olesen (editor-of-record)
  date: '2026-11-11'
  notes: "Approved by the owner on 2026-11-11 after his own review of the place on the family-rating checklist (2026-11-10) and the tag checklist (2026-11-11), on top of the agent fact-check. Practical details that are still unknown stay shown as 'check before visiting'."
redirects: []
---
