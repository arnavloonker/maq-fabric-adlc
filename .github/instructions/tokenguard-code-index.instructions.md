---
applyTo: "**"
---

<!-- Managed by TokenGuard. This file is overwritten when the code index guidance changes. -->

## TokenGuard Knowledge Index

Use `tokenguard_index` first for code, architecture, domain/module, dependency, and impact lookup. Default `answer` with a natural-language `query`. For multi-part tasks, batch each distinct question with `queries`; each useful query counts as one hit. Use the index again for distinct follow-up lookups before grep/read. Do not repeat a no-hit query.
When delegating multi-file codebase discovery, architecture, dependency, or impact research, use the `TokenGuard Index Research` subagent so the child receives the index tools; generic subagents may not expose extension-contributed tools.