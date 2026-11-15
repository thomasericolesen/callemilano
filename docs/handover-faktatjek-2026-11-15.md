# Overdragelse til Desktop (Opus): faktatjek af 68 nye kandidater

Repo: callemilano. Regler: `AGENTS.md` (indlæses via `CLAUDE.md`). Rapportér på dansk.

## Opgave
Faktatjek 68 nye kandidatsteder inden for 30 min kørsel (køretid er allerede rutetjekket, læs den ikke igen). Fakta der skal bekræftes pr. sted: **hvad stedet faktisk er** (type, fx tapasbar vs. restaurant), **prisniveau/priser**, **åbningstider/lukkedage**, **børnevenlighed** (børnemenu, høje stole, legeområde, mindstealder/-højde, børnepriser), **om stedet stadig er åbent**. Kørestolsadgang er mindre vigtigt.

## Hvad gik galt første gang (så det ikke gentages)
Haiku-læsere hentede tekst fra hjemmesider, og jeg åbnede ingen sider selv. Resultatet: tapasbar blev ikke opdaget, prisniveau mangler, nogle sider var forkert identitet (fx "Cafetería San Chocolate" er et marokkansk chokoladebrand, ikke en café), og "ok, 0 citater" blev godtaget som færdigt.

## Arbejdsmåde (Opus som orkestrator)
1. For hvert sted: **åbn selv hjemmesiden** (eller Google Maps-kortet, hvis ingen hjemmeside) og bekræft identitet: samme navn, adresse og stedtype som kandidaten. Noter stedtypen med egne ord fra siden (tapasbar, strandbar osv.). Stemmer typen ikke med gruppen, markér det.
2. Brug Google Maps til identitet, adresse, kontaktoplysninger og kildelink. Maps må **ikke** bruges som kilde til priser, børneregler eller adgang (AGENTS.md).
3. Hvis hjemmesiden mangler eller ikke virker: Facebook, derefter Instagram (Claude in Chrome, logget ind).
4. Smalle, mekaniske opgaver kan uddelegeres til Haiku (hent menu-PDF, udtræk priser fra en given side), men Opus **læser selv resultatet**, tjekker mindst to citater pr. batch mod den levende side, og afviser "0 citater" uden forklaring.
5. Ordrette citater i originalsprog, med URL og dato. Ingen gæt. Ukendt forbliver ukendt. Ratings og anmeldelsestal registreres aldrig.
6. Konflikter (fx modstridende åbningstider) lukkes aldrig: de går til redaktøren.

## Status fra skyen (mine fund, ikke garanteret korrekte)
- 28 sider gav citater (mest åbningstider), 14 sider læst uden fakta, 14 uden officiel side, 7 kræver Facebook/Instagram, 5 blokerede.
- Kendte problemer: La Reja og Café Bar Europa har modstridende åbningstider på egen side. E07 og E08 er det samme museum. H02 San Chocolate er forkert identitet. F07 Meli Melo har en parkeringsside som domæne. To restaurantsider viser "$" ved "€".
- Strandfakta kun for Calahonda og San Francisco (spain.info). Fire strande har "Strandtype ikke tjekket": Arroyo de la Miel, La Cala, Bonita, Víbora. Reglen om klippestrande kræver officiel kilde.

## Hvad der ikke må ske
Ingen stedposter, ingen ændring af status, kategori, tags eller familiescores (niveau C/D: redaktøren vælger). Ingen commit uden PR.

## Filer
Kandidatlisten, ruter og læsernes output ligger i skyens scratchpad og forsvinder med sessionen. Filerne ligger i `docs/handover-faktatjek-2026-11-15/`: `candidates-routed-part1/2.json` (rutetjekkede kandidater), `checklist-groups.json` (de 68 med faktatjek og forslag), `cloud-reader-output/` (Haiku-input og -output, upålidelige) og `checklist-template-with-assessment.html` (tjekliste-skabelon med vurderingsfelter).

Artifact med tjekliste (valg i `choices`): https://claude.ai/artifact/M3PyJYkeaA6hNrzS2mTbzu
