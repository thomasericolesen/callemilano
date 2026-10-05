# CalleMilano project guidance

## Purpose

CalleMilano is a family travel guide to Andalusia and Spain. Google Maps saved places are discovery inputs. Verify factual claims from appropriate sources before including them in editorial content.

## Canonical project files

- Place records: `docs/places/` (canonical editable place data).
- Place schema and controlled vocabulary: `docs/place-schema.md`.
- Agent specifications and workflows: `docs/maps-import-agent-spec.md` and `docs/multi-agent-workflow.md`.
- Source/rights evidence for images: central asset-rights register at `data/image-rights.csv`.
- Place ID allocation: central ID register at `data/place-id-registry.csv`.
- Generated catalog index: `data/place-catalog.csv`; derive this from place records and never edit it as a second source of truth.
- Images: `images/`.

Do not store editable place records in `data/`; the Markdown files with YAML front matter in `docs/places/` are the only canonical record source.

## Categories and controlled labels

Every place has exactly one primary category: `Restaurants`, `Beaches`, `Excursions`, `Nature`, `City`, or `Family activities`. Use the exact enum spelling in `docs/place-schema.md`. Do not use `Cities` as a category.

Use only schema-controlled values for tags, age groups, family scores, energy, seasonality, booking, accessibility, parking, and cost. Age groups are `Small children (0-6)`, `Children (7-12)`, `Teenagers (13-17)`, `Adults`, `Seniors`; ratings are separate `family_score` values. Do not substitute informal groups such as “toddlers,” “teens,” or “all ages.”

Tags are: `Beach`, `Restaurant`, `Nature`, `Hiking`, `Viewpoint`, `Historic town`, `Museum`, `Adventure`, `Rainy day`, `Half day`, `Full day`, `Free`, `Premium`. Energy is exactly `Low`, `Medium`, or `High`. Seasons are `Spring`, `Summer`, `Autumn`, `Winter`, or `All year`.

Only the human editor-of-record may approve changes to categories, tags, enums, or the schema. Record approved changes in `docs/change-log.md` and update all relevant documentation and records together. Do not introduce synonyms or new values locally.

## Place record format and lifecycle

Each place record is a Markdown file with YAML front matter, named with a lowercase kebab-case slug, in `docs/places/`. The YAML front matter is the canonical data. Narrative Markdown may follow it but must not duplicate structured fields as a competing source.

Records declare `schema_version` and `status`. Valid statuses and transitions are defined in `docs/place-schema.md`. Unknown values are allowed only in draft workflow states and only in fields whose schema permits them. Never mark a record `approved` or `published` while publication-blocking facts, source evidence, validation errors, or review decisions remain unresolved.

Use stable IDs allocated through `data/place-id-registry.csv`; check the registry before creating a record. Do not derive a replacement ID when a name changes. A slug change requires a redirect entry according to the schema.

## Sources, evidence, and accuracy

Use official venue, government, tourism, transport, park, or heritage sources wherever available. Maps may establish identity, coordinates, and the source link, but not claims about safety, access, prices, facilities, opening, or family suitability. Record source URLs, supported claims/fields, dates checked, and checker in the record's evidence ledger. Apply the source-quality policy in the agent specifications.

Do not fabricate experience, reviews, amenities, prices, accessibility, child suitability, or travel time. If sources conflict or evidence is absent, retain an allowed unknown value and a review issue; do not guess. Preserve Spanish spelling and accents. Keep fact statements distinct from editorial judgments.

Driving time is an approximate one-way route from **Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain** to a named destination point. Record route source and check date. Do not estimate from memory.

## Images and rights

Do not copy Google Maps images or user-uploaded material unless reuse permission is documented. Each image needs a stable asset ID, source, documented rights, required credit, role, dimensions when known, and useful context-specific alt text. Track rights and review status in `data/image-rights.csv`. Exclude assets with unclear or withdrawn rights. Alt text is for accessibility, not keyword insertion.

## Content and review

Write clear, useful, family-focused descriptions. Make suitability, energy, season, cost, and access claims evidence-aware and qualified. Accessibility and family ratings require human review under the evidence policy. Check volatile details according to the review intervals in `docs/multi-agent-workflow.md`.

The human editor-of-record owns final approval, source disputes, taxonomy, schema changes, correction escalation, and archival decisions. Agents prepare drafts and may not publish or deploy. Use the issue and handoff formats in the workflow for ambiguity, failures, corrections, and unresolved evidence.

## Validation

Before a record advances to human approval, validate YAML/front matter, schema version, required fields, enums, unique ID and slug, ID registry, duplicate place identity, URLs, evidence, and SEO uniqueness against the catalog. The validation gate is mandatory; a validation failure leaves the record in a draft/review status.
