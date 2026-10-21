# Data Warehouse procedure

## Companion skills and tools
| Operation | Preferred | Notes |
| --- | --- | --- |
| Warehouse DDL/DML authoring | `sqldw-cli` | DEV only |
| Read, profile, reconcile | MCP `fabric-sqlendpoint-execute_query` | Read-only, bounded |
| Dimensional design from schemas | `fabric-model-studio` | Optional, design only |

## Steps
1. Read the matrix row in `capability-matrix.json`; report `blocked` or `manual-only` with the manual path when automation is not permitted.
2. Resolve the target workspace from `maq-project.json`. Writes only to DEV with `allowMutation: true`. UAT/PROD may be read when authorized.
3. Profile before designing: key uniqueness, grain, nulls, and relationships using aggregate queries.
4. Every query states its purpose, applies `queryLimits.maxReturnedRows` and `timeoutSeconds`, and is bounded by predicate or sample. A row limit alone does not bound scan cost; narrow the scan.
5. Preview DDL/DML and get approval for those exact statements and targets.
6. Execute through the companion skill and capture counts and reconciliation results without sensitive rows.
7. On timeout, check object state and reconcile before retrying.

## Unavailable paths
If the SQL endpoint tool or companion skill is absent, report it and give the manual SQL for a human to run in DEV.
