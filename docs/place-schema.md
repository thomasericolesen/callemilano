# CalleMilano place schema

Schema version: **1.0.0**. This is the canonical contract for records stored as Markdown with YAML front matter in `docs/places/`. The YAML front matter is the only editable structured source of truth. Examples in `docs/examples/` illustrate fields but are not place records and must not be published directly.

## Required record fields

| Field | Type | Required | Definition |
|---|---|---:|---|
| `schema_version` | string | Yes | Schema version, currently `1.0.0`. |
| `status` | enum | Yes | Lifecycle status; see Record lifecycle. |
| `id` | string | Yes | Stable ID allocated in `data/place-id-registry.csv`, format `ES-{REGION}-{PROVINCE}-{PLACE}-{NNN}` (example `ES-AND-MAL-NERJA-001`). Never change after allocation. |
| `slug` | string | Yes | Unique lowercase kebab-case canonical page slug. Changing it requires a redirect entry in `redirects`. |
| `name` | string | Yes | Canonical public name, preserving correct local spelling and accents. |
| `category` | enum | Yes | Exactly one primary category from the controlled list. |
| `tags` | string array | Yes | Applicable controlled tags; empty array if none. |
| `coordinates` | object | Yes | WGS 84 decimal latitude/longitude, purpose, source, and check date. |
| `google_maps_url` | URL or null | Yes | Original saved-place/listing URL when supplied; otherwise `null` with an issue note. |
| `external_ids` | object | Yes | Known external identifiers, such as Google Maps Place ID or an official venue ID; empty object if unavailable. |
| `municipality` | string | Yes | Administrative municipality, not merely the locality. |
| `province` | string | Yes | Spanish province. |
| `autonomous_community` | string | Yes | Autonomous community, using its official name. |
| `country` | string | Yes | Country name; use `Spain` for Spanish destinations. |
| `driving_time_from_casa_de_la_familia` | object | Yes | One-way duration from the fixed origin to a named destination point, route source, and check date. Duration may be unresolved in draft. |
| `age_groups` | string array | Yes | Suitable controlled age groups; empty only if none can be assessed, with an issue note. |
| `family_score` | object | Yes | Rating for every audience key using `low`, `medium`, `high`, or `unknown`. |
| `energy_level` | enum | Yes | Exactly `Low`, `Medium`, or `High`. |
| `seasonality` | string array | Yes | Applicable controlled seasons. |
| `accessibility` | object | Yes | Structured access facts by access dimension; see Accessibility. |
| `wheelchair_friendly` | enum | Yes | Derived summary: `yes`, `no`, `partial`, or `unknown`; must agree with mobility details in `accessibility`. |
| `parking` | object | Yes | Structured parking facts; unknown fields are explicit in draft. |
| `transport_options` | array | Yes | Known transit, shuttle, walking, cycling, or other non-driving options; empty array if none are verified. |
| `booking_required` | boolean or enum | Yes | `true`, `false`, or `unknown`. |
| `dog_friendly` | enum | Yes | `yes`, `no`, `partial`, or `unknown`. |
| `toilets_available` | enum | Yes | `yes`, `no`, or `unknown`. |
| `food_available` | enum | Yes | `yes`, `no`, or `unknown`; food must be available at the place, not merely nearby. |
| `cost_level` | enum | Yes | `Free`, `€`, `€€`, `€€€`, `€€€€`, or `Unknown`, based on per-person core experience. |
| `visit_information` | object | Yes | Optional structured opening/schedule, typical visit duration, booking lead time, and validity period; unknown values are explicit. |
| `links` | object | Yes | Official website, booking, visitor information, transport, and contact links; use null for unavailable links. |
| `related_places` | array | Yes | References by stable ID, with relationship type; empty array if none. |
| `description_short` | string | Yes | Concise family-oriented summary. |
| `description_long` | string | Yes | Accurate detail and relevant practical limitations. |
| `seo_title` | string | Yes | Unique and accurate search title. |
| `seo_description` | string | Yes | Unique, accurate search snippet. |
| `images` | image object array | Yes | Rights-aware metadata for used images; empty array when no approved image is available. |
| `evidence` | evidence object array | Yes | Claim/field-to-source ledger; may be incomplete only in draft statuses. |
| `review_issues` | array | Yes | Open issue objects; empty array when none. |
| `created_at` | date | Yes | Record creation date (`YYYY-MM-DD`). |
| `updated_at` | date | Yes | Date any record content was last changed. |
| `last_verified` | date or null | Yes | Most recent fact check date; null only before any fact check. |
| `last_reviewed_at` | date or null | Yes | Most recent editorial review date. |
| `next_review_at` | date or null | Yes | Next review date based on field volatility; null only while draft has no review schedule. |
| `review_decision` | object or null | Yes | Human approval decision, reviewer, date, and notes; required on approval and publication. |
| `redirects` | string array | Yes | Former slugs that must redirect to this page; empty array if none. |

### Record lifecycle

Allowed statuses: `draft`, `needs_fact_check`, `needs_editorial_review`, `approved`, `published`, `archived`.

