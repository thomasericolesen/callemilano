# CalleMilano – statusrapport 3. november 2026

**Til:** uafhængig gennemgang (fx OpenAI/ChatGPT) af ejeren, Eric Olesen.
**Skrevet af:** Claude (Claude Code) kl. 21.30 dansk tid, efter dagens arbejde.
**Grundlag:** `CalleMilano_produktkoncept_og_udviklingsplan_v1.1.md`, instruksen *"statusanalyse og test af
Tourguide"*, `AGENTS.md` og koden i de to repoer `thomasericolesen/callemilano` (steder og data) og
`thomasericolesen/callemilano-f388b2be` (appen på callemilano.dk, Lovable).

Rapporten skelner mellem det, der er **observeret** (kode, data og ejerens test på siden), og det, der
**anbefales**. Tal er hentet fra repoerne og appens database samme aften.

---

## 1. Kort fortalt

Turforslag på callemilano.dk er nu en samlet turguide for admins. Brugeren beskriver et ønske i almindeligt
sprog eller søger generisk ("strand lokalt", "restaurant billig"). Claude og OpenAI foreslår steder i
fællesskab (konsensus). Siden samler vejr, trafik, helligdage, åbningstider og spisesteder, og Ecco (Claude)
skriver turforslaget på dansk. Ejeren har testet hele kæden på siden. Det virker, med kendte mangler, som er
listet i afsnit 6.

## 2. Hvad der blev lavet i dag (observeret)

| Område | Resultat | PR |
|---|---|---|
| Ecco i appen | Første rigtige kald mod Claude API virkede. Teksten bygger kun på data. | f388b2be#3, #4 (en afhængighed, der manglede efter en merge) |
| Søgning efter type | Dansk søgeordsliste: lokalt, restaurant/frokost, billig/mellem/dyr, strand, by, natur, børn, regnvejr … Kategoriknapper med antal. Restauranter kan vælges som stop. | f388b2be#5 |
| Nye prisniveauer (ejerbeslutning) | Midterste hovedret + én drik: € under 20 €, €€ 20–50 €, €€€ over 50 €. Erstatter 15/35 €. Alle poster genberegnet. | callemilano#43, f388b2be#6 |
| Lokale billige spisesteder | El Trópico er nu en restaurant og ikke en bar (ejerbeslutning). Cerros del Águila har € med ejeren som kilde. | callemilano#44 |
| Gratis sidelæsning før Firecrawl | curl → PDF-tekst → Chromium (Playwright) → Firecrawl kun til sidst. Facebook/Instagram markeres `login_wall`. | callemilano#45 |
| Pristjek og faktatjek | 21 restauranter inden for 30 min er læst. 6 fik pris fra egen menu, og 5 blev faktatjekket og kom med i appen. | callemilano#46 |
| AI-turplan lagt sammen med Turforslag (ejerbeslutning) | Frit ønske → Claude og OpenAI foreslår 1–3 steder ved konsensus. Den gamle `/ai-tur` sender videre. | f388b2be#7 |
| Afstand mellem stop + ny søgning | Afstanden fra forrige stop i stedet for summerede køretider fra huset. Knapperne "Foreslå noget andet", "Start forfra" og "Ny søgning". | f388b2be#8 (**ikke merget ved rapportens skrivning**) |

**Data i aften:** 220 stedposter med 0 valideringsfejl. 69 restauranter (uden barer): 7 med €, 31 med €€, 1
med €€€ og 30 med ukendt pris. App-eksporten har 149 steder, og 5 restauranter med € ligger inden for 30
minutter fra huset: Cerros del Águila, Café NOMAD, Ragazzi, El Trópico og Marvelous Burger.

## 3. Sådan virker Turforslag nu (observeret i koden)

