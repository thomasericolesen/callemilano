# Overdragelse til Codex (OpenAI) – CalleMilano

**Skrevet:** 4. november 2026 kl. 16 (dansk tid) af Claude (Claude Code), på ejerens ønske.
**Ejer og redaktør:** Eric Olesen (GitHub `thomasericolesen`). Al kommunikation med ejeren foregår på dansk.
**Formål:** Codex overtager udviklingsopgaverne helt eller delvist. Filen er selvstændig. Læs den først, og derefter `AGENTS.md` i begge repoer.

---

## 1. Projektet på ét minut

CalleMilano er en privat, dansksproget familie- og turguide til feriehuset **Casa de la Familia** (Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga). Guiden bruges **under opholdet**: "Hvad laver vi i dag?". Hjemmesiden er https://callemilano.dk (Google-login, kun familien).

To repoer:

| Repo | Indhold | Lokal mappe (Claude) |
|---|---|---|
| `thomasericolesen/callemilano` | **Steder og data:** stedposter (`docs/places/*.md`, YAML front matter er den kanoniske kilde), værktøjer (`tools/places.py`, `tools/intake.py`, `tools/app_export.py`, `tools/trip.py`), ændringslog, overdragelse | `/home/user/callemilano` |
| `thomasericolesen/callemilano-f388b2be` | **Appen** på callemilano.dk: TanStack Start + React 19, Supabase via Lovable Cloud, udgives af **Lovable** (synkroniserer `main`) | `/home/user/callemilano-f388b2be` |

Produktbeslutninger og retning: `docs/history/status-rapport-2026-11-03.md`, `docs/history/status-rapport-2026-11-04.md`, ejerens produktkoncept v1.1 og `docs/history/handoff-next-session.md`. Beslutninger står med dato i `docs/change-log.md`. Genåbn dem ikke.

## 2. Regler, der altid gælder

- **Læs `AGENTS.md`** i places-repoet (regler for stedposter, kilder, beviser og kategorier) og `CLAUDE.md` og `AGENTS.md` i app-repoet (stack, Lovable, migrationer).
- **Opfind aldrig fakta:** ingen priser, åbningstider, køretider eller børnevenlighed uden kilde. Køretider skal være route-tjekkede. Usikre data markeres.
- **Kun ejeren godkender:** stedposter, kategorier og skema. Agenter sætter højst `needs_fact_check`.
- **Git-arbejdsgang:** arbejd på en branch, og lav én PR pr. levering. Ejeren merger. Pres aldrig og omskriv aldrig historik på `main`, fordi Lovable synkroniserer den. Ingen PR uden at ejeren har bedt om den.
- **Én samlet levering ad gangen (ejerbeslutning 4. november):** Ejeren vil ikke være tester i små ryk. Byg færdigt, test selv, og lav én PR med en testrapport. Bed først ejeren om at merge, når **alt** er pushet. En commit, der pushes efter merge, kommer ikke med, og det er sket flere gange.
- **Hemmeligheder:** Læg aldrig nøgler eller tokens i repo eller chat.

## 3. Appen: hvordan Turforslag virker

Siden `/turforslag` er kun for admins i starten (ejerbeslutning). Admins ser den i menuen.

1. **Frit ønske → steder** (`src/lib/suggest.server.ts`, serverfunktionen `suggestTrip`):
   - Claude (`claude-sonnet-5-5`, Anthropic SDK, `ANTHROPIC_API_KEY`) vælger 1–3 steder fra kataloget.
   - **OpenAI** (Lovable AI Gateway, `LOVABLE_API_KEY`, modellen `openai/gpt-6-astra`) bruges **kun som reserve**, hvis Claude ikke svarer (ejerbeslutning 4. november). Konsensus mellem modellerne er tænkt til udviklingsgennemgang, ikke til turforslag.
   - Serveren beholder kun id'er fra kataloget. "Foreslå noget andet" udelukker steder, der allerede er foreslået (`exclude_ids`).
2. **Data** (`src/lib/trip-plan.server.ts`, `buildTripPlan`, serverfunktionen `planTrip`):
   - **Vejr:** Open-Meteo først. Det svarer ofte 429 fra Lovables delte IP, så met.no "complete" er reserven, med varianterne 3 decimaler → 4 decimaler → compact, plus met.no Sunrise. met.no har ikke regnrisiko i procent for Spanien, og UV kun ca. 2 dage frem.
   - **Trafik:** DGT DATEX II.
   - **Øvrigt:** helligdage (tabellen `holidays`), åbningstider fra stedposten, spisesteder inden for 800 m / 3 km i tre prisbånd, og automatiske tjek.
   - **Afstand mellem stop:** i luftlinje og nu også route-tjekket (se afsnit 6).
