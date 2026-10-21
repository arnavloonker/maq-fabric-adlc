# Industry Solutions procedure

## Companion skills and tools
| Operation | Preferred | Notes |
| --- | --- | --- |
| Discover items and catalog metadata | `onelake-catalog-govern-cli` | Read-only |
| Solution item creation or configuration | No validated companion | `manual-only` |

## Steps
1. Read the matrix row in `capability-matrix.json`. Industry and preview offerings must be checked against the chosen catalog snapshot; if absent, report `blocked`.
2. Record prerequisites: tenant switches, licensing, capacity, region, and required permissions. Report them as findings to verify, not assumptions.
3. Identify which underlying workload adapters apply (warehouse, lakehouse, pipelines) and delegate those parts to them.
4. Solution-specific setup is a manual action in an approved DEV workspace only; provide numbered steps and expected evidence.
5. Verification uses bounded reads through the matching adapter.

## Unavailable paths
Report `manual-only` with reason. Never configure solutions in UAT or PROD.
