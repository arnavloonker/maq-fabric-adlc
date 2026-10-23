# /implement outcome

## Produces
Reviewed code, tests, and documentation for one story scope on a dedicated Git branch and worktree, with approved Fabric lower-environment authoring/execution (DEV recommended; UAT only for explicitly prompted validation), optionally a published PR linked to the work. Result goes to the repository, an optional PR, and a conversation report.

## Inputs
- Story ID (required) and optional selected task IDs; authorized repository; implementation scope.
- Story state: build-ready status, agreed `/approach` seam, blockers. A missing task list does not block an otherwise ready story. An unresolved consequential design choice blocks the affected implementation.
- `maq-project.toon` (ADO repository and Fabric workspace identities), any explicitly requested target, and `capability-matrix.json`. Verify live environment and permissions. Resolve the repository default branch at runtime. Query bounds are fixed: stated purpose, 250 returned rows, 60-second timeout/budget where supported, no sensitive-row persistence.

## Direct Fabric skills
Use the `runtimeSkills` and `toolBindings` for the artifact type in the capability matrix and invoke the installed Fabric skill directly; there is no internal adapter layer. Execute and validate `planned` and `validated-dev` rows in the approved lower-environment runtime. Missing prior DEV evidence or unverified `branchWorkspaceSupport` is not a block. Report blocked/manual-only only when no runtime skill/tool binding exists or required access is genuinely missing; never improvise a binding or claim validation not performed. Direct skills get no broader authority than this skill.

## Output report
Exact commit, branch/worktree, Fabric workspace/environment, target mode (`branch-workspace`, `shared-prefix`, or `user-directed-target`), prefix if used, user approval and rationale for a non-default target, TDD Red/Green evidence, PR if published, checks run, untested areas, outstanding blockers, and any tool substitutions.

## Approvals and stop gates
Each is tied to a concrete operation set, target, and payload; any change invalidates it. Distinct approvals: (1) approach for lower-environment authoring/execution and change set; (2) each commit; (3) each push; (4) PR creation; (5) each ADO comment/link/progress update. Recommend DEV and branch-workspace or `<branch_slug>_` isolation. Honor an explicitly prompted lower-environment workspace or existing/unprefixed artifact after concrete approval, recording the target and rationale instead of hard-blocking. UAT execution is limited to explicitly requested validation. Execution approval is not authority to promote or deploy a release.
Stop when: the seam is missing, a design decision is open, a permission or tool is unavailable, the Git worktree cannot be isolated safely, a write times out and reconciliation is inconclusive, or publication would violate human-only closure.

## Prohibitions
- Never enable PR autocomplete, bypass branch/PR policies, merge, or auto-close or transition work items to done. Link PRs/commits without requesting closure.
- Never mutate PROD, promote, or deploy. UAT is read-only except explicitly prompted, concretely approved lower-environment validation. A manual fallback may not instruct bypassing this.
- Never discard, reset, stash-drop, or overwrite existing or dirty work.
- Never commit secrets, tokens, connection strings, or raw sensitive query results.
- Never claim a practice was consulted when the lookup failed.
