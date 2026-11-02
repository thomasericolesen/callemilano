---
name: restaurant-indsamling
description: Fase 1 (forarbejde). Byg eller opdatér CalleMilanos restaurantkatalog (data/restaurant-directory.csv) pr. område med agenten Charlie. Brug ved /restaurant-indsamling, når kataloget har huller, eller ved kvartalsvis opdatering.
---

# /restaurant-indsamling (fase 1)

1. Kør `date` og `python3 tools/trip.py coverage`. Det viser områderne fra `data/restaurant-areas.csv` og hullerne
   pr. sted (mål: 3 dyre, 3 mellem og 4 billige inden for ca. 10 minutters gang).
2. Spørg værten (AskUserQuestion), hvilke områder der skal tages nu. Foreslå efter `priority` og huller.
   Der tages højst 3 områder pr. kørsel.
3. Start én **charlie** pr. område **parallelt**. Hver får sit `area_id` og en id-blok (område 1: R-0100–R-0199,
   område 2: R-0200–R-0299 osv., over de højeste eksisterende id'er) og skriver til `trips/_indsamling/<area_id>.csv`.
4. Når alle er færdige: flet filerne ind i `data/restaurant-directory.csv`, fjern dubletter (samme navn
   < 100 m; behold det ældste id), og kør `python3 tools/trip.py check-restaurants`, indtil den siger `"ok": true`.
5. Kør `coverage` igen, og vis værten en kort tabel: område, sted, dyr/mellem/billig og huller.
6. Commit kun, hvis værten beder om det. Notér i så fald kørslen kort i `docs/change-log.md`.

Opdatering hver 3. måned: tag rækker med `checked_at` ældre end ca. 3 måneder og rækker med status
`skal tjekkes` først. Lukkede restauranter sættes til `lukket` og slettes ikke.
