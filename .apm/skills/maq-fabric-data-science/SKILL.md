---
name: maq-fabric-data-science
description: Use when a MAQ workflow skill needs Fabric Data Science work on experiments, models, or training and scoring workflows in DEV.
---
# MAQ Fabric Data Science adapter

Internal adapter called by workflow skills such as /approach, /implement, and /verify. Read [the procedure](reference/procedure.md).

Scope: ML experiments, models, and training/scoring workflows. Most item operations have no dedicated companion skill, so expect `manual-only` or `planned` in `capability-matrix.json`.

Rules:
- Run training, scoring, or registration only in approved DEV workspaces, within an approved change set.
- Include experiment cleanup in the approved scope.
- Use sampled or bounded data; never persist sensitive rows.
- If the operation is `planned`, `manual-only`, or `blocked`, stop and report the gap with the manual path. Never touch UAT or PROD.
