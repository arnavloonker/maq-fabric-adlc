---
name: maq-fabric-industry-solutions
description: Use when a MAQ workflow skill needs Fabric industry solution items and must check their prerequisites and support before any DEV work.
---
# MAQ Fabric Industry Solutions adapter

Internal adapter called by workflow skills such as /approach and /implement. Read [the procedure](reference/procedure.md).

Scope: Specific supported industry solutions and their items. No companion automation exists, so operations are `planned` or `manual-only` in `capability-matrix.json` until validated.

Rules:
- Confirm the solution and items against the chosen catalog snapshot; many are preview or tenant-gated.
- Report prerequisites, licensing, and capacity needs as findings, not assumptions.
- Any change is manual, in an approved DEV workspace only.
- Never touch UAT or PROD. Report `blocked` or `manual-only` with the reason.
