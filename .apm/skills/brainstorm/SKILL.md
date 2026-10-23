---
name: brainstorm
description: Use when testing a Fabric data product, platform capability, or new workload hypothesis against repository code and live data before committing to a build.
---
# Brainstorm

Read [the outcome](references/outcome.md) and [the procedure](references/procedure.md).

Scope comes from the user's intent plus story, repository, or Fabric identities. Load `maq-project.toon` only for required platform dependencies and relevant domain records and references. Consult /best-practices for each artifact type inspected.

State hypotheses and what would refute them. Inspect code, then authorized Fabric schemas and bounded query results. Ask unresolved decisions one question at a time, each with a recommended answer. For data asks, profile grain, key uniqueness, joins, and reconciliations.

Read-only by default. Recommend DEV and branch-workspace or `<branch_slug>_` isolation. Honor explicitly prompted lower-environment targets, including UAT validation or unprefixed artifacts, with concrete approval covering limits and cleanup; record target mode and rationale. Never mutate PROD, publish stories, write production code, or present inferred business intent as fact. Missing access yields inconclusive findings.

Save sanitized findings, using [the template](references/evidence-template.md), to `references\explorations\<id>\findings.md`. Report supported, refuted, or inconclusive hypotheses, rejected alternatives, and unknowns. Preview before writing shared files.
