---
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-JAY-JANGLES-001
slug: jay-jangles
name: Jay Jangles
category: Family activities
tags: []
coordinates:
  latitude: 36.551564
  longitude: -4.6824603
  purpose: venue
  label: Jay Jangles, La Cala Hills, C. Tomillo de la Torre, Local 3, 29650 Costa, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJr-2xwa3hcg0RAiysSGRZ4iM, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=2585727423314930690
external_ids:
  google_place_id: ChIJr-2xwa3hcg0RAiysSGRZ4iM
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 8 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Jay Jangles, La Cala Hills, C. Tomillo de la Torre, Local 3, 29650 Costa, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.551564,-4.6824603); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.551564%2C-4.6824603&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 8 min, 4.59 km. One predicted sample, not the Google Maps app''s main figure.'
age_groups: []
family_score:
  small_children: unknown
  children: unknown
  young_adults: unknown
  seniors: unknown
energy_level: Medium
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
  contact: null
related_places: []
description_short: 'Jay Jangles: children''s centre in La Cala Hills, about 8 min by car from Casa de la Familia. Draft; sources describe it as a nursery, not a visitor activity.'
description_long: Jay Jangles is listed by Google at La Cala Hills, C. Tomillo de la Torre, Local 3, 29650 Costa, Málaga, about 8 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). The only sources found (a 2015 newspaper article and a directory) describe it as a bilingual nursery, Jay Jangles Children's Centre, for enrolled children aged 1-6, not as a play centre open to visitors. It is not recommended until the owner has decided whether it belongs in the guide.
seo_title: Jay Jangles, Mijas | CalleMilano draft record
seo_description: 'Draft record for Jay Jangles (Mijas): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Jay Jangles' at La Cala Hills, C. Tomillo de la Torre, Local 3, 29650 Costa, Málaga, España (36.551564,-4.6824603), business status OPERATIONAL.
  source_url: https://maps.google.com/?cid=2585727423314930690
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 8 min by car (4.59 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.551564%2C-4.6824603&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: 'Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time removed 2026-11-02 (owner decision: walking times of 20 minutes or more are not shown).'
- field: description_long, category
  claim: 'Olive Press (22 Nov 2015): ''Pauline Wilson''s bilingual Jay Jangles Children''s Centre opened in October in La Cala Hills, with its number of enrolled children growing rapidly. The centre helps youngsters aged 1-6 years old by implementing the Early Years British curriculum.'''
  source_url: https://www.theolivepress.es/spain-news/2015/11/22/jay-jangles-all-the-way/
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: medium
  notes: Read via Firecrawl on 2026-11-02. Search results also show a 2015 Facebook post calling it 'a new nursery in La Cala Hills' and a directory listing it under nurseries. No own website or social page found; current operation and any drop-in play offer are unverified.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  description: Age groups and family scores are not assessed; energy_level Medium is an editorial estimate from the type of place.
  retryable: true
  owner: human_editor
- code: no_official_website
  severity: info
  fields:
  - links
  description: Google lists no website; facts may have to come from a social page or a direct contact.
  retryable: true
  owner: fact_check
- code: not_a_visitor_activity
  severity: blocking
  fields:
  - category
  - description_long
  description: 'Sources describe Jay Jangles as a nursery for enrolled children aged 1-6, not a play centre for visiting families. Owner decision needed: archive, or confirm a drop-in play offer from the venue.'
  retryable: true
  owner: human_editor
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: '2026-11-02'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
