# Version 1 vs. Version 2 recommendation comparison

`data/demo-groups.csv` contains 20 synthetic group examples and their automatically derived personas. V1 uses the closest current persona as a group-composition proxy and ranks all existing destinations with the unchanged current engine; the CSV contains no drive-limit or duration answers, so no questionnaire filters are applied here. V2 uses the same candidate destinations and non-age persona factors, but replaces the persona’s separate age terms with the count-weighted group suitability described in `docs/group-composition-v2.md`.

Names are shown in rank order; raw scores are omitted. The V1 demographic proxy is assigned by closest available profile: children only → Family with young children; teenagers only → Family with teenagers; minors plus seniors and no adults → Grandparents with grandchildren; other minors-plus-seniors or mixed child/teen groups → Mixed-age family group; seniors without minors → Active retired couple; adults-only or unclassified compositions → Mixed-age family group. V2 personas follow the precedence in `docs/group-composition-v2.md`. The 20 group rows are synthetic examples, not real guest records. No web research or destination data was used or changed. V2 mobility filtering cannot be completed: destination records do not contain reviewed access status. For groups marked `yes`, the shown V2 order is composition-only and must not be presented as mobility-screened.

## G01: Grandparents with two grandchildren

**Group:** 0 adults, 0 teenagers, 2 children, 2 seniors. **Reduced mobility:** No. **Derived persona:** V1 — Grandparents with grandchildren; V2 — Grandparents with grandchildren.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Playa la Malagueta; 3. Mercado de Atarazanas; 4. Marbella Old Town; 5. Selwo Aventura.

**V2 composition-adjusted top five:** 1. Palmeral de Las Sorpresas; 2. Playa la Malagueta; 3. Mercado de Atarazanas; 4. Marbella Old Town; 5. Selwo Aventura.

**Where V1 is weaker:** No visible top-five change occurs in this run. V1 still hides the actual cohort proportions, but that difference does not change these five results here.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of children and seniors and reduces that of teenagers and adults, based on group counts rather than the persona’s preset age weights. The derived persona remains **Grandparents with grandchildren**; changes come from replacing the persona’s age split with actual headcounts. This run shows no top-five membership or order change.

## G02: Two parents with three teenagers

**Group:** 2 adults, 3 teenagers, 0 children, 0 seniors. **Reduced mobility:** No. **Derived persona:** V1 — Family with teenagers; V2 — Family with teenagers.

**V1 top five:** 1. Selwo Aventura; 2. Olvera Castle; 3. Aracena; 4. Alcalá del Júcar; 5. Playa la Malagueta.

**V2 composition-adjusted top five:** 1. Selwo Aventura; 2. Olvera Castle; 3. Aracena; 4. Alcalá del Júcar; 5. Playa la Malagueta.

**Where V1 is weaker:** No visible top-five change occurs in this run. V1 still hides the actual cohort proportions, but that difference does not change these five results here.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of adults and reduces that of teenagers, based on group counts rather than the persona’s preset age weights. The derived persona remains **Family with teenagers**; changes come from replacing the persona’s age split with actual headcounts. This run shows no top-five membership or order change.

## G03: Couple aged 70+

**Group:** 0 adults, 0 teenagers, 0 children, 2 seniors. **Reduced mobility:** No. **Derived persona:** V1 — Active retired couple; V2 — Mixed-age family group.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Mercado de Atarazanas; 3. Aracena; 4. Olvera Castle; 5. Selwo Aventura.

**V2 composition-adjusted top five:** 1. Palmeral de Las Sorpresas; 2. Mercado de Atarazanas; 3. Selwo Aventura; 4. Aracena; 5. Playa la Malagueta.

**Where V1 is weaker:** No visible top-five change occurs in this run. V1 still hides the actual cohort proportions, but that difference does not change these five results here.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of seniors and reduces that of children, teenagers, and adults, based on group counts rather than the persona’s preset age weights. Persona also changes from **Active retired couple** in V1 to **Mixed-age family group** in V2, affecting the existing non-age preferences. New entries in the V2 top five: Playa la Malagueta.

## G04: Three-generation family

**Group:** 2 adults, 1 teenager, 2 children, 1 senior. **Reduced mobility:** Yes. **Derived persona:** V1 — Mixed-age family group; V2 — Mixed-age family group.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Selwo Aventura; 3. Playa la Malagueta; 4. Aracena; 5. Mercado de Atarazanas.

