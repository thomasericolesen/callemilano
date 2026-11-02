# Handover for the next session (written 2026-11-02, evening)

Start here. Details per step are in `docs/change-log.md`; owner decisions 1-16 in `docs/owner-decisions-2026-11-02.md`.

## How we work now
- **One system, two phases.** Advance work (places, opening hours, restaurants) goes into place records via `tools/intake.py` and subagents; trip plans (`/turforslag`) read those records via `tools/trip.py` and the agent Ecco. See `docs/agent-pipeline.md` and `docs/trip-planner-agents.md`.
- **Subagents** (in `.claude/agents/`, loaded at session start): `candidate-screener` and `source-reader` (Haiku), `record-writer`, `alpha`, `charlie`, `ecco` (Sonnet). The main session keeps owner dialogue, decisions, spot checks (at least two quotes per batch), commits and PRs.
- **Cost rules:** curl via `intake.py fetch` before Firecrawl; Firecrawl only in query mode; read JSON summaries, not pages; one subagent call per batch.
- Optional for the owner: add `"Bash(python3 tools/intake.py *)"` to `allow` in `.claude/settings.json` (agents may not edit it).
- Restaurants are full place records; `data/restaurant-directory.csv` (26 Fuengirola-area rows) is a lead list.

## State
- 190 records, 0 validation errors. PR #38 (pipeline, nature batch, trip-planner merge) is merged into `main`.
- Old branch `claude/awesome-clarke-tvlhrg` is superseded by this merge; it can be closed without merging (its Fuengirola change was wrong for the beach record).

## Next, in suggested order
1. **Restaurant price bands (2026-11-02 evening):** 23 non-approved restaurant records now have `cost_level` (7 from own menus, 16 from TheFork/Tripadvisor as noted fallback). Owner approved the 5 approved-record proposals and set Somos de Banús to `€€€`; done. Still `Unknown`: 12 non-bar records listed in `docs/change-log.md` (La Sierra / Cerrado del Águila resolved and merged; Juanito Juan confirmed and priced).
2. **Directory leads converted (2026-11-02):** 21 owner-selected rows are records (7 `needs_fact_check`, 14 draft with `no_readable_own_source`); 3 rows `fravalgt`, KFC still a lead. Six more restaurant records came from the owner's recommendations on callemilano.dk (Lovable table `recommendations`); they need a fact check (own sites: cafenomadfuengirola.com, utopialacala.com, ventaloscondes.com, elsheriff.com; Sheriff is possibly closed). The three hotels from the site (Castillo de Monda, Molino del Santo, Casas Cuevas Almagruz) are restaurant records in `excursions_4h` (owner decision); check whether non-residents can eat there. Next for the 14 drafts: owner screenshots of menus/Facebook, or the TheFork/Tripadvisor fallback for price only.
3. **First real `/turforslag`** with a local beach and Fuengirola town, to test end to end.
4. **Open sources:** Angosturas (council page blocks robots), Río Grande Coín (no official page), Paseo Marítimo de Marbella and Senda Litoral Málaga (pages found cover other sections), Puerto Banús beach facilities, Juanar walking route.
5. **Owner input:** re-answer Marabierta and Vista al Mar on https://claude.ai/artifact/1uvFqCZBd5LEWGDDS3aVr7; screenshots for 7 restaurants without own sites (El Andaluz, Juanito Juan, Casa Manuel de la Lonja, Norte, Central Beach, La Escollera, Mar de Alborán); family assessments for the new records; Marbella boat trips (provider sweep and reputation screen first).
6. Still open from earlier: bars to confirm by phone/visit, beach lifeguard seasons 2027, 2027 event dates in `docs/season-calendar-draft.md`, owner review of `docs/practical-information-draft.md`.

## Pending: price markings found 2026-11-02, not yet applied

Owner said to use TheFork/Tripadvisor for the new restaurant records without readable own prices. The lookup ran, but Firecrawl credits ran out before the orchestrator spot check (Tripadvisor returns 403 to curl and WebFetch), so nothing was written. Next session: spot-check at least two lines (credits reset 2026-11-03 15:55 UTC), then apply `€€` for the five identity-confirmed rows (`secondary`, low confidence, issue `cost_level_secondary_source`). For the four unconfirmed rows, confirm the address first; Sollo (TheFork 250 €) and El Higuerón (`$$$$`) would be `€€€`.

| Record | Marking | Identity by address | URL |
|---|---|---|---|
| `juan-playa-fuengirola` | tripadvisor "$$ - $$$" | no | https://www.tripadvisor.com/Restaurants-g315915-c33-zfp5-Fuengirola_Costa_del_Sol_Province_of_Malaga_Andalucia.html |
| `vegetalia-fuengirola` | tripadvisor "€€ - €€€" | yes | https://www.tripadvisor.es/Restaurant_Review-g315915-d984713-Reviews-Vegetalia_Fuengirola-Fuengirola_Costa_del_Sol_Province_of_Malaga_Andalucia.html |
| `ragazzi-fuengirola` | tripadvisor "$$ - $$$" | yes | https://www.tripadvisor.com/Restaurant_Review-g315915-d8401666-Reviews-Ragazzi-Fuengirola_Costa_del_Sol_Province_of_Malaga_Andalucia.html |
| `fosters-hollywood-miramar` | tripadvisor "$$ - $$$" | yes | https://www.tripadvisor.com/Restaurant_Review-g315915-d4025871-Reviews-Foster_s_Hollywood-Fuengirola_Costa_del_Sol_Province_of_Malaga_Andalucia.html |
| `la-tagliatella-miramar` | tripadvisor "$$ - $$$" | yes | https://www.tripadvisor.com/Restaurant_Review-g315915-d23330362-Reviews-La_Tagliatella_Fuengirola-Fuengirola_Costa_del_Sol_Province_of_Malaga_Andalucia.html |
| `kalifato-benalmadena` | tripadvisor "$$ - $$$" | yes | https://www.tripadvisor.com/Restaurant_Review-g562812-d984662-Reviews-El_Kalifato-Benalmadena_Costa_del_Sol_Province_of_Malaga_Andalucia.html |
| `sollo-fuengirola` | thefork "Precio medio: 250 €" | no | https://www.thefork.es/restaurante/sollo-r869790 |
| `freiduria-el-choco-fuengirola` | tripadvisor "$$ - $$$" | no | https://www.tripadvisor.com/Restaurant_Review-g315915-d2480160-Reviews-Freiduria_Pulperia_El_Choco-Fuengirola_Costa_del_Sol_Province_of_Malaga_Andalucia.html |
| `el-higueron-fuengirola` | tripadvisor "$$$$" | no | https://www.tripadvisor.com/Restaurant_Review-g315915-d1003583-Reviews-or45-El_Higueron_Restaurante-Fuengirola_Costa_del_Sol_Province_of_Malaga_Andaluci.html |

No TheFork/Tripadvisor listing found: `monnalisa-fuengirola`, `kamura-sushi-fuengirola`, `da-vinci-los-boliches`, `meson-salvador-fuengirola`, `burger-king-miramar`, `the-good-burger-miramar`, `casa-carmen-miramar`, `antonio-playa-fuengirola`, `cafe-nomad-fuengirola`, `heladeria-casa-esteban-fuengirola`, `marvelous-burger-fuengirola`, `utopia-la-cala`, `venta-los-condes`, `restaurante-sheriff`. For these, owner screenshots (menu or Facebook) are the remaining route.
