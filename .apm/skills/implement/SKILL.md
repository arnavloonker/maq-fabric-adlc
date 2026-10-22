---
name: implement
description: Use when implementing an approved Azure DevOps story or selected tasks in Fabric DEV.
---
# Implement

Read [the contract](reference/contract.md), [the procedure](reference/procedure.md), and [DEV isolation](reference/dev-isolation.md).

Inputs: story, optional task IDs, repository, scope.
Load platform identifiers from `maq-project.toon`, capability-matrix.json, and relevant domain records. Consult /best-practices per artifact type.

Use a dedicated branch and worktree, never discarding dirty work. Isolate Fabric DEV. Write a failing seam test (Red), implement, pass (Green).

Delegate lakehouse, notebook, Spark job, and environment work to the spark-cli runtime companion. Delegate other workloads to maq-fabric-* adapter skills. Report unsupported paths as blocked or manual-only.

Approval gates: DEV execution, commits, pushes, PR creation, ADO progress updates. Stop on unresolved design decisions, missing permissions, or timeout uncertainty.

Never autocomplete or merge PRs, bypass policy, close work items, or touch UAT/PROD.

Report commit, branch, isolation, Red/Green evidence, PR, blockers.
