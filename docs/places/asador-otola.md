---
schema_version: 1.0.0
status: approved
id: ES-AND-MAL-ASADOR-OTOLA-001
slug: asador-otola
name: Asador Otola
category: Restaurants
tags:
- Restaurant
- Rainy day
- Half day
- Premium
coordinates:
  latitude: 36.540219199999996
  longitude: -4.6490593
  purpose: venue
  label: Asador Otola, Camino Viejo de Coín, 4, 29651 Las Lagunas de Mijas, Málaga (Google Places listing)
  source: Google Places API (New), place ChIJm-I9tvThcg0RdvVIsw6anIk, read 2026-11-02
  checked_at: '2026-11-02'
google_maps_url: https://maps.google.com/?cid=9915969867491112310
external_ids:
  google_place_id: ChIJm-I9tvThcg0RdvVIsw6anIk
municipality: Mijas
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: 6 min
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: Asador Otola, Camino Viejo de Coín, 4, 29651 Las Lagunas de Mijas, Málaga
  source: Google Routes API computeRoutes, run 2026-11-02 from the project origin (36.5356875, -4.6626875) to the Google Places coordinates (36.540219199999996,-4.6490593); departure Saturday 2026-11-07 10:00 Europe/Madrid, predicted traffic (TRAFFIC_AWARE_OPTIMAL); tolls not avoided - https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.540219199999996%2C-4.6490593&travelmode=driving
  checked_at: '2026-11-02'
  note: 'Routes API figure: 6 min, 2.24 km. One predicted sample, not the Google Maps app''s main figure.'
age_groups:
- Children (7-12)
- Young adults
- Seniors
family_score:
  small_children: low
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
  schedule: Mon 12:00-24:00; Tue 12:00-18:00; Wed closed; Thu-Sun 12:00-24:00 (own website, read 2026-11-02).
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: 'No prices on own site; Tripadvisor price marking "€€ - €€€" read as the middle band. Fallback source per docs/trip-planner-agents.md. Band rule: median main on the menu + one drink; € <20, €€ 20-50, €€€ >50 (owner decision 2026-11-03).N'
  cost_checked_at: '2026-11-02'
links:
  official_website: https://www.asadorotola.com/es
  booking: null
  visitor_information: null
  transport: null
  contact: tel:+34604241785
related_places: []
description_short: 'Asador Otola: Basque grill (asador) at Cortijo la Herradura, about 6 min by car from Casa de la Familia. Draft; partly fact-checked.'
description_long: 'Asador Otola is a Basque grill (asador) at Cortijo la Herradura at Camino Viejo de Coín, 4, 29651 Las Lagunas de Mijas, Málaga. From Casa de la Familia it is about 6 minutes by car (Google route check, Saturday 10:00). Owner''s own knowledge: Already among the owner''s recommendations, with a caveat: the meat has a much more intense flavour. Its own website describes Basque cooking with aged meats grilled over embers (more than 18 years in business), lists dishes such as beef and lamb, txuleton and grilled octopus, and gives opening hours of Monday 12:00-24:00, Tuesday 12:00-18:00, Wednesday closed, Thursday to Sunday 12:00-24:00 (phone 604 241 785). Prices, booking, children''s facilities and accessibility are not stated; check before visiting. Owner''s recommendation (callemilano.dk): A good steak restaurant; be careful with very long-aged meat such as Galician beef, which the owner finds tastes mostly of umami rather than meat - a small portion as a flavour enhancer is fine.'
seo_title: Asador Otola, Mijas | CalleMilano draft record
seo_description: 'Draft record for Asador Otola (Mijas): location and walking and driving time from Casa de la Familia.'
images: []
evidence:
- field: name, coordinates, google_maps_url, external_ids, municipality, food_available
  claim: Google Places lists 'Asador Otola - Cortijo la Herradura' at Camino Viejo de Coín, 4, 29651 Las Lagunas de Mijas, Málaga, España (36.540219199999996,-4.6490593), business status OPERATIONAL, website http://www.asadorotola.com/.
  source_url: https://maps.google.com/?cid=9915969867491112310
  source_type: maps_identity
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: Google Places API (New) on 2026-11-02. Maps establishes identity and position only, not hours, prices, facilities or suitability.
- field: driving_time_from_casa_de_la_familia
  claim: 'From Casa de la Familia: 6 min by car (2.24 km, Saturday 10:00 predicted traffic).'
  source_url: https://www.google.com/maps/dir/?api=1&origin=36.5356875%2C-4.6626875&destination=36.540219199999996%2C-4.6490593&travelmode=driving
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Claude (nearby intake 2026-11-02)
  confidence: medium
  notes: 'Google Routes API computeRoutes from the project origin to the Google Places coordinates; DRIVE with TRAFFIC_AWARE_OPTIMAL for Saturday 2026-11-07 10:00. Walking time removed 2026-11-02 (owner decision: walking times of 20 minutes or more are not shown).'
