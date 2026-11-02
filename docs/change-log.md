# Change log

## 2026-11-02 - Owner-approved family assessments written; eight records to editorial review (no schema change)

- The owner corrected and approved the family assessment for 18 of 20 records (`docs/family-assessment-decisions-2026-11-02.md`). `age_groups` and `family_score` were written into those records, with an evidence entry each. `subjective_assessments_need_human_review` / `family_suitability_not_assessed` were closed and replaced by the info-level issue `energy_level_editorial_estimate` (energy, and for beaches the character label, still to be confirmed at editorial review). Not approved and unchanged: Chiringuito Rafael and Fuente de la Salud.
- Owner knowledge added to descriptions with evidence entries: Cabopino-Artola (very fine sand, not deep quickly, nudism only on a smaller part, small harbour with restaurants), Castillo-Ejido (Marenostrum concert venue is part of the area), La Butibamba (towards La Cala centre more child-friendly, with parasols and sunbeds), Carvajal (mixed sand, gravel and stones).
- Status `needs_fact_check` -> `needs_editorial_review` for the eight records left with only info-level issues: Castillo-Ejido, La Butibamba, Los Marinos Paco, Chiringuito Cristóbal, Chiringuito Los Moreno, La Mar Salá, Morrofino and Santa Ana Denis. Not approved; the editor-of-record decides.
- Validation: 68 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Family assessment proposal for beaches and restaurants (proposal only)

Added `docs/family-assessment-proposal-2026-11-02.md`: proposed `age_groups` and `family_score` for the 12 local beaches and 8 restaurants (owner decisions 2 and 6), with the rubric and the sourced facts behind each value. No record was changed; the values wait for the owner's corrections. Progress note added to `docs/approval-decisions-2026-11-01.md`.

## 2026-11-02 - Beaches: Google Maps links, official beach data, unsourced claims removed (draft, no schema change)

Next-session step 3 from `docs/approval-decisions-2026-11-01.md`, for the 12 active local beaches.

- Google Maps links: `google_maps_url` and `external_ids.google_place_id` from Google Places API (New), with a `maps_identity` evidence entry; `google_maps_url_missing` closed. Boliches-Gaviotas uses the Playa de las Gaviotas listing (the record point is on it); Castillo-Ejido uses Playa del Ejido (about 180 m from the point, which is at the Castillo Sohail).
- New warning `coordinates_far_from_named_beach` on Fuengirola centro: the accepted point lies about 2.5 km north-east of Google's "Playa de Fuengirola" (by the centre and port) and north of the Boliches-Gaviotas point. Coordinates not changed; owner to check.
- Sand, size, waves, occupancy and listed services now come from spain.info (Turespaña official tourism portal, data from the national beach guide, undated). For Fuente de la Salud the source is andalucia.org (Junta de Andalucía), which also gives adapted toilets (`toilets_available: yes`). All evidence entries without a source URL were removed together with their claims in `description_long`: snapshot child-friendliness statements ("often recommended for children", "family-oriented", gentle slope), the anecdotal Facebook replies, unnamed or unverified beach bars, and unsourced "nearby" items. Beach descriptions now name only verified restaurant records ("see the linked record").
- Notable differences from the old snapshot: Carvajal is listed as dark sand with gravel and cobbles (*bolos*), not "fine golden sand" (noted on `rocks_not_verified`); Castillo is white sand with a fenced dog-beach section; La Butibamba is listed as dark sand, while the owner's own knowledge (stones) is kept and the difference stated.
- Closed: `secondary_sources_unverified`, `source_urls_missing`, `snapshot_restaurant_misidentified` (Castillo-Ejido), `snapshot_restaurants_wrong_beach` (La Carihuela), `lively_atmosphere_not_rated` (Los Álamos; the claim had no source). `description_short`/`seo_description` no longer call the record a snapshot draft.
- Validation: 68 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Owner decisions 1, 3, 4, 5, 7 and 8 applied to beaches and restaurants (draft, no schema change)

Applied the owner answers of 2026-11-01 (`docs/approval-decisions-2026-11-01.md`) to the 12 active local beaches and 8 restaurants. Each record gets one evidence entry per decision, pointing to the decisions file (`source_type: secondary`, the nearest schema value, with a note that it is an editor decision, not an external source). Status values are unchanged.

- Decision 1 (all 12 beaches): owner-read Google marker accepted as the place point; `coordinates.source` and the drive-time note updated; `route_and_coordinates_owner_measured` closed.
- Decision 3 (all 12 beaches): `seasonality` = `Spring`, `Summer`, `Autumn`; `seasonality_unknown` closed.
- Decision 4: no rocks for Boliches-Gaviotas, Cabopino-Artola, Castillo-Ejido, Fuengirola centro and La Butibamba (`rocks_not_verified` closed; description updated). La Butibamba: owner clarified on 2026-11-02 that it is a stone beach (walnut- to plum-sized stones), not a rocky one; `rock_claim_source_conflict` closed. For Carvajal, El Bajondillo, Fuente de la Salud, La Carihuela, Los Álamos, Playamar and Santa Ana the owner does not know, so `rocks_not_verified` stays open with that noted. The old unsourced "rocks not mentioned" evidence entries were removed in all 12 beaches.
- Decision 5 (all 12 beaches): practical details deliberately unknown; `practical_details_out_of_scope` closed and the decision kept as an evidence entry.
- Decision 7 (8 restaurants): prices and season stay unknown with a "check before visiting" sentence in `description_long`; `season_and_prices_unverified` closed. Chiringuito Las Dunas keeps `winter_opening_unclear`.
- Decision 8 (8 restaurants): practical details deliberately unknown; `practical_details_unverified` closed. Los Marinos Paco keeps its venue-confirmed `dog_friendly: partial` and `booking_required: false`.
- Validation: 68 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-01 - Owner approval decisions recorded (not yet applied)

