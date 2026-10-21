# Best-practices contract

## Modes and inputs
- `consult`: artifact type(s) the caller inspects, authors, updates, or assesses. Usually invoked automatically by another skill.
- `propose-add`: artifact type plus a source link to add.
- `propose-update`: an existing catalog entry plus the replacement or removal and a reason.

## Catalog
- Lives only in the installed central package: `reference\catalog.md`. Consultation reads the pinned installed copy, never the branch tip.
- Format: links grouped by artifact type. No per-entry rule schema, severity, rationale, or automatic lesson adoption.
- No project-local catalog, no `references\best-practices` folder in a consumer. A project may record that a practice was considered as run evidence only.

## Consultation rules
1. Read only the group(s) matching the caller's artifact types; retrieve only pages relevant to the task, on demand.
2. Apply retrieved page content. Never infer guidance from link titles.
3. Absent optional entry: continue silently; the caller uses official documentation through its normal procedure.
4. Retrieval failure, unchecked required standard, or consequential conflict is not an empty lookup. Report it with the source and affected scope. A consequential conflict pauses the affected operation.
5. Never state a practice was consulted when it was unavailable.
6. Do not recurse: this skill and its procedures never invoke `/best-practices`. No bulk loading.
7. Links supplement, never override, repository-local engineering standards or shared safety rules. No project setting selects or overrides package policy.
8. Consultation needs no onboarding configuration beyond the installed catalog.

## Maintenance rules
- Target: the installed APM dependency's source repository and pinned revision, resolved from package metadata or the consumer's APM dependency/lock record. The catalog path is always `.apm\skills\best-practices\reference\catalog.md`. Never assume the consumer repository is the central source. Resolve the source repository default branch at runtime; if source resolution is unavailable or ambiguous, return a proposed patch only.
- Never edit installed package resources, a consumer pin, or a local copy.
- Preview the exact diff and obtain approval before any branch push or pull request creation. Approval covers one change set and is void if it changes.
- Never merge, enable autocomplete, or treat a suggestion as an accepted practice. Reviewed central releases distribute accepted changes; consumers stay on their pinned version until they update it.
- If the source is unreachable, unresolved, or ambiguous, return a patch and say no catalog update was made.
- Accept only real, verified Microsoft Learn or official vendor links; no placeholders.

## Output
Consult: entries consulted (URL, retrieval time, package version), failures, conflicts. Propose: PR URL or patch, and the approval state.
