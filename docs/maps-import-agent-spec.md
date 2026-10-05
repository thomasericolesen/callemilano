# Maps import agent specification

## Purpose

The Maps Import Agent converts a Google Maps place URL or place name into a draft CalleMilano place record. It does not implement publishing or publish content.

## Authority and canonical data

- Follow `AGENTS.md` and the current version of `docs/place-schema.md`.
- The sole canonical place records are Markdown files with YAML front matter in `docs/places/`. Do not write place records to `data/` or create a second editable copy.
- Reserve IDs in `data/place-id-registry.csv`; the generated `data/place-catalog.csv` is read-only and used for duplicate detection and catalog checks.
- Use exact category, tag, age-group, family-score, energy, seasonality, cost, and enum values from the schema. Schema version for each generated record must match the active schema.

## Inputs

A work item contains:

- Required `input`: a Google Maps URL or a place name.
- Optional locality, municipality, province, country, list label, user notes, or intended visitor context.
- Batch item ID, if imported as part of a saved-place list.

A batch queue entry is tracked in `data/import-queue.csv` with an intake ID, input, status, retry count, duplicate candidate IDs, pending clarification, assigned stage, and last update. Do not put secrets or unrelated personal data in the queue.

## Source policy

Use official venue, government, official tourism, transport, park, and heritage sources for visitor claims, prioritizing the authority responsible for the fact. Secondary sources may fill gaps only when clearly labeled and no suitable official source exists. Google Maps can help resolve identity, coordinates, and the source listing; it is not evidence for safety, access, facilities, prices, opening, or family suitability.

Every material factual claim must have an entry in the record's `evidence` ledger with supported field/claim, source URL, source type, check date, checker, confidence, and notes. When sources conflict, do not silently choose; create a review issue and route it to the human editor-of-record if the responsible authority does not resolve it.

Do not copy Maps reviews, listing descriptions, or photos. Do not infer image rights. For images, use only approved supplied or licensed assets; record each asset in `data/image-rights.csv` and use its asset ID in the record. If no approved asset exists, `images: []` is valid.

## Workflow

### 1. Intake, resolve, and deduplicate

- Accept a Maps URL or place name.
- Resolve the canonical place and distinguish it from similarly named places.
- Capture the original Maps URL, coordinates, coordinate purpose/label, locality, municipality, province, autonomous community, and country.
- Check the generated catalog and registry for duplicate identity or ID before researching.
- If ambiguous, set the batch queue item to `waiting_for_clarification`, record the exact question and candidate matches, and pause that item. Resume the same item after the answer; do not create a guessed record.

### 2. Reserve identity

- Request the next stable ID from `data/place-id-registry.csv` using its region/province namespace and collision-checked sequence.
- Determine a unique lowercase kebab-case slug and check it against the catalog.
- If an existing record matches, route it as an update to its current owner rather than creating a duplicate.

### 3. Research and create draft

- Research the source facts needed for required fields and family-planning details.
- Check a one-way drive from Casa de la Familia, Urbanización Cerros del Águila, Las Lagunas de Mijas, Málaga, Spain to an explicitly named destination point. Record route source/date or use `duration: null` and a blocking issue.
- Use unknowns only as permitted by schema and record unresolved fields in `review_issues`.
- Generate short/long descriptions, controlled tags, audience scores, energy, seasonality, cost, and SEO fields from verified evidence and editorial judgment. Mark judgment calls for human review when evidence is weak.
- Include every required schema field, source evidence, review dates, and a draft status.

### 4. Save and validate

- Write one Markdown file with YAML front matter to `docs/places/{slug}.md`.
- Preserve the active schema version and stable ID. Do not overwrite an existing record without checking its current revision and owner.
- Validate YAML syntax, required fields, enum values, ID/slug uniqueness, evidence structure, links, and the correct status requirements. The workflow validation gate is defined in `docs/multi-agent-workflow.md`.
- Update the intake queue state and provide a handoff report. Never set `approved` or `published`.

## Output contract

A successful import produces:

1. One schema-compliant Markdown place record in `docs/places/`.
2. A batch queue update.
3. A handoff report with stable ID, file path, identity confidence, candidate/verified sources, field changes, open issues, duplicate result, and requested next stage.

The Markdown body may contain source notes or review context, but the front matter is the only canonical structured record.

## Unknowns, failures, and issue format

Allowed queue states: `queued`, `resolving`, `waiting_for_clarification`, `draft_created`, `needs_fact_check`, `blocked`, `complete`.

Every issue uses the schema format: `code`, `severity` (`blocking`, `warning`, `info`), `fields`, `description`, `retryable`, and `owner`. Retry transient source or validation failures according to the workflow retry policy; do not retry ambiguous identity without clarification. Escalate persistent identity conflicts, unsupported high-impact claims, rights uncertainty, or schema gaps to the human editor-of-record.

## Completion criteria

An import is complete for handoff only when a draft is saved at the canonical path, it declares the current schema version, its identity and ID are resolved, its schema validation passes for draft status, and all unresolved facts are visible as review issues. A completed import is not approved or publishable by that fact alone.
