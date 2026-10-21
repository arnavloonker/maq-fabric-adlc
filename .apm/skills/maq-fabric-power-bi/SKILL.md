---
name: maq-fabric-power-bi
description: Use when a MAQ workflow skill needs Power BI semantic model, report, or dashboard discovery, authoring, or bounded DAX queries in DEV.
---
# MAQ Fabric Power BI adapter

Internal adapter called by workflow skills such as /approach, /implement, and /verify. Read [the procedure](reference/procedure.md).

Scope: Semantic models, reports, and supported dashboard operations. Check `capability-matrix.json` for the operation's status before acting.

Rules:
- Model or report changes only in approved DEV workspaces, within an approved change set.
- DAX queries are bounded, purpose-stated, and read-only; prefer aggregates.
- Discovery tools cover models and reports only, not every Fabric workload.
- If the matrix says `planned`, `manual-only`, or `blocked`, or a tool is absent, stop and report the gap with the manual path. Never publish to UAT or PROD.
