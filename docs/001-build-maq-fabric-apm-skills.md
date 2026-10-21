---
id: 001-build-maq-fabric-apm-skills
title: "Build MAQ Fabric Agentic Engineering APM Skill Package (First Deliverable)"
labels:
  - ready-for-agent
status: open
---

## Problem Statement

PMs, tech leads, and data engineers delivering Microsoft Fabric projects on Azure DevOps (ADO) lack a portable, governed, and repeatable set of agent skills that span the full delivery lifecycle. Today, discovery hypotheses, data modeling, ADO story authoring, vertical task slicing, workspace-isolated TDD implementation, adversarial verification, PR impact briefs, and sprint status tracking happen through ad-hoc prompts or disconnected tools. Without a standardized Agent Package Manager (APM) package, teams suffer from:

- **Late or missing test seams**: Engineers begin building pipelines, notebooks, or semantic models before agreeing on how the outcome will be verified, resulting in rework or unverified claims.
- **Silent architectural assumptions**: Agents guess consequential design choices (such as Spark vs. Warehouse, key uniqueness, or grain) instead of interrogating the user one question at a time with a recommended default.
- **Horizontal task slicing and DEV workspace collisions**: Medallion tasks get split horizontally by layer ("all bronze, then all silver") rather than thin vertical tracer bullets, and concurrent engineers overwrite shared live Fabric DEV artifacts.
- **Context bloat and inconsistent tool flows**: Oversized skill files consume context windows, ignore central best practices, or mutate ADO/Fabric state without preview, approval, or revision safety.

## Solution

Build the `maq-fabric-engineering` APM producer package targeting GitHub Copilot CLI (`targets: [copilot]`). The package ships ten human-facing workflow skills (`/brainstorm`, `/to-story`, `/domain`, `/approach`, `/to-tasks`, `/implement`, `/verify`, `/code-diff`, `/status`, `/best-practices`), internally maintained Fabric workload adapters covering the full Fabric workload catalog, a separate `maq-adversarial-reviewer` agent, safety instructions, a versioned capability matrix, and minimal platform dependencies in `maq-project.toon`.

Every skill entry point (`SKILL.md`) is strictly under 200 whitespace-delimited words and uses progressive disclosure (`reference/contract.md`, `reference/procedure.md`, and optional `script/` helpers) to guide preferred ADO and Fabric MCP/CLI flows, automatic `/best-practices` consultation, one-question-at-a-time grilling, vertical tracer-bullet slicing, workspace/prefix DEV isolation, fast-feedback TDD around a single highest-level seam, and human-only work-item closure.

## User Stories

