---
name: maq-fabric-data-warehouse
description: Use when a MAQ workflow skill needs Fabric Data Warehouse or SQL analytics endpoint authoring, profiling, or reconciliation queries in DEV.
---
# MAQ Fabric Data Warehouse adapter

Internal adapter called by workflow skills such as /approach, /implement, and /verify. Read [the procedure](reference/procedure.md).

Scope: Warehouses, SQL authoring, and SQL analytics endpoint reads. Check `capability-matrix.json` for the operation's status before acting.

Rules:
- DDL/DML only in approved DEV workspaces, within an approved change set.
- Reads need a purpose, row limit, and timeout; profile grain and keys with aggregates, not raw rows.
- UAT and PROD are read-only and only when authorized.
- If the matrix says `planned`, `manual-only`, or `blocked`, or a tool is absent, stop and report the gap with the manual path.
