"""Contract tests: python tests\\contracts\\test_fixtures.py
Validates maq-project fixtures against the schema and checks capability-matrix invariants."""
import json, sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    sys.exit("jsonschema required: pip install jsonschema")

root = Path(__file__).resolve().parents[2]
schema = json.loads((root / "project-config/maq-project.schema.json").read_text(encoding="utf-8"))
validator = jsonschema.Draft202012Validator(schema)
errors = []

fixtures = root / "tests" / "fixtures"
pos = sorted(fixtures.glob("positive-*.json"))
neg = sorted(fixtures.glob("negative-*.json"))
if not pos or len(neg) < 8:
    errors.append("expected positive fixtures and at least 8 negative fixtures")
for f in pos:
    errs = list(validator.iter_errors(json.loads(f.read_text(encoding="utf-8"))))
    if errs:
        errors.append(f"{f.name}: should be valid but failed: {errs[0].message[:120]}")
for f in neg:
    if not list(validator.iter_errors(json.loads(f.read_text(encoding="utf-8")))):
        errors.append(f"{f.name}: should be invalid but passed")

REQUIRED_DIMS = """catalogVersion documentationUrl workload itemType operation adapterSkill adapterVersion
toolBindings requiredPermissions tenantAndCapacityPrerequisites supportedEnvironments sourceControlSupport
branchWorkspaceSupport sharedWorkspacePrefixFallback authoringPath validationPath manualFallback status
lastValidatedAt validationEvidence knownLimitations""".split()
ALLOWED = {"planned", "manual-only"}
AREAS = {"Data Engineering", "Data Factory", "Data Warehouse", "Databases", "Real-Time Intelligence",
         "Data Science", "Power BI", "Fabric IQ", "Industry Solutions", "Platform"}

m = json.loads((root / "capability-matrix.json").read_text(encoding="utf-8"))
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
    if not (root / ".apm/skills" / str(r.get("adapterSkill")) / "SKILL.md").is_file():
        errors.append(f"matrix row {i}: adapter skill missing")
    seen.add(r.get("workload"))
if AREAS - seen:
    errors.append(f"matrix missing workloads: {sorted(AREAS - seen)}")

if errors:
    print("FAIL"); [print(" -", e) for e in errors]; sys.exit(1)
print(f"PASS ({len(pos)} positive, {len(neg)} negative fixtures, {len(rows)} matrix rows)")