The owner answered eight shared approval questions for the local beaches and restaurants (coordinates, family assessment, seasonality, rocks per beach, out-of-scope practical details, restaurant prices and season). Answers and the next-session plan are in `docs/approval-decisions-2026-11-01.md`. No record was changed in this entry.

## 2026-11-01 - Six legacy import drafts: provisional energy level and archive decision

Owner request: clear the six long-standing validation errors (`energy_level` None) in `cares`, `conil-de-la-frontera`, `cueva-de-los-arcos`, `miradouro-da-serpente-do-medal`, `roca-foradada` and `salt-de-la-coromina`. Owner decision the same day: give them provisional energy values and archive them.

- `energy_level` set as a provisional editorial estimate from the place type: Cares `High`, Conil de la Frontera `Low`, Miradouro da Serpente do Medal `Low`, Cueva de los Arcos, Roca Foradada and Salt de la Coromina `Medium`. Each record has a `energy_level_provisional` warning.
- Archive: all six are outside `local_30km` and in no excursion layer (archive under AGENTS.md); Miradouro da Serpente do Medal is in Portugal, out of scope since 2026-10-16. Their status stays `draft` because the validator requires an allocated ID outside `draft`, and allocation needs the unresolved identity (province/region) first; guessing it would break the stable-ID rule. Each record carries an `archive_out_of_scope` note with the owner decision. No schema or validator change.
- `python3 tools/places.py validate` now reports 0 errors (68 records). Regenerated `data/place-catalog.csv`.

## 2026-11-01 - Los Monteros archived (owner decision)

Owner decision: remove Los Monteros (Adelfas), Marbella, from the guide. The editor's reasoning is that the area is best known for Nikki Beach, an adult venue for young, affluent visitors, which does not fit the family audience (editorial judgment, not a fact-checked claim).

- `docs/places/los-monteros.md`: status `draft` -> `archived`, with `review_decision` recording the decision. The record is kept as archive, not deleted; ID `ES-AND-MAL-LOS-MONTEROS-001` stays allocated in `data/place-id-registry.csv` and must not be reused.
- No other record linked to it. Historical mentions in `data/route-checks-2026-11-01-local.csv`, `docs/beach-draft-open-points.md` and earlier change-log entries are left as they were. Regenerated `data/place-catalog.csv`.

## 2026-11-01 - Restaurant pilot, round 2: Fuengirola and Benalmádena (draft, no schema change)

Owner request: extend the restaurant pilot. Same method as round 1 (own record per restaurant, `related_places` both ways, Places API for identity only, Routes API Saturday 10:00 for drive time).

