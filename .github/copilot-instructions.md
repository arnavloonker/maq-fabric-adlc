# Copilot instructions: maq-fabric-engineering

This repo is an APM package of MAQ agentic engineering skills for Fabric and Azure DevOps. The source of truth is `.apm\` (skills, agents, instructions), and `apm.yml` declares the package and its dependencies. Read `README.md` and `docs\` before larger changes.

## Every session

1. Ask what a human would have to do, then write that down as a structured step or SOP in skill format.
2. Keep the repo clean. Do not create scratch, planning, or note files here; use the session folder instead.
3. Write guidance as plain, natural sentences for humans. Do not add code or scripts unless they are needed as an external reference.

## Skills

- A skill takes vague input, synthesizes it, and directs it to a defined output.
- The contract (`reference\contract.md`) defines the output; the procedure (`reference\procedure.md`) is the SOP for synthesizing it.
- Modes are separate reference files in the skill; switch between them to produce a different outcome.
- Each `SKILL.md` stays under 200 words (the validator enforces 199), counting frontmatter, headings, links, and code.
- Put detail in the skill's `reference\` folder and deterministic actions in `scripts\`, created only when first needed. Link each file from `SKILL.md`. Workflow skills need `reference\contract.md` and `reference\procedure.md`.
- Each skill has one goal. Check the README skills table first, and extend an existing skill's `reference\` files instead of adding a near-duplicate. Shared behavior has one owner, such as `/best-practices`; link to it rather than copying it.

## Commits

Keep each commit to one logical change, ideally 200 changed lines or fewer. Use an imperative subject of 72 characters or fewer and a body explaining what and why.

## Safety (see `.apm\instructions\maq-safety.instructions.md`)

- Change DEV only; UAT and PROD are read-only.
- Never enable auto-complete, merge, bypass branch policies, or close or transition work items.
- Get approval for the exact commit, push, PR, or ADO write before doing it.
- Never commit secrets, tokens, PATs, connection strings, or raw sensitive query results.

## Validate before committing

After changing `.apm\`, `docs\`, `tests\`, `project-config\`, `README.md`, or `apm.yml`, run `python tests\contracts\validate_package.py` and `python tests\contracts\test_fixtures.py` (first install `tests\contracts\requirements.txt`). Both must print `PASS`. Never edit the validators to make them pass.

## Conventions

- `reference\` is the package folder; `references\` in skill text is the consumer repo's output folder.
- Project configuration is TOON (`project-config\maq-project.example.toon`); do not add JSON config or schemas.
- Use backslashes in local paths and forward slashes in Markdown link targets.
- Do not hand-edit the TokenGuard-managed files under `.github\instructions\` and `.github\agents\`.
- Make surgical edits instead of rewriting a whole skill.
