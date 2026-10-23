# Mode: experiment

Use when the selected direction is a bounded experiment, for example proving a new Fabric workload capability. `/brainstorm` may already have run discovery; do not duplicate it or promote results to production claims.

## Specify
- **Hypothesis** and the learning result that counts as support, refutation, or inconclusive.
- **Baseline**: current behavior and measurements, with observation time.
- **Artifact and configuration changes**: exact items by name, each create / update / remove. Recommend a branch workspace or `<branch_slug>_` prefix; honor explicitly requested existing/unprefixed lower-environment targets after concrete approval, recording target mode (`branch-workspace`, `shared-prefix`, or `user-directed-target`) and rationale.
- **Bounded lower-environment execution**: recommend DEV; specify the user-approved workspace/environment, permissions, maximum run time, capacity/cost limit, and query windows. UAT is limited to explicitly prompted validation.
- **Measurements**: metrics, how collected, thresholds.
- **Cleanup and rollback**: exact items removed, order, and how failure of cleanup is reported.
- Cleanup is a mutation and is included in the approved scope.

## Seam
The single highest-level observable result of the experiment. Draft contract checks: output row count in the bounded window, key uniqueness, and a measure (DAX or SQL aggregate) compared to a known or baseline value.

## Gates
- Nothing runs from `/approach`; this mode only specifies. Execution happens later under explicit approval of the concrete operation set.
- UAT is read-only except explicitly requested, concretely approved lower-environment validation. PROD is never mutated. Missing permissions yield a blocker, not fabricated results; missing recommended isolation alone does not.
- Tag ready only when the experiment definition, limits, cleanup, and contract are approved.
