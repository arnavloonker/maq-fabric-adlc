---
name: domain
description: Use when creating or incrementally updating business domain records and the domain index for a Fabric project.
---
# Domain

Read [the contract](reference/contract.md) and [the procedure](reference/procedure.md). Start from [the template](reference/domain-template.md).

Inputs: selected domains, or a request to discover candidate business boundaries.
Load project configuration and only relevant domain records and references.
Consult /best-practices for applicable artifact types.

Inspect repository sources and existing records. Optionally validate against authorized live metadata; discover available tools and prefer read-only ones.

Keep vocabulary free of implementation details. Separate source systems, data products, reviewed rules, provisional observations, and explicit conflicts. Never treat code behavior as business policy.

Stop gates: preview a diff of every existing-file change, including the index, and get approval for that exact set. A changed target or payload invalidates approval. Stop on unresolved conflicts you cannot attribute. Never overwrite human edits or store secrets or raw sensitive data.

Output: `domain\<business-domain>.md` plus `domain\index.md`. Read back, then report changed files and open conflicts.
