"""Contract tests: python tests\\contracts\\test_fixtures.py
Checks minimal TOON dependencies, fixed skill policies, and capability-matrix invariants."""
import json, sys
from pathlib import Path

try:
    import toon_format
except ImportError:
    sys.exit("TOON decoder required: python -m pip install -r tests\\contracts\\requirements.txt")

root = Path(__file__).resolve().parents[2]
errors = []

template = (root / "project-config" / "maq-project.example.toon").read_text(encoding="utf-8")
config = toon_format.loads(template)
if set(config) != {"ado", "fabric"}:
    errors.append("TOON config must contain platform dependencies only")
ado_keys = {"organizationUrl", "project", "team", "repository", "areaPath", "iterationPath"}
fabric_keys = {"devWorkspaceIds", "uatWorkspaceIds", "prodWorkspaceIds"}
if set(config.get("ado", {})) != ado_keys or set(config.get("fabric", {})) != fabric_keys:
    errors.append("TOON config contains missing or non-platform settings")
for key, value in config.get("ado", {}).items():
    if not isinstance(value, str) or not value.strip():
        errors.append(f"ado.{key}: expected nonempty string")
for key, value in config.get("fabric", {}).items():
    if not isinstance(value, list) or not value or any(not isinstance(v, str) or not v for v in value):
        errors.append(f"fabric.{key}: expected nonempty workspace list")
if config["ado"]["areaPath"] != r"REPLACE_PROJECT\REPLACE_AREA":
    errors.append("TOON ADO path escaping changed")
filled = template
replacements = {
    "REPLACE_ORG": "contoso", "REPLACE_PROJECT": "Contoso", "REPLACE_TEAM": "Engineering",
    "REPLACE_REPOSITORY_ID": "11111111-1111-1111-1111-111111111111",
    "REPLACE_AREA": "Data", "REPLACE_ITERATION": "Sprint 1",
    "REPLACE_DEV_WORKSPACE_GUID": "22222222-2222-2222-2222-222222222222",
    "REPLACE_UAT_WORKSPACE_GUID": "33333333-3333-3333-3333-333333333333",
    "REPLACE_PROD_WORKSPACE_GUID": "44444444-4444-4444-4444-444444444444",
}
for old, new in replacements.items():
    filled = filled.replace(old, new)
decoded = toon_format.loads(filled)
if "REPLACE_" in filled or toon_format.loads(toon_format.dumps(decoded)) != decoded:
    errors.append("filled TOON example must round-trip without placeholders")
multiple = filled.replace("devWorkspaceIds[1]:", "devWorkspaceIds[2]:").replace(
    replacements["REPLACE_DEV_WORKSPACE_GUID"],
    replacements["REPLACE_DEV_WORKSPACE_GUID"] + ",55555555-5555-5555-5555-555555555555")
if len(toon_format.loads(multiple)["fabric"]["devWorkspaceIds"]) != 2:
    errors.append("multiple DEV workspaces must remain supported")
for invalid in ('items[2]: one', 'path: "bad\\q"', 'items[1]: one,two'):
    try:
        toon_format.loads(invalid)
    except toon_format.ToonDecodeError:
        pass
    else:
        errors.append(f"malformed TOON accepted: {invalid!r}")

fixed_contracts = {
    ".apm/instructions/maq-safety.instructions.md": (
        "fabric.devWorkspaceIds", "UAT/PROD are always read-only", "lists must not overlap",
        "at most 250 rows", "60-second", "<branch_slug>_", "Never accept policy overrides",
        "default branch at runtime", "System.Title", "Microsoft.VSTS.Common.AcceptanceCriteria",
        "Never auto-complete, auto-merge, or close", "Closure is human-only",
    ),
    ".apm/skills/approach/references/procedure.md": ("build-ready", "revision-checked"),
    ".apm/skills/implement/references/procedure.md": ("TDD",),
    ".apm/skills/verify/references/procedure.md": ("separate",),
    ".apm/skills/to-tasks/references/outcome.md": (
        "vertical end-to-end tracer bullets", "one context window", "never horizontal",
        "one granularity question at a time",
    ),
    ".apm/skills/status/references/procedure.md": (
        "30 days", "50 events", "No completion percentage", "Only if asked",
    ),
    ".apm/skills/best-practices/references/outcome.md": (
        "pinned revision", "Never assume the consumer repository", "proposed patch only",
    ),
}
for rel, requirements in fixed_contracts.items():
    text = (root / rel).read_text(encoding="utf-8")
    for requirement in requirements:
        if requirement not in text:
            errors.append(f"{rel}: missing fixed policy {requirement!r}")

REQUIRED_DIMS = """catalogVersion documentationUrl workload itemType operation runtimeSkills
toolBindings requiredPermissions tenantAndCapacityPrerequisites supportedEnvironments sourceControlSupport
branchWorkspaceSupport sharedWorkspacePrefixFallback authoringPath validationPath manualFallback status
lastValidatedAt validationEvidence knownLimitations""".split()
ALLOWED = {"planned", "manual-only"}
AREAS = {"Data Engineering", "Data Factory", "Data Warehouse", "Databases", "Real-Time Intelligence",
         "Data Science", "Power BI", "Fabric IQ", "Industry Solutions", "Platform"}

m = json.loads((root / "capability-matrix.json").read_text(encoding="utf-8"))
source_manifest = json.loads((root / "upstream-sources.json").read_text(encoding="utf-8"))
fabric_skills = {
    companion["name"]
    for companion in source_manifest.get("runtimeCompanions", [])
    if companion.get("kind") == "skill"
}
rows = m.get("rows", [])
seen = set()
for i, r in enumerate(rows):
    merged = {**{k: m.get(k) for k in ("catalogVersion", "documentationUrl")}, **r}
    for d in REQUIRED_DIMS:
        if d not in merged:
            errors.append(f"matrix row {i}: missing {d}")
    if r.get("status") not in ALLOWED:
        errors.append(f"matrix row {i}: status {r.get('status')!r} not allowed before DEV validation")
    if r.get("supportedEnvironments") != ["DEV"]:
        errors.append(f"matrix row {i}: supportedEnvironments must be ['DEV']")
    if r.get("status") == "validated-dev" or r.get("validationEvidence"):
        errors.append(f"matrix row {i}: must not claim validation")
    if r.get("lastValidatedAt") is not None:
        errors.append(f"matrix row {i}: lastValidatedAt must be null")
    if not isinstance(r.get("runtimeSkills"), list):
        errors.append(f"matrix row {i}: runtimeSkills must be a list")
    elif any(skill not in fabric_skills for skill in r["runtimeSkills"]):
        errors.append(f"matrix row {i}: runtimeSkills must name declared Fabric companions")
    elif not set(r["runtimeSkills"]).issubset(set(r.get("toolBindings", []))):
        errors.append(f"matrix row {i}: runtimeSkills must also appear in toolBindings")
    if "adapterSkill" in r or "adapterVersion" in r:
        errors.append(f"matrix row {i}: internal adapter fields are not supported")
    seen.add(r.get("workload"))
if AREAS - seen:
    errors.append(f"matrix missing workloads: {sorted(AREAS - seen)}")

if errors:
    print("FAIL"); [print(" -", e) for e in errors]; sys.exit(1)
print(f"PASS (TOON template, filled and multi-workspace examples, malformed inputs, {len(rows)} matrix rows)")