Normal transitions are `draft` → `needs_fact_check` → `needs_editorial_review` → `approved` → `published` → `archived`. A failed check returns the record to `draft` with a review issue. An approved or published record with a material correction re-enters `needs_fact_check`; it is not silently edited in place while retaining approval. Only the human editor-of-record may set `approved`, `published`, or `archived`. `published` additionally requires the separate publication process; agents never publish.

Unknown values and open review issues are allowed in `draft`, `needs_fact_check`, or `needs_editorial_review` when represented as specified. `approved` and `published` require all publication-blocking fields verified, no blocking issues, a complete evidence ledger, successful validation, and human review decision. Unknowns may remain only in explicitly non-blocking fields and must be displayed honestly.

### Geography and coordinates

Use standardized official administrative names and ISO 3166-1 alpha-2 country codes in `external_ids` or related metadata where useful; the display field `country` remains a readable name. Coordinates require:

```yaml
coordinates:
  latitude: 36.746
  longitude: -3.879
  purpose: town_center # venue | entrance | town_center | representative_point
  label: "Balcón de Europa area"
  source: https://example.org/map-or-official-source
  checked_at: 2026-10-03
```

For a large destination, select and label one stable public visitor reference point, normally the official visitor entrance or central public square. Never imply the coordinates represent every attraction in the municipality.

### Driving time

Origin is **Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain**. The object contains `duration`, `origin`, `destination`, `source`, `checked_at`, and `note`. Duration is a one-way route estimate; state minutes or hours/minutes, not distance. Route and traffic affect travel time. Drafts may use `duration: null` with a `review_issues` entry; do not use free-text fake durations such as “Not yet verified.”

### Categories and tags

Choose exactly one primary category:

- `Restaurants` — restaurants, cafés, and food/drink venues.
- `Beaches` — beaches, coves, and coastal bathing areas.
- `Excursions` — organized outings, routes, and destination-led trips not better represented by another category.
- `Nature` — natural areas/features such as parks, reserves, rivers, or caves, when not primarily a hike.
- `City` — a city, town, or village recommended as a destination.
- `Family activities` — attractions/activities centered on a visitor activity.

Controlled tags: `Beach`, `Restaurant`, `Nature`, `Hiking`, `Viewpoint`, `Historic town`, `Museum`, `Adventure`, `Rainy day`, `Half day`, `Full day`, `Free`, `Premium`. Use exact spelling. Tags describe secondary features and never replace category. New or retired terms require editor-of-record approval and a schema change recorded in `docs/change-log.md`.

### Age groups and family suitability

`age_groups` may contain: `Small children (0-6)`, `Children (7-12)`, `Teenagers (13-17)`, `Adults`, `Seniors`.

`family_score` has all five keys: `small_children`, `children`, `teenagers`, `adults`, `seniors`. Values are `low`, `medium`, `high`, or `unknown`. Ratings are suitability guidance, not safety guarantees. Consider age limits, supervision, terrain, stairs, sensory demands, visit length, and mobility. A high rating does not override a formal restriction.

### Energy, season, and cost

Energy is `Low` (little physical effort), `Medium` (some manageable walking/activity), or `High` (sustained or challenging activity). Seasonality uses one or more of `Spring`, `Summer`, `Autumn`, `Winter`, `All year`; use `All year` only if reasonably suitable in every season, and separately report seasonal opening.

Cost is a qualitative **per-person estimate for the core experience** in euros: `Free`, `€`, `€€`, `€€€`, `€€€€`, or `Unknown`. Record `cost_basis` and `cost_checked_at` inside `visit_information`; separate optional parking, transport, meals, and equipment. Tiers are not price guarantees and should not be compared across unlike place types without context.

### Accessibility

Use one structured object as the source of truth. `wheelchair_friendly` is a derived display summary and must not contradict `accessibility`.

```yaml
accessibility:
  overall: "Known summary or unknown"
  mobility:
    route: "Surface, gradients, stairs, distance"
    wheelchair_route: "yes | no | partial | unknown"
    facilities: "Relevant mobility facilities"
  sensory:
    notes: "Relevant noise, lighting, or sensory information, or unknown"
  accessible_toilets: "yes | no | unknown"
  source: https://example.org/access
  checked_at: 2026-10-03
  confidence: "high | medium | low | unknown"
```

Do not infer access from a generic venue label or a photograph. If route or facilities vary by area, describe the scope.

### Parking and transport

`parking` contains `availability`, `location_type` (`onsite`, `nearby`, `street`, `none`, `unknown`), `cost`, `restrictions`, `walk_distance`, `source`, and `checked_at`. Distinguish destination parking from nearby parking. `transport_options` entries identify mode, stop/access point, source, and check date. Do not invent transit service or schedules.

### Links and visit information

`links` supports nullable `official_website`, `booking`, `visitor_information`, `transport`, and `contact` URLs. `visit_information` supports nullable schedule, typical duration, booking lead time, validity start/end, cost basis, and cost check date. Volatile information must include source evidence and validity/check date. These are optional facts even though the containing objects are required; represent unknown subfields as null.

### Related places

