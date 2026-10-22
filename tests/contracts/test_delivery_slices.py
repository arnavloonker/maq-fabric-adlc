"""Delivery-slice contracts: python tests\\contracts\\test_delivery_slices.py"""
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[2]
errors = []

ALLOWED_HTML = ("<h2>", "<p>", "<ul>", "<ol>", "<li>", "<strong>", "<table>")
SAFETY = root / ".apm" / "instructions" / "maq-safety.instructions.md"
FIELD_WRITERS = (
    ".apm/skills/to-story/reference/contract.md",
    ".apm/skills/to-tasks/reference/contract.md",
    ".apm/skills/approach/reference/contract.md",
)

safety = SAFETY.read_text(encoding="utf-8")
if "allowed HTML" not in safety or "Do not write Markdown" not in safety:
    errors.append("safety rules: work-item fields must name allowed HTML and forbid Markdown")
for tag in ALLOWED_HTML:
    if tag not in safety:
        errors.append(f"safety rules: allowed HTML missing {tag}")

for rel in FIELD_WRITERS:
    text = (root / rel).read_text(encoding="utf-8")
    if "allowed HTML" not in text or "Do not write Markdown" not in text:
        errors.append(f"{rel}: must require allowed HTML and forbid Markdown in work-item fields")

catalog_path = root / ".apm" / "skills" / "best-practices" / "reference" / "catalog.md"
catalog = catalog_path.read_text(encoding="utf-8")
pr_section = catalog.split("## ADO Pull Request", 1)[-1].split("\n## ", 1)[0]
local_links = [link for link in re.findall(r"\]\(([^)]+)\)", pr_section) if not link.startswith("http")]
if not local_links:
    errors.append("ADO Pull Request consult does not resolve to an in-package page")
else:
    page = (catalog_path.parent / local_links[0]).resolve()
    if not page.is_file() or catalog_path.parent.resolve() not in page.parents:
        errors.append("ADO Pull Request in-package page is missing")
    else:
        prose = [
            line.strip() for line in page.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#") and "learn.microsoft.com" not in line
            and not line.strip().startswith("http")
        ]
        if not any(len(line.split()) >= 8 for line in prose):
            errors.append("ADO Pull Request page is not MAQ prose")
procedure = (root / ".apm" / "skills" / "best-practices" / "reference" / "procedure.md").read_text(encoding="utf-8")
if "in-package" not in procedure:
    errors.append("consult procedure does not read in-package pages")

apm = (root / "apm.yml").read_text(encoding="utf-8")
if "https://github.com/microsoft/skills-for-fabric#v0.3.19" not in apm:
    errors.append("apm.yml does not pin the Fabric skills package")
matrix = json.loads((root / "capability-matrix.json").read_text(encoding="utf-8"))
for row in matrix["rows"]:
    if row.get("itemType") in ("Lakehouse", "Notebook") and row.get("adapterSkill") != "spark-cli":
        errors.append(f"{row.get('itemType')} matrix row does not name the upstream skill spark-cli")
if (root / ".apm" / "skills" / "maq-fabric-data-engineering").exists():
    errors.append("data-engineering adapter directory is still present")

diff_contract = (root / ".apm" / "skills" / "code-diff" / "reference" / "contract.md").read_text(encoding="utf-8")
if "read-only until a separate approval" not in diff_contract:
    errors.append("code-diff default is not read-only until a separate approval")
if "one Markdown pull-request comment" not in diff_contract:
    errors.append("code-diff has no approved single Markdown comment")
if "no PR comments" in diff_contract:
    errors.append("code-diff still forbids the approved comment")

if errors:
    print("FAIL")
    for error in errors:
        print(" -", error)
    sys.exit(1)
print("PASS (work-item HTML, in-house pull-request practice, first runtime companion, code-diff comment)")
