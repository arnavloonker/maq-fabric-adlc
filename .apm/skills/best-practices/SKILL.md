---
name: best-practices
description: Use when another skill or a user needs guidance links for a Fabric or Azure DevOps artifact type, or wants to propose a catalog addition or update.
---
# Best practices

Read [the outcome](references/outcome.md) and [the procedure](references/procedure.md).

Inputs: mode (consult, propose-add, propose-update), artifact type, optional source link.

Consult: read only the matching group in [the catalog](references/catalog.md), then retrieve only relevant linked pages. Apply fetched content, never link titles. Stay silent when an optional entry is absent. Surface retrieval failures and consequential conflicts. Never claim consultation that did not happen. Never invoke this skill recursively or load the whole catalog.

Propose: resolve the installed APM dependency source and pinned revision. Draft the link change against that source, preview, and publish a pull request only after approval. If source resolution or access fails, return a patch and state nothing was updated.

Never keep a project-local catalog, edit installed resources, merge, or update consumer pins.

Report the entries consulted, failures, conflicts, or the proposal link or patch.
