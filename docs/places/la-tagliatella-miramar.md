---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-LA-TAGLIATELLA-MIRAMAR-001
slug: la-tagliatella-miramar
name: La Tagliatella (C.C. Miramar)
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.528461899999996
  longitude: -4.6317998
  purpose: venue
  label: Restaurante La Tagliatella | Fuengirola, CC Miramar, Av. de la Encarnación, s/n, Planta 1, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJHzgiD37jcg0ROY-ZzB1cFE8, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=5698280711586942777
external_ids:
  google_place_id: ChIJHzgiD37jcg0ROY-ZzB1cFE8
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 8 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Restaurante La Tagliatella | Fuengirola, CC Miramar, Av. de la Encarnación, s/n, Planta 1, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.528461899999996,-4.6317998); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.528461899999996%2C-4.6317998&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 8 min, 4.2 km. One predicted sample.'
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
  schedule: Mon-Thu 12:00-23:00; Fri-Sat 12:00-23:30; Sun 12:00-23:00. Not stated as seasonal (official page, read 2026-11-10).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: https://www.latagliatella.es/restaurantes/malaga/cc-miramar-fuengirola?utm_source=gmb&utm_medium=organic&utm_campaign=gmb&utm_content=web
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34951026629
related_places: []
description_short: 'La Tagliatella (C.C. Miramar): Italian restaurant chain at the Miramar shopping centre, open daily from 12:00, about 8 min by car from Casa de la Familia.'
description_long: La Tagliatella (C.C. Miramar) is an Italian restaurant chain branch at the Miramar shopping centre, Av. de la Encarnación s/n, 29640 Fuengirola (phone +34 951 02 66 29), about 8 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). The official page lists opening hours of 12:00-23:00 Monday to Thursday and on Sunday, and 12:00-23:30 on Friday and Saturday, and offers booking and takeaway (delivery is shown greyed out). Menu prices were not checked.
seo_title: La Tagliatella (C.C. Miramar), Fuengirola | CalleMilano draft record
seo_description: 'Draft record for La Tagliatella (C.C. Miramar) (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Restaurante La Tagliatella | Fuengirola' at CC Miramar, Av. de la Encarnación, s/n, Planta 1, 29640 Fuengirola, Málaga, España (36.528461899999996,-4.6317998), status OPERATIONAL, type italian_restaurant.
  source_url: https://maps.google.com/?cid=5698280711586942777
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. Owner selected directory lead R-0207 on 2026-11-02 (checklist https://claude.ai/artifact/VCrXrv5vKsUhruvVk6R9ZT).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 8 min by car (4.2 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.528461899999996%2C-4.6317998&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: links.contact; address; visit_information.schedule
  claim: '"CC Miramar, Fuengirola", "Av. de la Encarnación s/n, 29640, Málaga", "+34951026629". Monday 12:00-23:00; Tuesday 12:00-23:00; Wednesday 12:00-23:00; Thursday 12:00-23:00; Friday 12:00-23:30; Saturday 12:00-23:30; Sunday 12:00-23:00'
  source_url: https://www.latagliatella.es/restaurantes/malaga/cc-miramar-fuengirola
  source_type: official_venue
  checked_at: '2026-11-10'
  checked_by: Claude (main session), Claude in Chrome, logged-in read-only
  confidence: high
  notes: Official chain page for this branch, read in a real browser 2026-11-10. Page offers booking and takeaway; delivery greyed out. Hours may differ on holidays.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children high, children high, young_adults high, seniors high; energy_level Low. Owner note (Danish): ''Pizza og pasta i Shoppingcenteret Miramar''.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
review_issues:
- code: facts_partly_checked
  severity: warning
  fields:
  - cost_level
  - accessibility
  - parking
  description: 'Address, phone and weekly hours from the official page (2026-11-10). Still open: menu prices (cost_level Unknown), accessibility, parking, child facilities.'
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-10'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
