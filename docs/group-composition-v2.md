# Group composition recommendations: Version 2 design

## Purpose and boundaries

Version 1 remains the current three-question prototype in `docs/guest-questionnaire-spec.md`. This document designs a future model that uses the group’s age composition and reduced-mobility needs. It does not change the current recommendation engine, its specification, or destination records.

The design reuses destination suitability estimates, the existing persona weights, and the existing recommendation formula. It adds no new destination score scale. Raw values remain internal; guest-facing results remain natural-language recommendations.

## Inputs

Collect counts for:

- **Adults:** ages 18–69
- **Teenagers:** ages 13–17
- **Children:** ages 0–12, including under 6 and ages 6–12
- **Seniors:** ages 70+
- **Reduced mobility:** yes if anyone in the group has a mobility limitation that affects choosing or using a destination; otherwise no

The age bands must be mutually exclusive so one person is counted once. The existing destination record has one `children_score`, so children under 6 and children 6–12 currently use the same estimate. Version 2 cannot claim age-specific suitability for those two child bands without new destination evidence and fields.

## How group composition changes ranking

### Group suitability

For each destination, calculate the group suitability estimate as the member-count-weighted average of the existing age suitability values:

```text
party_suitability =
  (children × children_score
   + teenagers × teen_score
   + adults × adult_score
   + seniors × senior_score)
  / total_group_size
```

This is on the existing 0–5 suitability scale. A cohort with zero members contributes zero. A larger cohort has proportionally more influence. If the group size is zero or any required suitability estimate is missing, do not present the result as a complete group-fit calculation; flag the destination for review.

### Preserve the existing recommendation formula

Derive an existing persona from composition as described below. Keep that persona’s drive, duration, weather, season, and tag rules unchanged. Replace its four separate age-suitability contributions with one group contribution, while keeping the same total age-factor weight:

```text
age_weight = children_suitability_weight
           + teen_suitability_weight
           + adult_suitability_weight
           + senior_suitability_weight

group_age_contribution = age_weight × party_suitability / 5
```

Use `group_age_contribution` in place of the persona’s separate age contributions in the existing base score. Keep its drive, duration, weather, and season contributions and its 15% tag component exactly as defined in `docs/recommendation-engine-spec.md`. This preserves the existing 0–100 formula and total persona weights; the group counts only redistribute the age-fit contribution among the age bands actually present.

### Effect of each input

| Input | Destination data used | Exact effect on ranking |
|---|---|---|
| Adults count | `adult_score` | Each adult contributes one `adult_score` term to `party_suitability`. More adults increase the share of group fit determined by adult suitability. |
| Teenagers count | `teen_score` | Each teenager contributes one `teen_score` term. More teenagers increase the share determined by teen suitability. |
| Children count | `children_score` | Each child, whether under 6 or 6–12, contributes one `children_score` term. The current data cannot distinguish the two child bands. |
| Seniors count | `senior_score` | Each senior aged 70+ contributes one `senior_score` term. More seniors increase the share determined by senior suitability. |
| Reduced mobility: no | None | No mobility filter or adjustment is applied. Use the existing recommendation formula. |
| Reduced mobility: yes | No suitable field exists in the current destination metadata | Do not infer accessibility from `energy_level`, age scores, or tags. Require a separately reviewed destination access status. Destinations confirmed to meet the group’s stated access need may remain eligible; known barriers are excluded from the accessible set; unknown status is shown separately as “access not confirmed,” never presented as accessible. |

The mobility answer cannot produce a responsible numerical ranking from the current files alone. A future destination record would need a human-reviewed access description and a status such as `confirmed suitable`, `known barrier`, or `unknown`, with supporting evidence. The yes/no guest answer also cannot represent the type or degree of mobility need; if testing shows that matters, ask a short follow-up rather than guessing.

## Automatic persona derivation

Use this deterministic precedence for the demographic persona. “Minor” means children or teenagers. Count the age bands with at least one person.

1. **Mixed-age family group:** adults, at least one minor, and seniors are all present (three generations).
2. **Grandparents with grandchildren:** at least one minor and one senior are present, but adults are not present.
3. **Family with young children:** at least one child aged 0–12 is present and no senior is present. This remains the closest current persona if teenagers are also present.
4. **Family with teenagers:** at least one teenager is present, no child aged 0–12 is present, and no senior is present.
5. **Active retired couple:** adults and seniors are present, with no minors. This is only the closest existing profile; it does not establish that the adults are retired or active.
6. **Mixed-age family group:** fallback for compositions not covered above, including adults-only and seniors-only groups. This fallback is a broad proxy, not a precise persona match.

The derived persona supplies the existing non-age weights and tag preferences. Composition supplies the group age-fit calculation. Activity interests such as aviation, hiking, or beach focus cannot be inferred from age counts. If those interests remain important in Version 2, retain a separate existing activity/profile selection and use its existing tag preferences; do not infer an interest from composition.

## Worked examples

The examples show the derived demographic persona and the exact suitability calculation. Destination scores are not shown; full ranking also needs each destination’s existing estimates for drive time, duration, weather, season, and tags. No example assumes a destination or adds destination data.

### 1. Two adults + two children

Assume both children are under 13. Derive **Family with young children**. For every destination:

```text
party_suitability = (2 × adult_score + 2 × children_score) / 4
                  = (adult_score + children_score) / 2
```

The children and adult suitability estimates each account for half of this group-fit average. Under-6 and ages 6–12 children use the same existing `children_score`.

### 2. Two adults + three teenagers

Derive **Family with teenagers**. For every destination:

```text
party_suitability = (2 × adult_score + 3 × teen_score) / 5
```

Teen suitability accounts for three fifths of the group-fit average and adult suitability for two fifths. The persona’s existing non-age preferences remain in use.

### 3. Four adults + two seniors

Derive **Active retired couple** as the closest available persona, with a visible caveat that this is a six-person adult/senior group, not necessarily a retired couple. For every destination:

```text
party_suitability = (4 × adult_score + 2 × senior_score) / 6
                  = (2 × adult_score + senior_score) / 3
```

Adult suitability accounts for two thirds of the group-fit average and senior suitability for one third. The derivation must not claim retirement or activity from age alone.

### 4. Three-generation family group

Example composition: two adults, one teenager, two children aged 0–12, and one senior. Derive **Mixed-age family group**. For every destination:

```text
party_suitability =
  (2 × adult_score + 1 × teen_score + 2 × children_score + 1 × senior_score) / 6
```

Adults and children each account for two sixths of the group-fit average; teenagers and seniors each account for one sixth. All represented generations affect suitability in proportion to group size.

## Reduced-mobility handling

1. Ask whether anyone has reduced mobility that should shape the choice.
2. If no, run normal ranking.
3. If yes, require reviewed access information for each candidate. Exclude destinations with a known barrier to the stated need from the accessible recommendation set.
4. Keep unknown access in a separate “access not confirmed” group with a clear explanation. Do not mix it into accessible recommendations as though it were verified.
5. Do not use low energy, senior suitability, or a destination tag as evidence of step-free access, seating, surface quality, distances, or accessible toilets.

This handling is a suitability gate, not a new numeric scoring system. It depends on destination access evidence that does not currently exist in the metadata file; until it is collected and reviewed, a “yes” answer can only produce an honest uncertainty notice, not verified mobility-aware recommendations.

## Version boundary

Version 2 is a design only. Version 1 remains unchanged. Implementing this design would require changes to the recommendation engine and additional reviewed access data, but neither is made by this document.
