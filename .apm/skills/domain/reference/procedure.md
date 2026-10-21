# /domain procedure

1. **Scope.** Identify the consumer root and the selected domains. If asked to discover boundaries, propose candidates by business responsibility and ownership, not by system, workspace, or layer, and get the user's selection before writing.
2. **Dependencies.** Read `maq-project.toon` only if live platform metadata is needed. Use fixed `domain\` and `references\` paths; read ownership from domain records. Missing dependencies block only dependent steps.
3. **Context.** Read `domain\index.md` and the existing record for each selected domain. Load relevant references and repository-local engineering standards only.
4. **Best practices.** Consult /best-practices for applicable artifact types. Report a failed lookup; never claim consultation that did not occur.
5. **Gather evidence (read-only).** Inspect repository sources: code, docs, schemas, definitions. Optionally validate against authorized live metadata or bounded data samples using discovered read-only tools. A read-only query tool is not equivalent to a generic SQL surface that can mutate. Lack of access yields an inconclusive observation, not fabricated support.
6. **Classify each finding.**
   - Vocabulary: business term, definition, synonyms. Strip implementation detail.
   - Source system or data product: name, owner if known, where it lives, link to authority.
   - Reviewed rule: only if a named reviewer and date exist in the source or are supplied by the user.
   - Provisional observation: anything inferred from code or data, with provenance.
   - Conflict: two claims that disagree; record both with sources.
7. **Compute an incremental update.** Compare to the existing file section by section. Add new entries; mark changed ones as new provisional observations or conflicts instead of overwriting. Never delete or reword human-reviewed content or text outside generated entries. Keep stable entry identifiers. Append to the change log with a collision-resistant run ID.
8. **Preview.** Show a diff for each existing file, including `domain\index.md`, and the full text of each new file. List targets exactly.
9. **Approval.** Obtain approval for that exact set. If the payload or target changes, preview again. Treat unresolved conflicts as stop conditions for any claim of "reviewed"; they may still be recorded.
10. **Write.** Create new files only where the path does not exist. Edit existing files by targeted edits against the version previewed; if the file changed since, reread and redo the preview.
11. **Read back.** Reread the files, confirm required sections are present, the vocabulary section has no implementation terms, and human edits remain.
12. **Report.** List files changed, new observations, open conflicts, unknown owners, and any local-only evidence marked as unpublished.

## Safety
No secrets, raw sensitive results, or connection strings in records. Keep scratch output ignored. Do not close or modify ADO items from this skill.
