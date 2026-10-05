# MVP wireframes

**Audience:** Guests staying at Casa de la Familia in Cerros del Águila.  
**Design goal:** Make a good outing choice quickly, show practical limits before commitment, and keep the next action obvious.

The MVP has three core pages—Home, Search/Browse, and Place detail—with Filters opening as a panel from Browse. The wireframes below show content order and actions, not visual styling. Recommendation cards appear on Home and Browse. Directions and official booking links are actions on the Place detail page, not separate CalleMilano pages.

## 1. Home page

```text
┌────────────────────────────────────┐
│ CalleMilano            Browse ▾     │
├────────────────────────────────────┤
│ Find a day out from Casa de la      │
│ Familia                             │
│ [Search an activity or place…]      │
│                                    │
│ What kind of day do you have?       │
│ [Short outing] [Full day]           │
│ [Low effort]   [Rainy-day ideas]    │
│ [Good for younger children]         │
├────────────────────────────────────┤
│ A few good places to start          │
│ [Recommendation card]              │
│ [Recommendation card]              │
│ [Recommendation card]              │
│                                    │
│ [Browse all activities]             │
└────────────────────────────────────┘
```

### Page sections

- **Header:** CalleMilano name and a clear Browse action.
- **Welcome/search:** Explain that choices are planned from Casa de la Familia; accept a place or activity search.
- **Day-intent shortcuts:** Short outing, full day, low effort, younger children, and rainy-day ideas.
- **Starting recommendations:** A small number of checked options with travel and visit-time cues.
- **Browse all:** A clear path to the full collection.

### User actions

Search by place/activity, select a day-intent shortcut, open a recommendation, or browse all activities.

### Mobile layout

Stack sections in the wireframe order. Keep the search and first useful shortcuts near the top. Show one recommendation card per row; avoid requiring horizontal scrolling to compare basic details.

### Desktop layout

Keep the welcome and search prominent at the top. Arrange day-intent shortcuts in a compact grid and show starting recommendations in two or three columns. Keep Browse visible in the header.

## 2. Search/Browse page

```text
┌────────────────────────────────────┐
│ ← Home     Browse activities        │
├────────────────────────────────────┤
│ [Search places or activities…]      │
│ [Filters]  Open date: [Choose date] │
│ Active: [Short visit ×] [Low effort]│
│ 12 places                     Clear │
├────────────────────────────────────┤
│ [Recommendation card]              │
│ [Recommendation card]              │
│ [Recommendation card]              │
│                                    │
│ No match? [Change filters]          │
└────────────────────────────────────┘
```

### Page sections

- **Search and date:** Search by name/activity and optionally choose a visit date when opening information is available.
- **Filter controls:** Open Filters; show active filters as removable labels.
- **Result summary:** Number of matches and a clear reset action.
- **Recommendation list:** Cards with consistent decision information.
- **Empty state:** Explain that no options match and suggest removing a constraint or broadening the search.

### User actions

Search, choose a date, open or clear filters, remove a single active filter, open a place, or open directions from a card. Returning from a place keeps the search and filters.

### Mobile layout

Use a single-column card list. Keep Filters, chosen date, and result count visible before results. Active filter labels wrap onto additional lines; no important card detail should require sideways scrolling.

### Desktop layout

Place search and date above results. Show a compact filter area alongside a two- or three-column card grid. Keep active filters and result count above the cards.

## 3. Filters panel

```text
┌────────────────────────────────────┐
│ Close             Filter activities│
├────────────────────────────────────┤
│ Visit time                          │
│ [Short] [Half day] [Full day]       │
│ Drive from the house                │
│ [Any distance              ▾]       │
│ Activity type                       │
│ [Beach] [Nature] [Attraction] …     │
│ Good fit for                        │
│ [Age group                 ▾]       │
│ Effort                              │
│ [Low] [Medium] [High]               │
│ Budget                              │
│ [Maximum per person       ▾]        │
│ Also consider                       │
│ [ ] Access needs [ ] Dog            │
│ [ ] Toilets      [ ] Food on-site   │
│ [ ] Booking needed                  │
│                                    │
│ [Clear all]       [Show 12 places]  │
└────────────────────────────────────┘
```

### Page sections

