---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-MAL-MIRADOR-DEL-COMPAS-001
slug: mirador-del-compas
name: Mirador del Compás (Virgen de la Peña)
category: Excursions
tags: []
coordinates:
  latitude: 36.5953395
  longitude: -4.6358648
  purpose: venue
  label: Mirador del Compás, 29650 Mijas, Málaga, España (Google Places listing)
  source: Google Places API (New), place ChIJrbTatfrjcg0R61fvsLvW2is, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=3160074190169528299
external_ids:
  google_place_id: ChIJrbTatfrjcg0R61fvsLvW2is
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 21 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Mirador del Compás, 29650 Mijas, Málaga, España
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875,-4.6626875) to the Google Places coordinates (36.5953395,-4.6358648); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5953395%2C-4.6358648&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 21 min, 11.38 km. One predicted sample, not the Google Maps app''s main figure.'
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
  official_website: null
  booking: null
  visitor_information: null
  transport: null
  contact: null
related_places:
- id: ES-AND-MAL-MIJAS-PUEBLO-001
  relationship: part_of
  note: Viewpoint and hermitage in Mijas Pueblo.
description_short: 'Mirador del Compás (Virgen de la Peña): viewpoint by the Virgen de la Peña hermitage in Mijas Pueblo, about 21 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: Mirador del Compás, also called Mirador Virgen de la Peña, is a viewpoint beside the Ermita de la Virgen de la Peña on Avenida del Compás in Mijas Pueblo, with wide views over the Costa del Sol. From Casa de la Familia it is about 21 minutes by car (Google route check, Saturday 10:00). The hermitage, built into the rock, holds a carved wooden image of the Virgin said to have been found in 1586; the Santuario de la Virgen de la Peña is one of the village sights named by Andalusia's official tourism site. It is in the village itself, not a mountain hike. Opening of the hermitage and access for wheelchairs and pushchairs were not checked. Check before visiting.
seo_title: Mirador del Compás (Virgen de la Peña), Mijas | CalleMilano draft record
seo_description: 'Draft record for Mirador del Compás (Virgen de la Peña) in Mijas Pueblo: location and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality
  claim: Google Places lists 'Mirador del Compás' at 29650 Mijas, Málaga, España (36.5953395,-4.6358648), business status OPERATIONAL, primary type scenic_spot.
  source_url: https://maps.google.com/?cid=3160074190169528299
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) text search on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 21 min by car (11.38 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.5953395%2C-4.6358648&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (local extension intake 2026-11-02)
  confidence: medium
  notes: Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time over 20 minutes, so not shown (owner rule).
- field: name, coordinates, description_long
  claim: 'Google Places: ''Ermita de la Virgen de la Peña'', Av. del Compás 7, 29650 Mijas (36.5955369,-4.6356259), about 30 m from the ''Mirador del Compás'' point (36.5953395,-4.6358648); ''Santuario de la Virgen de la Peña'', Av. del Compás 8.'
  source_url: https://maps.google.com/?cid=9334915565214010936
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: high
  notes: Places API text search 2026-11-02; shows the viewpoint is in Mijas Pueblo, not on a mountain trail.
- field: name, description_long
  claim: '''El Mirador Virgen de la Peña es también conocido como Mirador del Compás. Se encuentra junto a la Ermita de la Virgen de la Peña. Este mirador deja unas vistas impresionantes de la Costa del Sol.'' Ermita: ''La imagen de la virgen está tallada en madera y fue descubierta en el año 1586.'''
  source_url: https://www.allincarhire.com/es/mijas-mirador.php
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: medium
  notes: Owner screenshot (supplied 2026-11-02) of a car-hire company's travel page; secondary. The two names agree with Google's positions.
- field: description_long
  claim: andalucia.org 'Mijas' names the 'Santuario de la Virgen de la Peña' among the village's places of special interest.
  source_url: https://www.andalucia.org/listing/mijas/19913102/
  source_type: official_tourism
  checked_at: '2026-11-02'
  checked_by: Claude (local extension fact check 2026-11-02)
  confidence: high
  notes: Read 2026-11-02 (batch B).
review_issues:
- code: category_editorial_choice
  severity: info
  fields:
  - category
  description: 'Category ''Excursions'' was chosen by Claude from the schema definitions (routes and sights: Excursions; towns: City; natural areas: Nature; visitor attractions: Family activities). Confirm at editorial review.'
  retryable: true
  owner: human_editor
- code: family_suitability_not_assessed
  severity: warning
  fields:
  - age_groups
  - family_score
  - tags
  description: 'Age groups, family scores and tags not assessed; energy_level Low (corrected 2026-11-02 from High: the viewpoint is in the village, not a hike).'
  retryable: true
  owner: human_editor
- code: possible_merge_with_mijas_pueblo
  severity: info
  fields:
  - status
  - related_places
  description: 'The viewpoint lies inside Mijas Pueblo next to the Virgen de la Peña hermitage. Owner decision: keep as its own record (linked to Mijas Pueblo) or fold it into the Mijas Pueblo record and archive this one.'
  retryable: true
  owner: human_editor
- code: official_detail_missing
  severity: info
  fields:
  - visit_information
  - accessibility
  description: Hermitage opening and access are not from an official source yet (Turismo de Mijas).
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