3. **Tekst:** Ecco (`src/lib/ecco.server.ts`, `writeTrip`, Claude) skriver dansk tekst ud fra planens JSON. `tidyEcco()` retter kendte modelfejl: "Kør hjemmefra" først, ä/ö → æ/ø og ingen tomme punkter.
4. **Data i appen:** tabellen `recommendations` (kolonnen `guide` jsonb) importeres fra places-repoet. Kør `python3 tools/app_export.py`, og ejeren importerer `data/app-export/places.json` på Admin-siden. Prisbånd: `€` under 20 €, `€€` 20–50 €, `€€€` over 50 € (den midterste hovedret + én drik).

## 4. Selvtest – brug den før og efter hver levering

| Del | Hvad |
|---|---|
| `src/lib/selftest.ts` | 14 scenarier og kontroller af plan, forslag og Ecco-tekst. **Tilføj et scenarie for hver fejl, der findes.** |
| `src/lib/selftest.server.ts` | Kører ét scenarie gennem hele kæden |
| `scripts/selftest-local.mts` | Lokalt mod et øjebliksbillede af databasen og live vejr og trafik; `OPEN_METEO_DOWN=1` efterligner Lovables server |
| `POST /api/selftest` + `scripts/selftest-remote.mts` | Samme scenarier på https://callemilano.dk med de rigtige nøgler |

**Lokalt:**
1. Hent øjebliksbilledet med en SQL-forespørgsel på Lovable-projektet `97bd306c-caee-40f2-9a42-afd1b87b45fd` (Lovable MCP `query_database`, kun læsning):
   `select json_build_object('recommendations',(select json_agg(json_build_object('id',id,'title',title,'category',category,'lat',lat,'lng',lng,'url',url,'google_maps_url',google_maps_url,'guide',guide)) from recommendations where guide is not null),'holidays',(select json_agg(h) from holidays h))`
2. Gem resultatet som `snapshot.json`.
3. Kør: `SNAPSHOT=snapshot.json [OPEN_METEO_DOWN=1] npx tsx --tsconfig tsconfig.json scripts/selftest-local.mts`
4. Scenarier med frit ønske springes lokalt over, fordi de kræver Claude.
5. Google Routes lokalt kræver en Google-nøgle i `GOOGLE_API_KEY`. I Claudes cloudmiljø indsatte proxyen den, med `NODE_USE_ENV_PROXY=1`.

**På den rigtige side:**
1. Hent nøglen fra tabellen `public.selftest_tokens`, som kun service role kan læse, med `select token from public.selftest_tokens where expires_at > now()` via `query_database`. Den udløber 2. februar 2027. En ny nøgle oprettes med INSERT på 48 hex-tegn.
2. Kør `SELFTEST_TOKEN=... npx tsx scripts/selftest-remote.mts`.

Sidste kørsel på callemilano.dk var 4. november efter #13: **14/14 OK**.

**Andre kontroller:** `./node_modules/.bin/tsc --noEmit`, `npx eslint <filer>` og `npm run build`. Kør aldrig `prettier --write` på hele `src/lib`, fordi det omformaterer filer, der ikke hører til leveringen.

## 5. Lovable – faldgruber, vi har lært

- **Publish kører ikke `drizzle/migrations/`.** Skemaændringer skal både ligge i `drizzle/migrations/NNNN_*.sql` med en post i journalen og anvendes manuelt med `query_database`. Det er gjort for `0004_add_holidays` og `0005_add_selftest_tokens`.
- **Forhåndsvisningen** (`id-preview--…lovable.app`) ligger bag Lovables login. Selvtesten kan kun køre på callemilano.dk efter Publish.
- **Spørg ikke Lovables agent i plan-tilstand.** Den overskrev `.lovable/plan.md` ved et rent spørgsmål (4. november) og venter nu på godkendelse af en "plan". Den må ikke godkendes. Filen er gendannet i app-PR #14.
- **Publish-knappen** har en gang ikke virket for ejeren. Lovable MCP `deploy_project` kan udgive, men kun når ejeren har bedt om det.
- **Google Maps-forbindelsen er "Managed by Lovable"** (koblet til 4. november). Server-kald til Google, fx Routes, går gennem `https://connector-gateway.lovable.dev/google_maps/<api>/<path>` med `Authorization: Bearer LOVABLE_API_KEY` og `X-Connection-Api-Key: GOOGLE_MAPS_API_KEY`. Det er samme mønster som Google Calendar i `src/lib/calendar.functions.ts`. Gatewayen har et loft på 6.000 kald pr. døgn pr. workspace.
- **Kort i browseren** bruger `VITE_LOVABLE_CONNECTOR_GOOGLE_MAPS_BROWSER_KEY` på `*.lovable.app` og familiens egen nøgle på callemilano.dk (`src/lib/maps-loader.ts`, skrevet af Lovable).

