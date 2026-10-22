# Best-practices procedure

## Consult
1. Map the caller's scope to artifact groups in `catalog.md` (for example notebook edit -> Notebook; story drafting -> ADO User Story; PR publication -> ADO Pull Request).
2. Open `catalog.md` and read only those groups. If the file cannot be read, report a retrieval failure; do not continue as if consulted.
3. Select the links relevant to the task. Retrieve each with an available fetch tool. Retrieve nothing speculative.
4. If a group has no entry, return nothing and let the caller proceed. Do not announce it.
5. If a retrieval fails (network, permission, moved page), report URL and error to the caller, and mark that source unchecked.
6. Compare retrieved guidance with the approved project standards and shared safety rules. If they conflict consequentially, report both sources and the affected operation, and pause that operation for a human decision. Never weaken safety rules.
7. Return concise applicable points with their source URLs. Return control to the caller; do not call `/best-practices` again.

## Propose-add / propose-update
1. Resolve the installed APM dependency source repository and pinned revision from package metadata or the consumer's dependency/lock record. Never assume the consumer repository is the central source. If unresolved or ambiguous, skip to step 7.
2. Verify the proposed link loads and is a real Microsoft Learn or official vendor page. Reject others.
3. Confirm the link belongs to an existing artifact group (or add a new group heading) and is not a duplicate.
4. Resolve the source repository default branch at runtime and inspect its catalog against the pinned copy. In a scratch clone based on that branch, edit only `.apm\skills\best-practices\reference\catalog.md` as a link line under the group. Preserve intervening changes; if versions conflict, stop and report. Add no metadata fields.
5. Show the diff, target repository/branch, and proposed branch name. Ask for approval.
6. After approval, push a new branch and create a pull request to the resolved source default branch using discovered tools for its provider. No autocomplete, no merge, no work-item closure. Read the PR back and report its URL. On a timeout, search for an existing PR from that branch before retrying.
7. If source resolution, supported tooling, access, or approval is missing, output a unified patch against the catalog file and state that no catalog update was made.
8. Tell the user consumers receive the change only through a reviewed release and explicit pin update.
