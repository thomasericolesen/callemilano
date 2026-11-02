---
name: aabningstider
description: Fase 1 (forarbejde). Opdatér åbningstider, sæsoner og lukkedage i CalleMilanos stedposter med agenten Alpha, så turforslag kan bruge dem uden websøgning. Brug ved /aabningstider, efter et turforslag har haft noter til redaktøren, eller ca. hver 2. måned.
---

# /aabningstider (fase 1)

1. Kør `date` og `python3 tools/trip.py hours-status`. `needs_work` viser steder med manglende, udløbne eller
   over 60 dage gamle åbningstider. Har seneste turforslag noter i `trips/*/hours-check.json` (`for_editor`), så
   tag dem med.
2. Vis værten listen kort, og spørg (AskUserQuestion), hvilke der skal tages. Der tages højst 5 pr. kørsel.
3. Start én **alpha** (tilstand A: forarbejde) pr. sted **parallelt**. Hver agent redigerer kun sin egen stedpost.
4. Bagefter: kør `python3 tools/places.py validate` og `python3 tools/places.py catalog`, og så
   `python3 tools/trip.py hours-status` igen.
5. Vis værten: steder opdateret, kilder og uenigheder (review issues). Commit kun, hvis værten beder om det, og
   notér i så fald kørslen i `docs/change-log.md`.

Helligdage: `data/holidays.csv` dækker Andalusiens helligdage for 2026 og 2027 (BOJA). Kommunernes lokale
helligdage mangler endnu og kan tilføjes af Alpha med kilde. Når næste års dekret udkommer (normalt i maj),
tilføjes året.
