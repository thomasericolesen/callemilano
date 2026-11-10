---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-FUENGIROLA-TOWN-001
slug: fuengirola-town
name: Fuengirola (town)
category: City
tags: []
coordinates:
  latitude: 36.5391308
  longitude: -4.623502
  purpose: town_center
  label: Plaza de la Constitución, Pl. de la Constitución, 29640 Fuengirola, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ64o92Gricg0RM2XkaMd4I90, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=15934712704420570419
external_ids:
  google_place_id: ChIJ64o92Gricg0RM2XkaMd4I90
municipality: Fuengirola
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 15 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Plaza de la Constitución, Pl. de la Constitución, 29640 Fuengirola, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5391308,-4.623502); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5391308%2C-4.623502&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 15 min, 6.55 km. One predicted sample, not the Google Maps app''s main figure.'
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
  availability: 'yes'
  location_type: onsite
  cost: unknown
  restrictions: unknown
  walk_distance: Under or next to Plaza de la Constitución, by the church and the post office
  source: Owner's own repeated use (Eric Olesen, editor-of-record), confirmed 2026-11-02; arrival point chosen by the owner 2026-11-01
  checked_at: '2026-11-02'
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
  official_website: https://www.somosfuengirola.es/
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places: []
description_short: 'Fuengirola (town): the town of Fuengirola; the point is its main square, Plaza de la Constitución, about 15 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: Fuengirola (town) is the town of Fuengirola; the point is its main square, Plaza de la Constitución (Pl. de la Constitución, 29640 Fuengirola, Málaga, España). From Casa de la Familia it is about 15 minutes by car (Google route check, Saturday 10:00). Fuengirola's official tourism portal (Somos Fuengirola, checked 2026-11-02) presents the town through sunsets from the breakwater, concerts, shopping and walks along the Mediterranean. The municipal tourist office is at the entrance to the port. A fuller description of the centre (Plaza de la Constitución, church, old streets, market) is still to come from an official source. Check before visiting.
seo_title: Fuengirola (town), Fuengirola | CalleMilano draft record
seo_description: 'Draft record for Fuengirola (town) (Fuengirola): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Plaza de la Constitución' at Pl. de la Constitución, 29640 Fuengirola, Málaga, España (36.5391308,-4.623502), business status None, primary type None.
  source_url: https://maps.google.com/?cid=15934712704420570419
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 15 min by car (6.55 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5391308%2C-4.623502&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time over 20 minutes, so not shown (owner rule).
- field: description_long
  claim: 'Somos Fuengirola, ''Portal Oficial de Turismo de Fuengirola'': ''En Fuengirola somos de quienes nos viven: atardeceres desde el espigón, conciertos inolvidables, tardes de compras, paseos a orillas del Mediterráneo y noches ...''. andalucia.org: Fuengirola Municipal Tourist Office ''located in the centre of Fuengirola, at the entrance of the Port in a new building''.'
  source_url: https://www.somosfuengirola.es/
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: medium
  notes: Read via Firecrawl on 2026-11-02. Search excerpts; the portal's pages on the old centre were not found in this pass.
- field: parking
  claim: 'The underground car park at Plaza de la Constitución (by the church and the post office) exists and is the owner''s normal arrival point in Fuengirola: ''Parkeringskælderen er absolut ægte. Jeg bruger den hver gang jeg er i Spanien.'''
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/owner-decisions-2026-11-02.md
  source_type: secondary
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: high
  notes: Owner's first-hand knowledge given in the session chat 2026-11-02 (decision 15). source_type is the nearest schema value. Opening hours, prices and the exact entrance are not recorded.
  checked_at: '2026-11-02'
- field: driving_time_from_casa_de_la_familia (owner sample)
  claim: 'Owner''s Google Maps check 2026-11-01 (Sunday about 19:00) to Pl. de la Constitución: 16 min, 6.4 km via Av. Leopoldo Werner; alternatives 17 min / 6.6 km and 16 min / 6.3 km.'
  source_url: https://github.com/thomasericolesen/callemilano/tree/claude/awesome-clarke-tvlhrg
  source_type: secondary
  checked_by: Eric Olesen (owner), screenshot 2026-11-01; moved from the beach record by Claude 2026-11-02
  confidence: medium
  notes: Recorded on 2026-11-01 in the beach record by mistake (branch claude/awesome-clarke-tvlhrg, not merged). Matches this record's Routes API figure (15 min). The record keeps the Routes API value as its driving time.
  checked_at: '2026-11-02'
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children medium, children medium, young_adults high, seniors high; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
review_issues:
- code: category_editorial_choice
  severity: info
  fields:
  - category
  description: 'Category ''City'' was chosen by Claude from the schema definitions (routes and sights: Excursions; towns: City; natural areas: Nature; visitor attractions: Family activities). Confirm at editorial review.'
  retryable: true
  owner: human_editor
- code: town_description_thin
  severity: warning
  fields:
  - description_long
  - visit_information
  description: Only the tourism portal's general tagline and the tourist office location are sourced. Add the centre's sights from somosfuengirola.es before review; the record point is Plaza de la Constitución.
  retryable: true
  owner: fact_check
created_at: '2026-11-02'
updated_at: '2026-11-10'
last_verified: '2026-11-02'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
