---
schema_version: 1.0.0
status: approved
id: ES-AND-MAL-SOLO-BEACH-MARBELLA-001
slug: solo-beach-marbella
name: Solo Beach Marbella
category: Restaurants
tags:
- Beach
- Restaurant
- Full day
- Premium
coordinates:
  latitude: 36.4754104
  longitude: -4.9822923999999995
  purpose: venue
  label: Solo Beach Marbella, Av. Carlos Cano, 29670 Marbella, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ66dm7Pwrcw0RgbV8HvrKl2Y, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=7392600488954082689
external_ids:
  google_place_id: ChIJ66dm7Pwrcw0RgbV8HvrKl2Y
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 40 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Solo Beach Marbella, Av. Carlos Cano, 29670 Marbella, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.4754104,-4.9822923999999995); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4754104%2C-4.9822923999999995&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 40 min, 39.4 km. One predicted sample.'
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
  schedule: Daily 09:00-21:00 (own site, read 2026-11-02).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Own website: main tartar de atún 22 €, cocktails 12 €; main plus one drink about 34 €. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).'
  cost_checked_at: '2026-11-02'
links:
  official_website: https://solobeachmarbella.com/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- playa-de-san-pedro-alcantara
description_short: 'Solo Beach: Mediterranean beach restaurant and sunbeds on the sand at San Pedro de Alcántara.'
description_long: Solo Beach is a beach restaurant and beach club on the sand at San Pedro de Alcántara, serving Mediterranean food, poke and cocktails (own website). The site lists daily opening 09:00-21:00, sunbed hire ('Solo Hamaca', 10 €) and table booking on request; phone +34 621 35 09 97.
seo_title: Solo Beach Marbella, Marbella | CalleMilano
seo_description: 'Solo Beach Marbella (Marbella): food, opening hours and drive time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, related_places
  claim: Google Places lists 'Solo Beach Marbella' at Av. Carlos Cano, 29670 Marbella, Málaga, España (36.4754104,-4.9822923999999995), business status OPERATIONAL, primary type bar_and_grill; about 472 m straight line from the related beach point.
  source_url: https://maps.google.com/?cid=7392600488954082689
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Identity and position only. Owner selected this candidate on the restaurant checklist (docs/one-hour-beach-restaurants-intake-2026-11-02.md, row rE01).
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 40 min by car (39.4 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.4754104%2C-4.9822923999999995&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long, visit_information, food_available
  claim: 'Own site: ''Solo Beach nace en la arena de San Pedro de Alcántara''; cocina mediterránea, poke, cócteles; ''Lunes – Domingo 09:00 – 21:00''; ''Solo Hamaca 10 €''; Solicitar reserva; +34 621 35 09 97.'
  source_url: https://solobeachmarbella.com/
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (one-hour restaurant fact check 2026-11-02)
  confidence: high
  notes: Own website read with Firecrawl (direct quotes) on 2026-11-02.
- field: cost_level
  claim: '"Tartar de atún 22 €"; "Dubai Pancakes 9,5 €"; "Piña Colada Classic · 12 €"; "Aperol Spritz Aperitif · 12 €"; "Time to Share 36 € por persona"'
  source_url: https://solobeachmarbella.com/
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
  claim: "Owner's tag selection on the CalleMilano tag checklist: Beach, Restaurant, Full day, Premium."
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
