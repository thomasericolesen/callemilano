# V2 vs. V3 recommendation analysis

## V3 model used for this run

This is an analytical prototype using the current `data/destination-metadata.csv`, `data/destination-classification.csv`, `data/personas.csv`, `data/demo-groups.csv`, `docs/recommendation-engine-spec.md`, `docs/group-composition-v2.md`, and `docs/enriched-place-metadata.csv`. It does not change the existing recommendation engine or destination records. V2 is recalculated from the current files using the group-weighted age calculation in the V2 design; V3 starts from that V2 score.

V3 adds a confidence-weighted evidence component:

```text
V3 = 0.75 × V2 + 0.25 × enriched_metadata_fit
```

`enriched_metadata_fit` is a 0–100 value built from:

- Group-specific suitability evidence (65% for groups without a reduced-mobility flag; 50% when reduced mobility is flagged). The destination’s stated ratings for represented age groups are averaged by group member count. `low`, `medium`, and `high` map to 1, 3, and 5 on the existing 0–5 fit scale.
- Practical facilities (35% without a reduced-mobility flag; 30% with one), using only confidence-supported toilet, food, and shade evidence. Confirmed availability scores 5 and confirmed absence scores 0.
- Accessibility (20%, only for groups that flagged reduced mobility). Limited access receives a lower fit than explicitly supported access. Unknown access is not treated as accessible.

For each field, calculate `adjusted_fit = confidence × observed_fit + (1 − confidence) × 2.5`, where confidence is `confidence_score_0_100 / 100`. Unknown/unscored fields use 2.5. Average the adjusted represented-cohort ratings by guest counts for group suitability; average adjusted verified facility values for practical support. For reduced-mobility groups, accessibility is confidence-adjusted separately and included as its own factor. Convert each 0–5 factor to 0–100 before applying the stated factor weights. Unknown or unscored values therefore contribute neutral fit rather than a penalty. The inputs are prototype editorial estimates, not safety determinations. The existing activity-tag component remains in V2; the enriched tag descriptions are not double-counted. Duration and weather are also not scored twice because V2 already uses those dimensions.

**Important limitation:** the enriched metadata is sparse and has not received human approval. Only sourced, scored values affect the V3 adjustment; an empty source field or zero confidence contributes neutral fit. Reduced-mobility groups still cannot be promised an accessibility-screened result: unknown access must be surfaced as unconfirmed.

## Results by group

The lists below are ordered from rank 1 to rank 5. “Changes” shows V3 rank moves for destinations retained in the top five, plus entries/exits.

