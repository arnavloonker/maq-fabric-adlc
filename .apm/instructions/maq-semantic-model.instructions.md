---
applyTo: "**/*.SemanticModel/**"
description: MAQ engineering intent for Fabric semantic-model artifacts.
---
# MAQ semantic-model engineering intent

- Prefer preparing stable, reusable transformations and justified aggregations upstream rather than compensating for avoidable preparation work in DAX. Preserve required grain, business meaning, and necessary detail.
- Retain context-dependent analytical calculations in DAX rather than materializing dynamic filter-context results upstream.
- Diagnose the actual bottleneck and compare measured results before keeping an optimization. Choose DAX, cardinality, aggregation, or other changes when evidence and the consumption scenario justify them, not because a reference lists them.
- Delegate modeling, authoring, and diagnostic mechanics to the applicable installed official Fabric skills rather than duplicating their capabilities.
- Apply relevant practices during authoring and report gaps during review. Verification gates remain governed by approved requirements; shared safety rules still apply.

## Supporting guidance

- [Diagnose with Performance analyzer](https://learn.microsoft.com/en-us/training/modules/optimize-semantic-model-performance/2-performance-analyzer)
- [Optimize DAX calculations](https://learn.microsoft.com/en-us/training/modules/optimize-semantic-model-performance/3-optimize-dax)
- [Reduce cardinality and evaluate trade-offs](https://learn.microsoft.com/en-us/training/modules/optimize-semantic-model-performance/4-reduce-cardinality)
- [Use aggregations when justified](https://learn.microsoft.com/en-us/training/modules/optimize-semantic-model-performance/5-implement-aggregations)
- [Troubleshoot common performance issues](https://learn.microsoft.com/en-us/training/modules/optimize-semantic-model-performance/6-troubleshoot)
- [Power BI optimization guidance](https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization)
