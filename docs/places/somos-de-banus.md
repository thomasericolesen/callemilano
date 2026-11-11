---
schema_version: 1.0.0
status: approved
id: ES-AND-MAL-SOMOS-DE-BANUS-001
slug: somos-de-banus
name: Somos de Banús
category: Restaurants
tags:
- Restaurant
- Full day
- Premium
coordinates:
  latitude: 36.4897645
  longitude: -4.9496195
  purpose: venue
  label: Somos de Banús, Av. de Julio Iglesias, Nueva Andalucía, 29660 Marbella, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ0z22kyUpcw0RnZmvtIburS4, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=3363606759040063901
external_ids:
  google_place_id: ChIJ0z22kyUpcw0RnZmvtIburS4
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 39 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Somos de Banús, Av. de Julio Iglesias, Nueva Andalucía, 29660 Marbella, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4897645,-4.9496195); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4897645%2C-4.9496195&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 39 min, 36.3 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: medium
  children: medium
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
  cost_basis: 'Own menu: mains 25-38 € (median about 29 €); drink prices not on own menu, so main plus one drink is about 31-35 €, inside 20-50 €. Owner decision 2026-11-08: €€ under the 2026-11-03 rule (replaces the 2026-11-02 choice of €€€). Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-08'
links:
  official_website: https://somosbanus.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- playa-puerto-banus
description_short: 'Somos de Banús: Mediterranean restaurant by the beach at Puerto Banús.'
description_long: Somos de Banús describes itself as a Mediterranean restaurant in Puerto Banús with cocktails and sea views (own website description). It lies about 50 m from the Puerto Banús beach point. Opening hours, prices and booking were not readable on the site.
seo_title: Somos de Banús, Marbella | CalleMilano
seo_description: 'Somos de Banús (Marbella): food, opening hours and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'Somos de Banús' at Av. de Julio Iglesias, Nueva Andalucía, 29660 Marbella, Málaga, España (36.4897645,-4.9496195), business status OPERATIONAL, primary type restaurant; about 51 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=3363606759040063901
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/decisions/one-hour-beach-restaurants-intake-2026-11-02.md, row rD01).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 39 min by car (36.3 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4897645%2C-4.9496195&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long, visit_information, food_available
  claim: 'Own site description: ''Gastronomía mediterránea, ambiente exclusivo, cócteles premium y vistas al Mediterráneo'' (page meta description, modified 2026-06-03).'
  source_url: https://somosbanus.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant fact check 2026-11-02)
  confidence: medium
  notes: Own website read with Firecrawl (direct quotes) on 2026-11-02. Only the page description was readable.
- field: cost_level
  claim: '"Arroz del "Senyoret" SOMOS Style 29€"; "Costilla de Ternera Angus 24h 38€"; "Churrasco Pollo "Jengibre & Lima" 25€"'
  source_url: https://somosbanus.com/menu/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: high
  notes: Menu lines quoted verbatim; name and price on adjacent lines joined with a space.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults high, seniors high; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Restaurant, Full day, Premium."
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
