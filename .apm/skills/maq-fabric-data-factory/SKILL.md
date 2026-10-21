---
name: maq-fabric-data-factory
description: Use when a MAQ workflow skill needs Fabric Data Factory work on data pipelines, Dataflow Gen2, or orchestration in DEV.
---
# MAQ Fabric Data Factory adapter

Internal adapter called by workflow skills such as /implement and /verify. Read [the procedure](reference/procedure.md).

Scope: Data pipelines, Dataflow Gen2, and orchestration items. Check `capability-matrix.json` for the operation's status before acting.

Rules:
- Mutate and execute only in approved DEV workspaces, within an approved change set.
- Triggering a pipeline or refresh is an execution; it needs its own approval and a bounded scope.
- Never deploy or schedule into UAT or PROD.
- If the matrix says `planned`, `manual-only`, or `blocked`, or the companion skill is absent, stop and report the gap with the manual path.
