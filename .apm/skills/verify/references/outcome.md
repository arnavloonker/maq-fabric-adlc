# /verify outcome

## Produces
An independent verdict on one story at one exact version, supported by two-tier runtime and reconciliation proof within the approved Verification Contract. Produce a human-readable Validation Report, a matching previewed ADO story comment, and a local evidence record.

## Inputs
- Story ID (required) and the exact version under review: Git commit SHA and, for live artifacts, item ID plus definition version or last-modified timestamp.
- The approved Verification Contract and seam from the story's `/approach` section. An explicit contract supplied by the engineer is accepted if `/approach` was bypassed.
- Optional: PR ID, task IDs, relevant domain records.
- Requested target environment/workspace and explicit engineer approval of its concrete execution and check operations.

## Verification Contract (contract.json)
Fields: `storyId`, `origin` (`reused-from-approach` | `proposed-in-verify`), `seam`, `criteria[]` (id, expected result, check, tolerance), `target` (commit, artifact names, item IDs, item types, definition versions/timestamps), `environment`, `workspaceId`, `permittedExecutions[]`, `permittedChecks[]`, `dataLimits` (row caps, partitions/windows, timeout), `expectedEvidence` (both tiers and criterion coverage), `cleanup`, `approvedBy`, `approvedAt`.

Rules:
- Reuse the approach contract by default. Propose a new one only when none exists or scope/criteria changed; any change needs renewed engineer approval.
- Approval covers one concrete operation set, target and version. A changed payload, target, environment or plan invalidates it.
- Recommend lower-environment runtimes identified in `maq-project.toon`: DEV by default, or UAT for explicitly requested, concretely approved validation under governing safety. Resolve prompted workspaces/environments and obtain exact engineer approval rather than silently substituting a target. PROD remains read-only; never claim reads prove a job ran there.
- Recommend a branch workspace or shared lower-environment `<branch_slug>_` prefix. When the engineer explicitly approves an existing workspace/unprefixed artifact, record the live target, rationale and isolation mode (`branch-workspace`, `shared-prefix`, or `user-directed-target`) and help execute it. Missing workspace isolation alone is not a refusal gate.
- A `planned` capability row is not itself a blocker. Discover the installed runtime skill and validate live support, prerequisites and permissions before approved execution. If no supported path exists, report the actual blocker; target approval is not permission to bypass identity, access or production restrictions.

## Two-tier proof
- **Tier 1 — Runtime Execution Proof (`executions[]`).** Actively execute the approved artifact through its installed companion skill. Record artifact name and item ID, itemType, definition version/timestamp, runtime skill and tool, environment and workspace ID, run/job/operation ID, start/end UTC, duration, and terminal status (`Succeeded`, `Completed`, or `Failed`). Preserve the provider's raw status separately when normalizing; cancellation is unsuccessful, never `Completed`. A pending or unknown outcome has no terminal status and prevents `passed`.
- Poll asynchronous jobs, refreshes, and operations to terminal state before seam checks. Synchronous SQL/DAX executions require a returned query/operation ID and completion evidence, not an invented job ID. Definition inspection or a successful submission alone is not execution proof.
- **Tier 2 — Seam & Reconciliation Proof (`checks[]`).** Record criterion, linked execution IDs, upstream/seam boundary, sanitized query or command, tool, environment/workspace, expected and actual quantitative values, delta, approved tolerance, operation ID, start/end UTC, and result. Cover source-to-target counts, rejects/quarantine, key uniqueness and grain, schema/null boundaries, and DAX/SQL aggregates as applicable; justify exclusions.
- Both tiers must identify the current approved target version and the same data window/parameters. Explain count equations, join/filter effects, duplicates, units, and tolerances rather than assuming every source count equals its target count.

## Verdicts
- `passed`: all required artifact executions succeeded/completed, every criterion reconciles within its approved tolerance at the current target version, and the independent reviewer has no unresolved finding that invalidates those claims.
- `failed`: an approved artifact execution failed or a required check violates its expected value/tolerance.
- `blocked`: approval, permission, tool, target version or separate reviewer is unavailable.
- `inconclusive`: checks partially ran, results ambiguous, or evidence is stale.
A static code/definition review alone can never produce `passed`. Missing permissions, partial tests, missing either proof tier, or an absent reviewer can never yield `passed`. Record demonstrated failures even when other criteria are blocked or inconclusive; never treat skipped or stale evidence as success.

## Safety
- The reviewer runs in a separate context; a same-context substitute is never claimed as independent.
- Never fix code, approve/merge a PR, close or change the state of a work item.
- Formal ADO Test Case creation needs separately approved scope.
- Evidence excludes secrets, tokens, connection strings and raw sensitive rows; use aggregates.
- Preview before every external write (ADO comment, repository commit, attachment).

## Outputs
- `references\stories\<story-id>\verification\<run-id>\contract.json`, `evidence.md`, `results.json` (see [template](evidence-template.md)).
- Previewed ADO comment via `azure-devops-wit_work_item_comment_write` action `add`.
- Both report and comment use the template's seven sections: Executive Summary & Verdict Banner; Runtime Execution Proof Table; Seam & Acceptance Criteria Reconciliation Table; Data Quality & Grain Verification; Independent Adversarial Review; Risks, Untested Scope & Limitations; Reproducibility Guide.
