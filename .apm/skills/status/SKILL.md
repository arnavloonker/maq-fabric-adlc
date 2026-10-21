---
name: status
description: Use when you need a read-only personal sprint summary of your Azure DevOps work in the configured team's current iteration.
---
# Status

Read [the contract](reference/contract.md) and [the procedure](reference/procedure.md).

Scope is the signed-in user, the ADO project/team in `maq-project.toon`, plus explicit story, iteration, or person filters. History is fixed at 30 days and 50 events; no status settings are required. Consult /best-practices for ADO User Story and Task guidance.

Resolve the team's current iteration dynamically with the azure-devops-work iteration tools, never the static creation `iterationPath`. Ask if scope is ambiguous.

Report actual ADO states, labeled parent, child, and dependency context, an explicit or clearly labeled inferred phase, bounded chronology, blockers, and remaining actions. Never fabricate completion percentages, or treat a PR merge as deployment.

Strictly read-only: make no work-item, PR, or sprint writes. Stop and report any access gap rather than guessing.

Output goes to the conversation. Save a snapshot to `references\status\<snapshot-id>.md` only when requested, previewing before writing.
