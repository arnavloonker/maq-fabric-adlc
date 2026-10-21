# Mode: data-model

Use for data-product asks. Commit decisions that the evidence supports; reuse `/brainstorm` findings, revalidating when stale.

## Specify
- **Grain** of each table, stated as one sentence ("one row per order line per day").
- **Keys**: business key, surrogate key, and proof of uniqueness (duplicate count query and result).
- **Cardinalities** and join completeness (FULL OUTER JOIN match/orphan counts).
- **Source mappings** column by column, with transformations and quality rules.
- **History behavior** (overwrite, SCD2, snapshot).
- **Medallion placement**: bronze raw with provenance, silver enriched, gold curated. Apply only where relevant.
- **Downstream**: semantic model relationships, measures, and report changes.

## Before/after
Show current and proposed schemas, relationships, or transformations side by side (tables or Mermaid). Mark each table/column create/update/remove/no-change.

## Seam
Normally the semantic model measure over gold. Draft contract checks:
- Gold row counts equal reconciled source counts.
- Key uniqueness: `COUNT(*) - COUNT(DISTINCT key) = 0`.
- DAX measure example: `EVALUATE ROW("Total Sales", [Total Sales])` equals a known value for a fixed date window.

## Contradictions
Duplicate keys, grain mismatch, or incomplete joins reopen the decision: ask one question with a recommended answer (for example, dedupe by latest `modified_at` versus change the grain). Do not tag ready until resolved.
