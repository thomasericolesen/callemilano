# Byggeplan: Oplev, feedback og familiens adgang

**Dato:** 8. november 2026 · **Grundlag:** mockup https://claude.ai/artifact/3hvQeqQLi1ek2kp92Acs5j (version 2), `docs/product/vurdering-familieadgang-turforslag.md`, Erics beslutninger 8. november, app-repoets `main` (`9c32633`) og databasen (læst 8. nov.).

> **Afløst 2026-11-10:** Mærkerne "Ikke endeligt godkendt" og "Familiens forslag" er afløst af ejerbeslutningen 2026-11-10 (faktatjekket tæller som godkendt; kun "Ikke faktatjekket" er et advarselsmærke; "Familiens forslag" hedder nu "Andre mulige steder"). Se `AGENTS.md` og `docs/change-log.md`.

## Erics beslutninger, som planen bygger på

1. Én side, **Oplev**, erstatter Inspiration, Find en tur, Turforslag og Anbefalinger.
2. Kategoriknapper med billeder: Strand, Restauranter, Seværdigheder, Natur, Eventyr, Byer og udflugter.
3. Kategoribilleder er frie billeder (CC0/public domain). Restauranter viser Google-fotos, som hentes direkte fra Google med fotografens navn og ikke kopieres.
4. Anbefalinger nedlægges som side. "Vi anbefaler det" bliver en type feedback; Eric giver mærket "Familien anbefaler".
5. Feedback ændrer aldrig noget automatisk. Den lander på Erics liste med navn og dato, og Eric tager en snak med brugeren. Der er ingen tidsgrænse. Én melding om "lukket" eller "farligt" giver straks mærket "tjek før besøg".
6. Familien får først adgang, når siden er på plads.

## Det, der findes i dag (databasen 8. nov.)

| Indhold | Antal |
|---|---|
| Steder fra places-repoet (`external_place_id` = `ES-…`) | 151 (3 som "anbefaling", 148 som "inspiration") |
| Håndskrevne sider (`published-…`) | 2 |
| Andre med guide-data | 15 |
| Familiens egne steder uden guide-data | 110 (3 anbefalinger, 107 inspiration) |
| Gemte ture / dagbogs-tags | 0 / 0 |
| Brugere | 3 admins, 7 familie |

## Leverancen: én app-PR plus én PR i places-repoet

Eric vil have færre, større leveringer, så det hele samles i **én app-PR**. Ved siden af kommer en lille PR i places-repoet med billedrettigheder og eksport. Der er fem dele.

### Del 1 · Oplev-siden (`/oplev`)

- **Ny rute** `src/routes/_authenticated/oplev.tsx`, som erstatter `inspiration`, `find-tur`, `turforslag` og `anbefalinger`. De gamle adresser sender videre til `/oplev`, så gamle links virker. `mine-ture` bliver.
- **Forside:** de 6 kategoriknapper (billeder fra `public/oplev/` med kilde i `data/image-rights.csv`), knappen "Overrask os" (det frie ønske, `suggestTrip`), filtrene "Hvem skal med?" og "Hvor langt vil I køre?" (genbrug `PERSONAS`, `DRIVE_LIMITS` og `rankPlaces` fra `src/lib/guide.ts`) og "Foreslå et nyt sted".
- **Kategoriliste:** stedkort med køretid, prisniveau, mærket "Familien anbefaler", "Ikke endeligt godkendt" (findes allerede), "Læg i turen" og "Anbefal / feedback". Restauranter får et Google-foto via den eksisterende `GooglePhoto`-komponent, og fotografens navn vises under billedet.
- **Kategorier → data:** Strand = `strand`, Restauranter = `restaurant` (barer vises med et mærke "Bar"), Seværdigheder = `sevaerdighed` uden tagget Adventure, Natur = `natur`, Eventyr = temaet `eventyr` (tagget Adventure) på tværs af kategorier, Byer og udflugter = `by` + `udflugt`. Fordelingen ligger i én tabel i `guide.ts`, så den er let at ændre.
- **Turbjælken** nederst holder 1–3 steder (gemt i `sessionStorage`, så de ikke forsvinder ved skift mellem kategorier). "Lav turforslag" åbner formularen med dato og hvem der skal med, og derefter køres den eksisterende `writeTrip` (Ecco). Turvisningen genbruger `trip-plan-view.tsx`.
- **Værtsværktøjer** ("Kun data", "Rådata", "Noter til værten", modelnavn) vises kun for admins.

### Del 2 · Feedback

- **Ny tabel `place_feedback`** (migrering `drizzle/migrations/0008_place_feedback.sql`):
  - `id`, `user_id`, `recommendation_id` (eller `null` for et nyt sted), `saved_trip_id` (valgfri), `type` (`anbefal` | `fakta` | `oplevelse` | `nyt_sted` | `tur`), `text`, `place_name` (til nye steder), `created_at`.
  - Ekstra felter, som kun admin bruger: `status` (`ny` | `talt_med` | `afsluttet`), `admin_note`, `talked_together` (har brugerne talt sammen?).
  - RLS: alle familiemedlemmer og admins må oprette egne rækker. Kun admins må læse og opdatere.
