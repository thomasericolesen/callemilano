---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-PASEO-MARITIMO-MARBELLA-001
slug: paseo-maritimo-marbella
name: Paseo Marítimo de Marbella
category: Excursions
tags: []
coordinates:
  latitude: 36.507252799999996
  longitude: -4.8971162
  purpose: representative_point
  label: Paseo Maritimo De Marbella, P.º Marítimo, 2, 29602 Marbella, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJ22WccAAocw0RnQKI29MdqCI, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=2497278789135368861
external_ids:
  google_place_id: ChIJ22WccAAocw0RnQKI29MdqCI
municipality: Marbella
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 37 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Paseo Maritimo De Marbella, P.º Marítimo, 2, 29602 Marbella, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.507252799999996,-4.8971162); departure 2026-11-07T09:00:00Z (next Saturday morning), predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.507252799999996%2C-4.8971162&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 37 min, 27.4 km. One predicted sample.'
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
  visitor_information: https://turismo.marbella.es/servicios/oficinas-de-informacion-turistica/oficina-de-turismo-el-faro.html
  transport: null
  contact: null
related_places:
- marbella-old-town
- playa-de-nagueles
description_short: Marbella's seafront promenade, linked to the old town by the Avenida del Mar with its Dalí sculptures; about 37 min by car from Casa de la Familia.
description_long: The Paseo Marítimo is Marbella's seafront promenade. About 37 minutes by car from Casa de la Familia (Google route check). According to Turismo Marbella, the Avenida del Mar, decorated with fountains, pergolas and ten bronze sculptures designed by Salvador Dalí, links La Alameda at the edge of the old town with the promenade. The municipal El Faro tourist office stands beside the promenade on the way to the marina (Monday-Friday 08:30-19:30, weekends and holidays 10:00-16:00). A Turismo Marbella brochure lists the promenade at about 7 km (seen only in a search excerpt). Parking, toilets, accessibility and dog rules have not been checked.
seo_title: Paseo Marítimo de Marbella, Marbella | CalleMilano draft record
seo_description: 'Draft record for Paseo Marítimo de Marbella (Marbella): location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Paseo Maritimo De Marbella' at P.º Marítimo, 2, 29602 Marbella, Málaga, España (36.507252799999996,-4.8971162), status OPERATIONAL, type scenic_spot.
  source_url: https://maps.google.com/?cid=2497278789135368861
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Places API (New). Identity and position only.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 37 min by car (27.4 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.507252799999996%2C-4.8971162&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (intake pipeline 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes, DRIVE, TRAFFIC_AWARE_OPTIMAL.
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children high, children high, young_adults high, seniors high; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: description_long
  claim: 'Avenida del Mar: "Enlaza La Alameda con el Paseo Marítimo. Su superficie se encuentra adornada con fuentes, pérgolas, jardineras y una colección de 10 esculturas diseñadas por Salvador Dalí y fundidas en bronce por Bonvicini en Verona."'
  source_url: https://turismo.marbella.es/vive/naturaleza/parques-y-jardines/avenida-del-mar.html
  source_type: official_tourism
  checked_at: '2026-11-14'
  checked_by: Claude (main session), read in Claude in Chrome
  confidence: high
  notes: null
- field: description_long, links.visitor_information
  claim: '"La oficina de turismo de El Faro está ubicada junto al paseo marítimo, lugar de paso hacia al puerto deportivo." Hours: "De lunes a viernes de 08:30 a 19:30" "Fines de semana y festivos de 10:00 a 16:00".'
  source_url: https://turismo.marbella.es/servicios/oficinas-de-informacion-turistica/oficina-de-turismo-el-faro.html
  source_type: official_tourism
  checked_at: '2026-11-14'
  checked_by: Claude (main session), read in Claude in Chrome
  confidence: high
  notes: null
- field: description_long (length)
  claim: 'Search excerpt of the Turismo Marbella brochure "Marbella arqueológica": "Paseo Marítimo. 7kms / Seafront Promenade."'
  source_url: https://turismo.marbella.es/images/media/attachments/area-profesional/material-turistico/marbella_arqueologica.pdf
  source_type: official_tourism
  checked_at: '2026-11-14'
  checked_by: Claude (main session), read in Claude in Chrome
  confidence: medium
  notes: Search excerpt only; the PDF could not be read as text in this session.
review_issues:
- code: facts_partly_checked
  severity: warning
  owner: fact_check
  fields:
  - parking
  - toilets_available
  - accessibility
  - wheelchair_friendly
  - dog_friendly
  - cost_level
  retryable: true
  description: Read 2026-11-14 from Turismo Marbella (Avenida del Mar and El Faro tourist office pages). Length 7 km only from a search excerpt of an official brochure. Parking, toilets, accessibility, dog rules and cost (no official statement that it is free) not found.
created_at: '2026-11-02'
updated_at: '2026-11-14'
last_verified: '2026-11-14'
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---
