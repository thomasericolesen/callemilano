# Change log

## 2026-11-14 - Editor list (2) answered and written in (owner decisions, list)

Source: https://claude.ai/artifact/2HgGANPzRn8pRQqqdGcur1, answers read from collection `editorlist-2026-11-14b` (all 14 items decided). Written as the editor's own judgement with an evidence entry (date, link) per record; `last_reviewed_at` 2026-11-14. 42 records; no status changed.

- **Closed `excursion_layer_scope`** on 15 places (the layer was decided on 2026-10-15).
- **Closed `owner_has_not_visited`** on 13 bars; family feedback in the app replaces it.
- **Bars (13):** age groups Young adults and Seniors; family_score small children low, children low, young adults high, seniors medium; energy Low. `audience_not_assessed` closed.
- **Category, tags and audience (5):** values confirmed as shown, with changes: `baelo-claudia` tags + Historic town; `mercado-de-atarazanas` tags Rainy day and Free, age groups + Small children (0-6). Categories unchanged. Both review issues closed.
- **Family ratings (5):** confirmed as shown, except `marbella-old-town` seniors medium -> high. `family_ratings_estimated` closed.
- **Energy (4):** Low confirmed for `boliches-gaviotas`, `cabopino-artola`, `santa-ana-benalmadena` and `chiringuito-las-dunas-cabopino`.

## 2026-11-14 - Wheelchair "delvis" dropped (owner decision, chat)

- Nobody in the family uses a wheelchair, so showing "Delvist egnet" in the app is not a priority. App PR thomasericolesen/callemilano-f388b2be#39 and export PR #113 are closed; the branches are kept. `partial` stays in the records and is exported as "ukendt" (not shown in the app).

## 2026-11-14 - Freshness job, wheelchair "delvis" and editor list (2) (level A; the list's decisions are the editor's)

- **Freshness job:** new `tools/freshness.py` (tests in `tests/test_freshness.py`) lists overdue places, places without `next_review_at` and days until the import token expires; `--apply` sets overdue fact-checked places back to `needs_fact_check` with a `review_overdue` warning. A local scheduled task (`callemilano-friskhed`, 09:00 on the 1st of each month, on the owner's Mac while the Claude app is open) runs it and then follows the freshness procedure in `docs/multi-agent-workflow.md`.
- **Wheelchair:** records with `wheelchair_route`/`wheelchair_friendly` `partial` were exported as "ukendt". App PR thomasericolesen/callemilano-f388b2be#39 adds "delvis" ("Delvist egnet"); export PR #113 sends it. #113 is merged and imported only after the owner has published #39.
- **Editor list (2):** https://claude.ai/artifact/2HgGANPzRn8pRQqqdGcur1 (collection `editorlist-2026-11-14b`), 14 items: close `excursion_layer_scope` on 15 places (decided 2026-10-15), close `owner_has_not_visited` on 13 bars, audience values for the bars, and category/tags/audience/scores/energy for 14 places. Nothing changes until answered.

## 2026-11-14 - Ronda `cost_level` from the official timetable PDF (level A)

- `ronda`: `cost_level` set to EUR from the Ronda tourist office PDF of 1 October 2026 (read with Firecrawl; the PDF is image-only for other tools): Puente Nuevo interpretation centre 2.50 EUR, baths 4.50 EUR, gorge 12 EUR. The bridge and old town are free. `cost_level` removed from the `not_found_after_two_attempts` issue.
- Firecrawl also got "Access Denied" from andalucia.org. Status file `docs/status-2026-11-14.md` updated with the day's work.

## 2026-11-14 - `next_review_at` set on 34 app places (level A)

- **Set** on the app places that had none (34 of the 35; `canon-de-las-angosturas` is still `needs_fact_check` and keeps no date until it is checked).
- **Three months (2027-02-14):** all 20 restaurants and bars, plus `baelo-claudia`, `selwo-aventura`, `olvera-castle`, `ronda`, `mercado-de-atarazanas` and `duna-de-bolonia` (hours, prices or access change often).
- **Five months (2027-04-14):** the other beaches, the towns and the remaining places (the default for fact-checked places); beaches are read again before the bathing season.
- Nothing else changed; the app export is unchanged because `next_review_at` is not exported.

## 2026-11-14 - Second source attempt for 21 app places with open facility issues (level A)

- **Read:** 21 places with `visitor_facilities_unverified` (19) or `record_incomplete` (2), in three batches of seven, with `source-reader` (curl, PDF, Playwright). Tavily was not available in the session. Chrome read the Tolox spa and the Malaga cathedral page; andalucia.org gave "Access Denied" there too.
- **Found and written (official sources, quotes in the evidence ledger):**
  - `granada` (Alhambra FAQ): car park with 360 spaces, wheelchair itinerary (value `partial`), toilets, no dogs except guide and assistance dogs.
  - `selwo-aventura` (own site): barrier-free route with steep points (`partial`), adapted toilets, EUR 5 parking with reserved spaces, no pets except assistance animals, food outlets. Issue closed.
  - `el-torcal-de-antequera`: two adapted accesses (wheelchair `partial`), cafe/restaurant confirmed. Only toilets remain open.
  - `antequera`: `cost_level` set to EUR from the Alcazaba price list (5 EUR adults); the Alcazaba is pet friendly (evidence only, the town value stays unknown); booking only stated for groups.
  - `cadiz`, `gibraltar`, `playa-la-malagueta`: evidence added, no values changed.
  - `olvera-castle`: `visit_information` closed (hours were decided by the editor on 2026-11-13); coordinates and driving time stay in `record_incomplete`.
- **Not found:** the remaining fields on all places are closed as `not_found_after_two_attempts` (info), values left unknown and shown as "check before visiting".
- **Not changed:** statuses, categories, tags, family scores. Danish texts are unaffected (the hash covers summary and practical only), 0 stale. The Selwo price conflict (24.90 vs 29.90 EUR) is a separate open point.
- **Still blocked for a later try:** andalucia.org (403 even in Chrome), the Ronda hours PDF (image only), the Antequera dolmen PDFs, the Cordoba ticket site (JavaScript shell).

## 2026-11-14 - Editor list of 14 November answered: three bars archived (owner decisions, list)

Source: https://claude.ai/artifact/AFi2EGnFQEcEM7zUjt6m7y, answers read from collection `editorlist-2026-11-14`.

- **Archived** (`archived` with `review_decision`, date 2026-11-14): `nautic-bar-fuengirola`, `mon-2-sun` and `retrock-bart`. No activity in 2026 after two source attempts; the editor does not know the bars. Names and slugs unchanged; the IDs stay allocated.
- **App:** the export now holds 156 places (156 Danish, none stale). The import does not remove places that leave the export, so the three app rows are hidden as before (as on 2026-11-08 for Los Caños de Meca, Aracena and Palmeral): guide status set to `archived` in `public.recommendations`; the rows are kept.
- My note on the editor list that the bars would disappear from the app at the next import was not correct on its own; the hiding step above is what removes them.

## 2026-11-14 - Editor list of 14 November published (level A; the decisions are the editor's)

- Private list: https://claude.ai/artifact/AFi2EGnFQEcEM7zUjt6m7y (answers stored in the page's collection `editorlist-2026-11-14`). 3 archiving proposals for bars that are in the app but show no activity in 2026 after two source attempts: `nautic-bar-fuengirola` (last own post August 2023), `mon-2-sun` (December 2024) and `retrock-bart` (December 2025). Recommendation preselected: archive all three; the alternatives are keep and retry (a call, visit or message) or ask the family.
- Nothing is changed in the records until the editor has answered.

## 2026-11-14 - Danish texts for the remaining 22 app places (level A)

- The 22 app places that had no Danish text in the repository (so the app kept older Danish texts written in the app) now have Danish texts in `data/app-texts-da.json`, translated from the current English summary, hours and prices. Facts are unchanged; owner choices and source caveats are kept in the text. All 159 app places now take their Danish text from the repository (159 Danish, none stale), so a later change in hours or prices makes the text stale in the export instead of being hidden by an old app text.

## 2026-11-14 - Danish texts for Baelo Claudia and Sevilla (level A)

- After the import, the app still showed old Danish texts for Baelo Claudia (2024 hours, no price) and Sevilla. The app's import keeps Danish texts written in the app when the repository sends only English (`mergeGuide` in the app repo), so a newer English fact does not replace an older Danish text. Danish texts for the two places were added to `data/app-texts-da.json`, so the import now overwrites them. The general problem (other places with only English in the repository but old Danish in the app) is still open.

## 2026-11-14 - Second source attempt for the 21 app places with `source_attempt_not_found` (level A; three archiving proposals go to the editor)

- Second attempt, 13 November: 12 social-media pages and 4 blocked pages were read in Claude in Chrome; 9 official pages went through `source-reader` (two quotes spot-checked against the fetched text).
- **Found and written (evidence with verbatim quotes):** opening hours for Changueiro (own post 19 Oct 2026), Chiringuito Las Dunas (winter hours, Nov 2026), La Terraza de Panda, Bar Burbujas, Groove Music Bar (also free Wednesday jam and food), Café Teatro, Noniná and Red&White (holiday closure 16 Nov-1 Dec 2026). The last three come from old Facebook hours boxes and carry low confidence. Baelo Claudia: 2026 hours, free for EU citizens (EUR 1.50 others, `cost_level` Free), no pets, on-site car park. Sevilla cathedral: hours, EUR 13/14, free under 13, free wheelchair service. Mercado de Atarazanas: hours reconfirmed, no access for reduced mobility (City Council). Speakeasy: concert tickets are table reservations credited to drinks (EUR 56 Friday, EUR 84 Saturday). Boliches-Gaviotas: 2026 accessible zone and lifeguards from 1 June 11:00-20:00 (Ayuntamiento). La Senda del Norte and Groove: `food_available: yes`.
- **Not found after two attempts:** the open warning is closed and replaced by an info issue `not_found_after_two_attempts`; the value stays unknown and the app shows it as unknown. This covers bar prices, Nerja and Sevilla visitor facilities, the Torrecilla permit and parking in Sierra de las Nieves, La Floja's hours, and the admission, parking and access at Duna de Bolonia.
- Duna de Bolonia: the official portal still lists the partial trail closure of 22 September 2026, so a new warning `partial_trail_closure_listed` replaces `trail_closure_unconfirmed`.
- **For the editor list (not decided by Claude):** `mon-2-sun` (last own post December 2024), `nautic-bar-fuengirola` (August 2023, website gone) and `retrock-bart` (December 2025) show no 2026 activity; their `activity_unverified` warnings stay open, and archiving is proposed.
- 9 Danish app texts updated (`data/app-texts-da.json`); `data/app-export/` regenerated (159 places, 135 Danish, none stale). Validation: 220 records, 0 errors, 26 warnings.

## 2026-11-13 - Automatic sign-out wished for later (owner decision, chat)

- When the app becomes a "real" app rather than a page in the browser, it should sign out by itself after a few minutes without use. Not built now; listed under "Åbent" in `docs/project-state.md`. It touches login, so the app change waits for the owner's merge when it is made.
- The owner confirmed that Spørg now uses its own quota. "Log ud" stays as it is for now (it signs out on all devices).

## 2026-11-13 - Trip quota given back; phone logged out (level A, owner report in chat)

- The owner could not make trip plans (5 of 5 used). Those 5 uses were Spørg questions charged to the trip quota before migration 0010 worked. Claude set today's `trip_ai_usage` row for the owner from 5 to 0. Checked as the owner's user: trip quota 0 of 5, Spørg quota 0 of 20.
- Claude also asked PostgREST to reload its schema (`NOTIFY pgrst, 'reload schema'`), since the functions were created directly with SQL.
- The phone went straight to the login page because all of the owner's older sessions are gone; only two from 19:23 and 19:34 remain, while other users' sessions are intact. The app's "Log ud" calls `supabase.auth.signOut()`, whose default scope is global, so signing out on one device signs out all of them. Nothing in today's PWA or update code clears login data. The owner has to sign in again on the phone. Changing sign-out to `scope: 'local'` touches login and waits for the owner's merge (app `AGENTS.md`).

## 2026-11-13 - App import after the editor list (level A)

- `POST /api/import-places?apply=1`: 159 updated, 0 created, 0 skipped (dry run first, same counts). Spot check: `olvera-castle` carries the new tourism-site hours (10:30), `el-oceano-beach-hotel` shows "check before visiting", and `canon-de-las-angosturas` is in the app with status `needs_fact_check`.
- Spørg quota after migration 0010: the owner reported that Spørg still used the trip quota. In the database, `get_ask_ai_quota()` called as the owner's user returns its own quota (20, 0 used), and the published code calls it (the self-test probe reaches the function). Today's 5 trip-quota uses most likely came before the migration ran, or from a page still showing the old quota; the owner was asked to reload the app and try again.

## 2026-11-13 - App migration 0010 applied (level A, owner's merge)

- App repo PR thomasericolesen/callemilano-f388b2be#38 (Spørg gets its own AI quota: 20 questions per person per day, a shared family cap of 60, admins exempt) was merged by the owner. Lovable Publish does not run drizzle migrations, so Claude applied `drizzle/migrations/0010_ask_ai_daily_quota.sql` with the Lovable `query_database` tool in one transaction: table `public.ask_ai_usage` (RLS on, no policies, no grants to anon/authenticated) and the SECURITY DEFINER functions `get_ask_ai_quota()` and `consume_ask_ai_quota()` (execute for authenticated only). The function bodies in the database match the file exactly (md5).
- Remote self-test against `https://callemilano.dk`: all scenarios OK; `spoerg-live` reached `get_ask_ai_quota` without the "migration 0010 not run" warning.

## 2026-11-13 - Retry in Claude in Chrome for the drafts kept on the editor list (level A)

- `canon-de-las-angosturas`: the Benahavís council page (dated 14 June 2021, blocked for automated reading) was read in Claude in Chrome. It gives hours 10:00-20:00 with the last descent at 19:00, level 1 canyoning, under-14s accompanied by an adult, pets forbidden. Record: schedule, `dog_friendly: no`, visitor link, evidence (medium confidence, source is from 2021) and `facts_partly_checked`; `draft` to `needs_fact_check` (identity clear, official evidence), so it enters the app with the "Ikke faktatjekket" label (159 places, 135 Danish). Price, duration, parking and accessibility are still open.
- `castillo-de-monda`: the hotel's own restaurant page (Albacar, 6th floor, table booking) was read; it gives no hours, prices or rule for non-resident diners, and the menu link led to the wine list. Evidence and visitor link added; stays `draft`.
- `paseo-maritimo-marbella`: not retried yet; the right Turismo Marbella page for this section has still to be found. Stays `draft`.
- Danish text for `canon-de-las-angosturas` added to `data/app-texts-da.json`.

## 2026-11-13 - Editor list of 13 November answered (owner decisions, list)

Source: https://claude.ai/artifact/EpwDTtUv1wLvgu1u5Yy5Jn, answers read from collection `editorlist-2026-11-13`.

- **Conflicts decided:** `el-oceano-beach-hotel`: write "check before visiting" and leave the Sunday menu prices unknown (noted in `cost_basis`). `olvera-castle`: use the Olvera tourism site's hours (Tuesday to Sunday, split hours, winter 10:30-14:00 / 16:00-18:00, summer 10:30-15:00 / 16:00-20:30), replacing the 2026-11-11 tourist-office hours. `tarifa`: the castle office phone is 607 984 871. The three blocking `source_conflict` issues are closed with an evidence entry each.
- **Archived** (`archived` with `review_decision`): `moga-la-cala`, `sky-bar-veramar`, `rio-grande-coin`, `senda-litoral-malaga-oeste`. All were drafts, so none was in the app. `sould-park-fuengirola` was archived earlier today after the editor's chat message (see the entry below); the list answer "keep and retry" was given before it and is superseded by that later chat decision.
- **Keep and retry:** `castillo-de-monda`, `canon-de-las-angosturas`, `paseo-maritimo-marbella` stay `draft` and are read again with Claude in Chrome.
- **App:** the Danish texts for `olvera-castle` and `el-oceano-beach-hotel` were rewritten in `data/app-texts-da.json` (new hash), so the export shows them in Danish (134 Danish, none stale). `data/app-export/` regenerated; the app needs an import (2 places changed).

## 2026-11-13 - `sould-park-fuengirola` archived (owner decision, chat)

- The editor said the place is Sould Park Miramar and asked to try the operator's Facebook and Instagram again, and to archive if that failed. Read in Claude in Chrome: `souldpark.com/ocio/` lists "FUENGIROLA / CC MIRAMAR" but its tab only opens a map link; Instagram `souldpark_es` and Facebook `souldpark` name Fuengirola as a location but give no hours, prices, age rules or attractions. (My earlier statement on the editor list that the operator's site had no Fuengirola venue was wrong.)
- The record is `archived` with `review_decision` (date 2026-11-13, source: chat). It was a draft, so the app is unchanged (158 places). Name and slug are not changed; the ID stays allocated. Removed from the editor list's open items by the decision; the other 7 archiving proposals and 3 conflicts still wait.

## 2026-11-13 - Editor list of 13 November published (level A; the decisions are the editor's)

