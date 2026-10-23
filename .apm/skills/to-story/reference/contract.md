# /to-story contract

## Inputs
- Conversation context or a selected exploration (`references\explorations\<id>\findings.md`).
- Optional existing story ID (update mode); otherwise create mode.
- Consumer-root `maq-project.toon`: ADO organization, project, team, repository, area path, and iteration path. Use `User Story`, native ADO fields, and fixed classification tags `platform`, `data-engineering`, and `experiment` when applicable. Stop dependent writes if the project process does not support the native type or fields. Missing configuration blocks only dependent operations.

## Outputs
- A previewed field change set, then an ADO User Story created or updated after approval.
- Story sections: outcome; evidenced business context; scope/non-goals; acceptance criteria; decisions; consequential open questions; exploration findings/examples; references; technical approach.
- Chat report: story URL, revision read back, tags applied, unresolved blockers. Never a false ready-for-build claim.

## Preferred tool bindings (reference profile; rediscover schemas, never invent arguments)
| Operation | Tool |
| --- | --- |
| Read story, type metadata, comments | `azure-devops-wit_work_item`: `get`, `get_type`, `list_comments` |
| Related work search | `azure-devops-search_workitem`, `azure-devops-wit_query` |
| Create / update | `azure-devops-wit_work_item_write`: `create`, `update` |
| Revision-safe update | `updates` begins with `Test` on `/rev` using the revision just read |
| Evidence comment | `azure-devops-wit_work_item_comment_write`: `add` (readable summary included) |
| Fabric evidence (optional) | `FabricIQ-DiscoverArtifacts`, `FabricIQ-ResolveFabricItem`, bounded `FabricIQ-ExecuteQuery` |

## Safe substitutions
Allowed only when semantics, target scope, permissions, approval boundaries, and evidence are equivalent; record the substitution in the run findings. An unavailable read path is not permission to edit external records. If revision tests are unsupported, reread immediately before writing and report the reduced guarantee.

## Approval rules
- Approval covers one concrete operation set: target story/project, payload, and read revision.
- Changed payload, target, or revision invalidates approval; reread and re-preview.
- Creating a story, updating a story, and adding a comment are distinct operations.
- Local evidence paths are not clickable proof; mark unpublished evidence as local.
- Never close, resolve, or transition a work item to a done state. Never touch UAT/PROD artifacts.
- No secrets or raw sensitive query results in story content.
