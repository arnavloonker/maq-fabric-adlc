# Databases procedure

## Companion skills and tools
| Operation | Preferred | Notes |
| --- | --- | --- |
| Fabric SQL database authoring | `sqldb-cli` | DEV only |
| SQL reads | MCP `fabric-sqlendpoint-execute_query` | Read-only, bounded |
| Mirroring setup and monitoring | No validated companion | `manual-only` until validated |

## Steps
1. Read the matrix row in `capability-matrix.json`; report `blocked` or `manual-only` with the manual path when automation is not permitted.
2. Writes only to DEV workspaces with `allowMutation: true`, using `fabric.devIsolation` naming.
3. Preview schema or data changes and get approval for those exact operations.
4. Execute through the companion skill; bound reads by purpose, rows, and timeout.
5. For mirroring, report source prerequisites, capacity, and permissions as findings; configuration is a manual DEV action.
6. Capture counts and schema evidence without sensitive rows or connection strings.
7. On timeout, read current state and reconcile before retrying.

## Unavailable paths
Report the missing companion and manual DEV steps. Never alter UAT or PROD databases or mirrors.
