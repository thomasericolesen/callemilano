# Family assessment proposal, 2026-11-02

**Status: proposal for the owner to correct. Nothing here has been written into the records.** Owner decisions 2 and 6 of 2026-11-01 (`docs/approval-decisions-2026-11-01.md`): Claude drafts age groups and family scores for the 12 local beaches and 8 restaurants; the owner (editor-of-record) corrects them. After correction, the values go into `age_groups` and `family_score`, and `subjective_assessments_need_human_review` / `family_suitability_not_assessed` can be closed.

Scores use the schema values `low`, `medium`, `high` (and `unknown`). They are editorial suitability guidance, not safety advice. Columns: SC = `small_children` (0-6), C = `children` (7-12), YA = `young_adults`, S = `seniors`.

## How the proposal was made

The proposal uses only facts already in the records, with sources: municipal 2026 service charters and announcements, spain.info and andalucia.org beach data, venue websites, and the owner's own knowledge where it was recorded as a decision. Unsourced snapshot statements ("often recommended for children", Facebook replies) were removed on 2026-11-02 and were not used.

| Factor | Counts towards |
|---|---|
| Calm water (*aguas tranquilas*) | SC up |
| Moderate waves (*oleaje moderado*) | SC at most medium |
| Stones, gravel or cobbles instead of sand | SC and S down |
| Children's area, trampolines, lifeguards in season, toilets | SC and C up |
| Assisted bathing, adapted toilets, ramps or walkways, promenade | S up |
| Water sports, surf area, sports area, beach bars, nature or town nearby | C and YA up |
| Isolated beach, nudist sections, few services | SC down |

`age_groups` rule used in the proposal: list the audiences rated `high`. Where no audience is `high`, list the `medium` ones the place suits best (marked "judgment").

## Beaches

| Beach | SC | C | YA | S | Proposed `age_groups` | Main reasons (facts in the record) |
|---|---|---|---|---|---|---|
| Boliches-Gaviotas | high | high | medium | high | Small children, Children, Seniors | Calm water, children's area, trampolines, lifeguards, toilets; adapted bathing platform; promenade; windsurf and pedalos. |
| Cabopino-Artola | medium | medium | high | medium | Young adults | Golden sand but moderate waves; isolated, with nudism on parts of the beach; dunes and pine woods (nature). Assisted bathing in season; toilets not confirmed by a dated source. |
| Carvajal | medium | medium | medium | medium | Small children, Children (judgment) | Calm water, children's area, lifeguards, toilets, train stop; but spain.info lists gravel and cobbles (*bolos*) with the sand. Rocks still open. |
| Castillo-Ejido | medium | high | medium | medium | Children | Large white-sand beach by the Castillo Sohail; sports area; moragas; moderate waves; no children's area on the charter map; fenced dog beach. Assisted bathing and adapted showers. |
| El Bajondillo | medium | medium | medium | high | Seniors | Moderate waves; central Torremolinos; accessible walkways, staffed assisted bathing, accessible toilets, public lift; surf area. |
| Fuengirola centro | high | high | medium | high | Small children, Children, Seniors | Calm water, golden sand, children's area, trampolines, lifeguards and drone surveillance; assisted bathing; easy on foot. (Coordinates issue open.) |
| Fuente de la Salud | medium | medium | medium | medium | Children, Seniors (judgment) | Small (about 150 m), moderate waves, by the marina; lifeguard point, accessibility point, adapted toilets; play area not confirmed. |
| La Butibamba | low | medium | medium | low | Children, Young adults (judgment) | Stone beach (owner), narrow and busy; calm water; lifeguards in summer; no assisted bathing; no Blue Flag 2026; beach bars with live music nearby. |
| La Carihuela | medium | high | high | high | Children, Young adults, Seniors | Long beach, moderate waves; described by spain.info as equipped for the whole family; restaurants and fishing-village promenade; accessible walkways, assisted bathing, accessible toilets. |
| Los Álamos | medium | medium | medium | medium | Children, Young adults (judgment) | Wide golden-sand beach, moderate waves, semi-urban; accessible walkways and assisted bathing. Atmosphere ("younger, livelier") had no source; the owner may know it. |
| Playamar | medium | medium | medium | high | Seniors | Moderate waves; toilets; accessible walkways, staffed assisted bathing, accessible toilets. |
| Santa Ana | medium | medium | low | low | Small children, Children (judgment) | Small and narrow (about 500 x 15 m), moderate waves; children's area listed (undated); not named in Benalmádena's 2026 lifeguard or accessibility lists. |

## Restaurants

Confidence is lower here: only Los Marinos Paco states facilities for children on its own website. The other ratings are judgments from the type of venue.

| Restaurant | SC | C | YA | S | Proposed `age_groups` | Main reasons |
|---|---|---|---|---|---|---|
| Los Marinos Paco (Carvajal) | high | high | medium | medium | Small children, Children | Own website: children's menu and high chairs; family-run beach restaurant. Accessibility not confirmed. |
| Restaurante Santa Ana Denis (Santa Ana) | medium | high | medium | medium | Children | Own website calls the atmosphere ideal for families and groups (the venue's own wording); paella, espetos. |
| La Mar Salá (Los Boliches) | medium | medium | high | medium | Young adults | Beach bar open daily 12:00-00:00 with a sunbed lounge. |
| Chiringuito Los Moreno (La Butibamba) | medium | medium | high | medium | Young adults | Own Instagram: espetos, sunbeds, live music. |
| Morrofino (Playamar) | medium | medium | medium | medium | Young adults, Seniors (judgment) | Restaurant on the promenade with online booking and gluten-free, vegan and vegetarian options; no children's facilities stated. |
| Chiringuito Cristóbal (La Butibamba) | medium | medium | medium | medium | Children (judgment) | Listed beach bar (Turismo de Mijas); nothing on children's facilities. |
| Chiringuito Las Dunas (Cabopino) | medium | medium | medium | medium | Young adults (judgment) | Beach bar at a natural beach; winter opening unclear. |
| Chiringuito Rafael (Fuente de la Salud) | unknown | unknown | unknown | unknown | none yet | Identity rests on its own Facebook page only (`weak_identity_source`); rate it after identity and operation are confirmed. |

## For the owner

1. Correct any value in the tables. Your answers can be short, for example "Carvajal SC high".
2. Two judgments that the sources do not settle:
   - Carvajal: is it mostly sand, or gravel and cobbles?
   - Los Álamos: is it a "young, lively" beach?
3. After your corrections, Claude writes the values into the 20 records and closes the matching issues. Records whose only open issue was the family assessment can then move to `needs_editorial_review`, with an approval checklist per record. At present these are Castillo-Ejido and Los Marinos Paco, plus Chiringuito Cristóbal, Chiringuito Los Moreno, La Mar Salá and Santa Ana Denis.
