# Handover for the next session (updated 2026-11-04, 11:45 Danish time)

Start here. Details in `docs/change-log.md` (entries dated 2026-11-03 and 2026-11-04) and the owner-facing summaries in `docs/status-rapport-2026-11-03.md` and `docs/status-rapport-2026-11-04.md` (Danish, written for an independent review in ChatGPT). Confirm today's date with a tool before any time-sensitive step (owner preference).

## How we work now
- **One system, two phases.** Advance work (places, opening hours, restaurants) goes into place records via `tools/intake.py` and subagents; trip plans (`/turforslag`) read those records via `tools/trip.py` and the agent Ecco. See `docs/agent-pipeline.md` and `docs/trip-planner-agents.md`.
- **Subagents** (in `.claude/agents/`, loaded at session start): `candidate-screener` and `source-reader` (Haiku), `record-writer`, `alpha`, `charlie`, `ecco` (Sonnet). The main session keeps owner dialogue, decisions, spot checks (at least two quotes per batch), commits and PRs.
- **Cost rules:** `intake.py fetch` first (curl, PDF text, headless Chromium; all free, PR #45); Firecrawl only for pages still `needs_firecrawl`, only in query mode; Facebook/Instagram are `login_wall` (owner screenshot); read JSON summaries, not pages; one subagent call per batch.
- Optional for the owner: add `"Bash(python3 tools/intake.py *)"` to `allow` in `.claude/settings.json` (agents may not edit it).
- Restaurants are full place records; `data/restaurant-directory.csv` is a lead list; converted rows have status `konverteret`, owner-rejected rows `fravalgt` (only `aktiv` rows are read by `tools/trip.py`).

- **Firecrawl:** the owner got an e-mail that all credits were used (the allowance ran out on 2026-11-02 and reset 2026-11-03 16:55 Danish time); about 6 calls were used on 2026-11-03 after the reset and worked. Check the balance in the Firecrawl dashboard before a large batch. Tripadvisor blocks curl, Chromium and WebFetch (403); tools that evade bot protection are not used (owner agreed 2026-11-03).
- **Owner's website:** callemilano.dk is the Lovable project "Vores Spanske Hjem"; recommendations are in its database table `recommendations` (read with the Lovable MCP `query_database`, read-only use).

## State at hand-over
- 220 records, 0 validation errors. Restaurants (non-bar, not archived): 69; `€` 7, `€€` 31, `€€€` 1, `Unknown` 30. App export: 149 places; local `€` restaurants (≤ 30 min): Cerros del Águila, Café NOMAD, Ragazzi, Lounge El Trópico, Marvelous Burger.
- Price-band rule (owner decision 2026-11-03, replaces the 15/35 € rule): median main on the menu + one drink; `€` < 20 €, `€€` 20-50 €, `€€€` > 50 €.
- Places repo: work on branch `claude/trusting-fermat-1trzme`; the change-log entries for the app decisions, this handover and the status report are in an open PR (check whether merged; if so start from `main`).
- App (`thomasericolesen/callemilano-f388b2be`, Lovable syncs `main`): `/turforslag` is admin-only and in the admin menu. Ecco (Claude Sonnet 5.5) works against the live API. Free-text wish -> Claude suggests 1-3 places, OpenAI (Lovable AI Gateway) only as fallback (owner decision 2026-11-04, app PR #11; consensus is for development reviews, not trip plans). `/ai-tur` redirects. Merged: thomasericolesen/callemilano-f388b2be#8 (distance between stops instead of summed drive times) and #9 ("Foreslå noget andet", "Start forfra", "Ny søgning", picked places numbered in route order); published by Claude via the Lovable deploy tool on 2026-11-03 (the owner could not publish; live bundle checked); owner test: Ecco writes about 470 m on foot, chips numbered.
- Lovable Publish does not run `drizzle/migrations/`; schema changes must be applied with the Lovable `query_database` tool after the owner merges (see 2026-11-02 entries).

## Next session, in suggested order
1. **Test app PR #11** (merged and published by the owner 2026-11-04 ~11:50; live bundle checked: reserve text and "UV op til" present, agreement badges gone): one trip plan; weather shows "UV op til X, sol 07:45-18:18" and no rain %; "Foreslå steder" shows no agreement badges.
2. **Weather (done 2026-11-04):** Open-Meteo answers the Lovable server with HTTP 429 (free quota per shared IP); met.no "complete" + Sunrise 3.0 is the effective source (UV clear-sky, sunrise/sunset; no rain % or gusts for Spain). Option: AEMET OpenData (official, free API key the owner registers at opendata.aemet.es) for rain probability and UV per municipality; ask the owner before building.
3. **Route-checked drive time between stops** (Google Routes, as `tools/intake.py` does from the house) for the 1-3 chosen stops, so `from_previous` gets minutes instead of only straight-line distance.
4. **Ecco polish:** "Køb hjemmefra" instead of "Kør hjemmefra" (2026-11-04); restaurants without fixed hours show "åbent område" (consider "ring og tjek" for restaurants); "Sevärdighed" (Swedish ä) seen once; keep the guest text short; check that `host_notes` are useful (they are folded on the page).
5. **Owner by phone:** Restaurante Sheriff open or closed (+34 952 493 722, then a drink price for the band); Old Swiss House hours and street number 26/28.
6. **Owner screenshots** (menus or Facebook): Venta La Morena, La Sierra Restaurante (Facebook `login_wall`), UTOPÍA and Venta los Condes (PDF menus unreadable), Kamura Sushi (image menu), Heladería Casa Esteban, Monnalisa, Mesón Salvador, Casa Carmen, Antonio Playa, Da Vinci Los Boliches (website does not resolve; check URL).
7. **Price check batch 2** (own menus, free fetch): Marisquería El Ancla (PDF carta readable), Tasca Laska (PDF), Taberna Casa Blanca (carta page), Chiringuito El Cachalote; then fact check, as for batch 1.
8. **Owner decisions still open:** Somos de Banús `€€€` (owner 2026-11-02) vs `€€` under the new rule; KFC yes/no; Marabierta and Vista al Mar on https://claude.ai/artifact/1uvFqCZBd5LEWGDDS3aVr7; family assessments for the new records.
9. **Owner decision 2026-11-04:** OpenAI/Claude consensus is for development reviews (OpenAI reviews Claude's reports, plans and changes), not for trip plans; agree a fixed review routine with the owner if wanted. **Next product step (status report):** the smallest turkort: save a trip and reopen it from "Mine ture" on a phone. A per-user daily cap before Turforslag opens to the family (each suggestion costs Claude and Lovable AI credits).
10. **Parity:** `tools/trip.py` (places repo, used by the Ecco subagent for PDFs) still prints the summed one-way drive time; align it with app PRs #8/#9 (`from_previous`, `first_stop_driving_min`).
11. Still open from earlier: Danish texts for imported places (`text_language: en`), open sources (Angosturas, Río Grande Coín, Paseo Marítimo de Marbella, Senda Litoral Málaga, Puerto Banús facilities, Juanar), bars to confirm, lifeguard seasons 2027, 2027 event dates, owner review of `docs/practical-information-draft.md`.

## Pending Tripadvisor/TheFork markings (found 2026-11-02, not applied)
Under the new bands, Tripadvisor "$$ - $$$" still reads as `€€` (low confidence). Ragazzi, Kalifato and Juan Playa were priced from own menus on 2026-11-03 and are no longer pending. Remaining (spot-check needs Firecrawl, Tripadvisor 403 elsewhere; confirm identity by address first where marked "no"):

| Record | Marking | Identity by address |
|---|---|---|
| `vegetalia-fuengirola` | tripadvisor "€€ - €€€" | yes |
| `fosters-hollywood-miramar` | tripadvisor "$$ - $$$" | yes |
| `la-tagliatella-miramar` | tripadvisor "$$ - $$$" | yes |
| `freiduria-el-choco-fuengirola` | tripadvisor "$$ - $$$" | no |
| `el-higueron-fuengirola` | tripadvisor "$$$$" | no |
| `sollo-fuengirola` | thefork "Precio medio: 250 €" (own site: 180 € tasting menu) | no |
