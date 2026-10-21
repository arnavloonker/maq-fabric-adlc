# Platform procedure

## Companion skills and tools
| Operation | Preferred | Notes |
| --- | --- | --- |
| Git integration (connect, commit, update) | `git-integration-operations-cli` | DEV workspaces only |
| Deployment pipelines | `deployment-pipelines-authoring-cli` | Inspect and plan only; never deploy |
| Variable libraries | `variable-library-cli` | DEV values only |
| OneLake catalog, governance, search | `onelake-catalog-govern-cli` | Read-only unless approved in DEV |
| Lineage and release readiness | `fabric-devops-analyze-lineage`, `fabric-devops-validate` | Read-only |
| Workspace SQL reads | MCP `fabric-sqlendpoint-execute_query` | Bounded |

## Steps
1. Read the matrix row in `capability-matrix.json`; support varies by item type. Report `blocked` or `manual-only` with the manual path when automation is not permitted.
2. Separate repository change, workspace change, execution, and promotion in the plan; a successful PR is not proof of deployment.
3. Use the branch workspace when supported, else the shared-DEV prefix fallback.
4. Preview the change set and get approval for those exact operations.
5. Git sync and variable changes only in DEV workspaces with `allowMutation: true`.
6. Do not run deployment-pipeline deploy operations. Describe the human steps for promotion instead.
7. On timeout, read sync or operation state and reconcile before retrying.

## Unavailable paths
Report the missing companion and manual steps. Never promote or mutate UAT or PROD.
