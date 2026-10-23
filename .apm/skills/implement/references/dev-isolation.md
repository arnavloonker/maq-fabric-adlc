# Fabric lower-environment isolation

Recommend DEV execution and isolation by default. UAT is read-only unless the prompt explicitly requests lower-environment validation and approves its concrete operations. PROD is always read-only. Verify live environment identity and permissions for every target.

## Mode selection (per item type, from `capability-matrix.json`)
1. **`branch-workspace` (recommended).** Prefer a pre-created workspace listed in `fabric.devWorkspaceIds` in `maq-project.toon` and connected to this branch. Use `branchWorkspaceSupport` and `sourceControlSupport` as planning hints; verify the live workspace identity, Git connection, and permissions rather than inferring mapping from list membership or matrix flags. This skill does not create workspaces, capacities, or Git connections.
2. **`shared-prefix` (recommended fallback).** Otherwise propose an exact shared DEV workspace and prefix each scoped item, table, schema object, and job with `<branch_slug>_` (same slug as the branch). Treat `sharedWorkspacePrefixFallback` as guidance to verify at runtime, not a stop gate.
3. **`user-directed-target`.** If the prompt explicitly targets another lower-environment workspace or existing/unprefixed artifacts, obtain concrete operation approval and proceed after verifying exact identity, environment, permissions, and collisions. Record the target and rationale; isolation recommendations must not hard-block this approved mode. UAT scope is validation only. If the target is ambiguous, resolve it before execution.
4. Use `runtimeSkills` and `toolBindings` on `planned` or `validated-dev` rows to execute and validate in the approved runtime. Unverified branch support or absent prior DEV evidence is not a block. Report blocked/manual-only only when runtime skill/tool bindings or required access are genuinely missing; unresolved identity or approval still stops execution.

## Rules
- Resolve exact workspace IDs against `maq-project.toon` and explicit prompt targets, never by guessing or fuzzy name match. Verify live identity and environment even for configured IDs.
- Before creating, list existing items and check collisions. Modify only exact approved artifacts; unprefixed/existing targets require `user-directed-target` approval, never blanket ownership.
- All target modes need an approved change set; cleanup is a mutation and must be in the approved scope. Preserve pre-existing artifacts outside approved changes.
- Execution (notebook runs, pipeline runs, refreshes) targets only approved items, with bounded inputs.
- Authoring/execution needs approval of the explicit change set; it is not authority to promote, deploy, sync to UAT/PROD, or mutate PROD.
- Record the mode, workspace/environment, prefix if used, item list, approval, and target rationale in the report.
