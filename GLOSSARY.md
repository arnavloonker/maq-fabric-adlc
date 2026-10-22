# MAQ Fabric engineering

The vocabulary for the MAQ agentic delivery package: workflow skills, the Fabric expertise they rely on, and the records they produce.

## Language

**Workflow skill**:
A human-invoked skill shipped by this package, such as `/approach` or `/code-diff`.
_Avoid_: Adapter, tool, agent

**Runtime companion**:
A Fabric skill or MCP server resolved on the consumer machine and not copied into this package.
_Avoid_: Fork, vendored skill, bundled server

**In-house practice**:
MAQ-authored guidance stored in this package and consulted by `/best-practices`.
_Avoid_: Wiki page, catalog link, standard

**Code review**:
A read of a pull request diff against in-house practices and the practices catalog. It is not a code-diff brief and not seam verification.
_Avoid_: Verify, code diff, adversarial review
