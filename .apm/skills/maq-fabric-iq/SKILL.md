---
name: maq-fabric-iq
description: Use when a MAQ workflow skill needs Fabric IQ work on ontologies, graphs, planning, or data agent items, including previews, in DEV.
---
# MAQ Fabric IQ adapter

Internal adapter called by workflow skills such as /approach and /implement. Read [the procedure](reference/procedure.md).

Scope: Ontology, graph, planning, and agent item types as documented. Many are previews; check `capability-matrix.json` and the catalog snapshot before acting.

Rules:
- Create or change items only in approved DEV workspaces, within an approved change set.
- Flag preview status and known limitations in every report.
- Ontology queries are bounded and purpose-specific.
- If the operation is `planned`, `manual-only`, or `blocked`, or the companion skill is absent, stop and report the gap with the manual path. Never touch UAT or PROD.
