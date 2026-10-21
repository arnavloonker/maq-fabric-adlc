# /status contract

## Produces
A read-only personal sprint summary for the signed-in user in the configured team's current iteration.

## Inputs
- Signed-in identity (resolved from the ADO connection, never typed from memory).
- `ado.organizationUrl`, `ado.project`, `ado.team`.
- `status` settings: `phaseField` (nullable), `allowLabeledPhaseInference`, `history.lookbackDays`, `history.maxEvents`, `history.includeLinkedPrBuildEvents`, `completionPercentage` (always false), `persistence` (save only when requested).
- Optional explicit filters: story, iteration, person. Reflect every filter in the reported scope.

## Rules
1. The iteration is the configured team's current iteration, resolved at run time. `ado.iterationPath` is for new-item placement and must never determine scope.
2. If the identity, team, or iteration does not resolve uniquely, ask; do not guess.
3. Personal workload is only items assigned to the signed-in user in the resolved iteration. Parents, children, and dependencies owned by others or outside the iteration are labeled `context`, never counted as the user's workload.
4. Show actual ADO states verbatim. Show phase from `phaseField` when configured; otherwise, only if `allowLabeledPhaseInference` is true, show a phase labeled `inferred` with its evidence.
5. Never report a completion percentage. Task counts by state are allowed but are not progress.
6. A PR merge is not evidence of deployment. Absence of a verification record is not proof verification never happened.
7. Chronology stays within `lookbackDays` and `maxEvents`; each event has a timestamp and source link. State what was omitted and any access gaps. Do not imply a complete audit trail or causation.
8. Next actions must be grounded in retrieved records.

## Output
Scope, snapshot time, story/task hierarchy with states, labeled context, phase, chronology, blockers and waiting states, unverified claims, remaining actions, limitations.

## Safety
No ADO writes of any kind (work items, comments, links, iterations, capacity, PRs). An unavailable read path is not permission to write. Publishing the report anywhere requires a separate previewed and approved request. Do not include secrets or raw sensitive data in saved snapshots.

## Persistence
Default is conversation output. Only when requested, save `references\status\<snapshot-id>.md`, where the id is a timestamp plus a collision-resistant suffix. Create non-destructively and preview before modifying any existing file. Record subject, sources, observation time, authoring run, and limitations.
