# End-to-end recommendation demo

Ten example guest sessions run through the questionnaire in `docs/guest-questionnaire-spec.md` and the existing recommendation engine in `docs/recommendation-engine-spec.md`. The candidate set is the existing `data/destination-metadata.csv`; tags and classification confidence come from `data/destination-classification.csv`. No destination data has been added or changed.

The engine first applies the selected profile, drive-limit filter, and available-time filter, then ranks eligible destinations with the current formula. For drive ranges, the questionnaire spec uses the upper end to decide whether a finite limit is met. Time filters follow the spec: half-day keeps half-day visits; full day keeps half-day and full-day visits; overnight or longer keeps all recorded durations. Recommendations expose names and natural-language explanations, never raw scores or suitability values.

Drive times below are rough editorial ranges from Casa de la Familia, not route-checked estimates. Confidence is the source classification confidence where available, not confidence that current hours, access, facilities, or conditions have been verified.


## 1. Nearby half-day with young children

**Guest answers**

- **Group profile:** Family with young children
- **Maximum one-way drive:** Up to 2 hours
- **Time available:** half-day

**Filtering**

Keep places within the two-hour drive limit and with a recorded duration that fits half-day availability. 5 existing destinations remain eligible; the first five are shown. The existing persona weights and tag preferences rank the eligible set.

**Top recommendations**

1. **Palmeral de Las Sorpresas** — The collection’s themes suggest a waterfront walk and scenic views, which may suit your family with young children. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm the exact route segment, current facilities, accessible route, and useful visit duration. **Confidence:** High classification confidence; this does not verify current visitor details.
2. **Playa la Malagueta** — The collection’s themes suggest beach time and a waterfront walk, which may suit your family with young children. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm current bathing/water information, seasonal services, access, facilities, and any restrictions. **Confidence:** High classification confidence; this does not verify current visitor details.
3. **Mercado de Atarazanas** — The collection’s themes suggest a local market and everyday city atmosphere, as well as archaeological or historic interest, which may suit your family with young children. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm current hours, market days, facilities, access details, and holiday schedule. **Confidence:** High classification confidence; this does not verify current visitor details.
4. **Marbella Old Town** — It is among the better-fitting options for your family with young children in the existing collection; its estimated half-day visit and medium energy level fit the time available. **Estimated drive:** 30–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.
5. **Frigiliana** — It is among the better-fitting options for your family with young children in the existing collection; its estimated half-day visit and high energy level fit the time available. **Estimated drive:** 1.25–1.5 h one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.


## 2. Full day with teenagers

**Guest answers**

- **Group profile:** Family with teenagers
- **Maximum one-way drive:** Up to 2 hours
- **Time available:** full-day

**Filtering**

Keep places within the two-hour drive limit and with a recorded duration that fits full-day availability. 7 existing destinations remain eligible; the first five are shown. The existing persona weights and tag preferences rank the eligible set.

**Top recommendations**

1. **Selwo Aventura** — It is among the better-fitting options for your family with teenagers in the existing collection; its estimated full-day visit and high energy level fit the time available. **Estimated drive:** 20–30 min one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.
2. **Playa la Malagueta** — The collection’s themes suggest beach time and a waterfront walk, which may suit your family with teenagers. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm current bathing/water information, seasonal services, access, facilities, and any restrictions. **Confidence:** High classification confidence; this does not verify current visitor details.
3. **Ronda** — It is among the better-fitting options for your family with teenagers in the existing collection; its estimated full-day visit and medium energy level fit the time available. **Estimated drive:** 1.5–1.75 h one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.
4. **Marbella Old Town** — It is among the better-fitting options for your family with teenagers in the existing collection; its estimated half-day visit and medium energy level fit the time available. **Estimated drive:** 30–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.
5. **Palmeral de Las Sorpresas** — The collection’s themes suggest a waterfront walk and scenic views, which may suit your family with teenagers. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm the exact route segment, current facilities, accessible route, and useful visit duration. **Confidence:** High classification confidence; this does not verify current visitor details.


## 3. Low-effort half-day for an active retired couple

**Guest answers**

- **Group profile:** Active retired couple
- **Maximum one-way drive:** Up to 2 hours
- **Time available:** half-day

**Filtering**

Keep places within the two-hour drive limit and with a recorded duration that fits half-day availability. 5 existing destinations remain eligible; the first five are shown. The existing persona weights and tag preferences rank the eligible set.

**Top recommendations**

