---
name: to-tasks
description: Use when decomposing an Azure DevOps story into vertical child tasks with dependencies.
---
# To tasks

Read [the outcome](references/outcome.md) and [the procedure](references/procedure.md).

Inputs: story ID, its approach and seam, project sizing conventions.
Load platform identifiers from `maq-project.toon` and relevant domain records. Consult /best-practices for ADO Task guidance.

Propose thin vertical tracer-bullet slices, each fitting one fresh context window. Never create horizontal medallion-layer tasks.

Quiz the engineer on granularity, one question at a time with a recommended answer, until approved.

Discover Azure DevOps tools and link types. Read existing children, preview creates and dependency links, then create only after approval.

Stop when the story lacks an agreed seam, a consequential decision is open, or reconciliation is inconclusive. Never duplicate, update, or close existing tasks. After timeouts, reconcile children before retrying.

Read back and report task URLs, dependencies, and blockers.