- Private list: https://claude.ai/artifact/EpwDTtUv1wLvgu1u5Yy5Jn (answers stored in the page's collection `editorlist-2026-11-13`). 11 items: 3 source conflicts (`el-oceano-beach-hotel` Sunday menu prices, `olvera-castle` opening hours against the 2026-11-11 choice, `tarifa` office phone) and 8 archiving proposals (the drafts that failed two source attempts). Recommendation preselected on each: archive 5 (`moga-la-cala`, `sky-bar-veramar`, `rio-grande-coin`, `senda-litoral-malaga-oeste`, `sould-park-fuengirola`); keep and retry 3 that have an official source the tools could not read (`castillo-de-monda`, `canon-de-las-angosturas`, `paseo-maritimo-marbella`).
- Nothing is changed in the records until the editor has answered. Answers will be written to the records with date and a link to the list, and the blocking `source_conflict` issues closed then.

## 2026-11-13 - Warnings and info on app places: first batch of source reading (level A; conflicts go to the editor)

- Scope: the 45 app places with fact-type warnings or info (69 issues). The 38 editorial issues (audience, family ratings, tags and category, scope, owner has not visited, overlaps) are not source questions and stay for the editor. Three batches of 15 went through `source-reader` and `record-writer` (WebSearch instead of Tavily, which was not available to the subagents).
- Result: 21 places got one new evidence entry each (official sources only; Frigiliana at low confidence because the page is dated 2016); no field values were set and no warning was closed, because no quote fully answered an open issue. 21 places with nothing usable (login wall, no official page, blocked) got an info issue `source_attempt_not_found`; a second failed attempt closes their open facts as "not found". `el-torcal-de-antequera` was skipped on purpose: its official page showed injected spam text and needs a second source.
- New blocking `source_conflict` issues for the editor, none resolved by Claude: `el-oceano-beach-hotel` (Sunday menu gives both 49/59 EUR and 45/55 EUR on the same page; the fillet steak is above the recorded main-course range), `olvera-castle` (official page gives Tue-Sun seasonal hours, the record says daily), `tarifa` (official page: office phone 607 984 871, the record says 607 684 871). Statuses unchanged.
- Other points for later: Selwo's official page says "from 24.90 EUR", the record has 29.90 EUR box office; Gibraltar's cable car notice "Closed For Refurbishment" has no date.
- `record-writer` rewrote the YAML of 21 records in its own format; parsed values are unchanged except `evidence`, `review_issues` and `updated_at` (checked by comparing the parsed data), so the diff is large but semantic changes are small. Validation: 220 records, 0 errors, 26 warnings; all tests pass. `data/app-export/` regenerated (only dates changed), no app import needed.

## 2026-11-13 - Second source attempt for the 8 drafts (level A; archiving proposed, not done)

- The 8 drafts (`castillo-de-monda`, `canon-de-las-angosturas`, `moga-la-cala`, `sky-bar-veramar`, `paseo-maritimo-marbella`, `rio-grande-coin`, `senda-litoral-malaga-oeste`, `sould-park-fuengirola`) went through the pipeline again (source-reader, then own checks). No usable official source was found for any of them: Castillo de Monda's own site only shows a "Book your table" button; Sould Park's site lists no Fuengirola venue; the other six have no readable official page (only guides and booking sites, which are not recorded as facts).
- No facts were added and no status changed; all 8 stay `draft`. Each record got a `second_source_attempt_failed` issue (owner: editor) with what was tried. Under the rule "facts too hard to obtain, the place drops off" they go on the next editor list as archiving proposals; nothing is archived until the editor says yes.
- Validation: 220 records, 0 errors, 26 warnings (unchanged). Catalogue regenerated.

## 2026-11-13 - `docs/project-state.md` rewritten (level A, documentation only)

- The file was from 2026-10-05 (30 records, the 30 km straight-line rule, an obsolete next-actions list). Rewritten in Danish from the current records, layers, tools and status file; the next-actions list now points to the newest `docs/status-*.md`. No rules or data changed.

## 2026-11-11 (night) - Claude Code may run `gh pr merge` (owner decision, chat)

- `.claude/settings.json` now allows `Bash(gh pr merge *)`. Claude Code's own safety filter had blocked merges although `AGENTS.md` ("Push, PR, merge and import") already gives standing permission for level A/B work. The rule in `AGENTS.md` is unchanged: level C/D changes still wait for the editor.
- Same day, app repository: Claude may merge and publish its own app changes under conditions written in the app's `AGENTS.md` (owner decision in chat).

## 2026-11-11 (night) - `check-restaurants` accepts `konverteret` and `fravalgt` (level A, tooling only)

- The row statuses `konverteret` (the row became a place record; slug in `notes`) and `fravalgt` (the owner deselected it) were introduced on 2026-11-02 and are listed in `docs/trip-planner-agents.md`, but the check in `tools/trip_restaurants.py` only allowed `aktiv`, `skal tjekkes` and `lukket`. All 26 rows (22 `konverteret`, 4 `fravalgt`) were reported as errors. The check now allows all five values; `check-restaurants` passes.
- Not an editor item after all: no change to `data/restaurant-directory.csv`. Trip plans were never affected, since they read only `aktiv` rows and take restaurants from the place records.

## 2026-11-11 (night) - Language rule in `AGENTS.md` (owner decision, chat)

- New section "Language" in `AGENTS.md`: Claude reports to the editor-of-record in Danish (chat replies, reports, editor lists, weekly summaries, PR descriptions and status files). Code, file names, commands, schema values and the English record texts are unchanged. The owner asked for Danish reports in chat and for the rule in `AGENTS.md` on 2026-11-11.

## 2026-11-11 (night) - `CLAUDE.md` added (owner request in chat)

- New `CLAUDE.md` at the repository root imports `AGENTS.md` (`@AGENTS.md`), so every Claude Code session loads the project rules, also on the web, in the cloud and on the phone. It adds no rules of its own: it points to `docs/project-state.md`, the newest status file, the change log and the documentation map, points to the language rule, and lists what exists only on the owner's Mac (import token, Claude in Chrome, `trips/`).
- `CLAUDE.md` needs no daily update: the daily state lives in `docs/change-log.md` and `docs/status-*.md`, which reach git through PRs.

## 2026-11-11 (night) - `docs/` sorted into subfolders (level B, owner's yes in chat)

