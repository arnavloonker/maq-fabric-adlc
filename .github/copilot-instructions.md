# Copilot instructions: maq-fabric-engineering

This repo is an APM package of MAQ agentic engineering skills for Fabric and Azure DevOps. The source of truth is `.apm\` (skills, agents, instructions), and `apm.yml` declares the package and its dependencies. Read `README.md` and `docs\` before larger changes.

## Every session

1. Ask what a human would have to do, then write that down as a structured step or SOP in skill format.
2. Keep the repo clean. Do not create scratch, planning, or note files here; use the session folder instead.
3. Write guidance as plain, natural sentences for humans. Do not add code or scripts unless they are needed as an external reference.

## Skills

- A skill takes open-ended user context, synthesizes it, and directs it to a defined outcome. Ask for or enforce additional details only when they are required to produce a valid result.
- Each skill folder contains `SKILL.md` and a `references\` folder. Workflow skills require an outcome definition (`references\outcome.md`) and a procedure (`references\procedure.md`). Put every mode in its own `references\modes\<mode>.md` file.
- `SKILL.md` is the concise entry statement: when to use the skill, what context it accepts, which references to read, and the essential routing or stop conditions. Keep it under 200 words (the validator enforces 199), counting frontmatter, headings, links, and code.
- The outcome definition (`references\outcome.md`) defines the input-to-output setup: required or optional inputs, defaults, output shape, modes, invariants, and completion criteria. User context is the default input unless the outcome requires more.
- The procedure (`references\procedure.md`) is the agentic sequence of steps that transforms the inputs into the specified output, including discovery, decisions, execution, validation, and reporting.
- Modes are packaged context for producing or representing different outcomes. Each mode file may change the procedure path, output structure, or presentation so the user can quickly understand the result and take the next action.
- Put detailed guidance in `references\`, mode context in `references\modes\`, and deterministic actions in `scripts\`, created only when first needed. Link every referenced file from `SKILL.md`.
- Each skill has one goal. Check the README skills table first, and extend an existing skill's `references\` files instead of adding a near-duplicate. Shared behavior has one owner, such as `/best-practices`; link to it rather than copying it.

## Commits

Keep each commit to one logical change, ideally 200 changed lines or fewer. Use an imperative subject of 72 characters or fewer and a body explaining what and why.

## Validate before committing

After changing `.apm\`, `docs\`, `tests\`, `project-config\`, `README.md`, or `apm.yml`, run `python tests\contracts\validate_package.py` and `python tests\contracts\test_fixtures.py` (first install `tests\contracts\requirements.txt`). Both must print `PASS`. Never edit the validators to make them pass.

## Conventions

- `references\` is both the skill resource folder and the conventional consumer output root; use the surrounding path and wording to distinguish package guidance from generated project evidence.
- Project configuration is TOON (`project-config\maq-project.example.toon`); do not add JSON config or schemas.
- Use backslashes in local paths and forward slashes in Markdown link targets.
- Do not hand-edit the TokenGuard-managed files under `.github\instructions\` and `.github\agents\`.
- Make surgical edits instead of rewriting a whole skill.
