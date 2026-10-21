# /code-diff procedure

1. **Identify the PR.** Resolve repository and PR ID. Read metadata with `repo_pull_request` `get`: status, source/target branches, commits, linked work items, creation/completion times.
2. **Anchor the baseline.** List iterations. Use the requested iteration, else the latest. Record the iteration ID, source and target (common) commits. For completed PRs use the recorded merge/review commits, not current branch tips. If no baseline or diff is available, stop and report the limitation.
3. **Read the diff.** Fetch changes for that iteration; paginate until complete. List files by kind (code, notebook, pipeline, semantic model, config, generated, binary). State any unavailable, generated, binary, or truncated surface explicitly.
4. **Consult /best-practices** for the PR and the affected artifact types before judging.
5. **Inspect changes.** Read changed definitions at the target and source commits with `repo_file`. Trace evidenced dependencies (search code, referenced items, upstream/downstream tables, reports). Mark each relationship `evidenced` or `inferred`; otherwise `unknown`.
6. **Read intent (optional).** From PR-linked or supplied story/approach/verification, collect acceptance criteria, approach decisions, and evidence. When absent, say intent is not stated; do not invent it.
7. **Build the brief** from `brief-template.md`: plain-language summary, before/after Mermaid topology, impact, intended versus verified table. Write for a non-author: short sentences, concrete names, no filler, no praise, no hedging stacks.
8. **Self-check.** Every claim traces to a file, commit, or record. Verified means evidence exists; a static read is "reviewed", not "run". Mermaid is unrendered unless you rendered it.
9. **Present** the brief in chat. Offer to save to `references\pull-requests\<repository-id>\<pr-id>\<review-version>.md` (review-version = iteration ID). Save only on request after previewing the path and content.

Stop conditions: PR not found or no access; baseline unavailable; user asks for any ADO write (explain it is out of scope or require preview and approval for a separately requested publication).
