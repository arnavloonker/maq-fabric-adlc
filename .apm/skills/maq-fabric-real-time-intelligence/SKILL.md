---
name: maq-fabric-real-time-intelligence
description: Use when a MAQ workflow skill needs Fabric Real-Time Intelligence work on eventstreams, Eventhouse/KQL, real-time dashboards, or Activator in DEV.
---
# MAQ Fabric Real-Time Intelligence adapter

Internal adapter called by workflow skills such as /implement and /verify. Read [the procedure](reference/procedure.md).

Scope: Eventstreams, Eventhouse and KQL databases, real-time dashboards, and Activator rules. Check `capability-matrix.json` for the operation's status before acting.

Rules:
- Mutate only in approved DEV workspaces, within an approved change set.
- Starting streams or enabling alert actions is a mutation; Activator actions must not notify real recipients without approval.
- KQL reads need a time window, row limit, and timeout.
- If the matrix says `planned`, `manual-only`, or `blocked`, or the companion skill is absent, stop and report the gap. Never touch UAT or PROD.
