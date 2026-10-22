---
applyTo: "**/*.Notebook/**/*.py,**/*.Notebook/.platform"
description: MAQ engineering intent for Fabric notebook Python sources and notebook metadata.
---
# MAQ notebook engineering intent

- Open notebook `.py` source with a purpose and concise changelog. State whether it is an orchestrated component, reusable framework, or one-off; let that role guide its lifecycle and operational expectations.
- Organize logical source cells/sections with meaningful `##` headings. Preserve Fabric-generated cell markers; do not require comments on every Python control-flow block.
- In the notebook's `.platform`, keep `metadata.description` consistent with its purpose and role. Source headings and changelogs belong in notebook source, not new metadata fields.
- For production-intent notebooks, make run progress, timings, and failures diagnosable through the project's existing logging/monitoring approach. Report a missing mechanism rather than inventing a framework. Never log secrets or raw sensitive rows.
- Choose Spark capacity, resource profiles, and V-Order for the workload's volume, read/write balance, and downstream consumers, not blanket settings.
- Delegate authoring, monitoring, and tuning mechanics to the applicable installed official Fabric skills rather than duplicating their capabilities.
- Apply relevant practices during authoring and report gaps during review. Verification gates remain governed by approved requirements; shared safety rules still apply.

## Supporting guidance

- [Spark capacity and cluster planning](https://learn.microsoft.com/en-us/fabric/data-engineering/spark-best-practices-capacity-planning)
- [Delta optimization and V-Order trade-offs](https://learn.microsoft.com/en-us/fabric/data-engineering/delta-optimization-and-v-order?tabs=sparksql)
- [Workload-driven resource profiles](https://learn.microsoft.com/en-us/fabric/data-engineering/configure-resource-profiles)
