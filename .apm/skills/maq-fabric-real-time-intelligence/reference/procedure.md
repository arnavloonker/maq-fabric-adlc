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
2. Target only DEV workspaces with `allowMutation: true`, using `fabric.devIsolation` naming.
3. Preview the change set and get approval for those exact operations, including start/stop of streams and alert actions.
4. Execute through the companion skill.
5. KQL reads use a time window, `take`/summarize limits, and the configured timeout; purpose stated.
6. Capture ids, status, and aggregate evidence without sensitive rows or secrets.
7. On timeout, read item state and reconcile before retrying.

## Unavailable paths
Report the missing companion and manual DEV steps. Never connect DEV rules to production sinks or recipients.
