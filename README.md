# CalleMilano

CalleMilano is a family travel guide for guests staying at Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas (Málaga). Its recommendations start from places saved in Google Maps and are organized to help families choose and plan outings.

## Current scope (from 2026-10-05)

- **Area:** destinations within a one-way drive of at most 30 minutes from Casa de la Familia, using Google Maps' main figure (owner decision 2026-10-29; straight-line distance is no longer used). Places further away belong to the excursion layers or stay in the collection as an archive; archive places are not developed or recommended in the current phase.
- **Primary audience:** families with children who do not want long drives.
- **Secondary audiences:** adults, seniors, and teenagers.
- **Origin point:** Plus Code `8C8QG8PP+7W` = 36.53569, -4.66269.
- **Excursion layer (from 2026-10-15):** destinations up to about 4 h one-way by route-checked drive, aimed at young adults. See `AGENTS.md` and `data/layers.csv`.

See [AGENTS.md](AGENTS.md) for the full guidance and [docs/README.md](docs/README.md) for a map of the documentation.

## Place categories

- Restaurants
- Beaches
- Excursions
- Nature
- City
- Family activities

## Place content

Each published place should include a short description, a long description, recommended age groups, one-way driving time from Casa de la Familia, tags, an SEO title, an SEO description, and alt text for each image. See [docs/place-schema.md](docs/place-schema.md) for the data contract.

## Project folders

- `docs/places/` — canonical place records (Markdown with YAML front matter)
- `docs/` — project, editorial, and design documentation
- `data/` — registers (IDs, import queue, image rights), the generated catalog, and analytical datasets for the recommendation prototype; see [docs/data-dictionary.md](docs/data-dictionary.md)
- `tools/` — `places.py` (validation and catalog), `app_export.py` (app export), `intake.py` (intake pipeline), `trip.py` (trip plans; command line only, the logic is in `trip_core.py`, `trip_weather.py`, `trip_traffic.py`, `trip_restaurants.py`, `trip_plan.py` and `trip_render.py`), `route_check.py` (drive times); shared paths, origin and helpers live in `common.py`
- `tests/` — unit tests
- `demo/` — static questionnaire prototype
- `prompts/` — reusable prompts for research and content drafting

## Tooling

```sh
pip install pyyaml
python3 tools/places.py validate   # structural validation gate
python3 tools/places.py catalog    # regenerate data/place-catalog.csv
python3 -m unittest discover -s tests   # run all tests
```
