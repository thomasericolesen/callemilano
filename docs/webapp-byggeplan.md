# Byggeplan: turforslag og tale i callemilano.dk

Udkast 2026-11-01. Ejerens beslutninger 2026-11-02 er indført nedenfor. Intet er bygget eller ændret i Lovable-projektet endnu (sidst ændret 2026-10-19).

## Udgangspunkt

callemilano.dk er Lovable-projektet **"Vores Spanske Hjem"** (React/TanStack Start, Lovable Cloud/Supabase,
login med Google, mobil-først). Siden har allerede:

- **Find en tur**: tre spørgsmål (hvem, køretid, tid) og en rangeret liste af steder;
- **Inspiration / Anbefalinger** og en admin-import fra dette repo (`importPlacesCatalog`).

Importen tager i dag kun poster med status `published` (der er ingen endnu) og kun kategorierne
City/Nature/Excursions. Strande, restauranter og familieaktiviteter, altså hele det lokale lag, kommer ikke med.

Repoet er stadig **eneste kilde** til stedfakta. Fase 1 (`/restaurant-indsamling`, `/aabningstider`) kører videre
i Claude Code. Appen får en kopi via import, ligesom i dag.

## Målbillede

```text
Find en tur → vælg 1–3 steder → dato + hvem (skriv ELLER 🎤 tal) → "Lav turforslag"
                                         │
   App-server: planTrip (= tools/trip.py plan i TypeScript)
     vejr (Open-Meteo/met.no) · trafik (DGT, hentet hvert 10. min) · helligdage
     åbningsstatus · restauranter i gåafstand · forslag i nærheden · automatiske tjek
                                         │
   Claude (Ecco) → turforslag (struktureret) + kort talt resumé
                                         │
   🔊 resumé læses op · turforslag vises · "Gem som PDF" / "Del" · gemmes under "Mine turforslag"
```

## Status trin 1 (2026-11-02)

- **Punkt 1 (eksport) er lavet:** `python3 tools/app_export.py` skriver `data/app-export/places.json` og `holidays.json`. Kør den efter ændringer i stedposter (afledte data som `data/place-catalog.csv`; ret aldrig i dem i hånden). Den 2026-11-02 gav den 144 steder (48 restauranter) og 28 helligdage. Kun det aktuelle område eksporteres (køretid højst 30 min eller medlem af et udflugtslag).
- **Punkt 2 (import) er lavet på branch** `claude/vigilant-cray-dtqaxz` i app-repoet `thomasericolesen/callemilano-f388b2be` (synkroniseret med Lovable). Admin vælger `places.json` på Admin-siden. Simulering mod databasen 2026-11-02: 25 opdateres via stedets ID, 4 via Google place ID, Bioparc springes over (redaktionel side), 114 oprettes.
- **Tekster:** nye steder kommer med postens engelske tekst (`text_language: "en"`); danske tekster, der allerede findes i appen, bevares. Dansk oversættelse er en åben opgave.
- **Helligdage:** tabellen `public.holidays` laves med drizzle-migration 0004 i app-repoet (punkt 3).
- **Punkt 3 (`planTrip`) er lavet på branch** `claude/vigilant-cray-dtqaxz` i app-repoet: `src/lib/trip-plan.ts` (regler fra `tools/trip.py plan`), server-funktionen `planTrip` (kun admins) og siden `/turforslag` (menuen for admins). Eksporten har nu en `trip`-blok pr. sted (åbningstider og tjekdato, faste åbningstider, regnvejrsdag, bar, telefon). Afprøvet 2026-11-02 med eksporten og live-data: DGT-hændelser og spisesteder er identiske med `tools/trip.py`; met.no-reserven virker. Open-Meteo havde lukket testmaskinens IP for dagen (dagskvote), så den gren blev testet via fejlhåndteringen.
- **Efter merge:** kør eksporten igen og importér `places.json` på ny, så stederne får `trip`-blokken.

## Trin 1: turforslag med tekst

1. **Eksport fra repoet:** et lille script laver `data/app-export/` (steder med status, restauranter, helligdage,
   områder og åbningstider) som JSON.
2. **Import i appen:** udvid den eksisterende admin-import, så den
   - tager alle seks kategorier;
   - tager udkast-poster med en synlig "Udkast"-markering, hvis ejeren beslutter det (se beslutning 1);
   - importerer restauranter og helligdage i nye tabeller (`restaurants`, `holidays`).
