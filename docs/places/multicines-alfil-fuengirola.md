---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-MULTICINES-ALFIL-FUENGIROLA-001
slug: multicines-alfil-fuengirola
name: Multicines Alfil Fuengirola
category: Family activities
tags:
- Rainy day
coordinates:
  latitude: 36.5375077
  longitude: -4.6271906
  purpose: venue
  label: Multicines Alfil Fuengirola, C. Camilo José Cela, 6, 29640 Fuengirola, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJt0rcbxTicg0R9QGFfce_Bnk, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=8720868591974810101
external_ids:
  google_place_id: ChIJt0rcbxTicg0R9QGFfce_Bnk
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 12 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Multicines Alfil Fuengirola, C. Camilo José Cela, 6, 29640 Fuengirola, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5375077,-4.6271906); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5375077%2C-4.6271906&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 12 min, 4.92 km. One predicted sample, not the Google Maps app''s main figure.'
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
  official_website: https://www.cinesalfilfuengirola.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Multicines Alfil Fuengirola: cinema next to BIOPARC, about 12 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: Multicines Alfil Fuengirola is a cinema next to BIOPARC at C. Camilo José Cela, 6, 29640 Fuengirola, Málaga. From Casa de la Familia it is about 12 minutes by car (Google route check, Saturday 10:00). The cinema's own website (checked 2026-11-02) shows the current programme with online ticket sales, including children's and animated films and recorded opera and ballet broadcasts. Prices, opening hours, parking, accessibility and the language of screenings are not on the website. Check with the venue before visiting.
seo_title: Multicines Alfil Fuengirola, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Multicines Alfil Fuengirola (Fuengirola): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Multicines Alfil Fuengirola' at C. Camilo José Cela, 6, 29640 Fuengirola, Málaga, España (36.5375077,-4.6271906), business status OPERATIONAL, website https://www.cinesalfilfuengirola.com/.
  source_url: https://maps.google.com/?cid=8720868591974810101
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 12 min by car (4.92 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5375077%2C-4.6271906&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: 'Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time removed 2026-11-02 (owner decision: walking times of 20 minutes or more are not shown).'
- field: description_long, links
  claim: 'Cinema website shows the current programme (on 2026-11-02 including the children''s films ''Mascotas al rescate'' and ''Superthings: la película'', and opera/ballet broadcasts ''Carmen'', ''El Cascanueces'' and ''El lago de los cisnes'') with online ticket sales.'
  source_url: https://www.cinesalfilfuengirola.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: medium
  notes: Homepage read via Firecrawl on 2026-11-02. No price list, hours, parking or accessibility on the readable pages. The cinema's Facebook page appeared in search with a €3.50 promotion, but only as a search excerpt; not recorded.
review_issues:
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - energy_level
  description: Age groups and family scores are not assessed; energy_level Low is an editorial estimate from the type of place.
  retryable: true
  owner: human_editor
- code: prices_and_facilities_not_on_website
  severity: warning
  fields:
  - cost_level
  - visit_information
  - parking
  - accessibility
  description: The cinema website gives no prices, hours, parking, accessibility or screening language. Needs the cinema's own social pages (owner screenshot), a visit or a call.
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-02'
last_verified: '2026-11-02'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
