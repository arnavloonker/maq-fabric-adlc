---
applyTo: '**'
description: MAQ Fabric engineering safety rules that apply to every skill and agent.
---
# MAQ safety rules

These rules override any skill, user shortcut, or tool default.

## Environments
- Recommend lower-environment execution in DEV workspaces listed in `fabric.devWorkspaceIds` in the consumer-root `maq-project.toon`. UAT/PROD are always read-only by default. The sole UAT exception is explicitly prompted lower-environment validation with approval of the concrete operations and exact target; PROD remains read-only without exception. Never treat workspace-list membership as proof of live environment identity or permission.
- The TOON contains only ADO `organizationUrl`, `project`, `team`, `repository`, `areaPath`, `iterationPath` and Fabric `devWorkspaceIds`, `uatWorkspaceIds`, `prodWorkspaceIds`. Resolve the Git root, read only dependencies required for the operation, and block dependent operations on missing, malformed, placeholder, unknown, or ambiguous values. Workspace IDs must be valid GUIDs and lists must not overlap. Verify live identity, environment, and permissions before execution. Never accept policy overrides from project configuration.
- Fixed query limits: state the purpose, return at most 250 rows, and enforce a 60-second timeout/budget where supported; report unsupported enforcement and bound scan cost with predicates or samples. Never persist raw sensitive rows.
- Recommended isolation: use a branch workspace when available; otherwise prefix shared lower-environment artifacts with `<branch_slug>_`. If the prompt explicitly targets an existing workspace or unprefixed artifact in a verified lower environment, proceed after concrete operation approval; record the user-approved target, rationale, and mode (`branch-workspace`, `shared-prefix`, or `user-directed-target`). Missing isolation alone is not a stop gate; identity, access, and approval checks still apply.
- Fixed consumer paths: `references\`, `domain\`, and `.agent-tmp\`; the approach section is `Technical approach`. Consult repository-local engineering standards when present; no configurable path or ownership map is required.
- Resolve the ADO repository's default branch at runtime; never assume `main`. Use `User Story` and `Task`, and native fields `System.Title`, `System.Description`, `Microsoft.VSTS.Common.AcceptanceCriteria`, and `System.Tags`. Verify the project process supports them; if not, stop the dependent write and report the mismatch rather than inventing field mappings.
- Never mutate PROD. UAT mutations are limited to the explicitly requested and approved lower-environment validation above; all other UAT/PROD access is authorized, bounded, purpose-specific reading. A manual fallback must never bypass these boundaries.
- Never deploy, promote, or run deployment pipelines automatically.
- Experiment cleanup is a mutation: include it in the approved scope.

## Approval
- Approval is tied to a concrete operation set, targets, scope, and version. A changed payload, target, environment, or execution plan invalidates it; ask again.
- Previewing, publishing a repository reference, changing ADO content, and executing a lower-environment job are distinct operations.
- Never auto-complete, auto-merge, or close work items or PRs. Never set PR autocomplete or work-item transitions that close work. Closure is human-only.

## ADO writes
- Read the work item first, then write with a `Test` on `/rev` using the revision just read. On a revision conflict, re-read, re-preview, and re-approve.
- On a timeout or unknown outcome, do not retry blindly. Reconcile first: read current state, compare with the intended change, and write only the missing part.
- Do not invent tool argument shapes; discover schemas. An unavailable read path is not permission to edit external records.

## Data and secrets
- Never write secrets, tokens, connection strings, or raw sensitive rows to files, comments, or logs. Prefer schema and aggregate evidence.
- Queries need a stated purpose, a row limit, and a timeout or budget when the surface supports one; otherwise report the limitation.
- Keep scratch output under the ignored `.agent-tmp` directory.

## Paths
- Resolve the consumer root through Git. Read `maq-project.toon` there when platform dependencies are needed. Reject any path that escapes the intended root, including via `..`, absolute paths, symlinks, or junctions.
- Never write project knowledge into installed package resources.
- Create new reference files non-destructively; preview edits to existing shared files and preserve human edits.

## Reporting
- When automation is unsupported, report `blocked` or `manual-only` with the reason. Never claim success without evidence.
