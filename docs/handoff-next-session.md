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
1. **Restaurant price bands (2026-11-02 evening):** 23 non-approved restaurant records now have `cost_level` (7 from own menus, 16 from TheFork/Tripadvisor as noted fallback). Owner approved the 5 approved-record proposals and set Somos de Banús to `€€€`; done. Still `Unknown`: 12 non-bar records listed in `docs/change-log.md` (La Sierra / Cerrado del Águila resolved and merged; Juanito Juan identity still to check).
2. **Convert directory leads:** turn the 26 rows in `data/restaurant-directory.csv` into records (`intake.py sweep` by name -> owner checklist -> `create` -> fact check), then mark the rows as converted.
3. **First real `/turforslag`** with a local beach and Fuengirola town, to test end to end.
4. **Open sources:** Angosturas (council page blocks robots), Río Grande Coín (no official page), Paseo Marítimo de Marbella and Senda Litoral Málaga (pages found cover other sections), Puerto Banús beach facilities, Juanar walking route.
5. **Owner input:** re-answer Marabierta and Vista al Mar on https://claude.ai/artifact/1uvFqCZBd5LEWGDDS3aVr7; screenshots for 7 restaurants without own sites (El Andaluz, Juanito Juan, Casa Manuel de la Lonja, Norte, Central Beach, La Escollera, Mar de Alborán); family assessments for the new records; Marbella boat trips (provider sweep and reputation screen first).
6. Still open from earlier: bars to confirm by phone/visit, beach lifeguard seasons 2027, 2027 event dates in `docs/season-calendar-draft.md`, owner review of `docs/practical-information-draft.md`.