## 6. Status lige nu

**App-repoet (`callemilano-f388b2be`):** PR #14 (ruter mellem stop) og #17 (AEMET-connector) er merget. Lovable-projektet er publiceret på `1911a510ea55c902bd3248d7dd6703b5dea6e70f`. PR #18 blev lukket som overflødig, fordi dens rettelse allerede var på `main`.
- Live-selvtesten blev kørt 5. november: **14/14 scenarier OK**, inkl. `aemet-live`.
- Ruteopslagene i appen går gennem Lovables Google Maps-gateway med projektets egen nøgle som reserve.

**Places-repoet (`callemilano`):** PR #54 er merget (`b13fd38`) og tilføjer route-tjekket tid mellem stop. Ejeren har besluttet, at disse beregninger bruger det aktuelle tidspunkt; lørdagsstandard er droppet. Den opfølgende ændring og regressionstest er under forberedelse.
- `X-Goog-Api-Key: dummy` er den tilsigtede session-proxy-konvention i agentmiljøet, dokumenteret i `tools/intake.py`; den er ikke en rigtig Google-nøgle.

**places-repoet:** 220 stedposter, 0 valideringsfejl, `main` er ren.

## 7. Opgaveliste (prioriteret)

1. **Afslut #14:** Færdig. Live-selvtesten efter Publish gav 14/14 OK 5. november.
2. **Regnrisiko i procent:** AEMET OpenData er koblet til Lovable Cloud; `aemet-live` bestod. Overvågning og brugerfladens integration hører til den normale Turforslag-validering.
3. **Turkort ("Mine ture"):** næste produktskridt. Gem en tur, og åbn den igen på telefonen.
4. **Loft pr. bruger** før Turforslag åbnes for familien, fordi hvert forslag og hver tekst koster Claude-kald.
5. **Afstemning:** `tools/trip.py` i places-repoet bruger nu `from_previous` og `first_stop_driving_min` via PR #54. Opfølgning: brug aktuelt tidspunkt for ruteopslag mellem stop (ejerbeslutning 2026-11-05); den faste lørdagsafgang skal ikke længere bruges dér.
6. **Data (pristjek runde 2 og faktatjek):**
   - El Ancla, Tasca Laska, Taberna Casa Blanca og El Cachalote.
   - Brug `tools/intake.py fetch`: curl → pdftotext → Chromium. Firecrawl kun som sidste udvej.
   - Facebook og Instagram er `login_wall`, så der skal ejerens screenshots til.
7. **Ejerens åbne punkter:**
   - Sheriff: åben eller lukket? Ring på +34 952 493 722.
   - Old Swiss House: åbningstider og husnummer.
   - Screenshots af menuer for Venta La Morena, La Sierra, UTOPÍA, Venta los Condes og Kamura.
   - Somos de Banús: €€€ eller €€?
   - KFC: ja eller nej?
   - Familievurderinger.
8. **Små ting:** Restauranter uden pris vises uden pris. Restaurantbeskrivelser i appen er på engelsk (`text_language: en`), og de danske tekster mangler.

## 8. Sådan afleverer du til ejeren

- Skriv kort og på dansk: hvad der er gjort, hvad det betyder for brugeren, hvad ejeren skal gøre (merge, publish eller import), og hvad der stadig er åbent.
- Én PR pr. levering, med en testrapport i beskrivelsen. Afslut PR-beskrivelsen med en linje om, hvilket værktøj der har skrevet den.
- Efter ejerens merge og publish kører du selvtesten på callemilano.dk og melder resultatet. Ejeren skal ikke lave manuelle turforslag.
