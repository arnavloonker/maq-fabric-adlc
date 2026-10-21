"""Package contract validator: python tests\\contracts\\validate_package.py [package_root]
Checks: SKILL.md <=199 words, frontmatter name==dir, relative links resolve inside skill dir,
schema validity (if jsonschema installed), required workflow skills, /best-practices hook."""
import json, re, sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[2])
skills_dir = root / ".apm" / "skills"
WORKFLOW = ["brainstorm", "to-story", "domain", "approach", "to-tasks", "implement",
            "verify", "code-diff", "status", "best-practices"]
errors = []

for name in WORKFLOW:
    if not (skills_dir / name / "SKILL.md").is_file():
        errors.append(f"missing workflow skill: {name}")

for skill in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
    md = skill / "SKILL.md"
    if not md.is_file():
        errors.append(f"{skill.name}: no SKILL.md")
        continue
    text = md.read_text(encoding="utf-8")
    words = len(text.split())
    if words > 199:
        errors.append(f"{skill.name}: {words} words (max 199)")
    m = re.match(r"---\r?\n(.*?)\r?\n---", text, re.S)
    if not m:
        errors.append(f"{skill.name}: missing frontmatter")
    else:
        nm = re.search(r"^name:\s*(\S+)", m.group(1), re.M)
        if not nm or nm.group(1).strip("\"'") != skill.name:
            errors.append(f"{skill.name}: frontmatter name mismatch")
        if not re.search(r"^description:", m.group(1), re.M):
            errors.append(f"{skill.name}: missing description")
    for link in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", text):
        if re.match(r"[a-z]+://", link):
            continue
        t = (skill / link).resolve()
        if not t.is_file() or skill.resolve() not in t.parents:
            errors.append(f"{skill.name}: bad link {link}")
    if skill.name in WORKFLOW and skill.name != "best-practices" and "best-practices" not in text:
        errors.append(f"{skill.name}: no /best-practices consultation hook")
    for req in ("contract.md", "procedure.md"):
        if skill.name in WORKFLOW and not (skill / "reference" / req).is_file():
            errors.append(f"{skill.name}: missing reference/{req}")

for rel in ["apm.yml", ".apm/instructions/maq-safety.instructions.md",
            ".apm/agents/maq-adversarial-reviewer.agent.md", "capability-matrix.json",
            "upstream-sources.json", "THIRD-PARTY-NOTICES.md",
            "project-config/maq-project.schema.json", "project-config/maq-project.example.json"]:
    if not (root / rel).is_file():
        errors.append(f"missing {rel}")

try:
    import jsonschema
    sch = json.loads((root / "project-config/maq-project.schema.json").read_text(encoding="utf-8"))
    ex = json.loads((root / "project-config/maq-project.example.json").read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(sch).validate(ex)
except ImportError:
    print("jsonschema not installed; schema check skipped")
except Exception as e:
    errors.append(f"schema/example: {str(e)[:200]}")

if errors:
    print("FAIL"); [print(" -", e) for e in errors]; sys.exit(1)
print("PASS")