**V2 composition-adjusted top five:** 1. Palmeral de Las Sorpresas; 2. Selwo Aventura; 3. Playa la Malagueta; 4. Aracena; 5. Mercado de Atarazanas.

**Where V1 is weaker:** V1 has no reduced-mobility input. V2 would need access evidence to screen this group, but current records do not support that screen; the displayed V2 list is not accessibility-confirmed.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of children and adults and reduces that of teenagers and seniors, based on group counts rather than the persona’s preset age weights. The derived persona remains **Mixed-age family group**; changes come from replacing the persona’s age split with actual headcounts. This run shows no top-five membership or order change. Reduced mobility is yes: actual V2 mobility-aware recommendations cannot be confirmed from current data, so this is only a composition-adjusted list.

## G05: Young active couple

**Group:** 2 adults, 0 teenagers, 0 children, 0 seniors. **Reduced mobility:** No. **Derived persona:** V1 — Mixed-age family group; V2 — Mixed-age family group.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Selwo Aventura; 3. Playa la Malagueta; 4. Aracena; 5. Mercado de Atarazanas.

**V2 composition-adjusted top five:** 1. Mercado de Atarazanas; 2. Olvera Castle; 3. Selwo Aventura; 4. Palmeral de Las Sorpresas; 5. Aracena.

**Where V1 is weaker:** No visible top-five change occurs in this run. V1 still hides the actual cohort proportions, but that difference does not change these five results here.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of adults and reduces that of children, teenagers, and seniors, based on group counts rather than the persona’s preset age weights. The derived persona remains **Mixed-age family group**; changes come from replacing the persona’s age split with actual headcounts. New entries in the V2 top five: Olvera Castle.

## G06: Mixed-age family of nine

**Group:** 4 adults, 2 teenagers, 2 children, 1 senior. **Reduced mobility:** Yes. **Derived persona:** V1 — Mixed-age family group; V2 — Mixed-age family group.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Selwo Aventura; 3. Playa la Malagueta; 4. Aracena; 5. Mercado de Atarazanas.

**V2 composition-adjusted top five:** 1. Selwo Aventura; 2. Palmeral de Las Sorpresas; 3. Playa la Malagueta; 4. Olvera Castle; 5. Aracena.

**Where V1 is weaker:** V1 has no reduced-mobility input. V2 would need access evidence to screen this group, but current records do not support that screen; the displayed V2 list is not accessibility-confirmed.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of teenagers and adults and reduces that of children and seniors, based on group counts rather than the persona’s preset age weights. The derived persona remains **Mixed-age family group**; changes come from replacing the persona’s age split with actual headcounts. New entries in the V2 top five: Olvera Castle. Reduced mobility is yes: actual V2 mobility-aware recommendations cannot be confirmed from current data, so this is only a composition-adjusted list.

## G07: Single parent with two children

**Group:** 1 adult, 0 teenagers, 2 children, 0 seniors. **Reduced mobility:** No. **Derived persona:** V1 — Family with young children; V2 — Family with young children.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Playa la Malagueta; 3. Mercado de Atarazanas; 4. Marbella Old Town; 5. Frigiliana.

**V2 composition-adjusted top five:** 1. Palmeral de Las Sorpresas; 2. Playa la Malagueta; 3. Mercado de Atarazanas; 4. Marbella Old Town; 5. Frigiliana.

**Where V1 is weaker:** No visible top-five change occurs in this run. V1 still hides the actual cohort proportions, but that difference does not change these five results here.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of adults and reduces that of children, based on group counts rather than the persona’s preset age weights. The derived persona remains **Family with young children**; changes come from replacing the persona’s age split with actual headcounts. This run shows no top-five membership or order change.

## G08: Two adults with two school-age children

**Group:** 2 adults, 0 teenagers, 2 children, 0 seniors. **Reduced mobility:** No. **Derived persona:** V1 — Family with young children; V2 — Family with young children.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Playa la Malagueta; 3. Mercado de Atarazanas; 4. Marbella Old Town; 5. Frigiliana.

**V2 composition-adjusted top five:** 1. Palmeral de Las Sorpresas; 2. Mercado de Atarazanas; 3. Playa la Malagueta; 4. Marbella Old Town; 5. Frigiliana.

**Where V1 is weaker:** No visible top-five change occurs in this run. V1 still hides the actual cohort proportions, but that difference does not change these five results here.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of adults and reduces that of children, based on group counts rather than the persona’s preset age weights. The derived persona remains **Family with young children**; changes come from replacing the persona’s age split with actual headcounts. This run shows no top-five membership or order change.

