# Fabric DEV isolation

DEV only. UAT/PROD may be read within authorized scope and are never mutated.

## Mode selection (per item type, from `capability-matrix.json`)
1. **Mapped feature-branch workspace.** Use it only when the matrix row for the item type and operation has `branchWorkspaceSupport` true and `sourceControlSupport` available, and a workspace for this branch is already pre-created and mapped in `maq-project.json`. Verify the workspace identity, the Git connection to the branch, and your permissions. This skill does not create workspaces, capacities, or Git connections.
2. **Shared DEV prefix fallback.** Otherwise use the configured shared DEV workspace and name every item, table, schema object, and job created by this work with the deterministic prefix `<branch_slug>_` (same slug as the branch). Check the row's `sharedWorkspacePrefixFallback`; if unsupported for the item type, report it blocked/manual-only.
3. If neither is verifiably available, stop for that operation.

## Rules
- Resolve exact workspace IDs from configuration, never by guessing or fuzzy name match.
- Before any create, list existing items and confirm no unprefixed or foreign collision; never alter items lacking your prefix or outside the mapped workspace.
- Prefixed or branch-workspace items are part of the approved change set; cleanup is a mutation and must be in the approved scope.
- Execution (notebook runs, pipeline runs, refreshes) targets only the isolated items, with bounded inputs.
- Authoring/execution in DEV needs approval of the explicit change set; it is not authority to promote, deploy, or sync to UAT/PROD.
- Record the mode, workspace, prefix, and item list in the report.
