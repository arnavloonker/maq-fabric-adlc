# /code-diff contract

## Inputs
- PR identity: repository and PR ID (or URL). Optional review iteration/version.
- Optional references: linked story, `/approach` specification, `/verify` evidence. Existing PR work-item relations may supply them.
- Platform identifiers from `maq-project.toon`: organization and project when ADO access is needed. Missing dependencies block only dependent operations.

## Outputs
- Markdown brief (see [brief template](brief-template.md)): what changed and why (when known), paired Before/After views, direct and downstream impact, intended versus verified outcomes, source links.
- Optional saved copy at `references\pull-requests\<repository-id>\<pr-id>\<review-version>.md`, only after approval.

## Before/After views
Choose one format per change, not every format for every change. Repeat the selected view for each meaningful change with its artifact/path and source links. Before = target (common) review commit; After = source review commit. Keep enough unchanged context to make the delta readable.

- **Structured table:** paired Before/After tables for schemas, settings, or mappings; bold added/changed values in After and label them `added` or `changed`. Label removals in Before and omit them from After.
- **Artifact/diagram:** paired Mermaid views for topology or data flow, with matching Before/After labels; highlight added/changed nodes using styles and textual labels. Removed nodes appear only in Before. This is a view of the artifact, not permission to publish a separate report.
- **Code blocks:** paired fenced `diff` blocks. Prefix unchanged lines with a space, removed/old versions with `-` only in Before, and added/new versions with `+` only in After. These are display markers, not source text; removed lines must not appear as current After content.

For creates/deletes, mark the absent side `not present` with evidence from the review diff. If content cannot be read, mark it `unavailable`, explain the coverage gap, and do not reconstruct it from assumptions. Highlighting never substitutes for provenance or implies runtime verification.

## Preferred tool bindings (reference profile; rediscover schemas, never invent arguments)
| Operation | Tool |
| --- | --- |
| PR metadata, linked work items | `azure-devops-repo_pull_request`: `get` |
| Review iterations, changes, diff baselines | `azure-devops-repo_pull_request`: `iterations` |
| Threads (context only) | `azure-devops-repo_pull_request_thread` |
| File content at a commit | `azure-devops-repo_file` |
| Linked story / criteria | `azure-devops-wit_work_item`: `get` |
| Linked builds (optional) | `azure-devops-pipelines_build` |
| Dependency evidence (optional) | `azure-devops-search_code`; direct Fabric companion skills in read-only scope |

## Safe substitutions
Allowed only when semantics, baseline, permissions, and evidence are equivalent; record the substitution in the brief. If the native review diff is unavailable, report that limitation; never substitute an unrelated branch-tip comparison.

## Rules
- Read-only on ADO and Fabric: no PR comments, approval votes, completion, work-item updates, or verification verdicts. Any requested external publication needs a preview and approval.
- Completed PRs use the recorded review/merge context, not current tips that may have moved.
- Label inferred lineage and impact; unknown relationships remain unknown.
- Do not invent business benefits or intent when references are absent.
- Static changes never prove runtime success; do not claim a Fabric job ran.
- Do not claim Mermaid rendering was checked unless it was rendered.
- Saving: preview the path and content; follow existing-file preview rules; save only when requested.
- No secrets or raw sensitive data in the brief.