## G09: Two adults with three teenagers

**Group:** 2 adults, 3 teenagers, 0 children, 0 seniors. **Reduced mobility:** No. **Derived persona:** V1 — Family with teenagers; V2 — Family with teenagers.

**V1 top five:** 1. Selwo Aventura; 2. Olvera Castle; 3. Aracena; 4. Alcalá del Júcar; 5. Playa la Malagueta.

**V2 composition-adjusted top five:** 1. Selwo Aventura; 2. Olvera Castle; 3. Aracena; 4. Alcalá del Júcar; 5. Playa la Malagueta.

**Where V1 is weaker:** No visible top-five change occurs in this run. V1 still hides the actual cohort proportions, but that difference does not change these five results here.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of adults and reduces that of teenagers, based on group counts rather than the persona’s preset age weights. The derived persona remains **Family with teenagers**; changes come from replacing the persona’s age split with actual headcounts. This run shows no top-five membership or order change.

## G10: Blended family with children and a teenager

**Group:** 2 adults, 1 teenager, 2 children, 0 seniors. **Reduced mobility:** No. **Derived persona:** V1 — Mixed-age family group; V2 — Family with young children.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Selwo Aventura; 3. Playa la Malagueta; 4. Aracena; 5. Mercado de Atarazanas.

**V2 composition-adjusted top five:** 1. Palmeral de Las Sorpresas; 2. Mercado de Atarazanas; 3. Playa la Malagueta; 4. Marbella Old Town; 5. Frigiliana.

**Where V1 is weaker:** No visible top-five change occurs in this run. V1 still hides the actual cohort proportions, but that difference does not change these five results here.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of teenagers and adults and reduces that of children, based on group counts rather than the persona’s preset age weights. Persona also changes from **Mixed-age family group** in V1 to **Family with young children** in V2, affecting the existing non-age preferences. New entries in the V2 top five: Marbella Old Town, Frigiliana.

## G11: Two adults with three young children

**Group:** 2 adults, 0 teenagers, 3 children, 0 seniors. **Reduced mobility:** No. **Derived persona:** V1 — Family with young children; V2 — Family with young children.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Playa la Malagueta; 3. Mercado de Atarazanas; 4. Marbella Old Town; 5. Frigiliana.

**V2 composition-adjusted top five:** 1. Palmeral de Las Sorpresas; 2. Mercado de Atarazanas; 3. Playa la Malagueta; 4. Marbella Old Town; 5. Frigiliana.

**Where V1 is weaker:** No visible top-five change occurs in this run. V1 still hides the actual cohort proportions, but that difference does not change these five results here.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of adults and reduces that of children, based on group counts rather than the persona’s preset age weights. The derived persona remains **Family with young children**; changes come from replacing the persona’s age split with actual headcounts. This run shows no top-five membership or order change.

## G12: Two adults, a teenager, and a senior

**Group:** 2 adults, 1 teenager, 0 children, 1 senior. **Reduced mobility:** No. **Derived persona:** V1 — Mixed-age family group; V2 — Mixed-age family group.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Selwo Aventura; 3. Playa la Malagueta; 4. Aracena; 5. Mercado de Atarazanas.

**V2 composition-adjusted top five:** 1. Selwo Aventura; 2. Palmeral de Las Sorpresas; 3. Mercado de Atarazanas; 4. Olvera Castle; 5. Aracena.

**Where V1 is weaker:** No visible top-five change occurs in this run. V1 still hides the actual cohort proportions, but that difference does not change these five results here.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of teenagers and adults and reduces that of children and seniors, based on group counts rather than the persona’s preset age weights. The derived persona remains **Mixed-age family group**; changes come from replacing the persona’s age split with actual headcounts. New entries in the V2 top five: Olvera Castle.

## G13: Four adults and two seniors

**Group:** 4 adults, 0 teenagers, 0 children, 2 seniors. **Reduced mobility:** Yes. **Derived persona:** V1 — Active retired couple; V2 — Active retired couple.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Mercado de Atarazanas; 3. Aracena; 4. Olvera Castle; 5. Selwo Aventura.

**V2 composition-adjusted top five:** 1. Mercado de Atarazanas; 2. Palmeral de Las Sorpresas; 3. Aracena; 4. Olvera Castle; 5. Selwo Aventura.

