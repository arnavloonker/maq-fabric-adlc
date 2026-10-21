# /verify contract

## Produces
An independent verdict on one story at one exact version, limited to the approved Verification Contract, plus a previewed ADO story comment and a local evidence record.

## Inputs
- Story ID (required) and the exact version under review: Git commit SHA and, for live artifacts, item ID plus definition version or last-modified timestamp.
- The approved Verification Contract and seam from the story's `/approach` section. An explicit contract supplied by the engineer is accepted if `/approach` was bypassed.
- Optional: PR ID, task IDs, relevant domain records.

## Verification Contract (contract.json)
Fields: `storyId`, `origin` (`reused-from-approach` | `proposed-in-verify`), `seam`, `criteria[]` (id, expected result, check), `target` (commit, artifact versions), `environment` (DEV only), `permittedChecks[]`, `dataLimits` (row caps, partitions/windows, timeout), `expectedEvidence`, `cleanup`, `approvedBy`, `approvedAt`.

Rules:
- Reuse the approach contract by default. Propose a new one only when none exists or scope/criteria changed; any change needs renewed engineer approval.
- Approval covers one concrete operation set, target and version. A changed payload, target, environment or plan invalidates it.
- Checks run only in DEV. UAT/PROD may be read within authorized scope, never mutated.

## Verdicts
- `passed`: every criterion met by executed evidence at the current version.
- `failed`: at least one criterion has actual != expected.
- `blocked`: approval, permission, tool, target version or separate reviewer is unavailable.
- `inconclusive`: checks partially ran, results ambiguous, or evidence is stale.
A static review is not evidence that a Fabric job or query ran. Missing permissions, partial tests or an absent reviewer can never yield `passed`.

## Safety
- The reviewer runs in a separate context; a same-context substitute is never claimed as independent.
- Never fix code, approve/merge a PR, close or change the state of a work item.
- Formal ADO Test Case creation needs separately approved scope.
- Evidence excludes secrets, tokens, connection strings and raw sensitive rows; use aggregates.
- Preview before every external write (ADO comment, repository commit, attachment).

## Outputs
- `references\stories\<story-id>\verification\<run-id>\contract.json`, `evidence.md`, `results.json` (see [template](evidence-template.md)).
- Previewed ADO comment via `azure-devops-wit_work_item_comment_write` action `add`.
