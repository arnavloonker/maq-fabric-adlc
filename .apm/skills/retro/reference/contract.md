# /retro contract

## Produces
A local markdown report, formatted as a GitHub issue, assessing how invoked MAQ skills performed versus the initial prompt and each skill's own contract. Optionally filed as an issue in this repository after approval.

## Inputs
- Skill names (default: every folder in `.apm\skills\`), time window (default 14 days), optional session IDs or repository filter.
- Each skill's `SKILL.md` and `reference\contract.md` as the baseline of what it promised.

## Per-run digest
`sessionId`, skill, date, initial prompt (redacted, truncated), contract promises, actions taken (tools, files, writes), artifacts produced, outcome, deviations.

## Reviewer verdicts
The `maq-adversarial-reviewer` is used unchanged, in a separate context, with the digest as evidence and the skill contract as criteria. Its `passed`, `failed`, `blocked`, `inconclusive` verdicts are reported as-is. No separate reviewer means `blocked`; never substitute the current context.

## Safety
- Read-only: never edit skills, commit, push, merge, or write to ADO.
- Evidence excludes secrets, tokens, connection strings and raw sensitive rows; quote short redacted excerpts only.
- Filing the issue needs approval of the exact `gh issue create` command, targeting this repository only.
- Only recorded sessions are visible; state coverage gaps.

## Outputs
`references\retros\<yyyyMMdd>\retro.md` (never overwrite; add a suffix) and, if approved, the created issue URL.