Each `related_places` item references an existing stable ID and a controlled relationship such as `nearby`, `part_of`, `alternative_to`, or `itinerary_next`. Never duplicate another place's record as a relationship.

### Evidence and review issues

Every factual claim used in descriptions or visitor fields must be represented in `evidence`:

```yaml
evidence:
  - field: "visit_information.schedule"
    claim: "Published visiting schedule"
    source_url: https://example.org/official-info
    source_type: official_venue # official_venue | government | official_tourism | official_transport | secondary | maps_identity
    checked_at: 2026-10-03
    checked_by: "agent-or-editor identifier"
    confidence: high # high | medium | low
    notes: null
review_issues: []
```

A review issue contains `code`, `severity` (`blocking`, `warning`, `info`), `fields`, `description`, `retryable`, and `owner`. Source notes in the Markdown body may summarize the ledger but do not replace it.

### Image metadata and asset rights

Each image object contains `asset_id`, `role` (`cover`, `gallery`, `map`, `decorative`), `src`, `alt`, `caption`, `source`, `rights`, `credit`, `width`, `height`, and `rights_status` (`approved`, `pending`, `withdrawn`). Asset IDs are unique and recorded in `data/image-rights.csv` with permission evidence and review date. Only `approved` rights status can be published. Empty alt text is for decorative images only.

### ID and slug allocation

Reserve IDs in `data/place-id-registry.csv` before creating records. Use region/province codes from the project registry and the next unused zero-padded sequence in that namespace. Check both ID and place identity to avoid duplicates. Never recycle an ID. On rename, retain the ID; if the slug changes, add the old slug to `redirects`.

## Example record: Nerja

This is illustrative only and is not approved for publication. Unverified values are explicitly unknown, and the record remains a draft. The front-matter format below is used for canonical records; this documentation example is shown as YAML for readability.

```yaml
schema_version: 1.0.0
status: draft
id: ES-AND-MAL-NERJA-001
slug: nerja-malaga
name: Nerja
category: City
tags:
  - Beach
  - Viewpoint
  - Historic town
coordinates:
  latitude: 36.746
  longitude: -3.879
  purpose: town_center
  label: "Balcón de Europa area"
  source: https://visitanerja.es/atracciones/balcon-de-europa/
  checked_at: 2026-10-03
google_maps_url: https://www.google.com/maps/search/?api=1&query=Balcon+de+Europa%2C+Nerja%2C+Spain
external_ids: {}
municipality: Nerja
province: Málaga
autonomous_community: Andalusia
country: Spain
driving_time_from_casa_de_la_familia:
  duration: null
  origin: Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain
  destination: "Balcón de Europa area, Nerja, Málaga, Spain"
  source: null
  checked_at: null
  note: Verify current one-way route before publication.
age_groups:
  - Small children (0-6)
  - Children (7-12)
  - Teenagers (13-17)
  - Adults
  - Seniors
family_score:
  small_children: unknown
  children: unknown
  teenagers: unknown
  adults: unknown
  seniors: unknown
energy_level: Medium
seasonality:
  - Spring
  - Summer
  - Autumn
  - Winter
accessibility:
  overall: unknown
  mobility:
    route: unknown
    wheelchair_route: unknown
    facilities: unknown
  sensory:
    notes: unknown
  accessible_toilets: unknown
  source: null
  checked_at: null
  confidence: unknown
wheelchair_friendly: unknown
parking:
  availability: unknown
  location_type: unknown
  cost: unknown
  restrictions: unknown
  walk_distance: unknown
  source: null
  checked_at: null
transport_options: []
booking_required: unknown
dog_friendly: unknown
toilets_available: unknown
food_available: unknown
cost_level: Unknown
visit_information:
  schedule: null
  typical_duration: null
  booking_lead_time: null
  valid_from: null
  valid_until: null
  cost_basis: null
  cost_checked_at: null
links:
  official_website: https://visitanerja.es/
  booking: null
  visitor_information: https://www.spain.info/en/destination/nerja/
  transport: null
  contact: null
related_places: []
description_short: "A coastal town in Málaga province with a historic center and sea views."
description_long: "Nerja is a coastal town in Málaga province. Confirm the specific visitor route, facilities, seasonal details, and suitability before planning a visit."
seo_title: "Nerja, Málaga: Coastal Town and Historic Center"
seo_description: "Plan a visit to Nerja, a coastal town in Málaga province. Check current access, facilities, and visitor details before travelling."
images: []
evidence:
  - field: "name, municipality, province, description_short"
    claim: "Nerja is a destination in Málaga province with a coastal setting."
    source_url: https://www.spain.info/en/destination/nerja/
    source_type: official_tourism
    checked_at: 2026-10-03
    checked_by: "example-author"
    confidence: high
    notes: "Illustrative citation; reconfirm before using this draft as a live record."
review_issues:
  - code: driving_time_unverified
    severity: blocking
    fields: [driving_time_from_casa_de_la_familia]
    description: "Verify one-way route and record a routing source and date."
    retryable: true
    owner: fact_check
created_at: 2026-10-03
updated_at: 2026-10-03
last_verified: null
last_reviewed_at: null
next_review_at: null
review_decision: null
redirects: []
```