- **Server:** `createFeedback` (familie og admin, højst 20 pr. person pr. dag), `listFeedback` og `updateFeedback` (kun admin).
- **"Tjek før besøg":** Feedback af typen `fakta` med ordet lukket eller farligt (valgt med et afkrydsningsfelt, ikke med tekstsøgning) sætter feltet `recommendations.check_before_visit = true`. Mærket vises på stedet, indtil Eric fjerner det. Dette er den eneste automatiske virkning.
- **Erics liste** under Administration, fanen "Feedback": grupperet pr. sted med navn, dato, type og tekst. Knapper: "Talt med", "Giv mærket Familien anbefaler", "Fjern Tjek før besøg" og "Afslut". Det, Eric beslutter, føres tilbage i places-repoet som kilde, ligesom screenshots i dag.
- **Mærket "Familien anbefaler"** gemmes som `recommendations.family_recommended` (sat af admin), ikke som en `kind`.

### Del 3 · Anbefalinger flyttes

- De 3 anbefalinger, der allerede er steder fra kataloget, får `family_recommended = true`.
- De 3 anbefalinger, der ikke er i kataloget, bliver feedback af typen `nyt_sted` med den oprindelige tekst og bruger. Rækkerne beholdes, til Eric har set dem.
- Familiens 107 egne inspirationsrækker uden guide-data bliver vist under deres kategori med mærket "Familiens forslag" og kan ikke bruges til et turforslag. Alternativt kan de også gøres til `nyt_sted`-feedback, så Eric kan tjekke dem. Det er Erics valg (se nedenfor).
- Typen `kind` bliver i databasen indtil videre, så intet går tabt. Den bruges bare ikke længere i brugerfladen.

### Del 4 · Familiens adgang

- **Én migrering** (`0009_family_trip_access.sql`): kvotefunktionerne og `saved_trips`-reglerne tillader `family` og `admin`.
- **Serverfunktioner og sider:** én fælles kontrol `requireFamilyOrAdmin` i stedet for `requireAdmin` / `requireTripAdmin`.
- **Fælles dagligt loft:** `consume_trip_ai_quota()` tjekker også familiens samlede forbrug pr. dag (forslag: 20). Admin-oversigt over forbruget med en knap til at nulstille dagens tal.
- **Slået fra ved levering:** Adgangen styres af én indstilling i `house_config` (`family_trip_access = false`). Eric slår den til, når han vil åbne. Så kan PR'en merges og publiceres, uden at familien får adgang samme dag.

### Del 5 · Places-repoet

- Kategoribillederne registreres i `data/image-rights.csv` (kilder fra `docs/product/oplev-category-images-2026-11-08.json`), og filerne lægges i appens `public/oplev/`.
- `tools/app_export.py` uændret. Tagget `Adventure` ligger allerede i `guide.themes` som `eventyr`.

## Kontrol før PR'en gives til Eric

1. `npx tsc --noEmit`, produktionsbuild og lint på de ændrede filer. Fejl i den samlede lint, som fandtes i forvejen, oplyses særskilt.
2. Migreringerne testes mod en kopi af skemaet: kan køres to gange, RLS afviser en familiebruger ved læsning af feedback, og det fælles loft holder.
3. **Selvtesten udvides** med 4 scenarier: en familiebruger, der laver et turforslag (når adgangen er slået til), en familiebruger, der rammer det fælles loft, en familiebruger, der ikke kan se værtsværktøjerne eller læse andres feedback, og en feedback om "lukket", der giver mærket "tjek før besøg".
4. Et uafhængigt review af hele diffen, lavet af en delagent, før PR'en går til Eric.
5. Skærmbilleder af Oplev på telefonbredde (390 px) vedlægges PR'en.

## Efter merge og publicering

1. Claude anvender migreringerne 0008 og 0009 med Lovable `query_database` (Lovable kører dem ikke selv) og flytter de 6 anbefalinger (del 3).
2. Den fulde selvtest køres på callemilano.dk.
3. Eric prøver siden på telefonen som admin.
4. Eric slår `family_trip_access` til, når han er klar. Selvtesten køres igen med familiescenarierne.

## Erics beslutninger 8. november (aften)

1. **Fælles dagligt loft:** 20 AI-handlinger pr. dag for hele familien. Intet månedsloft i kroner for nu.
2. **Gemte ture:** private som udgangspunkt; ejeren kan dele en tur med familien (knap "Del med familien"). Delte ture kan ses, ikke redigeres, af familie og admins. Serveren gemmer planen selv, når en tur deles, så delt indhold ikke kommer fra browseren.
3. **Familiens egne inspirationssteder uden turdata (107):** vises under deres kategori med mærket "Familiens forslag"; de kan ikke bruges i et turforslag.
4. **Barer:** under Restauranter med mærket "Bar".

## Omfang og risiko

- Den største del er Oplev-siden, men den genbruger det meste: `PlacesPage`, `GooglePhoto`, `rankPlaces`, `writeTrip`, `suggestTrip` og `trip-plan-view`. Det nye er sidelayoutet, turbjælken, feedback og admin-listen.
- **Risiko:** gamle links og bogmærker til Inspiration og Anbefalinger. Det løses af omdirigeringerne.
- **Risiko:** at familien ser værtsværktøjer. Det dækkes af selvtest-scenarie 3.
- **Risiko:** AI-udgift. Den dækkes af det fælles loft, og adgangen er slået fra ved levering.
