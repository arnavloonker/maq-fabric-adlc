# Approach contract

## Inputs
- ADO story ID (required) and mode: `data-model`, `architecture`, or `experiment`.
- Optional: exploration findings under `references\explorations\<id>\findings.md`, domain records, repository and workspace identities from `maq-project.toon`.
- Missing configuration blocks only the dependent operation (for example, no Fabric workspace blocks live validation but not repository-only analysis).

## Outputs
1. A technical approach section written into the story's dedicated approach field/section (other story sections are preserved untouched).
2. A single **Seam** and a draft **Verification Contract** inside that section.
3. The fixed `build-ready` tag present or absent on the story.
4. A final report: story URL, tag state, resolved decisions, open blockers, unvalidated assumptions.

## Approach section required content
- Provenance: repository revision (commit), live observation time, environment, artifact definition/version where available.
- Current behavior (before) and proposed behavior (after). Proposed changes are never described as deployed.
- Artifact-by-artifact scope: each artifact marked create / update / remove / no-change.
- Dependencies and interfaces; migration, compatibility, rollout and rollback where relevant.
- Decisions made, each with the rejected alternatives and reason.
- Seam and draft Verification Contract (see below).

## Seam
Exactly one: the highest-level Fabric boundary at which the outcome is observable (for a data product, typically the semantic model measure over gold tables). TDD in `/implement` and the final check in `/verify` must exercise this same Seam.

## Draft Verification Contract
- Seam identity (workspace, item, artifact version/environment).
- Checks, each with the exact query, expected value, and tolerance:
  - Gold row counts, e.g. `SELECT COUNT(*) FROM gold.fact_sales` equals the agreed reconciled source count.
  - Key uniqueness, e.g. `SELECT COUNT(*) - COUNT(DISTINCT sale_id) FROM gold.fact_sales` equals 0.
  - DAX measure against a known value, e.g. `EVALUATE ROW("TotalSales", [Total Sales])` equals the independently known figure for a stated filter window.
- Fast-feedback window (partition filter, sample keys, or parameter window) used by `/implement`.
- Pass/fail rule and what evidence is recorded.
- Status: `draft` until the user approves it; then `approved` with approver and date.

## Readiness tag
- Applied only when every consequential decision is resolved AND the contract is approved AND no blocking question is open.
- Removed (with a comment stating why) if any blocker reopens, the baseline is found stale, or the contract is changed after approval.
- The tag name is always `build-ready`; never substitute another readiness tag.

## Work-item HTML
The approach section written into the story uses the allowed HTML set from the safety rules. Do not write Markdown into that field. Preview the rendered field.

## Safety
- Read-only by default; only approved, bounded DEV scratch work in experiment mode, including cleanup.
- Never mutate UAT/PROD, enable PR auto-complete, or close work items.
- Missing access yields an explicit unvalidated assumption or blocker, never invented profiling results.
- No secrets, tokens, connection strings, or raw sensitive rows in the story or findings.
