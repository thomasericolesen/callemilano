# Data dictionary

Last updated: 2026-10-05

This file defines every CSV in `data/` and `docs/enriched-place-metadata.csv`. Canonical place data lives only in the YAML front matter of `docs/places/*.md` (see `docs/place-schema.md`); nothing here overrides it.

## Registers and generated files (operational)

| File | Role | Edited by |
|---|---|---|
| `data/place-id-registry.csv` | Allocates stable place IDs. One row per allocated ID. | Intake, before a record leaves `draft` |
| `data/import-queue.csv` | Per-item intake progress for Maps imports. | Intake / workflow agents |
| `data/image-rights.csv` | Rights evidence for every image asset used by a record. | Editorial; human approves |
| `data/place-catalog.csv` | **Generated** read-only index of all records. | Only `python3 tools/places.py catalog` |

### `place-id-registry.csv`

| Column | Meaning |
|---|---|
| `namespace` | `ES-{REGION}-{PROVINCE}` prefix, e.g. `ES-AND-MAL` |
| `id` | Full stable ID `ES-{REGION}-{PROVINCE}-{PLACE}-{NNN}`; never reused or changed |
| `slug` | Record file name stem in `docs/places/` |
| `place_name` | Name at time of allocation |
| `state` | `allocated` (others such as `reserved`/`retired` are not yet used) |
| `reserved_at` | Allocation date |

Records whose identity is still unresolved (see `docs/identity-clarification-report.md`) stay in `draft` with `id: null` and have no registry row. This is intentional: an ID is allocated only once the place identity is confirmed.

### `import-queue.csv`

`intake_id`, `input` (name as saved in Maps), `status` (record lifecycle status), `retry_count`, `duplicate_candidate_ids` (semicolon list), `pending_clarification`, `assigned_stage` (`fact_check`, `editorial`, `seo`, `validation`, `human_review`), `last_update`. Only the first five pilot imports are queued; the later records were created without queue rows.

### `image-rights.csv`

`asset_id` (unique), `place_id`, `file` (path under `images/`), `source`, `rights` (licence/permission), `credit`, `permission_evidence` (URL or reference), `rights_status` (`approved`, `pending`, `withdrawn`), `reviewed_at`, `reviewer`. Only `approved` assets may be published.

### `place-catalog.csv` (generated)

`id`, `slug`, `name`, `status`, `category`, `tags`, `municipality`, `province`, `latitude`, `longitude`, `distance_km_from_casa` (great-circle km from the Casa origin in `AGENTS.md`), `within_primary_radius` (`yes` if ≤ 30 km; blank if coordinates are missing), `driving_time` (route-checked duration from the record, blank if unresolved), `record_file`. Sorted by distance.

### `maps-intake-projekt-spanien.csv` (212 rows)

Discovery input from the owner's Google Takeout export (2026-10-05), list "Projekt Spanien". Not place records and not evidence. Columns: `name` (as saved in Maps), `ring` (`origin`, `0-30`, `30-60`, `60-100`, `>100` km straight line from Casa; blank if unplaced), `distance_km`, `latitude`, `longitude`, `coord_precision`, `location_note`, `maps_feature_id`, `maps_url`.

The export contains no coordinates. Coordinates were assigned from general place knowledge (`approx` = known town/feature, town-level accuracy; `uncertain` = ambiguous name or inferred from the Maps feature-ID cluster; `origin` = the Casa address itself). Unplaced rows carry a region hint inferred from the feature ID. Coordinates must be confirmed from the Maps listing when a record is created; they are for triage only.

## Recommendation prototype datasets (analytical, non-canonical)

These feed `docs/recommendation-engine-spec.md` and the V1–V3 analyses. Values are **editorial estimates** unless a `source` column says otherwise. All keyed by `destination` (display name), not by place ID.

### `personas.csv` (8 rows)

| Column | Meaning |
|---|---|
| `persona` | Persona name |
| `*_weight` (8 columns) | Integer weights for children, teen, adult, senior suitability, drive time, duration, weather dependence, season. Each row sums to 100 |
| `preferred_duration`, `preferred_seasons` | Semicolon lists using `half-day`/`full-day`/`overnight` and `spring`/`summer`/`autumn`/`winter`/`all-year` |
| `*_scoring_rule` | Human-readable rule text; the authoritative rules are in the engine spec |

### `destination-metadata.csv` (30 rows)

| Column | Values |
|---|---|
| `children_score`, `teen_score`, `adult_score`, `senior_score` | Integer 0–5, editorial estimate |
| `energy_level` | `low`, `medium`, `high` |
| `duration` | `half-day`, `full-day`, `overnight` |
| `drive_time_from_casa` | Free-text range such as `4–5 h`; **not route-checked** |
| `season` | `all-year` or semicolon list of seasons |
| `weather_dependency` | `low`, `medium`, `high` |
| `estimate_notes` | Which values are estimates and why |

### `destination-classification.csv` (25 rows)

`collection_tags` (semicolon list from `destination-tag-vocabulary.csv`), `confidence` (`high`/`medium`/`low` for identity and classification, not visitor facts), `missing_information`, `classification_basis`. Frigiliana, Marbella Old Town, Ronda, Selwo Aventura and Zahara de la Sierra have no row; the engine then uses a neutral tag score.

### `destination-tag-vocabulary.csv` (18 tags)

`tag`, `description`. Collection tags in kebab-case (e.g. `beach-and-bathing`). Separate from, and not mapped to, the schema tags in `place-schema.md`.

### `demo-groups.csv` (20 synthetic groups)

`group_id`, `group_description`, counts of `adults`, `teenagers`, `children`, `seniors`, `reduced_mobility` (`yes`/`no`), `derived_persona_v1`, `derived_persona_v2`.

### Enrichment files (30 rows each)

All have `destination`, a `confidence` integer 0–100 (evidence strength for that row), and `source` (URLs, `;`-separated). Free-text values; `Unknown` means not established.

| File | Attribute columns |
|---|---|
| `accessibility-metadata.csv` | `wheelchair_access`, `stroller_access`, `accessible_toilets`, `parking_distance`, `steep_sections`, `step_free_route` |
| `booking-access-metadata.csv` | `reservation_required`, `seasonal_closure`, `age_restrictions`, `advance_booking_recommended`, `opening_hours_available` |
| `effort-metadata.csv` | `walking_distance`, `elevation_change`, `stairs_present`, `physical_effort`, `wheelchair_possible` |
| `facilities-metadata.csv` | `toilets`, `restaurant`, `cafe`, `parking`, `shade`, `stroller_friendly` |

### `docs/enriched-place-metadata.csv`

Long format, one row per destination and field: `destination`, `record_file`, `field` (schema field name), `value`, `confidence_score_0_100`, `source_urls`, `evidence_notes`, `checked_at`. A staging ledger for fact-check candidates; values must be re-verified before they enter a record's `evidence`. Located in `docs/` for historical reasons.

## Known gaps

- The analytical datasets cover the original Spain-wide collection. Only Marbella Old Town and the three Málaga city destinations lie near the primary 30 km area; the local launch candidates in `docs/launch-backlog.md` are not in these datasets yet.
- No mapping exists between collection tags and schema tags.
- Confidence uses two scales (`high/medium/low` and 0–100).
