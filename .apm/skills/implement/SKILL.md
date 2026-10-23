---
name: implement
description: Use when implementing an approved Azure DevOps story or selected tasks in Fabric lower environments.
---
# Implement

Read [the outcome](references/outcome.md), [the procedure](references/procedure.md), and [DEV isolation](references/dev-isolation.md).

Inputs: story, optional task IDs, repository, scope.
Load platform identifiers from `maq-project.toon`, capability-matrix.json, and relevant domain records. Consult /best-practices per artifact type.

Use a dedicated branch and worktree; preserve dirty work. Recommend DEV and branch-workspace or `<branch_slug>_` isolation. Honor explicitly prompted, concretely approved lower-environment targets, including UAT validation or unprefixed artifacts; record mode and rationale. Write a failing seam test (Red), implement, pass (Green).

Use declared `runtimeSkills` and `toolBindings` on `planned` or `validated-dev` matrix rows; execute and validate in the approved runtime. Block only missing bindings or access, not unverified branch support.

Approval gates: execution, commits, pushes, PRs, ADO updates. Stop on unresolved decisions, missing permissions, or timeout uncertainty.

Never autocomplete, merge, bypass policy, close work, or mutate PROD.

Report commit, branch, isolation, Red/Green evidence, PR, blockers.
