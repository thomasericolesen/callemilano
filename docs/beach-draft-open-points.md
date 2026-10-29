# Beach drafts: open points (2026-10-29)

**Status:** local working note, committed locally only (not pushed). Covers the 14 draft records created from `strandoversigt.md` (snapshot 2026-10-15) and the points the owner asked to have noted rather than fixed. Nothing here changes an existing record, the published pages, `docs/change-log.md` or the app database.

## Open points

1. **La Cala: sand colour disagrees across sources; no record created (owner decision 2026-10-29).**
   - Snapshot: dark sand per the Mijas municipal-association document; the owner says fine sand.
   - `docs/published/la-cala-beach.md` (Mijas Tourism profile, checked 2026-10-04): fine sand and a sandy seabed, 1,258 m x 38 m on average.
   - Not resolved. The published page is unchanged. Resolve against the primary Mijas source before a record is created.
2. **Boliches-Gaviotas: location of the bathing zone for older people is disputed [partial].** Concejalía de Playas (https://www.fuengirola.es/concejalia/concejalia-de-playas/, undated) says Los Boliches; Fuengirola Accesible 2025 (edition 03/03/2025, p. 9) says Playa de San Francisco; the Carta de Servicios 2026 names no beach. Recorded as a warning issue (`elderly_bathing_zone_location_disputed`) with both sources; not stated as fact for this beach. Pergola 41 (accessible platform) is sourced from Fuengirola Accesible 2025 (p. 6, 2025 edition; the 2026 charter has no pergola numbers). It is no longer treated as an owner-supplied fact.
3. **Duplicate in the app database:** "Playa Bolonia" (Maps intake, no guide data) and "Duna de Bolonia" (`ES-AND-CAD-DUNA-DE-BOLONIA-001`, with guide data) are the same place. Noted only; nothing merged or deleted.
4. **Carvajal:** municipality set to Fuengirola by the owner (the Fuengirola Carta de Servicios 2026 counts it among its four beaches). The ADEAC list and El Español list it under both Fuengirola and Benalmádena.
5. **Driving times and coordinates (owner, 2026-10-29):** measured by Eric in Google Maps, Saturday 2026-07-18 10:00 (one sample), start Calle Milano 35, 29649 Las Lagunas de Mijas (36.5356, -4.6627), destination = Google's marker (Cabopino: parking point). Google's main figure is stored in `driving_time_from_casa_de_la_familia`, the typical range and the method in its note. No route URL exists, so `source` is a text description. The origin address is treated as Casa de la Familia because the coordinates match the project origin to about 10 m; no address source in the repo confirms it. Bajondillo, Playamar and Los Álamos are unchecked (Eric's own figure about 30 min; coordinates and times not yet read from the links) and keep the blocking issues. Still open for all 13: independent check of rocks, seasonality, source URLs for beach facts.
   - By the 30-minute rule on Google's main figure, these ten qualify for `local_30km`: Cabopino 20, Los Monteros 28, La Butibamba 16, Castillo-Ejido 12, Fuengirola centrum 18, Boliches-Gaviotas 16, Carvajal 20, Santa Ana 28, Fuente de la Salud 30, La Carihuela 30. `data/layer-membership.csv` is not changed. Fuente de la Salud and La Carihuela sit exactly on the limit; Google's range for both is 26-40 min.
   - Río Real was removed (owner decision 2026-10-29): draft, registry row and catalog row deleted; it does not become a record.
6. **Carta de Servicios 2026 also covers the other Fuengirola beaches** (Castillo-Ejido, Fuengirola, Carvajal); only Boliches-Gaviotas was mined for facts.

## Proposed change-log entry (not applied; awaiting the owner's approval)

Append a new dated entry; the log is chronological, so the old entry stays and gets a one-line pointer.

> ## 2026-10-29 - Rule for local_30km: Google driving time, whole layer (no schema change)
>
> Owner decision 2026-10-29: membership of `local_30km` is decided by a one-way driving time of at most 30 minutes, taken as Google Maps' main figure, not by straight-line distance. The rule applies to the whole layer, not only to beaches. This supersedes the "Layer boundary rule" bullet in the entry "2026-10-15 - Layer-boundary decision and post-fact-check corrections" (straight-line placement).
>
> Measurement method (beaches): measured by the owner in Google Maps on Saturday 2026-07-18 at 10:00, one sample, from Calle Milano 35, 29649 Las Lagunas de Mijas (36.5356, -4.6627) to Google's marker for the destination (Cabopino: the parking point). Google's main figure is stored in `driving_time_from_casa_de_la_familia.duration`; the typical range and method are stored in its note.
>
> - Rio Real was removed (draft; it does not become a record). 13 beach drafts remain.
> - Google main figures (min): Cabopino 20, Los Monteros 28, La Butibamba 16, Castillo-Ejido 12, Fuengirola centrum 18, Boliches-Gaviotas 16, Carvajal 20, Santa Ana 28, Fuente de la Salud 30, La Carihuela 30. All are within the limit. Fuente de la Salud and La Carihuela sit exactly on it and stay in the layer.
> - Bajondillo, Playamar and Los Alamos: not checked. The owner's own figure is about 30 min; coordinates and Google times have not been read. Proposed to stay in the layer on that figure, provisionally, until measured.
> - Moved out of `local_30km` by the new rule (proposed): Malaga (36 min), Marbella old town (34 min, `data/route-checks-2026-10-16.csv`), Tolox (56 min). New layer for the three: `excursions_4h` (their layer before 2026-10-15), to be confirmed by the owner.
> - Not changed by this entry: `AGENTS.md` line 9, `data/layers.csv`, `data/layer-membership.csv`, schema, categories, tags, enums.
> - Open: update `AGENTS.md` line 9 and the `local_30km` rule text in `data/layers.csv` to the new rule; the measurement is one summer-Saturday sample.
> - Local only. Not pushed or merged.

Suggested pointer under the old bullet: `Superseded 2026-10-29, see the local_30km rule entry above.`

## App database (Supabase): proposed text fixes, not executed (waiting until the owner has spoken with Christian)

Table `public.recommendations`. Expected effect: 1 row and 14 rows.

```sql
-- Preview
select title, description from public.recommendations
where description like '%anslået 15–30 min%' or description like '%(ny i 2026)%';

-- 1. Remove "ny i 2026": the snapshot only says Blue Flag 2026, and El Español names only Carvajal and Fuente de la Salud as new.
update public.recommendations
set description = replace(description, 'Blå flag 2026 (ny i 2026)', 'Blå flag 2026')
where title = 'Playa Fuengirola (centrum)' and kind::text = 'inspiration' and category::text = 'strand';

-- 2. "15–30 min" is the inclusion criterion, not a measurement.
update public.recommendations
set description = replace(description, 'Køretid fra huset er ikke målt (anslået 15–30 min).', 'Køretid fra huset er ikke målt.')
where kind::text = 'inspiration' and category::text = 'strand' and guide is null and lat is null
  and description like '%anslået 15–30 min%';
```

A 15th row, "La Cala bystrand", has the same sentence but also guide data with `drive_minutes` 12, so the text contradicts its own row. It is left out of the update; it needs a separate decision.

## Toilets

`toilets_available` is `unknown` for Cabopino/Artola (owner decision 2026-10-29) and, by the same rule, Castillo-Ejido and Fuengirola centrum (previously `yes` from secondary sources). Easily reversed once a source is verified.