3. **`planTrip` (server):** samme regler som `tools/trip.py plan`. Trafikfilen fra DGT (2,8 MB) hentes af et
   baggrundsjob hvert 10. minut og gemmes. Vejr gemmes i 1 time. Så tager et turforslag sekunder i stedet for
   35 sekunder.
4. **Ecco (server):** ét kald til Claude API med Eccos instrukser (`.claude/agents/ecco.md`) og `plan.json`.
   Svaret er struktureret (samme felter som `trip.json`) plus et felt `spoken_summary` på højst ca. 600 tegn.
   API-nøglen ligger kun på serveren som hemmelighed.
5. **Visning:** en side "Turforslag" i appens design med klikbare telefonnumre og kortlinks. "Gem som PDF" bruger
   browserens udskrivning med et print-stylesheet. "Del" bruger telefonens delemenu. Tidligere turforslag
   gemmes pr. bruger.
6. **Værn mod udgifter:** højst f.eks. 10 turforslag pr. bruger pr. dag og et månedligt udgiftsloft i
   Anthropic Console.

## Trin 2: tale

1. **🎤-knap** på "Find en tur". Gæsten siger fx "to voksne og to børn på 4 og 9, stranden og noget med dyr i
   morgen". Teksten vises, så den kan rettes.
2. **Tale til tekst:** version 0 bruger telefonens indbyggede genkendelse (gratis, men ustabil på iPhone).
   Version 1 optager lyden og sender den til Google Speech-to-Text (Chirp, dansk). Lyden gemmes ikke.
3. **Forstå ønsket:** Claude omsætter teksten til steder, dato og gruppe (struktureret svar). Mangler der
   noget, stiller appen ét kort spørgsmål på skærmen og med stemme.
4. **Oplæst resumé:** `spoken_summary` læses op. Version 0 bruger telefonens danske stemme (gratis). Version 1
   bruger Google Chirp 3 HD (naturlig dansk stemme) med en udtaleliste for spanske navne (Benalmádena,
   Alcazaba, Fuengirola).
