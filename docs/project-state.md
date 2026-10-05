# CalleMilano project state

**Last updated:** 2026-10-05
**Purpose:** Handoff for the next working session. `AGENTS.md` and `docs/place-schema.md` are the primary instructions and data contract. See `docs/README.md` for a map of all documents.

## Scope decision (2026-10-05)

The owner narrowed the first phase to destinations within about 30 km of Casa de la Familia (origin 36.53569, -4.66269, Plus Code `8C8QG8PP+7W`), confirmed by route-checked driving time. Primary audience: families with children who prefer short drives. Secondary: adults, seniors, teenagers. The Spain-wide collection is kept as an archive for later expansion.

## What exists

- **Place records:** 30 in `docs/places/`, all schema 1.0.0. 24 are `needs_fact_check`; 6 are `draft` with unresolved identity and `id: null` (Cares, Conil de la Frontera, Cueva de los Arcos, Miradouro da Serpente do Medal, Roca Foradada, Salt de la Coromina). None is approved or published.
- **Inside the primary area:** only Marbella Old Town (20 km) has coordinates. Mercado de Atarazanas, Palmeral de las Sorpresas and Playa la Malagueta lie at about 29–31 km but have no coordinates in their records yet.
- **Gold-standard page drafts:** `docs/published/` holds BIOPARC Fuengirola, La Cala Beach and Restaurante Sheriff as hand-written pages. They have no place record, ID or front matter and are outside the lifecycle.
- **Launch candidates:** `docs/launch-backlog.md` lists ten local destinations (Sheriff, La Cala, El Bombo, BIOPARC, Senda Litoral, Carromato de Mijas, Mijas Pueblo, Marbella Old Town, La Muralla route, La Familia Beach Club). Only Marbella Old Town has a record.
- **Tooling:** `tools/places.py validate` (structural validation gate) and `tools/places.py catalog` (generates `data/place-catalog.csv` with distance from Casa). Current run: 30 records, 6 errors (the six identity-unresolved drafts have `energy_level: null`, which the schema does not allow), 60 warnings (missing coordinates and unresolved driving times).
- **Registers:** `data/place-id-registry.csv` (24 IDs), `data/import-queue.csv` (only the first 5 pilots), `data/image-rights.csv` (header only), `data/place-catalog.csv` (generated). `images/` exists but is empty.
- **Recommendation prototype:** V1 engine spec, V1 questionnaire, V2 group-composition design, V3 enrichment analysis, all run on the 30-destination Spain-wide set in the analytical CSVs (`docs/data-dictionary.md`). `demo/index.html` is a static mock with 12 hard-coded destinations; it does not compute scores.

## Open issues

### Scope-driven (new)
1. No dataset of local destinations yet. Waiting for the owner's Google Takeout export (Saved lists, starred places, labelled places) to sort all saved places by distance from Casa.
2. Engine spec does not fit the 30 km scope: every local place scores 5 on drive time (≤ 1 h), durations stop at half-day, and three personas (aviation, hiking, overnight-oriented) are irrelevant locally. Needs finer drive-time bands, shorter durations, and beach factors (lifeguard season, shade, toilets, parking distance, sand/shallow water, child menu, stroller access).
3. The engine reads analytical CSVs keyed by display name, not the canonical records. Decide whether the next engine version reads `docs/places/` directly.

### Data and records
4. 24 of 30 records lack coordinates; no record has a route-checked driving time.
5. The six identity-unresolved drafts need identity confirmation, then `energy_level`, ID allocation and queue rows.
6. Five destinations lack a classification row (Frigiliana, Marbella Old Town, Ronda, Selwo Aventura, Zahara de la Sierra).
7. Two tag vocabularies (schema tags vs. collection tags) and two confidence scales coexist without mapping.
8. `docs/published/` pages need matching records in `docs/places/` before they can count as published.
9. Questionable categories for editor review: Alcázar de Segovia (`Family activities`), Mercado de Atarazanas (`Excursions`), Baelo Claudia (`Family activities`).

### Schema and editorial rules (carried over from 2026-10-03)
10. Place scope/pin rules for towns, `last_verified` semantics, criteria for duration/season/tags, age-group vs. family-score guidance, cost basis, SEO conventions, `wheelchair_friendly` derivation rule. See `docs/remediation-plan.md` for items beyond P0/P1.
11. Editor-of-record is referred to throughout but not named.

## Next actions

1. Import the Takeout export, compute distance from Casa for every saved place, and produce a ranked intake list (0–30 km first).
2. Create records with coordinates for the 15–20 most relevant local places (beaches in Fuengirola, Los Boliches, La Cala, Benalmádena, Torremolinos; BIOPARC; nearest excursions), starting with the launch backlog.
3. Revise the engine spec and personas for the local scope; then run top-10 recommendation tests per persona and compare with the owner's local knowledge.
4. Route-check driving times for local records.
5. Fact-check in batches; validate with `tools/places.py validate` before human review.

## Resume checklist

Read `AGENTS.md`, `docs/place-schema.md`, this file and `docs/data-dictionary.md`. Run `python3 tools/places.py validate`. Do not treat analytical CSV values or pilot record values as verified, and do not mark anything approved or published.