1. As a PM or tech lead, I want to invoke `/brainstorm` on a data product, architectural framework, or new Fabric workload ask, so that I can test hypotheses against repository code and live Fabric data before committing to a build.
2. As a PM or tech lead, I want `/brainstorm` to interrogate me one question at a time with a recommended answer whenever a hypothesis or requirement is ambiguous, so that we converge on clear decisions without overwhelming multi-question forms.
3. As a PM or tech lead, I want `/brainstorm` to profile candidate grain, key uniqueness, join completeness, and sample reconciliations for data asks, so that broken data assumptions are refuted early.
4. As a PM or tech lead, I want `/brainstorm` to support explicitly approved, bounded DEV scratch experiments with mandatory cleanup, so that we can prove or refute new Fabric workload capabilities safely.
5. As a PM or tech lead, I want `/brainstorm` to save sanitized exploration findings under `references\explorations\<id>\findings.md` with provenance and timestamps, so that downstream skills and teammates can reuse the evidence.
6. As a PM or tech lead, I want to invoke `/to-story` to synthesize our agreed exploration or conversation into an ADO User Story, so that engineers receive structured business context, decisions, acceptance criteria, examples, and explicit open questions.
7. As a PM or tech lead, I want `/to-story` to automatically consult `/best-practices` for ADO User Story guidance before drafting fields, so that every story follows MAQ standards.
8. As a PM or tech lead, I want `/to-story` to preserve any existing Technical Approach section and apply fixed package classification tags (`platform-architecture`, `data-engineering`, `experiment`) using revision-checked updates after preview and approval, so that concurrent edits are never overwritten.
9. As a team member, I want to invoke `/domain` to create or incrementally update one Markdown file per business domain under `domain\<business-domain>.md` plus `domain\index.md`, so that agents and engineers share a single business vocabulary and source-of-truth map.
10. As a team member, I want `/domain` to keep its vocabulary section free of implementation details while recording source systems, data products, reviewed rules, provisional observations, and explicit conflicts in dedicated sections, so that inferred code behavior is never confused with authoritative business policy.
11. As a data engineer, I want to invoke `/approach` in `data-model`, `architecture`, or `experiment` mode to write a build-ready before/after technical specification into the story's dedicated approach section, so that implementation requires zero consequential guesswork.
12. As a data engineer, I want `/approach` to validate baseline assumptions against the repository and live Fabric artifacts and interrogate me one question at a time with a recommended answer when contradictions appear (such as duplicate keys), so that flawed specs are never marked ready.
13. As a data engineer, I want `/approach` to define the draft Verification Contract anchored to a single highest-level Fabric seam (such as gold row counts, key uniqueness, and a DAX measure against a known value), so that TDD and final verification test the exact same boundary.
14. As a data engineer, I want `/approach` to apply the fixed `build-ready` tag to the ADO story only when all consequential decisions are resolved and the seam verification contract is approved (and remove it if blockers reopen), so that build readiness is visible in ADO.
15. As a data engineer, I want to invoke `/to-tasks` on a story to decompose the work into thin vertical tracer-bullet tasks across bronze, silver, gold, semantic model, and report rather than horizontal medallion-layer tasks, so that each task delivers verifiable end-to-end value within one fresh context window.
16. As a data engineer, I want `/to-tasks` to run a one-question-at-a-time quiz-until-approved loop on slice granularity before previewing and creating ADO child tasks and dependency links, so that task sizing matches engineering expectations.
17. As a data engineer, I want `/to-tasks` to reconcile existing child tasks on timeout or re-invocation, so that duplicate ADO tasks are never created.
18. As a data engineer, I want to invoke `/implement` on a story or selected task to work inside a dedicated Git branch and worktree while preserving any dirty existing worktrees, so that local changes never collide.
19. As a data engineer, I want `/implement` to isolate live Fabric DEV state using a mapped feature-branch workspace when supported by the capability matrix and pre-created, or fall back to deterministic `<branch_slug>_` item/table prefixing in the shared DEV workspace, so that concurrent engineers never overwrite each other's live Fabric artifacts.
20. As a data engineer, I want `/implement` to automatically consult `/best-practices` for each target Fabric and ADO artifact type (such as notebooks, pipelines, semantic models, and pull requests) and load only the relevant linked guidance on demand, so that implementation adheres to central standards without context bloat.
21. As a data engineer, I want `/implement` to execute a fast-feedback TDD loop anchored to the `/approach` seam (optimizing data-ask test queries via partition filters/sample keys and architectural changes via narrow parameter windows) from Red to Green before proposing a PR, so that defects are caught in seconds.
22. As a data engineer, I want `/implement` to delegate workload-specific mechanics to internal forked Fabric adapter skills governed by a versioned capability matrix, and report unsupported automation paths as `blocked` or `manual-only` with clear manual instructions, so that no skill improvises unsafe mutations.
23. As a data engineer, I want `/implement` to preview and approval-gate commits, pushes, PR creation, and ADO progress updates while never enabling PR auto-complete, bypassing policies, or closing work items, so that humans retain final merge and closure authority.
24. As a data engineer, I want to invoke `/verify` on a story and commit/artifact version to run an independent `maq-adversarial-reviewer` agent against the story's approved Verification Contract from `/approach` (or propose and approve a contract first if `/approach` was skipped), so that implementation claims are independently audited.
25. As a data engineer, I want `/verify` to execute permitted seam checks, invalidate stale evidence if commits or live artifacts drift, issue a truthful verdict (`passed`, `failed`, `blocked`, or `inconclusive`), and preview an ADO story comment with reproducible test-case evidence, so that reviewers have trustworthy proof before closing a story.
26. As a PM, tech lead, or engineer, I want to invoke `/code-diff` on an ADO PR to get an unslopped plain-language Markdown and Mermaid impact brief anchored to the PR's native review/merge diff baseline, so that I can quickly see what changed, before/after topology, downstream impact, and intended vs. verified outcomes.
27. As a PM, tech lead, or engineer, I want `/code-diff` to optionally compare the PR against linked ADO story, approach, and verification records and offer to save the brief under `references\pull-requests\<repo-id>\<pr-id>\<review-version>.md`, so that review context can be preserved when needed.
28. As a PM, tech lead, or engineer, I want to invoke `/status` to view a read-only personal sprint summary for the signed-in user in the configured team's current iteration, including labeled related parent/child/dependency context, actual ADO states, explicit or clearly labeled inferred phase, bounded chronology, and remaining actions, so that I have an accurate daily operational view without fabricating completion percentages.
29. As a skill author or engineer, I want `/best-practices` to maintain a central-package-only catalog of guidance links grouped by Fabric and ADO artifact type, stay silent when optional entries are absent, surface real retrieval failures or consequential conflicts, and propose additions/updates via an approval-gated PR or patch against the central source repository, so that standards evolve cleanly across all consumer projects.
30. As a platform maintainer, I want every packaged `SKILL.md` (both the 10 workflow skills and all forked Fabric specialist adapters) to be strictly under 200 whitespace-delimited words, pass link and schema validation, and track upstream provenance and licenses in `upstream-sources.json` and `THIRD-PARTY-NOTICES.md`, so that the package stays lightweight, auditable, and maintainable.

