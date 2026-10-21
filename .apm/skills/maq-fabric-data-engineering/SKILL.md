---
name: maq-fabric-data-engineering
description: Use when a MAQ workflow skill needs Fabric Data Engineering work on lakehouses, notebooks, Spark job definitions, or environments in DEV.
---
# MAQ Fabric Data Engineering adapter

Internal adapter called by workflow skills such as /implement and /verify. Read [the procedure](reference/procedure.md).

Scope: Lakehouses, notebooks, Spark job definitions, environments, and related items. Check `capability-matrix.json` for the operation's status before acting.

Rules:
- Mutate and execute only in approved DEV workspaces, within an approved change set.
- Use bounded, purpose-stated queries; prefer schema and aggregates over raw rows.
- Apply the configured dev isolation prefix or branch workspace.
- If the matrix says `planned`, `manual-only`, or `blocked`, or the companion skill is absent, stop and report the gap with the manual path. Never touch UAT or PROD.
