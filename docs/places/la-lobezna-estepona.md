---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-LA-LOBEZNA-ESTEPONA-001
slug: la-lobezna-estepona
name: La Lobezna (Estepona)
category: Restaurants
tags:
- Restaurant
coordinates:
  latitude: 36.4203681
  longitude: -5.1562643
  purpose: venue
  label: La Lobezna – Bar Restaurante en Estepona, Calle Tres Banderas, 30, 29680 Estepona, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJo_Gfz1rXDA0RWQTAsvoNI1U, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=6134762487800661081
external_ids:
  google_place_id: ChIJo_Gfz1rXDA0RWQTAsvoNI1U
municipality: Estepona
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 54 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: La Lobezna – Bar Restaurante en Estepona, Calle Tres Banderas, 30, 29680 Estepona, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4203681,-5.1562643); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4203681%2C-5.1562643&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 54 min, 60.0 km. One predicted sample.'
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
cost_level: €
visit_information:
  schedule: Mon-Tue, Thu-Sat 13:00-23:00; Sun 12:00-16:30; Wednesday not listed (own site, read 2026-11-02).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own menu: quoted mains 13,50, 14,75 and 21,00 € (median 14,75 €) plus caña 1,60 € gives about 16,35 € per adult. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-02'
links:
  official_website: https://www.lalobezna.es/en/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- playa-de-la-rada-estepona
description_short: 'La Lobezna, Estepona: bar-restaurant with seafood, Spanish and Latin American dishes.'
description_long: 'La Lobezna is a bar-restaurant in Estepona serving seafood, Spanish and Latin American dishes, with table booking and takeaway (own ordering website). Hours on the site: Monday-Tuesday and Thursday-Saturday 13:00-23:00, Sunday 12:00-16:30, closed Wednesday.'
seo_title: La Lobezna (Estepona), Estepona | CalleMilano
seo_description: 'La Lobezna (Estepona) (Estepona): food, opening hours and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'La Lobezna – Bar Restaurante en Estepona' at Calle Tres Banderas, 30, 29680 Estepona, Málaga, España (36.4203681,-5.1562643), business status OPERATIONAL, primary type bar_and_grill; about 411 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=6134762487800661081
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/one-hour-beach-restaurants-intake-2026-11-02.md, row rF02).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 54 min by car (60.0 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4203681%2C-5.1562643&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long, visit_information, food_available
  claim: 'Own ordering site: ''Seafood, Spanish, Latinoamericana''; Table Reservation; Pick-up; Monday-Tuesday, Thursday-Saturday 13:00-23:00; Sunday 12:00-16:30.'
  source_url: https://www.lalobezna.es/en/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant fact check 2026-11-02)
  confidence: medium
  notes: Own website read with Firecrawl (direct quotes) on 2026-11-02.
- field: cost_level
  claim: '"Entrecot de ternera 21,00 EUR"; "Paella de pollo 13,50 EUR"; "Lubina a la plancha 14,75 EUR"; "Caña 1,60 EUR"; "Verdejo Copa 2,50 EUR"'
  source_url: https://www.lalobezna.es/en/menu
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: high
  notes: Menu lines quoted verbatim; name and price on adjacent lines joined with a space.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children unknown, children unknown, young_adults unknown, seniors unknown; energy_level Low. Owner note (Danish): ''Eftermiddag og aften restaurant''.'
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
  - booking_required
  description: 'Own website checked 2026-11-02. Still open: cost_level. Opening hours change by season; check before publishing.'
  retryable: true
  owner: fact_check
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - tags
  description: 'Owner answered ''Ved ikke'' (or left blank) on the 2026-11-10 checklist for: small_children, children, young_adults, seniors. Energy level set by owner. Tags not assessed.'
  retryable: true
  owner: human_editor
created_at: '2026-11-02'
updated_at: '2026-11-10'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
