# Handover for the next session (written 2026-11-02, 21:20 Danish time)

Start here. Details per step are in `docs/change-log.md` (entries dated 2026-11-02 evening/late evening); owner decisions 1-16 in `docs/owner-decisions-2026-11-02.md`. Confirm today's date with a tool before any time-sensitive step (owner preference).

## How we work now
- **One system, two phases.** Advance work (places, opening hours, restaurants) goes into place records via `tools/intake.py` and subagents; trip plans (`/turforslag`) read those records via `tools/trip.py` and the agent Ecco. See `docs/agent-pipeline.md` and `docs/trip-planner-agents.md`.
- **Subagents** (in `.claude/agents/`, loaded at session start): `candidate-screener` and `source-reader` (Haiku), `record-writer`, `alpha`, `charlie`, `ecco` (Sonnet). The main session keeps owner dialogue, decisions, spot checks (at least two quotes per batch), commits and PRs.
- **Cost rules:** curl via `intake.py fetch` before Firecrawl; Firecrawl only in query mode; read JSON summaries, not pages; one subagent call per batch.
- Optional for the owner: add `"Bash(python3 tools/intake.py *)"` to `allow` in `.claude/settings.json` (agents may not edit it).
- Restaurants are full place records; `data/restaurant-directory.csv` is a lead list; converted rows have status `konverteret`, owner-rejected rows `fravalgt` (only `aktiv` rows are read by `tools/trip.py`).

- **Firecrawl:** credits ran out on 2026-11-02; the daily allowance resets 2026-11-03 at 15:55 UTC (16:55 Danish time). Tripadvisor blocks curl and WebFetch (403), so TheFork/Tripadvisor work must wait for that reset.
- **Owner's website:** callemilano.dk is the Lovable project "Vores Spanske Hjem"; recommendations are in its database table `recommendations` (read with the Lovable MCP `query_database`, read-only use).

## State at hand-over
- 220 records, 0 validation errors, catalog regenerated. Work is on branch `claude/vigilant-cray-dtqaxz` (PR to `main` opened 2026-11-02; merge status: check on GitHub).
- Restaurants (non-bar, not archived): 68 records; 32 have `cost_level`, 36 are `Unknown`. Bars (18) are skipped by `tools/trip.py` and were not priced.
- Price-band rule (owner decision 2026-11-01, confirmed 2026-11-02): adult main + one drink; `€` < 15 €, `€€` 15-35 €, `€€€` > 35 €. Own menu first; TheFork average price / Tripadvisor marking as a noted low-confidence fallback (owner decision 2026-11-02). Google Maps prices are never used (AGENTS.md).

### Done 2026-11-02 evening
1. `cost_level` from own menus for 11 records and from TheFork/Tripadvisor for 17; five approved records priced after owner approval (`docs/cost-level-proposals-2026-11-02.md`); Somos de Banús `€€€` (owner).
2. La Sierra Restaurante = Cerrado del Águila (owner screenshot): kept `la-sierra-restaurante` (now `needs_fact_check`, `€€`), archived `restaurante-cerrado-del-aguila`.
3. Juanito Juan identity confirmed by address; `€€`.
4. Directory: owner checklist https://claude.ai/artifact/VCrXrv5vKsUhruvVk6R9ZT -> 21 new records (7 `needs_fact_check`, 14 draft with `no_readable_own_source`); 3 `fravalgt`; KFC (R-0201) "maybe", still `skal tjekkes`.
5. callemilano.dk: 5 owner recommendations created (Café NOMAD, Heladería Casa Esteban, Marvelous Burger, UTOPÍA, Venta los Condes) with the owner's text as owner-knowledge evidence; same added to Asador Otola; Restaurante Sheriff created with blocking issue `possibly_closed`.
6. Hotels Castillo de Monda, El Molino del Santo, Casas Cuevas Almagruz created as `Restaurants` in `excursions_4h` (owner: not standalone excursions; facilities guest-only).

## Next, in suggested order (2026-11-03)
1. **After 16:55 Danish time:** spot-check two lines from the pending price table below, then apply. Confirm the address for the four unconfirmed rows before applying.
2. **Fact check the 9 new website/hotel records** (source-reader -> record-writer): own sites cafenomadfuengirola.com, utopialacala.com, ventaloscondes.com, elsheriff.com (confirm Sheriff open/closed by phone +34 952 493 722), castillodemonda.com, molinodelsanto.com, cuevasalmagruz.com; for the hotels, whether non-residents can eat and whether booking is needed. Heladería Casa Esteban and Marvelous Burger have no own site.
3. **Owner screenshots** (fastest route where sites are blocked or missing): menus or Facebook pages for Monnalisa, Kamura Sushi, Da Vinci, Mesón Salvador, Casa Carmen, TGB, Burger King, Antonio Playa, Heladería Casa Esteban, Marvelous Burger, UTOPÍA, Venta los Condes; earlier list: El Andaluz, Casa Manuel de la Lonja, Norte, Central Beach, La Escollera, Mar de Alborán, Chiringuito Cristóbal.
4. **Old Swiss House:** resolve `source_conflict` (hours and street number 26/28) by phone or owner knowledge. **El Choco:** re-read Wednesday-Sunday hours.
5. **First real `/turforslag`** with a local beach and Fuengirola town, to test end to end (Fuengirola now has many priced restaurants).
6. **Open sources:** Angosturas (council page blocks robots), Río Grande Coín (no official page), Paseo Marítimo de Marbella and Senda Litoral Málaga, Puerto Banús beach facilities, Juanar walking route.
7. **Owner input still open:** re-answer Marabierta and Vista al Mar on https://claude.ai/artifact/1uvFqCZBd5LEWGDDS3aVr7; family assessments for the new records; KFC yes/no; Marbella boat trips (provider sweep and reputation screen first).
8. Still open from earlier: bars to confirm by phone/visit, beach lifeguard seasons 2027, 2027 event dates in `docs/season-calendar-draft.md`, owner review of `docs/practical-information-draft.md`.

### Restaurants still without `cost_level` (36, non-bar)
antonio-playa-fuengirola, burger-king-miramar, cafe-nomad-fuengirola, casa-carmen-miramar, casas-cuevas-almagruz, castillo-de-monda, chiringuito-cristobal (approved; owner only), courtside-by-wissler, da-vinci-los-boliches, el-andaluz-de-la-malagueta, el-higueron-fuengirola, fosters-hollywood-miramar, freiduria-el-choco-fuengirola, heladeria-casa-esteban-fuengirola, juan-playa-fuengirola, kalifato-benalmadena, kamura-sushi-fuengirola, la-tagliatella-miramar, la-zambra-resort, marvelous-burger-fuengirola, meson-salvador-fuengirola, mixs-lounge, molino-del-santo, monnalisa-fuengirola, pena-al-tranco, ragazzi-fuengirola, restaurante-cerros-del-aguila, restaurante-sheriff, singh-doner-kebab, sol-y-sombra-mijas, sollo-fuengirola, taberna-mar-de-alboran-estepona, the-good-burger-miramar, utopia-la-cala, vegetalia-fuengirola, venta-los-condes.

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
