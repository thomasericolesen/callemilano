---
schema_version: 1.0.0
status: needs_fact_check
id: ES-AND-CAD-ZAHARA-DE-LA-SIERRA-001
slug: zahara-de-la-sierra
name: Zahara de la Sierra
category: City
tags:
  - Historic town
  - Viewpoint
  - Nature
coordinates:
  latitude: 36.840068
  longitude: -5.388687
  purpose: representative_point
  label: Municipal tourism office, C/ Camino Nazarí
  source: https://www.zaharadelasierra.es/turismo-zahara
  checked_at: 2026-10-03
google_maps_url: https://maps.google.com/?q=Zahara+de+la+Sierra%2C+C%C3%A1diz%2C+Spain
external_ids: {}
municipality: Zahara de la Sierra
province: Cádiz
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 130 min
  origin: Casa de la Familia (Calle Milano 35, 29649 Las Lagunas de Mijas, Málaga, Spain)
  destination: Google Maps village marker (postcode 11688)
  source: Google Maps screenshots supplied by Eric Olesen (owner) on 2026-10-30; departure setting Saturday 2026-07-18 10:00 from Calle Milano 35, 29649 Las Lagunas de Mijas (36.5356, -4.6627); no route URL recorded
  checked_at: '2026-10-30'
  note: 'Google''s main figure: 130 min (typical range shown by Google: 2:00-2:20 h:min), 122 km via A-397. Measured by the owner in Google Maps (screenshots supplied 2026-10-30), one sample, departure setting Saturday 2026-07-18 10:00; traffic and season change the time. Firecrawl route data flags 13.7 km of AP-7 as toll road on the A-397 route. Toll roads were not avoided for this measurement (the owner avoids tolls only for trips under 60 minutes). Destination is Google''s marker: Google Maps village marker (postcode 11688). Origin Calle Milano 35 (36.5356, -4.6627) is treated as the same place as Casa de la Familia because the coordinates agree with the project origin to about 10 m. No route URL recorded. Supersedes the earlier OSRM figure (None). Firecrawl re-check gave 134 km / 2 h 13 min for the same road names (A-397/A-374), 143 km / 2 h 05 min via A-384; Google''s 122 km could not be reproduced.'
age_groups:
  - Small children (0-6)
  - Children (7-12)
  - Young adults
  - Seniors
family_score:
  small_children: low
  children: medium
  young_adults: high
  seniors: low
energy_level: High
seasonality:
  - Spring
  - Autumn
  - Winter
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
booking_required: false
dog_friendly: unknown
toilets_available: unknown
food_available: unknown
cost_level: Unknown
visit_information:
  schedule: 'Tourist office (municipal site): daily 9:30-14:00 and 18:00-21:15. The text mentions no guided tours ''until after summer'', so these are probably summer hours and may be out of date. Torre del Homenaje: no opening hours on the municipal pages.'
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'Not stated on the municipal pages. Third-party sources (not official): EUR 3.50 per adult, free under 4 - unverified.'
  cost_checked_at: 2026-10-30
links:
  official_website: https://www.zaharadelasierra.es/turismo-zahara
  booking: null
  visitor_information: https://www.zaharadelasierra.es/turismo/villa-medieval
  transport: null
  contact: https://www.zaharadelasierra.es/turismo-zahara
related_places: []
description_short: "A hilltop white village in the Sierra de Grazalema with a Nasrid castle and tower, many viewpoints and a reservoir beach nearby; about 2 hours 10 minutes' drive from Casa de la Familia (Google Maps main figure)."
description_long: "Zahara de la Sierra's municipal tourism site highlights its historic heritage, viewpoints, and the Torre del Homenaje at the castle's highest point. The municipal tourism office is used as the representative arrival pin. Reaching elevated viewpoints involves walking uphill; exact route gradients, step-free access, parking, facilities, monument schedules, and summer suitability have not been verified. The town's tourism office notes that guided visits pause during the hottest part of summer, so check current conditions before planning."
seo_title: "Zahara de la Sierra: Historic Village and Castle Views"
seo_description: "Discover Zahara de la Sierra in Cádiz, with a historic center, viewpoints, and its hilltop castle. Check current access and visitor information before travelling."
images: []
evidence:
  - field: coordinates
    claim: The municipal tourism site links its visitor office location to a Google Maps point at these coordinates.
    source_url: https://www.zaharadelasierra.es/turismo-zahara
    source_type: government
    checked_at: 2026-10-03
    checked_by: maps-import-agent
    confidence: high
    notes: Coordinate represents the visitor-office arrival point, not the castle or whole town.
  - field: description_short, description_long, tags
    claim: Municipal tourism information highlights the town's heritage, viewpoints, and Torre del Homenaje at the castle.
    source_url: https://www.zaharadelasierra.es/turismo-zahara
    source_type: government
    checked_at: 2026-10-03
    checked_by: maps-import-agent
    confidence: high
    notes: null
  - field: description_long, seasonality
    claim: The municipal tourism site says guided visits pause during hot summer conditions.
    source_url: https://www.zaharadelasierra.es/turismo-zahara
    source_type: government
    checked_at: 2026-10-03
    checked_by: maps-import-agent
    confidence: high
    notes: Check again before travel; schedule is time-sensitive.
  - field: driving_time_from_casa_de_la_familia
    claim: One-way drive 130 min (122 km via A-397), Google Maps main figure.
    source_url: n/a (owner-supplied Google Maps screenshots, no route URL)
    source_type: secondary
    checked_at: 2026-10-30
    checked_by: claude-code-agent (branch udflugter-verificering-2)
    confidence: medium
    notes: Owner screenshots 2026-10-30; one sample; typical range 2:00-2:20. Firecrawl route data flags 13.7 km of AP-7 as toll road on the A-397 route.
  - field: visit_information
    claim: Tourist office hours (possibly summer hours); no tower hours or prices published.
    source_url: https://www.zaharadelasierra.es/turismo-zahara
    source_type: government
    checked_at: 2026-10-30
    checked_by: claude-code-agent (branch udflugter-verificering-2)
    confidence: medium
    notes: Third-party price of EUR 3.50 (Tripadvisor, adondevoyconmifamilia.es) is not an official source and is not used as a fact.
  - field: body.nearby_suggestions
    claim: Nearby sights and viewpoints named in the 'Nearby suggestions' section.
    source_url: https://www.zaharadelasierra.es/turismo-zahara
    source_type: official_tourism
    checked_at: 2026-10-30
    checked_by: claude-code-agent (branch udflugter-verificering-2)
    confidence: medium
    notes: Names taken from official tourism or heritage pages (all listed in the section); no restaurant or rest-stop venue is claimed.
  - field: body.owner_supplied_suggestions
    claim: 'Editor-supplied additions for Zahara: village lanes, Paseo de los Refranes, La Playita, reservoir activities, Garganta Verde (permit required).'
    source_url: https://mylittleworldoftravelling.com/things-to-do-in-zahara-de-la-sierra/
    source_type: secondary
    checked_at: 2026-10-30
    checked_by: claude-code-agent (branch udflugter-verificering-2)
    confidence: low
    notes: Supplied by the owner/editor on 2026-10-30 (Eric Olesen (owner), message 2026-10-30; text partly from a Google AI summary and third-party travel sites); not verified against an official source unless an official URL is given in the section.
