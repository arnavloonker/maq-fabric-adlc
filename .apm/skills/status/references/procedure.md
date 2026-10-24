# /status procedure

Follow in order. Every step is read-only.

1. **Dependencies.** Load only `ado.organizationUrl`, `ado.project`, and `ado.team` from `maq-project.toon`. No status policy block exists. Missing values block only dependent steps; report which.
2. **Practices.** Consult /best-practices for ADO User Story and ADO Task. Do not claim consultation if retrieval failed; report the failure. Do not invoke it recursively.
3. **Discover tools.** Read schemas before use; do not invent arguments. Preferred: `azure-devops-core_list_project_teams` (confirm the team), `azure-devops-work` iteration actions (team iterations, current/timeframe filter), `azure-devops-wit_query` or `azure-devops-search_workitem` (assigned items), `azure-devops-wit_work_item` (`get`, `list_comments`, relations, revisions), `azure-devops-repo_pull_request` and `azure-devops-pipelines_build` (linked events). Do not call `work_iteration_write`, `work_capacity_write`, or any `*_write` tool. Record any substitution; it must remain read-only.
4. **Identity.** Resolve the signed-in user from the connection and match it to the ADO identity. If it does not match uniquely, ask.
5. **Iteration.** Ask the work tools for the team's current iteration and record its name, path, and dates. If none or several are current, ask. Apply explicit user filters and show them.
6. **Query.** Fetch stories and tasks assigned to the user in that iteration (WIQL with `@Me` or the resolved identity, and the iteration path), bounded to a sensible page size.
7. **Related context.** Fetch only the parents, children, and dependency (predecessor/successor/related) items needed to explain assigned items. Label each `parent`, `child`, or `dependency`, and `context` when not assigned to the user or outside the iteration.
8. **Phase.** Derive a phase only from retrieved states, linked PRs/builds, and comments and label it `inferred: <evidence>`. If evidence is insufficient, say phase is not available.
9. **Chronology.** Collect revisions (state, assignment changes), comments, and linked PR/build events from the past 30 days. Sort by time, keep the newest 50 events, and state how many were omitted or inaccessible. Include timestamp, actor, and link for each.
10. **Analyze.** Identify blockers, waiting and dependency states, stale items, and unverified claims. Draft remaining actions that cite the record they come from.
11. **Report.** Use this order: scope and snapshot time; hierarchy with actual states; context; phase; chronology; blockers; remaining actions; limitations (omitted history, access gaps, unavailable links). No completion percentage.
12. **Persist.** Only if asked: preview, then create `references\status\<snapshot-id>.md` non-destructively with the report, sources, and observation time.

## Stop conditions
Ambiguous identity, team, or iteration; no read access to work items; request to update ADO (decline and offer a separate approved workflow).
