# maq-fabric-engineering

MAQ agentic engineering workflow and Fabric engineering expertise, packaged as an [APM](https://github.com/microsoft/apm) package for GitHub Copilot.

## Install

In your Fabric project repository:

```powershell
apm install <git url of this package> --target copilot
```

APM also resolves the official `microsoft/fabric-skills` dependency; its skill files remain external and are not copied into this package.

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
Copy-Item <package>\project-config\maq-project.example.toon maq-project.toon
```

Replace every `REPLACE_*` placeholder and validate live identities, workspaces, and permissions during onboarding. The TOON contains only six ADO connection/placement settings and three Fabric workspace lists. There is no schema or policy configuration: safety, task slicing, TDD, verification, paths, and best-practices behavior live in the skills and instructions. Set up MCP servers per [docs\mcp-onboarding.md](docs/mcp-onboarding.md).

TOON arrays declare their length: when adding a workspace, update `[1]` to the new count and comma-separate the IDs. Keep ADO paths quoted with escaped backslashes, for example `"Project\\Data"`. List only verified workspace IDs; DEV, UAT, and PROD lists must not overlap. UAT/PROD are always read-only. Resolve the repository's default branch at runtime.

For existing consumers, replace the old JSON configuration with the TOON template, carrying over only ADO identifiers/paths and workspace IDs. Remove the old JSON and schema; do not copy workflow or architecture decisions into TOON. Pin the package release in `apm.yml`, not in project configuration.

## Skills

Invoke from Copilot CLI by name:

| Skill | Purpose |
| --- | --- |
| `/brainstorm` | Explore a problem and capture evidence |
| `/to-story` | Turn context into an ADO User Story (approved write) |
| `/domain` | Record business-domain knowledge |
| `/approach` | Data-product, platform, or experiment approach with visual lineage and seam verification |
| `/to-tasks` | Vertical-slice ADO Tasks |
| `/implement` | Build in DEV with TDD at the seam |
| `/verify` | Verify the seam; separate-context review |
| `/code-diff` | PR change brief with highlighted Before/After views |
| `/status` | Read-only sprint summary |
| `/retro` | Review past skill runs vs initial prompts; issue-ready feedback report |
| `/best-practices` | Consult or maintain the central practices catalog |

Workflow skills use the relevant skills supplied by `microsoft/fabric-skills` directly. The capability matrix identifies the runtime skill/tool bindings and keeps operations without a supported direct path `blocked` or `manual-only`.

## Safety

See `.apm\instructions\maq-safety.instructions.md`: DEV-only mutation, no automatic merge, completion, or closure, approval tied to concrete operations, no secrets.

## Capability matrix

`capability-matrix.json` lists each Fabric item and operation with status `planned` or `manual-only`. No row is `validated-dev` until DEV evidence exists.

## Tests

```powershell
python tests\contracts\test_fixtures.py
python tests\contracts\validate_package.py
python tests\contracts\test_visual_briefs.py
```

Install the test-only TOON decoder with `python -m pip install -r tests\contracts\requirements.txt`. Consumers do not need a parser or JSON Schema to use the skills.
