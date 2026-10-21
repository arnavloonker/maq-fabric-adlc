---
name: brainstorm
description: Use when testing a Fabric data product, architecture, or new workload hypothesis against repository code and live data before committing to a build.
---
# Brainstorm

Read [the contract](reference/contract.md) and [the procedure](reference/procedure.md).

Scope comes from the user's intent plus story, repository, or Fabric identities. Load `maq-project.toon` only for required platform dependencies and relevant domain records and references. Consult /best-practices for each artifact type inspected.

State hypotheses and what would refute them. Inspect code, then authorized Fabric schemas and bounded query results. Ask unresolved decisions one question at a time, each with a recommended answer. For data asks, profile grain, key uniqueness, joins, and reconciliations.

Read-only by default. Stop for explicit approval before any DEV scratch experiment, including its limits and cleanup. Never mutate UAT/PROD, publish stories, write production code, or present inferred business intent as fact. Insufficient access yields an inconclusive finding.

Save sanitized findings, using [the template](reference/evidence-template.md), to `references\explorations\<id>\findings.md`. Report supported, refuted, or inconclusive hypotheses, rejected alternatives, and unknowns. Preview before writing shared files.
