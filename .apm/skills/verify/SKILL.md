---
name: verify
description: Use when independently verifying an implemented Azure DevOps story against its approved Verification Contract.
---
# Verify

Read [the contract](reference/contract.md) and [the procedure](reference/procedure.md).

Inputs: story ID and exact commit or artifact versions. Load project configuration and relevant domain records. Consult /best-practices for each artifact type reviewed.

Reuse the approach's approved contract and seam. If missing or changed, propose one and get approval.

Dispatch maq-adversarial-reviewer in a separate context. Run only permitted seam checks, in DEV.

Stop when approval, reviewer, permissions, or target version are missing. Never fix code silently, merge, or close work. Recheck versions before publishing; drift makes evidence stale.

Report passed, failed, blocked, or inconclusive. Preview the ADO comment, post after approval, and save evidence under references\stories.
