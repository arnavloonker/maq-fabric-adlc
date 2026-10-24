---
name: approach
description: Use when a story needs a build-ready before/after technical approach and draft Verification Contract in data-product, platform, or experiment mode.
---
# Approach

Produces the story's approach section: before/after spec, single highest-level Seam, draft Verification Contract. Inputs: story ID, mode.

Read [the outcome](references/outcome.md) and [the procedure](references/procedure.md), then the mode file: [data-product](references/modes/data-product.md), [platform](references/modes/platform.md), or [experiment](references/modes/experiment.md).

Load `maq-project.toon` only for required platform identifiers and relevant domain records and findings. Consult /best-practices for each artifact type inspected or specified.

Validate the baseline against the repository and live Fabric artifacts. Ask one question at a time, each with a recommended answer, when evidence contradicts an assumption.

Stop gates:
- Preview the exact story update; obtain approval before writing.
- Update with a revision check; on conflict, reread and re-preview.
- Apply `build-ready` only when all consequential decisions are resolved and the contract is approved; remove it if blockers reopen.
- Recommend DEV experiments with branch-workspace or `<branch_slug>_` isolation. Honor explicitly prompted lower-environment targets, including UAT validation or unprefixed artifacts, with concrete approval; record target mode and rationale. Never mutate PROD or close work items.

Report the story URL, tag state, and open blockers.