1. **Palmeral de Las Sorpresas** — The collection’s themes suggest a waterfront walk and scenic views, which may suit an active retired couple. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm the exact route segment, current facilities, accessible route, and useful visit duration. **Confidence:** High classification confidence; this does not verify current visitor details.
2. **Mercado de Atarazanas** — The collection’s themes suggest a local market and everyday city atmosphere, as well as archaeological or historic interest, which may suit an active retired couple. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm current hours, market days, facilities, access details, and holiday schedule. **Confidence:** High classification confidence; this does not verify current visitor details.
3. **Marbella Old Town** — It is among the better-fitting options for an active retired couple in the existing collection; its estimated half-day visit and medium energy level fit the time available. **Estimated drive:** 30–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.
4. **Playa la Malagueta** — The collection’s themes suggest beach time and a waterfront walk, which may suit an active retired couple. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm current bathing/water information, seasonal services, access, facilities, and any restrictions. **Confidence:** High classification confidence; this does not verify current visitor details.
5. **Frigiliana** — It is among the better-fitting options for an active retired couple in the existing collection; its estimated half-day visit and high energy level fit the time available. **Estimated drive:** 1.25–1.5 h one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.


## 4. Nearby half-day with grandparents and grandchildren

**Guest answers**

- **Group profile:** Grandparents with grandchildren
- **Maximum one-way drive:** Up to 2 hours
- **Time available:** half-day

**Filtering**

Keep places within the two-hour drive limit and with a recorded duration that fits half-day availability. 5 existing destinations remain eligible; the first five are shown. The existing persona weights and tag preferences rank the eligible set.

**Top recommendations**

1. **Palmeral de Las Sorpresas** — The collection’s themes suggest a waterfront walk and scenic views, which may suit grandparents and grandchildren. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm the exact route segment, current facilities, accessible route, and useful visit duration. **Confidence:** High classification confidence; this does not verify current visitor details.
2. **Playa la Malagueta** — The collection’s themes suggest beach time and a waterfront walk, which may suit grandparents and grandchildren. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm current bathing/water information, seasonal services, access, facilities, and any restrictions. **Confidence:** High classification confidence; this does not verify current visitor details.
3. **Mercado de Atarazanas** — The collection’s themes suggest a local market and everyday city atmosphere, as well as archaeological or historic interest, which may suit grandparents and grandchildren. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm current hours, market days, facilities, access details, and holiday schedule. **Confidence:** High classification confidence; this does not verify current visitor details.
4. **Marbella Old Town** — It is among the better-fitting options for grandparents and grandchildren in the existing collection; its estimated half-day visit and medium energy level fit the time available. **Estimated drive:** 30–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.
5. **Frigiliana** — It is among the better-fitting options for grandparents and grandchildren in the existing collection; its estimated half-day visit and high energy level fit the time available. **Estimated drive:** 1.25–1.5 h one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.


## 5. Full day for an aviation enthusiast

**Guest answers**

- **Group profile:** Aviation enthusiast
- **Maximum one-way drive:** Any distance
- **Time available:** full-day

**Filtering**

Keep places with no drive limit and with a recorded duration that fits full-day availability. 19 existing destinations remain eligible; the first five are shown. The existing persona weights and tag preferences rank the eligible set.

**Top recommendations**

1. **Selwo Aventura** — The current record does not identify an aviation experience; this appears because the broader group and outing estimates ranked it highly. Treat it as a general outing, not an aviation recommendation. **Estimated drive:** 20–30 min one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.
2. **Olvera Castle** — The collection’s themes suggest historic fortifications, distinctive town character and scenic views, but none of the recorded themes identifies an aviation experience. **Estimated drive:** 1.75–2.25 h one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm official venue identity, hours, admission, access/stairs, and town approach. **Confidence:** Medium classification confidence; this does not verify current visitor details.
3. **Ronda** — The current record does not identify an aviation experience; this appears because the broader group and outing estimates ranked it highly. Treat it as a general outing, not an aviation recommendation. **Estimated drive:** 1.5–1.75 h one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.
4. **Mercado de Atarazanas** — The collection’s themes suggest a local market and everyday city atmosphere, as well as archaeological or historic interest, but none of the recorded themes identifies an aviation experience. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm current hours, market days, facilities, access details, and holiday schedule. **Confidence:** High classification confidence; this does not verify current visitor details.
5. **Aracena** — The collection’s themes suggest distinctive town character, caves or underground features and historic fortifications, but none of the recorded themes identifies an aviation experience. **Estimated drive:** 3–3.5 h one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, choose the intended town or attraction scope; current opening and booking details for specific sights. **Confidence:** Medium classification confidence; this does not verify current visitor details.


## 6. Manageable day for a mixed-age group

**Guest answers**

