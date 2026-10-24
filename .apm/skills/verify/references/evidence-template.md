# Validation Report: story <story-id>

## 1. Executive Summary & Verdict Banner

**VERDICT: passed | failed | blocked | inconclusive**

<One sentence explaining the business/technical outcome and its proof or limitation.>

- Run ID: <yyyyMMddTHHmmssZ>-<6 hex>
- Run date-time (UTC): 
- Story: <ADO ID and URL>
- Target version: commit <sha>; artifacts <item ID + definition version/modified time>
- Target environment/workspace: <environment, workspace name and ID; execution or read-only scope>
- Contract origin: reused-from-approach | proposed-in-verify (approved by <name> at <time>)
- Reviewer: maq-adversarial-reviewer, separate context: yes | no
- Staleness recheck (UTC): <time>; target unchanged: yes | no
- Publication: local/unpublished | committed in <commit/PR> | attached to ADO
- Sensitivity handling: <what was aggregated, masked or excluded>

`passed` requires both proof tiers at the current approved target version and completed independent review. A static code/definition review, submission receipt, or skipped check cannot establish success.

## 2. Runtime Execution Proof Table

| Artifact | Type | Workspace/Env | Skill/Tool | Run/Job ID | Duration (UTC start → end) | Status |
| --- | --- | --- | --- | --- | --- | --- |
| <name; item ID; definition version/timestamp> | <itemType> | <workspace ID; env> | <skill; actual tool> | <run/job/operation ID> | <seconds; start UTC → end UTC> | <Succeeded / Completed / Failed; raw status if different> |

Include every required runtime operation, not just the successful ones. For SQL/DAX, use the actual query operation ID. Mark missing IDs or nonterminal outcomes explicitly; never invent a terminal status. Record polling deadline, last observed state and failures. Link these executions to reconciliation checks.

## 3. Seam & Acceptance Criteria Reconciliation Table

| Criterion | Check / Query | Expected | Actual | Delta / Tolerance | Operation ID | Result |
| --- | --- | --- | --- | --- | --- | --- |
| <criterion ID; boundary> | <sanitized query/command or reproducibility anchor; execution ID> | <numeric value; unit> | <observed value; unit> | <actual minus expected; approved absolute/relative tolerance> | <query/operation ID; UTC start/end> | <pass / fail / skipped> |

Use the same approved version, source snapshot/window and parameters for both tiers. Explain categorical schema checks alongside quantitative mismatch counts. Missing required checks prevent `passed`.

## 4. Data Quality & Grain Verification

- Source-to-target: <source count, filters/join effects, target count, rejects/quarantine, count equation and unexplained delta>.
- Key uniqueness/grain: <declared grain, total vs distinct keys, duplicate count, expected vs actual>.
- Schema/null boundaries: <required types/columns, schema mismatch count, null counts/rates and tolerances>.
- Measures: <SQL/DAX aggregate, units, expected vs actual, delta/tolerance>.
- Link each finding to its criterion, execution and query operation IDs; explain inapplicable checks.

## 5. Independent Adversarial Review (`maq-adversarial-reviewer`)

<Separate-context reviewer identity/session reference, exact target version and completion time.>

<Challenge summary per criterion; agreements and disagreements with implementer claims, evidence considered, resolutions and unresolved findings. No same-context substitute.>

## 6. Risks, Untested Scope & Limitations

<Skipped checks, missing execution proof, access gaps, static-only findings, tool substitutions, matrix status, isolation mode/rationale, polling/query limits, environment restrictions and stale evidence. Distinguish approved DEV or explicitly approved UAT execution from read-only target observations; PROD remains read-only.>

## 7. Reproducibility Guide

<Exact skill/tool commands as executed, sanitized SQL/DAX/other queries, artifact IDs/versions, environment/workspace, parameters, UTC filter windows/source snapshots, budgets, polling commands and approved cleanup. Retain placeholders for redacted sensitive values; never include secrets or raw sensitive rows.>

## ADO comment preview

Render sections 1–7 above with populated tables and explanations as the complete comment, including run ID, staleness recheck, and published evidence link or explicit `local/unpublished` path. Do not replace the report with an outline or require readers to open local files. Preview the exact sanitized comment and obtain approval before posting.

## results.json shape
```json
{
  "runId": "",
  "storyId": "",
  "verdict": "passed|failed|blocked|inconclusive",
  "target": {
    "commit": "",
    "environment": "",
    "workspaceId": "",
    "artifacts": [
      { "artifactName": "", "itemId": "", "itemType": "", "definitionVersion": "", "modifiedAtUtc": "" }
    ]
  },
  "stale": false,
  "stalenessCheckedAtUtc": "",
  "executions": [
    {
      "artifactName": "",
      "itemId": "",
      "itemType": "",
      "definitionVersion": "",
      "modifiedAtUtc": "",
      "runtimeSkill": "",
      "tool": "",
      "environment": "",
      "workspaceId": "",
      "operationId": "",
      "operationKind": "run|job|refresh|query|ingestion",
      "startedAtUtc": "",
      "endedAtUtc": null,
      "durationSeconds": null,
      "terminalStatus": null,
      "rawStatus": ""
    }
  ],
  "checks": [
    {
      "criterion": "",
      "boundary": "",
      "executionIds": [],
      "targetVersion": "",
      "environment": "",
      "workspaceId": "",
      "expected": null,
      "actual": null,
      "unit": "",
      "delta": null,
      "tolerance": { "kind": "absolute|relative", "value": 0 },
      "runtimeSkill": "",
      "tool": "",
      "sanitizedQueryOrCommand": "",
      "parameters": {},
      "filterWindowUtc": { "start": "", "end": "" },
      "operationId": "",
      "startedAtUtc": "",
      "endedAtUtc": "",
      "result": "pass|fail|skipped",
      "reason": ""
    }
  ],
  "reviewer": {
    "agent": "maq-adversarial-reviewer",
    "separateContext": true,
    "sessionReference": "",
    "targetVersion": "",
    "agreements": [],
    "disagreements": [],
    "unresolvedFindings": []
  },
  "untested": [],
  "limitations": [],
  "publication": "local/unpublished"
}
```

`terminalStatus` is `Succeeded`, `Completed`, or `Failed` only after a terminal response; otherwise leave it null and explain the incomplete execution. Normalize cancelled terminal runs to `Failed` while retaining `rawStatus`. Use numeric expected/actual/delta values and approved tolerance for quantitative checks; missing observations remain null. IDs in `checks[].executionIds` reference `executions[].operationId`. Record only observed evidence, not the illustrative placeholders.
