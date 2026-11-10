---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-CHIRINGUITO-LA-CONCHA-EL-PALO-001
slug: chiringuito-la-concha-el-palo
name: Chiringuito La Concha (El Palo)
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.7190139
  longitude: -4.3596761
  purpose: venue
  label: Chiringuito La Concha - Sabores del Mediterráneo Málaga, C. Quitapenas, 115, Málaga-Este, 29017 Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJEbj4vddZcg0RpqAJYxegnoM, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=9484193887595110566
external_ids:
  google_place_id: ChIJEbj4vddZcg0RpqAJYxegnoM
municipality: Málaga
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 43 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Chiringuito La Concha - Sabores del Mediterráneo Málaga, C. Quitapenas, 115, Málaga-Este, 29017 Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.7190139,-4.3596761); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.7190139%2C-4.3596761&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 43 min, 46.8 km. One predicted sample.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: medium
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
cost_level: €
visit_information:
  schedule: 'Summer: daily 11:00-17:00 and 18:00-23:30 (own site); winter hours not published.'
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own menu: quoted mains 9,00 € pp (rice, min. 2), 14,00 € and 23,00 € (median 14,00 €) plus caña 2,30 € gives about 16,30 € per adult. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-02'
links:
  official_website: https://www.chiringuitolaconcha.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- playas-del-palo
description_short: 'Chiringuito La Concha: espetos and seafood on the beach at El Palo.'
description_long: 'Chiringuito La Concha is a beach restaurant on the front line of the beach at El Palo, serving sardine espetos grilled over open embers and fresh seafood, with a terrace and takeaway (own website). Summer hours on the site: daily 11:00-17:00 and 18:00-23:30; winter hours are not published there. Table booking via the website.'
seo_title: Chiringuito La Concha (El Palo), Málaga | CalleMilano
seo_description: 'Chiringuito La Concha (El Palo) (Málaga): food, opening hours and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'Chiringuito La Concha - Sabores del Mediterráneo Málaga' at C. Quitapenas, 115, Málaga-Este, 29017 Málaga, España (36.7190139,-4.3596761), business status OPERATIONAL, primary type bar; about 91 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=9484193887595110566
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/one-hour-beach-restaurants-intake-2026-11-02.md, row rB01).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 43 min by car (46.8 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.7190139%2C-4.3596761&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long, visit_information, food_available
  claim: 'Own site (modified 2026-07-17): ''Espetos y Pescados en EL PALO''; ''Espetos y Mariscos Frescos en Primera Línea de Playa''; terraza o para llevar; ''HORARIO DE VERANO 11:00 A 17:00/ 18:00 A 23:30 Todos los días''; Reservar.'
  source_url: https://www.chiringuitolaconcha.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant fact check 2026-11-02)
  confidence: high
  notes: Own website read with Firecrawl (direct quotes) on 2026-11-02.
- field: cost_level
  claim: '"Dorada a la plancha o al espeto 23,00€"; "Entrecot de ternera (Halal) 14,00€"; "Paella de Marisco 9,00€/ pers."; "Caña Cerveza 2,30€"; "Copa de Vino 3,50€"'
  source_url: https://chiringuitolaconcha.com/carta/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: high
  notes: Menu lines quoted verbatim; name and price on adjacent lines joined with a space.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children high, young_adults high, seniors high; energy_level Low.'
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
  description: 'Own website checked 2026-11-02. Still open: cost_level. Opening hours change by season; check before publishing.'
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
