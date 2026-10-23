# Mode: platform

Use to build reusable platform capabilities in Fabric that many data products consume: cross-cutting pipelines and notebooks, logging, audit and observability, orchestration or metadata-driven frameworks, shared libraries and environments, workspace topology, and team-specific engineering patterns that simplify or optimize work across products. Medallion layering is a baseline convention these capabilities serve, not the subject. Product-specific ingestion, transformation, model, or pipeline changes belong in `data-product` mode. Reference the reason an alternative was selected (from `/brainstorm` or the story); do not restart an unbounded options exercise.

## Capability kinds
Name the kind(s) in scope: cross-cutting operation (retry, alerting, scheduling), logging/audit/observability, ingestion or transformation framework, orchestration/metadata-driven control, shared library/environment, deployment/CI-CD pattern, or workspace/item topology.

## Specify
- **Platform need**: the repeated engineering pattern, the teams or products affected, and the cost or risk it removes.
- **Current boundaries** and **proposed boundaries**: components, workspaces, items, and owners (before/after diagram in Mermaid).
- **Selected interfaces**: the capability's consumer contract: entry points, parameters, schemas, log/audit tables, triggers.
- **Consumer adoption**: reference consumers, onboarding steps, what a product must change to adopt.
- **Compatibility**: consumers affected, versions, deprecation steps.
- **Dependencies**: upstream/downstream items, permissions, capacity prerequisites.
- **Operability**: where the capability logs, how failures surface, and who owns it.
- **Rollout** order within DEV and promotion intent; **rollback** steps.
- Artifact scope: create / update / remove / no-change per item.
- Adapter and capability-matrix status for each Fabric item type; mark `blocked` or `manual-only` where automation is unavailable.

## Seam
Prefer a reference-consumer seam: invoke the capability from a reference consumer pipeline/notebook with a narrow parameter window (single date partition or sample key set) and check the highest-level observable output.
Draft contract checks:
- Output row count for the window equals the expected count.
- Key uniqueness on the output is 0 duplicates.
- Capability records (log, audit, or control rows) for the run exist with expected status and counts; a forced failure is recorded and surfaces as designed.
- A rerun for the same window is idempotent.
- A downstream DAX measure for the window equals a known value, or an equivalent invariant before and after the change (before/after equality when behavior must not change).

## Contradictions
If inspection shows a hidden consumer, unsupported item type, or broken assumption, ask one question with a recommended answer before specifying further.
