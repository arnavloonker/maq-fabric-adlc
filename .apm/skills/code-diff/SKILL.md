---
name: code-diff
description: Use when you need a plain-language impact brief for an Azure DevOps pull request, with Mermaid diagrams.
---
# Code diff

Read [the contract](reference/contract.md) and [the procedure](reference/procedure.md); fill [the brief template](reference/brief-template.md).

Inputs: PR identity, optional review iteration, optional story, approach, or verification references.
Consult /best-practices for the PR and affected artifact types.
Anchor to the PR's native review diff (get, iterations) at recorded baselines, never current branch tips.
Paginate; name unavailable, generated, binary, or truncated surfaces.

Gates: read-only on ADO. No comments, votes, work-item updates, or verdicts. Saving to references\pull-requests\<repo-id>\<pr-id>\<review-version>.md only after approval. Never claim Mermaid was rendered unless it was.

Output: Markdown brief with Mermaid: what changed, before/after topology, downstream impact, intended versus verified, sources. Label inference; unknown stays unknown.