- **Group profile:** Mixed-age family group
- **Maximum one-way drive:** Up to 2 hours
- **Time available:** full-day

**Filtering**

Keep places within the two-hour drive limit and with a recorded duration that fits full-day availability. 7 existing destinations remain eligible; the first five are shown. The existing persona weights and tag preferences rank the eligible set.

**Top recommendations**

1. **Palmeral de Las Sorpresas** — The collection’s themes suggest a waterfront walk and scenic views, which may suit a mixed-age family group. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm the exact route segment, current facilities, accessible route, and useful visit duration. **Confidence:** High classification confidence; this does not verify current visitor details.
2. **Selwo Aventura** — It is among the better-fitting options for a mixed-age family group in the existing collection; its estimated full-day visit and high energy level fit the time available. **Estimated drive:** 20–30 min one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.
3. **Playa la Malagueta** — The collection’s themes suggest beach time and a waterfront walk, which may suit a mixed-age family group. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm current bathing/water information, seasonal services, access, facilities, and any restrictions. **Confidence:** High classification confidence; this does not verify current visitor details.
4. **Mercado de Atarazanas** — The collection’s themes suggest a local market and everyday city atmosphere, as well as archaeological or historic interest, which may suit a mixed-age family group. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm current hours, market days, facilities, access details, and holiday schedule. **Confidence:** High classification confidence; this does not verify current visitor details.
5. **Ronda** — It is among the better-fitting options for a mixed-age family group in the existing collection; its estimated full-day visit and medium energy level fit the time available. **Estimated drive:** 1.5–1.75 h one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.


## 7. Full day for a hiking enthusiast

**Guest answers**

- **Group profile:** Hiking enthusiast
- **Maximum one-way drive:** Up to 3 hours
- **Time available:** full-day

**Filtering**

Keep places within the three-hour drive limit and with a recorded duration that fits full-day availability. 13 existing destinations remain eligible; the first five are shown. The existing persona weights and tag preferences rank the eligible set.

**Top recommendations**

1. **Mercado de Atarazanas** — The collection’s themes suggest a local market and everyday city atmosphere, as well as archaeological or historic interest, but the current classification does not identify a hiking route for this place. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm current hours, market days, facilities, access details, and holiday schedule. **Confidence:** High classification confidence; this does not verify current visitor details.
2. **Olvera Castle** — The collection’s themes suggest historic fortifications, distinctive town character and scenic views, but the current classification does not identify a hiking route for this place. **Estimated drive:** 1.75–2.25 h one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm official venue identity, hours, admission, access/stairs, and town approach. **Confidence:** Medium classification confidence; this does not verify current visitor details.
3. **Palmeral de Las Sorpresas** — The collection’s themes suggest a waterfront walk and scenic views, but the current classification does not identify a hiking route for this place. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm the exact route segment, current facilities, accessible route, and useful visit duration. **Confidence:** High classification confidence; this does not verify current visitor details.
4. **Zahara de la Sierra** — The current record does not identify a hiking route; this appears because the broader group and outing estimates ranked it highly. Confirm it fits your main interest before setting out. **Estimated drive:** 2–2.5 h one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.
5. **Marbella Old Town** — The current record does not identify a hiking route; this appears because the broader group and outing estimates ranked it highly. Confirm it fits your main interest before setting out. **Estimated drive:** 30–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.


## 8. Beach-focused family day

**Guest answers**

- **Group profile:** Beach-focused family
- **Maximum one-way drive:** Up to 2 hours
- **Time available:** full-day

**Filtering**

Keep places within the two-hour drive limit and with a recorded duration that fits full-day availability. 7 existing destinations remain eligible; the first five are shown. The existing persona weights and tag preferences rank the eligible set.

**Top recommendations**

1. **Palmeral de Las Sorpresas** — The collection’s themes suggest a waterfront walk and scenic views, but no beach feature is identified for this place. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm the exact route segment, current facilities, accessible route, and useful visit duration. **Confidence:** High classification confidence; this does not verify current visitor details.
2. **Selwo Aventura** — The current record does not identify a beach feature; this appears because the broader family and outing estimates ranked it highly. Treat it as a general outing, not a beach recommendation. **Estimated drive:** 20–30 min one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.
3. **Playa la Malagueta** — The collection’s themes suggest beach time and a waterfront walk, but no beach feature is identified for this place. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm current bathing/water information, seasonal services, access, facilities, and any restrictions. **Confidence:** High classification confidence; this does not verify current visitor details.
4. **Ronda** — The current record does not identify a beach feature; this appears because the broader family and outing estimates ranked it highly. Treat it as a general outing, not a beach recommendation. **Estimated drive:** 1.5–1.75 h one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.
5. **Marbella Old Town** — The current record does not identify a beach feature; this appears because the broader family and outing estimates ranked it highly. Treat it as a general outing, not a beach recommendation. **Estimated drive:** 30–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.


