# /implement procedure

## 1. Scope and context
1. Resolve the consumer repository root via Git; load required platform identifiers from `maq-project.toon` and `capability-matrix.json`. Missing dependencies block only dependent steps.
2. Read the story, selected tasks, comments, build-ready status, agreed `/approach` seam, and blockers (`azure-devops-wit_work_item`: `get`, `list_comments`). Stop and recommend `/approach` if no seam exists; `/domain` or `/brainstorm` for open decisions.
3. Load only relevant domain records and references.

## 2. Git isolation
1. Inspect `git status`, `git worktree list`, current branch, and stashes. Record dirty state.
2. Derive `<branch_slug>` deterministically from the story ID and title (lowercase, `[a-z0-9_]`, no leading digit, max 40 chars), for example `s1234_orders_gold`.
3. Resolve the ADO repository's default branch at runtime and create a dedicated branch from it in a new worktree beside the repo (`git worktree add`). Reuse an existing worktree for the same scope. Never reset, clean, checkout over, or stash-drop dirty work; if the primary tree is dirty, leave it untouched and work only in the new worktree.
4. Record branch, worktree path, and base commit.

## 3. Fabric DEV isolation
Follow [DEV isolation](dev-isolation.md). Record the mode chosen and why.

## 4. /best-practices consultation
For each artifact type to be authored or changed (for example notebook, pipeline, warehouse SQL, semantic model, report, Eventstream/KQL, PR, ADO progress comment), consult /best-practices on demand, loading only applicable linked pages. Apply them. Report a failed lookup or unchecked required standard; stay quiet on an absent optional entry. Do not recurse. Catalog guidance never overrides approved requirements or safety rules.

## 5. Discover tools and direct Fabric skills
Read MCP/tool and installed-skill schemas; do not guess argument shapes. Match each artifact operation to a matrix row (workload, itemType, operation), then invoke the listed runtime skills and tool bindings directly. If no supported binding is listed, report the operation as blocked/manual-only instead of improvising. Substitute a tool only with equivalent semantics, scope, permissions, approval boundary, and evidence; record it.

## 6. Plan and approve
Preview the change set: files, Fabric items/operations with target workspace or prefix, DEV executions, seam tests, and expected publication. Obtain explicit approval for DEV authoring/execution. Re-preview if anything changes. Unsupported operations are listed as blocked/manual-only.

## 7. Fast-feedback Red-Green TDD loop (per slice, anchored to the seam)
1. Write the smallest fast executable seam test first. Data asks: partition filters, sample keys, or bounded windows; enforce query timeouts/budgets where the surface supports them (a row limit alone does not bound scan cost); prefer schema/aggregate evidence over raw rows. Architectural changes: narrow parameter windows.
2. Run it and confirm Red for the expected reason. Capture the command and result.
3. Implement the slice through the listed direct Fabric skill/tool; write documentation with it.
4. Re-run until Green. Then run relevant broader checks. Capture evidence without raw sensitive rows.
5. Medallion layers apply only to relevant data-product work; slices stay vertical.
A test that cannot be run because its direct skill/tool is unavailable is reported as untested, not passed.

## 8. Publish (each step separately approved)
1. Show the diff summary and proposed commit message; commit after approval, only the approved files. Never commit secrets or scratch output.
2. Preview and, after approval, push the branch. Never force-push shared branches.
3. Preview the PR (title, description within the server limit, base, reviewers) and create it after approval with `azure-devops-repo_pull_request_write`. Do not set autocomplete or work-item transitions. Inspect repository automation for indirect state transitions; if publication would close work, report the conflict and stop before publishing.
4. Link the PR/commit to the work item (`link_to_pull_request`, `add_artifact_link`) and, after approval of the exact text, add a progress comment with a readable summary. Revision-check any field updates; never change state.

## 9. Timeout reconciliation
Never blindly repeat a write. Inspect branches, PRs, comments, links, or Fabric operations by scoped identifiers and recorded intent. If inconclusive, stop and report uncertainty.

## 10. Report
Re-read published state. Report exact commit, branch/worktree, isolation used, TDD Red/Green evidence, PR URL if published, checks, untested areas, substitutions, and blockers. A PR is not proof of deployment or data execution. Do not close anything.
