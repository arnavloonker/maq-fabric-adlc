---
name: retro
description: Use when reviewing how MAQ skills performed in past sessions, comparing the initial prompt with what the skill did, and producing an issue-ready feedback report.
---
# Retro

Read [the contract](reference/contract.md) and [the procedure](reference/procedure.md).

Inputs: skill names (default all), time window (default 14 days), optional session IDs. Find runs with the [queries](reference/queries.md). Consult /best-practices when judging artifact quality.

Compare each run's initial prompt and the skill's contract with the actions taken. Dispatch maq-adversarial-reviewer in a separate context to challenge each digest; if it cannot launch, report blocked.

Write the report from the [issue template](reference/issue-template.md) to references\retros. Redact secrets and raw data.

Never edit skills, commit, or write to ADO. Preview the report, then file it as a GitHub issue in this repo only after approval of the exact command.
