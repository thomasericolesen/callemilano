---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-MAYAN-MONKEY-MIJAS-CHOCOLATE-FACTORY-001
slug: mayan-monkey-mijas-chocolate-factory
name: Mayan Monkey Mijas Chocolate Factory
category: Excursions
tags:
- Rainy day
coordinates:
  latitude: 36.596157999999996
  longitude: -4.6377387
  purpose: venue
  label: Mayan Monkey Mijas Chocolate Factory, Pl. Virgen de la Peña, 15, 29650 Mijas, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJRZr4teTjcg0RCuP2NwKx00E, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=4743329455638242058
external_ids:
  google_place_id: ChIJRZr4teTjcg0RCuP2NwKx00E
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 21 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Mayan Monkey Mijas Chocolate Factory, Pl. Virgen de la Peña, 15, 29650 Mijas, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.596157999999996,-4.6377387); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.596157999999996%2C-4.6377387&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 21 min, 11.3 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: high
  children: high
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
  schedule: Every day 10:30-18:00 (own website, 2026-11-15).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own website 2026-11-15: factory tours free; workshops 19,95-139,95 € (unit not stated on the front page).'
  cost_checked_at: '2026-11-15'
links:
  official_website: https://mayanmonkey.es/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Mayan Monkey Mijas: working chocolate factory in Mijas Pueblo with free tours and workshops from age 3, about 21 min by car.'
description_long: Mayan Monkey is a working chocolate factory on Plaza Virgen de la Peña in Mijas Pueblo, open every day 10:30-18:00. Factory tours are free; hands-on chocolate workshops start at 19,95 € (25 min) and run up to 139,95 € for a 2-hour masterclass. Workshops are hands-on from age 3, under-3s are free, and a weekend workshop is designed for families with children aged 3-10 (own website, checked 2026-11-15). About 21 minutes by car from Casa de la Familia.
seo_title: Mayan Monkey Mijas Chocolate Factory, Mijas | CalleMilano draft record
seo_description: 'Draft record for Mayan Monkey Mijas Chocolate Factory (Mijas): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Mayan Monkey Mijas Chocolate Factory' at Pl. Virgen de la Peña, 15, 29650 Mijas, Málaga, España (36.596157999999996,-4.6377387), status OPERATIONAL, type tourist_attraction.
  source_url: https://maps.google.com/?cid=4743329455638242058
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 21 min by car (11.3 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.596157999999996%2C-4.6377387&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule, description_long
  claim: '''a real working chocolate factory in the heart of Mijas Pueblo''; ''Open every day from 10:30 to 18:00 at Plaza Virgen de la Peña''; ''Free factory tours available daily''.'
  source_url: https://mayanmonkey.es/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
- field: age_groups (input), visit_information.cost_basis
  claim: '''Hands-on from age 3'', ''Under 3s free''; ''Weekend Wonder Workshop ... Designed for families with younger kids (aged 3 to 10)''; workshops 25 min €19.95, 40 min €35.00, 1h10 €49.95–€59.95, 1h €69.95, 1h30 €109.95–€119.95, ''MMM Masterclass'' 2h €139.95.'
  source_url: https://mayanmonkey.es/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
  notes: Whether workshop prices are per person is not stated on the front page.
- field: status
  claim: 'Lifted needs_fact_check -> needs_editorial_review: official or own-venue evidence for the core facts, no blocking or facts_not_checked issue (editor workflow, level A).'
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/AGENTS.md
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (main session)
  confidence: high
- field: tags, age_groups, family_score, energy_level
  claim: 'Editor decision 2026-11-15 on the tags list: tags = Rainy day; age_groups = Small children (0-6), Children (7-12), Young adults, Seniors; family_score = small_children high, children high, young_adults medium, seniors medium; energy_level = Low.'
  source_url: https://claude.ai/artifact/VoHiKgGvqiiP3YA66KP3s5
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-15
  confidence: high
  notes: The editor's own judgement; answers stored in collection tags_2026_11_15.
review_issues: []
created_at: '2026-11-15'
updated_at: '2026-11-15'
last_verified: '2026-11-15'
last_reviewed_at: '2026-11-15'
next_review_at: '2027-04-15'
review_decision: null
redirects: []
---