**Where V1 is weaker:** V1 has no reduced-mobility input. V2 would need access evidence to screen this group, but current records do not support that screen; the displayed V2 list is not accessibility-confirmed.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of adults and reduces that of seniors, based on group counts rather than the persona’s preset age weights. The derived persona remains **Active retired couple**; changes come from replacing the persona’s age split with actual headcounts. This run shows no top-five membership or order change. Reduced mobility is yes: actual V2 mobility-aware recommendations cannot be confirmed from current data, so this is only a composition-adjusted list.

## G14: One adult, one senior, and two children

**Group:** 1 adult, 0 teenagers, 2 children, 1 senior. **Reduced mobility:** Yes. **Derived persona:** V1 — Mixed-age family group; V2 — Mixed-age family group.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Selwo Aventura; 3. Playa la Malagueta; 4. Aracena; 5. Mercado de Atarazanas.

**V2 composition-adjusted top five:** 1. Palmeral de Las Sorpresas; 2. Playa la Malagueta; 3. Selwo Aventura; 4. Mercado de Atarazanas; 5. Aracena.

**Where V1 is weaker:** V1 has no reduced-mobility input. V2 would need access evidence to screen this group, but current records do not support that screen; the displayed V2 list is not accessibility-confirmed.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of children and adults and reduces that of teenagers and seniors, based on group counts rather than the persona’s preset age weights. The derived persona remains **Mixed-age family group**; changes come from replacing the persona’s age split with actual headcounts. This run shows no top-five membership or order change. Reduced mobility is yes: actual V2 mobility-aware recommendations cannot be confirmed from current data, so this is only a composition-adjusted list.

## G15: One adult with three seniors

**Group:** 1 adult, 0 teenagers, 0 children, 3 seniors. **Reduced mobility:** Yes. **Derived persona:** V1 — Active retired couple; V2 — Active retired couple.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Mercado de Atarazanas; 3. Aracena; 4. Olvera Castle; 5. Selwo Aventura.

**V2 composition-adjusted top five:** 1. Palmeral de Las Sorpresas; 2. Mercado de Atarazanas; 3. Aracena; 4. Selwo Aventura; 5. Alcalá del Júcar.

**Where V1 is weaker:** V1 has no reduced-mobility input. V2 would need access evidence to screen this group, but current records do not support that screen; the displayed V2 list is not accessibility-confirmed.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of seniors and reduces that of adults, based on group counts rather than the persona’s preset age weights. The derived persona remains **Active retired couple**; changes come from replacing the persona’s age split with actual headcounts. New entries in the V2 top five: Alcalá del Júcar. Reduced mobility is yes: actual V2 mobility-aware recommendations cannot be confirmed from current data, so this is only a composition-adjusted list.

## G16: Three adults, two teenagers, and one child

**Group:** 3 adults, 2 teenagers, 1 child, 0 seniors. **Reduced mobility:** No. **Derived persona:** V1 — Mixed-age family group; V2 — Family with young children.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Selwo Aventura; 3. Playa la Malagueta; 4. Aracena; 5. Mercado de Atarazanas.

**V2 composition-adjusted top five:** 1. Mercado de Atarazanas; 2. Palmeral de Las Sorpresas; 3. Playa la Malagueta; 4. Marbella Old Town; 5. La Vall d'Uixó.

**Where V1 is weaker:** No visible top-five change occurs in this run. V1 still hides the actual cohort proportions, but that difference does not change these five results here.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of teenagers and adults and reduces that of children, based on group counts rather than the persona’s preset age weights. Persona also changes from **Mixed-age family group** in V1 to **Family with young children** in V2, affecting the existing non-age preferences. New entries in the V2 top five: Marbella Old Town, La Vall d'Uixó.

## G17: Grandparents with a teenager and a child

**Group:** 0 adults, 1 teenager, 1 child, 2 seniors. **Reduced mobility:** No. **Derived persona:** V1 — Grandparents with grandchildren; V2 — Grandparents with grandchildren.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Playa la Malagueta; 3. Mercado de Atarazanas; 4. Marbella Old Town; 5. Selwo Aventura.

**V2 composition-adjusted top five:** 1. Palmeral de Las Sorpresas; 2. Playa la Malagueta; 3. Mercado de Atarazanas; 4. Marbella Old Town; 5. Selwo Aventura.

