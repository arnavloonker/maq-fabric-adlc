# maq-fabric-engineering

MAQ agentic engineering workflow and Fabric engineering expertise, packaged as an [APM](https://github.com/microsoft/apm) package for GitHub Copilot.

## Install

In your Fabric project repository:

```powershell
apm install <git url of this package> --target copilot
```

Consumer `apm.yml` skeleton (pin an immutable internal release):

```yaml
name: my-fabric-project
version: 0.1.0
targets:
  - copilot
dependencies:
  apm:
    - <git url of this package>#<release-tag>
  mcp: []
```

Then configure the project:

```powershell
Copy-Item <package>\project-config\maq-project.example.json maq-project.json
```

Replace every `REPLACE_*` placeholder, then validate live identities, workspaces, and permissions during onboarding. Keep `maq-project.json` next to the schema; UAT/PROD must stay `allowMutation: false`. Set up MCP servers per [docs\mcp-onboarding.md](docs/mcp-onboarding.md).

## Skills

Invoke from Copilot CLI by name:

| Skill | Purpose |
| --- | --- |
| `/brainstorm` | Explore a problem and capture evidence |
| `/to-story` | Turn context into an ADO User Story (approved write) |
| `/domain` | Record business-domain knowledge |
| `/approach` | Technical approach, seam verification contract, readiness tag |
| `/to-tasks` | Vertical-slice ADO Tasks |
| `/implement` | Build in DEV with TDD at the seam |
| `/verify` | Verify the seam; separate-context review |
| `/code-diff` | PR change brief |
| `/status` | Read-only sprint summary |
| `/best-practices` | Consult or maintain the central practices catalog |

Internal `maq-fabric-*` adapter skills (one per Fabric workload area) are called by the workflow skills, not directly.

## Safety

See `.apm\instructions\maq-safety.instructions.md`: DEV-only mutation, no automatic merge, completion, or closure, approval tied to concrete operations, no secrets.

## Capability matrix

`capability-matrix.json` lists each Fabric item and operation with status `planned` or `manual-only`. No row is `validated-dev` until DEV evidence exists.

## Tests

```powershell
python tests\contracts\test_fixtures.py
python tests\contracts\validate_package.py
```

Requires `pip install jsonschema`.
