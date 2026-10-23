# /retro procedure

1. **Scope.** Resolve repository root via Git. Confirm skill list, window and filters with the engineer. Reject paths escaping the root.
2. **Baseline.** Read each target skill's `SKILL.md` and `reference\contract.md`. Consult /best-practices for artifact types involved.
3. **Discover runs.** Use [queries](queries.md) with `session_store_sql`, always time-bound with LIMIT. Record coverage (sessions scanned, runs found, skills with zero runs). If the store is unavailable, report `blocked`.
4. **Digest.** Per run, fetch the turns after the invocation and build the digest defined in the [contract](contract.md): initial prompt, promised outputs, actions, artifacts, outcome. Redact secrets, PATs, connection strings, sensitive rows.
5. **Compare.** For each run list: prompt intent vs what the skill did, contract promises met/missed, safety rule breaches (non-DEV mutation, unapproved writes, auto-complete, state changes), unnecessary steps, user corrections or retries.
6. **Dispatch reviewer.** Launch `maq-adversarial-reviewer` in a separate context per run (or small batch) with digest, skill contract and the comparison. It tries to falsify the comparison. If it cannot be launched, verdict `blocked`; do not substitute the current context.
7. **Aggregate.** Group findings per skill; rank recurring patterns; propose concrete edits to the skill's `reference\` files (suggestions only).
8. **Write.** Fill the [issue template](issue-template.md); save to `references\retros\<yyyyMMdd>\retro.md` without overwriting.
9. **Preview.** Show the report and the exact `gh issue create --repo <this repo> --title ... --body-file ...` command. Wait for approval.
10. **File.** Run only the approved command. Report the issue URL. Never edit skills, commit, or push.
