# Turforslag i to faser: forarbejde og turforslag

Ejerbeslutninger 2026-11-01 (se `docs/change-log.md`). Turforslag er et præsentationslag oven på stedposterne.
Det ændrer ikke stedskemaet eller livscyklussen i `docs/place-schema.md`.

## Princip

Den langsomme og usikre research (websøgning efter restauranter og åbningstider) laves **på forhånd** med agenter,
hvor der er tid til kilder, og hvor redaktøren kan godkende. Selve turforslaget er derefter et hurtigt opslag
plus live-data (vejr, trafik). AI bruges kun til at skrive teksten og til hurtige tjek, når noget mangler.

```text
FASE 1 – FORARBEJDE (agenter, efter behov / hver 2.–3. måned)
  /restaurant-indsamling  → CHARLIE pr. område → data/restaurant-directory.csv
  /aabningstider          → ALPHA (A) pr. sted  → visit_information + evidens i docs/places/
  (redaktøren gennemser og committer)

FASE 2 – TURFORSLAG (ca. et minut)
  /turforslag → spørgsmål: steder, dag, gruppe
       │
       ▼
  tools/trip.py plan   ── script, ingen AI ──────────────────────────────────────────────
     • steder + forslag i nærheden (Alphas punkt 1, som regler)
     • åbningsstatus fra stedposten + helligdage (data/holidays.csv)
     • "Bravo": vejr (Open-Meteo, reserve met.no) + råd; trafik (DGT) + live-link
     • restauranter fra kataloget: 3 dyre / 3 mellem / 4 billige i gåafstand
     • "Delta": automatiske tjek → ok / ok_med_forbehold / kræver_tjek / blokeret
       │
       ├─ kræver_tjek → ALPHA (B): hurtigt tjek af kun de markerede steder → hours-check.json
       ▼
  ECCO → trip.json → turforslag.pdf + turforslag.html (mobil)
```

Navnene lever videre. **Alpha** og **Charlie** er indsamlingsagenter. **Bravo** (vejr/trafik) og
**Delta** (kvalitetskontrol) er nu regler i `tools/trip.py`. **Ecco** skriver turforslaget.

## Filer

| Fil | Hvad |
|---|---|
| `.claude/agents/alpha.md` | Åbningstider: A = forarbejde i stedposter, B = hurtigt tjek til et turforslag |
| `.claude/agents/charlie.md` | Restauranter pr. område (kun forarbejde) |
| `.claude/agents/ecco.md` | Skriver turforslaget og laver PDF |
| `.claude/skills/turforslag/` | `/turforslag` (fase 2) |
| `.claude/skills/restaurant-indsamling/` | `/restaurant-indsamling` (fase 1) |
| `.claude/skills/aabningstider/` | `/aabningstider` (fase 1) |
| `tools/trip.py` | `plan`, `hours-status`, `coverage`, `check-restaurants`, `render` og enkeltopslag (`places`, `nearby`, `weather`, `traffic`, `restaurants`) |
| `data/restaurant-directory.csv` | Det lette restaurantkatalog |
| `data/restaurant-areas.csv` | Områder til restaurantindsamling (lokalt lag: 5 områder, 13 steder) |
| `data/holidays.csv` | Helligdage i Andalusien 2026–2027 fra BOJA, plus lokale helligdage, når de er fundet |
| `trips/<id>/` | Et turforslags filer: `plan.json`, evt. `hours-check.json`, `trip.json`, `turforslag.pdf/.html` (ikke i git) |

## Ejerbeslutninger 2026-11-01

1. **Værten kører det.** En selvbetjeningsløsning for gæster kan bygges senere oven på `tools/trip.py plan`.
2. **To faser** (forarbejde + hurtigt turforslag) i stedet for fem agenter, der arbejder ved hvert turforslag.
3. **Restauranter indsamles på forhånd pr. område** og opdateres ca. hver 3. måned.
4. **Prisklasser** (voksens hovedret + én drikkevare): billig < 15 €, mellem 15–35 €, dyr > 35 €.
5. **Afstand restaurant–sted:** ca. 10 minutters gang (≤ 800 m luftlinje). Det udvides kun ved mangel, til ca. 3 km
   markeret "kort kørsel".
6. **Restauranter i et let katalog**, ikke som fulde stedposter.
7. **Gratis datakilder:** Open-Meteo/met.no og DGT. Ingen betalt trafikprognose.
8. **Levering:** PDF til print og telefon; den mobilvenlige HTML kan også sendes.
9. **Sprog:** dansk.

## Regler i `tools/trip.py plan`

**Åbningsstatus** (fra stedpostens `visit_information` og evidens med feltet `visit_information` eller
`visit_information.schedule`):

| Status | Betydning | Følge |
|---|---|---|
| `aktuel` | Åbningstider tjekket ≤ 60 dage siden og ikke udløbet (`valid_until`) | Ecco læser fritekst for turdatoen |
| `forældet` | Over 60 dage eller `valid_until` passeret (fx sæsonlukket) | Hurtigt tjek (Alpha B) |
| `uden_dato` | Åbningstider uden evidensdato | Hurtigt tjek |
| `ukendt` | Ingen åbningstider, men kategorien har normalt faste tider (`Family activities`, `Excursions`, tag `Museum`) | Hurtigt tjek |
| `åbent_område` | Strand, by, natur uden registrerede tider | "Åbent område" |

