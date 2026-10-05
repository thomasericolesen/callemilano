# Recommendation engine specification

## Scope and inputs

This specification calculates a persona-specific destination fit score using only:

- `data/personas.csv`
- `data/destination-metadata.csv`
- `data/destination-classification.csv`
- `data/destination-tag-vocabulary.csv`

A score is an editorial fit indicator from **0 to 100**, not a prediction of satisfaction or a safety assessment. Values in the destination metadata may be estimates, as identified in its `estimate_notes` column. The calculation does not adjust for the reliability of an estimate.

## Formula

Each non-tag destination factor is converted to a score from 0 to 5. First calculate the existing metadata-only base score using the persona weights:

```text
base_score =
  (children_suitability_weight × children_score / 5) +
  (teen_suitability_weight × teen_score / 5) +
  (adult_suitability_weight × adult_score / 5) +
  (senior_suitability_weight × senior_score / 5) +
  (drive_time_weight × drive_score / 5) +
  (duration_weight × duration_score / 5) +
  (weather_dependence_weight × weather_score / 5) +
  (season_weight × season_score / 5)
```

The weights in `personas.csv` total 100, so `base_score` is 0–100. Keep the unrounded value during calculation. Apply tags as a separate 15% component; scale the base score to 85% so the combined result remains on the same 0–100 scale:

```text
final_score = (0.85 × base_score) + (0.15 × tag_score_on_0_to_100)
             = (0.85 × base_score) + (15 × tag_fit / 5)
```

`tag_fit` is 0–5, defined below. Keep full precision for sorting; display the final result rounded to the nearest whole number. Do not renormalize the existing persona weights when a factor weight is zero; that factor contributes zero by design.

## Factor scoring

### Suitability

Use the numeric values in the destination row directly:

- `children_score` with `children_suitability_weight`
- `teen_score` with `teen_suitability_weight`
- `adult_score` with `adult_suitability_weight`
- `senior_score` with `senior_suitability_weight`

Each value is expected to be an integer from 0 through 5. A persona's zero weight means that age group does not affect that persona's score.

### Drive time

Convert `drive_time_from_casa` to hours, using the midpoint for a stated range. Apply the persona's `drive_time_scoring_rule`:

| Estimated one-way drive | Score |
|---|---:|
| Up to and including 1 hour | 5 |
| More than 1 hour through 2 hours | 4 |
| More than 2 hours through 3 hours | 3 |
| More than 3 hours through 5 hours | 2 |
| More than 5 hours | 1 |
| No direct drive or unknown | 0 |

For a range that crosses a threshold, use its midpoint. Text such as “No direct drive” and “Unknown” receives 0. The existing drive estimates are rough editorial ranges, not route-checked travel predictions.

### Duration

Match the destination's `duration` value to the persona's `preferred_duration` and its `duration_scoring_rule`. The supported values are `half-day`, `full-day`, and `overnight`. Use the persona's explicit mappings in `duration_scoring_rule`; where that field says `unknown:2`, an unknown duration scores 2. Do not infer a new duration from drive time during scoring: trip duration is already set in the destination row.

### Weather dependence

Use the persona's `weather_scoring_rule`, which maps the destination's `weather_dependency` value as follows:

| Destination weather dependence | Score |
|---|---:|
| `low` | 5 |
| `medium` | 3 |
| `high` | 1 |
| `unknown` | 2 |

Higher destination weather dependence therefore lowers the fit score for all current personas; personas differ in how much this factor weighs.

### Season

Use `season` from the destination row and `preferred_seasons` from the persona row. Values are semicolon-separated. Normalize case and whitespace before comparing.

- Destination season `all-year`: score 5.
- Every listed destination season is preferred by the persona: score 5.
- At least one, but not all, listed destination seasons are preferred: score 3.
- No destination season overlaps the persona's preferences: score 1.
- Missing or unrecognized season: score 2.

`all-year` means the destination is listed as suitable all year in the metadata; it does not imply every facility or activity operates year-round.

## Destination tags

Read each destination's tags from `data/destination-classification.csv`; use the exact controlled vocabulary in `data/destination-tag-vocabulary.csv`. Tag preferences below are editorial persona rules. Each vocabulary tag is assigned once per persona as preferred, neutral, or avoided.

