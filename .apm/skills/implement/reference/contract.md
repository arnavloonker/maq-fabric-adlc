# /implement contract

## Produces
Reviewed code, tests, and documentation for one story scope on a dedicated Git branch and worktree, with approved Fabric DEV authoring/execution, optionally a published PR linked to the work. Result goes to the repository, an optional PR, and a conversation report.

## Inputs
- Story ID (required) and optional selected task IDs; authorized repository; implementation scope.
- Story state: build-ready status, agreed `/approach` seam, blockers. A missing task list does not block an otherwise ready story. An unresolved consequential design choice blocks the affected implementation.
- `maq-project.toon` (ADO repository and Fabric DEV workspace identities) and `capability-matrix.json`. Resolve the repository default branch at runtime. Query bounds are fixed: stated purpose, 250 returned rows, 60-second timeout/budget where supported, no sensitive-row persistence.

## Adapter delegation
Delegate lakehouse, notebook, Spark job, and environment work to the spark-cli runtime companion. Delegate other artifact types to internal skills: maq-fabric-data-factory, maq-fabric-data-warehouse, maq-fabric-databases, maq-fabric-real-time-intelligence, maq-fabric-data-science, maq-fabric-power-bi, maq-fabric-iq, maq-fabric-industry-solutions, maq-fabric-platform. A runtime companion is not a packaged adapter. An operation with status `blocked`, `manual-only`, `planned`, or `deprecated` in the matrix, or lacking DEV evidence, is reported as blocked or manual-only with manual instructions; never improvised. Adapters get no broader authority than this skill.

## Output report
Exact commit, branch/worktree, Fabric workspace or prefix isolation used, TDD Red/Green evidence, PR if published, checks run, untested areas, outstanding blockers, and any tool substitutions.

## Approvals and stop gates
Each is tied to a concrete operation set, target, and payload; any change invalidates it. Distinct approvals: (1) approach for DEV authoring/execution and change set; (2) each commit; (3) each push; (4) PR creation; (5) each ADO comment/link/progress update. DEV execution approval is not authority to promote or deploy a release.
Stop when: the seam is missing, a design decision is open, a permission or tool is unavailable, the Git worktree cannot be isolated safely, a write times out and reconciliation is inconclusive, or publication would violate human-only closure.

## Prohibitions
- Never enable PR autocomplete, bypass branch/PR policies, merge, or auto-close or transition work items to done. Link PRs/commits without requesting closure.
- Never mutate UAT/PROD, promote, or deploy. A manual fallback may not instruct bypassing this.
- Never discard, reset, stash-drop, or overwrite existing or dirty work.
- Never commit secrets, tokens, connection strings, or raw sensitive query results.
- Never claim a practice was consulted when the lookup failed.
