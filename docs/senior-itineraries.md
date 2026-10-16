# Senior itineraries (day trips and overnight routes)

**Request:** owner, 2026-10-16. **Status:** draft package awaiting editor-of-record approval and a change-log decision. **Prepared by:** agent (Claude); not human-reviewed.

## Audience and scope

- Audience: fit seniors aged about 60–75 without walking or other mobility limits, using Casa de la Familia as the base. This is the schema age group `Seniors`; no schema change is proposed.
- Reach: day trips from the base and overnight routes all the way to the Portuguese border.
- Additive only: no existing place record, category, tag, enum, schema field, `AGENTS.md` rule or layer definition was changed. `data/layers.csv` is untouched.

## Decision needed from the editor

`excursions_4h` stops at about 4 h one-way. Route-checked times in this package show the Portuguese-border end lies beyond it (Ayamonte 265 min, Vila Real de Santo António 270 min, Tavira 286 min; Aracena 241 min is on the boundary). Two things need an editor decision before any record is created for these places:

1. Whether to add a layer beyond `excursions_4h` (or extend it) for overnight routes.
2. Whether Portuguese places are in scope. They need a territory code under the ID rule in `docs/place-schema.md`.

Seniors are also not the stated audience of the excursion layer (young adults). Records stay in their layer; itineraries only reference them.

## Files

- `data/senior-itineraries.csv` lists 14 itineraries' stops with place slug, ID (where a record exists), route-checked minutes, basis and status. Day trips are D1–D9; overnight routes are O1–O5.
- `data/route-checks-2026-10-16.csv` holds 12 new OSRM route checks from the fixed origin.
- This document holds the fact-check ledger below.

## Route checks

New checks use the repo's OSRM driving profile from the fixed origin (36.5356875, -4.6626875) and carry source URLs. **Destination coordinates are approximate reference points, not taken from an official source** (the OpenStreetMap geocoder refused automated access). Times are therefore indicative until the visitor point is confirmed per `docs/place-schema.md`. Values were not written into any place record.

| Place | One-way | Existing record |
|---|---|---|
| Mijas Pueblo | 21 min | no |
| Marbella old town | 34 min | yes (time was null) |
| Casares | 80 min | no |
| Olvera | 123 min | yes (time was null) |
| Grazalema | 131 min | no |
| Zahara de la Sierra | 138 min | yes (time was null) |
| Arcos de la Frontera | 169 min | no |
| El Rocío | 232 min | no |
| Aracena | 241 min | yes (time was null) |
| Ayamonte | 265 min | no |
| Vila Real de Santo António | 270 min | no |
| Tavira | 286 min | no |

## Fact-check ledger

Checked 2026-10-16. "Official" means an official or government source; "secondary" means commercial or press.

### Corrected against earlier chat answers

| Earlier claim | Result | Source |
|---|---|---|
| Gibraltar: passport needed, border queues | Outdated. Frontier gates and barrier removed on 15 July 2026; no routine immigration controls. Residual friction and non-EU Schengen checks at airport/port are only secondary-sourced. | Existing record `gibraltar.md` (official press release) |
| Gibraltar about 1 h; Caminito about 1 h; Tarifa about 1½ h | Gibraltar 92 min, Caminito 75 min, Tarifa 116 min | Existing records, route-checked |
| Mijas about 15 min; Marbella about 25 min; Casares 45–60 min | Mijas 21 min, Marbella 34 min, Casares 80 min | `data/route-checks-2026-10-16.csv` |
| Mijas to Ayamonte about 5 h | 265 min (4 h 25 min) | OSRM, see CSV |
| Paradores include Nerja | Not on the list reached (see below); unconfirmed | secondary |

### Confirmed

| Claim | Source | Type |
|---|---|---|
| Vía Verde de la Sierra is 36 km from Olvera station to Puerto Serrano station | [andalucia.org](https://andalucia.org/en/routes-via-verde-de-la-sierra) | official tourism board |
| Gruta de las Maravillas (Aracena): group visits about 45 min; about 1,200 m open to the public; 16–19 °C, 98–100 % humidity; max 1,000 visitors per day; closed 24, 25, 31 Dec and 6 Jan; small staircase down at the entrance | [andalucia.org](https://andalucia.org/en/la-gruta-de-las-maravillas-grotto-an-underground-treasure) | official tourism board |
| Cave entry is guided and time-specific; advance purchase recommended | Existing record `aracena.md` (municipal source) | official |
| Caminito del Rey: under-8s not admitted; over-8s show ID; booking effectively required; about €10 entry | Existing record `caminito-del-rey.md` | official |
| Alhambra Nasrid Palaces use timed entry; about 3 h visit; book ahead | Existing record `granada.md` | official |
| Parador de Ayamonte and Parador de Mazagón exist | [andalucia.com](https://andalucia.com/costa-de-la-luz/hotels/paradors) | secondary |
| Paradores in Granada, Carmona, Antequera, Ronda, Ayamonte, Córdoba, Mazagón, Cádiz, Arcos de la Frontera (and two in Málaga) are listed | [andalucia.com](https://www.andalucia.com/hotels/four-star-paradors.htm) | secondary; confirm on the Paradores site before booking |

### Partly verified or unverified (do not publish as fact)

| Claim | Status |
|---|---|
| Ayamonte–Vila Real ferry: about 12 min, €2.50 each way | One secondary source dated June 2024; operator named as Transporte Fluvial del Guadiana; timetable and 2026 price unconfirmed. [Source](https://www.nomadicbackpacker.com/spain-to-portugal-ayamonte-vila-real-ferry.html). The same source is consistent with Portugal being one hour behind Spain. |
| Sierra de Grazalema Pinsapar route needs a Junta de Andalucía permit | Secondary source says yes; also about 12 km, 4–5 h, medium difficulty, so not a light outing. Summer rules conflict between its sections; confirm with the Junta. [Source](https://www.elviajedesofi.com/ruta-del-pinsapar-de-grazalema-cadiz-como-hacerla/) |
| Caminito del Rey about 8 km, 3–4 h | Not confirmed from an official page (official site blocks automated access); existing record flags length, duration and difficulty as unconfirmed. |
| Sierra Greenway is flat | Not stated by the source above; unverified. |
| Doñana guided 4x4 tours (day, booking needed) | Only commercial listings reached; official operator and rules not confirmed. |
| Granada free tapas with drinks | Not checked; do not use. |
| Tarifa is often windy | Not checked. |
| Parador in Nerja | Not on the lists reached; unconfirmed. |

### Not fact-checked in this pass

Ratings, energy and "seniors" suitability in existing records are editorial estimates requiring human review. Opening hours, prices, parking and accessibility for places not listed above were not rechecked here; see each record's own evidence ledger and review issues.

## Suggested next steps

1. Editor decides the layer and Portugal questions above.
2. Create draft records for the candidates (Mijas Pueblo, Casares, Arcos de la Frontera, Grazalema, El Rocío, Ayamonte, and any Portuguese places approved) through the ID registry and the lifecycle.
3. Confirm visitor coordinates from official sources, then write route-checked times into records.
4. Merge with the second project once the editor approves; see the open question in the change log.
