# Real-Time Intelligence procedure

## Companion skills and tools
| Operation | Preferred | Notes |
| --- | --- | --- |
| Eventhouse, KQL databases and tables | `eventhouse-cli` | |
| Eventstreams | `eventstream-cli` | |
| Event schema sets | `eventschemaset-cli` | |
| Activator rules and actions | `activator-cli` | Alerts must not reach real recipients unapproved |
| Real-time dashboards | No validated companion | `manual-only` until validated |

## Steps
1. Read the matrix row in `capability-matrix.json`; report `blocked` or `manual-only` with the manual path when automation is not permitted.
2. Mutate or execute only in the exact approved, verified workspace from `fabric.devWorkspaceIds` in `maq-project.toon`. Use a branch workspace or prefix shared-DEV artifacts with `<branch_slug>_`.
3. Preview the change set and get approval for those exact operations, including start/stop of streams and alert actions.
4. Execute through the companion skill.
5. KQL reads state their purpose, use a bounded time window, return at most 250 rows with `take`/summarize, and use a 60-second timeout/budget where supported. Report unavailable enforcement; never persist raw sensitive rows.
6. Capture ids, status, and aggregate evidence without sensitive rows or secrets.
7. On timeout, read item state and reconcile before retrying.

## Unavailable paths
Report the missing companion and manual DEV steps. Never connect DEV rules to production sinks or recipients.
