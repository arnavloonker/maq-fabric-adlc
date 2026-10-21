---
name: maq-fabric-databases
description: Use when a MAQ workflow skill needs Fabric SQL database, mirroring, or other supported database experiences in DEV.
---
# MAQ Fabric Databases adapter

Internal adapter called by workflow skills such as /implement and /verify. Read [the procedure](reference/procedure.md).

Scope: SQL database, mirroring, and other supported database items. Check `capability-matrix.json` for the operation's status before acting.

Rules:
- Schema or data changes only in approved DEV workspaces, within an approved change set.
- Starting, stopping, or reconfiguring mirroring is a mutation needing explicit approval.
- Reads are bounded and purpose-specific; never persist sensitive rows.
- If the matrix says `planned`, `manual-only`, or `blocked`, or the companion skill is absent, stop and report the gap with the manual path. Never touch UAT or PROD.
