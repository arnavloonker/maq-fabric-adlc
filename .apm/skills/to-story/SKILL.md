---
name: to-story
description: Use when turning an agreed discussion or exploration into an Azure DevOps User Story, or refreshing an existing one.
---
# To story

Read [the outcome](references/outcome.md) and [the procedure](references/procedure.md).

Inputs: conversation or selected exploration, optional story ID.
Load platform identifiers from `maq-project.toon` and only relevant domain records and references.
Consult /best-practices for User Story guidance before drafting fields.
Extract intent, evidence, acceptance criteria, decisions, and blocking questions.
Never invent business context or resolve consequential decisions silently.

Discover available Azure DevOps tools, read type metadata, search related work, then preview the full field change set.

Stop gates: no ADO write without approval of the exact previewed payload; a changed payload, target, or revision invalidates it. Stop if a write timeout cannot be reconciled.

Preserve existing content, especially Technical Approach. Revision-check updates. Apply `platform`, `data-engineering`, or `experiment` when applicable.

Output: read back the story, report its URL and unresolved blockers in chat. Never close it.
