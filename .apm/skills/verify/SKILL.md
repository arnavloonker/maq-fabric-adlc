---
name: verify
description: Use when independently verifying an implemented Azure DevOps story against its approved Verification Contract.
---
# Verify

Read [the outcome](references/outcome.md), [the procedure](references/procedure.md), and [the evidence template](references/evidence-template.md).

Inputs: story ID and exact commit or artifact versions. Load platform identifiers from `maq-project.toon` and relevant domain records. Consult /best-practices for each artifact type reviewed.

Reuse the approach's approved contract and seam. If missing or changed, propose one and get approval.

Recommend lower-environment runtimes (DEV or explicitly approved UAT) from `maq-project.toon`. Honor engineer-approved prompted targets within governing safety. Discover installed companion skills through `capability-matrix.json`; neither `planned` status nor missing isolation alone blocks approved validation.

Trigger real artifact execution, poll to terminal state, then reconcile quantitative seam and upstream checks. Capture runtime proof in `executions[]` and reconciliation proof in `checks[]`. Static review alone never passes.

Dispatch maq-adversarial-reviewer in a separate context.

Stop when approval, reviewer, permissions, or target version are missing. Never fix code silently, merge, or close work. Recheck versions before publishing; drift makes evidence stale.

Report passed, failed, blocked, or inconclusive using the Validation Report template. Preview the ADO comment, post after approval, and save evidence under references\stories.