- 69 files moved with `git mv` into `docs/history/` (old status files and handovers, superseded reviews and engine analyses), `docs/decisions/` (dated intake, selection and decision notes), `docs/product/`, `docs/engine/` and `docs/content/`. Everything `AGENTS.md`, the agents, the skills and the tools point to stays at the top of `docs/`, so `AGENTS.md` is unchanged.
- All references were rewritten: 375 `docs/...` paths (including GitHub source URLs in the place records' evidence and in `data/*.csv`), 44 bare file names inside `docs/` and 25 Markdown links. A check of every text file finds no reference to a missing file (also none before the move).
- `docs/README.md` rewritten as a map of the new layout. Going forward, the newest `status-*.md` stays at the top and the previous one moves to `history/`.
- Verified unchanged: `places.py validate` output, `data/place-catalog.csv` and `data/app-export/*.json`. All tests pass. In 68 place records only file paths to moved documents changed, in evidence `source_url` and `notes`; no values, statuses or dates.

## 2026-11-11 (night) - `tools/trip.py` split into modules (level A, tooling only)

- `tools/trip.py` (1,067 lines) is now only the command line; the logic moved verbatim into `trip_core.py` (place list, routes between stops, fetching), `trip_weather.py`, `trip_traffic.py`, `trip_restaurants.py`, `trip_plan.py` (holidays, opening status, the plan) and `trip_render.py`. Commands and options are unchanged, so `/turforslag`, `/aabningstider`, `/restaurant-indsamling` and the agents run as before.
- Verified: all 69 definitions are identical to the original (compared as syntax trees); `LOCAL_MAX_MIN` now comes from `tools/common.py` (same value, 30). `places`, `nearby`, `restaurants`, `hours-status`, `coverage`, `check-restaurants` and `plan` give the same output before and after (only DGT's live publication time differs). All 7 tests pass.
- Known, unchanged at the time: `check-restaurants` reported every row in `data/restaurant-directory.csv` as an error; fixed the same day (see the entry above).

## 2026-11-11 (night) - Shared helpers for the tools (level A, tooling only)

- New `tools/common.py` holds the project paths, the origin point (Casa de la Familia), record reading (`load_front_matter`), `haversine_km` and drive-time parsing (`minutes`). `places.py`, `app_export.py`, `trip.py`, `route_check.py` and `intake.py` import from it instead of each keeping their own copy; `places.py` still exposes `CASA_LAT`/`CASA_LON` and `load_front_matter` for older imports.
- Fixed: drive times in Google's format "2 hours 35 mins" were read as 120 minutes by `app_export.py` (the "mins" part was dropped) and as unknown by `trip.py` (it only read "NN min"). Both now use `common.minutes`, which reads 155. No exported place was affected today: the 18 records with hour-long drives are archive or lack coordinates.
- Verified unchanged: `places.py validate` output, `data/place-catalog.csv`, `data/app-export/*.json`, the Danish to-do list, `trip.py places` and `trip.py check-restaurants` are byte-identical before and after.
- New tests in `tests/test_common.py`; all tests run with `python3 -m unittest discover -s tests` (now in `README.md`).
- Housekeeping: a macOS text clipping under `Claude.md/` removed from git (the file stays on disk) and `*.textClipping` ignored. `README.md` now states the 30-minute drive rule (owner decision 2026-10-29) instead of the old 30 km straight-line rule.
- No change to records, schema, statuses or `AGENTS.md`.

## 2026-11-11 (night) - First editor list answered: 7 conflicts decided, 19 drafts archived

- Answers from the first editor list (Artifact "Redaktørlisten", https://claude.ai/artifact/C1Lu1WExnpBw8YRw5K1Jrc): the owner decided all 26 items, each as Claude recommended, with no notes. Evidence entries (owner's judgement, medium confidence) added to the records.
- Conflicts decided: `old-swiss-house-fuengirola` hours stay unknown ("check before visiting"; only Tuesday closed is consistent), `olvera-castle` tourist-office hours (winter 10:00-19:00, summer 10:00-20:00), `frigiliana` museum hours (Saturday 10:00-14:00 and 16:00-20:00), `ronda` official PDF (Tue-Fri 9:30), `castillo-de-colomares` 3.50 €/2.50 € (`cost_level` `€`, no longer Unknown), `crocodile-park-torremolinos` hours page (Sept-June 11:00-17:00, July-August 11:00-18:00; now in `visit_information.schedule`), `zero-latency-miramar` age text (no fixed minimum age, minimum height per game, the chain recommends 13+, call before bringing children). The conflict issues were closed; the three conflicts that had been closed in bulk on 2026-11-11 are now resolved by decision.
- Archived (`archived`, `review_decision` filled in): `cares`, `conil-de-la-frontera`, `cueva-de-los-arcos`, `miradouro-da-serpente-do-medal`, `roca-foradada`, `salt-de-la-coromina` (incomplete drafts without ID, outside the layers) and `casa-carmen-miramar`, `casa-manuel-de-la-lonja`, `chiringuito-central-beach-estepona`, `courtside-by-wissler`, `el-andaluz-de-la-malagueta`, `el-mirador-del-golf`, `juanito-juan`, `norte-puerto-banus`, `pena-al-tranco`, `restaurante-el-golf-mijas`, `restaurante-la-escollera-estepona`, `singh-doner-kebab`, `sol-y-sombra-mijas`. None was in the app, so the export is unchanged in size (158).
- Tooling: `tools/places.py` now checks an archived record without an ID (the six stubs) like a draft: missing ID, coordinates and route time are warnings, not errors. Archived records with an ID are checked as before. No schema change.
- Danish app texts rewritten for the four places whose English text changed (`data/app-texts-da.json`); no stale Danish texts remain.
- Eight drafts wait for the next list because a new source attempt comes first: `castillo-de-monda`, `canon-de-las-angosturas`, `moga-la-cala`, `sky-bar-veramar`, `paseo-maritimo-marbella`, `rio-grande-coin`, `senda-litoral-malaga-oeste`, `sould-park-fuengirola`.

## 2026-11-11 (night) - Coordinates filled for three records (level A)

- `mercado-de-atarazanas` (36.718434, -4.424058), `olvera-castle` (36.9356854, -5.2675481) and `palmeral-de-las-sorpresas` (36.7183501, -4.415388): place points read in Google Maps in Chrome (identity and position only), evidence entry added, and the `blocking` issue `schema_blocking_unknowns` (unknown coordinates) closed on all three. Not an editor decision: the coordinates are a Google Maps identity fact.
- The two real editor items that remain on those records are conflicts (Olvera Castle winter closing time 19:00 vs 20:00) and go to the editor list.

## 2026-11-11 (night) - Import without a browser login (owner decision)

- App repo PR thomasericolesen/callemilano-f388b2be#29 (merged, published): new route `POST /api/import-places` with a Bearer token, the import logic moved to `recommendations-import.server.ts` (`dryRun` option; the admin button uses the same function), new table `public.import_tokens` (only the SHA-256 of the token, RLS without policies). The migration was not applied automatically, so the table was created with the migration's SQL through the Lovable connector (RLS on, no policies, like `selftest_tokens`).
- Token: created on the owner's Mac in `~/.callemilano-import-token` (mode 600), only the hash inserted; expires 2027-02-09. Tested: no or wrong token gives 401; dry run 158 updated, 0 created, 0 skipped; real import `?apply=1` 158 updated; the database shows `last_used_at` set. The first Lovable publish ran before Lovable had fetched the merge, so it was published a second time.
- Chrome is now only needed for the Facebook/Instagram and Google Maps checks. `AGENTS.md` and `docs/multi-agent-workflow.md` updated.

## 2026-11-11 (night) - Seven restaurants fact-checked and lifted (level A, editor workflow)

- First run under the new editor workflow. The seven restaurants still labelled "Ikke faktatjekket" (`el-higueron-fuengirola`, `freiduria-el-choco-fuengirola`, `gali-gali-fuengirola`, `los-enebros-fuengirola`, `mias-pizzorante-fuengirola`, `old-swiss-house-fuengirola`, `sollo-fuengirola`) were read again from their own websites (`tools/intake.py fetch`; Tavily extract for El Choco, Sollo and El Higuerón's carta, which curl cannot read). All quotes recorded in the evidence were checked verbatim against the fetched text. All seven moved from `needs_fact_check` to `needs_editorial_review`; the stale `facts_not_checked` and `facts_partly_checked` issues were closed (what could not be found stays unknown).
- New facts: El Higuerón regular hours (Monday closed; Tuesday-Saturday 12:30-00:00; Sunday 12:30-18:00), phone and mains 21-43 € (`€€`, with info issue `cost_level_borderline`); the earlier schedule text came from the 24 and 31 December notices and was replaced. El Choco Tuesday-Sunday 13:00-16:00 and 20:00-23:00 (days read in order Monday to Sunday; medium confidence). Los Enebros full weekly hours; median main 23,50 € (32 mains), `€€`, `cost_level_borderline` closed. Mia's phone and booking contact. Sollo `cost_level` `€€€€` (only a 180 € tasting menu is shown). Gali Gali unchanged facts, re-read.
- Source conflict for the editor list: `old-swiss-house-fuengirola` own website contradicts itself on Wednesday lunch and Sunday (new warning `opening_hours_conflict`, owner `editor`); hours stay unset.
- Danish app texts rewritten for the four places whose English texts changed (`data/app-texts-da.json`); no stale Danish texts remain. App export regenerated: 158 places, 103 `approved`, 55 `needs_editorial_review`, none `needs_fact_check`; the app needs a new import.
- Chrome was not connected during this run; none of this needed it, because the sources were own websites.

## 2026-11-11 (late night) - Editor workflow written into the rules (owner decision)

- Reviewed with the owner on 2026-11-11 and written into `AGENTS.md` (section "Editor workflow"), `docs/multi-agent-workflow.md` (section "Editor workflow", with the full decision table) and `docs/place-schema.md` (status note). Decided: four levels (A Claude alone, B Claude and informed, C the editor decides, D only the editor); a weekly editor list (only when there is something); standing permission for Claude to push, open PRs with `gh`, merge and import changes made only of A/B work, with C/D changes waiting for the editor's answer; Claude closes `warning` and `info` issues, conflicts and `blocking` go to the editor; archiving proposals go on the list and happen only after a yes; monthly freshness job; `approved` retired as a step (`needs_editorial_review` is the end station, existing `approved` records unchanged, no schema change).
- The owner confirmed that nothing is missing from the decision table.
- `gh` is installed and logged in on the owner's Mac (`thomasericolesen`); GitHub work no longer needs Claude in Chrome. The import in the app and the Facebook, Instagram and Google Maps checks still do.

## 2026-11-11 (night) - 90 owner-reviewed places set to approved (owner decision)

- Owner decision 2026-11-11: places the owner reviewed himself on both checklists (family ratings 2026-11-10, tags 2026-11-11) and that are fact-checked are `approved`. 90 records (all in the app export; each has `review_decision`: approved, reviewer Eric Olesen, date 2026-11-11; `last_reviewed_at` 2026-11-11, `next_review_at` 2027-04-11).
- `approved` cannot carry open `review_issues` (validator and `AGENTS.md`). 87 of the 90 had issues; on the owner's instruction all 130 were closed (removed) with the approval, including `price_conflict`, `opening_hour_conflict` and `minimum_age_conflict` (conflicting source information) and 36 `facts_partly_checked`. The gaps and conflicts stay recorded in the evidence ledger and `notes`; they are no longer listed as open issues.
- App export now: 103 `approved`, 48 `needs_editorial_review`, 7 `needs_fact_check`. The app labels `approved` and `needs_editorial_review` alike ("Faktatjekket"); `places.json` regenerated, so the app needs a new import.

## 2026-11-11 (night) - Fact-checked places raised to needs_editorial_review (owner decision)

- Owner decision 2026-11-11: the "Ikke faktatjekket" label stood on 126 of 158 app places although most had been through the agent fact-check, which ends at `needs_fact_check` (agents never set a higher status). 119 records in the app export with official evidence (`official_venue`, `government`, `official_tourism` or `official_transport`) and without an open `facts_not_checked` issue moved from `needs_fact_check` to `needs_editorial_review`, which the app shows as "Faktatjekket" (owner decision 2026-11-10). By category: Restaurants 47, Family activities 33, City 15, Excursions 11, Beaches 10, Nature 3.
- Still `needs_fact_check` in the app (label stays): `el-higueron-fuengirola`, `freiduria-el-choco-fuengirola`, `gali-gali-fuengirola`, `los-enebros-fuengirola`, `mias-pizzorante-fuengirola`, `old-swiss-house-fuengirola`, `sollo-fuengirola` (open `facts_not_checked`). 14 `needs_fact_check` records outside the app (archive) are unchanged. Records with `facts_partly_checked` were raised too; their remaining gaps are noted in their evidence and notes, not in the status.
- `data/app-export/places.json` regenerated (158 places: 138 `needs_editorial_review`, 13 `approved`, 7 `needs_fact_check`); the app needs a new import.

## 2026-11-11 (night) - Tags set from the owner's tag checklist

- Owner checklist (Artifact `Tag-tjekliste`, https://claude.ai/artifact/DZv9cLLQ1BEcYs3NeewdEF): 97 active places whose tags had never been assessed (`status` needs_fact_check or later, listed on the 2026-11-10 family-rating checklist). The owner reviewed all 97 on 2026-11-11; 96 changed from the imported estimates, 1 unchanged. Choices were read back from the artifact's database and written to `tags` in schema order, with one evidence entry per record (`field: tags`, owner's own judgment, confidence medium).
- Result: Half day 81, Premium 54, Restaurant 42, Free 36, Adventure 32, Rainy day 28, Historic town 16, Viewpoint 15, Full day 15, Beach 14, Nature 11, Hiking 3, Museum 2, Overnight 0. No place has no tags. No conflicts (one of Half day/Full day/Overnight, at most one of Free/Premium). Every record in `Restaurants` has `Restaurant`; every `Beaches` record has `Beach`. `Restaurant` is also on `monda`, `puerto-deportivo-estepona`, `puerto-banus`, `puerto-marina-benalmadena` and `mijas-golf`, and `Beach` is on nine non-beach places (e.g. chiringuitos, `paseo-maritimo-fuengirola`, `dunas-de-artola`), as chosen by the owner; the schema allows tags beside the category.
- `data/app-export/places.json` regenerated (themes, duration and `rainy_day` follow the tags); the app needs a new import.

## 2026-11-11 (night) - Open issues closed, three more drafts archived (owner decision)

- Owner decision 2026-11-11: the open issues do not matter much for the whole; close them. Removed from `review_issues`: `hours_and_prices_unverified` on `venta-la-morena`; `facts_partly_checked` on `meson-salvador-fuengirola` and `vegetalia-fuengirola`; `family_suitability_not_assessed` on `mijas-golf`, `playa-de-la-rada-estepona`, `puerto-marina-benalmadena`, `playa-puerto-banus`, `coin`, `la-lobezna-estepona` and `sollo-fuengirola`. Field values are unchanged: unassessed family scores stay as they were, cost_level stays Unknown or from the secondary source. Kept: `cost_level_secondary_source` on `venta-la-morena` (info, says the price band comes from Tripadvisor) and issues of other kinds (e.g. `facts_partly_checked` on `coin`, `la-lobezna-estepona`, `sollo-fuengirola`, `lifeguard_season_unchecked`, `green_fees_unknown`).
- `archived` under the same rule as the six restaurant drafts: `casas-cuevas-almagruz`, `molino-del-santo`, `taberna-mar-de-alboran-estepona` (drafts with no verified facts). Export still 158 places; `places.json` regenerated (issue changes), so the app needs a new import.

## 2026-11-11 (late) - Toll roads rule for driving times (owner decision)

- Owner decision 2026-11-11: driving times use Google Maps' main figure (the fastest route it proposes) and do not avoid toll roads; the difference is a few minutes and is small next to local traffic. This replaces the owner's earlier standing setting "toll roads avoided" (2026-10-29) for new and re-checked records. Added to `AGENTS.md`. The three figures the owner measured on 2026-10-29 (`antequera`, `el-torcal-de-antequera`, `caminito-del-rey`) stay replaced by the 2026-11-11 figures (66, 73 and 63 min); same-day toll-free alternatives were about 71, 81 and 63 min. `tools/route_check.py` already follows this rule.

## 2026-11-11 (late) - Open points via Facebook, "Ved ikke" places, drive times re-checked (owner request)

- Read-only in Claude in Chrome (owner logged in to Facebook and Instagram). Instagram search returned nothing usable; Facebook pages used. No facts written to the three fact-checked restaurants because nothing new fits a field: `venta-la-morena` (only a "Menú del día" from 29 June 2020, no prices), `meson-salvador-fuengirola` (only company, Christmas and group menus at 38-55 EUR per person and hour notices; nothing for a regular carta), `vegetalia-fuengirola` (daily menu posted 11 Nov 2026 so the place is active; ovo-lacto vegetarian buffet, reviews mention pricing by weight; no prices or hours). Their issues stay open.
- The 10 "Ved ikke" places: Facebook/Instagram do not answer the family-suitability question (they describe the business, not child suitability), so no family ratings were changed. Pages found: `la-lobezna-estepona` ("Bar Restaurante Andaluz con un toque Latinoamericano", no hours or menu), Mijas Golf (course page, "Moderat", 92 % recommended). None found for Sollo; beaches and Coín are municipal. Per the 2026-11-11 rule the draft restaurants (`casas-cuevas-almagruz`, `molino-del-santo`, `taberna-mar-de-alboran-estepona`) are candidates for archive; not archived yet.
- Drive times re-checked in Google Maps (main figure, tolls not avoided, live traffic about 09:51 on 2026-11-11) for the eight of the 26 old `route_check` records that are in use: `antequera` 75 -> 66 min, `caminito-del-rey` 65 -> 63, `el-torcal-de-antequera` 85 -> 73, `malaga` 45 -> 48, `marbella-old-town` 35 -> 35, `selwo-aventura` 46 -> 47, `mercado-de-atarazanas` 37 -> 42, `palmeral-de-las-sorpresas` 37 -> 40. The first three were measured by the owner on 2026-10-29 with "toll roads avoided" as the owner's standing setting; the new figures replace them. No `Tæt på` / `Dagsture` grouping changes (Caminito stays above 60 min). The other 18 records are far outside the layers (over 2.5 h, no layer) and stay as archive. `data/app-export/places.json` regenerated (drive times); the app needs a new import.

## 2026-11-11 (evening) - Six restaurant drafts archived (owner decision)

- Owner decision 2026-11-11: if getting usable facts for a restaurant is too much effort, it simply drops off the list; we already have enough restaurants, and the same rule applies to the remaining places.
- `archived` (kept as records, IDs stay allocated, `review_decision` filled in): `da-vinci-los-boliches`, `fosters-hollywood-miramar`, `burger-king-miramar`, `the-good-burger-miramar`, `monnalisa-fuengirola`, `antonio-playa-fuengirola`. All were drafts, so the app export is unchanged (158 places). Facts found for Da Vinci (Facebook page: Av. de los Boliches 95, +34 632 38 78 52; both websites dead) are in this entry only and not in the record.
- Not archived: `venta-la-morena`, `meson-salvador-fuengirola`, `vegetalia-fuengirola` (fact-checked, shown in the app; menu or price still missing, issues stay open).

## 2026-11-11 - route_check.py fixed (owner request)

- `tools/route_check.py` now follows the project conventions: toll roads are not avoided (Google Maps' main figure, owner decision 2026-10-29), origin is the AGENTS.md constant 36.5356875,-4.6626875 (same as `tools/places.py`), and durations are written as "15 min" / "1 hour 5 min". The Maps link and the source text no longer say "toll roads avoided". Not run against the live API in this session (no API key available); compiled and the formatting and origin checked locally.
- Records written by the script on 2026-11-01 still carry the old settings (26 with "toll roads avoided" in `source`, 18 with "mins" and the old origin 36.5357505,-4.6627914, e.g. `zumaia`, `aracena`, `bellver-slot`). They are not changed; re-check with `--slugs ... --force` when those places are needed.

## 2026-11-11 (afternoon) - Own-source retries, four restaurants (owner request)

- Read-only in Claude in Chrome. `da-vinci-los-boliches`: own site still fails with a DNS error. `fosters-hollywood-miramar`: still blocked (Imperva, Access denied, Error 15), not bypassed. `burger-king-miramar` and `the-good-burger-miramar`: only national brand pages, no location page, hours or menu prices. No facts were added; the `no_readable_own_source` issues stay open with the retry date. Facebook/Instagram login was not needed.

## 2026-11-10 (late night) - Family ratings, second and final pass

- Second pass on the same owner checklist: 46 more places written (`family_score`, `energy_level`, `age_groups` = groups rated high or medium; evidence as in the first pass). No first-pass answers were changed.
- `family_suitability_not_assessed` closed for 39 of them. Still open where the owner answered "Ved ikke": `alora`, `chiringuito-central-beach-estepona`, `juan-playa-fuengirola` (small children) and `casas-cuevas-almagruz`, `coin`, `la-lobezna-estepona`, `molino-del-santo` (all four groups).
- Final pass (same day): the owner answered the last 13 places and filled in the three small-children "Ved ikke" answers (`alora`, `chiringuito-central-beach-estepona`, `juan-playa-fuengirola`), which closes their issue. All 110 checklist places now have owner ratings.
- `family_suitability_not_assessed` stays open on 10 checklist places with "Ved ikke": `mijas-golf`, `playa-de-la-rada-estepona`, `puerto-marina-benalmadena`, `playa-puerto-banus`, `casas-cuevas-almagruz`, `coin`, `la-lobezna-estepona`, `molino-del-santo`, `sollo-fuengirola`, `taberna-mar-de-alboran-estepona`.

## 2026-11-10 (night) - Family ratings from the owner checklist

- Owner checklist (Artifact `familievurderinger`, 110 places with `family_suitability_not_assessed`, status `needs_fact_check` or later or in `data/layer-membership.csv`, archive skipped). The owner answered 51 places on 2026-11-10 (partial pass).
- Written to the 51 records: `family_score` (four keys), `energy_level`, and `age_groups` = the groups rated high or medium. Evidence: owner's own knowledge, callemilano-tjekliste, confidence medium; owner notes quoted in the evidence claim.
- `family_suitability_not_assessed` closed for 47 places. Still open, with an updated description, where the owner answered "Ved ikke": `mijas-golf`, `playa-de-la-rada-estepona`, `puerto-marina-benalmadena` (all four groups) and `playa-puerto-banus` (small children, children).
- Tags were part of the closed issue but were not assessed on the checklist; they stay as they were. The remaining 59 places stay open for a later pass on the same page.

## 2026-11-10 (evening) - Danish app texts and route_check.py (owner request)

- Danish app texts for `kamura-sushi-fuengirola`, `meson-salvador-fuengirola`, `vegetalia-fuengirola` and `la-tagliatella-miramar`; stale texts refreshed for El Cachalote, Casa Esteban and La Sierra. Export: 134 of 158 places in Danish, 0 stale.
- Added `tools/route_check.py` (owner approved committing it): fills missing driving times from Casa de la Familia with the Google Routes API (computeRouteMatrix); dry run by default, `--apply` writes to `docs/places/`, `--force` overwrites. Key from `GOOGLE_MAPS_API_KEY`. Known deviations to fix before use: avoids tolls (existing records do not), origin 36.5357505,-4.6627914 differs from the AGENTS.md constant, writes "15 mins" instead of "15 min". Overlaps only partly with `tools/trip.py`, which checks between-stop routes and does not write records.

## 2026-11-10 (afternoon) - Fact-check via Facebook/Instagram and own sites in a real browser

- Read-only in the owner's logged-in Chrome (Claude in Chrome), per the owner decision of 2026-11-09. Raw notes kept in the session; quotes and URLs are in each record's evidence.
- `la-sierra-restaurante` €€ -> € (own IG menu, autumn 2024: median main 15 €; borderline, menu may be outdated). `kamura-sushi-fuengirola` draft -> needs_fact_check, €€ (own carta: median sushi set 21 €) and hours from the own website.
- draft -> needs_fact_check with contacts/hours: `meson-salvador-fuengirola` (Mon-Sat 8:30-23:00, Sun closed; undated FB notices), `vegetalia-fuengirola` (buffet, address, phone), `la-tagliatella-miramar` (weekly hours from the official page). Export now 158 places; the four new ones have no Danish app text yet.
- `heladeria-casa-esteban-fuengirola`: Fuengirola shop stays open in winter (IG 2026-11-09); hours still unknown. `venta-la-morena`: contacts and a 15-30 June holiday closure; still no menu. `chiringuito-el-cachalote`: hours for season 2026; menu still 'BORRADOR'.
- `casa-carmen-miramar`: own website is compromised (spam injection); `links.official_website` set to null with issue `official_site_compromised`.
- Still no usable own source: Da Vinci (DNS), Foster's Hollywood (Incapsula block), Monnalisa and Antonio Playa (no Facebook page). Burger King and The Good Burger not checked.

## 2026-11-10 - Approval rule: fact-checked counts as approved; new app labels (owner decision)

- Owner decision: a record that has passed fact-check (`needs_editorial_review`) counts as approved for use in the app and in trip plans. The editor-of-record no longer signs off each record in advance; approval is a running process driven by family feedback in the app. Statuses in the records are unchanged.
- Labels in the app (app PR in callemilano-f388b2be): only places that are not fact-checked carry the amber label "Ikke faktatjekket"; fact-checked places get a discreet grey "Faktatjekket"; green is reserved for "Familien anbefaler"; "Tjek før besøg" moves to its own colour (rose). The section "Familiens forslag" is renamed "Andre mulige steder" (it lists places without trip data, not places the family suggested). The children's-age field now opens the normal phone keyboard, so "5, 10" can be typed.
- Updated: `AGENTS.md` (new section), `docs/multi-agent-workflow.md`, `docs/place-schema.md`, `docs/trip-planner-agents.md`, `.claude/agents/ecco.md`, `tools/trip.py` (no "udkast" note for fact-checked stops) and the `tools/app_export.py` docstring.
- Housekeeping: two duplicate local clones of this repo (`~/CalleMilano` and `Documents/ChatGPT/callemilano/callemilano-content`) were moved to the Trash; work continues in `~/Desktop/callemilano`.

## 2026-11-08 (night) - Three family suggestions fact-checked (owner request)

- The three `nyt_sted` items on the owner's feedback list (UTOPÍA and Venta los Condes from Eric, Heladería Casa Esteban from Christian) were closed in the app; the places already existed as drafts.
- `utopia-la-cala` -> `needs_fact_check`: hours (Wed-Sun 17:00-02:00), address, phone, booking, kids' section and burger prices (median 16,50 €; burger page verified from a rendered PDF) -> `€` with `cost_level_borderline` (no drink prices).
- `venta-los-condes` -> `needs_fact_check`: hours (Tue-Sun 13:00-22:00), phone/WhatsApp booking, kids' menu 9 €, grilled mains 21-59 € (median about 31 €) -> `€€` (menu read by Firecrawl from an image PDF, low confidence).
- `heladeria-casa-esteban-fuengirola` -> `needs_fact_check`: Fuengirola shop at Paseo Marítimo Rey de España 26, phone, from the shop's own Instagram/Facebook (search excerpts); hours and prices still open. Recommendation attribution corrected to Christian.
- Danish app texts for all three. Export 154 places, 130 in Danish. Note: the subagent still had the pre-switch tool list and used Firecrawl (which has credits again); Tavily could not open these PDFs.

## 2026-11-08 (late evening) - Owner answers to the decision list

- Setenil and Zahara: no call to the tourist offices. The towns are free to walk; the ticketed castles get approximate prices from travel sites (Setenil about 2 EUR combined ticket; Zahara 3,50 EUR adult, free under 4) with a "check online before going" note. Issues `hours_prices_missing` and `tower_hours_prices_unverified` closed; info issue `sight_prices_unofficial` added.
- Juan Playa stays €€; Café NOMAD stays € (`cost_level_borderline` closed on both).
- Old Swiss House: the owner's screenshot of the own website settles the conflict: Tuesday closed, Wednesday dinner only, Monday and Thursday-Sunday lunch and dinner; address Calle Marina Nacional 28 (Google lists 26). `source_conflict` closed. Danish app texts for Old Swiss House and Zahara refreshed.
- Tavily replaces Firecrawl (no credits): `source-reader`, `alpha`, `charlie`, `docs/agent-pipeline.md` and `.claude/settings.json` now use `tavily_search` / `tavily_extract`; `tools/intake.py fetch` marks blocked pages `needs_extract` instead of `needs_firecrawl`.

## 2026-11-08 (late evening) - Price bands from guest menu photos (owner decision)

- Owner decision: guest photos of menus (Google Maps, and the owner's own screenshots of Tripadvisor/Google) may be used for the price band, recorded as `secondary`, confidence `low`, with info issue `cost_level_menu_photo`.
- From the owner's screenshots: `casa-manuel-de-la-lonja` €€ -> € (grilled fish and meat 9-18 €, median about 12 €); `restaurante-la-escollera-estepona` €€ -> € (seafood raciones median 15,50 €, no drink price; `cost_level_borderline`).
- From Google Maps guest photos fetched with the Places API (up to 10 photos per place, 21 restaurants checked; only 2 more had a readable menu): `el-andaluz-de-la-malagueta` Unknown -> € (median main 13,50 €); `taberna-mar-de-alboran-estepona` Unknown -> € (median 13,50 €; fish column spot-checked). `norte-puerto-banus` only had a breakfast menu (not used).
- All four records stay `draft`, so the app is unchanged. Validation 0 errors.

## 2026-11-08 (evening) - Olvera and Zahara back in the excursion layer; three stale app rows hidden (owner decision)

- Five app rows came from an early import (2026-10-19) and were never refreshed because their records are not in `data/layer-membership.csv`.
- Owner decision: `olvera-castle` (110 min) and `zahara-de-la-sierra` (130 min) added to `excursions_4h`, group `Dagsture`, like Setenil, Ronda and Vejer (fact-checked together on 2026-10-30; drive times from the owner's Google Maps screenshots). Danish app texts added for both. Export now 151 places, 127 in Danish.
- Owner decision: `palmeral-de-las-sorpresas`, `los-canos-de-meca` and `aracena` stay archive (records incomplete); their app rows are hidden with guide status `archived` (app change in callemilano-f388b2be), rows kept.

## 2026-11-08 (evening) - Danish texts for the remaining app places

- `data/app-texts-da.json`: Danish `summary` and `practical` texts for 72 more places (31 sights, 16 beaches, 12 towns, 10 excursions, 3 nature), three translator subagents; every price and opening-hours text compared with its English source by the main session. 125 of the 149 exported places now go to the app in Danish. The 24 places whose Danish texts were written in the app are left out, so the app keeps those texts.
- App export regenerated (`manifest.danish` 125, no stale). No place records changed.

## 2026-11-08 (evening) - Oplev page decisions and category images (owner decisions)

- Owner decisions: one app page "Oplev" replaces Inspiration, Find en tur, Turforslag and Anbefalinger; feedback replaces Anbefalinger (Eric's list, no automatic changes, no time limit); family-wide AI cap 20 per day; saved trips private but shareable; family's own places without trip data shown as "Familiens forslag"; bars under Restaurants. Plan: `docs/product/byggeplan-oplev.md`; mockup https://claude.ai/artifact/3hvQeqQLi1ek2kp92Acs5j.
- Six generic category images (CC0 / Public Domain Mark, via Openverse; no identifiable people) registered in `data/image-rights.csv` as `APP-OPLEV-*-001`; sources in `docs/product/oplev-category-images-2026-11-08.json`. Restaurants will use Google Places photos shown live with author attribution (not copied).

## 2026-11-08 (evening) - Sheriff page removed from the app (owner decision)

- Owner instruction "Slet Sheriff": the hand-written inspiration page `published-restaurante-sheriff` in the app table `recommendations` was deleted (no diary tags referenced it). A full copy of the row is in `docs/archive/app-rows/restaurante-sheriff-2026-11-08.json`; `docs/published/restaurante-sheriff.md` is marked archived. The place record stays `archived`.
- Same day, after PR #58: the 53 restaurant guides in the app were updated from the export (Danish texts, Somos de Banús €€, El Ancla hours); remote self-test 16/16 OK (2 UV warnings from met.no).

## 2026-11-08 - Owner decisions, price check batch 3 and Danish restaurant texts for the app

- Owner decisions 2026-11-08: `restaurante-sheriff` is closed (not a seasonal closure) -> status `archived`, ID kept, info issue `closed_permanently`, owner statement in the evidence ledger; `somos-de-banus` `€€€` -> `€€` (median main about 29 € + drink, rule of 2026-11-03); directory lead R-0201 KFC -> `fravalgt`.
- Price check batch 3 (two `source-reader` runs, `tools/intake.py fetch`; Firecrawl only for blocked pages): no own-menu prices found for Asador Otola, El Mirador del Golf, Jack's Smokehouse or Restaurante Hoyo 19; no own website found for Chiringuito Las Dunas, Chiringuito Rafael or Restaurante El Golf (Mijas). These keep their Tripadvisor/TheFork band. Still no prices or still blocked: Burger King, Casa Carmen, Da Vinci Los Boliches (DNS failure), Foster's Hollywood (403), La Tagliatella, The Good Burger. No records changed for these.
- `ragazzi-fuengirola`: own website names only the Fuengirola restaurant, so `menu_branch_unconfirmed` is closed (spot-checked). Price unchanged (`€`).
- `marisqueria-el-ancla-san-pedro`: hours (13:00-23:00; Monday closed in summer except holidays) and booking phone from the own contact page (undated, last modified 2021; spot-checked); bookings by phone only.
- `chiringuito-el-cachalote`: the menu page still has only the February 2026 'BORRADOR' images; `cost_level_menu_draft` stays.
- Danish texts for the app (owner request, handover task 3): new `data/app-texts-da.json` with Danish `summary` and `practical` texts for all 53 exported restaurants and bars (two translator subagents plus the main session; every price text compared with its English source, two corrected). `tools/app_export.py` sends them with `text_language: "da"` only while a hash of the English texts still matches; otherwise it falls back to English and lists the place in `manifest.danish_stale`. New test `tests/test_app_export_danish.py`. Described in `docs/product/webapp-byggeplan.md`.
- Validation 220 records, 0 errors; catalog and app export regenerated.

## 2026-11-05 - Price check batch 2: own menus for four restaurants

- Owner request (handover task 2): replace the TheFork/Tripadvisor price markings with own-menu prices for El Ancla, Tasca Láska Malagueta, Taberna Casa Blanca Banús and Chiringuito El Cachalote. Fetched with `tools/intake.py fetch` (curl and pdftotext; no Firecrawl calls). El Cachalote's menu is image-only and was read visually by the main session. Rule of 2026-11-03: median main + one drink.
- `marisqueria-el-ancla-san-pedro`: own carta PDF, median main 25 €, no drink prices -> stays `€€`. New info issue `menu_possibly_outdated` (PDF last modified August 2022).
- `tasca-laska-malagueta`: own digital menu for the Malagueta branch (the PDF on the branch page is the Avenida branch's menu, same main prices), median 18,00 € + glass of wine 3,80 € = about 21,80 € -> stays `€€`. All facts in `facts_partly_checked` are now checked, so the issue is closed.
- `taberna-casa-blanca-banus`: own Puerto Banús menus (dated 02-10-26), median 'Lonja y mercado' plate 16,25 € + caña 2,70 € = about 18,95 € -> `€€` to `€`. New info issue `cost_level_borderline` (close to 20 €; owner may prefer `€€`).
- `chiringuito-el-cachalote`: own menu images (named 'BORRADOR', February 2026), median 15,00 € + draught beer 2,90 € = about 17,90 € -> `€€` to `€`. New info issue `cost_level_menu_draft`. Schedule corrected from the own site: open 11:30-19:00, kitchen 12:00-18:00 (the earlier record gave 11:30-19:00 as kitchen hours).
- Owner decision 2026-11-05 (later): Casa Blanca Banús is `€`; `cost_level_borderline` removed and the decision noted in `cost_basis`. App database row updated with the same guide.
- All four: `cost_level_secondary_source` closed; the stray trailing "N" in three `cost_basis` texts is gone. Older secondary evidence entries are kept. Statuses unchanged (`needs_fact_check`). Validation 0 errors; catalog and app export regenerated.

## 2026-11-05 — Use the current time for between-stop route estimates (owner decision)

- Owner decision: Google Routes between-stop estimates use the current instant, rather than the next Saturday or the requested trip date. The Saturday assumption was introduced to standardize route comparisons, but observed weekday variation did not justify it. `tools/trip.py` now sends the current UTC instant as the Routes API `departureTime`; the separate static place-intake route checks are unchanged.
- Added a focused unit test for the UTC timestamp and route request payload. No place records or route-check evidence were changed.

## 2026-11-04 (afternoon) - Self-test instead of trial and error (owner decision)

- Owner decision: stop the trial-and-error loop (owner merging, publishing and making manual trip plans after every small fix). App PRs thomasericolesen/callemilano-f388b2be#12 and #13 add a self-test: 14 scenarios with automatic checks on plan data, place suggestions and Ecco's text (`src/lib/selftest.ts`), a local runner against a DB snapshot with live weather/traffic (`scripts/selftest-local.mts`, `OPEN_METEO_DOWN=1` mimics the Lovable server), and `POST /api/selftest` on the live site with real keys (`scripts/selftest-remote.mts`; token in `public.selftest_tokens`, RLS, service role only, expires after 90 days; table created with the Lovable `query_database` tool). An independent review agent checked the code before the owner merged.
- Fixes found by the self-test: met.no sent a truncated cached answer for Puerto Colorado (now 3 decimals, then 4, then compact); restaurants without hours showed as "åbent område" (now "ring og tjek"); Ecco left out "Kør hjemmefra" with three stops, wrote "Sevärdighed" and promised a waterfall that is not in the data (prompt rules plus `tidyEcco()`); met.no UV "0" a few days ahead (daytime hours only).
- Result on https://callemilano.dk after #13: 14 of 14 scenarios OK (4 warnings: met.no has no UV beyond about 2 days).

## 2026-11-04 - Weather source and the role of OpenAI (owner decisions)

- Open-Meteo: the live site showed "HTTP 429: Daily API request limit exceeded" (free quota per IP; the Lovable server shares IPs). App PR thomasericolesen/callemilano-f388b2be#10 (merged) retries with short timeouts, keeps the reason and caches; #11 makes met.no the effective source with clear-sky UV and sunrise/sunset. met.no has no precipitation probability or gusts for Spain. Option noted for later: AEMET OpenData (official, free API key, rain probability and UV per municipality).
- Owner decision: consensus between OpenAI and Claude was meant for development (the two systems challenging each other to get the best, most robust and most interactive model), not for agreeing on trip plans. In the app, Claude picks places (as Ecco writes the text) and OpenAI is only a fallback when Claude does not answer (owner chose this over Claude only). App PR #11.

## 2026-11-03 (late evening) - AI-turplan merged into Turforslag (owner decision)

- Owner decision 2026-11-03: the Lovable page "AI-turplan" (`/ai-tur`, OpenAI through the Lovable AI Gateway) is merged into `/turforslag`. Owner chose admin-only access at first and then asked for consensus between OpenAI and Claude, not either/or.
- App PR thomasericolesen/callemilano-f388b2be#7: a "Beskriv jeres ønske" box on `/turforslag`; Claude and OpenAI (Lovable AI Gateway) each pick 1-3 places in parallel from the same catalog; places both pick come first ("Claude og OpenAI enige"), single-model picks fill up to 3 and are marked; if one model fails the other's picks are used with a "no consensus" note. Ecco still writes the text with Claude. The catalog includes restaurants and excludes bars, and the server keeps only catalog ids; the picks become the selected places and the wish goes to Ecco. `/ai-tur` redirects to `/turforslag`; admins get a "Turforslag" menu item.

## 2026-11-03 (late evening) - Fact check: five priced restaurants to needs_fact_check

- `source-reader` read the own sites (home, contact and menu pages; 1 Firecrawl call) for Ragazzi, Marvelous Burger, Café NOMAD, Kalifato and Juan Playa; `record-writer` wrote descriptions, evidence, schedules (Ragazzi 12:30-23:30 except Tuesday; Café NOMAD daily 9:00-15:00; Juan Playa daily 13:00-17:00 and 19:00-23:00; season not stated), phone links and booking notes. All five `draft` -> `needs_fact_check`; `no_readable_own_source` and `facts_not_checked` resolved, `facts_partly_checked` added (hours for Marvelous Burger and Kalifato, children's facilities, accessibility, season, parking). Marvelous Burger has no phone (only a WhatsApp booking link on its Linktree). Sheriff left out (possibly closed).
- Orchestrator spot checks against the live pages: Ragazzi "12:30 a 23:30h", Café NOMAD "9.00 — 15.00", Juan Playa "13:00h a 17:00h", Kalifato phone "952 56 82 59", and Ragazzi take-away/delivery (evidence added).
- Catalog and app export regenerated: Ragazzi, Marvelous Burger and Café NOMAD now reach the app as `€`, Kalifato and Juan Playa as `€€`.

## 2026-11-03 (late evening) - Price check batch 1: restaurants within 30 minutes

- First batch with the free fetch steps: `source-reader` read own sites and menus for 21 restaurants within 30 min of Casa de la Familia (La Mar Salá skipped: approved; La Zambra: hotel resort). 5 Firecrawl calls (Ragazzi and Kalifato PDFs are images). Spot checks by the orchestrator against the live sources: Sheriff (Pollo asado 14,20 €, Entrecot plancha 26,20 €, Spaguetti bolognese 12,00 €) and Juan Playa (Escalope de pollo 14,00 €, Hamburguesa con patatas 10,95 €, Coca Cola 3,25 €) match.
- New `cost_level` (median quoted main + one drink, rule of 2026-11-03): `ragazzi-fuengirola` `€` (about 16,30 €; issue `menu_branch_unconfirmed`), `marvelous-burger-fuengirola` `€` (about 16,15 €), `kalifato-benalmadena` `€€` (about 23,75 €). Owner decisions on borderline cases: `cafe-nomad-fuengirola` `€` (median 13,20 €, no drink price), `juan-playa-fuengirola` `€€` (median 16,75 €; caña 2,90 or 3,60 € not pairable in the PDF), `restaurante-sheriff` stays `Unknown` (median 16,70 €, no drink price, possibly closed). Borderline cases carry `cost_level_borderline`. Evidence quotes verbatim; statuses unchanged (draft).
- No prices on the own pages: Restaurante Hoyo 19, Asador Otola, El Mirador del Golf, La Tagliatella, Burger King (only a "desde 3,50€" bundle), Casa Carmen, The Good Burger, Freiduría El Choco, Kamura Sushi (image menu), El Higuerón, Sollo (only a 180 € tasting menu). Blocked: Foster's Hollywood (403), Da Vinci Los Boliches (DNS failure; URL to check), UTOPÍA and Venta los Condes (PDFs not readable).
- Catalog and app export regenerated.

## 2026-11-03 (late evening) - Free page fetching before Firecrawl (owner request)

- Owner asked for an alternative to Firecrawl (credits ran out on 2026-11-02). `tools/intake.py fetch` now tries free steps in order: curl; PDF text with `pdftotext` (also when the server says the page is a PDF); headless Chromium through the new `tools/render_page.mjs` (Node Playwright, already installed in the cloud environment) when curl is blocked, empty or needs JavaScript. Only pages that still fail are marked `needs_firecrawl`. Facebook/Instagram URLs are marked `login_wall` (no tool gets past the login; owner screenshot instead). `_status.json` now records `method` and up to ten menu/carta/PDF links per page.
- Test on 17 pages from the last blocked or price-less batches (2026-11-03): El Ancla's PDF carta, earlier recorded as "PDF without text", gives 8 018 characters with prices; Tasca Laska's PDF menu reads in full; Upstairs read via Chromium when curl got 429. Still blocked: Tripadvisor (403), Speakeasy (403), Sky Bar Veramar (404, site moved). Jack's Smokehouse and La Floja have no menu text on their home pages for any tool. No records were changed by the test.
- `source-reader`: follows up to three menu/carta/PDF links when prices are asked for, reports `login_wall`, uses `WebSearch` before `firecrawl_search` to find an official URL, and records `method` (`curl`, `pdf`, `playwright`, `firecrawl`). Same order in `alpha`, `charlie` and `docs/agent-pipeline.md`.

## 2026-11-03 (evening) - Lounge El Trópico is a restaurant; Cerros del Águila priced € (owner decisions)

- Owner decision 2026-11-03 (with the own website https://chiringuitoeltropico.com/en/home/, read again with curl the same day): Lounge El Trópico serves breakfast, lunch and dinner and is treated as a beach restaurant (chiringuito), like Chiringuito Los Moreno. It came in through the bars intake (`docs/decisions/bars-intake-2026-11-02.md`).
- `lounge-el-tropico`: `description_long` no longer carries the bar advice ("take a taxi or Uber", "keep an eye on your drink"), so `tools/app_export.py` no longer flags it as a bar and `/turforslag` can use it; it now names the own-site name Chiringuito El Trópico and the menu prices already in the evidence. Issue `prices_unknown` removed (prices were read 2026-11-02, `cost_level` `€`). Name, ID, slug, category, tags and status (`needs_fact_check`) unchanged.
- `restaurante-cerros-del-aguila`: `cost_level` `Unknown` -> `€` on the owner's own knowledge (owner, 2026-11-03: a typical main plus a beer or a glass of wine is under 20 €; "sæt mig som kilde"). Evidence `confidence: low`; the own Facebook page's price range "moderate" is recorded as a conflict resolved by the editor-of-record; info issue `cost_level_owner_source`. Status unchanged (`needs_fact_check`).
- App export regenerated.

## 2026-11-03 (evening) - New restaurant price bands (owner decision)

- Owner decision 2026-11-03, replacing the 15/35 € bands of 2026-11-01: price = the median main course on the menu + one drink per adult; `€` under 20 €, `€€` 20-50 €, `€€€` over 50 €. Reason: a fast-food meal in Denmark costs 120-140 kr (about 16-19 €), so the old `€` limit was below what guests see as cheap, and no record had `€`.
- Recomputed from the quoted menu prices already in each record's evidence (median of the quoted mains plus the cheapest quoted drink; no new fetches): `chiringuito-la-concha-el-palo` (about 16,30 €), `la-lobezna-estepona` (about 16,35 €) and `lounge-el-tropico` (about 16,50 €) move from `€€` to `€`. All other own-menu records stay `€€`; `cost_basis` rewritten with the median for each.
- Borderline, kept `€€`: `gali-gali-fuengirola` and `los-marinos-paco` (median main 17,50 €, no single-drink price). `los-enebros-fuengirola` (median 19 € + drink) stays `€€` at the lower edge.
- `cost_level_borderline` issues removed where the old band edge no longer applies (Océano, El Trópico, Casa Fernando, Solo Beach).
- Tripadvisor, TheFork and Facebook price markings stay `€€` until an own menu is found; only the rule text in `cost_basis` changed (approved records Chiringuito Los Moreno, La Mar Salá, Los Marinos Paco, Morrofino and Santa Ana Denis: rule text only, level unchanged).
- Not changed, waiting for the owner: `somos-de-banus` is `€€€` by owner decision 2026-11-02, but its median main (29 €) plus a drink is `€€` under the new rule.
- Rule text updated in `tools/trip.py` (PDF labels), `.claude/agents/charlie.md`, `docs/trip-planner-agents.md`, `docs/history/handoff-next-session.md` and a note in `docs/decisions/cost-level-proposals-2026-11-02.md`. The band column in `data/restaurant-directory.csv` (lead list) was computed under the old rule and is not recomputed.

## 2026-11-02 (late evening) - Ecco in the app (trip agent step 1, point 4)

- App PR thomasericolesen/callemilano-f388b2be#3: Ecco writes the Danish trip plan with Claude Sonnet 5.5 (owner decision) from `planTrip` data; structured output, no new facts (restaurants, weather figures and links come from data). Owner stored `ANTHROPIC_API_KEY` as a Lovable Cloud secret.

## 2026-11-02 (late evening) - planTrip in the app (trip agent step 1, point 3)

- `tools/app_export.py`: each place's `guide` now carries a `trip` block (schedule and its check date, `valid_until`, fixed-hours need, rainy-day tag, bar flag, phone, booking lead time, typical duration). Export regenerated (144 places).
- App repository branch `claude/vigilant-cray-dtqaxz`: `planTrip` server function and admin-only `/turforslag` page with the same rules as `tools/trip.py plan`; drizzle migration 0004 adds `public.holidays` (28 rows). Verified against `tools/trip.py` with live DGT data and the export: identical incidents and restaurant picks.
- Merged by the owner; places re-imported (143 with the `trip` block). Lovable Publish did not run drizzle migration 0004, so Claude applied it with the Lovable `query_database` tool (table `public.holidays`, 28 rows, RLS select for family/admin).

## 2026-11-02 (late evening) - App export and import (trip agent step 1, points 1-2)

- New `tools/app_export.py` -> `data/app-export/places.json` (144 places, status `needs_fact_check` or later, primary area or layer membership; the app's `guide` schema) and `holidays.json` (28). Derived data; re-run after record changes.
- App repository `thomasericolesen/callemilano-f388b2be` (Lovable sync) branch `claude/vigilant-cray-dtqaxz`: import of the export with file upload, matching by ID, then Google place ID, keeps Danish texts and family rows, skips editorial pages; "Ikke endeligt godkendt" labels; restaurants left out of "Find en tur". Typecheck and build pass; not merged.

## 2026-11-02 (late evening) - Interactive trip agent: owner decisions (no schema change)

- Recorded in `docs/product/webapp-byggeplan.md`: show records with status `needs_fact_check` or later in the app, non-approved ones labelled "Ikke endeligt godkendt", drafts hidden; build via GitHub connection and Claude Code; Ecco on Claude Sonnet 5.5; admins only at first. Voice v0 (phone) and the $20/month, 10-per-user-per-day caps remain proposals.

## 2026-11-02 (late evening) - Restaurants from callemilano.dk (owner instruction)

- Owner instruction: the recommendations already on callemilano.dk (Lovable app "Vores Spanske Hjem", table `recommendations`) belong in the restaurant list. The site has 6 own restaurant recommendations (`kind` anbefaling) and 4 inspiration entries.
- Created draft records for the 5 missing own recommendations: `cafe-nomad-fuengirola`, `heladeria-casa-esteban-fuengirola`, `marvelous-burger-fuengirola`, `utopia-la-cala`, `venta-los-condes` (10-25 min), and for the inspiration entry `restaurante-sheriff` (12 min; it had only a hand-written page in `docs/published/`). Each owner text is quoted verbatim in an owner-knowledge evidence entry and summarised in `description_long`; the same was added to the existing `asador-otola`.
- `restaurante-sheriff`: blocking issue `possibly_closed` (Google CLOSED_TEMPORARILY; Mijas Tourism note cited on the gold page).
- TheFork/Tripadvisor price lookup for 23 new records: 9 markings found (5 identity-confirmed by address), 14 none. Not applied yet: the orchestrator spot check could not run (Firecrawl credits exhausted; Tripadvisor blocks curl). Results listed in `docs/history/handoff-next-session.md`.
- Owner decision 2026-11-02: Casas Cuevas Almagruz, Castillo de Monda and El Molino del Santo are not standalone excursions; they are visited for their restaurants, and other facilities are for hotel guests only. Created as `Restaurants` draft records in layer `excursions_4h`: `castillo-de-monda` (35 min, Tæt på, nearby Monda), `molino-del-santo` (105 min, Dagsture, nearby Ronda), `casas-cuevas-almagruz` (120 min, Længere væk; ID namespace corrected to `ES-AND-GRA` right after allocation). Info issue `guest_only_facilities` on each.

## 2026-11-02 (late evening) - Directory leads: owner checklist (step 2 started)

- Google sweep of the 25 unconverted rows in `data/restaurant-directory.csv` (all OPERATIONAL, 8-18 min by car). Flags: R-0109 Taco Tikka's address now shows "DA LEONE" on Google; R-0302 Chiringuito La Cubana's Google listing is named "CAMBIO DE UBICACIÓN" (moved).
- Owner checklist published: https://claude.ai/artifact/VCrXrv5vKsUhruvVk6R9ZT (collection `choices`).
- Owner selection 2026-11-02: 21 yes, 3 no (R-0109 Taco Tikka, R-0111 The Wessex Bar, R-0302 Chiringuito La Cubana -> row status `fravalgt`), 1 maybe (R-0201 KFC stays a lead). Created 21 draft records with `tools/intake.py create` (category `Restaurants`, tag `Restaurant`, primary area, 8-18 min by car, IDs in the registry); their directory rows are `konverteret` with the slug in `notes`.
- Fact check (source-reader -> record-writer): 7 records to `needs_fact_check` (los-enebros, freiduria-el-choco, gali-gali, old-swiss-house, mias-pizzorante, sollo, el-higueron), each with `facts_partly_checked`; 14 stay draft with `no_readable_own_source` (blocked sites, image-only menus, PDFs that timed out, or no own site). Spot checks: Los Enebros (entrecot 32.00 €, Monday closed) and Old Swiss House (opening note) match the fetched pages. Corrected El Choco's schedule to the quoted days only (issue `schedule_partly_quoted`); Old Swiss House has `source_conflict` on hours and street number. `cost_level` `€€` from own menus for Los Enebros (borderline issue), Gali Gali, Old Swiss House and Mia's.
- R-0102 Chiringuito La Mar Salá already exists as the approved record `la-mar-sala`; row status set to `konverteret` (new directory status value; `tools/trip.py` uses only `aktiv` rows, so converted rows are no longer read twice).

## 2026-11-02 (late evening) - La Sierra Restaurante = Cerrado del Águila (owner screenshot)

- Owner screenshot of the own Facebook page "La Sierra Restaurante - Cerrado del Águila Golf and Resort" confirms that `la-sierra-restaurante` and `restaurante-cerrado-del-aguila` are the same venue (Google points about 10 m apart). Owner decision: keep `la-sierra-restaurante`; `restaurante-cerrado-del-aguila` archived with issue `duplicate_record` (ID kept, registry status `superseded_by_ES-AND-MAL-LA-SIERRA-RESTAURANTE-001`).
- `la-sierra-restaurante`: from the page, address at Cerrado del Águila Golf and Resort, phone +34 951 74 19 90, WhatsApp, daily breakfast, coast views; `cost_level` `€€` from the page's Facebook price range "Moderate"; status `draft` -> `needs_fact_check`. Ratings and e-mail not recorded. Hours, menu prices and booking link still open.
- `juanito-juan`: owner Google Maps screenshot gives Av. Salvador Allende 26, El Palo; Tripadvisor "Restaurante Juanito" photo pages give the same address, so the listing is the same venue. `cost_level` `€€` from Tripadvisor "€€ - €€€" (low confidence, info issue). Google's user-reported 20-30 € agrees but is not used as a price source (AGENTS.md). Status stays `draft` (no own website).
- `restaurante-cerros-del-aguila` (the bar and grill at the Cerros del Águila sports area) is a different place and is unchanged.

## 2026-11-02 (evening) - Restaurant price bands from own menus (owner confirmed bands)

- Owner confirmed the price bands on 2026-11-02: adult main course + one drink; `€` under 15 €, `€€` 15-35 €, `€€€` over 35 €.
- `source-reader` read 18 own-venue menu pages. 7 of them had prices: `cost_level` is now `€€` for `chiringuito-la-concha-el-palo`, `el-oceano-beach-hotel`, `la-lobezna-estepona`, `lounge-el-tropico`, `restaurante-casa-fernando-san-pedro`, `solo-beach-marbella` and `somos-de-banus`, with `visit_information.cost_basis`, `cost_checked_at` and verbatim evidence. Spot checks: La Concha (entrecot 14,00 €, caña 2,30 €) and Casa Fernando (entrecote 29.50 €) match the fetched pages.
- Borderline cases have an info issue `cost_level_borderline` (Océano, El Trópico, Casa Fernando, Solo Beach, Somos de Banús); Somos de Banús may be `€€€` if the owner prefers.
- No prices found on own pages: Asador Otola, Restaurante Hoyo 19, Tasca Laska, Upstairs. Blocked or unreadable: El Cachalote, Jack's Smokehouse, La Floja, El Ancla (PDF without text), Sky Bar Veramar (site moved to veramaraparthotel.com), Speakeasy, Taberna Casa Blanca. These stay `Unknown`.
- Same evening, owner decision: use the TheFork/Tripadvisor price marking as a noted fallback where the own site has no prices. 16 more records set to `€€` with a `secondary` low-confidence evidence entry and info issue `cost_level_secondary_source`: asador-otola, casa-manuel-de-la-lonja, chiringuito-central-beach-estepona, chiringuito-el-cachalote, chiringuito-las-dunas-cabopino, chiringuito-rafael, el-mirador-del-golf, jacks-smokehouse-puerto-banus, marisqueria-el-ancla-san-pedro, norte-puerto-banus, restaurante-el-golf-mijas (TheFork 26 €), restaurante-hoyo-19, restaurante-la-escollera-estepona, taberna-casa-blanca-banus, tasca-laska-malagueta (TheFork 24 €), venta-la-morena. Spot checks: Tasca Láska (TheFork "Precio medio: 24 €") and El Cachalote (Tripadvisor "€€ - €€€") confirmed by a separate search.
- Left `Unknown`: partial snippet markings (el-andaluz-de-la-malagueta, taberna-mar-de-alboran-estepona, restaurante-cerros-del-aguila), identity to confirm (juanito-juan listed as "Restaurante Juanito"; restaurante-cerrado-del-aguila possibly renamed La Sierra Restaurante), no source (courtside-by-wissler, la-zambra-resort, mixs-lounge, pena-al-tranco, singh-doner-kebab), blocked (la-sierra-restaurante, sol-y-sombra-mijas). Bars not looked up (excluded from trip plans).
- Approved records: proposals for owner approval in `docs/decisions/cost-level-proposals-2026-11-02.md` (5 x `€€`, Chiringuito Cristóbal without source).
- Owner approval 2026-11-02 (later): all five proposals in `docs/decisions/cost-level-proposals-2026-11-02.md` approved; `cost_level` `€€` set by the main session on the approved records los-marinos-paco, santa-ana-denis, morrofino, la-mar-sala and chiringuito-los-moreno (status unchanged). Owner decision: `somos-de-banus` is `€€€` (borderline issue removed). Chiringuito Cristóbal stays `Unknown`.
- Not changed: status, schema, categories, tags.

## 2026-11-02 - Trip planner merged with the intake pipeline (owner decisions 15-16)

- Brought over from the unmerged branch `claude/awesome-clarke-tvlhrg` (work of 2026-11-01, entries below): `tools/trip.py`, `docs/trip-planner-agents.md`, `docs/product/webapp-byggeplan.md`, agents `alpha`, `charlie`, `ecco`, skills `/turforslag`, `/restaurant-indsamling`, `/aabningstider`, `data/holidays.csv`, `data/restaurant-areas.csv`, `data/restaurant-directory.csv` (26 Fuengirola-area leads), `trips/` (git-ignored).
- Not brought over: the branch's change to `fuengirola-centro` (it moved the approved beach record's point to Plaza de la Constitución). Owner clarification 2026-11-02: the beach point stays between the harbour and the Río Fuengirola bridge; the town centre is Plaza de la Constitución, which is the separate record `fuengirola-town`. The owner-confirmed underground car park at Plaza de la Constitución is now in `fuengirola-town` (parking, evidence).
- Owner decision 16: restaurants are full place records. `tools/trip.py` reads restaurant records first (bars excluded) and uses directory rows only for places not yet recorded; price band comes from `cost_level`. Alpha and Charlie follow the shared pipeline rules (fetch first, record changes only via `tools/intake.py apply`, reviews only as low-confidence leads) and run on Sonnet; Ecco on Sonnet.

## 2026-11-01 (later) - Trip planner restructured into two phases (owner decision, no schema change)

Owner decision 2026-11-01: replace five agents per trip plan with two phases. Branch `claude/awesome-clarke-tvlhrg`.

- Phase 1 (advance work): `/restaurant-indsamling` (Charlie, per area) and new `/aabningstider` (Alpha mode A, updates `visit_information` and evidence in place records under the normal workflow, status unchanged).
- Phase 2 (trip plan): `python3 tools/trip.py plan` gathers places, nearby suggestions, opening status, holidays, weather and advice, DGT traffic, restaurants and automatic checks into `trips/<id>/plan.json`; Alpha mode B runs a quick check only for places marked `kræver_tjek` and writes `hours-check.json` without editing records; Ecco writes the plan and PDF.
- Bravo (weather/traffic) and Delta (quality checks) are now rules in `tools/trip.py`; their agent files are removed.
- New: `data/restaurant-areas.csv` (5 areas covering the 13 local places), `data/holidays.csv` (Andalusian holidays 2026 and 2027 from Decreto 101/2025, BOJA 93 of 19-05-2025, and Decreto 84/2026, BOJA 84 of 05-05-2026; local municipal holidays not yet added), `area_id` column in `data/restaurant-directory.csv`, commands `plan` and `hours-status`.
- Opening hours count as current when the latest evidence for `visit_information` or `visit_information.schedule` is at most 60 days old and `valid_until` has not passed. On 2026-11-01 only `tolox` needs work (season ended 2026-10-16).
- Not changed: schema, categories, tags, enums, layers, place records.

## 2026-11-01 - Trip planner agents (Alpha-Ecco) and light restaurant directory (owner decisions, no schema change)

Owner request: make CalleMilano interactive; when guests pick one or more places, agents prepare a printable trip plan. Branch `claude/awesome-clarke-tvlhrg`.

- Owner decisions 2026-11-01 (answered in session): the host runs `/turforslag` (guest self-service later); restaurants are collected in advance and refreshed about every 3 months; price bands per adult main course + one drink: `billig` < EUR 15, `mellem` EUR 15-35, `dyr` > EUR 35; delivery as one PDF for print and phone (native push postponed); restaurants within about 10 min walk (800 m straight line), widened to about 3 km only when short; restaurants stored in a light directory, not as place records; free data sources first (Open-Meteo with met.no fallback, DGT DATEX II incidents, no paid traffic forecast); plans written in Danish.
- New: `.claude/agents/{alpha,bravo,charlie,delta,ecco}.md`, `.claude/skills/turforslag/`, `.claude/skills/restaurant-indsamling/`, `tools/trip.py`, `data/restaurant-directory.csv` (header only, no rows yet), `docs/trip-planner-agents.md`. Trip working files go to `trips/` (git-ignored, may hold guest details).
- `data/restaurant-directory.csv` is a light list outside the place-record lifecycle: no IDs in `data/place-id-registry.csv`, not in `data/place-catalog.csv`. Restaurants that deserve an editorial page stay full records in `docs/places/`.
- Trip plans may use records not yet `approved`, marked "Udkast" in the PDF; archive places are refused by `tools/trip.py`.
- Not changed: schema, categories, tags, enums, layers, place records.
- Open: restaurant directory is empty; first `/restaurant-indsamling` run needed, starting with the local layer.

## 2026-11-02 - Agent pipeline and first pipeline batch (nature and experiences)

- Owner decision: routine work moves to scripts and cheaper subagents. Added `tools/intake.py` (sweep, nearby, fetch, create, apply, checklist), `tools/templates/` (blank record, checklist page), `.claude/agents/` (`candidate-screener`, `source-reader` on Haiku; `record-writer` on Sonnet) and `docs/agent-pipeline.md`; pointer in `AGENTS.md`.
- First batch via the pipeline: 11 new records (jardin-botanico-la-concepcion, juanar-macho-montes, canon-de-las-angosturas, rio-grande-coin, paseo-maritimo-marbella, cueva-del-tesoro, senda-litoral-malaga-oeste, funny-hill-karting, puerto-deportivo-estepona, aventura-amazonia-marbella, museo-aeronautico-malaga). Senda Litoral (30 min), Aventura Amazonia (21 min) and Museo Aeronáutico (28 min) are in the local layer, the rest in `excursions_4h` / `Tæt på`.
- source-reader found official or own pages for 7; record-writer moved those 7 to `needs_fact_check`. Orchestrator spot-checked 12 quotes against the fetched pages (all verbatim). Still draft with a review issue: Angosturas (council page blocks automated reading), Río Grande (no official page found), Paseo Marítimo de Marbella and Senda Litoral Málaga (pages found cover other sections).
- Not yet done: boat trips from Marbella (provider sweep and reputation screen first); Selwo Aventura already had a record.

## 2026-11-02 - One-hour band: towns and Málaga

- Nine new records (IDs allocated, `excursions_4h` / `Tæt på`): puerto-banus (Excursions), san-pedro-alcantara, estepona-old-town, ojen, istan, benahavis, monda, coin, alora (City). Route-checked; descriptions checked against the Andalusian tourist board (andalucia.org) and Spain.info -> `needs_fact_check`. Parking and practical details still open; San Pedro's play-area claim has only a secondary source.
- Folded in per the owner's selection: the mural route into estepona-old-town; Avenida del Mar (Dalí sculptures, Turismo Marbella) into marbella-old-town; Málaga city sights (Teatro Romano, Museo Picasso, MIMMA, Parque de Málaga, Muelle Uno, Museo del Automóvil y la Moda) into `malaga`, which moves from needs_editorial_review to needs_fact_check (issue `reopened_material_change`).
- Álora: the castle is the town cemetery (Andalusian tourist board); noted in the record.

## 2026-11-02 - Restaurants near the one-hour beaches: records and first fact check

- Owner selection read from the restaurant checklist: 17 yes. Rows rE04 and rF05 were duplicates of rE02 and rF01 in the first page version (name-matching error); fixed to Restaurante Marabierta and Restaurante Vista al Mar, the owner's answers to those two rows cleared, and the owner asked to choose again.
- 17 new restaurant records (IDs allocated, `excursions_4h` / `Tæt på`, `related_places` set to the nearby beach), each with a Google Places identity and a Routes API drive time.
- Fact check from own websites for 10: Tasca Láska, El Cachalote, La Concha (El Palo), Somos de Banús, Jack's Smokehouse, Solo Beach, Casa Fernando, El Ancla, La Lobezna, Casa Blanca Banús -> `needs_fact_check`. Seven without a readable own site stay `draft` with issue `no_readable_own_source`: El Andaluz de la Malagueta, Juanito Juan, Casa Manuel de la Lonja, Norte, Central Beach, La Escollera, Mar de Alborán.

## 2026-11-02 - Restaurant candidates near the one-hour beaches

- Added `docs/decisions/one-hour-beach-restaurants-intake-2026-11-02.md`: 24 candidates near the six selected beaches, shortlisted from Google Places. Owner selects on a checklist page; no records created.

## 2026-11-02 - One-hour band: layer decision and beaches

- Owner decision 12: catalogue group `Tæt på` means a route-checked drive of at most 60 min. Caminito del Rey, Sierra de las Nieves and Gibraltar moved to `Dagsture` in `data/layer-membership.csv`; note added to `AGENTS.md`; decisions 12-14 in `docs/owner-decisions-2026-11-02.md`.
- Added to `excursions_4h` / `Tæt på`: playa-la-malagueta, selwo-aventura, mercado-de-atarazanas (existing records) and five new beach records.
- New records (IDs allocated): playas-del-palo, playa-de-nagueles, playa-puerto-banus, playa-de-san-pedro-alcantara, playa-de-la-rada-estepona.
- Fact check of all six selected beaches against Spain.info (Turespaña), Málaga City Council beach pages and ADEAC's Blue Flag 2026 list. All six meet the rocks rule. Blue Flag 2026: Malagueta, El Palo, Nagüeles-Casablanca, San Pedro (Guadalmina stretch); not Puerto Banús or any Estepona beach. Malagueta got coordinates and a new route check (41 min); its blocking issue is resolved.
- Open: lifeguard seasons for 2027, Puerto Banús facilities (tourist-board page blocks automated reading), family assessments.

## 2026-11-02 - Owner selection for the one-hour band

- Added `docs/decisions/one-hour-selection-2026-11-02.md`: 41 yes, 12 maybe, 1 no, read from the owner's checklist page. Avenida del Mar folds into Marbella old town, the mural route into Estepona old town, Málaga city items into `malaga`.

## 2026-11-02 - Taxi and train on the practical page

- Owner asked for taxi numbers and local train stations before the one-hour work continues.
- `docs/decisions/practical-information-draft.md`: new sections 'Taxi' (Radio Taxi Mijas from Mijas council's list, Radio Taxi de Fuengirola, Uber, nearest ranks) and 'Train (Cercanías C1)' (nearest stations with route-checked drive times, frequency and journey times from the CTMAM timetable, Renfe station facts). Sources 10-16. Parking and fares still open.

## 2026-11-02 - Intake for the 30-60 minute band

- Owner asked to look at destinations beyond the local area but within about one hour's drive, with restaurants nearby or on the way.
- Added `docs/decisions/one-hour-intake-2026-11-02.md`: 54 candidates in seven groups (beaches, towns, Málaga city, coastal history, nature, experiences, and four places under 30 minutes found on the way), route-checked with Google Routes. No records created; selection pending on the owner's checklist page.
- Open owner decision: which layer holds this band.

## 2026-11-02 - Season calendar, first draft (step 3, no records)

Added `docs/decisions/season-calendar-draft.md` with the 8 selected events by month: fixed 2027 dates for Noche de San Juan (23-24 June, Benalmádena tourism), Feria de San Juan Arroyo de la Miel (24-29 June), Virgen del Carmen (16 July) and Feria del Rosario (6-12 October, 'always'); Semana Santa 2027 from the computed Easter date; Carnaval, Feria de Mijas (2026: 7-12 September), Reyes and Christmas await the councils' 2027 announcements. No place record changed.

## 2026-11-02 - Practical page: emergency info left to the website note (owner)

The owner already has a note on emergency numbers and A&E on the website. `docs/decisions/practical-information-draft.md` now refers to it; the emergency numbers and the hospital entry moved to an appendix for comparison only. Recorded as owner decision 11.

## 2026-11-02 - Practical information page, first draft (step 2, no records)

Added `docs/decisions/practical-information-draft.md` for the 9 everyday places the owner selected (owner decision 7): emergency numbers (112, 061, Salud Responde) from the Junta de Andalucía; Centro de Salud Las Lagunas (Mon-Fri 08:00-20:00) from Mijas council and SAS; Hospital Costa del Sol contacts from SAS; duty-pharmacy finder; market days from Turismo de Mijas and Fuengirola council (Las Lagunas Saturday, La Cala Wednesday and Saturday, Fuengirola Tuesday market and Saturday rastro, with fair-time exceptions); market hall and supermarkets by Google identity only. Shop hours remain open. No place record changed.

## 2026-11-02 - Mirador del Compás folded into Mijas Pueblo (owner decision)

The viewpoint and the Virgen de la Peña hermitage are now described in `mijas-pueblo` (description and evidence moved); `mirador-del-compas` archived with a `review_decision` (ID kept, not reused). Validation: 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Mirador del Compás corrected (owner tip, no schema change)

The owner pointed out that Mirador del Compás is also called Mirador Virgen de la Peña. Google's positions confirm the point is about 30 m from the Ermita de la Virgen de la Peña in Mijas Pueblo, so the record's earlier description ('a viewpoint in the Sierra de Mijas reached on foot') and `energy_level: High` were wrong. Corrected: name **Mirador del Compás (Virgen de la Peña)** (ID and slug unchanged; registry updated), description, `energy_level: Low`, linked to `mijas-pueblo`; status `draft` -> `needs_fact_check`. New info issue `possible_merge_with_mijas_pueblo` for the owner. Intake doc wording corrected. Validation: 0 errors.

## 2026-11-02 - Maui Paddlesurf Club from owner screenshot (no schema change)

`maui-paddle-surf-la-cala`: own Instagram (owner screenshot) gives the club's own name **Maui Paddlesurf Club (La Cala)** (ID and slug unchanged; registry name updated), address C/ La Butibamba 7, phone, and a summer camp for ages 5-14 (29 June-31 August, 10:00-14:00, €100/week, €30/day). Status `draft` -> `needs_fact_check`; linked one way to La Butibamba (the approved beach record was not edited). Regular hire and lesson prices remain open. Validation: 0 errors.

## 2026-11-02 - Local extension fact check, batch C: walks and nature (no schema change)

`draft` -> `needs_fact_check` for 5: `dunas-de-artola` (andalucia.org: Natural Monument since 2003, three dune types, keep to marked paths), `senda-litoral-la-cala` (GR 92/E-12 overview; La Cala section details open), `paseo-maritimo-fuengirola` (only the council's 2021 cycle-lane article; `promenade_facts_thin`), `ermita-del-calvario-mijas` and `puerto-colorado-sierra-de-mijas` (Gran Senda family stage via the Via Crucis, search excerpt; 2018 municipal walk 7.5 km / 500 m; `trail_data_unread`). `mirador-del-compas` stays `draft` (no official source found). Validation: 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Local extension fact check, batch B: towns and sights (no schema change)

`draft` -> `needs_fact_check` for 6, from official tourism portals (andalucia.org, Somos Fuengirola, This is Benalmádena) and own sites: `mijas-pueblo` (village and main sights; practicalities open), `fuengirola-town` (thin: portal tagline and tourist office only; issue `town_description_thin`), `benalmadena-pueblo` (old village at about 300 m, Plaza de España, Jardines del Muro, La Niña), `castillo-sohail` (history; Tue-Fri 10-14, weekends 10-18, closed Mon; free), `castillo-de-colomares` (seasonal hours, closed Mon; exterior visit only; price conflict on its own site), `puerto-marina-benalmadena` (1,140 moorings, Blue Flag, toilets, disabled facilities, parking). Validation: 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Local extension fact check, batch A: attractions (no schema change)

Checked against own or official sources on 2026-11-02; `draft` -> `needs_fact_check` for 7: `selwo-marina` (prices and age bands; seasonal calendar, winter unconfirmed), `parque-de-la-paloma` (andalucia.org: 200,000 m², lake, two playgrounds, animals; free entry not stated), `crocodile-park-torremolinos` (prices, guided-tour times; hours conflict on its own page), `sea-life-benalmadena` (open daily, adult €18.50 online / €21 door, child €11.50), `mariposario-benalmadena` (full hours and prices, open all year), `teleferico-benalmadena` (calendar opening, prices, under-12s with an adult per cabin), `mijas-golf` (two 18-hole courses; green fees not read). `maui-paddle-surf-la-cala` stays `draft` (Instagram only). Validation: 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - 20 local-extension draft records created (owner selection, no schema change)

From `docs/decisions/local-extension-selection-2026-11-02.md`, created 20 records with status `draft` and allocated IDs: 6 `Excursions` routes and walks plus 3 `Excursions` sights (Senda Litoral La Cala, Paseo Marítimo de Fuengirola, Ermita del Calvario, Mirador del Compás, Puerto Colorado; Castillo Sohail, Castillo de Colomares, Puerto Marina Benalmádena), 1 `Nature` (Dunas de Artola, linked both ways with Cabopino/Artola), 3 `City` (Mijas Pueblo, Fuengirola town, Benalmádena Pueblo) and 7 `Family activities` (Teleférico, Selwo Marina, Parque de la Paloma, Crocodile Park, Sea Life, Mariposario, Maui Paddle Surf, Mijas Golf). Identity and coordinates from Google Places API; drive time from Routes API (Saturday 2026-11-07 10:00). Categories are Claude's choice from the schema definitions (issue `category_editorial_choice`). Boat trips wait for a provider sweep and reputation screen. Validation: 148 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Owner selection for the local extension (no records yet)

Read the owner's 49 answers from the checklist page and recorded them in `docs/decisions/local-extension-selection-2026-11-02.md`: yes 38 (9 everyday life, 6 nature, 7 towns and culture, 8 experiences, 8 events), maybe 8 (four museums or sights, the stupa, riding club, sports centre, Spanish lessons), no 3 (library, vet, laundry). No place record, ID or register was changed.

## 2026-11-02 - Owner decisions on the local extension (no schema change)

All five areas are in scope; everyday life goes on a separate practical-information page and events in a monthly season calendar, so no new category is needed. A private checklist page was published for the owner's selection. Recorded in `docs/owner-decisions-2026-11-02.md` (6-9).

## 2026-11-02 - Local extension candidate list (intake only, no records)

Owner request: guests stay a few weeks across a long season. Added `docs/decisions/local-extension-intake-2026-11-02.md`: 41 candidates in four groups (everyday life, nature and walks, towns and culture, longer-stay experiences) with Google Places identity and Routes API drive times, plus a list of yearly events without dates. Two structure questions for the owner (where everyday-life places and events belong, since neither fits the six categories). No place record, ID or register was changed.

## 2026-11-02 - Alfil own Facebook page; Sould Park chain page (no schema change)

- `multicines-alfil-fuengirola`: own Facebook page (owner screenshot): eight screens, three with 3D X-PAND, opera and ballet season September 2026-May 2027, phone +34 952 59 35 87. Prices, parking and accessibility still open.
- `sould-park-fuengirola`, `sould-park-bowling-miramar`: the chain's Facebook page has nothing venue-specific; noted on the open issues with its WhatsApp contact.
- Validation: 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Zero Latency own Facebook page (no schema change)

`zero-latency-miramar`: own Facebook page (owner screenshot) confirms online booking, Spanish and English, active posting (30 October) and phone +34 951 81 11 05, which settles the phone discrepancy with Google. Validation: 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Bolera Mijas facilities from its own page (no schema change)

`bolera-mijas-dubai-boll`: own Facebook page (owner screenshot) confirms restaurant, bowling, children's area, bouncy castle, arcade and an indoor trampoline area for the Mijas venue; the owner's impression (mostly adults and seniors) is kept beside it. Issue narrowed to `hours_and_prices_unverified`. Validation: 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Zero Latency voucher prices; Bolera leads (no schema change)

- `zero-latency-miramar`: gift-voucher price €29.95 per ticket and group-booking contact from the own booking site (owner screenshot); `prices_not_readable` lowered to info `booking_prices_unconfirmed`; phone discrepancy between Google and the operator noted.
- `bolera-mijas-dubai-boll`: owner screenshot showed only a Google AI overview; its claims (8 lanes, extra games, hours, offers) are noted on the open issue as leads, not recorded as facts.
- Validation: 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Cosmozone price list from owner screenshot (no schema change)

`cosmozone-lasertag`: prices and pack contents from the venue's own price list (owner screenshot of cosmozone.es/en/, which Firecrawl cannot read): 1-hour laser tag €18 Mon-Fri / €20 weekends, 2-hour pack €28/€30, birthday pack €26/€28 (min. 10), extra room games €3/€4, Laser Maze from age 9. Issue narrowed to `hours_not_readable`. Validation: 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Fuengirola (centrum) re-approved (owner decision)

`fuengirola-centro`: `needs_fact_check` -> `approved` by the owner after the older-people zone was added; `reopened_for_addition` closed; new `review_decision` recorded. Validation: 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Older-people zone stays in Fuengirola (centrum) (owner decision)

The owner decided to keep the Playa de San Francisco bathing zone for older people in `fuengirola-centro` despite San Francisco lying north of the port. Issue `reopened_for_addition` updated; the record stays `needs_fact_check` until the owner re-approves it. Validation: 0 errors.

## 2026-11-02 - Owner decisions on beaches (no schema change)

- `fuente-de-la-salud`: owner approved the family assessment (all four audiences `medium`; Children, Young adults, Seniors); `subjective_assessments_need_human_review` closed.
- `cabopino-artola`: `toilets_available: yes` from the owner's own local knowledge; `toilets_listed_but_unverified` closed.
- `fuengirola-centro`: summer bathing zone for older people at Playa de San Francisco added with municipal sources; status `approved` -> `needs_fact_check` (material addition), previous `review_decision` cleared and noted on new issue `reopened_for_addition`; needs the owner's re-approval. Correction the same day: Playa de San Francisco lies north of the port (towards Los Boliches) while the record's point is south of it; wording changed to say so, and the owner is asked to confirm the zone belongs in this record.
- Decisions recorded in `docs/owner-decisions-2026-11-02.md` and `docs/decisions/family-assessment-decisions-2026-11-02.md`. Validation: 128 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Beach follow-ups (handoff point 5, no schema change)

- `boliches-gaviotas`: bathing zone for older people resolved - it is at Playa de San Francisco by the port (Fuengirola council 2021, Fuengirola TV 2023, Fuengirola Accesible 2025), not on this beach. Description corrected; `elderly_bathing_zone_location_disputed` closed. The approved `fuengirola-centro` record was not edited; adding the zone there needs the owner (a material change re-opens fact check).
- `santa-ana-benalmadena`: Blue Flag 2026 confirmed by Diputación de Málaga; Benalmádena (21 Aug 2026) lists loudspeaker points at Santa Ana and Torrebermeja. No 2026 source names a lifeguard post on this beach; issue kept and updated.
- `cabopino-artola`: Diputación de Málaga's beach sheet lists no toilets (spain.info does); `toilets_available` stays unknown.
- `chiringuito-rafael`: identity corroborated by independent listings; `weak_identity_source` lowered to info; season and hours still open.
- `chiringuito-las-dunas-cabopino`: no new source on winter opening. `fuente-de-la-salud`: family assessment awaits the owner (the earlier blocker, rocks, was settled by the 2026-11-02 rule).
- Validation: 128 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Three bars archived; MOGA has no own page (owner decisions)

Owner decision: `bar-meson-campanales` (inactive since 2016), `el-rimero` (wine shop, inactive since 2020) and `terraza-chill-out-bar` (inactive since 2021) are removed from the guide. Status -> `archived` with a `review_decision` from the editor-of-record; records and IDs stay (IDs must not be reused). `moga-la-cala`: the owner could not find an own page either; it stays `draft` with the issue updated. Validation: 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Last three bars from owner screenshots (no schema change)

- `draft` -> `needs_fact_check` (2): `la-senda-del-norte` (café-bar with a covered street terrace; no hours or prices on its page), `mon-2-sun` ("the friendly family/community bar" at La Hacienda, Mijas Golf; outdoor seating, price range "cheap"; latest post December 2024 and mon2sun.es gone, issue `activity_unverified`).
- `terraza-chill-out-bar` stays `draft` with blocking `possibly_closed`: own page inactive since June 2021 and its phone number is a placeholder. Suggested: archive.
- Validation: 128 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Four more bars from owner screenshots (no schema change)

- `draft` -> `needs_fact_check` (2): `la-floja-vinos-y-latas` (own Facebook page confirms address and phone +34 952 31 47 63; hours and prices still unknown), `groove-bar-fuengirola` (renamed to its own name **Groove Music Bar**, ID and slug unchanged, registry name updated; live music Wednesday-Sunday, jam session Wednesdays 21:30, DJ Thursdays 23:00, food such as wings and pizza; new issue `hours_prices_and_entry_unknown`).
- Stay `draft` with a blocking issue for the owner: `bar-meson-campanales` (own Facebook page inactive since May 2016; `possibly_closed`), `el-rimero` (own page describes a wine shop, on/offline retail, not a bar; no activity since 2020 and elrimero.com gone; `not_a_bar_possibly_closed`). Suggested: archive both.
- The Café Teatro screenshot was the same as before; no change. Validation: 128 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Five more bars from owner screenshots (no schema change)

- `draft` -> `needs_fact_check` (4), from the venues' own Facebook pages (`official_venue`, medium): `bar-burbujas` (late-night sparkling-wine cocktail bar, open Friday and Saturday from 22:00, "since 1986"; issue `closing_time_and_prices_unknown`), `la-terraza-de-panda` (terrace by the church on Plaza de la Constitución, open seven days from 12:00 per a post of 2 Nov 2026), `changueiro-bar-de-vinos` (hours from an undated image: Mon, Thu-Sat 12:00-16:00 and 19:00-23:30, Sun 12:00-16:00, closed Tue-Wed; `hours_conflicting` replaced by `hours_image_undated`), `red-and-white-fuengirola` (wine bar and Mediterranean restaurant; hours and prices unknown).
- `sky-bar-veramar` stays `draft`: season and hours come only from a 2025 schedule image uploaded by a Google Maps user (`secondary`, low); per that schedule the bar is open mid-April to 31 October and closed in winter. New issue `season_from_user_photo`.
- One-off event prices (New Year's Eve, Valentine's menu) and personal e-mail addresses not recorded. Validation: 128 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Five bars checked from owner screenshots (no schema change)

The owner supplied screenshots of Facebook pages. Facts taken from the venues' own pages (`official_venue`, medium confidence); review ratings, follower counts and personal e-mail addresses were not recorded. All three websites linked from the pages are gone (noninafuengirola.com and gruponautic.es do not resolve; cafeteatrofuengirola.com is a parked domain).

- `draft` -> `needs_fact_check` (4): `nonina-fuengirola` (flamenco bar at the port; posts tie it to the Feria de Fuengirola 2026, new issue `possibly_seasonal_venue`), `retrock-bart` (rock bar, Paseo Costa del Sol 10, price range "cheap", dogs on a lead welcome; latest post December 2025, new issue `activity_unverified`), `nautic-bar-fuengirola` (renamed to its own name **Nautic Cocktail & Drinks**, ID and slug unchanged, registry name updated; gin and premium-spirits bar; latest post August 2023, `activity_unverified`), `cafe-teatro-ocean-drive` (lounge terrace with live music and cocktails, current event posters; house number 4 on own page vs 5 on Google, new issue `hours_prices_and_entry_unknown`).
- `moga-la-cala` stays `draft`: only a third-party reel (new opening, 19 July, year not shown) recorded as `secondary`, low confidence.
- Validation: 128 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Jay Jangles archived (owner decision)

Owner decision: `jay-jangles` is removed from the guide; sources describe a nursery for enrolled children aged 1-6, not a visitor activity. Status `draft` -> `archived` with a `review_decision` from the editor-of-record; the record and its ID stay (ID must not be reused). The blocking issue `not_a_visitor_activity` is kept as the reason. Validation: 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Equestrian Centre archived (owner decision)

Owner decision: `equestrian-centre-chaparral` is a riding school, not a drop-in attraction, and is removed from the guide. Status `draft` -> `archived` with a `review_decision` from the editor-of-record; the record and its ID stay (ID must not be reused). Validation: 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Mixs Longe identified from the owner's screenshot (no schema change)

The owner supplied a screenshot of a Google search showing the venue's own Facebook page (`facebook.com/p/Mixs-Longe-61550506887933/`) and its Google listing. `mixs-lounge`: name corrected to the venue's own spelling **Mixs Longe** (ID and slug unchanged; registry name updated); own page describes a new Scandinavian and Italian restaurant in Cerros del Águila at Calle Buitre 45; Google lists it as Indian with phone +34 632 13 47 36, and Uber Eats has "Mixs Curry & Pizza" on the same street, so cuisine is left as an open issue. Google hours, the user-reported price range and Google's AI overview were not recorded. Closed `name_unconfirmed`, `no_official_website` and `facts_not_checked`; new `cuisine_and_hours_unverified`. Status `draft` -> `needs_fact_check`. Validation: 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Nearby fact check, batch 4: remaining activities (no schema change)

Checked against the venues' own, operator, council or shopping-centre sources on 2026-11-02.

- `draft` -> `needs_fact_check` (7): `mk2-cinesur-miramar` (price list incl. under-12 and over-65 rates, free parking, 3D, bar, bus lines 1/4/5; accessibility not stated), `multicines-alfil-fuengirola` (programme incl. children's films and opera/ballet broadcasts; no prices or facilities on the website), `zero-latency-miramar` (standard hours, arena over 200 m², up to eight players, 15-30 min games; new warning `minimum_age_conflict`: Málaga page says no fixed minimum age with a minimum height, chain FAQ says 13+), `bolera-mijas-dubai-boll` (bowling, bar, karaoke and sport screens from the chain's Mijas page; other games may be copied from the Jaén venue; hours only from conflicting third-party sources, not recorded), `parque-el-esparragal` (fenced play area with 20 m zip line, swings and barbecues from Mijas council sources dated 2021; issue `sources_dated_2021`), `cosmozone-lasertag` (terms: no under-6s, under-15s need an adult in their team, 48 h cancellation; hours and prices still inside an unreadable booking widget), `sould-park-bowling-miramar` (opened June 2026 per CC Miramar: four lanes, 50+ arcade machines, pool, table football; operator: no bar at this venue, shoes free, prices shown when booking).
- Still `draft`: `jay-jangles` - sources (Olive Press 2015, directory) describe a nursery for enrolled children aged 1-6, not a visitor play centre; new blocking issue `not_a_visitor_activity` for the owner (archive or confirm a drop-in offer). `sould-park-fuengirola` - the operator only lists Fuengirola with a map link; `details_not_readable` updated.
- Search excerpts with prices (Instagram, Facebook) were noted on review issues but not recorded as facts.
- Validation: 128 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Bars fact check; Bamboleo merged into La Zambra (owner decisions, no schema change)

- Owner decision: Bamboleo is described under La Zambra Resort; `bamboleo-la-zambra` archived (ID kept), La Zambra description and evidence updated. The owner does not know Mixs Lounge or Equestrian Centre either; noted on their issues.
- Bars checked against own websites and social pages on 2026-11-02 (`draft` -> `needs_fact_check` for four): `upstairs-rooftop-bar` (non-smoking rooftop, daily 16:00-22:00, everyone welcome, no booking; tag `Viewpoint`), `lounge-el-tropico` (beach bar, 09:30-00:00 April-November, food, sunbeds; tag `Beach`), `el-oceano-beach-hotel` (restaurant with live music almost every evening, pool bar), `speakeasy-jazz-club-fuengirola` (concert tickets at 23:30, €56/€84 options; terms unclear).
- Own channels found but not readable or incomplete: La Floja (address only), Changueiro (Instagram; hours conflicting), La Terraza de Panda (Instagram), Red & White (Facebook), Bar Burbujas, Terraza Chill Out, La Senda del Norte, Groove Bar. Sky Bar Veramar's listed website returns 404. No own source found: MOGA, Nautic, Café Teatro, Noniná, RetROCK BARt, Mon 2 Sun, El Rimero, Bar Mesón Campanales.
- Validation: 128 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Walking times of 20 minutes or more removed (owner decision)

Owner decision: show walking time only where guests can realistically walk. In 27 nearby records with a Google walking time of 20 minutes or more, the walking time was removed from `description_short`, `description_long`, the drive-time note and the route evidence; only the drive time remains. The 11 records under 20 minutes on foot keep it (Mixs Lounge, Singh Doner Kebab, Restaurante Cerros del Águila, El Gran Parque de Mijas, Equestrian Centre, Peña Al Tranco and the five buggy/quad operators). Intake doc annotated. Validation: 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Bars: walking times replaced by taxi/Uber wording (owner decision)

Owner decision: walking times make no sense for bars in town; guests go by taxi or Uber. In the 22 bar records the walking time was removed from `description_long`, the drive-time note and the route evidence; descriptions now give the time "by car, taxi or Uber" and advise a taxi or Uber both ways when drinking. Intake and selection docs updated. Validation: 0 errors.

## 2026-11-02 - 22 bar draft records created; ByCosmos Skybar removed (owner decisions, no schema change)

Owner selection and reputation screen in `docs/decisions/bars-selection-2026-11-02.md`. ByCosmos Skybar removed by owner decision after the screen (no record). Created 22 draft records (21 bars plus El Oceano Beach Hotel), category `Restaurants`, IDs allocated, with Google identity, Routes API drive and walking times, a general drink-safety note and taxi advice in each description, and open issues for facts, audience and the owner not having visited. Bamboleo linked to La Zambra Resort. Validation: 128 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Zooloco Party archived (owner decision)

Owner decision: remove Zooloco Party from the guide (a private party room for hire, not a drop-in attraction). `docs/places/zooloco-party.md`: status `archived` with `review_decision`; the record is kept and its ID stays allocated. Owner bar selection saved the same day (22 of 27 candidates plus El Oceano Beach Hotel); reputation screening of the selected bars was reported to the owner before any record is created. Validation: 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Bars and cocktail bars candidate list (intake only, no records)

Owner observation: the guide lacks places for adults and seniors, especially bars and cocktail bars. Added `docs/decisions/bars-intake-2026-11-02.md`: 27 bars, wine bars, cocktail and rooftop bars within about 16 minutes' drive (2 within walking distance, 7 in Las Lagunas/Mijas Golf, 14 in Fuengirola, 4 in La Cala de Mijas), with Google Places identity and Routes API walking and driving times. No place record, ID or register was changed.

## 2026-11-02 - Nearby fact check, batch 3: activities a short drive away (no schema change)

Checked against the venues' own websites on 2026-11-02.

- `needs_fact_check` now: `jumpjoy-mijas` (indoor, air-conditioned park over 5,000 m², age zones, grip socks, hours; tag `Rainy day`), `bioparc-fuengirola` (open daily from 10:00, ~3 h visit, under-3s free, child rate 3-9, fully accessible, café, no outside food, no pets, discounted car park opposite), `fuengirola-adventure-golf` (19 holes, ~1 h, bar and restaurant), `karting-experience-miramar` and `karting-experience-mijas` (track descriptions; price lists not clearly tied to each track), `aqualand-torremolinos` (opening days in November 2026, 10:00-17:00/18:00), `zooloco-party` (private party room for hire only; new warning `private_hire_only` for the owner).
- Not readable, still `draft` with `details_not_readable`: `cosmozone-lasertag`, `sould-park-fuengirola`, `sould-park-bowling-miramar`.
- Not yet checked: cinemas (mk2 Miramar, Alfil), Zero Latency, Bolera Mijas, Jay Jangles, Parque El Esparragal.
- Validation: 106 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Restaurante Cerros del Águila: own Facebook page (no schema change)

The owner supplied a screenshot of the restaurant's own Facebook page (profile id 100054645841442). Recorded as an `official_venue` source: Spanish restaurant, outdoor seating, dine-in, phone +34 952 66 81 91, address Urbanización Cerrado del Aguila s/n. "Always open" is not recorded as a schedule. `no_official_source_found` replaced by `hours_and_prices_unverified`; status `draft` -> `needs_fact_check`. Validation unchanged (0 errors). Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Nearby fact check, batch 2: eleven records (no schema change)

Walkable places and the Camino Viejo de Coín restaurants, checked 2026-11-02.

- Buggy and quad operators, from their own websites (status `draft` -> `needs_fact_check`): `rangers-safari-tours` (type-B licence, children from 6 with a licensed parent, 30% deposit), `aventouralia` (same rules, 50% deposit; same address as Rangers), `atv-adventures-mijas` (passengers from 4 in buggies and 6 on quads, 1/2/3 h tours, "from €80"), `mijas-buggys` (2 h and 3 h tours, 1 h sunset tour June-September, per-buggy prices; minimum ages not found, issue kept).
- `restaurante-hoyo-19`: own site gives address and phone; hours by weekday unclear (`needs_fact_check`).
- Still `draft`, with a new issue: `mixs-lounge` (`name_unconfirmed`: Google/Just Eat "Mixs longe", Uber Eats "Mixs Curry & Pizza"), `equestrian-centre-chaparral` (`identity_unclear`), and `no_official_source_found` for `singh-doner-kebab`, `sol-y-sombra-mijas`, `pena-al-tranco` and `el-mirador-del-golf`.
- Validation: 106 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Nearby fact check, batch 1: seven records (no schema change)

Checked against the venues' own or official sources on 2026-11-02; status `draft` -> `needs_fact_check` for all seven.

- `aquamijas`: own website (visit and ticket pages) - 2026 season from 1 May, closed from 14 September 2026, hours 10:30-18:30, 2026 prices including afternoon tickets from 15:00 (confirms the owner's off-peak note), under-13s accompanied, free customer car park, food on site and own food allowed. Seasonality Spring/Summer from those dates.
- `bigfoot-buggy-tours`: own safety page - type-B driving licence to drive, passengers from 4 years with booster seats (1 m recommended), seat belts, closed-toe shoes. `age_and_licence_rules_unknown` closed; tour lengths and prices only in the booking system.
- `asador-otola`: own website - Basque asador, hours (Wednesday closed), phone. Prices, booking and children's facilities not stated.
- `el-gran-parque-de-mijas`: Mijas Town Hall (12 June 2026) - splash park with 41 water features, daily 10:00-22:00 in season, age zones 1-3 / 4-9 / 10-11, under-8s accompanied; municipal media report the season has closed. Rest of the park unsourced.
- `la-zambra-resort`: Hyatt page - four restaurants plus Sarao, Mood Spa, kids' clubs for hotel guests. New warning `non_guest_access_unknown`.
- `venta-la-morena`: own Facebook page found but not read; Google's "website" is a directory page.
- `restaurante-cerros-del-aguila`: no official source found; new warning `no_official_source_found` (owner knowledge stays).
- Validation: 106 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - 38 nearby draft records created (owner selection, no schema change)

The owner selected all 37 candidates from `docs/decisions/nearby-intake-2026-11-02.md` and added La Zambra Resort (`docs/decisions/nearby-selection-2026-11-02.md`). Created 38 records with status `draft` and allocated IDs: 15 `Restaurants` (including La Zambra Resort) and 23 `Family activities`. Identity and coordinates from Google Places API; drive time from Routes API (Saturday 2026-11-07 10:00, predicted traffic) with Routes API walking time in the note and description; owner notes recorded as owner knowledge; Aquamijas season from its own website (search excerpt). Opening hours, prices, age rules, facilities and family suitability are open review issues. Validation: 106 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Nearby places candidate list (intake only, no records)

New focus from the owner: restaurants and family activities very close to Casa de la Familia, preferably within walking distance. Added `docs/decisions/nearby-intake-2026-11-02.md`: 14 restaurants/bars and 23 activities/parks with Google Places identity and Routes API walking and driving times (2026-11-02). Season status from official sites for Aquamijas (closed from 14 September 2026) and Aqualand Torremolinos (open into October 2026). No place record, ID or register was changed.

## 2026-11-02 - Eight local beaches approved by the owner (no schema change)

Owner decisions in `docs/decisions/approval-decisions-2026-11-02.md` (second round, new approval page). `castillo-ejido`, `la-butibamba`, `carvajal`, `el-bajondillo`, `fuengirola-centro`, `la-carihuela`, `los-alamos` and `playamar`: `needs_editorial_review` -> `approved`, with `review_decision`, energy level Low and character label confirmed, `last_reviewed_at` 2026-11-02 and `next_review_at` 2027-04-01. Remaining info notes closed and quoted in the decision notes; "draft" wording removed from SEO title/description and `description_short`. Not published. Validation: 68 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - New rocks rule for beaches; Fuengirola centro point moved (owner decisions)

Owner decisions in `docs/owner-decisions-2026-11-02.md`.

- Rocks rule (also added to `AGENTS.md`): only pure rock beaches, and beaches reached by climbing down rocks, are excluded; rocks on a sand beach do not exclude a beach. Applied to the seven beaches where rocks were still open (Carvajal, El Bajondillo, Fuente de la Salud, La Carihuela, Los Álamos, Playamar, Santa Ana): each is a sand beach with easy access on foot per spain.info / andalucia.org and the municipal accessibility sources, so `rocks_not_verified` is closed with a rule-check evidence entry and the description's rocks sentence is updated.
- Fuengirola centro: the point moves from the owner-read marker (36.5573, -4.6095, near Las Gaviotas) to Google's "Playa de Fuengirola" (36.5372915, -4.6215859), between the marina and the bridge over the Río Fuengirola, as the owner asked. Driving time re-checked with Routes API: 14 min, 6.2 km (Saturday 2026-11-07 10:00, predicted traffic; previously 17 min to the old point). `coordinates_far_from_named_beach` closed. `data/route-checks-2026-11-01-local.csv` is not changed (historical batch).
- Status `needs_fact_check` -> `needs_editorial_review` for the records left with only info-level issues: Carvajal, El Bajondillo, La Carihuela, Los Álamos, Playamar and Fuengirola centro. Santa Ana (2026 services) and Fuente de la Salud (family assessment not approved) stay in `needs_fact_check`.
- Validation: 68 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Six restaurants approved by the owner (no schema change)

Owner decisions in `docs/decisions/approval-decisions-2026-11-02.md`. `los-marinos-paco`, `chiringuito-cristobal`, `chiringuito-los-moreno`, `la-mar-sala`, `morrofino` and `santa-ana-denis`: `needs_editorial_review` -> `approved`, with `review_decision`, `last_reviewed_at` and energy level Low confirmed; remaining info notes closed and quoted in the decision notes; "draft record" removed from SEO title/description. These are the first approved records in the catalogue. Not published. `castillo-ejido` and `la-butibamba` got no decision and stay in `needs_editorial_review`. Validation: 68 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Owner-approved family assessments written; eight records to editorial review (no schema change)

- The owner corrected and approved the family assessment for 18 of 20 records (`docs/decisions/family-assessment-decisions-2026-11-02.md`). `age_groups` and `family_score` were written into those records, with an evidence entry each. `subjective_assessments_need_human_review` / `family_suitability_not_assessed` were closed and replaced by the info-level issue `energy_level_editorial_estimate` (energy, and for beaches the character label, still to be confirmed at editorial review). Not approved and unchanged: Chiringuito Rafael and Fuente de la Salud.
- Owner knowledge added to descriptions with evidence entries: Cabopino-Artola (very fine sand, not deep quickly, nudism only on a smaller part, small harbour with restaurants), Castillo-Ejido (Marenostrum concert venue is part of the area), La Butibamba (towards La Cala centre more child-friendly, with parasols and sunbeds), Carvajal (mixed sand, gravel and stones).
- Status `needs_fact_check` -> `needs_editorial_review` for the eight records left with only info-level issues: Castillo-Ejido, La Butibamba, Los Marinos Paco, Chiringuito Cristóbal, Chiringuito Los Moreno, La Mar Salá, Morrofino and Santa Ana Denis. Not approved; the editor-of-record decides.
- Validation: 68 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Family assessment proposal for beaches and restaurants (proposal only)

Added `docs/decisions/family-assessment-proposal-2026-11-02.md`: proposed `age_groups` and `family_score` for the 12 local beaches and 8 restaurants (owner decisions 2 and 6), with the rubric and the sourced facts behind each value. No record was changed; the values wait for the owner's corrections. Progress note added to `docs/decisions/approval-decisions-2026-11-01.md`.

## 2026-11-02 - Beaches: Google Maps links, official beach data, unsourced claims removed (draft, no schema change)

Next-session step 3 from `docs/decisions/approval-decisions-2026-11-01.md`, for the 12 active local beaches.

- Google Maps links: `google_maps_url` and `external_ids.google_place_id` from Google Places API (New), with a `maps_identity` evidence entry; `google_maps_url_missing` closed. Boliches-Gaviotas uses the Playa de las Gaviotas listing (the record point is on it); Castillo-Ejido uses Playa del Ejido (about 180 m from the point, which is at the Castillo Sohail).
- New warning `coordinates_far_from_named_beach` on Fuengirola centro: the accepted point lies about 2.5 km north-east of Google's "Playa de Fuengirola" (by the centre and port) and north of the Boliches-Gaviotas point. Coordinates not changed; owner to check.
- Sand, size, waves, occupancy and listed services now come from spain.info (Turespaña official tourism portal, data from the national beach guide, undated). For Fuente de la Salud the source is andalucia.org (Junta de Andalucía), which also gives adapted toilets (`toilets_available: yes`). All evidence entries without a source URL were removed together with their claims in `description_long`: snapshot child-friendliness statements ("often recommended for children", "family-oriented", gentle slope), the anecdotal Facebook replies, unnamed or unverified beach bars, and unsourced "nearby" items. Beach descriptions now name only verified restaurant records ("see the linked record").
- Notable differences from the old snapshot: Carvajal is listed as dark sand with gravel and cobbles (*bolos*), not "fine golden sand" (noted on `rocks_not_verified`); Castillo is white sand with a fenced dog-beach section; La Butibamba is listed as dark sand, while the owner's own knowledge (stones) is kept and the difference stated.
- Closed: `secondary_sources_unverified`, `source_urls_missing`, `snapshot_restaurant_misidentified` (Castillo-Ejido), `snapshot_restaurants_wrong_beach` (La Carihuela), `lively_atmosphere_not_rated` (Los Álamos; the claim had no source). `description_short`/`seo_description` no longer call the record a snapshot draft.
- Validation: 68 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-02 - Owner decisions 1, 3, 4, 5, 7 and 8 applied to beaches and restaurants (draft, no schema change)

Applied the owner answers of 2026-11-01 (`docs/decisions/approval-decisions-2026-11-01.md`) to the 12 active local beaches and 8 restaurants. Each record gets one evidence entry per decision, pointing to the decisions file (`source_type: secondary`, the nearest schema value, with a note that it is an editor decision, not an external source). Status values are unchanged.

- Decision 1 (all 12 beaches): owner-read Google marker accepted as the place point; `coordinates.source` and the drive-time note updated; `route_and_coordinates_owner_measured` closed.
- Decision 3 (all 12 beaches): `seasonality` = `Spring`, `Summer`, `Autumn`; `seasonality_unknown` closed.
- Decision 4: no rocks for Boliches-Gaviotas, Cabopino-Artola, Castillo-Ejido, Fuengirola centro and La Butibamba (`rocks_not_verified` closed; description updated). La Butibamba: owner clarified on 2026-11-02 that it is a stone beach (walnut- to plum-sized stones), not a rocky one; `rock_claim_source_conflict` closed. For Carvajal, El Bajondillo, Fuente de la Salud, La Carihuela, Los Álamos, Playamar and Santa Ana the owner does not know, so `rocks_not_verified` stays open with that noted. The old unsourced "rocks not mentioned" evidence entries were removed in all 12 beaches.
- Decision 5 (all 12 beaches): practical details deliberately unknown; `practical_details_out_of_scope` closed and the decision kept as an evidence entry.
- Decision 7 (8 restaurants): prices and season stay unknown with a "check before visiting" sentence in `description_long`; `season_and_prices_unverified` closed. Chiringuito Las Dunas keeps `winter_opening_unclear`.
- Decision 8 (8 restaurants): practical details deliberately unknown; `practical_details_unverified` closed. Los Marinos Paco keeps its venue-confirmed `dog_friendly: partial` and `booking_required: false`.
- Validation: 68 records, 0 errors. Regenerated `data/place-catalog.csv`.

## 2026-11-01 - Owner approval decisions recorded (not yet applied)

The owner answered eight shared approval questions for the local beaches and restaurants (coordinates, family assessment, seasonality, rocks per beach, out-of-scope practical details, restaurant prices and season). Answers and the next-session plan are in `docs/decisions/approval-decisions-2026-11-01.md`. No record was changed in this entry.

## 2026-11-01 - Six legacy import drafts: provisional energy level and archive decision

Owner request: clear the six long-standing validation errors (`energy_level` None) in `cares`, `conil-de-la-frontera`, `cueva-de-los-arcos`, `miradouro-da-serpente-do-medal`, `roca-foradada` and `salt-de-la-coromina`. Owner decision the same day: give them provisional energy values and archive them.

- `energy_level` set as a provisional editorial estimate from the place type: Cares `High`, Conil de la Frontera `Low`, Miradouro da Serpente do Medal `Low`, Cueva de los Arcos, Roca Foradada and Salt de la Coromina `Medium`. Each record has a `energy_level_provisional` warning.
- Archive: all six are outside `local_30km` and in no excursion layer (archive under AGENTS.md); Miradouro da Serpente do Medal is in Portugal, out of scope since 2026-10-16. Their status stays `draft` because the validator requires an allocated ID outside `draft`, and allocation needs the unresolved identity (province/region) first; guessing it would break the stable-ID rule. Each record carries an `archive_out_of_scope` note with the owner decision. No schema or validator change.
- `python3 tools/places.py validate` now reports 0 errors (68 records). Regenerated `data/place-catalog.csv`.

## 2026-11-01 - Los Monteros archived (owner decision)

Owner decision: remove Los Monteros (Adelfas), Marbella, from the guide. The editor's reasoning is that the area is best known for Nikki Beach, an adult venue for young, affluent visitors, which does not fit the family audience (editorial judgment, not a fact-checked claim).

- `docs/places/los-monteros.md`: status `draft` -> `archived`, with `review_decision` recording the decision. The record is kept as archive, not deleted; ID `ES-AND-MAL-LOS-MONTEROS-001` stays allocated in `data/place-id-registry.csv` and must not be reused.
- No other record linked to it. Historical mentions in `data/route-checks-2026-11-01-local.csv`, `docs/decisions/beach-draft-open-points.md` and earlier change-log entries are left as they were. Regenerated `data/place-catalog.csv`.

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
- Applied later on 2026-10-29 (separate commit on branch `strande-kladder`): Malaga, Tolox and Marbella old town moved to `excursions_4h` in `data/layer-membership.csv`; the `local_30km` rule text in `data/layers.csv` and `AGENTS.md` line 9 now state the driving-time rule; `docs/decisions/excursions-layer-overlap.md` updated for Marbella old town. Still open: `tools/places.py` keeps a straight-line helper column (`within_primary_radius`, 30 km) that no longer decides layer placement; the other open points above remain.
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

Editor-approved schema change: age groups `Teenagers (13-17)` and `Adults` merged into `Young adults`; `family_score` keys `teenagers` and `adults` merged into `young_adults` (rule: max; `unknown` if either input is unknown). Updated: all `docs/places/*.md`, `tools/places.py` constants, `data/personas.csv` (weights summed), `AGENTS.md`, `docs/place-schema.md`. Analytical datasets and the engine spec were not migrated by this commit; see `docs/decisions/schema-change-proposal-young-adults.md` and issue #5 for the follow-up below, which completes that work.

## 2026-10-16 — Young adults migration: analytical datasets and recommendation engine (closes #5)

Completes the follow-up issue #5 raised by the schema migration above. Two PRs, in order:

- **`data/destination-metadata.csv`**: merged `teen_score`/`adult_score` into a single `young_adult_score` column, same max rule as the schema migration. **`docs/engine/recommendation-engine-spec.md`**: `base_score` formula and factor list updated to use `young_adult_score`/`young_adult_suitability_weight` (this also fixed a real bug — the spec still referenced `teen_suitability_weight`/`adult_suitability_weight`, which `personas.csv` no longer had since the original migration already merged them). **`docs/data-dictionary.md`** and **`docs/engine/guest-questionnaire-spec.md`**: column references updated to match. **`docs/examples/*.md`** (4 files): illustrative `age_groups`/`family_score` examples updated to `Young adults`, merged with the same max rule, so they don't teach the deprecated taxonomy.
- **`docs/history/end-to-end-demo.md`**: all 10 worked guest-session scenarios recomputed against the current formula and data (a throwaway script implementing the spec exactly); 7 of 10 changed ranking or top-5 membership, since several destinations had `teen_score` ≠ `adult_score` pre-merge. A genuine exact tie in scenario 5 (aviation enthusiast) is broken alphabetically and noted in the document, since the engine spec defines no tie-break rule. **`docs/engine/group-composition-v2.md`**: this document's party-composition formula weights age-suitability terms by headcount rather than selecting a persona-level score, so the main migration's max-rule approach didn't directly transfer; teenager and adult headcounts now combine into one `(teenagers + adults) × young_adult_score` term, and all 4 worked examples were recomputed. This collapses `party_suitability` to exactly `young_adult_score` for an all-adult/teenager party (Example 2), which is flagged explicitly in the document as a real behavior change, not just a rename.

Deliberately **not** migrated, per editor review (see issue #5 and the original proposal): `data/demo-groups.csv` (headcounts describing a synthetic test group's composition, not suitability scores — merging would lose information), `docs/content/gold-standard-sample-set.md` (uses "teen"/"adult" as ordinary English in editorial prose, not as schema field references), `docs/history/discrimination-analysis.md` (a historical analysis snapshot of the old data, not a live spec). `README.md` and `demo/index.html` were checked and already carried no stale references.

`python3 tools/places.py validate` unaffected both times (same 6 pre-existing errors in unrelated archive records).

## 2026-10-15 — Excursion layer (additive; no schema change)

Owner decision: add a second layer, `excursions_4h` (route-checked one-way drive up to about 4 h), beside the 30 km primary area.

- Added 17 draft records in `docs/places/` (Málaga, Sierra de las Nieves, Tolox, Caminito del Rey, Setenil de las Bodegas, Antequera, El Torcal de Antequera, Nerja, Tarifa, Vejer de la Frontera, Granada, Sevilla, Córdoba, Cádiz, Jerez de la Frontera, Gibraltar, Las Alpujarras). All `draft`, no coordinates, no route-checked driving time, no sourced facts; blocking review issues on each.
- Reserved the 17 IDs in `data/place-id-registry.csv` and added 17 rows to `data/import-queue.csv`.
- Added `data/layers.csv` and `data/layer-membership.csv`.
- Added persona `Young adults` to `data/personas.csv` (weights are editorial estimates).
- Added the scope section to `AGENTS.md` and a bullet to `README.md`; added `docs/decisions/excursions-layer.md` and `docs/decisions/excursions-layer-overlap.md`.
- Not changed: existing place records, categories, tags, enums, schema. The merge of `Teenagers (13-17)` and `Adults` into `Young adults` is a separate proposal: `docs/decisions/schema-change-proposal-young-adults.md`.

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

Applied the P0 contract decisions and P1 operational design from `docs/history/remediation-plan.md`. This update changes project guidance and specifications; it does not implement executable validators, create registry/queue data files, migrate standalone examples, or publish place records.

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
