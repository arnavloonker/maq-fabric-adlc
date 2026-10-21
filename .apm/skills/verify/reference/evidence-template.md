# Verification evidence: story <story-id>

- Run ID: <yyyyMMddTHHmmssZ>-<6 hex>
- Run date-time (UTC): 
- Story: <ADO ID and URL>
- Target version: commit <sha>; artifacts <item ID + definition version/modified time>
- Environment: DEV (<workspace>)
- Contract origin: reused-from-approach | proposed-in-verify (approved by <name> at <time>)
- Reviewer: maq-adversarial-reviewer, separate context: yes | no
- Staleness recheck (UTC): <time>; target unchanged: yes | no
- Publication: local/unpublished | committed in <commit/PR> | attached to ADO
- Sensitivity handling: <what was aggregated, masked or excluded>

## Verdict
passed | failed | blocked | inconclusive: <one-sentence reason, limited to the contract>

## Criteria results
| Criterion | Check (tool/query identity) | Expected | Actual | Operation ID | Executed at (UTC) | Result |
| --- | --- | --- | --- | --- | --- | --- |

## Reviewer findings
Independent findings per criterion, including disagreements with the implementer's claims.

## Not tested / limitations
Untested criteria, access gaps, static-only reviews, tool substitutions.

## Reproduce
Exact commands or sanitized queries, parameters and data windows to rerun each check.

## Draft ADO comment
Verdict; version tested; criteria table (expected vs actual); untested areas; evidence location.

## results.json shape
```json
{
  "runId": "",
  "storyId": "",
  "verdict": "passed|failed|blocked|inconclusive",
  "target": { "commit": "", "artifacts": [] },
  "stale": false,
  "checks": [
    { "criterion": "", "expected": "", "actual": "", "tool": "", "operationId": "", "executedAt": "", "result": "pass|fail|skipped" }
  ],
  "untested": [],
  "publication": "local/unpublished"
}
```
