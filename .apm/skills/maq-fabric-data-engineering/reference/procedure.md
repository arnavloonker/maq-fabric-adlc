# Data Engineering procedure

## Companion skills and tools
| Operation | Preferred | Notes |
| --- | --- | --- |
| Notebooks, Spark jobs, lakehouse tables, environments | `spark-cli` | Fabric notebook authoring and execution |
| Lakehouse SQL reads | MCP `fabric-sqlendpoint-execute_query` | Read-only, bounded |
| Databricks code conversion | `databricks-migration` | Only when migrating existing code |
| Medallion layout | `e2e-medallion-architecture` | Only for data-product requests |

## Steps
1. Read the matrix row in `capability-matrix.json`. Proceed only if status permits; otherwise report `blocked` or `manual-only` with the manual path.
2. Resolve the DEV workspace from `maq-project.json` (`allowMutation: true`). Refuse any other target.
3. Apply `fabric.devIsolation`: use the branch workspace if available, else the shared-DEV prefix `prefixTemplate`.
4. Preview the change set (items, names, code) and get approval for those exact operations.
5. Execute through the companion skill. For queries, state the purpose and apply `queryLimits` (rows, timeout). Aggregates over raw rows.
6. Record evidence (item ids, run ids, counts) without sensitive rows or secrets.
7. On timeout or unknown outcome, read current state and reconcile before any retry.

## Unavailable paths
If a companion skill or tool is missing, report which one and the manual steps for a human in DEV. Never substitute a broader-authority path.
