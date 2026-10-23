# Mode: architecture

Use for shared platform, reusable framework, workspace topology, or cross-product contract changes. Product-specific ingestion, transformation, model, or pipeline changes belong in `data-product` mode. Reference the reason an alternative was selected (from `/brainstorm` or the story); do not restart an unbounded options exercise.

## Specify
- **Current boundaries** and **proposed boundaries**: components, workspaces, items, and owners (before/after diagram in Mermaid).
- **Selected interfaces**: contracts, parameters, schemas, triggers.
- **Compatibility**: consumers affected, versions, deprecation steps.
- **Dependencies**: upstream/downstream items, permissions, capacity prerequisites.
- **Rollout** order within DEV and promotion intent; **rollback** steps.
- Artifact scope: create / update / remove / no-change per item.
- Adapter and capability-matrix status for each Fabric item type; mark `blocked` or `manual-only` where automation is unavailable.

## Seam
Prefer a parameter-window seam: run the changed pipeline/notebook with a narrow parameter window (single date partition or sample key set) and check the highest-level observable output.
Draft contract checks:
- Output row count for the window equals the expected count.
- Key uniqueness on the output is 0 duplicates.
- A downstream DAX measure for the window equals a known value, or an equivalent invariant before and after the change (before/after equality when behavior must not change).

## Contradictions
If inspection shows a hidden consumer, unsupported item type, or broken assumption, ask one question with a recommended answer before specifying further.
