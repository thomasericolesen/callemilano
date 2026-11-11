# Minimum viable CalleMilano

**Audience:** Guests staying at Casa de la Familia in Cerros del Águila.  
**Product goal:** Help a guest quickly find an outing that fits their party, available time, budget, and conditions, then leave with a workable plan.

The first version should be a small, trustworthy guide, not an exhaustive destination catalogue. Its value depends on accurate, current answers for the places it includes. A guest should be able to compare a few suitable choices and understand the drive, time commitment, costs, access, and next planning step before setting out.

Complexity is relative to a simple, mobile-friendly guide with manually maintained content. “High” usually means live integrations or substantial ongoing operations.

## Must: required for a genuinely useful first release

### 1. Curated, decision-ready activity collection

- **Problem solved:** A broad list of places leaves guests to do the research themselves and may include unverified or poorly scoped entries.
- **Guest value:** A manageable set of checked destinations gives guests confidence that each option has enough information to consider.
- **Implementation complexity:** Medium. Research and editorial review are the main effort; the interface can remain simple.
- **Priority:** Must.

### 2. Browse and filter by the day guests want

- **Problem solved:** Guests cannot quickly narrow choices by available time, distance, activity type, effort, age fit, or budget.
- **Guest value:** A guest can start with “short outing,” “low effort,” “works for our ages,” or “free/low cost” and see relevant options.
- **Implementation complexity:** Medium. Requires consistent, verified descriptions and a small set of useful filters.
- **Priority:** Must.

### 3. Practical destination pages

- **Problem solved:** A name and attractive description do not explain what the place actually offers or what could make the visit difficult.
- **Guest value:** Each page answers what the experience is, who may enjoy it, how long it takes, material limitations, and what to check next.
- **Implementation complexity:** Medium. The page layout is straightforward; maintaining useful, claim-supported content takes ongoing editorial work.
- **Priority:** Must.

### 4. Plan total time away from the house

- **Problem solved:** Guests cannot tell whether an outing fits their day if travel time and time at the destination are unclear or mixed together.
- **Guest value:** Show a dated one-way drive estimate to the exact visitor point separately from a typical on-site duration; help guests estimate total time away.
- **Implementation complexity:** Medium. Route estimates and visit durations need manual verification and clear caveats; live traffic integration is not required.
- **Priority:** Must.

### 5. Party fit, formal restrictions, and access details

- **Problem solved:** Broad family labels can hide age/height rules, physical demands, or access barriers for a particular guest.
- **Guest value:** Guests can check age suitability, restrictions, effort, steps/terrain, wheelchair or stroller limitations, and relevant facilities before committing.
- **Implementation complexity:** High editorial effort; medium interface complexity. Many details require venue-specific research and careful review.
- **Priority:** Must.

### 6. Clear cost and booking next steps

- **Problem solved:** A rough price label or booking link alone does not tell guests whether an outing fits their budget or can be booked for their date.
- **Guest value:** Show current adult/child or family prices when available, likely required add-ons, what the estimate includes, whether advance booking is needed, and a direct official link to confirm live availability.
- **Implementation complexity:** Medium for dated prices and links; high for live totals or reservation integrations. The first release should link out instead of promising live availability.
- **Priority:** Must.

### 7. Exact arrival point and essential logistics

- **Problem solved:** Guests may navigate to the wrong entrance or discover too late that parking, toilets, food, or return transport do not fit their needs.
- **Guest value:** Provide a clearly named visitor point with a directions link, plus verified parking cost/restrictions and on-site versus nearby facility information when material.
- **Implementation complexity:** Medium. Each destination needs a checked point and practical details; directions can open in an existing map app.
- **Priority:** Must.

### 8. Visible freshness and official next steps

- **Problem solved:** Hours, prices, access, and booking details change; guests cannot plan confidently if they cannot tell what is current.
- **Guest value:** Show when important practical details were last checked and link directly to the responsible venue or authority for live information.
- **Implementation complexity:** Medium. Requires a review routine and clear dates; automatic monitoring can wait.
- **Priority:** Must.

## Should: high-value additions after the core guide works

### 9. Compare and save a short list

- **Problem solved:** Guests weigh a few options across time, cost, travel, and suitability but must keep details in memory or reopen pages.
- **Guest value:** Compare two or three places side by side and keep a small shortlist during their stay.
- **Implementation complexity:** Medium. A browser-based shortlist can avoid accounts and complex profile handling.
- **Priority:** Should.

### 10. Weather-aware alternatives and backup choices

- **Problem solved:** Heat, rain, closures, or a mismatch in effort can derail the day after guests have already chosen a destination.
- **Guest value:** Offer a nearby or otherwise practical alternative with a clear reason it fits the same party and time window.
- **Implementation complexity:** Medium to high. Recommendations need curated relationships and current conditions; a manually prepared “if this plan changes” section is a good start.
- **Priority:** Should.

### 11. Non-driving and dog-friendly planning details

- **Problem solved:** A destination may be unsuitable when guests do not have a car or are travelling with a dog, even if the activity itself appeals.
- **Guest value:** Surface verified transport links, last-mile effort, return options, and material dog-policy conditions.
- **Implementation complexity:** Medium to high because schedules and policies change and vary by destination.
- **Priority:** Should.

## Could: defer until guests demonstrate the need

### 12. Build a multi-stop itinerary

- **Problem solved:** Guests may want to combine destinations, meals, and travel into a complete day plan.
- **Guest value:** A sequenced itinerary could reduce planning effort and make better use of a day.
- **Implementation complexity:** High. It requires dependable travel times, opening calendars, duration estimates, and conflict handling across stops.
- **Priority:** Could.

### 13. Live availability, traffic, and personalized recommendations

- **Problem solved:** Static guidance cannot reflect same-day traffic, changing weather, remaining booking slots, or a guest’s full preferences.
- **Guest value:** More tailored recommendations and fewer surprises when conditions change.
- **Implementation complexity:** High. Requires external services, ongoing reliability work, and clear handling of stale or unavailable data.
- **Priority:** Could.

## MVP release test

The first release is ready when a guest can:

1. Find a small set of relevant activities using time, travel, effort, age-fit, and cost preferences.
2. Understand the actual experience and any important restriction or access limitation.
3. Estimate the time and likely cost for their party, with uncertainty clearly shown.
4. Confirm current hours and booking details with the responsible source.
5. Navigate to the correct visitor point and know the essential arrival logistics.

If a destination cannot answer those questions reliably, leave it out of the recommended collection until it can. The guide should earn trust through useful choices, not the number of listings.
