# Vurdering: familiens adgang til Turforslag

**Dato:** 8. november 2026 · **Grundlag:** app-repoets `main` (`9c32633`) og den levende database (læst 8. nov.) · **Status:** forslag til Eric; der er ikke ændret noget.

> **Afløst 2026-11-10:** Mærkerne "Ikke endeligt godkendt" og "Familiens forslag" er afløst af ejerbeslutningen 2026-11-10 (faktatjekket tæller som godkendt; kun "Ikke faktatjekket" er et advarselsmærke; "Familiens forslag" hedder nu "Andre mulige steder"). Se `AGENTS.md` og `docs/change-log.md`.

## Kort konklusion

Turforslag kan åbnes for familien uden større ombygning. Adgangen er i dag låst til admins fire steder, og de skal ændres samlet i én PR: sider, serverfunktioner, databasefunktioner og databaseregler. Før åbningen bør tre ting på plads: (1) de dele af siden, der er værktøj for værten, skjules for familien; (2) der kommer et samlet loft over AI-forbruget, ud over de 5 handlinger pr. person pr. dag; (3) feedback-ordningen fra 8. november bygges med, så familiens oplevelser lander hos Eric og ikke i stedposterne.

## 1. Hvordan adgangen styres i dag

| Lag | Hvor | Regel i dag |
|---|---|---|
| Sider | `turforslag.tsx`, `mine-ture.tsx`, `mine-ture.$id.tsx` | Sender alle andre end admins til forsiden |
| Serverfunktioner | `trip-plan.functions.ts` (planTrip, writeTrip, suggestTrip, kvote), `saved-trips.functions.ts` | `requireAdmin` / `requireTripAdmin` |
| Databasefunktioner | `consume_trip_ai_quota()`, `get_trip_ai_quota()` | Afviser alle andre end admins |
| Databaseregler (RLS) | `saved_trips` (læs og gem) | Kun egen række, og kun admins |
| Menu | `app-shell.tsx` | Turforslag og Mine ture vises kun for admins |

Brugere i dag: 3 admins og 7 i familien. Ingen gemte ture endnu (`saved_trips` = 0), og kvotetabellen er tom.

Det, der allerede passer til familien: AI-kaldene kører kun på serveren, og nøglerne kommer ikke i browseren. Hver person kan højst bruge 5 AI-handlinger om dagen (atomisk talt i databasen). Gemte ture er private for den, der har gemt dem. Siden "Find en tur" (uden AI) er allerede åben for familien.

## 2. Hvad der skal ændres for at åbne

1. **Én databasemigrering** (`drizzle/migrations/`, kan gentages uden skade): kvotefunktionerne og `saved_trips`-reglerne skal tillade `family` og `admin` i stedet for kun `admin`. Lovable kører ikke migreringer selv; Claude anvender den med `query_database` efter merge, som ved #19.
2. **Serverfunktionerne:** én fælles kontrol "familie eller admin" i stedet for de to admin-kontroller.
3. **Siderne og menuen:** samme regel; admins beholder alt.
4. **Skjul værtsværktøjer for familien:** "Kun data (uden tekst)", "Rådata (til Ecco i næste trin)" og "Noter til værten". Modelnavnet ("Skrevet af Ecco (…)") og teksten om OpenAI som reserve kan erstattes af en neutral sætning.

## 3. Risici og forslag

| Risiko | Forslag |
|---|---|
| **AI-udgift.** 10 brugere × 5 handlinger giver højst 50 AI-kald om dagen. | Et fælles dagligt loft for hele familien (fx 20 handlinger), ud over loftet pr. person. Beløbet pr. kald måles i de første uger i stedet for at blive gættet. Loftet på 20 $ om måneden fra 2. november er stadig kun et forslag; Eric beslutter. |
| **Forkerte eller forældede oplysninger** (åbningstider, lukkede steder). | Siden siger allerede "Tjek åbningstider og vejr igen før afgang". Behold det. Mærket "Ikke endeligt godkendt" vises allerede på steder, der ikke er godkendt. |
| **Gemte ture med indhold fra browseren.** `saveTrip` gemmer den plan og tekst, som browseren sender. | Lav risiko, så længe ture kun kan ses af den, der har gemt dem. Hvis ture senere skal deles i familien, skal serveren selv gemme planen og teksten. |
| **Misbrug af fritekstfeltet** ("Beskriv jeres ønske", højst 800 tegn). | Allerede begrænset: modellen kan kun vælge steder fra kataloget, og serveren beholder kun katalog-ID'er. |
| **Kvoten kan ikke nulstilles af admin.** | Lille funktion under Administration: se forbrug pr. person og nulstil dagens tal. |

## 4. Feedback (Erics beslutning 8. november)

- Knap "Giv feedback" på hvert sted i et turforslag og på hele turen. Brugeren kan vælge "Fakta passer ikke" (lukket, tider, pris) eller "Min oplevelse", og der er et fritekstfelt.
- Feedback gemmes i en ny tabel med bruger, sted, tur, dato og type. Kun admins kan læse den. Den ændrer aldrig et sted eller en tur automatisk.
- Under Administration får Eric en liste, grupperet pr. sted. Hver linje har dato og navn, så Eric kan tage en snak med brugeren. Der er ingen tidsgrænse; Eric vurderer selv, om noget er forældet, og om brugerne har talt sammen.
- Én melding om "lukket" eller "farligt" giver straks mærket "tjek før besøg" på stedet, indtil Eric eller et faktatjek har afklaret det.
- Det, Eric beslutter, føres tilbage i places-repoet som kilde (`secondary`, Erics samtale med brugeren). Det er samme fremgangsmåde som ved screenshots i dag.

## 5. Forslag til rækkefølge

1. **PR 1 (app):** adgang for familien (punkt 2.1-2.4), fælles dagligt loft og admin-oversigt over kvoten. Selvtesten udvides med en familiebruger (skal blive afvist ved loftet og må ikke se værtsværktøjerne).
2. **PR 2 (app):** feedbackknap, feedbacktabel og Erics liste.
3. **Åbning:** Eric slår det til ved at merge og publicere. Derefter kører den fulde selvtest, og de første uger bruges til at følge forbruget.

PR 1 og 2 kan også samles i én levering, hvis Eric foretrækker det.

## Beslutninger, Eric skal træffe

1. Skal familien have adgang nu (efter PR 1), eller først når feedback er klar (efter PR 2)?
2. Hvor højt skal det fælles daglige loft være (forslag: 20 handlinger), og skal der være et månedsloft i kroner?
3. Skal gemte ture kunne deles med resten af familien, eller forbliver de private?