- New records (category `Restaurants`, status `needs_fact_check`, IDs allocated): `los-marinos-paco` (Carvajal, Fuengirola, 17 min; own website gives hours, children's menu, high chairs, dogs on the terrace, phone-only booking), `la-mar-sala` (Los Boliches, Fuengirola, 17 min; own website: daily 12:00-00:00, serviced sunbed area), `santa-ana-denis` (Playa de Santa Ana, Benalmádena, 27 min; own website), `chiringuito-rafael` (Playa de la Salud, Benalmádena, 28 min; only its own Facebook page and Google Places, flagged `weak_identity_source`).
- Beaches now linking to restaurants: Carvajal, Boliches-Gaviotas, Santa Ana and Fuente de la Salud (plus La Butibamba, Playamar, Los Álamos and Cabopino-Artola from round 1).
- `los-marinos-paco` sets `dog_friendly: partial` and `booking_required: false` from the venue's own FAQ. Family suitability, prices and accessibility remain open review issues for all four.
- Validation unchanged (same 6 pre-existing errors).

## 2026-11-01 - Restaurant pilot: four restaurant records linked to local beaches (draft, no schema change)

Owner request: a pilot of 5-6 restaurants, each with its own record and linked from the nearby beach (owner agreed the same day that restaurant facts live only in the restaurant record and beaches point to it through `related_places`).

- New records (category `Restaurants`, status `needs_fact_check`, IDs allocated in `data/place-id-registry.csv`): `chiringuito-cristobal` and `chiringuito-los-moreno` (La Butibamba, Mijas; identity from Turismo de Mijas), `morrofino` (Playamar, Torremolinos; own website with hours 12:00-24:00, closed Tuesday), `chiringuito-las-dunas-cabopino` (Cabopino, Marbella; own social pages, winter opening unclear).
- Coordinates and Place IDs from Google Places API (identity only); driving times from Google Routes API (Saturday 10:00 predicted traffic): 15, 15, 29 and 22 min, all inside `local_30km`.
- `related_places` (`nearby`) added both ways: La Butibamba, Playamar, Los Álamos and Cabopino-Artola now point to their restaurants. This is the first use of `related_places` in the catalogue.
- Snapshot errors found and corrected in beach descriptions: Castillo-Ejido's "Marenostrum (beach bar)" is the Marenostrum Fuengirola concert venue; Morrofino and Arrozante are not on La Carihuela (Morrofino is at Playamar, Arrozante inside the Occidental Torremolinos Playa hotel). Review issues added. Arrozante and Marenostrum were dropped from the pilot.
- Family suitability, prices, season, accessibility and practical details are not researched for the restaurants (review issues); `energy_level: Low` is an editorial default. Validation unchanged (same 6 pre-existing errors).

## 2026-11-01 - Local beaches: facilities fact-checked against municipal sources (draft, no schema change)

Owner request: fact-check the 13 local beaches. Owner decision the same day: keep `practical_details_out_of_scope` (parking, transport, dogs, cost, booking and food stay unknown on purpose); check only the description's claims about toilets, accessibility, lifeguards/season and play areas.

- Sources read 2026-11-01: Fuengirola Carta de Servicios 2026 (edition 2026-05-12, per-beach maps); Turismo de Torremolinos "Playas Accesibles" (updated 2026-05-11); Benalmádena Delegación de Playas news 2026-06-05; Mijas press release 2026-06-03 (plus La Opinión de Málaga the same day); Marbella news 2026-04-20 (plus Diario Sur 2026-03-31 and a marbella24horas excerpt).
- `toilets_available` set to `yes` with evidence for Castillo-Ejido, Fuengirola centrum, Carvajal, Boliches-Gaviotas, El Bajondillo, La Carihuela, Los Álamos and Playamar; `accessibility` filled from these sources for those beaches and for Fuente de la Salud, La Butibamba (no assisted-bathing point in 2026) and Cabopino-Artola. `wheelchair_friendly` stays `unknown` (route surfaces not specified; accessibility ratings need human review).
- Lifeguard seasons added to the descriptions as dated municipal facts. Issues resolved: `toilets_listed_but_unverified` (Castillo-Ejido, Fuengirola centrum), `play_area_not_tied_to_beach_in_charter` (Boliches-Gaviotas). New warning `santa_ana_not_named_in_2026_service` (Santa Ana is not named in Benalmádena's 2026 lifeguard or accessibility lists).
- Status `draft` -> `needs_fact_check` for 12 beaches: fact check is under way but rocks, sand/depth, beach-bar names and child-friendliness still rest on secondary sources or the owner's own observation. Los Monteros stays `draft`: no beach-specific municipal source was found.
- Not changed: categories, tags, family scores, energy, seasonality (left for the editor), coordinates, out-of-scope practical fields, schema. Regenerated `data/place-catalog.csv`; validation unchanged (same 6 pre-existing errors in other records).

## 2026-11-01 - Local area: Routes API driving times written into the records (draft, no schema change)

Owner decisions the same day, following the analytical route check below: (1) La Carihuela stays in the local area although the Routes API gave 31 min; (2) the Routes API figures are written into the records.

- Records edited (20): `boliches-gaviotas`, `cabopino-artola`, `carvajal`, `castillo-ejido`, `el-bajondillo`, `fuengirola-centro`, `fuente-de-la-salud`, `la-butibamba`, `la-carihuela`, `los-alamos`, `los-monteros`, `playamar`, `santa-ana-benalmadena`, `malaga`, `marbella-old-town`, `mercado-de-atarazanas`, `palmeral-de-las-sorpresas`, `playa-la-malagueta`, `selwo-aventura`, `tolox`.
- `driving_time_from_casa_de_la_familia` now holds the Routes API figure (Saturday 2026-11-07 10:00, predicted traffic, tolls not avoided) with source, route URL, check date 2026-11-01 and the previous value in the note; one evidence-ledger entry per record. Origin text set to the canonical Casa de la Familia address; the route was computed from the project origin coordinates.
- Beaches: the `route_and_coordinates_owner_measured` warning stays (coordinates are still the owner-read Google marker) with its description updated. `selwo-aventura`: blocking issue `driving_time_unverified` resolved and removed (route source and check date now recorded).
- Not changed: status values, coordinates, `data/layer-membership.csv`, schema. Regenerated `data/place-catalog.csv`; `python3 tools/places.py validate` reports the same 6 pre-existing errors (`energy_level` None in other records) as before the change.

## 2026-11-01 - Local area: driving times re-checked with Google Routes API (analytical, no record change)

Owner request: check the driving times in the local area now that the Google API key works.

- Added `data/route-checks-2026-11-01-local.csv`: 20 records whose recorded driving time is 60 min or less, checked with Google Routes API `computeRoutes` from the project origin (36.5356875, -4.6626875) to the record coordinates (address text for the three records without coordinates), departure Saturday 2026-11-07 10:00 Europe/Madrid with predicted traffic, tolls not avoided; an avoid-tolls run gave the same figures for all 20.
- 12 of the 13 local beaches confirmed within 30 min (differences from the owner's 2026-07-18 Google Maps readings are -2 to +1 min). La Carihuela came out at 31 min (recorded 30) and Fuente de la Salud at 30: both borderline for `local_30km`. The seven records above 30 min stayed above 30 min (Marbella old town 35, Mercado de Atarazanas 37, Palmeral de las Sorpresas 37, Playa la Malagueta 40, Málaga 45, Selwo Aventura 46, Tolox 56).
- Values are not written into the records and no layer membership was changed; the Routes API figure is a predicted-traffic estimate and not identical to the Google Maps main figure that decides `local_30km`. Editor decision open: whether to record these as route evidence and how to treat La Carihuela.

## 2026-10-30 - Excursion records: Google driving times, hours/prices and nearby suggestions (draft, additive, no schema change)

Owner request: fact-check the Google Maps driving times for the excursion destinations and add opening hours, prices, official links and nearby suggestions. Branch `udflugter-verificering-2`; **draft, not pushed, not editor-approved, status values unchanged.**

- Records edited (14): `ronda`, `granada`, `gibraltar`, `cordoba`, `sevilla`, `cadiz`, `frigiliana`, `nerja`, `olvera-castle`, `zahara-de-la-sierra`, `vejer-de-la-frontera`, `tarifa`, `jerez-de-la-frontera`, `setenil-de-las-bodegas`.
- Driving times replaced by Google Maps main figures from the owner's screenshots (supplied 2026-10-30, departure setting Saturday 2026-07-18 10:00, Calle Milano 35, one sample): Ronda 90, Granada 110, Gibraltar 100 (town centre, about 10 min inside Gibraltar), Cordoba 120, Sevilla 160, Cadiz 150, Frigiliana 75, Nerja 75 (marker is the Cueva de Nerja at Maro, not the Balcon de Europa), Olvera 110, Zahara 130, Vejer 140, Tarifa 110, Jerez 140, Setenil 100 min. Old OSRM figures are superseded and marked as such in the evidence ledger. Toll roads were not avoided (owner avoids tolls only under 60 minutes); AP-7 toll sections are noted per record. Zahara: Google's 122 km could not be reproduced in a Firecrawl route check (134 km).
- Hours, prices, links and evidence: read on 2026-10-30 from official venue, municipal or tourism pages; conflicts are kept as review issues (Ronda Tue-Fri 9:30 vs 10:00; Olvera winter hours and castle price; Frigiliana Saturday hours; Vejer museum EUR 2 vs 4; Tarifa hours from a 2025 page). No official hours or prices were found for the Zahara tower or for Setenil (blocking issues).
- New section "Nearby suggestions" in each record body (sights, viewpoints, combinations) with sources from official tourism or heritage pages. No restaurant or roadside rest stop is named without a source; none was verified in this pass. Owner decision 2026-10-30: nearby suggestions stay as text, no new schema field; revisit when feedback shows a need for filtering.
- Owner decision 2026-10-30: the chosen main-sight markers (including Real Alcazar for Sevilla and the cathedral for Cadiz) are accepted; the guide is a suggestion, not a complete fact sheet.
- Regenerated `data/place-catalog.csv`. `python3 tools/places.py validate` reports the same 6 pre-existing errors in other records (`energy_level` None) and no errors in the 14 edited records.
- Editor input the same day (17:15): `nerja` is centred on the caves, the Balcon de Europa and the nearby beach, with the Cuevas de Nerja as the suggested starting point (the Google marker is the caves); `zahara-de-la-sierra` and `setenil-de-las-bodegas` got editor-supplied additions (La Playita, Garganta Verde permit, Paseo de los Refranes, Mirador del Carmen and others). These come from a Google AI summary and third-party sites, are marked as editor-supplied in the body and the evidence ledger (confidence low) and carry an info issue; Nerja, Zahara and Setenil are otherwise closed by the owner and get no further work.
- Not changed: schema, categories, tags, enums, layers, `AGENTS.md`, `data/layer-membership.csv`, `cost_level`, accessibility and family ratings.
- Open: Frigiliana Saturday hours, Vejer museum price, Zahara tower and Setenil hours/prices need a phone call; language of the "Nearby suggestions" text (English, matching the records) vs. a Danish presentation layer; Saturday-morning measurement is one sample per route.

## 2026-10-29 - Excursion pilot: five places re-verified (draft, additive, no schema change)

Owner request: verify excursion records for young adults and seniors, pilot of five places. Branch `udflugter-verificering-1`; **draft, not pushed, not editor-approved.**

- Records edited: `malaga`, `marbella-old-town`, `antequera`, `el-torcal-de-antequera`, `tolox`, `caminito-del-rey`.
- Driving times replaced by Google Maps figures measured by the owner on Thursday 2026-10-29, toll roads avoided (owner's standing setting): Marbella old town car park 36 min, Malaga Alcazaba 47 min (car park C/ Alcazabilla 2: 49 min), Antequera Alcazaba 75 min, El Torcal visitor centre 85 min, Caminito del Rey reception centre 65 min. Old OSRM figures (34-36, 65, 72, 75 min) are superseded. One sample each, not a Saturday morning; Tolox (56 min, OSRM) not re-measured.
- Malaga: added Cercanias C1 train from Fuengirola (about 46 min, every 20 min; station 16 min by car from the house). Fare, station parking and walking distances not verified.
- Antequera: opening hours and prices confirmed from the municipal tourism site; blocking issue `official_links_unverified` removed; status `needs_editorial_review`.
- El Torcal: hours corrected (earlier secondary figures were wrong); visitor-centre closing time 17:00 vs 17:30 unresolved; operator site shows injected spam text.
- Tolox: spa open 1 June - 16 October only, closed now. Owner decision 2026-10-29: Tolox stays and is marked seasonal (June-October).
- Caminito del Rey: reception hours, walking time and shuttle details added from the official site.
- Not changed: schema, categories, tags, enums, layers, `AGENTS.md`.

## 2026-10-29 - Rule for local_30km: Google driving time, whole layer (no schema change)

Owner decision 2026-10-29: membership of `local_30km` is decided by a one-way driving time of at most 30 minutes, taken as Google Maps' main figure, not by straight-line distance. The rule applies to the whole layer, not only to beaches. This supersedes the "Layer boundary rule" bullet in the entry "2026-10-15 - Layer-boundary decision and post-fact-check corrections" (straight-line placement).

Measurement method (beaches): measured by the owner in Google Maps on Saturday 2026-07-18 at 10:00, one sample, from Calle Milano 35, 29649 Las Lagunas de Mijas (36.5356, -4.6627) to Google's marker for the destination (Cabopino: the parking point). Google's main figure is stored in `driving_time_from_casa_de_la_familia.duration`; the typical range, the owner's own figure where given, and the method are stored in its note.

- Rio Real was removed (draft; it does not become a record). 13 beach drafts exist in `docs/places/` (status `draft`, local, not pushed).
- Google main figures (min): Cabopino 20, Los Monteros 28, La Butibamba 16, Castillo-Ejido 12, Fuengirola centrum 18, Boliches-Gaviotas 16, Carvajal 20, Santa Ana 28, Fuente de la Salud 30, La Carihuela 30, El Bajondillo 28, Playamar 28, Los Alamos 30. All 13 are measured and within the limit. Fuente de la Salud, La Carihuela and Los Alamos sit exactly on it and stay in the layer. Los Alamos is measured (30 min).
- Moved out of `local_30km` by the new rule: Malaga (36 min), Marbella old town (34 min, `data/route-checks-2026-10-16.csv`) and Tolox (56 min). Owner decision: they return to `excursions_4h`, where they were before 2026-10-15. This entry does not itself edit `data/layer-membership.csv`.
- Not changed by this entry: `AGENTS.md` line 9, `data/layers.csv`, `data/layer-membership.csv`, schema, categories, tags, enums.
- Open: update `AGENTS.md` line 9 and the `local_30km` rule text in `data/layers.csv` to the new rule; apply the layer moves in `data/layer-membership.csv`; the beach measurement is one summer-Saturday sample.
- Applied later on 2026-10-29 (separate commit on branch `strande-kladder`): Malaga, Tolox and Marbella old town moved to `excursions_4h` in `data/layer-membership.csv`; the `local_30km` rule text in `data/layers.csv` and `AGENTS.md` line 9 now state the driving-time rule; `docs/excursions-layer-overlap.md` updated for Marbella old town. Still open: `tools/places.py` keeps a straight-line helper column (`within_primary_radius`, 30 km) that no longer decides layer placement; the other open points above remain.
- On branch `strande-kladder`; not merged to `main`.

## 2026-10-16 — Senior itineraries (draft package; additive, no schema change)

Owner request: day trips and overnight routes for fit seniors (about 60–75), from Casa de la Familia as far as the Portuguese border. **Draft; not editor-approved.**

- Added `docs/senior-itineraries.md` (scope, fact-check ledger, open decisions), `data/senior-itineraries.csv` (14 itineraries referencing existing record IDs) and `data/route-checks-2026-10-16.csv` (12 new OSRM route checks with approximate destination coordinates).
- Not changed: place records, `AGENTS.md`, `data/layers.csv`, `data/layer-membership.csv`, schema, categories, tags, enums.
- Owner decisions the same day: the time limit is extended to about 5 h one-way, added as layer `excursions_5h` in `data/layers.csv` (`excursions_4h` unchanged); Portuguese places are out of scope for now (Vila Real de Santo António and Tavira removed from the itineraries, route checks kept and marked out of scope). `AGENTS.md` got a matching bullet.
- Open editor decisions: creation of draft records for the places that have none (Mijas Pueblo, Casares, Arcos de la Frontera, Grazalema, El Rocío, Ayamonte); whether seniors become a named audience of the excursion layers.
- Merge target named by the owner: `christiano-ez/callemilano`. Not merged.

## 2026-10-15 — New controlled tag: Overnight

Editor-approved schema change: added `Overnight` to the controlled tag vocabulary in `docs/place-schema.md`, `AGENTS.md`, and `tools/places.py`'s `TAGS` set. `Overnight` replaces `Full day` for a destination whose realistic one-way drive time makes a day trip impractical (e.g. Sevilla, Córdoba in the excursion layer); a record uses one or the other, never both.

## 2026-10-15 — Non-Spain territory code in the place ID format

Editor-approved schema change: `docs/place-schema.md`'s `id` format now documents the leading segment as the place's own country/territory code (`ES` for Spain, or another appropriate code — e.g. `GI` for Gibraltar, a British Overseas Territory — for a place outside Spain), with a shorter `{TERRITORY}-{PLACE}-{NNN}` form for a territory without Spain's region/province structure.

Gibraltar's ID is corrected from the borrowed `ES-AND-CAD-GIBRALTAR-001` to `GI-GIBRALTAR-001`. The old ID is retired (not deleted) in `data/place-id-registry.csv`; the new ID is allocated under a new `GI` namespace. Updated: `docs/places/gibraltar.md` (`id` field, `not_spain` review issue resolved), `data/place-id-registry.csv`, `data/layer-membership.csv`. No other record's ID changes — this correction was made before the record left draft/review status, per the stable-ID rule (never change an ID after `approved`).

## 2026-10-15 — Layer-boundary decision and post-fact-check corrections

Editor-of-record decisions following fact-check of the 17 excursion-layer records:

- *Superseded 2026-10-29, see the "Rule for local_30km" entry above.* **Layer boundary rule:** for records whose route-checked driving time was now known, the editor decided layer placement (`local_30km` vs `excursions_4h`) by straight-line km distance rather than driving time, since driving time varies with traffic/route. Málaga (29.9 km, `malaga.md`) and Tolox (27.7 km, `tolox.md`) fall within the 30 km primary radius and were moved from `excursions_4h` to `local_30km` in `data/layer-membership.csv`; their `layer_boundary_open` and `excursion_layer_scope` review issues were resolved and removed.
- **Gibraltar border treaty confirmed:** the previously secondary-sourced claim that routine checks were removed at the Gibraltar-Spain land frontier is now confirmed directly from an official Government of Gibraltar press release (15 July 2026, frontier gates/barrier removed). `gibraltar.md`'s `border_treaty_unconfirmed` blocking issue is resolved; a narrower, non-blocking issue remains for downstream mechanics (exact Schengen/customs handling, current queue conditions) that are still only secondary-sourced. Status advanced to `needs_editorial_review`.
- **Jerez bodega-tasting age policy:** editor decision — no venue-specific minimum age needs chasing beyond Spain's standard legal drinking age (18), which governs the tasting regardless of how the tour is marketed. `jerez-de-la-frontera.md`'s `alcohol_age_policy_unknown` blocking issue is resolved and removed.

## 2026-10-15 — Young adults migration

Editor-approved schema change: age groups `Teenagers (13-17)` and `Adults` merged into `Young adults`; `family_score` keys `teenagers` and `adults` merged into `young_adults` (rule: max; `unknown` if either input is unknown). Updated: all `docs/places/*.md`, `tools/places.py` constants, `data/personas.csv` (weights summed), `AGENTS.md`, `docs/place-schema.md`. Analytical datasets and the engine spec were not migrated by this commit; see `docs/schema-change-proposal-young-adults.md` and issue #5 for the follow-up below, which completes that work.

## 2026-10-16 — Young adults migration: analytical datasets and recommendation engine (closes #5)

Completes the follow-up issue #5 raised by the schema migration above. Two PRs, in order:

- **`data/destination-metadata.csv`**: merged `teen_score`/`adult_score` into a single `young_adult_score` column, same max rule as the schema migration. **`docs/recommendation-engine-spec.md`**: `base_score` formula and factor list updated to use `young_adult_score`/`young_adult_suitability_weight` (this also fixed a real bug — the spec still referenced `teen_suitability_weight`/`adult_suitability_weight`, which `personas.csv` no longer had since the original migration already merged them). **`docs/data-dictionary.md`** and **`docs/guest-questionnaire-spec.md`**: column references updated to match. **`docs/examples/*.md`** (4 files): illustrative `age_groups`/`family_score` examples updated to `Young adults`, merged with the same max rule, so they don't teach the deprecated taxonomy.
- **`docs/end-to-end-demo.md`**: all 10 worked guest-session scenarios recomputed against the current formula and data (a throwaway script implementing the spec exactly); 7 of 10 changed ranking or top-5 membership, since several destinations had `teen_score` ≠ `adult_score` pre-merge. A genuine exact tie in scenario 5 (aviation enthusiast) is broken alphabetically and noted in the document, since the engine spec defines no tie-break rule. **`docs/group-composition-v2.md`**: this document's party-composition formula weights age-suitability terms by headcount rather than selecting a persona-level score, so the main migration's max-rule approach didn't directly transfer; teenager and adult headcounts now combine into one `(teenagers + adults) × young_adult_score` term, and all 4 worked examples were recomputed. This collapses `party_suitability` to exactly `young_adult_score` for an all-adult/teenager party (Example 2), which is flagged explicitly in the document as a real behavior change, not just a rename.

Deliberately **not** migrated, per editor review (see issue #5 and the original proposal): `data/demo-groups.csv` (headcounts describing a synthetic test group's composition, not suitability scores — merging would lose information), `docs/gold-standard-sample-set.md` (uses "teen"/"adult" as ordinary English in editorial prose, not as schema field references), `docs/discrimination-analysis.md` (a historical analysis snapshot of the old data, not a live spec). `README.md` and `demo/index.html` were checked and already carried no stale references.

`python3 tools/places.py validate` unaffected both times (same 6 pre-existing errors in unrelated archive records).

## 2026-10-15 — Excursion layer (additive; no schema change)

Owner decision: add a second layer, `excursions_4h` (route-checked one-way drive up to about 4 h), beside the 30 km primary area.

- Added 17 draft records in `docs/places/` (Málaga, Sierra de las Nieves, Tolox, Caminito del Rey, Setenil de las Bodegas, Antequera, El Torcal de Antequera, Nerja, Tarifa, Vejer de la Frontera, Granada, Sevilla, Córdoba, Cádiz, Jerez de la Frontera, Gibraltar, Las Alpujarras). All `draft`, no coordinates, no route-checked driving time, no sourced facts; blocking review issues on each.
- Reserved the 17 IDs in `data/place-id-registry.csv` and added 17 rows to `data/import-queue.csv`.
- Added `data/layers.csv` and `data/layer-membership.csv`.
- Added persona `Young adults` to `data/personas.csv` (weights are editorial estimates).
- Added the scope section to `AGENTS.md` and a bullet to `README.md`; added `docs/excursions-layer.md` and `docs/excursions-layer-overlap.md`.
- Not changed: existing place records, categories, tags, enums, schema. The merge of `Teenagers (13-17)` and `Adults` into `Young adults` is a separate proposal: `docs/schema-change-proposal-young-adults.md`.

## 2026-10-05 — Google Maps intake list

- Added `data/maps-intake-projekt-spanien.csv`: the 212 places in the owner's "Projekt Spanien" Maps list, with triage coordinates and distance rings from Casa. Coordinates are approximate (the export has none); see `docs/data-dictionary.md`. Result: 13 places within 30 km, 25 at 30–60 km, 17 at 60–100 km, 138 beyond 100 km, 18 unplaced, plus the Casa address.

## 2026-10-05 — Local scope, tooling, and documentation consistency

Owner decision plus consistency fixes from the 2026-10-05 repository review. No place record, category, tag, enum or schema field was changed.

### Scope decision (owner)
- First phase limited to destinations within about 30 km of Casa de la Familia, confirmed by route-checked driving time. Primary audience: families with children who prefer short drives; secondary: adults, seniors, teenagers. Spain-wide records are kept as an archive. Recorded in `AGENTS.md`, `README.md` and `docs/project-state.md`.
- Origin coordinates fixed from the owner's Plus Code `8C8QG8PP+7W` = 36.5356875, -4.6626875.

### Tooling
- Added `tools/places.py` with `validate` (structural validation gate: YAML, schema version, required fields, enums, ID/slug/registry, duplicate SEO titles, approval gate; warnings for missing coordinates and unresolved driving times) and `catalog` (generates `data/place-catalog.csv` with distance from Casa and a within-30-km flag). Fact accuracy and evidence adequacy remain human checks.
- Generated `data/place-catalog.csv` for the first time.

### Files
- Created `data/image-rights.csv` (header only) and `images/` so the files named in `AGENTS.md` exist.
- Removed `demo 2/index.html`, a byte-identical duplicate of `demo/index.html`.
- Added `docs/data-dictionary.md` (all CSVs) and `docs/README.md` (documentation map).

### Documentation
- `README.md`: `Cities` → `City`; corrected the description of `data/` (registers and analytical datasets, not place records); added scope, folders and tooling.
- `AGENTS.md`: added scope and audience; stated that the recommendation datasets in `data/` are analytical, non-canonical inputs with their own tag vocabulary; stated that `docs/published/` pages are drafts outside the lifecycle; referenced the validator.
- `docs/project-state.md`: rewritten to reflect 30 records, the new scope, tooling, and current open issues.

### Not changed (needs editor-of-record decision)
- `energy_level: null` in six identity-unresolved drafts (schema allows no unknown value); questionable categories for Alcázar de Segovia, Mercado de Atarazanas and Baelo Claudia; mapping between schema tags and collection tags; revision of the recommendation engine for the local scope.

## 2026-10-03 — P0/P1 documentation remediation

Applied the P0 contract decisions and P1 operational design from `docs/remediation-plan.md`. This update changes project guidance and specifications; it does not implement executable validators, create registry/queue data files, migrate standalone examples, or publish place records.

### `AGENTS.md`

- Made `docs/places/` the sole canonical home for editable place records and specified Markdown with YAML front matter as their single source of truth. This resolves conflicting storage guidance and prevents editable duplicates.
- Defined roles for the ID registry, generated catalog, and image-rights register under `data/`, while retaining `images/` for image assets. This assigns canonical responsibilities to project folders.
- Reconciled category labels by making `City` canonical and replacing informal audience wording with the schema's exact age groups and separate suitability scores. This prevents enum drift.
- Added lifecycle and unknown-value rules, stable ID/slug rules, source evidence expectations, asset-rights policy, and named human editor-of-record authority. This aligns agent guidance with the review and approval process.
- Added a mandatory pre-approval validation checklist and review of volatile facts. This establishes a quality gate for future records.

### `docs/place-schema.md`

- Declared schema version `1.0.0` and the canonical Markdown/front-matter format. This gives records and agents a versioned contract.
- Added required `status` and documented lifecycle transitions, approval ownership, draft-only unresolved values, and publication blockers. This resolves the missing lifecycle and inconsistent completeness rules.
- Standardized category `City`, controlled audience labels, and family-score keys. This aligns the schema with project vocabulary.
- Specified registered stable IDs, unique slugs, redirects on slug changes, external identifiers, coordinate purpose, and a representative-point convention. This reduces ambiguity and collisions.
- Added autonomous community and country fields. This makes Spanish administrative geography complete and supports future regional expansion.
- Added typed official/booking/visitor/transport/contact links and structured visit information for schedules, durations, booking lead time, validity, and cost basis. This provides a home for useful, time-sensitive visitor data.
- Added structured accessibility dimensions and made `wheelchair_friendly` a derived summary. This avoids contradictory access fields and makes mobility/sensory information explicit.
- Expanded parking details and added structured non-car transport options. This supports accurate arrival planning.
- Defined qualitative per-person cost tiers, required cost basis and checked date, and separated incidental costs. This makes comparisons less ambiguous.
- Added stable image asset IDs, image roles, rights status, and centralized rights-register requirements. This separates rights lifecycle from place facts.
- Added claim-level evidence and review-issue structures, including source type, checked date, checker, confidence, severity, owner, and retryability. This makes verification traceable and handoffs actionable.
- Added related-place references and record creation/update/review dates plus human review decisions. This supports catalog relationships and content maintenance.
- Replaced the embedded Nerja data illustration with a clearly labeled draft example using the new schema, explicit unknowns, and an illustrative claim-level citation. This demonstrates status, evidence, and unknown-value handling without presenting unresolved details as verified.
- Clarified that files in `docs/examples/` are illustrations, not canonical place records. This prevents examples from being confused with approved content.
- Created the empty `docs/places/` output directory so the newly designated canonical record location exists for future drafts.

### `docs/maps-import-agent-spec.md`

- Aligned record output with `docs/places/` and front matter; defined the roles of the ID registry, generated catalog, import queue, and image-rights register. This makes intake and storage consistent.
- Added batch queue fields and states, duplicate detection, ID/slug reservation, ambiguity persistence, and resume behavior. This covers bulk imports and clarification loops.
- Required claim-level evidence, schema version, complete fields, source dates, route evidence, and explicit review issues. This makes drafts verifiable and schema-bound.
- Defined image asset rights handling, validation requirements, handoff report, retry/escalation rules, and explicit limits on agent authority. This makes import outputs safer to review and operate.

### `docs/multi-agent-workflow.md`

- Aligned all stages to the canonical record path, ID registry, generated catalog, and image-rights register. This removes conflicting data locations.
- Added batch queue lifecycle, per-item progress, duplicate checks, clarification pause/resume, and update-versus-create behavior. This supports scalable intake.
- Clarified each agent's responsibilities and handoff outputs; allowed independent factual checks to run in parallel while retaining risk-based fact-check and human-review gates. This reduces unnecessary serial delay without weakening review of consequential facts.
- Added single-file ownership and version-checked edits. This prevents concurrent agents from overwriting one another.
- Added a validation gate covering YAML, schema/version, enums, ID/slug uniqueness, evidence, links, duplicate identity/SEO, and image rights. Until an executable validator exists, the workflow requires a named reviewer to perform and record this check manually.
- Defined shared issue format, retry limit, escalation authority, approval sign-off, rework, corrections, archives, stale-data handling, image-rights withdrawal, and taxonomy/schema change control. This completes operational handoffs and assigns accountability.
- Clarified that approval is a human action and publication remains a separate process. This keeps agent work within the editorial boundary.

## Implementation notes

- The specifications name `data/place-id-registry.csv`, `data/import-queue.csv`, `data/place-catalog.csv`, and `data/image-rights.csv` as canonical operational files. Their headers, generated catalog process, and queue/registry tooling still need implementation before those workflows can run operationally.
- The workflow now defines a mandatory validator but does not add validator code. Until that exists, perform and record the stated validation checklist manually.
- Standalone files under `docs/examples/` were not migrated in this change. They remain examples only; copy none into `docs/places/` without converting it to schema version `1.0.0`, adding required fields, and resolving its review issues.
- No website, publication, deployment, or external service was changed.
