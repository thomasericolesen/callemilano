# Guest questionnaire specification

## Goal

Collect the minimum needed to return useful recommendations in under 10 seconds. Ask three short questions, with tap-to-select answers. Use the current recommendation engine and its existing persona weights, destination metadata, and tag preferences. Do not show guests the underlying suitability values, weights, or recommendation scores.

## Questions

| # | Guest question and answer choices | Why it is needed | Existing data used | Effect on recommendations |
|---:|---|---|---|---|
| 1 | **Which profile best fits your outing?** Family with young children; family with teenagers; active retired couple; grandparents with grandchildren; aviation enthusiast; hiking enthusiast; beach-focused family; mixed-age family group. | The current engine requires a persona to choose suitability weights, preferred duration/seasons, and tag preferences. One tap avoids asking separately for adult and child counts, exact ages, and interests. | The matching row in `data/personas.csv`; destination `children_score`, `teen_score`, `adult_score`, `senior_score`; `collection_tags` in `data/destination-classification.csv`. | Selects the corresponding existing persona. Its weights and tag preferences change each destination’s existing model score and therefore its order. Do not derive a new persona or alter weights from the answer. |
| 2 | **What is the longest one-way drive you want?** Up to 1 hour; up to 2 hours; up to 3 hours; up to 5 hours; any distance. | Distance is a major practical constraint for a day out from Casa de la Familia. | `drive_time_from_casa` in `data/destination-metadata.csv`, plus the persona’s existing `drive_time_weight` and `drive_time_scoring_rule` in `data/personas.csv`. | Treat the answer as an eligibility filter, not a new score: for a stated drive range, keep a destination only when the range’s upper end is within the selected limit. Then order eligible places with the unchanged recommendation formula. If the estimate is unknown or says “No direct drive,” do not claim it fits a finite limit. Drive estimates are rough and not route-checked; show them as estimates. |
| 3 | **How much time do you have for the outing?** Half-day; full day; overnight or longer. | Prevents recommendations that do not fit the guest’s available time. | `duration` in `data/destination-metadata.csv`, plus the persona’s existing `duration_weight`, `preferred_duration`, and `duration_scoring_rule` in `data/personas.csv`. | Treat the answer as an eligibility filter: half-day keeps half-day destinations; full day keeps half-day and full-day destinations; overnight or longer keeps all supported durations. Then apply the existing duration factor and full recommendation formula unchanged to order the remaining places. |

## Profile choice guidance

For the first prototype, use the closest existing persona as an intentionally simplified proxy for group composition. This keeps the questionnaire short and matches the inputs the current engine can use:

- **Family with young children:** family outing with children in the current young-child profile. Its destination data uses a single children suitability estimate; it cannot distinguish individual child ages.
- **Family with teenagers:** family outing with teenagers.
- **Grandparents with grandchildren:** a group bringing grandchildren and grandparents.
- **Mixed-age family group:** a group spanning ages that does not fit the grandparents profile.
- **Active retired couple:** an active older couple.
- **Beach-focused family:** choose when a beach outing is the defining trip profile.
- **Hiking enthusiast** or **Aviation enthusiast:** choose when that existing interest profile best describes the outing. The aviation profile has no aviation-specific destination tag, so its results may not identify aviation experiences.

For this prototype, do not ask separate questions for number of adults, number of children, or exact ages: the existing engine has no count fields or age-specific child values. Do not ask for a free-form preferred activity: activity preference is represented only by the selected existing persona’s tag preferences, and the engine has no separate user-selected tag weighting.

Future versions may collect exact group composition and age ranges if testing shows that those details produce materially different recommendations. Add those questions only alongside corresponding engine inputs and evidence that the extra detail improves recommendations.

## Ranking behavior

1. Select the existing persona from Question 1.
2. Apply Questions 2 and 3 as eligibility filters using the existing drive-time and duration metadata. These filters remove options that do not meet the guest’s stated constraints; they do not add weights or modify the scoring formula.
3. Rank the remaining destinations using the current formula and selected persona, including the existing suitability, drive, duration, weather, season, and tag components.
4. Present the results as natural-language recommendations. Do not display raw suitability values, persona weights, factor contributions, or final scores.

The engine currently has no separate guest answer for weather tolerance or travel season. Use the persona’s existing preferences and the destination metadata for those factors; do not add questions or scoring adjustments for them in this questionnaire.

## Expected completion time

Three single-select taps, with concise labels and no required typing. A guest who knows their group profile, drive limit, and available time should finish in under 10 seconds.
