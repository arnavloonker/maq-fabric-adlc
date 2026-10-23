# Exploration findings: Data-product approach documentation

- Exploration ID: issue-8-data-product-51169477
- Authoring run / date-time (UTC): 2026-10-22T23:58:02Z
- Related story: GitHub issue arnavloonker/maq-fabric-adlc#8
- Review status: unreviewed
- Publication: local/unpublished
- Sensitivity handling: Repository definitions and public documentation only; no live Fabric data or sensitive rows inspected.

## Hypotheses
| # | Hypothesis | Supports if | Refutes if | Outcome (supported / refuted / inconclusive) |
| --- | --- | --- | --- | --- |
| 1 | `data-product` better represents end-to-end engineering intent than `data-model`. | The approach must cover sources, ETL, orchestration, serving, and operations in addition to schemas. | The skill is used only for isolated schema design. | supported |
| 2 | Composable documentation views improve clarity without producing template noise. | Each view resolves a distinct implementation decision and irrelevant views can be omitted explicitly. | Every approach requires the same artifacts and detail. | supported |
| 3 | Worked diagrams and mappings reduce ambiguity more than prose-only requirements. | Examples demonstrate lineage, model, and failure-path notation while remaining synthetic. | Examples are treated as mandated architecture or copied as facts. | supported with explicit synthetic labels |
| 4 | Source-to-Seam traceability connects design, implementation, and verification. | Every proposed output can be traced to sources, owning artifacts, orchestration, and a measurable product result. | The selected Seam cannot observe the intended product outcome. | supported |

## Evidence
| Subject | Source (workspace/item/path) | Environment | Observed at | Query/definition version | Result (sanitized) | Limitations |
| --- | --- | --- | --- | --- | --- | --- |
| Issue intent | GitHub issue arnavloonker/maq-fabric-adlc#8 | repository | 2026-10-22 | issue body; no comments | Current `/approach` is structurally sound but lacks data-engineering context. | No detailed acceptance criteria in the issue. |
| Existing mode | `.apm\skills\approach\reference\data-model.md` | repository | 2026-10-22 | commit `391d813` baseline | The file says it serves data-product asks but concentrates on grain, keys, mappings, and ER design. | Repository-only observation. |
| Pipeline practice | https://learn.microsoft.com/en-us/fabric/data-factory/pipeline-overview | public documentation | 2026-10-22 | page updated 2026-02-03 | Pipelines include activities, triggers, parameters, success/failure conditions, monitoring, and run history. | Conceptual guidance, not project-specific behavior. |
| Lakehouse practice | https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-overview and https://learn.microsoft.com/en-us/fabric/onelake/onelake-medallion-lakehouse-architecture | public documentation | 2026-10-22 | pages updated 2026-08-26 and 2026-09-02 | Fabric data products can span ingestion, Delta layers, Spark/SQL engines, pipelines, and Power BI serving. | No live workspace validation. |
| Modeling practice | https://learn.microsoft.com/en-us/power-bi/guidance/star-schema | public documentation | 2026-10-22 | page updated 2026-04-01 | Fact grain, dimension relationships, keys, ETL, and semantic measures are linked design concerns. | Does not prescribe every Fabric data-product pattern. |

## Data profile (data asks)
Not applicable. This exploration changed skill guidance and did not inspect a live data product.

## Decisions
The recommended backward-compatible option was to retain `data-model` and add composable views. The user selected replacing `data-model` with `data-product`. `architecture` remains for shared platform boundaries and `experiment` remains for bounded learning.

## Candidate models and rejected alternatives
- Selected: three intent modes (`data-product`, `architecture`, `experiment`) with five composable data-product views.
- Rejected by user: retain `data-model` and add views.
- Rejected by user: add `data-product` as a fourth overlapping mode.
- Rejected during analysis: one mandatory end-to-end template, because it would duplicate irrelevant detail and obscure the consequential decisions.

## Experiments (if any)
None.

## Tool substitutions
GitHub CLI was used to read the issue and comments as required. Public Microsoft Learn pages were retrieved directly for the catalog entries consulted.

## Unknowns and blockers
- No live Fabric artifact was in scope, so the documentation views are design guidance rather than validation against a specific product.
- The repository separately contains inconsistent wording about an attached `approach.md` versus an inline Technical Approach section; this exploration did not choose a storage surface.
