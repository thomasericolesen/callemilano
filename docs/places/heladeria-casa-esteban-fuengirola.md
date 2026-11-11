---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-HELADERIA-CASA-ESTEBAN-FUENGIROLA-001
slug: heladeria-casa-esteban-fuengirola
name: Heladería Casa Esteban
category: Restaurants
tags:
- Restaurant
- Half day
- Free
coordinates:
  latitude: 36.53738
  longitude: -4.622
  purpose: venue
  label: Heladería casa Esteban, P.º Marítimo Rey de España, 26, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJxcDPWADjcg0RzAbeG1NeKCI, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=2461320907400808140
external_ids:
  google_place_id: ChIJxcDPWADjcg0RzAbeG1NeKCI
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 15 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Heladería casa Esteban, P.º Marítimo Rey de España, 26, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.53738,-4.622); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.53738%2C-4.622&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 15 min, 5.1 km. One predicted sample.'
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
  contact: tel:+34952192942
related_places: []
description_short: 'Heladería Casa Esteban: artisan ice-cream parlour on the Paseo Marítimo in Fuengirola; this shop stays open in winter according to its own Instagram. About 15 min by car from Casa de la Familia.'
description_long: 'Heladería Casa Esteban is an artisan ice-cream parlour with three shops (Mijas Pueblo, La Cala de Mijas and Fuengirola); this record is the Fuengirola shop at Paseo Marítimo Rey de España 26 (phone 952 19 29 42), according to the shop''s own Instagram and Facebook pages. In an Instagram post of about 9 November 2026 the shop says that Sunday 15 November is the last day of the season in Mijas Pueblo and La Cala de Mijas, and that the Fuengirola shop stays open during the winter. Opening hours and prices are not published on its Facebook or Instagram pages; check before going. About 15 minutes by car from Casa de la Familia (Google route check, Saturday 10:00). Family recommendation (Christian, callemilano.dk): Good ice cream.'
seo_title: Heladería Casa Esteban, Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Heladería Casa Esteban (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Heladería casa Esteban' at P.º Marítimo Rey de España, 26, 29640 Fuengirola, Málaga, España (36.53738,-4.622), status OPERATIONAL, type ice_cream_shop.
  source_url: https://maps.google.com/?cid=2461320907400808140
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Places API (New). Identity and position only. From the owner's recommendations on callemilano.dk (Lovable app 'Vores Spanske Hjem', table recommendations), read 2026-11-02.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 15 min by car (5.1 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.53738%2C-4.622&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: description_long (owner knowledge)
  claim: Gode is 🍧🍨🍦
  source_url: https://callemilano.dk/
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Christian (family member, per Eric 2026-11-08); recorded by Claude 2026-11-02
  confidence: medium
  notes: 'Family recommendation by Christian (corrected 2026-11-08; first recorded as the owner''s) (kind ''anbefaling'') on callemilano.dk, read from the Lovable app database 2026-11-02; site tags: børn, is. Personal experience, not independently verified.'
- field: address; links.contact
  claim: '"Mijas Pueblo: Pasaje Esteban Moreno 1 952485216 La Cala de Mijas: Calle Marbella 3 952493549 Fuengirola: Paseo Marítimo Rey de España 26 952192942." ; "Nos encontramos en calle Marbella n3, La Cala de Mijas, Paseo Marítimo Rey de España n26, Fuengirola y pasaje Esteban Moreno n1, Mijas pueblo."'
  source_url: https://www.instagram.com/heladeriacasaesteban
  source_type: official_venue
  checked_at: '2026-11-08'
  checked_by: Claude (main session), Tavily search excerpts
  confidence: medium
  notes: Search excerpts of the shop's own Instagram profile and Facebook page (https://www.facebook.com/heladeriacasaesteban); the pages themselves are behind a login wall. Matches the Google Places point on the Paseo Marítimo in Fuengirola.
- field: description_long (seasonality)
  claim: '"El domingo 15 de noviembre será nuestro último día de esta temporada ... en Mijas Pueblo y La Cala de Mijas. Recordad que en la heladería de Fuengirola seguiremos abiertos durante el invierno."'
  source_url: https://www.instagram.com/p/DfgslxGNjUd/
  source_type: official_venue
  checked_at: '2026-11-10'
  checked_by: Claude (main session), Claude in Chrome, logged-in read-only
  confidence: high
  notes: Own Instagram post, about 2026-11-09. No opening hours on the Instagram or Facebook page. Facebook shows the category label 'Isbutik · Billig' (Facebook price range, not a menu price; not used for cost_level). Phone and email on Facebook (+34 952 48 52 16, heladeriacasaesteban@gmail.com) belong to the Mijas Pueblo shop.
- field: address; links.contact
  claim: '"Fuengirola: Paseo Marítimo Rey de España 26 952192942"'
  source_url: https://www.instagram.com/heladeriacasaesteban/
  source_type: official_venue
  checked_at: '2026-11-10'
  checked_by: Claude (main session), Claude in Chrome, logged-in read-only
  confidence: high
  notes: Own Instagram bio, confirms the earlier search-excerpt reading.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children high, children high, young_adults high, seniors high; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Restaurant, Half day, Free."
  source_url: https://claude.ai/artifact/DZv9cLLQ1BEcYs3NeewdEF
  source_type: secondary
  checked_at: '2026-11-11'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-11
  confidence: medium
  notes: Owner's own judgment on the tag checklist on 2026-11-11 (previous tags were estimates from import); not independently verified. source_type secondary is the nearest schema value.
review_issues:
- code: facts_partly_checked
  severity: warning
  fields:
  - visit_information
  - cost_level
  description: 'Address, phone and winter opening of the Fuengirola shop from the shop''s own Instagram (2026-11-10). Still open: weekly opening hours (not published on Facebook or Instagram) and prices; no own website.'
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
