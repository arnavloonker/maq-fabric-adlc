# /code-diff contract

## Inputs
- PR identity: repository and PR ID (or URL). Optional review iteration/version.
- Optional references: linked story, `/approach` specification, `/verify` evidence. Existing PR work-item relations may supply them.
- Platform identifiers from `maq-project.toon`: organization and project when ADO access is needed. Missing dependencies block only dependent operations.

## Outputs
- Markdown brief with Mermaid only (see `brief-template.md`): what changed and why (when known), before/after topology, direct and downstream impact, intended versus verified outcomes, source links.
- Optional saved copy at `references\pull-requests\<repository-id>\<pr-id>\<review-version>.md`, only after approval.

## Preferred tool bindings (reference profile; rediscover schemas, never invent arguments)
| Operation | Tool |
| --- | --- |
| PR metadata, linked work items | `azure-devops-repo_pull_request`: `get` |
| Review iterations, changes, diff baselines | `azure-devops-repo_pull_request`: `iterations` |
| Threads (context only) | `azure-devops-repo_pull_request_thread` |
| Approved brief comment | `azure-devops-repo_pull_request_thread_write` |
| File content at a commit | `azure-devops-repo_file` |
| Linked story / criteria | `azure-devops-wit_work_item`: `get` |
| Linked builds (optional) | `azure-devops-pipelines_build` |
| Dependency evidence (optional) | `azure-devops-search_code`; Fabric adapters read-only |

## Safe substitutions
Allowed only when semantics, baseline, permissions, and evidence are equivalent; record the substitution in the brief. If the native review diff is unavailable, report that limitation; never substitute an unrelated branch-tip comparison.

## Rules
- The default is read-only until a separate approval. That approval posts one Markdown pull-request comment containing the finished brief, and nothing else. No approval votes, completion, work-item updates, or verification verdicts.
- Completed PRs use the recorded review/merge context, not current tips that may have moved.
- Label inferred lineage and impact; unknown relationships remain unknown.
- Do not invent business benefits or intent when references are absent.
- Static changes never prove runtime success; do not claim a Fabric job ran.
- Do not claim Mermaid rendering was checked unless it was rendered.
- Saving: preview the path and content; follow existing-file preview rules; save only when requested.
- No secrets or raw sensitive data in the brief.
