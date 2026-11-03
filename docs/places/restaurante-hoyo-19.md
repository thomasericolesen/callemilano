---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-RESTAURANTE-HOYO-19-001
slug: restaurante-hoyo-19
name: Restaurante Hoyo 19
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.5438292
  longitude: -4.6550717
  purpose: venue
  label: Restaurante Hoyo 19, Camino viejo de Coín, 0 km 4 , 700, 29651 Las Lagunas de Mijas, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJzXgrOy3hcg0RUN29_2pjMNU, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=15361887640169078096
external_ids:
  google_place_id: ChIJzXgrOy3hcg0RUN29_2pjMNU
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 4 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante Hoyo 19, Camino viejo de Coín, 0 km 4 , 700, 29651 Las Lagunas de Mijas, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.5438292,-4.6550717); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5438292%2C-4.6550717&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 4 min, 1.58 km. One predicted sample, not the Google Maps app''s main figure.'
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
  official_website: https://restaurantehoyo19.metro.bar/
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34622797207
related_places: []
description_short: 'Restaurante Hoyo 19: Spanish restaurant on the Camino Viejo de Coín, about 4 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: Restaurante Hoyo 19 is a Spanish restaurant on the Camino Viejo de Coín at Camino viejo de Coín, 0 km 4 , 700, 29651 Las Lagunas de Mijas, Málaga. From Casa de la Familia it is about 4 minutes by car (Google route check, Saturday 10:00). Its own small website (hosted on METRO's restaurant-site service) gives the address and phone 622 797 207 and opening hours from 08:00 to about 23:00 on most days with one closing day, but the day-by-day table could not be read reliably. Prices, menu, children's facilities and accessibility are not checked; check before visiting.
seo_title: Restaurante Hoyo 19, Mijas | CalleMilano draft record
seo_description: 'Draft record for Restaurante Hoyo 19 (Mijas): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, food_available
  claim: Google Places lists 'Restaurante Hoyo 19' at Camino viejo de Coín, 0 km 4 , 700, 29651 Las Lagunas de Mijas, Málaga, España (36.5438292,-4.6550717), business status OPERATIONAL, website https://restaurantehoyo19.metro.bar/.
  source_url: https://maps.google.com/?cid=15361887640169078096
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 4 min by car (1.58 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5438292%2C-4.6550717&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: 'Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time removed 2026-11-02 (owner decision: walking times of 20 minutes or more are not shown).'
- field: links.contact, description_long
  claim: 'Own site: Restaurante Hoyo 19, Camino Viejo de Coín km 4.7, 29651 Las Lagunas de Mijas; phone +34 622 797 207 (also +34 951 322 558); opening hours 08:00-23:00 (one day 08:00-24:00, one day closed).'
  source_url: https://restaurantehoyo19.metro.bar/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: medium
  notes: Quoted via Firecrawl on 2026-11-02; the weekday labels of the hours table were not all captured, so no schedule is recorded.
- field: cost_level
  claim: '"€€ - €€€"'
  source_url: https://www.tripadvisor.es/Restaurant_Review-g580271-d1003386-Reviews-Restaurante_Hoyo_19-Mijas_Costa_del_Sol_Province_of_Malaga_Andalucia.html
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: low
  notes: Tripadvisor price marking only (search excerpt); no ratings or reviews recorded. Own-site prices preferred when available. Quote from search snippet of tripadvisor.es listing 'RESTAURANTE HOYO 19, Mijas'. Name and town match.
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
- code: hours_by_day_unclear
  severity: warning
  fields:
  - visit_information
  - cost_level
  description: Hours by weekday, closing day, menu and prices still need checking.
  retryable: true
  owner: fact_check
- code: cost_level_secondary_source
  severity: info
  fields:
  - cost_level
  description: cost_level is based on the Tripadvisor price marking, not the own menu; replace when an own menu with prices is found.
  retryable: true
  owner: human_editor
created_at: '2026-11-02'
updated_at: '2026-11-03'
last_verified: '2026-11-02'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
