# /to-story procedure

1. **Scope.** Identify the source (conversation, exploration findings, or both) and whether a story ID was given. Direct invocation without `/brainstorm` is valid; work from supplied evidence.
2. **Configuration.** Load `maq-project.json` for the story type, fields, tags, area path, and iteration behavior. Block only operations whose configuration is missing. A static creation iteration is not the current sprint.
3. **Context.** Load only relevant domain records and references; separate reviewed facts, hypotheses, and unresolved conflicts.
4. **Best practices.** Consult /best-practices for the ADO User Story artifact type and load only applicable linked pages. Report a failed lookup; never claim consultation that did not happen.
5. **Extract.** Gather outcome, evidenced business context, scope/non-goals, acceptance criteria, decisions, consequential open questions, examples, and references. Do not invent business context or settle consequential decisions silently. Blocking questions stay in the open-questions section, distinct from requirements.
6. **Discover.** Find the ADO tools and schemas. Call `get_type` on the configured type to confirm fields and allowed values; confirm configured tags exist in the project's conventions.
7. **Related work.** Search for duplicates and related items (`search_workitem`, `wit_query`); surface matches before creating.
8. **Read current state (update mode).** `get` the story with all fields and relations; record `/rev`; read recent comments. Preserve the existing **Technical Approach** section verbatim (written by `/approach`); refresh only other sections. Preserve human edits.
9. **Classify.** Propose configured tags by content: `platform-architecture` (framework/infrastructure), `data-engineering` (data products, pipelines, models), `experiment` (hypothesis testing). Use only tags present in configuration; keep existing tags; never assume they are universal.
10. **Preview.** Show the rendered field change set as a diff (new vs. existing), tags, and target. Ask for approval. Stop until approved.
11. **Write.** Create with `wit_work_item_write` `create`, or `update` with `updates` starting with `Test` on `/rev` using the revision from step 8. On a revision conflict, reread, merge, re-preview, and reapprove; never overwrite newer content.
12. **Timeout reconciliation.** On a timeout or ambiguous result, do not retry blindly. Search for the story by title, area, and recent creation time (or reread the known ID and compare `/rev` and fields) against the recorded intent. If it applied, treat it as done; if clearly not, ask approval to retry; if inconclusive, stop and report the uncertainty.
13. **Read back.** `get` the story, verify fields, tags, and the preserved Technical Approach match the approved preview. Optionally add an evidence comment (separate approval) with a readable summary.
14. **Report.** Give the story URL, new revision, applied tags, any substitutions, and unresolved blockers. Never close or transition the item to done.
