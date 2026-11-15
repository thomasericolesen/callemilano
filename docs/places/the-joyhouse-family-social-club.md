---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-THE-JOYHOUSE-FAMILY-SOCIAL-CLUB-001
slug: the-joyhouse-family-social-club
name: The Joyhouse family social club
category: Family activities
tags:
- Rainy day
- Premium
coordinates:
  latitude: 36.5462446
  longitude: -4.6179609
  purpose: venue
  label: The Joyhouse family social club, C. Asturias, 24, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJG_fvnvrjcg0RbJ6C_jRjj_A, read 2026-11-15
  checked_at: '2026-11-15'
google_maps_url: https://maps.google.com/?cid=17334182570031750764
external_ids:
  google_place_id: ChIJG_fvnvrjcg0RbJ6C_jRjj_A
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 15 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: The Joyhouse family social club, C. Asturias, 24, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-15 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5462446,-4.6179609); departure 2026-11-21T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5462446%2C-4.6179609&travelmode=driving
  checked_at: '2026-11-15'
  note: 'Routes API figure: 15 min, 6.3 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
family_score:
  small_children: high
  children: high
  young_adults: low
  seniors: low
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
cost_level: €
visit_information:
  schedule: Monday-Friday 14:30-22:00; Saturday-Sunday 11:00-22:00 (own website, 2026-11-15).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own website 2026-11-15: 7,95 € per child for 2 hours; adults free; socks 1 €.'
  cost_checked_at: '2026-11-15'
links:
  official_website: https://www.thejoyhouse.es/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'The Joyhouse: family social club in Fuengirola with soft play for children and a café-bar, open 7 days, about 15 min by car.'
description_long: The Joyhouse (formerly The Fun House) in Fuengirola is a family social club with a soft-play area and bouncy castle for children plus a café-bar for adults. Open Monday-Friday 14:30-22:00 and Saturday-Sunday 11:00-22:00. Play entry is 7,95 € per child for 2 hours, an extra hour 3,50 €; adults enter free. Socks are required in the play area and cost 1 € (own website, checked 2026-11-15). No age or height limit is stated. About 15 minutes by car from Casa de la Familia.
seo_title: The Joyhouse family social club, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for The Joyhouse family social club (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'The Joyhouse family social club' at C. Asturias, 24, 29640 Fuengirola, Málaga, España (36.5462446,-4.6179609), status OPERATIONAL, type indoor_playground.
  source_url: https://maps.google.com/?cid=17334182570031750764
  source_type: maps_identity
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: 'Google Places API (New). Identity and position only. Owner checklist 2026-11-15 (https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu): yes.'
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 15 min by car (6.3 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5462446%2C-4.6179609&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: visit_information.schedule, cost_level, description_long
  claim: '''Kids play centre'' / ''FAMILY SOCIAL CLUB · OPEN 7 DAYS''; ''Mon to Fri · 14:30pm – 10pm, Sat & Sun 11am – 10pm''; ''Play entry is just €7,95 per child for 2 hours''; ''extend your playtime for another hour for €3,50''; ''socks are available to buy for just €1''; ''Grown-ups enter for free!''; ''Socks are required in the play area.'''
  source_url: https://www.thejoyhouse.es/
  source_type: official_venue
  checked_at: '2026-11-15'
  checked_by: Claude (Desktop fact check 2026-11-15)
  confidence: medium
  notes: Page title says 'The Fun House Fuengirola' (earlier name).
- field: status
  claim: 'Lifted needs_fact_check -> needs_editorial_review: official or own-venue evidence for the core facts, no blocking or facts_not_checked issue (editor workflow, level A).'
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/AGENTS.md
  source_type: secondary
  checked_at: '2026-11-15'
  checked_by: Claude (main session)
  confidence: high
- field: tags, age_groups, family_score, energy_level
  claim: 'Editor decision 2026-11-15 on the tags list: tags = Rainy day, Premium; age_groups = Small children (0-6), Children (7-12); family_score = small_children high, children high, young_adults low, seniors low; energy_level = Low.'
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
