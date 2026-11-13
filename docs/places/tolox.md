---
schema_version: 1.0.0
status: needs_editorial_review
id: ES-AND-MAL-TOLOX-001
slug: tolox
name: Tolox
category: Excursions
tags:
- Historic town
- Nature
- Half day
coordinates:
  latitude: 36.6850627
  longitude: -4.9114074
  purpose: venue
  label: Balneario de Tolox (Fuente Amargosa), access road area
  source: https://www.openstreetmap.org/way/56157662
  checked_at: 2026-10-15
google_maps_url: https://maps.google.com/?q=Tolox%2C+M%C3%A1laga%2C+Spain
external_ids: {}
municipality: Tolox
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 56 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Balneario de Tolox (Fuente Amargosa), Tolox, Málaga, Spain
  source: Google Routes API computeRoutes, run 2026-11-01 from the project origin (36.5356875, -4.6626875); destination = record coordinates (36.6850627,-4.9114074); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6850627%2C-4.9114074&travelmode=driving
  checked_at: '2026-11-01'
  note: 'Routes API figure: 56 min with predicted Saturday 10:00 traffic (54 min without traffic), 45.0 km via A-7053 y A-366; an avoid-tolls run gave 56 min. One predicted sample, not the Google Maps app''s main figure; traffic and season change the time. Previous value 56 min (2026-10-15): OSRM route check, no traffic, about 43.7 km. Batch: data/route-checks-2026-11-01-local.csv.'
age_groups:
- Small children (0-6)
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: low
  children: low
  young_adults: high
  seniors: high
energy_level: Low
seasonality:
- Summer
- Autumn
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
  schedule: Season 1 June - 16 October (spa's own site, re-read 2026-10-29). Closed for the season as of 29 October 2026. Dates for 2027 not published on the page.
  typical_duration: null
  booking_lead_time: null
  valid_from: '2026-06-01'
  valid_until: '2026-10-16'
  cost_basis: null
  cost_checked_at: null
links:
  official_website: https://www.balneariodetolox.es/
  booking: null
  visitor_information: https://andalucia.org/en/tolox-health-and-beauty-balneario-de-tolox-2
  transport: null
  contact: tel:+34952487091
related_places: []
description_short: Tolox is a small white-village spa town in Málaga province; its historic Balneario de Tolox (Fuente Amargosa) thermal spa is real and documented, but only operates seasonally (1 June–16 October), not year-round.
description_long: 'Tolox sits at the foot of the Sierra de las Nieves, about 56 minutes'' drive from Casa de la Familia (OSRM route check; not yet re-measured in Google Maps). The town''s wellness draw is the Balneario de Tolox, also known as Fuente Amargosa: a thermal spa whose hypothermal, naturally gas-bearing waters were discovered in 1867 and have been used since 1869 for respiratory-condition treatments taken by inhalation; the current building dates to 1930, rebuilt after a major 1906 flood destroyed the original. Its own website states it is open only from 1 June to 16 October each year, not year-round — this directly resolves the open editorial question about Tolox''s wellness offering, but also means any visit must be timed to that window; the spa was closed for the winter when re-checked on 29 October 2026, and the 2027 dates are not yet published. Owner decision 2026-10-29: Tolox is kept and marked as a seasonal place (June-October). Daily hours, current treatment prices, whether day visitors (not staying at the spa) can use the facilities, and the historic town centre''s own sights have not yet been confirmed from an official source.'
seo_title: 'Tolox, Málaga: Seasonal Thermal Spa and Village'
seo_description: Tolox's Balneario de Tolox thermal spa is seasonal (June-October), not year-round. Plan around the season and the drive from Casa de la Familia.
images: []
evidence:
- field: coordinates
  claim: Balneario de Tolox (Fuente Amargosa) sits on the Carretera del Balneario, the access road into the spa from Tolox village.
  source_url: https://www.openstreetmap.org/way/56157662
  source_type: maps_identity
  checked_at: 2026-10-15
  checked_by: fact-check-agent
  confidence: medium
  notes: This is the access road, not a confirmed point for the spa building itself; the spa's exact street address is reported inconsistently across secondary sources (Calle Extramuros s/n vs Calle Balneario s/n) and should be confirmed directly with the venue.
- field: visit_information.schedule, visit_information.valid_from, visit_information.valid_until, description_long, category
  claim: The Balneario de Tolox (Fuente Amargosa) is a real, operating thermal spa, open seasonally from 1 June to 16 October, specializing in inhalation treatments for respiratory conditions.
  source_url: https://www.balneariodetolox.es/
  source_type: official_venue
  checked_at: 2026-10-15
  checked_by: fact-check-agent
  confidence: high
  notes: Directly fetched from the spa's own site; resolves the open 'category_open' review issue about whether Tolox actually has a wellness offering.
- field: description_long
  claim: 'History of the spa: waters discovered 1867, spa opened 1869, rebuilt 1930 after a 1906 flood; waters are hypothermal and gas-bearing, taken by inhalation.'
  source_url: https://andalucia.org/en/tolox-health-and-beauty-balneario-de-tolox-2
  source_type: official_tourism
  checked_at: 2026-10-15
  checked_by: fact-check-agent
  confidence: medium
  notes: Corroborated by secondary local-tourism sources; dates and flood year not independently cross-verified against a government archive.
- field: driving_time_from_casa_de_la_familia
  claim: One-way driving route from Casa de la Familia to the Balneario de Tolox area is approximately 56 minutes (43.7 km).
  source_url: https://router.project-osrm.org/route/v1/driving/-4.6626875,36.5356875;-4.9114074,36.6850627?overview=false
  source_type: secondary
  checked_at: 2026-10-15
  checked_by: fact-check-agent
  confidence: medium
  notes: OSRM public routing engine, driving profile; traffic not modelled.
- field: visit_information.schedule
  claim: The Balneario de Tolox states 'Abierto del 1 de junio al 16 de octubre'; on 2026-10-29 it is therefore closed for the season. No 2027 dates are published.
  source_url: https://www.balneariodetolox.es/
  source_type: official_venue
  checked_at: 2026-10-29
  checked_by: fact-check-agent
  confidence: high
  notes: Home page of the spa, re-read 2026-10-29 (page modified 2026-07-09). The Google AI summary seen by the owner on 2026-10-29 says the same; it is not used as a source.
- field: driving_time_from_casa_de_la_familia
  claim: 'One-way drive from Casa de la Familia to Balneario de Tolox (Fuente Amargosa), Tolox, Málaga, Spain: 56 min, 45.0 km (Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.6850627%2C-4.9114074&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-01'
  checked_by: Claude (Routes API batch 2026-11-01)
  confidence: medium
  notes: Google Routes API computeRoutes; destination = record coordinates (36.6850627,-4.9114074). Predicted-traffic estimate for one departure time; the local_30km rule uses the Google Maps app's main figure.
- field: visit_information.schedule
  claim: '"Abierto del 1 de junio al 16 de octubre" / "Llamanos al 952487091 o escríbenos por WhatsApp pinchando en el icono"'
  source_url: https://www.balneariodetolox.es/
  source_type: official_venue
  checked_at: '2026-11-13'
  checked_by: record-writer agent
  confidence: high
  notes: Spa's own site as fetched 2026-11-13 (page's own date stamp 2026-07-09). This is only the season the page states; no 2027 dates, daily hours, treatment prices, day-visitor access, parking or accessibility on the page. season_2027_dates_unconfirmed stays open. Phone matches links.contact.