## 9. Mixed-age group open to an overnight trip

**Guest answers**

- **Group profile:** Mixed-age family group
- **Maximum one-way drive:** Any distance
- **Time available:** overnight or longer

**Filtering**

Keep places with no drive limit and with a recorded duration that fits overnight or longer availability. 30 existing destinations remain eligible; the first five are shown. The existing persona weights and tag preferences rank the eligible set.

**Top recommendations**

1. **Palmeral de Las Sorpresas** — The collection’s themes suggest a waterfront walk and scenic views, which may suit a mixed-age family group. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm the exact route segment, current facilities, accessible route, and useful visit duration. **Confidence:** High classification confidence; this does not verify current visitor details.
2. **Selwo Aventura** — It is among the better-fitting options for a mixed-age family group in the existing collection; its estimated full-day visit and high energy level fit the time available. **Estimated drive:** 20–30 min one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.
3. **Playa la Malagueta** — The collection’s themes suggest beach time and a waterfront walk, which may suit a mixed-age family group. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm current bathing/water information, seasonal services, access, facilities, and any restrictions. **Confidence:** High classification confidence; this does not verify current visitor details.
4. **Aracena** — The collection’s themes suggest distinctive town character, caves or underground features and historic fortifications, which may suit a mixed-age family group. **Estimated drive:** 3–3.5 h one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, choose the intended town or attraction scope; current opening and booking details for specific sights. **Confidence:** Medium classification confidence; this does not verify current visitor details.
5. **Mercado de Atarazanas** — The collection’s themes suggest a local market and everyday city atmosphere, as well as archaeological or historic interest, which may suit a mixed-age family group. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm current hours, market days, facilities, access details, and holiday schedule. **Confidence:** High classification confidence; this does not verify current visitor details.


## 10. Teen family open to a long-distance trip

**Guest answers**

- **Group profile:** Family with teenagers
- **Maximum one-way drive:** Any distance
- **Time available:** overnight or longer

**Filtering**

Keep places with no drive limit and with a recorded duration that fits overnight or longer availability. 30 existing destinations remain eligible; the first five are shown. The existing persona weights and tag preferences rank the eligible set.

**Top recommendations**

1. **Selwo Aventura** — It is among the better-fitting options for your family with teenagers in the existing collection; its estimated full-day visit and high energy level fit the time available. **Estimated drive:** 20–30 min one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Visit duration is an editorial estimate. Current files do not provide destination-specific access, opening, or facility notes. **Confidence:** Limited; no classification is recorded, so the destination match is less specific.
2. **Olvera Castle** — The collection’s themes suggest historic fortifications, distinctive town character and scenic views, which may suit your family with teenagers. **Estimated drive:** 1.75–2.25 h one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm official venue identity, hours, admission, access/stairs, and town approach. **Confidence:** Medium classification confidence; this does not verify current visitor details.
3. **Aracena** — The collection’s themes suggest distinctive town character, caves or underground features and historic fortifications, which may suit your family with teenagers. **Estimated drive:** 3–3.5 h one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, choose the intended town or attraction scope; current opening and booking details for specific sights. **Confidence:** Medium classification confidence; this does not verify current visitor details.
4. **Alcalá del Júcar** — The collection’s themes suggest distinctive town character, geological features, historic fortifications and scenic views, which may suit your family with teenagers. **Estimated drive:** 4–5 h one way. **Expected duration:** full-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm the intended scope, specific attractions, opening dates, access/steps, and current costs. **Confidence:** High classification confidence; this does not verify current visitor details.
5. **Playa la Malagueta** — The collection’s themes suggest beach time and a waterfront walk, which may suit your family with teenagers. **Estimated drive:** 25–40 min one way. **Expected duration:** half-day. **Practical notes:** Drive range is a rough estimate, not route-checked. Before going, confirm current bathing/water information, seasonal services, access, facilities, and any restrictions. **Confidence:** High classification confidence; this does not verify current visitor details.


## What the demo shows

The same destinations recur because the existing collection is small and many profile outcomes depend on nearby drive estimates and broad suitability metadata. Some top results have no destination tag classification, so their tag component is neutral under the current engine. In the hiking and aviation scenarios, several results are not specifically about hiking or aviation; the available metadata and tags do not consistently represent those interests. These examples reflect current engine behavior and should not be read as verified trip advice.
