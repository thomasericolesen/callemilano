# CalleMilano: projektets tilstand

**Sidst opdateret:** 2026-11-13
**Formål:** Overblik over, hvad der findes, og hvad der er åbent. Reglerne står i `AGENTS.md`, dataaftalen i `docs/place-schema.md`. Det daglige overblik er den nyeste `docs/status-*.md`; kort over al dokumentation i `docs/README.md`. Beslutninger står i `docs/change-log.md`, nyeste først.

## Formål og omfang

CalleMilano er en familierejseguide til gæster på Casa de la Familia (Las Lagunas de Mijas). Primær målgruppe er børnefamilier, der ikke vil køre langt; sekundært voksne, seniorer og teenagere. Lagene er (se `data/layers.csv`):

- **Lokalt lag:** højst 30 minutters kørsel én vej, efter Google Maps' hovedtal (ejerbeslutning 29. oktober).
- **`excursions_4h`:** dagsture og overnatninger op til ca. 4 timer. Kataloggrupper: `Tæt på` (højst 60 min), `Dagsture` og `Længere væk`.
- **`excursions_5h`:** ruter på 4-5 timer med overnatning. Ingen portugisiske steder endnu.
- Steder uden for lagene ligger som arkiv og udvikles ikke, medmindre redaktøren siger det.

## Hvad der findes

- **Stedposter:** 220 i `docs/places/` (skema 1.0.0). Status: 104 `approved`, 52 `needs_editorial_review`, 15 `needs_fact_check` (14 arkiv uden for appen, plus `canon-de-las-angosturas` i appen), 2 `draft`, 47 `archived`. Efter godkendelsesreglen fra 10. november tæller `needs_editorial_review` som godkendt til appen og turforslag; `approved` bruges ikke længere som trin, men eksisterende poster er uændrede.
- **Kategorier:** 92 Restaurants, 39 Family activities, 33 City, 21 Beaches, 19 Nature, 16 Excursions.
- **Validering:** `python3 tools/places.py validate` giver 0 fejl og 26 advarsler (mest manglende koordinater på arkivposter). Alle tests består (`python3 -m unittest discover -s tests`).
- **Lagmedlemskab:** 69 steder i `data/layer-membership.csv`, alle i `excursions_4h` (46 `Tæt på`, 16 `Dagsture`, 7 `Længere væk`).
- **Appen (callemilano.dk):** 156 steder, alle med dansk tekst fra `data/app-texts-da.json`. Eksporteres med `tools/app_export.py` til `data/app-export/`, senest 14. november og importeret samme dag. Arkiverede steder fjernes ikke af importen; deres app-række skjules med guide-status `archived`. Appens kode ligger i `~/code/callemilano-app`.
- **Restauranter:** fulde stedposter. `data/restaurant-directory.csv` (26 rækker) er kun en emneliste: 22 `konverteret`, 4 `fravalgt`.
- **Værktøjer** (`tools/`): `places.py` (validering og katalog), `intake.py` (indsamling), `app_export.py`, `route_check.py` (ikke kørt), `trip.py` med moduler (`trip_core`, `trip_weather`, `trip_traffic`, `trip_restaurants`, `trip_plan`, `trip_render`) og fælles `common.py`.
- **Agenter og færdigheder:** `.claude/agents/` har Alpha (åbningstider), Charlie (restauranter), Ecco (turforslag), `candidate-screener`, `source-reader` og `record-writer`. `.claude/skills/` har `aabningstider`, `restaurant-indsamling` og `turforslag`.
- **Registre:** `data/place-id-registry.csv` (215 ID'er), `data/image-rights.csv` (7 billeder, alle til appens "Oplev"-sider), `data/import-queue.csv`, `data/place-catalog.csv` (genereret, aldrig redigeret i hånden).
- **Dokumentation:** `docs/` er sorteret i `history/`, `decisions/`, `product/`, `engine/` og `content/`. `docs/published/` har tre håndskrevne guldstandardsider (BIOPARC, La Cala, Sheriff) uden for livscyklussen.
- **Anbefalingsprototypen** (`docs/engine/`, analytiske CSV'er i `data/`) er stadig fra den første fase og læser ikke stedposterne. Den er ikke koblet til appen.

## Arbejdsgang

Redaktørarbejdsgangen (ejerbeslutning 11. november) er i `AGENTS.md` og `docs/multi-agent-workflow.md`: Claude klarer niveau A/B alene og må pushe, åbne PR, merge og importere for sådanne ændringer. Niveau C/D (konflikter, tags, familiescores, arkivering, kategorier, regler) går på redaktørlisten og venter på svar. Appimport sker uden browser med tokenet i `~/.callemilano-import-token` (udløber 9. februar 2027).

## Åbent

1. **2 kladder** venter på et nyt forsøg i Chrome: `castillo-de-monda` (ingen tider eller priser for gæster udefra) og `paseo-maritimo-marbella` (den rette side hos Turismo Marbella er ikke fundet).
2. **Åbne warnings (84) og info (52) på app-steder.** Fakta-delen af facilitetsissues er udført 14. november (andet kildeforsøg; resten lukket som `not_found_after_two_attempts`). Resten er redaktionelle (målgruppe, familievurderinger, tags, lagets omfang) og går på en tjekliste til redaktøren. Konflikter og `blocking` lukkes aldrig i bulk.
3. **Friskhedsjobbet** (månedligt) er ikke sat op. `next_review_at` er sat 14. november (undtagen `canon-de-las-angosturas`); første reelle tjek er 14. februar 2027. Jobbet skal også minde om tokenets udløb. Hold det billigt: script først, AI kun ved ændrede sider.
4. **`route_check.py`** er ikke kørt; det kræver en `GOOGLE_MAPS_API_KEY` på Mac'en.
5. **Menu og pris** mangler for Venta La Morena, Mesón Salvador og Vegetalia.
6. **Udskudt:** om appen skal vise `approved` anderledes end `needs_editorial_review`.
7. **Senere (ejerens ønske 13. november):** når appen bliver en "rigtig" app og ikke kun en side i browseren, skal den logge ud af sig selv efter nogle minutter uden brug. Det er en ændring i login og venter på ejerens merge. Indtil da forbliver "Log ud" som nu (logger ud på alle enheder).
8. **Appens import beholder gamle danske tekster**, når repoet kun sender engelsk (`mergeGuide` i app-repoet). Lige nu har alle app-steder dansk tekst i repoet, så det har ingen virkning. Et nyt sted skal derfor have dansk tekst i `data/app-texts-da.json`, før det importeres.

## Næste skridt

Følg "Først i næste session" og "Åbent" i den nyeste `docs/status-*.md`. Start med at læse `AGENTS.md`, kør `python3 tools/places.py validate`, og behandl aldrig værdier i de analytiske CSV'er som verificerede fakta.