review_issues:
- code: season_2027_dates_unconfirmed
  severity: warning
  fields:
  - visit_information.schedule
  description: 'The spa''s site (re-read 2026-10-29) still says 1 June - 16 October; the spa is closed for the winter. 2027 dates are not published. Confirm with the spa before recommending a visit next season.  Owner decision 2026-10-29: Tolox stays and is marked seasonal (June-October); seasonality is Summer and Autumn.'
  retryable: true
  owner: editor
- code: category_open
  severity: warning
  fields:
  - category
  - tags
  description: 'Resolved by this fact-check: Tolox''s wellness offering is a real, named thermal spa (Balneario de Tolox / Fuente Amargosa) per its own official site, but it is seasonal (June-October), not year-round. Editor to confirm category/tags reflect the seasonal nature.'
  retryable: false
  owner: editorial
- code: visitor_facilities_unverified
  severity: warning
  fields:
  - accessibility
  - wheelchair_friendly
  - parking
  - dog_friendly
  - toilets_available
  - cost_level
  - booking_required
  description: Daily hours, current treatment prices, day-visitor access, parking and accessibility remain unverified.
  retryable: true
  owner: fact_check
created_at: 2026-10-15
updated_at: '2026-11-13'
last_verified: 2026-10-29
last_reviewed_at: 2026-10-15
next_review_at: 2027-04-01
review_decision: null
redirects: []
---

Fact-checked 2026-10-15: confirmed the Balneario de Tolox is real but seasonal (1 Jun-16 Oct), resolving the open category question; exact address, daily hours, prices and current same-week opening status remain unverified and are flagged, not guessed. Draft source notes (import): Created from the Danish excursion catalogue of 2026-10-15 (an inspiration document, not a source). The Maps link is a place lookup, not a saved-list link.
