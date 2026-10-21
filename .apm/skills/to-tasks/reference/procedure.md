# /to-tasks procedure

## 1. Scope and context
1. Resolve the consumer repository root via Git and load relevant `maq-project.json` settings (org, project, task type, iteration, tags). Missing settings block only dependent steps.
2. Load only relevant domain records and references.
3. Consult /best-practices for the ADO Task artifact group; apply retrieved content. Report a failed lookup; stay quiet on an absent optional entry. Do not recurse.

## 2. Discover tools (do not guess argument shapes)
Preferred: `azure-devops-wit_work_item` (`get`, `get_type`, `list_comments`), `azure-devops-wit_work_item_write` (`create`, `add_child`), `azure-devops-wit_work_item_link_write` (dependency links). Read the schemas first. Discover valid link types and direction (for example predecessor/successor or related) from the process via `get_type`; do not assume. Substitute a tool only with equivalent semantics, scope, permissions, and approval boundaries, and note it in the report.

## 3. Read current state
- Get the story (fields, description, approach section, tags, revision) and its existing children with their titles, states, and links.
- Confirm an agreed seam and no open consequential decisions. If missing, stop and recommend `/approach`.
- Record the story revision and intent key (story ID + slice titles).

## 4. Propose slices
Draft vertical tracer-bullet slices from the approach, ordered by dependency. Each slice: title, scope, expected artifacts, fast seam-test check, evidence expectations, dependencies, rough size. Verify each is a vertical slice crossing the relevant layers and fits one context window. Map existing children onto slices and mark them keep/unmatched; never modify them.

## 5. Quiz-until-approved loop
Ask exactly one question at a time, each with a recommended answer. Typical questions: slice thickness, first tracer bullet, whether to split or merge a slice, dependency order, which seam check per slice. Update the proposal after each answer. Repeat until the engineer explicitly approves the granularity. Do not batch questions or proceed on silence.

## 6. Preview
Show a table of tasks to create (parent, type, title, description, tags, iteration/area, assignee if configured), tasks already existing (skipped), and dependency links (source, target, link type). Obtain explicit approval. Re-preview if anything changes.

## 7. Create
- Create each missing task with `add_child` (or `create` plus a parent link), one at a time, recording the returned ID against its intent key.
- Add dependency links with `wit_work_item_link_write` only after both ends exist.
- Do not set tasks to closed or any done state.

## 8. Timeout and re-invocation reconciliation
On a timeout, error, or re-invocation, never blindly repeat. Re-read the story's children and match by title and intent key. Create only slices with no match; add only missing links. If a match is ambiguous (similar titles, partial bodies), stop and report uncertainty for the engineer to resolve. Treat a repeated run on an already-decomposed story as reconcile-only.

## 9. Read back and report
Re-read children and links. Report task IDs and URLs, dependency graph, skipped existing tasks, any failed writes, and unresolved blockers. Do not claim completion of work; do not close anything.
