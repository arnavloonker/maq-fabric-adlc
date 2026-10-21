# Fabric IQ procedure

## Companion skills and tools
| Operation | Preferred | Notes |
| --- | --- | --- |
| Ontology authoring and inspection | `fabriciq-ontology-cli` | DEV only; preview features |
| Questions over models and reports | `fabriciq` skill; MCP `FabricIQ-*` tools | Read-only, bounded |
| Graph, planning, data agent items | No validated companion | `planned` or `manual-only` |

## Steps
1. Read the matrix row in `capability-matrix.json`; item types may be preview. Report `blocked` or `manual-only` with the manual path when automation is not permitted.
2. Confirm preview status, tenant settings, and capacity prerequisites; record them as findings.
3. Target only DEV workspaces with `allowMutation: true`.
4. Preview the change set and get approval for those exact operations.
5. Execute through the companion skill; bound any queries by purpose and `queryLimits`.
6. Capture item ids and definitions without secrets or sensitive rows.
7. On timeout, read item state and reconcile before retrying.

## Unavailable paths
Report the gap, preview limitations, and manual DEV steps. Never create or change items in UAT or PROD.
