# Approval decisions and handoff, 2026-11-01

Owner (editor-of-record) answers, given on the checklist page "CalleMilano godkendelsestjek" (https://claude.ai/artifact/8t67HJRhqoj8hHSrxityMi, private to the owner) on 2026-11-01 around 21:25 Danish time. They are decisions about how to close the review issues shared across the 12 active local beaches and 8 restaurants. **None of them has been applied to the records yet.**

## Decisions

| # | Question | Owner answer |
|---|---|---|
| 1 | Beach coordinates read by the owner from Google's marker | Accept them as the place point (close `route_and_coordinates_owner_measured`). |
| 2 | Family assessment of beaches (age groups, family scores) | Claude drafts a proposal per beach; the owner corrects it. |
| 3 | Beach seasonality | `Spring`, `Summer`, `Autumn` for all beaches. |
| 4 | Rocks (owner's own knowledge) | No rocks: Boliches-Gaviotas, Cabopino-Artola, Castillo-Ejido, Fuengirola centro, La Butibamba. Unknown (issue stays open): Carvajal, El Bajondillo, Fuente de la Salud, La Carihuela, Los Álamos, Playamar, Santa Ana. |
| 5 | Beach practical details (parking, transport, dogs, cost, food) deliberately unknown | Yes: move the existing owner decision into the approval note and close `practical_details_out_of_scope`. |
| 6 | Family assessment of restaurants | Claude drafts a proposal; the owner corrects it. |
| 7 | Restaurant prices and season unknown with "check before visiting" | Accepted. |
| 8 | Restaurant practical details deliberately unknown, as for beaches | Yes, same rule (Los Marinos Paco keeps its confirmed dog and booking facts). |

## Next steps for the next session

1. Apply decisions 1, 3, 4, 5, 7 and 8 to the records and close the matching review issues; record the owner decisions in each record (evidence or review note) and in `docs/change-log.md`.
2. Draft age groups and family scores for the 12 beaches and 8 restaurants (decisions 2 and 6) as a proposal for the owner to correct; do not treat them as approved.
3. Claude's own clean-up: add Google Maps links to the beaches via Places API (closes `google_maps_url_missing`); replace unverified restaurant names in beach descriptions with links to the verified restaurant records; add URLs for or remove evidence entries without a source (`source_urls_missing`).
4. Move records with no remaining issues to `needs_editorial_review` and give the owner a per-record approval checklist. Closest candidates: Los Marinos Paco, Carvajal, Fuengirola centro, El Bajondillo.
5. Still open beyond these decisions: Santa Ana lifeguard/facility cover (`santa_ana_not_named_in_2026_service`), Cabopino nudist zone and toilets, La Butibamba rock-claim source conflict, Chiringuito Rafael weak identity source, Las Dunas winter opening, the six legacy import drafts' identities.

Run `python3 tools/places.py validate` (currently 68 records, 0 errors) and `python3 tools/places.py catalog` after record changes.

## Progress 2026-11-02

- Step 1 done: decisions 1, 3, 4, 5, 7 and 8 applied (see `docs/change-log.md`). La Butibamba: owner clarified it is a stone beach, not rocky; the rock conflict is closed.
- Step 2: proposal in `docs/decisions/family-assessment-proposal-2026-11-02.md`, waiting for the owner's corrections. Not written into records.
- Step 3 done for beaches: Google Maps links, official beach data (spain.info / andalucia.org), unsourced evidence and claims removed, beach descriptions link only to verified restaurant records. New open point: Fuengirola centro coordinates (`coordinates_far_from_named_beach`).
- Step 4 waits for the owner's corrections to step 2.
- Step 2 done (2026-11-02): owner answers in `docs/decisions/family-assessment-decisions-2026-11-02.md`, written into 18 records.
- Step 4 started: eight records moved to `needs_editorial_review` (see change log); per-record approval still to be given by the owner.
