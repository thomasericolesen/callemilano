# Recommendation discrimination analysis

## Counts from the comparison lists

Counts below compare each group’s ordered V1 list against its ordered V2 list in `docs/v1-vs-v2-comparison.md`. “Identical” means the same destinations in the same positions. The list contents were counted directly; some per-group commentary in the comparison document conflicts with the lists.

| Comparison within each of the 20 groups | Groups | Share |
|---|---:|---:|
| Identical ordered top five | 7 | 35% |
| Identical ordered top three | 8 | 40% |
| Same top recommendation | 13 | 65% |

If order is ignored, 12 groups have the same set of five destinations and 14 groups have the same set of three. So V2 changes some ordering more often than it changes which destinations appear at the top.

### Similarity across groups

- V1 produces only **5 distinct ordered top-five lists** across the 20 groups. Its most common list appears for 8 groups.
- **Palmeral de Las Sorpresas** is V1’s top recommendation for 17 of 20 groups; Selwo Aventura leads the other 3.
- V2 produces **13 distinct ordered top-five lists**. Its top recommendation is Palmeral de Las Sorpresas for 10 groups, Selwo Aventura for 5, and Mercado de Atarazanas for 5.

The V2 composition calculation therefore adds measurable differentiation, but many group results still overlap.

## Why results remain similar

### The candidate set is small and repeatedly favors nearby places

The comparison ranks the same 30 destinations for every group. The existing drive estimates give several Malaga-area destinations short estimated journeys from Casa de la Familia, while many other entries are several hours away. Repeated candidates such as Palmeral de Las Sorpresas, Playa la Malagueta, Mercado de Atarazanas, and Selwo Aventura can score well across many profiles because proximity and broad suitability apply to many groups.

Drive estimates are rough editorial ranges, not route-checked times. The model turns those ranges into a small number of drive bands, so several nearby places can receive the same drive factor.

### Persona mapping compresses different groups into a few profiles

V1 maps the 20 synthetic groups to five demographic personas: Mixed-age family group (8), Active retired couple (4), Family with teenagers (3), Family with young children (3), and Grandparents with grandchildren (2). Groups with different member counts can therefore use identical weights and tag preferences.

V2 uses the same small set of existing personas for non-age factors. Its group counts change the age-fit contribution, but they do not add a distinct interest profile or change drive, duration, weather, season, or tag preferences unless the derived persona changes.

### The suitability inputs are coarse and often similar

The 30 metadata rows use integer suitability values from 0 to 5. Teen suitability is 5 for 20 destinations, and adult suitability is 5 for 22. Children suitability is 2 for 18 destinations. These repeated values give many destinations similar audience-fit contributions and limit the ability of group-size changes to separate them.

### Tags do not distinguish every destination or every group

The metadata contains no tags; tags are in the separate classification file. Of the 30 metadata destinations, 25 have a classification row. Destinations without a classification or tags receive a neutral tag fit under the current engine. That fallback removes a possible source of differentiation.

The tag component is also only 15% of the final score. It cannot always overcome common drive and suitability contributions. Group composition does not reveal a guest’s particular interest in aviation, hiking, beaches, food, or culture, so demographic matches do not necessarily become activity-specific matches.

### Other factors use broad categories

Duration has only half-day, full-day, and overnight values. Energy has only low, medium, and high. Weather dependence is low, medium, or high, and the existing metadata describes many destinations as weather-dependent. These broad estimates can help separate very different outings, but they cannot express finer differences among places in the same category.

### Mobility cannot currently differentiate recommendations

Five demo groups are marked as having reduced mobility, but the existing destination metadata has no mobility or accessibility fields. The V1 engine ignores the input; the V2 lists in the comparison are composition-only and were not mobility-screened. The two ranking lists therefore cannot show a verified mobility-related distinction.

## Missing destination attributes most likely to improve differentiation

This is an inventory of missing or under-specified information visible from the current files, not an engine redesign.

| Priority | Missing or under-specified destination attribute | Why it would distinguish these groups |
|---|---|---|
| Highest | **Verified accessibility detail:** step-free route, stairs, surface, distance and gradient, seating/rest points, and accessible toilets | The demo includes five reduced-mobility groups, but no destination access evidence can currently separate suitable options from unknown or unsuitable ones. A single low/medium/high energy label is not accessibility evidence. |
| Highest | **Specific activity and experience detail:** what visitors actually do or see, such as swimming, animal encounters, cave visits, a named trail, aviation-related activity, or food tasting | Broad collection tags cannot reliably distinguish an aviation outing from a viewpoint or a hiking route from a town visit. Specific experience information would make group interests more discriminating. |
| High | **Age-band-specific evidence**, especially separate suitability for children under 6 and ages 6–12, plus evidence behind teen and senior suitability | The current `children_score` combines children under 6 and ages 6–12, and all audience scores are coarse estimates. More precise evidence could distinguish groups with different child ages and reduce reliance on proxy personas. |
| High | **Physical effort detail:** route length, elevation gain, stairs, standing time, and whether effort is optional | `energy_level` has only three broad values. More detail would distinguish a scenic stop from a demanding walk and help groups with young children, seniors, or mobility limitations. |
| High | **Weather and seasonal exposure:** indoor/outdoor coverage, shade, water exposure, seasonal closure or service changes | `weather_dependency` and `season` are broad editorial estimates. These details could distinguish a robust option from one that depends on heat, rain, wind, or seasonal operations. |
| Medium | **Visit logistics:** reliable duration, opening pattern, booking requirement, capacity, and current cost | These are missing from the recommendation metadata and can change whether a destination is practical for a particular group, particularly for a short visit or large party. |
| Medium | **Group practicality:** facilities and activity options suitable for different age groups visiting together | Current group suitability is an average of age scores. Information about whether a destination offers meaningful options to multiple generations could distinguish a balanced group experience from one that mainly serves one cohort. |

The most visible causes of similarity are therefore repeated proximity and coarse suitability estimates, broad persona assignment, and neutral tag fallbacks. Accessibility and specific experience information are the largest gaps for the demo groups’ varied needs.

## Counting note

The source comparison document contains narrative statements such as “no visible top-five change” that do not always match its displayed lists. For example, G03 and G05 have different V1 and V2 top-five lists. The counts above use the displayed destination names and their order, not those narrative statements. The comparison is a simulation over existing estimates, not a verified guest-outcome study.