## Implementation Decisions

- **Three-Layer Contract Separation**:
  - **APM Manifest (`apm.yml`)**: Uses only documented APM fields (`name`, `version`, `description`, `targets: [copilot]`, `includes: auto`, `dependencies`, `scripts`). Never embed project-specific ADO or Fabric settings in `apm.yml`.
  - **Platform Dependencies (`maq-project.toon`)**: Six ADO identifiers/placement settings (`organizationUrl`, `project`, `team`, `repository`, `areaPath`, `iterationPath`) and three Fabric workspace lists (`devWorkspaceIds`, `uatWorkspaceIds`, `prodWorkspaceIds`). No schema, architecture decisions, policy switches, or maintenance settings.
  - **Runtime Procedures & Guardrails**: Enforced through `.apm\instructions\maq-safety.instructions.md`, `.apm\agents\maq-adversarial-reviewer.agent.md`, and per-skill `reference\contract.md` and `reference\procedure.md` files.
- **Strict `< 200` Word Entry-Point Budget with Progressive Disclosure**:
  - Every complete `SKILL.md` file (including YAML frontmatter, headings, links, and code blocks) in `.apm\skills\<name>\SKILL.md` must contain at most 199 whitespace-delimited words.
  - Each `SKILL.md` acts as a fast router that identifies inputs/outputs, instructs the agent to load `reference\contract.md` and `reference\procedure.md` (plus mode-specific references where applicable), triggers scoped `/best-practices` consultation, and states approval/stop gates.
- **Ten Workflow Skill Modules**:
  - `brainstorm`: Hypothesis framing, one-question-at-a-time grilling loop with recommended answers, data-model feasibility profiling (grain, keys, join completeness, reconciliation), read-only default with approval-gated bounded DEV scratch experiments and cleanup, output to `references\explorations\<id>\findings.md`.
  - `to-story`: Synthesizes agreed context into ADO User Story fields, consults `/best-practices` for ADO User Story, preserves the Technical Approach section, applies classification tags, uses optimistic concurrency (`Test` on `/rev`), reconciles timeouts, never closes items.
  - `domain`: Incremental updates to `domain\index.md` and `domain\<business-domain>.md`; separates implementation-free business vocabulary from source mappings, reviewed rules, provisional observations, and explicit conflicts.
  - `approach`: Supports `data-model`, `architecture`, and `experiment` modes (`reference\data-model.md`, `reference\architecture.md`, `reference\experiment.md`). Validates baseline evidence, interrogates consequential conflicts one question at a time with a recommended answer, defines the single highest-level **Seam** and draft **Verification Contract**, updates the story's dedicated approach section, and manages the fixed `build-ready` marker.
  - `to-tasks`: Enforces vertical end-to-end tracer-bullet slicing sized to a single context window (forbidding horizontal medallion-layer tasks), runs a one-question-at-a-time quiz-until-approved granularity loop, and creates/reconciles child tasks and dependency links in ADO.
  - `implement`: Isolates local code in a dedicated Git branch/worktree (preserving dirty worktrees) and isolates live Fabric DEV state via a mapped feature-branch workspace (when supported/pre-created) or deterministic `<branch_slug>_` item/table prefixing in shared DEV. Consults `/best-practices`, runs a fast-feedback Red-Green TDD loop against the `/approach` seam using minimal query/parameter windows, delegates to internal Fabric adapters, and previews commits/PRs/ADO updates without enabling auto-complete or closing work items.
  - `verify`: Reuses the approved Verification Contract and seam from `/approach` by default (proposing one for approval only if `/approach` was bypassed). Dispatches `maq-adversarial-reviewer` in a separate context, executes permitted seam checks, detects stale commits/artifacts, and previews an ADO story comment with `passed`, `failed`, `blocked`, or `inconclusive` test-case evidence.
  - `code-diff`: Anchors to the PR's native review/merge diff baseline, compares against optional story/approach/verification references, and outputs an unslopped Markdown + Mermaid change/impact brief (optionally saved under `references\pull-requests\<repo-id>\<pr-id>\<review-version>.md`).
  - `status`: Read-only personal sprint summary for the signed-in user in the configured team's current iteration (resolved dynamically, never from static creation `iterationPath`), with labeled related context, actual ADO states, explicit or labeled inferred phase, bounded chronology, and remaining actions.
  - `best-practices`: Central-package-only link catalog (`.apm\skills\best-practices\reference\catalog.md`) grouped by Fabric and ADO artifact type. Supports automatic scoped consultation (on-demand reading of relevant links, quiet on missing optional entries, explicit on retrieval failures or consequential conflicts) and `propose-add`/`propose-update` maintenance via approval-gated PR or patch to the central source repo.
