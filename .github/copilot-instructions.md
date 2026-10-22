# GitHub Copilot instructions: maq-fabric-engineering

This repo is an APM package of MAQ agentic engineering workflow skills for Fabric and Azure DevOps. The source of truth is `.apm\` (skills, agents, instructions). `apm.yml` declares the package and its external dependencies. Read `README.md` and `docs\` before larger changes.

## Operating principles

1. **Keep skill entry points short.** Every `.apm\skills\<name>\SKILL.md` must be under 200 words, counting frontmatter, headings, links, and code. `tests\contracts\validate_package.py` enforces 199.
2. **Expand through the skill folder, not the entry point.** Put SOP detail, contracts, and templates in `reference\`. Put deterministic actions (queries, file checks, formatting, API calls) in `scripts\`, and create it when a skill first needs one. `SKILL.md` links to each file with a relative link that resolves inside the skill folder. Workflow skills require `reference\contract.md` and `reference\procedure.md`.
3. **Keep commits small and readable.** Each commit is one logical change that a reviewer can read in about 10 minutes: aim for 200 changed lines or fewer, excluding generated files. Split larger work into a series. Use a plain-English imperative subject (72 characters or fewer) and a body that says what changed and why. Explain any commit over budget in its body.
4. **One uber goal per skill.** Each skill exists for one outcome. Before adding a skill, check the README skills table and `.apm\skills\`. If an existing skill already covers the goal, extend its `reference\` files instead. Shared behavior has one owner (for example, `/best-practices` is the central catalog), and other skills link to it instead of copying it.

## Safety (see `.apm\instructions\maq-safety.instructions.md`)

- Mutate DEV only. UAT and PROD are read-only.
- Never enable PR auto-complete, merge, bypass branch policies, or close or transition work items.
- Gate commits, pushes, PR creation, and ADO writes on approval of the exact operation.
- Never commit secrets, tokens, PATs, connection strings, or raw sensitive query results. Never embed a PAT in a URL.
- Do not reintroduce `maq-fabric-*` adapter skills. Fabric skills come from `microsoft/fabric-skills` through APM.

## Validate before you commit

Run these after any change under `.apm\`, `docs\`, `tests\`, `project-config\`, `README.md`, or `apm.yml`:

```powershell
python -m pip install -r tests\contracts\requirements.txt   # once: test-only TOON decoder
python tests\contracts\validate_package.py
python tests\contracts\test_fixtures.py
```

Both must print `PASS`. Fix failures before committing. Do not edit the validators to make them pass.

## Conventions

- The package folder is `reference\` (singular). `references\` inside skill text is the consumer repo's output folder, such as `references\explorations\<id>\`.
- Project configuration is TOON (`project-config\maq-project.example.toon`). Do not add JSON config or schemas.
- Use backslashes in PowerShell commands and local-path prose. Use forward slashes in Markdown link targets.
- Do not hand-edit `.github\instructions\tokenguard-code-index.instructions.md` or `.github\agents\tokenguard-index-research.agent.md`. TokenGuard manages them, and they are gitignored.
- Make surgical edits. Do not rewrite a whole skill to change one rule.