- **Header:** Close/cancel without losing current results.
- **Day constraints:** Visit time, approximate drive range, activity type, audience fit, effort, and budget.
- **Optional needs:** Access, dog policy, on-site toilets/food, booking, and chosen date/opening.
- **Actions:** Clear all and apply filters with a result count.

### User actions

Choose any combination of constraints, apply them, clear them, or close the panel. Keep prior choices selected when the guest returns to adjust filters.

### Mobile layout

Present as a full-height, vertically scrollable panel with grouped labels and a persistent bottom action area. Applying filters returns directly to Browse results.

### Desktop layout

Show filters as a left-side panel or column beside results. Keep the apply/reset actions easy to find without scrolling to the very top.

**Decision clarity:** Unknown access or opening information must not be treated as a confirmed match. Label unavailable values and allow guests to broaden the search rather than hiding the uncertainty.

## 4. Place detail page

```text
┌────────────────────────────────────┐
│ ← Results                 Place name│
├────────────────────────────────────┤
│ [Optional approved image]           │
│ Place name · Activity type          │
│ Why consider it: one clear sentence │
│ Fit: ages … · Effort: …             │
├────────────────────────────────────┤
│ Plan your visit                     │
│ Drive from Casa de la Familia: …    │
│ Time there: …                       │
│ Open: …   Checked: …                │
│ Price: …   Booking: …               │
├────────────────────────────────────┤
│ What the visit is like              │
│ Practical limits / restrictions     │
│ Access: …                           │
│ Parking: …                          │
│ Toilets / food / transport: …       │
├────────────────────────────────────┤
│ Visitor point: [named entrance]     │
│ [Map/location preview]              │
│ [Directions from Casa de la Familia]│
├────────────────────────────────────┤
│ Check current details               │
│ [Official site] [Book / check date] │
│ Details last checked: …             │
└────────────────────────────────────┘
```

### Page sections

- **Place identity and reason to go:** Name, experience type, concise benefit, and a qualified audience/effort summary.
- **Plan at a glance:** Drive estimate and visit duration shown separately; hours, price, booking, and check dates.
- **Experience and limits:** What guests do, formal restrictions, accessibility, seasonal caveats, and material practical details.
- **Arrival:** Named visitor point, location preview where useful, parking, and directions.
- **Next step:** Official information and booking/contact links, with a plain statement that live terms and availability are confirmed with the provider.

### User actions

Return to results; open directions from Casa de la Familia; copy the visitor point; open the official venue page; book or check the selected date; call/contact the venue when available. If saving/compare is included, offer it without obscuring the main actions.

### Mobile layout

Use a single column with the decision summary, travel/time, restrictions, and primary actions near the top. Keep “Directions” and “Book/check availability” easy to reach. Put supporting logistics below the core choice information; show unknowns beside the relevant fact.

### Desktop layout

Use a readable main column for the experience and practical details, with a compact planning panel for drive, duration, opening, price, booking, and primary actions. Keep the visitor point and directions adjacent to arrival information.

## Shared recommendation card

Cards appear on Home and Browse; they are not a separate page.

```text
┌──────────────────────────────┐
│ Place name · Activity type   │
│ A specific reason to consider│
│ Drive: …   Time there: …     │
│ Cost: …    Fit/effort: …     │
│ Hours checked: …             │
│ [Details]       [Directions] │
└──────────────────────────────┘
```

Show warnings where a key fact is unknown. Do not label an option “best” or “family-friendly” without a supported reason. On mobile cards stack vertically; on desktop, use a consistent grid so travel, duration, and cost cues line up for quick scanning.

## Map and external booking actions

- **Map/directions:** Show a named entrance or public visitor point. “Directions” opens the guest’s chosen map service with that exact point and Casa de la Familia as origin. For town-scale destinations, explain what the pin represents. Do not use a vague area pin as though it were an entrance.
- **Booking:** Label the official provider and state whether booking is required or recommended. The action opens the provider’s current booking page; tell guests that a link does not guarantee a slot or final price. Guests should be able to return to their CalleMilano results after checking.

## Flow and empty states

**Home → Browse → Filters (optional) → Place detail → Directions or official booking**

If no places match, suggest relaxing one filter and preserve the guest’s other choices. If a practical detail is unknown, say so next to that detail and offer the official confirmation link or a better-documented alternative.
