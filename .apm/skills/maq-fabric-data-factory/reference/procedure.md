# Data Factory procedure

## Companion skills and tools
| Operation | Preferred | Notes |
| --- | --- | --- |
| Pipeline definitions, conversion | `pipeline-migration` | Author pipeline JSON for Fabric |
| Dataflow Gen2 items, M, destinations, refresh history | `dataflows-cli` | |
| Warehouse/lakehouse reads for reconciliation | MCP `fabric-sqlendpoint-execute_query` | Read-only, bounded |

## Steps
1. Read the matrix row in `capability-matrix.json`; report `blocked` or `manual-only` with the manual path when automation is not permitted.
2. Target only DEV workspaces with `allowMutation: true`; apply `fabric.devIsolation` naming.
3. Preview the change set and get approval for those exact operations.
4. Author or update items through the companion skill.
5. Running a pipeline or refreshing a dataflow is a separate execution needing its own approval, with bounded inputs (date window, parameter range).
6. Capture run ids, status, and row-count evidence without sensitive rows or secrets.
7. On timeout or unknown outcome, read run status and reconcile before retrying.

## Unavailable paths
Report the missing companion and manual DEV steps. Never create schedules or triggers in UAT or PROD.
