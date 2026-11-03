# Intake and fact-check pipeline (owner decision 2026-11-02)

Goal: keep routine work out of the expensive main session. Deterministic steps run as scripts; narrow reading and writing tasks go to cheaper subagents; the main session (orchestrator) keeps owner dialogue, judgement and commits.

## Roles

| Layer | Who | Does | Never does |
|---|---|---|---|
| Scripts | `tools/intake.py` (no AI) | Google Places + Routes sweeps, nearby searches, page fetching (curl first), record creation with ID registry and layer membership, applying fact files, checklist pages | Judge facts |
| Subagent `candidate-screener` (Haiku) | `.claude/agents/candidate-screener.md` | Shortlist sweep results by fixed rules into checklist groups | Show ratings; invent features |
| Subagent `source-reader` (Haiku) | `.claude/agents/source-reader.md` | Fetch pages (`intake.py fetch`, Firecrawl `query` only when blocked) and return verbatim quotes as JSON | Paraphrase; paste pages into its reply |
| Subagent `record-writer` (Sonnet) | `.claude/agents/record-writer.md` | Turn quotes into an apply-file, run `intake.py apply`, validate, rebuild catalog | Status beyond `needs_fact_check`; touch approved records; family scores, categories, tags |
| Orchestrator | main Claude session | Owner questions and decisions, source conflicts, categories and editorial choices, spot checks, change log, commits, PRs | Read raw pages or long script output when a file will do |

## Standard batch

1. **Candidates:** orchestrator writes a query list -> `python3 tools/intake.py sweep q.json sweep.json` (or `nearby`) -> `candidate-screener` -> `python3 tools/intake.py checklist groups.json page.html --title ... --heading ... --lede ...` -> publish as an artifact with `capabilities: {db: {}}`.
2. **Owner selection:** the owner answers on the page; the orchestrator reads collection `choices` with ArtifactData (`out_dir`, not inline) and records the selection in `docs/`.
3. **Records:** orchestrator writes a create-spec (slug, name, category, municipality, short label) -> `python3 tools/intake.py create spec.json`.
4. **Facts:** orchestrator lists official/own URLs and questions -> `source-reader` -> `record-writer` (one call each per batch of up to about 20 places).
5. **Check:** orchestrator spot-checks at least two quotes per batch against the source, reads `git diff --stat`, writes the change-log entry, commits.

Work files go in the session scratchpad, not in the repo. Only records, data registers and `docs/` notes are committed.

## Cost rules

- One subagent call per batch, not per place; subagents reply in a few lines and leave details in files.
- `intake.py fetch` first: curl, then PDF text (pdftotext), then headless Chromium (`tools/render_page.mjs`, Playwright); all free. Firecrawl only for pages still marked `needs_firecrawl`, and only in `query` mode with `directQuote`, never full markdown. Facebook/Instagram are `login_wall`: ask the owner for a screenshot. Finding an official URL uses `WebSearch` before `firecrawl_search` (owner request 2026-11-03).
- The orchestrator reads JSON summaries, not pages.
- Re-use the templates in `tools/templates/`; do not write one-off record scripts.

## Quality rules (unchanged from AGENTS.md)

Official or own sources first; Maps only for identity and position; verbatim quotes in evidence; unknown stays unknown with a review issue; only the owner approves. Ratings and review counts are never recorded.

## Permissions

To avoid a prompt for each script call, the owner can add `"Bash(python3 tools/intake.py *)"` to the `allow` list in `.claude/settings.json`. Agents do not edit that file themselves.