| Persona | Preferred tags | Neutral tags | Avoided tags |
|---|---|---|---|
| Family with young children | `beach-and-bathing`, `caves-and-underground`, `family-attractions`, `markets-and-local-life`, `urban-waterfront` | `geology`, `dramatic-coastline`, `mountain-lakes`, `viewpoints`, `white-villages-and-towns`, `historic-fortifications`, `archaeology-and-heritage`, `waterfalls-and-cascades`, `rivers-and-gorges`, `protected-nature`, `unusual-engineering`, `island-and-mountain-landscapes` | `hiking-and-trails` |
| Family with teenagers | `beach-and-bathing`, `caves-and-underground`, `dramatic-coastline`, `geology`, `historic-fortifications`, `hiking-and-trails`, `island-and-mountain-landscapes`, `unusual-engineering` | `mountain-lakes`, `viewpoints`, `white-villages-and-towns`, `archaeology-and-heritage`, `waterfalls-and-cascades`, `rivers-and-gorges`, `protected-nature`, `urban-waterfront`, `family-attractions` | `markets-and-local-life` |
| Active retired couple | `archaeology-and-heritage`, `geology`, `historic-fortifications`, `markets-and-local-life`, `protected-nature`, `viewpoints`, `white-villages-and-towns` | `dramatic-coastline`, `beach-and-bathing`, `mountain-lakes`, `hiking-and-trails`, `waterfalls-and-cascades`, `rivers-and-gorges`, `caves-and-underground`, `urban-waterfront`, `unusual-engineering`, `island-and-mountain-landscapes` | `family-attractions` |
| Grandparents with grandchildren | `archaeology-and-heritage`, `beach-and-bathing`, `family-attractions`, `markets-and-local-life`, `urban-waterfront`, `viewpoints`, `white-villages-and-towns` | `geology`, `mountain-lakes`, `historic-fortifications`, `waterfalls-and-cascades`, `caves-and-underground`, `protected-nature`, `unusual-engineering`, `island-and-mountain-landscapes` | `dramatic-coastline`, `hiking-and-trails`, `rivers-and-gorges` |
| Aviation enthusiast | `geology`, `island-and-mountain-landscapes`, `unusual-engineering`, `viewpoints` | `dramatic-coastline`, `beach-and-bathing`, `mountain-lakes`, `white-villages-and-towns`, `historic-fortifications`, `archaeology-and-heritage`, `hiking-and-trails`, `waterfalls-and-cascades`, `rivers-and-gorges`, `caves-and-underground`, `protected-nature`, `urban-waterfront`, `markets-and-local-life`, `family-attractions` | None |
| Hiking enthusiast | `geology`, `hiking-and-trails`, `island-and-mountain-landscapes`, `mountain-lakes`, `protected-nature`, `rivers-and-gorges`, `viewpoints`, `waterfalls-and-cascades` | `dramatic-coastline`, `beach-and-bathing`, `white-villages-and-towns`, `historic-fortifications`, `archaeology-and-heritage`, `caves-and-underground`, `unusual-engineering`, `family-attractions` | `markets-and-local-life`, `urban-waterfront` |
| Beach-focused family | `beach-and-bathing`, `dramatic-coastline`, `family-attractions`, `protected-nature`, `urban-waterfront`, `viewpoints` | `geology`, `mountain-lakes`, `white-villages-and-towns`, `historic-fortifications`, `archaeology-and-heritage`, `waterfalls-and-cascades`, `rivers-and-gorges`, `caves-and-underground`, `markets-and-local-life`, `unusual-engineering`, `island-and-mountain-landscapes` | `hiking-and-trails` |
| Mixed-age family group | `archaeology-and-heritage`, `beach-and-bathing`, `family-attractions`, `historic-fortifications`, `markets-and-local-life`, `urban-waterfront`, `viewpoints`, `white-villages-and-towns` | `geology`, `dramatic-coastline`, `mountain-lakes`, `waterfalls-and-cascades`, `rivers-and-gorges`, `caves-and-underground`, `protected-nature`, `unusual-engineering`, `island-and-mountain-landscapes` | `hiking-and-trails` |

### Tag score calculation

- A preferred tag scores **5**.
- A neutral tag scores **3**.
- An avoided tag scores **0**.
- Deduplicate a destination’s tags before scoring.
- `tag_fit` is the arithmetic mean of its tag scores, from 0 to 5. Do not weight individual tags differently.
- If a destination has no classification row or no tags, set `tag_fit` to **3** (neutral). If a tag is not in the controlled vocabulary, ignore that tag and flag the classification for correction; if no valid tags remain, use 3.
- Convert to the tag component on the 0–100 scale as `tag_score_on_0_to_100 = tag_fit / 5 × 100`. Its maximum contribution to `final_score` is 15 points. A neutral-only tag set contributes 9 points; avoided tags lower the tag component.

The tag vocabulary contains no `aviation` tag. The Aviation enthusiast persona therefore uses `viewpoints`, `unusual-engineering`, `island-and-mountain-landscapes`, and `geology` as available indirect interests; this is not an aviation-specific match. Do not infer an aviation tag or add one to the controlled vocabulary here.

## Missing and malformed values

- Use the fallback score defined above for unknown drive time, season, duration, or weather values.
- Suitability values are numeric in the current metadata. If a suitability value is absent or nonnumeric, use 0 for that factor and flag the row for correction; do not silently invent a replacement.
- If a required persona weight is missing, do not calculate a score for that persona until its weights are complete and total 100.
- Preserve estimate notes alongside results. The score itself does not communicate evidence quality or confidence.

## Example

For a persona with a 30-point children weight and a destination `children_score` of 4, the children contribution to `base_score` is `30 × 4 / 5 = 24` points. Calculate and sum the other base contributions the same way. If `base_score` is 70 and the destination has one preferred tag and one neutral tag, `tag_fit = (5 + 3) / 2 = 4`; the tag component is 80/100 and `final_score = (0.85 × 70) + (0.15 × 80) = 71.5`, displayed as 72. A destination with an unknown drive time receives a drive score of 0 under the current persona rule; its estimate note should remain visible with the resulting recommendation.