| Group | V2 top 5 | V3 top 5 | Changes from V2 |
|---|---|---|---|
| G01 — Grandparents with two grandchildren | Palmeral de Las Sorpresas; Playa la Malagueta; Ronda; La Vall d'Uixó; Mercado de Atarazanas | Palmeral de Las Sorpresas; La Vall d'Uixó; Playa la Malagueta; Ronda; Mercado de Atarazanas | La Vall d'Uixó 4→2; Playa la Malagueta 2→3; Ronda 3→4 |
| G02 — Two parents with three teenagers | Olvera Castle; Aracena; Alcalá del Júcar; Los Caños de Meca; Duna de Bolonia | Aracena; Olvera Castle; La Vall d'Uixó; Alcalá del Júcar; Los Caños de Meca | Aracena 2→1; Olvera Castle 1→2; Alcalá del Júcar 3→4; Los Caños de Meca 4→5; +La Vall d'Uixó; −Duna de Bolonia |
| G03 — Couple aged 70+ | Palmeral de Las Sorpresas; Mercado de Atarazanas; Aracena; La Vall d'Uixó; Alcalá del Júcar | Palmeral de Las Sorpresas; La Vall d'Uixó; Mercado de Atarazanas; Alcalá del Júcar; Aracena | La Vall d'Uixó 4→2; Mercado de Atarazanas 2→3; Alcalá del Júcar 5→4; Aracena 3→5 |
| G04 — Three-generation family | Palmeral de Las Sorpresas; Aracena; Playa la Malagueta; Olvera Castle; Ronda | Palmeral de Las Sorpresas; La Vall d'Uixó; Aracena; Playa la Malagueta; Olvera Castle | Aracena 2→3; Playa la Malagueta 3→4; Olvera Castle 4→5; +La Vall d'Uixó; −Ronda |
| G05 — Young active couple | Olvera Castle; Mercado de Atarazanas; Aracena; La Vall d'Uixó; Palmeral de Las Sorpresas | Aracena; Olvera Castle; La Vall d'Uixó; Alcázar de Segovia; Mercado de Atarazanas | Aracena 3→1; Olvera Castle 1→2; La Vall d'Uixó 4→3; +Alcázar de Segovia; Mercado de Atarazanas 2→5; −Palmeral de Las Sorpresas |
| G06 — Mixed-age family of nine | Olvera Castle; Aracena; Palmeral de Las Sorpresas; La Vall d'Uixó; Playa la Malagueta | Aracena; La Vall d'Uixó; Olvera Castle; Playa la Malagueta; Palmeral de Las Sorpresas | Aracena 2→1; La Vall d'Uixó 4→2; Olvera Castle 1→3; Playa la Malagueta 5→4; Palmeral de Las Sorpresas 3→5 |
| G07 — Single parent with two children | Palmeral de Las Sorpresas; Frigiliana; La Vall d'Uixó; Ronda; Aracena | La Vall d'Uixó; Palmeral de Las Sorpresas; Frigiliana; Aracena; Ronda | La Vall d'Uixó 3→1; Palmeral de Las Sorpresas 1→2; Frigiliana 2→3; Aracena 5→4; Ronda 4→5 |
| G08 — Two adults with two school-age children | Frigiliana; Palmeral de Las Sorpresas; La Vall d'Uixó; Aracena; Ronda | La Vall d'Uixó; Aracena; Frigiliana; Palmeral de Las Sorpresas; Ronda | La Vall d'Uixó 3→1; Aracena 4→2; Frigiliana 1→3; Palmeral de Las Sorpresas 2→4 |
| G09 — Two adults with three teenagers | Olvera Castle; Aracena; Alcalá del Júcar; Los Caños de Meca; Duna de Bolonia | Aracena; Olvera Castle; La Vall d'Uixó; Alcalá del Júcar; Los Caños de Meca | Aracena 2→1; Olvera Castle 1→2; Alcalá del Júcar 3→4; Los Caños de Meca 4→5; +La Vall d'Uixó; −Duna de Bolonia |
| G10 — Blended family with children and a teenager | Frigiliana; La Vall d'Uixó; Aracena; Ronda; Palmeral de Las Sorpresas | La Vall d'Uixó; Aracena; Frigiliana; Ronda; Palmeral de Las Sorpresas | La Vall d'Uixó 2→1; Aracena 3→2; Frigiliana 1→3 |
| G11 — Two adults with three young children | Frigiliana; Palmeral de Las Sorpresas; La Vall d'Uixó; Aracena; Ronda | La Vall d'Uixó; Frigiliana; Palmeral de Las Sorpresas; Aracena; Ronda | La Vall d'Uixó 3→1; Frigiliana 1→2; Palmeral de Las Sorpresas 2→3 |
| G12 — Two adults, a teenager, and a senior | Olvera Castle; Aracena; La Vall d'Uixó; Palmeral de Las Sorpresas; Alcalá del Júcar | Aracena; La Vall d'Uixó; Olvera Castle; Palmeral de Las Sorpresas; Alcalá del Júcar | Aracena 2→1; La Vall d'Uixó 3→2; Olvera Castle 1→3 |
| G13 — Four adults and two seniors | Mercado de Atarazanas; Aracena; Palmeral de Las Sorpresas; La Vall d'Uixó; Olvera Castle | La Vall d'Uixó; Aracena; Mercado de Atarazanas; Palmeral de Las Sorpresas; Olvera Castle | La Vall d'Uixó 4→1; Mercado de Atarazanas 1→3; Palmeral de Las Sorpresas 3→4 |
| G14 — One adult, one senior, and two children | Palmeral de Las Sorpresas; Playa la Malagueta; Aracena; Ronda; La Vall d'Uixó | Palmeral de Las Sorpresas; Playa la Malagueta; La Vall d'Uixó; Aracena; Ronda | La Vall d'Uixó 5→3; Aracena 3→4; Ronda 4→5 |
| G15 — One adult with three seniors | Palmeral de Las Sorpresas; Mercado de Atarazanas; Aracena; La Vall d'Uixó; Alcalá del Júcar | Palmeral de Las Sorpresas; La Vall d'Uixó; Mercado de Atarazanas; Aracena; Alcalá del Júcar | La Vall d'Uixó 4→2; Mercado de Atarazanas 2→3; Aracena 3→4 |
| G16 — Three adults, two teenagers, and one child | La Vall d'Uixó; Frigiliana; Aracena; Olvera Castle; Ronda | Aracena; La Vall d'Uixó; Frigiliana; Olvera Castle; Ronda | Aracena 3→1; La Vall d'Uixó 1→2; Frigiliana 2→3 |
| G17 — Grandparents with a teenager and a child | Palmeral de Las Sorpresas; La Vall d'Uixó; Ronda; Playa la Malagueta; Aracena | Palmeral de Las Sorpresas; La Vall d'Uixó; Ronda; Playa la Malagueta; Aracena | No change |
| G18 — Two adults with four teenagers | Olvera Castle; Aracena; Alcalá del Júcar; Los Caños de Meca; Duna de Bolonia | Aracena; Olvera Castle; La Vall d'Uixó; Alcalá del Júcar; Los Caños de Meca | Aracena 2→1; Olvera Castle 1→2; Alcalá del Júcar 3→4; Los Caños de Meca 4→5; +La Vall d'Uixó; −Duna de Bolonia |
| G19 — Solo adult traveller | Olvera Castle; Mercado de Atarazanas; Aracena; La Vall d'Uixó; Palmeral de Las Sorpresas | Aracena; Olvera Castle; La Vall d'Uixó; Alcázar de Segovia; Mercado de Atarazanas | Aracena 3→1; Olvera Castle 1→2; La Vall d'Uixó 4→3; +Alcázar de Segovia; Mercado de Atarazanas 2→5; −Palmeral de Las Sorpresas |
| G20 — Three adults and two seniors | Mercado de Atarazanas; Palmeral de Las Sorpresas; Aracena; La Vall d'Uixó; Olvera Castle | La Vall d'Uixó; Aracena; Mercado de Atarazanas; Palmeral de Las Sorpresas; Olvera Castle | La Vall d'Uixó 4→1; Aracena 3→2; Mercado de Atarazanas 1→3; Palmeral de Las Sorpresas 2→4 |

