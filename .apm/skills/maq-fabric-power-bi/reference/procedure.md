# Power BI procedure

## Companion skills and tools
| Operation | Preferred | Notes |
| --- | --- | --- |
| Find reports and models | MCP `FabricIQ-DiscoverArtifacts`, `FabricIQ-ResolveFabricItem` | Models and reports only |
| Inspect schema and report metadata | MCP `FabricIQ-GetSemanticModelSchema`, `FabricIQ-GetReportMetadata` | |
| Resolve entity values | MCP `FabricIQ-ValueSearch` | |
| Bounded DAX | MCP `FabricIQ-ExecuteQuery` | Read-only; not Spark/SQL/KQL |
| Semantic model authoring | `semantic-model-authoring` | DEV only |
| Report authoring | `fabric-report-builder` | DEV only |
| Cross-environment model checks | `compare-semantic-models` | Read-only |

## Steps
1. Read the matrix row in `capability-matrix.json`; report `blocked` or `manual-only` with the manual path when automation is not permitted.
2. Rediscover tool schemas; do not assume argument shapes.
3. Resolve the artifact identity and confirm it is in a DEV workspace before any change.
4. DAX: state the purpose, aggregate, return at most 250 rows, and use a 60-second timeout/budget where supported. Bound scans, report unavailable enforcement, and never dump raw sensitive rows.
5. Preview model or report changes and get approval for those exact operations.
6. Author through the companion skill; verify by a bounded DAX check.
7. On timeout, read current definition and reconcile before retrying.

## Unavailable paths
Report the missing tool and manual steps. Never publish or overwrite UAT or PROD models or reports.
