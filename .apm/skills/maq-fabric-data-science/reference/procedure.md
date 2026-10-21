# Data Science procedure

## Companion skills and tools
| Operation | Preferred | Notes |
| --- | --- | --- |
| Training or scoring code in notebooks | `spark-cli` | DEV only; runs are executions |
| Reading prepared data | MCP `fabric-sqlendpoint-execute_query` | Read-only, bounded |
| ML experiments, model registry, endpoints | No validated companion | `manual-only` until validated |

## Steps
1. Read the matrix row in `capability-matrix.json`; report `manual-only` with the manual path when no automation is validated.
2. Run only in the exact approved, verified workspace from `fabric.devWorkspaceIds` in `maq-project.toon`. Use a branch workspace or prefix shared-DEV artifacts with `<branch_slug>_`.
3. Preview notebooks, experiment names, and data scope; get approval for those exact operations.
4. Use sampled or windowed data for training and scoring checks; state the purpose.
5. Capture run ids, metrics, and parameters. Do not persist sensitive rows.
6. Cleanup of experiments, runs, or models is a mutation and must be in the approved scope.
7. On timeout, read run state and reconcile before retrying.

## Unavailable paths
Report the gap and manual DEV steps. Never register or serve models in UAT or PROD.
