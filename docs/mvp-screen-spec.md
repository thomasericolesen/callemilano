# MVP screen specification

**Audience:** Guests staying at Casa de la Familia in Cerros del Águila.  
**Goal:** Help guests find an outing that fits their party and day, understand the practical details, and take the next step with confidence.

The first public version needs three core screens: Home, Search/Browse, and Place detail. Filters are a panel within Browse rather than a separate destination. Recommendation cards, directions, and booking links are shared guest experiences described below. Keep the experience useful on a phone and make important limitations visible before guests commit to a trip.

## 1. Home page

- **Purpose:** Give guests a fast starting point based on the kind of day they want, rather than asking them to know destination names.
- **Target user:** A guest beginning to plan, often with limited time or an undecided group.
- **Information shown:** Short explanation that recommendations are for guests staying at Casa de la Familia; prominent entry points such as “Short outing,” “Full day,” “Low effort,” “Good for younger children,” and “Rainy-day ideas”; a small selection of useful, recently checked places; clear starting drive and visit-time cues; practical note when details need confirmation.
- **Actions available:** Start browsing from a suggested intent; open a featured place; search by destination or activity; go to all activities.
- **Success criteria:** A first-time guest understands what CalleMilano helps with and reaches a relevant set of options in one action without needing prior local knowledge.

## 2. Search/Browse page

- **Purpose:** Help guests narrow the activity collection and compare the most relevant choices.
- **Target user:** A guest who knows a constraint—such as available time, ages, effort, travel, or budget—but has not chosen a place.
- **Information shown:** Search field; active filters; result count; recommendation cards; useful no-result guidance; indication when a result’s hours or prices need checking. Show travel time from the house separately from time at the destination.
- **Actions available:** Search names or activities; open Filters; remove individual filters or clear all; open a place; open directions; optionally save a place for later if shortlist saving is included.
- **Success criteria:** Guests can narrow results without learning internal categories, understand why an option matches, and can recover easily when filters return no results.

## 3. Filters panel

- **Purpose:** Let guests express the practical conditions that determine whether an outing works for them.
- **Target user:** A guest who needs to rule out unsuitable or impractical choices before reading detail pages.
- **Information shown:** Filters in plain language: visit time (short/half day/full day), approximate drive range from the house, activity type, age suitability, physical effort, budget, access needs, chosen visit date/opening where verified, booking needs, dog policy, and on-site basics such as toilets or food.
- **Actions available:** Select one or more filters; apply; clear all; cancel and return to results. Keep selected filters visible after returning from a place page.
- **Success criteria:** Guests can state their constraints in familiar terms, see how many options remain, and are not given false assurance when information is unknown. Unknown access or opening details must not silently count as a match.

## 4. Place detail page

- **Purpose:** Give guests enough context to make a go/no-go decision and prepare for the outing.
- **Target user:** A guest considering a specific destination or checking its logistics before leaving.
- **Information shown:**
  - A clear description of what the place is and what the core visit includes.
  - Who may enjoy it, the effort involved, formal age/height/supervision restrictions, and material access limitations.
  - Typical time at the destination and one-way drive estimate from Casa de la Familia, shown separately and dated.
  - Current opening information, seasonal limitations, booking requirement/lead time, and current price details when verified. Distinguish estimates and optional costs from fixed charges.
  - Exact visitor point, directions, parking cost/restrictions/walk, transport alternatives where useful, and on-site versus nearby toilets/food.
  - Date practical information was checked, specific unresolved details, and direct links to responsible sources.
- **Actions available:** Open directions; visit the official site; book or check live availability; call/contact the venue when provided; return to results; save/compare if that feature is included.
- **Success criteria:** A guest can tell whether the visit fits the party and day, identify unresolved details honestly, navigate to the right entrance, and confirm volatile facts with the responsible source.

## Shared guest experiences

### Recommendation cards

- **Purpose:** Let guests scan and compare likely options without opening every detail page.
- **Target user:** Guests browsing or reviewing filtered results.
- **Information shown:** Place name; one-sentence reason to consider it; activity type; typical visit duration; one-way drive estimate from the house; broad cost cue; age/effort fit; and a clear warning when a key practical fact is unknown or needs confirmation.
- **Actions available:** Open details; refine filters; optionally save; open directions when the visitor point is clear.
- **Success criteria:** A guest can distinguish options at a glance and does not mistake a broad cost cue, suitability rating, or estimated time for a guarantee.

### Map and directions

- **Purpose:** Connect a selected place to the actual visitor arrival point.
- **Target user:** A guest deciding whether the trip is manageable or ready to leave.
- **Information shown:** A clearly labeled visitor point and, where helpful, a simple location preview. Explain when a town-center pin represents a visitor reference point rather than every attraction in the area.
- **Actions available:** Open the point in the guest’s chosen map service; request directions from Casa de la Familia; copy the destination name/address.
- **Success criteria:** The directions lead to the named entrance or public visitor point, not an ambiguous municipality center or an unrelated pin. Drive-time estimates and map directions refer to the same destination.

### External booking links

- **Purpose:** Let guests confirm current rules and reserve directly with the responsible provider.
- **Target user:** A guest considering a date-sensitive or ticketed visit.
- **Information shown:** Whether booking is required or recommended, any known lead time, the name of the official booking provider, the date the guidance was checked, and a clear note that live availability and final terms are confirmed externally.
- **Actions available:** Open the official booking page; return to CalleMilano after checking; choose another result if the date is unavailable.
- **Success criteria:** Guests reach the correct provider and understand that a link is not confirmation of an available slot or final price.

## MVP navigation flow

**Home → Search/Browse → Filters (optional) → Place detail → Directions or official booking**

Guests should be able to return to their results without losing their search or filters. If key information is unknown, say what is unknown and give the next useful action—such as checking the official source or choosing a better-documented option.
