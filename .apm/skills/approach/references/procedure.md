# Approach procedure

1. **Scope.** Resolve the Git consumer root, load only required platform identifiers from `maq-project.toon`, and confirm mode. TDD and verification rules are fixed by this skill. If the mode is absent, ask one question with a recommended mode.
2. **Read the story.** Use the discovered ADO work item tool (preferred: `azure-devops-wit_work_item` `get`, `list_comments`). Record the `System.Rev` read. Note the existing approach section, tags, and open questions.
3. **Context.** Load relevant exploration findings and domain records only. Reuse prior evidence; revalidate if stale, do not redo discovery to satisfy sequence.
4. **Best practices.** Consult /best-practices for each artifact type inspected or specified; read only the applicable links. Stay quiet about absent optional entries; report failed retrieval or consequential conflicts.
5. **Baseline validation.** Inspect the repository (record commit) and live Fabric artifacts through authorized, bounded reads. Prefer schema, definitions, and aggregates over raw rows; use partition filters or sample keys. Invoke the direct Fabric skills/tools listed for the operation in the capability matrix; if no supported binding exists, report `blocked` or `manual-only`.
6. **Grilling loop.** For each unresolved consequential decision or contradiction (duplicate keys, grain mismatch, Spark vs Warehouse, missing seam):
   - Ask exactly ONE question.
   - Include the evidence and a recommended answer.
   - Wait for the answer, record it, and re-evaluate before the next question.
   Never batch questions or decide silently.
7. **Specify.** Follow the mode file. Write before/after, artifact scope, dependencies, rollout/rollback. For data-product mode, select the relevant documentation views from [the mode guidance](modes/data-product.md), explain omissions, and keep source-to-Seam traceability explicit.
8. **Seam and contract.** Pick the single highest-level Seam; draft the Verification Contract (gold counts, key uniqueness, DAX measure with known value, fast-feedback window). Ask the user to approve or amend it, one question at a time.
9. **Preview.** Show the exact approach section diff and the intended tag change (add, keep, or remove). Approval covers this payload only; any change invalidates it.
10. **Write.** Update through the ADO write tool (preferred `azure-devops-wit_work_item_write` `update`) with the first operation a `Test` on `/rev` using the revision read. On conflict, reread, merge or re-preview, never overwrite. On timeout, read the item and compare to intent before retrying; if inconclusive, stop and report.
11. **Readiness tag.** Add `build-ready` only if decisions are resolved and the contract is approved. Remove it if any blocker reopens or the approved contract changes. Include the tag change in the same revision-checked update.
12. **Read back** the story; confirm section and tag state. Report URL, tag state, blockers, unvalidated assumptions. Do not close the work item.

Tool substitution is allowed only with equivalent semantics, scope, permissions, and approvals; note it in the report.