1. **Ønske (valgfrit):** Brugeren skriver fx "Strand i La Cala og frokost". Serverfunktionen `suggestTrip`
   (kun admins) sender samme instrukser og samme katalog til **Claude** (Anthropic SDK) og **OpenAI**
   (Lovable AI Gateway) parallelt.
   - **Modellerne må kun vælge id'er fra kataloget.** Serveren sorterer alt andet fra, fjerner dubletter og
     tager højst 3.
   - **Fletning:** Steder, som begge valgte, kommer først ("Claude og OpenAI enige"). Derefter fyldes der op
     med steder, som kun én valgte ("kun Claude" / "kun OpenAI"), til det antal stop, den mest omfattende
     model foreslog (højst 3).
   - **Fejl:** Fejler den ene model, bruges den andens forslag med noten "Ingen konsensus".
   - **"Foreslå noget andet"** (PR #8) udelukker de steder, der allerede er foreslået.
2. **Steder:** Forslagene sættes ind som valgte steder og kan rettes. Man kan også søge selv, generisk eller
   på navn.
3. **Dato og gruppe:** voksne, børns alder, seniorer, og om nogen går dårligt eller bruger barnevogn.
4. **Data (`planTrip`):**
   - vejr fra Open-Meteo med met.no som reserve, og trafikhændelser fra DGT;
   - helligdage, og åbningstider fra stedposten med en markering af, om de er aktuelle, forældede eller
     ukendte;
   - spisesteder inden for ca. 800 m, op til 3 km hvis der er for få, i tre prisniveauer;
   - forslag i nærheden og automatiske tjek (blokeret, tjek, forbehold, info).
5. **Tekst (Ecco, Claude Sonnet):**
   - tidsplan, vejr, køretur, spisesteder, "Hvis I har tid" og "Godt at vide";
   - noter til værten og et kort resumé til oplæsning.
   - Ecco må ikke tilføje fakta, der ikke står i data.

**Ejerens test i aften, "Strand og frokost i La Cala", 2 voksne og børn på 5 og 8:**
- Claude og OpenAI var enige om La Butibamba og Chiringuito Los Moreno.
- Ejeren skiftede frokoststedet til El Trópico (€, 470 m fra stranden).
- Ecco lagde stranden om formiddagen, fordi der var regn kl. 15, foreslog indendørs plan B (bowling, biograf
  og JumpJoy) og nævnte Los Moreno som alternativ.
- **Fejl i testen:** Ecco beskrev frokoststedet som "ca. 13 minutters kørsel fra huset", og siden viste en
  summeret køretid på 28 min. Begge dele er rettet i PR #8.

## 4. Status pr. besluttet produktbeslutning

Statusserne er de samme som i instruksen.

| # | Beslutning (instruks) | Status | Evidens |
|---|---|---|---|
| 1 | Visuel smagemenu med typer af oplevelser | **Delvist implementeret** | Kategoriknapper og dansk søgning (`src/lib/place-search.ts`). Der er ingen visuelle fliser, og vandland, forlystelser og dyr er ikke egne indgange. |
| 2 | Vælge kategori uden at kende navnet | **Fungerer og er afprøvet** | Ejerens test: "frokost lokalt billig" gav 5 steder. |
| 3 | Fri beskrivelse af ønsket | **Fungerer og er afprøvet** | "Beskriv jeres ønske" → konsensus (f388b2be#7), testet live. |
| 4 | Kombinere flere oplevelser | **Implementeret, men ikke tilstrækkeligt afprøvet** | 1–3 stop, også restauranter. Modellerne kombinerer ud fra koordinater. "Forslag i nærheden" bruger luftlinje. |
| 5 | Realisme: køretid mellem stop, tidsbudget, åbningstider, sæson | **Delvist implementeret** | Vejr, helligdage og åbningstider tjekkes. Afstand mellem stop (PR #8) er i luftlinje, ikke route-tjekket. Tidsbudget findes kun som ønske i fri tekst. |
| 6 | Gemme turen som turkort | **Mangler** | Der er ingen tabel til ture og ingen "Mine ture". |
| 7 | Mobil og enkel | **Kan ikke afgøres ud fra kode/dokumentation** | Ikke testet på en telefon. Siden er lang og er indtil videre kun for admins. |

## 5. Ejerbeslutninger i dag

1. **Prisniveauer:** € under 20 €, €€ 20–50 €, €€€ over 50 € (midterste hovedret + én drik). Grænsetilfælde:
   Café NOMAD €, Juan Playa €€, Sheriff Unknown (muligvis lukket). Somos de Banús beholder €€€ indtil videre.
2. **El Trópico** er en restaurant og ikke en bar. **Cerros del Águila** har € med ejeren som kilde.
3. **Firecrawl:** brug gratis metoder først. Værktøjer, der omgår bot-beskyttelse, bruges ikke (Tripadvisors
   vilkår, og kildepolitikken prioriterer egne menuer).
4. **AI-turplan** lægges sammen med Turforslag. Kun admins i starten. Konsensus mellem Claude og OpenAI, ikke
   enten eller.

## 6. Kendte mangler og risici

- **Køretid mellem stop er ikke route-tjekket.** Den er kun i luftlinje, og AGENTS.md kræver route-tjekkede
  køretider for steder.
- **Vejret faldt tilbage til met.no** i begge tests i dag, fordi Open-Meteo ikke svarede. Derfor mangler
  regnrisiko i procent og UV. Årsagen er ikke undersøgt endnu.
- **Turkort mangler:** ingen gem, genåbn, PDF på telefonen, offline eller oplæsning. Ecco laver allerede et
  resumé til oplæsning, men intet læser det op.
- **Datahuller:** 30 restauranter mangler pris. Steder uden hjemmeside og Facebook-sider kræver ejerens
  screenshots. 44 stedposter er stadig kladder og vises ikke i appen.
- **Omkostninger:** Hvert "Foreslå steder" koster både Claude- og Lovable AI-kreditter, og hver Ecco-tekst
  koster Claude-kreditter. Der er endnu intet loft pr. bruger.
- **Danske tekster:** Stedernes beskrivelser i appen er på engelsk (`text_language: en`). Ecco skriver på
  dansk.
- **Modellernes rolle:** Konsensus gælder kun valget af steder. Teksten skrives af én model (Claude). Fakta
  kommer fra data, men vurderinger som "passer til børn" er modelens formulering.

## 7. Spørgsmål til den uafhængige gennemgang

1. Er fletteregel for konsensus fornuftig (fælles steder først, derefter skiftevis op til højst 3)? Bør et
   sted, kun én model valgte, kræve en bekræftelse fra brugeren?
2. Er reglen "midterste hovedret + én drik" med grænserne 20/50 € rimelig for familier på Costa del Sol?
3. Hvilke af manglerne i afsnit 6 bør komme før turkortet, set fra en førstegangsbruger på en telefon?
4. Er der risiko for, at Ecco eller modellerne alligevel præsenterer usikre data (åbningstider, børnevenlighed)
   som sikre? Hvordan kan siden gøre usikkerheden tydeligere?
5. Er det rigtigt at holde Turforslag for admins, indtil turkort og et loft pr. bruger findes?

## 8. Anbefalet næste skridt (Claude)

1. Merge og publicér f388b2be#8, og gentag testen fra La Cala.
2. Find årsagen til, at Open-Meteo ikke svarer (kvote eller blokering fra Lovables server).
3. Tilføj route-tjekket køretid mellem stop (Google Routes) til de valgte stop.
4. Turkort, mindste version: gem en tur, og åbn den igen fra "Mine ture" på telefonen.