- **Internal Fabric Specialist Adapters & Capability Matrix**:
  - Forked internal specialist skills (`maq-<fabric-specialist>`) cover all Fabric workload families (Data Engineering, Data Factory, Data Warehouse, Databases, Real-Time Intelligence, Data Science, Power BI, Fabric IQ, Industry Solutions, and Cross-workload platform/CI-CD).
  - Governed by `capability-matrix.json` tracking `branchWorkspaceSupport`, `sharedWorkspacePrefixFallback`, `toolBindings`, `authoringPath`, `validationPath`, `manualFallback`, and `status` (`planned`, `validated-dev`, `blocked`, `manual-only`, `deprecated`).
- **Fixed Skill Contract**:
  Skills and shared safety instructions define DEV-only mutation, read-only UAT/PROD, branch-workspace or `<branch_slug>_` isolation, 250-row/60-second query bounds, vertical one-context-window tasks, one-question-at-a-time approval, seam-anchored TDD, separate-context verification, fixed tags, and human-only closure. These are not consumer options. Best-practices source resolution uses the installed APM dependency metadata; unresolved sources yield a proposed patch only.

## Testing Decisions

- **What Makes a Good Test**:
  - Test observable external behavior at the compiled and installed consumer package boundary, never internal authoring drafts in isolation.
  - Verify that installing the package into a clean consumer repository produces valid, link-complete, word-budget-compliant primitives and rejects any configuration or capability-matrix fixture that violates safety invariants.
- **Single Agreed Test Seam**:
  - **The APM Package Compilation & Scratch Consumer Install Boundary (`apm install --target copilot` + Contract Validator Suite)**:
    1. Package installation into a scratch consumer repo deploys all 10 workflow skills and internal Fabric specialist adapters to `.agents\skills\<name>\SKILL.md` and deploys `maq-adversarial-reviewer.agent.md` to `.github\agents\`.
    2. Every deployed `SKILL.md` has `< 200` whitespace-delimited words (<= 199 words including frontmatter) and passes `apm audit` with zero hidden-Unicode or frontmatter/directory-name drift errors.
    3. Every relative link inside deployed skills (`reference\contract.md`, `reference\procedure.md`, mode files, and `reference\catalog.md`) resolves to an existing regular file inside the deployed skill bundle without escaping the root.
    4. The official TOON decoder parses the minimal template, filled values, and multi-workspace arrays, and rejects malformed inputs. Package contracts reject retired policy settings and verify fixed safety rules in skills/instructions; capability-matrix contracts prevent unsupported DEV validation claims.
    5. Behavioural contract fixtures verify that each of the 10 skills declares its required inputs, preferred tool bindings/substitutions, automatic `/best-practices` consultation hook, single-question grilling loop (where applicable), seam/TDD handoff, and approval/reconciliation rules.
- **Prior Art**:
  - Python TOON, word-count, link, and fixed-policy contract checks validate the package and minimal platform template.
  - APM's documented producer validation flow (`apm install --dry-run --target copilot`, `apm install --target copilot` in a scratch consumer, and `apm audit`).

## Out of Scope

- Executing live mutations against production or UAT Microsoft Fabric workspaces (strictly prohibited in v1).
- Claiming `validated-dev` status in `capability-matrix.json` for Fabric workload operations before they have been exercised with recorded evidence in an authorized DEV environment.
- Building custom MCP servers from scratch (the package governs and orchestrates existing/approved ADO and Fabric MCP servers, CLI tools, and SDK helpers).
- Supporting non-Copilot agent targets (`claude`, `cursor`, `windsurf`, etc.) in the first release (`targets: [copilot]` only).
- Automatic work-item state closure, automatic PR merge/auto-complete, or automatic consumer lockfile upgrades when central best practices change.

## Further Notes

- Full blueprint reference: `C:\Users\v-arloonker\.copilot\session-state\6fd1efbf-e684-4840-9063-42a2186f6aab\files\maq-fabric-apm-blueprint.md`
- Platform dependency template: `project-config\maq-project.example.toon`; no companion schema.
- Next step in the workflow: run `/mattpocock-skills:to-tickets` (or `/to-tasks`) against `001-build-maq-fabric-apm-skills.md` to slice the package build into vertical implementation tickets.