**Vejrråd** (tommelfingerregler): regn ≥ 50 % eller ≥ 2 mm betyder plan B for strand, og forslag med tag
`Rainy day` prioriteres. Vindstød ≥ 40 km/t (eller vind ≥ 30) giver et blæse-råd. UV ≥ 6 giver solråd, og
over 32 °C frarådes lange gåture midt på dagen.

**Automatiske tjek** (Delta), med niveauerne `blokeret`, `tjek`, `forbehold` og `info`:

- dato i fortiden (`blokeret`);
- helligdag på datoen (`forbehold`), og år uden helligdagsdata (`forbehold`);
- åbningstider ukendte, forældede eller uden dato (`tjek`);
- regn ved strand, over 30 min kørsel med børn ≤ 6 år, køretid ikke route-tjekket (`forbehold`);
- restauranthuller og restauranter tjekket for over 6 måneder siden (`forbehold`);
- udkast-poster, børn velkomne ukendt, tilgængelighed ikke vurderet (`info`).

Med børn udelades restauranter med `kids_welcome: nej`, og `ja` vises først.

## Kildepolitik

| Oplysning | Tilladt kilde | Ikke tilladt |
|---|---|---|
| Åbningstider, priser, booking | Stedets officielle side, kommune, turistkontor | Google Maps, blogs, hukommelse |
| Helligdage | BOJA/BOE, kommunens officielle side | Kalendersider uden kilde |
| Vejr | Open-Meteo, met.no (hentet til turdatoen) | "Normalt vejr" |
| Trafik | DGT DATEX II; route-tjekket køretid fra posten | Estimeret køretid |
| Restaurant: adresse, telefon, koordinater | Egen side; Google Maps-opslag (identitet) | |
| Restaurant: pris | Egen menu; ellers €-markering fra TheFork/Tripadvisor (noteres) | Gæt |
| Restaurant: børn, dresscode | Egen kilde; ellers ≥ 2 uafhængige anmeldelser (Tripadvisor, Google, TheFork, Reddit) | Én anmeldelse |

## Restauranter: stedposter først (ejerbeslutning 2026-11-02)

Restauranter er fulde stedposter i `docs/places/` (kategori `Restaurants`). `tools/trip.py` læser dem først (status `needs_fact_check` eller senere; barer udelades) og bruger kun rækker fra kataloget nedenfor for steder, der endnu ikke er stedposter. Prisklassen kommer fra `cost_level` (€ = billig, €€ = mellem, €€€/€€€€ = dyr); står den `Unknown`, vælges restauranten ikke i en prisklasse, før den er faktatjekket. Kataloget er en let kandidatliste, der efterhånden omdannes til stedposter med `tools/intake.py`. Fælles regler for kilder og agenter: `docs/agent-pipeline.md`.

## Restaurantkataloget (`data/restaurant-directory.csv`)

Det er en bevidst let liste, ikke stedposter. Den går ikke gennem livscyklussen, får ikke id i
`data/place-id-registry.csv` og indgår ikke i `data/place-catalog.csv`. Restauranter, der skal have en redaktionel
side (som `restaurante-sheriff`), er fortsat fulde stedposter.

| Kolonne | Indhold |
|---|---|
| `restaurant_id` | `R-0001` …, stabilt, genbruges aldrig |
| `area_id` | Område fra `data/restaurant-areas.csv` |
| `name`, `address`, `municipality` | Som restauranten skriver det |
| `latitude`, `longitude` | WGS 84 fra Maps-opslaget |
| `phone`, `website` | Mindst én udfyldt |
| `cuisine` | Kort fritekst |
| `price_band` / `price_basis` | `billig`/`mellem`/`dyr` og hvordan det er fundet |
| `kids_welcome` / `kids_basis` | `ja`/`nej`/`ukendt` og `egen kilde`/`anmeldelser`/`-` |
| `dress_code` | `ingen`/`pæn afslappet`/`formel`/`ukendt` |
| `hours_note` | Kort note om lukkedage o.l. |
| `sources` | URL'er adskilt af mellemrum |
| `checked_at`, `checked_by` | ÅÅÅÅ-MM-DD og agent/person |
| `status` | `aktiv`/`skal tjekkes`/`lukket` |
| `notes` | Fritekst |

Valideres med `python3 tools/trip.py check-restaurants`.

## Stedposternes status

Poster, der ikke er `approved`, må bruges i turforslag, som værten selv gennemser. Turforslaget bærer så teksten
"Udkast – oplysningerne er ikke endeligt godkendt af redaktøren". Arkivsteder afvises af `tools/trip.py`.
Alpha B ændrer aldrig stedposter; fund går til redaktøren via `hours-check.json` og `/aabningstider`.

## Senere (ikke besluttet)

- Gæste-selvbetjening (webside) oven på `tools/trip.py plan`.
- Kommunernes lokale helligdage i `data/holidays.csv`.
- Restaurantområder for udflugtslaget (i dag kun lokalt lag).
- Betalt live-trafikprognose; kalenderfil (.ics); flere sprog.
