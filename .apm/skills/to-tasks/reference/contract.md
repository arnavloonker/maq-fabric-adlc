# /to-tasks contract

## Produces
Outcome-based ADO child tasks under one story, with dependency links. Result goes to ADO; a summary with URLs and blockers goes to the conversation.

## Inputs
- Story ID (required). Current approach section, agreed test seam, and draft verification contract (read from the story).
- ADO identifiers and placement paths from `maq-project.toon`. Use the native `Task` type. Tasks are vertical end-to-end tracer bullets sized to one context window, never horizontal layer-only slices. Ask one granularity question at a time with a recommended answer until approved. Consult repository-local engineering guidance when present.
- Optional: engineer preferences on granularity.

## Slice rules
- A task is a thin vertical tracer-bullet: one entity, metric, or capability end-to-end across bronze, silver, gold, semantic model, and report (or across the relevant architectural seam for non-data work).
- Horizontal tasks by medallion layer ("all bronze, then all silver") are forbidden. Reject and re-slice any such proposal.
- Each task fits a single fresh context window; split a slice that does not.
- Every task records: scope, expected artifacts (create/update/remove/no-change), a fast seam-test check, dependencies, and evidence expectations.
- Dependencies are only real prerequisites; independent slices stay independent.

## Approvals and stop gates
- Granularity is approved by the engineer through the quiz loop before any preview.
- Creation and link writes need approval of the exact preview (targets, titles, bodies, links). Any change to payload, parent, or links invalidates approval.
- Stop and report if: the story has no agreed seam or has open consequential decisions; required ADO tools or link types are unavailable; reconciliation is inconclusive.
- A missing task list never blocks `/implement`; this skill is optional.

## Work-item HTML
Task description uses the allowed HTML set from the safety rules. Do not write Markdown into that field. Preview the rendered field.

## Prohibitions
- Never invent scope absent from the story. Never resolve consequential decisions silently.
- Never duplicate, edit, reparent, or close existing tasks. Humans decide state closure.
- Never mutate anything outside the story's child tasks and their links. UAT/PROD are never targets.
- Never put secrets or raw sensitive data in task text.