- field: description_long (owner knowledge)
  claim: 'Already among the owner''s recommendations, with a caveat: the meat has a much more intense flavour.'
  source_url: https://github.com/thomasericolesen/callemilano/blob/main/docs/decisions/nearby-selection-2026-11-02.md
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: medium
  notes: Owner's own local knowledge, given on the nearby selection page on 2026-11-02; not independently verified.
- field: visit_information, links, description_long
  claim: 'Own website: Basque asador specialising in aged meats on the grill, 18+ years; address Camino Viejo de Coín km 1.4, Mijas; hours Mon 12-24, Tue 12-18, Wed closed, Thu-Sun 12-24; phone +34 604 241 785.'
  source_url: https://www.asadorotola.com/es
  source_type: official_venue
  checked_at: '2026-11-02'
  checked_by: Claude (nearby fact check 2026-11-02)
  confidence: high
  notes: Homepage read via Firecrawl (structured extraction) on 2026-11-02; hours and phone are page text. The site gives km 1.4 while Google gives km 4; same venue name and Cortijo la Herradura.
- field: cost_level
  claim: '"€€ - €€€"'
  source_url: https://www.tripadvisor.es/Restaurant_Review-g11868685-d26732269-Reviews-Asador_Otola-Las_Lagunas_de_Mijas_Costa_del_Sol_Province_of_Malaga_Andalucia.html
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: source-reader agent; band set by orchestrator
  confidence: low
  notes: Tripadvisor price marking only (search excerpt); no ratings or reviews recorded. Own-site prices preferred when available. Quote from search snippet of the tripadvisor.es listing. The tripadvisor.com listing (d26732269, or30) shows '$$ - $$$' under PRICE. Name and town match (Las Lagunas de Mijas).
- field: description_long (owner knowledge)
  claim: God bøfrestaurant - men man bør være forsigtig med at vælge f.eks. galisisk, extremt modnet kød. Det har mistet “kødsmagen” og smager mest af “Umami “. En lille portion som smagsforstærker er fint
  source_url: https://callemilano.dk/
  source_type: secondary
  checked_at: '2026-11-02'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-02
  confidence: medium
  notes: 'Owner''s own recommendation (kind ''anbefaling'') on callemilano.dk, read from the Lovable app database 2026-11-02; site tags: -. Personal experience, not independently verified.'
- field: age_groups, family_score, energy_level
  claim: 'Owner''s assessment on the CalleMilano checklist: family_score small_children low, children medium, young_adults high, seniors high; energy_level Low.'
  source_url: https://claude.ai/artifact/Ju9yKgH8Vad7gQNWANxwK1
  source_type: secondary
  checked_at: '2026-11-10'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-10
  confidence: medium
  notes: Owner's own knowledge, given on the callemilano-tjekliste (familievurderinger) on 2026-11-10; not independently verified. age_groups lists the groups rated high or medium. source_type secondary is the nearest schema value.
- field: tags
  claim: "Owner's tag selection on the CalleMilano tag checklist: Restaurant, Rainy day, Half day, Premium."
  source_url: https://claude.ai/artifact/DZv9cLLQ1BEcYs3NeewdEF
  source_type: secondary
  checked_at: '2026-11-11'
  checked_by: Eric Olesen (editor-of-record); recorded by Claude 2026-11-11
  confidence: medium
  notes: Owner's own judgment on the tag checklist on 2026-11-11 (previous tags were estimates from import); not independently verified. source_type secondary is the nearest schema value.
review_issues: []
created_at: '2026-11-02'
updated_at: '2026-11-11'
last_verified: '2026-11-02'
last_reviewed_at: '2026-11-11'
next_review_at: '2027-04-11'
review_decision:
  decision: approved
  reviewer: Eric Olesen (editor-of-record)
  date: '2026-11-11'
  notes: "Approved by the owner on 2026-11-11 after his own review of the place on the family-rating checklist (2026-11-10) and the tag checklist (2026-11-11), on top of the agent fact-check. Practical details that are still unknown stay shown as 'check before visiting'."
redirects: []
---
