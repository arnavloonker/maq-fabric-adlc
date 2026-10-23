---
name: approach
description: Use when a story needs a build-ready before/after technical approach and draft Verification Contract in data-product, platform, or experiment mode.
---
# Approach

Produces the story's approach section: before/after spec, single highest-level Seam, draft Verification Contract. Inputs: story ID, mode.

Read [contract](reference/contract.md) and [procedure](reference/procedure.md), then the mode file: [data-product](reference/data-product.md), [platform](reference/platform.md), or [experiment](reference/experiment.md).

Load `maq-project.toon` only for required platform identifiers and relevant domain records and findings. Consult /best-practices for each artifact type inspected or specified.

Validate the baseline against the repository and live Fabric artifacts. Ask one question at a time, each with a recommended answer, when evidence contradicts an assumption.

Stop gates:
- Preview the exact story update; obtain approval before writing.
- Update with a revision check; on conflict, reread and re-preview.
- Apply `build-ready` only when all consequential decisions are resolved and the contract is approved; remove it if blockers reopen.
- Mutate nothing in Fabric except approved DEV experiments; never touch UAT/PROD; never close work items.

Report the story URL, tag state, and open blockers.
