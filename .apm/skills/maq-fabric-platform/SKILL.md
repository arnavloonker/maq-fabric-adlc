---
name: maq-fabric-platform
description: Use when a MAQ workflow skill needs cross-workload Fabric platform work on OneLake, catalog governance, Git integration, variables, or CI/CD in DEV.
---
# MAQ Fabric Platform adapter

Internal adapter called by workflow skills such as /implement and /verify. Read [the procedure](reference/procedure.md).

Scope: OneLake, governance and catalog, Git integration, variable libraries, deployment pipelines, and operational dependencies. Check `capability-matrix.json` before acting.

Rules:
- Distinguish repository change, workspace change, execution, and promotion; a merged PR is not a deployment.
- Git sync and variable changes only in approved DEV workspaces.
- Never run deployment pipelines or promote to UAT or PROD; read and plan only.
- If the matrix says `planned`, `manual-only`, or `blocked`, or the companion skill is absent, stop and report the gap with the manual path.
