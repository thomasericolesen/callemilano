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
5. **Not yet done for the 14 drafts:** coordinates and route-checked driving time (blocking), source URLs for beach facts (the ADEAC list URL is now recorded in all 14; it was read via a WebFetch summary, edition 2026-2027, with a 2027 verification footnote), independent check of rocks (absence of mention is not confirmation), seasonality.
6. **Carta de Servicios 2026 also covers the other Fuengirola beaches** (Castillo-Ejido, Fuengirola, Carvajal); only Boliches-Gaviotas was mined for facts.

## Proposed correction to the change-log (not applied)

Append a new dated entry; the log is chronological, so the old entry stays and gets a one-line pointer.

> ## 2026-10-29 - Correction: layer placement follows route-checked driving time
>
> Owner decision 2026-10-29: layer placement is decided by route-checked one-way driving time, as the scope section of `AGENTS.md` and the `local_30km` rule text in `data/layers.csv` already state. This supersedes the "Layer boundary rule" bullet in the entry "2026-10-15 - Layer-boundary decision and post-fact-check corrections", which placed records by straight-line distance.
>
> Threshold (owner decision 2026-10-29): `local_30km` means a route-checked one-way driving time of up to 30 minutes, not 30 km straight-line. It takes effect when the driving times have been measured (Google Maps, start Casa de la Familia, Saturday 10:00).
>
> Not changed by this entry: any record, `data/layer-membership.csv`, `data/layers.csv`. Consequence to resolve once the threshold applies: Malaga (36 min), Tolox (56 min) and Marbella old town (34 min in `data/route-checks-2026-10-16.csv`, no time on its record) exceed 30 minutes and would leave `local_30km`. Their new placement needs a decision.

Suggested pointer under the old bullet: `Superseded 2026-10-29, see the correction entry above.`

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
