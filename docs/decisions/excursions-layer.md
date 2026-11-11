# Excursion layer (3–4 h)

**Decision:** owner, 2026-10-15. **Status:** draft package awaiting editor-of-record approval and a change-log entry (see `docs/change-log.md`).

## What it is

A second layer beside the 30 km local layer (`local_30km`). The excursion layer (`excursions_4h`) holds destinations reachable by a route-checked one-way drive of up to about 4 h, for day trips and overnight stays. Audience: young adults. Themes: nature and hiking, city life, culture and architecture, food, bars, cafés and wellness.

Layers are defined in `data/layers.csv`. Which record belongs to which layer is listed in `data/layer-membership.csv`. This is an analytical file; it is not a second source of truth for place records. Layer is deliberately **not** a field in the record schema (no schema change needed): it follows from the route-checked driving time.

## What was added

17 draft records, all `status: draft`, with allocated IDs and:

- no coordinates and no route-checked driving time (blocking review issues),
- no sourced facts (identity-level placeholder descriptions, empty evidence),
- provisional editorial estimates only for `teenagers` and `adults` (other groups `unknown`).

| Catalogue group | Records |
|---|---|
| Tæt på | Málaga, Sierra de las Nieves, Tolox, Caminito del Rey, Gibraltar |
| Dagsture | Setenil de las Bodegas, Antequera, El Torcal de Antequera, Nerja, Tarifa, Vejer de la Frontera |
| Længere væk | Granada (incl. Alhambra), Sevilla, Córdoba, Cádiz, Jerez de la Frontera, Las Alpujarras |

The catalogue group is editorial (from the Danish inspiration catalogue of 2026-10-15) and says nothing verified about driving time.

## Not included, and why

- **Gibraltar:** included by owner decision (2026-10-15) although it is not in Spain; see its record for the ID and country handling the editor must approve.
- **El Puerto de Santa María and Sierra Nevada as separate places:** left for later; Sierra Nevada is mentioned under Las Alpujarras.
- **Alhambra:** part of the Granada record (owner decision 2026-10-15).

## Next steps per record (in order)

1. Establish the named visitor point and coordinates from an official source.
2. Route-check the one-way drive from Casa de la Familia; record source and date.
3. Fact-check from official sources; fill evidence; replace placeholder descriptions.
4. Set duration tag from the route-checked time; review ratings; human approval.