review_issues:
  - code: family_ratings_estimated
    severity: warning
    fields:
      - age_groups
      - family_score
      - energy_level
      - seasonality
    description: Audience ratings, energy, and suitable seasons are provisional editorial estimates; confirm hill access, heat exposure, and route demands.
    retryable: true
    owner: editorial
  - code: visitor_facilities_unverified
    severity: warning
    fields:
      - accessibility
      - wheelchair_friendly
      - parking
      - dog_friendly
      - toilets_available
      - food_available
      - cost_level
    description: Access, parking, facilities, dog policy, and costs remain unverified.
    retryable: true
    owner: fact_check
  - code: tower_hours_prices_unverified
    severity: blocking
    fields:
      - visit_information
    description: No official opening hours or price for the Torre del Homenaje; call the tourist office on 623 47 59 06.
    retryable: true
    owner: fact_check
  - code: owner_supplied_additions_unverified
    severity: info
    fields:
      - body.nearby_suggestions
    description: Editor-supplied additions (La Playita, Garganta Verde permit, Paseo de los Refranes, Puerta Árabe, reservoir activities) come from third-party travel sites and an AI summary; no official source yet.
    retryable: true
    owner: editorial
created_at: 2026-10-03
updated_at: 2026-10-30
last_verified: 2026-10-30
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
---

Draft source notes: Zahara de la Sierra municipal tourism pages checked on 2026-10-03. The municipality's map link was used for the visitor-office representative pin. No user-provided saved-place URL was supplied; the Maps search link is a place lookup, not a saved-list link.

## Nearby suggestions (draft, 2026-10-30)

Inspiration only; check current hours and availability before travelling.

**In the village (municipal tourism site)**
- Torre del Homenaje (highest point of the castle, 605 m) and the Torre del Reloj
- Iglesia de Santa María de la Mesa; Antigua Iglesia Mayor tower; Centro de interpretación de la Villa Medieval; Museo parroquial; Centro de interpretación del Pinsapo
- Viewpoints: Tres Provincias, Plaza Arco de la Villa (reservoir views), Arco de la Villa, Alameda Jardín de los Pinsapos, Plaza del Rey, Mirador de las Peñas, Mirador Boquete, Alameda de Lepanto, El Altillo, Alameda de D. Rodrigo Ponce de León, Peñón de la Horca

**Added by the editor (not verified against an official source)**
- The climb to the castle is on a steep path; the tower has a small visitor centre and wide views over the landscape and the reservoir.
- Old town lanes (Calle Fuerte, Calle Rueda) and the old Arab gate (Puerta Árabe); Paseo de los Refranes, a route with tiles showing Spanish proverbs.
- Plaza de Lepanto: good for sunset. Soaring vultures or eagles are often seen from the viewpoints.
- La Playita de Zahara: an artificial but popular freshwater beach on the reservoir shore, for a dip in summer.
- Embalse de Zahara-El Gastor: kayaking, paddleboarding and scenic drives along the shore.
- Garganta Verde: dramatic gorge walk of about 5 km nearby; a separate permit is required.

**Easy to combine with**
- Olvera and Setenil de las Bodegas (neighbouring white villages, separate records).

**Food, rest stops and viewpoints on the road**
- The municipal site has a restaurants page: https://www.zaharadelasierra.es/turismo/restaurantes (individual venues not verified here).

Sources: https://www.zaharadelasierra.es/turismo-zahara; editor-supplied text (see evidence ledger)
