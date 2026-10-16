# Excursion layer — overlap with existing material

Nothing listed here was edited by the package. Decisions are for the editor-of-record.

## Existing place records that match catalogue destinations

| Catalogue destination | Existing record | Note |
|---|---|---|
| Ronda og Setenil | `ronda` (ES-AND-MAL-RONDA-001) | Setenil is new (`setenil-de-las-bodegas`); link both via `related_places` after fact check. |
| Nerja og Frigiliana | `frigiliana` (ES-AND-MAL-FRIGILIANA-001) | Nerja is new (`nerja`). |
| Marbella og Puerto Banús | `marbella-old-town` (ES-AND-MAL-MARBELLA-OLD-TOWN-001) | In `local_30km`. Puerto Banús is not added (local layer, intake pending). |
| Tarifa, Bolonia, Vejer | `baelo-claudia`, `duna-de-bolonia` | Tarifa and Vejer are new. Baelo Claudia has category `Family activities` (open question from `docs/project-state.md`). |

## Examples in `docs/examples/`

- `nerja-example.md` uses ID `ES-AND-MAL-NERJA-001` (slug `nerja-malaga`). The new record `nerja` reuses that ID because the ID format fits the real place. The example is illustrative only, not a canonical record. Decide whether to rename the example's ID.
- `caminito-del-rey.md` uses ID `ES-AND-MAL-CAMINITO-DEL-REY-001` and category `Excursions`; the new record uses the same ID and category `Excursions` (owner decision 2026-10-15).

## Existing out-of-area records not in the catalogue (stay archive)

Zahara de la Sierra, Olvera Castle, Selwo Aventura, Aracena, Los Caños de Meca, Alcázar de Segovia and the northern/eastern Spain records. They are listed in no layer in `data/layer-membership.csv`. If the editor wants any of them in the excursion layer, add a membership row; no record change is needed.

## Local records without coordinates

Mercado de Atarazanas, Palmeral de las Sorpresas and Playa la Malagueta lie at roughly 29–31 km (see `docs/project-state.md`) and may belong to `local_30km` or the excursion layer depending on the route check. Not touched.