## Similarity counts

“Identical” means the ordered ranks match exactly. Set overlap is listed separately because two lists can contain the same places in a different order.

| Comparison | Groups |
|---|---:|
| Identical top recommendation (top 1) | 7 of 20 |
| Identical ordered top 3 | 1 of 20 |
| Identical ordered top 5 | 1 of 20 |
| Same top 3 membership, any order | 6 of 20 |
| Same top 5 membership, any order | 14 of 20 |

The 14/20 top-five set overlap and changes concentrated around a small number of destinations show that the added metadata alters ordering more often than it uncovers a broader set of group-specific options. Top-one recommendations differ for 13 groups, but several apparent changes reflect one destination’s richer evidence rather than robust preference matching.

## Does enriched metadata improve discrimination?

**Somewhat, but the present result is not strong evidence of a reliable improvement.** V3 changes the ordered top five for 19 of 20 groups and changes the top recommendation for 14 groups. Yet 14 groups still receive the same five destinations as V2, just reordered, and the shifts repeatedly favor La Vall d'Uixó and Aracena because those records have more populated, higher-confidence entries in the current enrichment file. Many other destinations have unknown fields and therefore receive neutral values. This is evidence of data-coverage imbalance as much as it is evidence of group discrimination.

The results should be treated as a calculation check, not guest-ready recommendations. The current enriched set needs consistent, source-backed accessibility and facility coverage across the candidate destinations; family ratings need human review; reduced-mobility access remains unknown for most places; and several imported names still have unresolved identities. Re-running with balanced, verified coverage is necessary before concluding that V3 meaningfully distinguishes different groups.