**Where V1 is weaker:** No visible top-five change occurs in this run. V1 still hides the actual cohort proportions, but that difference does not change these five results here.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of teenagers and seniors and reduces that of children and adults, based on group counts rather than the persona’s preset age weights. The derived persona remains **Grandparents with grandchildren**; changes come from replacing the persona’s age split with actual headcounts. This run shows no top-five membership or order change.

## G18: Two adults with four teenagers

**Group:** 2 adults, 4 teenagers, 0 children, 0 seniors. **Reduced mobility:** No. **Derived persona:** V1 — Family with teenagers; V2 — Family with teenagers.

**V1 top five:** 1. Selwo Aventura; 2. Olvera Castle; 3. Aracena; 4. Alcalá del Júcar; 5. Playa la Malagueta.

**V2 composition-adjusted top five:** 1. Selwo Aventura; 2. Olvera Castle; 3. Aracena; 4. Alcalá del Júcar; 5. Playa la Malagueta.

**Where V1 is weaker:** No visible top-five change occurs in this run. V1 still hides the actual cohort proportions, but that difference does not change these five results here.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of adults and reduces that of teenagers, based on group counts rather than the persona’s preset age weights. The derived persona remains **Family with teenagers**; changes come from replacing the persona’s age split with actual headcounts. This run shows no top-five membership or order change.

## G19: Solo adult traveller

**Group:** 1 adult, 0 teenagers, 0 children, 0 seniors. **Reduced mobility:** No. **Derived persona:** V1 — Mixed-age family group; V2 — Mixed-age family group.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Selwo Aventura; 3. Playa la Malagueta; 4. Aracena; 5. Mercado de Atarazanas.

**V2 composition-adjusted top five:** 1. Mercado de Atarazanas; 2. Olvera Castle; 3. Selwo Aventura; 4. Palmeral de Las Sorpresas; 5. Aracena.

**Where V1 is weaker:** No visible top-five change occurs in this run. V1 still hides the actual cohort proportions, but that difference does not change these five results here.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of adults and reduces that of children, teenagers, and seniors, based on group counts rather than the persona’s preset age weights. The derived persona remains **Mixed-age family group**; changes come from replacing the persona’s age split with actual headcounts. New entries in the V2 top five: Olvera Castle.

## G20: Three adults and two seniors

**Group:** 3 adults, 0 teenagers, 0 children, 2 seniors. **Reduced mobility:** No. **Derived persona:** V1 — Active retired couple; V2 — Active retired couple.

**V1 top five:** 1. Palmeral de Las Sorpresas; 2. Mercado de Atarazanas; 3. Aracena; 4. Olvera Castle; 5. Selwo Aventura.

**V2 composition-adjusted top five:** 1. Mercado de Atarazanas; 2. Palmeral de Las Sorpresas; 3. Aracena; 4. Olvera Castle; 5. Selwo Aventura.

**Where V1 is weaker:** No visible top-five change occurs in this run. V1 still hides the actual cohort proportions, but that difference does not change these five results here.

**How V2 changes the ranking:** V2 increases the relative age-fit influence of adults and reduces that of seniors, based on group counts rather than the persona’s preset age weights. The derived persona remains **Active retired couple**; changes come from replacing the persona’s age split with actual headcounts. This run shows no top-five membership or order change.

## Where V1 is clearly weaker

- **Different counts within the same profile:** V1 gives two adults and three teenagers the same fixed age-factor proportions as any other Family with teenagers group. V2 lets actual headcounts change how much each age suitability estimate contributes.
- **Three-generation and mixed-age groups:** V1 compresses the party into one broad profile. V2 reflects the actual proportions of children, teenagers, adults, and seniors in the group-fit calculation.
- **Senior-only or adult-only parties:** V1 has no exact senior-only or generic adult-only persona and must use a proxy. V2 still derives a closest existing persona for non-age factors, but the count-weighted fit represents the actual attendees. The proxy limitation remains visible.
- **Reduced mobility:** V1 ignores the answer. V2 can handle it only after destination access status is gathered and reviewed; current files have no such field, so no valid mobility-filtered ranking is available yet.
- **Activity interests:** Neither group counts nor V2 composition infer a preference for hiking, aviation, or beach activities. Those interests still require a separate supported profile or input; the demo does not invent one.

## Interpretation limits

The V2 lists are design simulations, not a change to the live engine or evidence that recommendations are safer, more accessible, or more satisfying. Existing age suitability and route estimates remain editorial estimates, tag classifications may be missing, and confidence is not included in the current scoring formula. Review the V2 formula and mobility data requirements before implementation.