5. **Samtykke:** én linje første gang ("Når du trykker på mikrofonen, sendes din tale til Google for at blive
   til tekst. Den gemmes ikke.").

## Trin 3: app på hjemmeskærmen og finpudsning

- Manifest og ikon, så callemilano.dk kan lægges på hjemmeskærmen og åbnes som en app (PWA).
- Det seneste turforslag kan læses uden net (praktisk i bjergene).
- Rettelser efter de første rigtige ture.

## Prisoverslag

Priser oktober–november 2026, omregnet med ca. 7 kr. pr. USD. **Tale-priserne er fra tredjepartsoversigter og
skal bekræftes på leverandørernes egne sider, før vi vælger.**

### Pr. turforslag (løbende)

| Del | Grundlag | Ca. pris |
|---|---|---|
| Claude Opus 5.5 (Ecco) | ~15.000 input-tokens à $4/mio. + ~5.000 output-tokens à $20/mio. | ~$0,16 ≈ **1,10 kr.** |
| *alternativ:* Claude Sonnet 5.5 | samme mængde à $2 / $10 pr. mio. | ~$0,08 ≈ 0,55 kr. |
| Forstå talt ønske (Claude) | ~2.000 input + ~500 output | ~$0,02 ≈ 0,15 kr. |
| Tale til tekst, Google Chirp | ~30 sek. à $0,016/min. | ≈ 0,06 kr. |
| Oplæst resumé, Google Chirp 3 HD | ~600 tegn à ~$30/mio. tegn | ≈ 0,13 kr. |
| Vejr og trafik | Open-Meteo, met.no, DGT | 0 kr. |
| **I alt, fuld version** | | **≈ 1,50 kr. pr. turforslag** |
| I alt, med telefonens gratis tale | | ≈ 1,25 kr. |

**Pr. måned:** 30 turforslag giver ca. 45 kr., og 100 turforslag ca. 150 kr. Google har efter de fundne
oversigter et gratis månedskvantum for både tale til tekst og Chirp 3 HD, som en families forbrug sandsynligvis
ligger under. Det er ikke bekræftet.

### Faste udgifter og opbygning

| Del | Ca. pris |
|---|---|
| Lovable Pro (betales allerede) | $25/md. ≈ 175 kr./md., 100 credits/md. + 5 dagligt |
| Lovable-credits til trin 1–3, hvis Lovable-agenten bygger | skønnet 40–80 credits; kan delvist dækkes af månedens credits, ellers top-up ca. $15 pr. 50 credits |
| Lovable Cloud (database, server) | inden for den inkluderede kvote ved familieforbrug (ikke bekræftet) |
| Claude API-konto | betaling efter forbrug; sæt et udgiftsloft, fx $20/md. |
| Google Cloud (kun tale version 1) | betaling efter forbrug; kræver Google Cloud-konto med betalingskort |

Skønnet for Lovable-credits er usikkert: et credit-forbrug pr. besked afhænger af ændringens størrelse.
**Billigere alternativ:** forbind Lovable-projektet med GitHub. Så kan Claude Code bygge koden her, og Lovable
synkroniserer den uden at bruge credits til selve programmeringen.

## Ejerbeslutninger 2026-11-02

1. **Udkast-steder:** appen og turagenten viser poster med status `needs_fact_check` og senere (samme grænse som `tools/trip.py`). Poster, der ikke er godkendt, får mærkatet "Ikke endeligt godkendt". Rene udkast (`draft`) vises ikke.
2. **Byggevej:** Lovable-projektet forbindes med GitHub; Claude Code bygger koden, og Lovable synkroniserer.
3. **Model til Ecco:** Claude Sonnet 5.5 (kan skiftes senere).
4. **Stemme:** telefonens gratis stemme og genkendelse først (version 0); Google Chirp senere (forslag; ikke afgjort).
5. **Adgang:** kun admins i starten, indtil 2–3 rigtige ture er testet.
6. **Udgiftsloft:** forslag $20/md. på Claude API og 10 turforslag pr. bruger pr. dag (ikke afgjort).

## Beslutninger til ejeren (oprindeligt udkast)

1. **Udkast-steder i appen:** skal poster, der ikke er godkendt, vises med "Udkast"-mærkat, eller kun godkendte?
   I dag vises intet fra repoet, fordi intet er publiceret.
2. **Byggevej:** Lovable-agenten (credits) eller GitHub-forbindelse og Claude Code (anbefales)?
3. **Model til Ecco:** Claude Opus 5.5 (bedst, ca. 1,10 kr.) eller Claude Sonnet 5.5 (ca. 0,55 kr.)?
4. **Stemme:** start med telefonens gratis stemme, eller gå direkte til Google Chirp 3 HD?
5. **Hvem må lave turforslag:** alle godkendte familiemedlemmer (som i dag) eller kun admins i starten?
6. **Udgiftsloft:** fx $20/md. på Claude API og 10 turforslag pr. bruger pr. dag?

## Rækkefølge

1. Ejeren svarer på beslutningerne ovenfor.
2. `/restaurant-indsamling` for Fuengirola-området (nødvendigt uanset app).
3. Trin 1, test med 2–3 rigtige ture.
4. Trin 2 (tale version 0, derefter version 1).
5. Trin 3.

## Kilder til priser

- Claude API-priser: Anthropics prisoversigt (cachet 2026-10-06): Opus 5.5 $4/$20, Sonnet 5.5 $2/$10 pr. mio. tokens.
- Lovable: [lovable.dev/pricing](https://lovable.dev/pricing?swcfpc=1); [eesel.ai](https://eesel.ai/blog/lovable-pricing) om top-ups (tredjepart).
- Google Text-to-Speech: [cloud.google.com/text-to-speech/pricing](https://cloud.google.com/text-to-speech/pricing/?authuser=2); [diyai.io](https://diyai.io/ai-tools/audio-generation/google-cloud-text-to-speech-pricing/) (tredjepart).
- Google Speech-to-Text: [cloud.google.com/speech-to-text/pricing](https://cloud.google.com/speech-to-text/pricing?authuser=1); [convertaudiototext.com](https://convertaudiototext.com/blog/google-cloud-speech-to-text-pricing-2026) (tredjepart).
- ElevenLabs (fravalgt alternativ, ca. $0,05 pr. 1.000 tegn med minimum 1.000): [llmreference.com](https://www.llmreference.com/model/eleven-flash-v2-5/elevenlabs) (tredjepart).
