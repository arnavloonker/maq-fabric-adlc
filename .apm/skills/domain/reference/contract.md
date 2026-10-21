# /domain contract

## Purpose
Produce one Markdown file per business domain, `domain\<business-domain>.md`, plus `domain\index.md`, as shared knowledge records for engineers and agents. Records are broader than glossaries.

## Definitions
- **Domain:** a business responsibility and vocabulary with identified ownership. A source system, workspace, or bronze/silver/gold layer is not automatically a domain.
- **Domain record:** reviewed knowledge plus clearly labeled provisional observations.

## Inputs
Selected domain names, or a request to discover candidate business boundaries. Repository root and `maq-project.json` (only the parts needed: paths, selected domain ownership, standards documents). Optional: authorized live metadata.

## Required sections per domain file (in order)
1. Purpose and owner. Unknown ownership is written as `Unknown`.
2. Business vocabulary. Implementation-free: no table, column, notebook, pipeline, workspace, layer, or code names, and no design decisions.
3. Source systems.
4. Data products.
5. Source-of-truth references (links to authoritative systems, not copies of data).
6. Reviewed rules. Only rules with a named reviewer and date.
7. Provisional observations. Inferred from code or data; each with source, timestamp, and confidence.
8. Explicit conflicts. Competing claims side by side with sources; never silently resolved.
9. Change log.

## Index
`domain\index.md` lists each domain with owner, one-line purpose, file link, last-reviewed date, and open conflict count.

## Rules
- Code behavior is never business policy; it is a provisional observation until a human reviews it.
- Do not claim a documentation folder establishes data-mesh governance.
- Never erase or rewrite human-reviewed content or human edits.
- Provenance (source identifier, observation time, environment/version, run ID, review status, limitations) is recorded for every non-vocabulary entry.
- No secrets, tokens, connection strings, or raw sensitive results. Link to authoritative systems.
- Consult /best-practices for applicable artifact types; do not claim consultation if the lookup failed, and report failures.

## Approvals and stops
- New files are created non-destructively (never overwrite an existing path).
- Existing files, including the index, require a previewed diff and approval of that exact operation set.
- A changed target, payload, or environment invalidates approval.
- Stop and report if live validation lacks access (record as inconclusive) or the existing file is not parseable into the template.

## Output
Changed files, new provisional observations, conflicts, and unknowns.
