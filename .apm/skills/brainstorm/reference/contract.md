# /brainstorm contract

## Inputs
- Intent: data product, architecture/framework, or new Fabric workload (experiment) question.
- Optional identities: ADO story ID, repository paths, Fabric workspace/item names, semantic model or report.
- Allowed exploration scope: environments, workspaces, row/time/cost limits. Default is read-only.
- Project configuration (`maq-project.json`) only for the parts the exploration uses. Read-only repository brainstorming needs no live-environment credentials.

## Outputs
- `references\explorations\<id>\findings.md` (see `evidence-template.md`); `<id>` = stable slug + collision-resistant run ID.
- Chat summary: each hypothesis marked supported / refuted / inconclusive, evidence-backed choices, rejected alternatives, candidate models, explicit unknowns.
- Never produces a story, spec, or production code. `/to-story` and `/approach` are optional follow-ups the user chooses.

## Preferred tool bindings (rediscover schemas first; do not invent arguments)
| Operation | Preferred tool |
| --- | --- |
| Read story, type metadata, comments | `azure-devops-wit_work_item`: `get`, `get_type`, `list_comments` |
| Related work search | `azure-devops-search_workitem`, `azure-devops-wit_query` (read-only) |
| Code/repo context | local files; `azure-devops-search_code`, `azure-devops-repo_file` |
| Find report/semantic model | `FabricIQ-DiscoverArtifacts` |
| Resolve item identity | `FabricIQ-ResolveFabricItem` |
| Model/report schema | `FabricIQ-GetSemanticModelSchema`, `FabricIQ-GetReportMetadata` |
| Value lookup | `FabricIQ-ValueSearch` |
| Bounded DAX | `FabricIQ-ExecuteQuery` |
| Lakehouse/Warehouse profiling | `fabric-sqlendpoint-execute_query` (bounded SELECT/aggregate only) |

FabricIQ discovery covers semantic models and reports only; its DAX tool is not Spark/SQL/KQL. Other workloads go through internal Fabric adapter skills per the capability matrix; unsupported paths are reported `blocked` or `manual-only`.

## Safe substitutions
Allowed only if semantics, target scope, permissions, approval boundary, and evidence are equivalent. Record each substitution in findings. A generic SQL surface that can mutate data is not equivalent to a read-only query; a CLI helper cannot exceed missing MCP permissions. Never claim a practice was consulted if lookup failed.

## Approval rules
- Approval names a concrete operation set, targets, scope, and version; any change to payload, target, environment, or plan invalidates it.
- A DEV scratch experiment needs explicit approval listing: scratch artifact names (prefixed with a branch/run slug), workspace, permissions, execution/time/cost limits, evidence expected, and cleanup steps. Creation, execution, and cleanup are each in scope of that approval; report failed cleanup.
- Creating a new findings file is non-destructive; modifying an existing file or index requires a preview and approval.
- ADO is read-only in this skill. No story creation, comments, or tag changes.

## Prohibitions
- Mutate DEV only when approved; never mutate UAT/PROD (reads allowed within authorized scope).
- No promotion of experimental artifacts, no production code, no secrets, tokens, connection strings, or raw sensitive rows in findings.
- No unbounded scans; a row limit alone does not bound cost. Prefer schema and aggregate evidence.
