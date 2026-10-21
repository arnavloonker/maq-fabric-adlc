# Data Warehouse procedure

## Companion skills and tools
| Operation | Preferred | Notes |
| --- | --- | --- |
| Warehouse DDL/DML authoring | `sqldw-cli` | DEV only |
| Read, profile, reconcile | MCP `fabric-sqlendpoint-execute_query` | Read-only, bounded |
| Dimensional design from schemas | `fabric-model-studio` | Optional, design only |

## Steps
1. Read the matrix row in `capability-matrix.json`; report `blocked` or `manual-only` with the manual path when automation is not permitted.
2. Resolve the target workspace from `maq-project.toon` and verify live identity and environment. Mutate or execute only in an approved workspace from `fabric.devWorkspaceIds`; UAT/PROD are read-only when authorized. Use a branch workspace or `<branch_slug>_` shared-DEV prefix.
3. Profile before designing: key uniqueness, grain, nulls, and relationships using aggregate queries.
4. Every query states its purpose, returns at most 250 rows, uses a 60-second timeout/budget where supported, and is bounded by predicate or sample. Report unavailable enforcement. A row limit alone does not bound scan cost; narrow the scan. Never persist raw sensitive rows.
5. Preview DDL/DML and get approval for those exact statements and targets.
6. Execute through the companion skill and capture counts and reconciliation results without sensitive rows.
7. On timeout, check object state and reconcile before retrying.

## Unavailable paths
If the SQL endpoint tool or companion skill is absent, report it and give the manual SQL for a human to run in DEV.
