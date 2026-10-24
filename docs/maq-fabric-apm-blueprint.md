# MAQ Fabric agentic engineering: APM blueprint

Status: confirmed design, not an implemented or installed package.

## 1. Product boundary

A centrally maintained, internally forked skill package for PMs, tech leads, and engineers delivering Microsoft Fabric projects through Azure DevOps (ADO). The outcome is shorter lead time from a request to tested delivery without sacrificing quality.

Ten human-facing skills form a vocabulary, not a mandatory pipeline:

| Skill | Primary users | Result |
| --- | --- | --- |
| `/brainstorm` | PMs and tech leads | Evidence-led hypothesis testing, feasibility findings, and candidate models |
| `/to-story` | PMs and tech leads | An understandable ADO story with decisions and acceptance criteria |
| `/domain` | Anyone | Reviewable, source-backed business-domain knowledge |
| `/approach` | Engineers | A build-ready before/after technical specification in the story |
| `/to-tasks` | Engineers | Outcome-based child tasks with dependencies |
| `/implement` | Engineers | Isolated implementation, documentation, findings, and proposed PR |
| `/verify` | Engineers | Independent adversarial review and agreed test evidence |
| `/code-diff` | Anyone | Plain-language PR change/impact brief with highlighted Before/After views |
| `/status` | Anyone | Read-only personal sprint progress, chronology, and remaining actions |
| `/best-practices` | Anyone and other skills | Relevant centrally maintained guidance links and proposed catalog updates |

Any skill can be invoked directly. Missing prerequisites are resolved locally or reported; invoking a skill never silently authorizes architectural decisions, external publication, or deployment.

## 2. Domain vocabulary

**Story:** The ADO record of intended outcome, business context, acceptance criteria, decisions, and unresolved questions. Its current requirement is authoritative over copied reference snapshots.

**Hypothesis:** A proposition about feasibility, semantics, or expected behavior that exploration can support, refute, or leave inconclusive.

**Approach:** The build-ready technical change specification recorded in a dedicated section of a story, identifying current and proposed artifact behavior, the agreed test seam, and the draft verification contract. It is not a second requirement document.

**Seam:** The highest-level boundary where a change is tested end-to-end (aiming for one: e.g., gold row counts, key uniqueness, and a DAX measure against a known value). Defined in `/approach` and exercised by `/implement` (TDD) and `/verify`.

**Build-ready marker:** The fixed `build-ready` ADO tag applied by `/approach` only when all consequential decisions are resolved and the test seam/verification contract are approved.

**Task:** A thin vertical tracer-bullet slice (one entity/metric end-to-end across bronze, silver, gold, semantic model, and report) sized to a single fresh context window under a story, with explicit dependencies.

**Domain:** A business responsibility and vocabulary with identified ownership. A source system, workspace, or bronze/silver/gold layer is not automatically a domain.

**Domain record:** Reviewed knowledge plus clearly labeled provisional observations about a domain.

**Reference:** A reusable, provenance-bearing project finding, decision-support document, or evidence record. Creation does not make it authoritative.

**Verification contract:** Engineer-approved criteria, scope, target version/environment, checks, and evidence expectations for one story.

**Fabric runtime skill:** A skill provided by the external `microsoft/fabric-skills` APM dependency and invoked directly by a workflow skill.

**Capability:** A documented operation whose support status depends on its direct runtime skills, available tools, permissions, environment, and validation evidence.

**Change brief:** An explanation of an identified PR review change set, separating observed changes, inferred impacts, intended outcomes, and verified results.

**Status snapshot:** A time-bounded view of the signed-in user's sprint work, with related work labeled as context rather than ownership.

**Practices catalog:** A central-package directory of guidance links grouped by artifact type. It is not a project-local policy database or evidence of having followed every linked practice.

## 3. Three separate contracts

1. **APM distribution:** `apm.yml`, package primitives, pinned dependencies, and lockfile. APM distributes context and gates installation; it is not the runtime authorization engine. [S1-S5]
2. **MAQ platform dependencies:** consumer-root `maq-project.toon`, containing only ADO connection/placement identifiers and Fabric DEV/UAT/PROD workspace ID lists. No schema or workflow policy.
3. **Runtime execution:** Skill procedures, available MCP/tool schemas, native tool approvals, scoped credentials, and Fabric/ADO permissions.

Written instructions and schema constants express required behavior. They do not prevent a model, user, or external client from bypassing it. Strong guarantees require independently enforced permissions and runtime controls.

## 4. Package and consumer layout

Paths below are relative Windows paths.

```text
maq-fabric-engineering\
  apm.yml
  apm.lock.yaml                         generated when dependencies are resolved
  README.md
  THIRD-PARTY-NOTICES.md
  upstream-sources.json                 source, revision, license, internal delta
  project-config\
    maq-project.example.toon
  capability-matrix.json
  tests\
    contracts\
    fixtures\
    integration\
  .apm\
    instructions\
      maq-safety.instructions.md
    agents\
      maq-adversarial-reviewer.agent.md
    skills\
      brainstorm\
        SKILL.md                       fewer than 200 words, complete file
        references\
          outcome.md
          procedure.md
          evidence-template.md
        scripts\                       only when an executable helper is needed
      to-story\
      domain\
      approach\
        references\
          modes\
            data-product.md
            platform.md
            experiment.md
      to-tasks\
      implement\
      verify\
      code-diff\
      status\
      best-practices\
        SKILL.md
        references\
          outcome.md
          procedure.md
          catalog.md                   links grouped by artifact type only
```

Each workflow directory has the same `SKILL.md` and `references` pattern. A `scripts` directory is optional; do not create empty scaffolding for its own sake. Fabric and Azure DevOps skills are external APM dependencies, not copied into this package.

APM documents conventional `references` and `scripts` resource directories and whole-skill-folder deployment. Mode-specific context lives under `references\modes\`. Treat preservation of those names as a package compatibility acceptance check, not a newly invented APM feature. [S3-S4]

```text
fabric-project\
  apm.yml
  apm.lock.yaml
  maq-project.toon
  domain\
    index.md
    <business-domain>.md
  references\
    index.md
    explorations\
      <stable-exploration-id>\
        findings.md
    pull-requests\                     optional saved Markdown change briefs
      <repository-id>\
        <pr-id>\
          <review-version>.md
    status\                            only saved when requested
      <snapshot-id>.md
    stories\
      <story-id>\
        observations\
          <run-id>.md
        verification\
          <run-id>\
            contract.json
            evidence.md
            results.json
  .agent-tmp\                           ignored scratch outputs
  .agents\skills\                       APM-managed Copilot skill output
  .github\agents\                       APM-managed Copilot agents
```

Package skill `references` files are operating instructions. Consumer-root `references` files are project knowledge/evidence. Never write project observations into installed package resources.

The practices catalog lives exclusively in the central package. Do not create a consumer `references\best-practices` catalog. A project may record evidence that a practice was considered, but must not turn that record into a competing catalog.

Resolve the consumer repository root through Git, not the agent's incidental working directory. Read `maq-project.toon` there only for required platform dependencies. Resolve bundled support files relative to the installed skill. Reject paths that escape the intended root, including through symlinks/junctions.

## 5. APM manifest skeletons

Producer manifest, using documented APM fields: [S1-S3]

```yaml
name: maq-fabric-engineering
version: 0.1.0
description: MAQ workflow and Fabric engineering expertise
targets:
  - copilot
includes: auto
dependencies:
  apm:
    - microsoft/fabric-skills
  mcp: []
scripts: {}
```

The official Fabric skill collection is resolved as an external APM dependency; its source files are not copied into this package. `includes: auto` is documented consent to include local package content, not a guarantee that only desirable files ship. Inspect the produced bundle before release; never keep customer artifacts or secrets in the producer tree.

Consumer skeleton:

```yaml
name: fabric-project
version: 0.1.0
description: Fabric delivery project
targets:
  - copilot
dependencies:
  apm:
    - git: https://dev.azure.com/REPLACE_ORG/REPLACE_PROJECT/_git/maq-fabric-engineering
      ref: REPLACE_IMMUTABLE_COMMIT
  mcp: []
scripts: {}
```

The Git URL and revision are placeholders, not a ready installation. Validate the selected APM release's private Azure Repos authentication and immutable-ref resolution in a scratch consumer. Never embed a PAT in the URL. Commit the generated consumer lockfile.

Do not add project-specific dependencies or approval settings to `apm.yml`. Put only ADO identifiers/placement paths and Fabric workspace IDs in `maq-project.toon`. Approval policy and native ADO field mappings live in skills/instructions; resolve the repository default branch at runtime.

MCP configuration is a deployment concern separate from simply naming a server. Onboard approved servers using the selected APM version's documented MCP format or supported local provisioning. Populate exact identities only after verification; empty lists do not provision ADO or Fabric connectivity.

## 6. Entry-point contract: fewer than 200 words

Count whitespace-delimited words in the entire `SKILL.md`, including YAML metadata, headings, links, and code. The maximum is 199. Enforce it for all packaged skills, including internal forks, and recheck deployed copies.

Every entry point must say:

1. What the skill produces and which inputs identify the scope.
2. Which bundled procedure to load next.
3. How it finds relevant project context and supporting capabilities.
4. Which approvals and stop conditions apply.
5. Where its result goes.

Example entry point, not a complete authored skill:

```markdown
---
name: to-story
description: Use when turning an agreed discussion into an Azure DevOps story.
---
# To story

Read [the outcome](references/outcome.md) and [the procedure](references/procedure.md).

Load `maq-project.toon` only for required platform identifiers and only relevant domain records and references.
Consult /best-practices for User Story guidance.
Extract intent, evidence, acceptance criteria, decisions, and blocking questions.
Never invent business context or resolve consequential decisions silently.

Discover the available Azure DevOps tools. Prefer reading project type metadata,
checking related work, previewing the field changes, then creating or updating
the story after approval. Follow the procedure for safe equivalent tools.

Preserve existing content, revision-check updates, and reconcile uncertain writes.
Read back the result and report its URL and unresolved blockers. Never close it.
```

Shortness cannot be achieved by hiding essential safety behavior in an unreferenced file. Avoid a giant shared manual that every invocation must load. Load the entry point, the applicable procedure, and only the branch-specific supporting material.

The ten workflow names are user-facing entry points; Fabric skills are invoked directly from the external APM dependency as needed. `/best-practices` also supports automatic scoped consultation by the other skills. Confirm invocation and name-collision behavior in the installed Copilot CLI version. APM packaging alone is not proof of slash-command discovery or human-only invocation. [S3]

## 7. Shared execution procedure

This is guided consistency, not strict determinism.

```text
Identify scope and consumer root
  -> resolve required platform identifiers from maq-project.toon
  -> load relevant domain/reference context
  -> consult /best-practices for applicable artifact types and linked guidance
  -> discover available tool schemas and directly installed Fabric skills
  -> read current external state
  -> choose documented procedure branch
  -> prepare changes or verification contract
  -> obtain required approval
  -> execute the approved bounded operation
  -> read back or reconcile the result
  -> record sanitized provenance and remaining blockers
```

Skills may run bounded research before a write decision. A missing task list does not prevent implementing an otherwise ready story. An unresolved consequential design choice does prevent affected implementation.

Other skills automatically consult `/best-practices` for the artifact types they inspect, author, update, or assess. Load only applicable linked pages. The catalog lookup must not require the entire authoring/onboarding configuration for a read-only consultation. `/best-practices` and its supporting procedures do not recursively invoke themselves.

An absent optional catalog entry need not be announced. A failed lookup/retrieval, an unchecked required standard, or a consequential conflict is not an empty lookup and must not be hidden. Do not claim a practice was consulted when it was unavailable. Catalog links do not replace approved project requirements or shared safety rules.

Tool substitution is allowed only when semantics, target scope, permissions, approval boundaries, and evidence remain equivalent. Record the substitution in the run findings. A read-only query tool is not equivalent to a generic SQL execution surface that could mutate data. A Fabric CLI helper cannot bypass a missing MCP permission.

On a write timeout, do not blindly repeat the operation. Inspect current work items, PRs, comments, or Fabric operations using scoped identifiers and recorded intent. If reconciliation is inconclusive, stop and report uncertainty. Do not pretend all external creates have idempotency keys.

Preserve concurrent changes. For ADO updates use the read revision where the discovered server supports revision tests. A conflict requires rereading and revising the preview, not overwriting the newer content.

## 8. Skill-specific contracts

### /brainstorm

Inputs: intent, relevant repository/story/artifact identities, allowed exploration scope.

Preferred flow: state the hypothesis and what would support or refute it; inspect code and domain index; consult artifact-specific practices and modeling expertise when relevant; resolve authorized Fabric artifacts; inspect schemas/definitions and bounded query results through directly installed Fabric skills/tools; elicit unresolved decisions from the user via a grilling loop (strictly one question at a time, always with a recommended answer); test alternatives and success criteria; record findings.

Branches: platform capability/framework feasibility, experiment/new workload, or data-product semantics and modeling feasibility. For a data ask, profile candidate grain, key uniqueness, joins, and sample reconciliations to establish whether the proposed model answers the requirement without distorting the data. This is exploratory modeling, not an implicit final implementation contract.

Read-only is the default. A hypothesis may require an explicitly approved, bounded DEV experiment with identified scratch artifacts, permissions, execution/time/cost limits, evidence expectations, and cleanup. Creation, execution, and cleanup are mutations within the approved scope; failed cleanup is reported. Do not promote an experimental artifact or write production code without a separate authorized scope.

Querying or executing an experiment is justified by a specific decision, not an automatic full scan or job run. Insufficient access produces an inconclusive finding rather than fabricated support.

Output: supported, refuted, or inconclusive hypotheses; evidence-backed choices; rejected alternatives; candidate models; explicit unknowns; and sanitized examples in `references\explorations\<id>\findings.md`. Findings identify source, timestamp, environment, query/definition version where available, and limitations.

Do not publish a story, mutate UAT/PROD, infer business intent as fact, or force `/to-story`. `/brainstorm` answers whether and why a direction is justified; `/approach` specifies exactly how the selected direction changes the system.

### /to-story

Inputs: conversation/selected exploration and optional existing story ID.

Preferred ADO flow: consult `/best-practices` for User Story; verify the native type/fields are supported; search related work; read the current story if updating; render and preview the field change set; obtain approval; create or revision-check update; read back. Stop dependent writes on an unsupported ADO process.

Story sections: outcome; evidenced business context; scope/non-goals; acceptance criteria; decisions; consequential open questions; exploration findings/examples; references; technical approach.

Preserve a current approach section when refreshing other sections. Propose fixed package tags `platform`, `data-engineering`, and `experiment` when applicable, preserving existing tags. Preview additions; these are not universal ADO tags.

A draft may retain blocking questions. The story must distinguish unresolved questions from requirements. Output includes the story URL and blockers, not a false ready-for-build claim.

### /domain

Inputs: selected domains or a request to discover candidate business boundaries.

Preferred flow: inspect repository sources and existing domain records; optionally validate against authorized live metadata/data; propose an incremental update with provenance and conflicts; preview existing-file changes.

One file per business domain, plus an index. Each file separates purpose/owner, canonical business vocabulary, source systems and data products, source-of-truth references, reviewed rules, provisional observations, and unresolved conflicts. Ownership not known is explicitly unknown.

Domain files are broader knowledge records, not pure glossaries. Keep the vocabulary section free of implementation decisions. Source metadata and provenance belong in separate sections.

Do not automatically treat code behavior as business policy, declare that a documentation folder establishes data-mesh governance, or erase human-reviewed definitions during regeneration.

### /approach

Inputs: story ID, consequential decisions, selected mode.

Preferred flow: read the story and relevant discovery findings; consult artifact-specific practices; inspect the current repository and relevant Fabric state through directly installed Fabric skills/tools; validate the baseline; resolve any open consequential choices or test-seam questions via a grilling loop (strictly one question at a time, always with a recommended answer); specify the chosen change and the draft verification contract anchored to the highest-level seam; preview and approval-gate a revision-checked update to the dedicated story section and fixed `build-ready` marker.

The specification identifies repository revision, live observation time and available artifact definition/version; current and proposed behavior; artifact-by-artifact changes; dependencies/interfaces; the agreed test seam and draft verification contract; and migration, compatibility, rollout/rollback where relevant. Aim for a single highest-level Fabric seam (for example: gold row counts, key uniqueness, and a DAX measure against a known value). For each artifact, make create/update/remove/no-change scope explicit. Proposed changes are not reported as already deployed outcomes.

"Deterministic" describes a sufficiently explicit implementation specification: the engineer should not have to invent consequential design choices. It does not promise identical tool calls, identical AI output, or a conflict-free external system.

Data-product mode: trace evidenced sources through ingestion, transformations, medallion layers, model grain/keys/history, pipeline orchestration, serving interfaces, operations, and the selected Seam. Select only consequential documentation views and explain omissions. Use source/mapping tables, lineage and orchestration flowcharts, and current/proposed Mermaid `erDiagram` views where relevant. Distinguish observed facts from proposed decisions; list unknown details and explicitly mark absent or unavailable baselines. Reuse discovery evidence, validating it when stale; do not repeat discovery merely to satisfy a workflow sequence.

Platform mode (reusable capabilities such as cross-cutting pipelines, logging, and frameworks): specify the platform need, current/proposed boundaries, consumer contract and adoption, compatibility, operability, dependencies, rollout/rollback, and parameter-window test seams. Reference the reasons for the selected alternative rather than restarting an unbounded options exercise.

Experiment mode: specify the selected experiment precisely, including baseline, artifact/configuration changes, bounded DEV execution, time/cost limits, measurements, acceptance of the learning result, and cleanup/rollback. `/brainstorm` may already have run discovery experiments; `/approach` does not need to duplicate them or turn them into production claims.

If inspection contradicts a consequential assumption, elicit a decision one question at a time with a recommended answer. When all consequential choices and the draft verification contract are approved, apply `build-ready`; if blocking questions remain or are reopened, omit or remove the tag. Missing access yields an explicit unvalidated assumption or blocker, not invented profiling results.

### /to-tasks

Inputs: story ID, current approach if needed, project sizing conventions.

Preferred flow: read the story, agreed seam, and existing children; propose thin vertical tracer-bullet slices; run a quiz-until-approved loop (one question at a time with a recommended answer) to calibrate slice granularity with the engineer; preview creation/link changes; obtain approval; create missing children and dependency links; read back.

Slice vertically end-to-end, never horizontally by medallion layer ("all bronze, then all silver" is forbidden). Each task traces one thin entity, metric, or capability across bronze, silver, gold, semantic model, and report (or across the relevant architectural seam), sized to fit a single fresh context window. Each task records scope, expected artifact, fast seam-test check, dependencies, and evidence expectations.

Task dependency direction and relation types must come from discovered ADO process capabilities. Reconcile partial creation and repeated invocations. Do not duplicate existing tasks or close them.

### /implement

Inputs: story and optional selected task IDs; authorized repository; implementation scope.

Preferred flow: read current story/tasks, build-ready status, agreed seam, and blockers; inspect Git status/worktrees; create a dedicated branch/worktree for the chosen scope without discarding existing work; isolate live Fabric DEV state using a mapped feature-branch workspace when pre-created and supported by the capability matrix, or fall back to the shared DEV workspace with deterministic item/table prefixing (`<branch_slug>_`); consult `/best-practices` for each applicable artifact type, such as notebook and PR; execute a fast-feedback TDD loop anchored to the approach seam; invoke applicable Fabric skills directly; implement code and documentation; run relevant checks.

Fast-feedback TDD loop: before writing implementation code for a slice, write a minimal, fast-running executable seam test (for data asks, optimize the test query via filtered partitions, sample keys, or bounded windows; for architectural changes, test narrow parameter windows), confirm it fails (Red), implement the slice, and re-run until it passes (Green).

Approved DEV authoring/execution is allowed when required by the selected direct Fabric skill and explicit change set. That is not authority to promote/deploy a release. Unsupported native item operations remain blocked with manual instructions.

Preview external updates and Git publication, including commits/pushes/PR creation as applicable. Publish only the approved change set. Link PRs/commits to work without requesting state closure.

Do not enable PR autocomplete, bypass policies, automatically merge, or automatically close items. Inspect repository automation for indirect state transitions; if publication would violate human-only closure, report the conflict before publishing.

Output identifies the exact commit, branch/worktree, Fabric workspace/prefix isolation used, TDD Red/Green evidence, PR if published, checks, untested areas, and outstanding blockers.

### /verify

Inputs: story ID and exact version under review, plus the verification contract defined in `/approach` (or an explicit contract if `/approach` was bypassed).

Reuse the story's approved verification contract and test seam from `/approach` by default. Only if no contract exists (because `/approach` was skipped) or scope/criteria changed, propose criteria, target commit/item definitions, environment, permitted tests, data limits, expected evidence, and cleanup before seeking engineer approval. Changed criteria or execution scope need renewed approval.

Launch a separate reviewer context with the story, applicable approach, exact diff/artifact versions, relevant domain records, and approved verification contract. It evaluates claims independently rather than accepting the implementer's summary.

Use executable checks only within approved scope. Record expected versus actual results, relevant tool/query identity, timestamps, environments, operation IDs, and sanitized evidence links. Recheck the target version before publishing; changed code or live artifacts make earlier evidence stale.

Verdicts: `passed`, `failed`, `blocked`, or `inconclusive`, each limited to the approved contract. A static review is not evidence that a Fabric job ran. Missing permissions, partial tests, or absent reviewer capability cannot produce a pass.

Preview and approval-gate an ADO story comment containing the test-case-style evidence summary. Formal ADO Test Case creation is not implied; it requires separately approved scope. Never fix code silently, approve/merge the PR, or close work items.

### /code-diff

Inputs: PR identity, optional review iteration/version, and optional story/approach/verification references.

Preferred flow: read PR metadata and the native review diff at identified source/target baselines; consult practices for the PR and affected artifact types; inspect changed definitions/code and evidenced dependencies through relevant Fabric skills/tools in read-only scope; read related ADO intent/evidence when available; produce the brief.

For completed PRs, use the recorded review/merge context rather than comparing current branch tips that may have moved. If the correct baseline or diff is unavailable, report that limitation rather than substituting an unrelated comparison. Paginate large diffs; identify unavailable, generated, binary, or truncated surfaces explicitly.

Output is Markdown: a concise plain-language explanation of what changed and why when known, paired Before/After views, direct/downstream impact, intended versus verified outcomes, and source links. Choose the appropriate format per meaningful change: structured tables, Mermaid artifact/diagram views, or fenced diff code blocks, rather than repeating every format. Anchor Before to the target review baseline and After to the source; highlight additions/changes, identify removals, and preserve unchanged context. Distinguish absent content from unavailable content. Label inferred lineage and impact; unknown relationships remain unknown. Do not invent business benefits or claim runtime success from static changes.

Optional existing PR relations or supplied references can connect the brief to story acceptance criteria, the technical specification, and verification evidence. Do not invent intent when those references are absent.

Offer to save under `references\pull-requests\<repository-id>\<pr-id>\<review-version>.md`; save only when requested. Respect existing-file preview rules. Do not claim Mermaid rendering was checked without actually rendering it. No automatic PR comments, work-item updates, approval votes, or verification verdict; any requested external publication requires a preview and approval.

### /status

Inputs: signed-in identity, configured ADO project/team, and optional explicit story/iteration/person filters.

Preferred flow: resolve the signed-in identity and the configured team's current iteration; consult relevant work-item practices; query the user's assigned stories/tasks in that iteration; fetch only related parents, children, and dependencies needed for context; inspect bounded relevant revisions/comments and linked PR/build events; summarize.

Use the resolved iteration, not the static `ado.iterationPath` used for new-item placement. If the current scope cannot be resolved uniquely, ask rather than guessing. Explicit filters must be reflected in the report scope. Related work assigned to others or outside the iteration is context, not the user's sprint ownership or a silently expanded personal workload.

Show scope, snapshot time, story/task hierarchy, actual ADO states, and an evidence-backed phase clearly labeled as inferred, or unavailable when evidence is insufficient. Task counts are not completion percentages. A PR merge is not evidence of deployment, and no observed verification record is not proof that verification never happened.

Show chronological relevant events with timestamps and source links from at most 30 days and 50 events, including linked PR/build events; label omitted history, access gaps, and unavailable linked data. Do not imply a complete audit trail or causation from timestamps. Identify blockers, waiting/dependency states, unverified claims, and grounded next actions.

The default result is read-only conversation output. Save a timestamped snapshot under `references\status\<snapshot-id>.md` only when requested. No silent work-item, PR, or sprint updates; any requested external publication remains previewed and approved.

### /best-practices

Inputs: consult, propose-add, or propose-update mode; Fabric/ADO artifact type; optional source link or existing catalog entry.

Consultation is automatic and scoped when another skill handles relevant artifacts. Read the installed central catalog, select applicable links from the artifact group, and retrieve only relevant pages through available tools. Apply actual source content, not advice inferred from link titles. Do not bulk-load the entire catalog or recursively invoke this skill.

The catalog contains links grouped by artifact type only, for example Fabric Notebook, Fabric Pipeline, ADO User Story, ADO Task, and ADO Pull Request. Keep the catalog a link directory: no per-entry rule schema, severity/rationale fields, automatic lesson adoption, or project-local copy. Contract and procedure details remain separate supporting documents.

An absent optional entry is unobtrusive; the caller may use official documentation through its normal procedure. Never fabricate a consulted source. Actual retrieval failures and required-standard gaps remain explicit; consequential conflicts pause the affected operation. Central links supplement, not override, approved project standards and shared safety.

Maintenance resolves the central source and pinned revision from the installed APM dependency metadata. Never assume the consumer repository is the source. Resolve the source default branch at runtime and preserve changes since the pin. Preview and obtain approval before Git publication or PR creation. If resolution or access fails, return a proposed patch and state that no catalog update was made. Never automatically merge, edit installed resources, update consumer pins, or accept generated suggestions as practices.

Reviewed central releases distribute accepted changes. Consumption stays at the pinned package version until explicitly updated. Record package/source revision and retrieval context in relevant run evidence, not as an expanded per-link catalog schema.

## 9. Preferred tool bindings

Names below were inspected in this session's available MCP schemas. Treat them as a reference profile, not a portable guarantee. Rediscover schemas during onboarding and after server changes.

| Operation | Inspected preferred tool family/action |
| --- | --- |
| Read story/type metadata/comments | `azure-devops-wit_work_item`: `get`, `get_type`, `list_comments` |
| Create/update story or task | `azure-devops-wit_work_item_write`: `create`, `update`, optionally `add_child` |
| Revision-safe field update | `updates` begins with `Test` on `/rev` using the revision just read |
| Evidence/progress comment | `azure-devops-wit_work_item_comment_write`: `add` |
| Link PR/commit to work | `azure-devops-wit_work_item_link_write`: `link_to_pull_request`, `add_artifact_link` |
| Inspect/create PR | `azure-devops-repo_pull_request`: `get`/`list`; `azure-devops-repo_pull_request_write`: `create` |
| Find report/model | `FabricIQ-DiscoverArtifacts` |
| Resolve supported artifact identity | `FabricIQ-ResolveFabricItem` |
| Query a semantic model | `FabricIQ-ExecuteQuery`, bounded DAX |

The inspected PR writer exposes autocomplete and work-item-transition controls. Never use them to enable automatic closure. PR descriptions have a server-declared 4,000-character maximum in this profile; link durable detail instead of silently truncating it.

Discover ADO search/query, team/current-iteration resolution, signed-in identity, PR iterations/diff baselines, linked builds, central-repository authoring, dependency linking, and attachment/upload schemas when their procedure needs them; do not invent argument shapes. `/status` should use read-only query/history surfaces; `/code-diff` should use PR review/diff surfaces. An unavailable read path is not permission to edit external records.

The inspected FabricIQ discovery tool supports semantic models and reports, not general discovery of every Fabric workload. Its DAX query tool is not Spark/SQL/KQL authoring. The current tool profile is not evidence that all-workload implementation is available.

Use directly installed Fabric skills for their documented scope. A skill's approved CLI/SDK helper remains subject to the same explicit permissions and safety boundaries; tool substitutions must be documented and equivalent, and do not receive broader authority. If no direct skill/tool covers an operation, report it as blocked or manual-only.

## 10. All-workload capability matrix

Use a versioned snapshot of the official Fabric workload catalog, then enumerate item types and operations. A row is an engineering contract, not a marketing claim. [S8]

Required dimensions:

```text
catalogVersion; documentationUrl; workload; itemType; operation;
runtimeSkills; toolBindings; requiredPermissions;
tenantAndCapacityPrerequisites; supportedEnvironments;
sourceControlSupport; branchWorkspaceSupport; sharedWorkspacePrefixFallback;
authoringPath; validationPath; manualFallback;
status; lastValidatedAt; validationEvidence; knownLimitations
```

Statuses: `planned`, `validated-dev`, `blocked`, `manual-only`, `deprecated`.

Initial catalog coverage must explicitly include:

| Area | Adapter coverage to enumerate |
| --- | --- |
| Data Engineering | Lakehouses, notebooks, Spark jobs/environments and related items |
| Data Factory | Pipelines, Dataflow Gen2, orchestration and applicable item types |
| Data Warehouse | Warehouses, SQL authoring and related integration |
| Databases | SQL database, mirroring, supported database experiences |
| Real-Time Intelligence | Eventstreams, Eventhouse/KQL, real-time dashboards and Activator |
| Data Science | Experiments, models, training/scoring workflows |
| Power BI | Semantic models, reports and supported dashboard operations |
| Fabric IQ | Ontology, graph, planning and agent item types as documented; mark previews |
| Industry Solutions | Specific supported solutions/items and their prerequisites |
| Cross-workload platform | OneLake, governance/catalog, Git integration, variable configuration, CI/CD and operational dependencies |

This list seeds the matrix; it does not claim every named item has an available direct skill or API. Industry/preview offerings must be checked against the chosen catalog snapshot. When no direct skill/tool binding is available, retain an explicit blocked or manual-only path.

All workloads remain v1 scope. Release cannot claim complete automated operation coverage just because each area has a skill. Every advertised automated operation needs DEV evidence. Explicit manual/blocked paths satisfy truthful handling of unavailable automation, not automated-support claims.

## 11. Fabric engineering rules

Apply medallion guidance to relevant data-product requests: bronze/raw, silver/enriched, gold/curated. Preserve raw-source provenance, specify transformations and quality expectations, and profile grain/keys/relationships before resolving the model. Do not impose three layers on unrelated transactional, real-time, framework, or experiment work. [S6]

Distinguish repository changes, workspace changes, execution, and promotion. Fabric documents Git integration with Azure DevOps/GitHub, deployment pipelines, APIs, CLI, variable configuration, and infrastructure-as-code options. Support varies by item and must be checked in the matrix. A successful PR is not proof of deployment or successful data execution. [S7]

Default reads are authorized, bounded, and purpose-specific. A row limit alone does not bound scan cost. Enforce query timeouts or budgets at the execution surface when supported; otherwise use an approved bounded alternative or report the limitation. Avoid collecting raw sensitive rows when schema/aggregate evidence suffices.

Approved DEV writes/executions only. UAT/PROD may be read within authorized scope, never mutated by v1 skills. A manual fallback cannot be an instruction to bypass that prohibition. Experiment cleanup is itself a mutation and must be included in the approved scope.

## 12. References, evidence, and approval

Every durable reference records its subject, source identifiers/locations, observation time, environment/version, authoring run, review status, sensitivity handling, limitations, and related story. Business rules distinguish reviewed facts, hypotheses, and unresolved conflicts.

Create new reference files non-destructively. Preview modifications to existing shared files, including indexes. Use stable identifiers plus collision-resistant run IDs. Preserve human edits.

ADO comments must include a readable summary even when full evidence is linked. Local paths are not clickable proof for remote teammates. Publish sanitized evidence through an approved repository commit or discovered ADO attachment path; until then, mark it local/unpublished.

Do not commit secrets, raw sensitive query results, tokens, connection strings, or logs containing them. Keep scratch output ignored. Domain records link to authoritative systems rather than duplicating sensitive datasets.

Approval is tied to a concrete operation set, targets, scope, and relevant version. A changed payload, target, environment, or materially different execution plan invalidates it. Publishing a repository reference, changing ADO content, and executing a DEV job are distinct operations even when approved together.

## 13. Platform dependency boundary

Copy `project-config\maq-project.example.toon` to the consumer Git root as `maq-project.toon`. There is no schema. Its only settings are:

- ADO `organizationUrl`, `project`, `team`, `repository`, `areaPath`, and creation `iterationPath`.
- Fabric `devWorkspaceIds`, `uatWorkspaceIds`, and `prodWorkspaceIds` arrays.

The template contains placeholders, not verified access. Resolve exact identities, environment mapping, native ADO types/fields, placement paths, permissions, and supported tool bindings during onboarding. Workspace IDs must be valid GUIDs and lists must not overlap. Reject policy keys and block dependent operations on missing, malformed, placeholder, or ambiguous values. Resolve the repository default branch and team's current iteration at runtime.

Safety, query limits (250 returned rows/60 seconds where supported), isolation, paths, readiness/classification tags, task sizing, TDD, verification, status/history, and practices maintenance are fixed in skills/instructions. Domain ownership belongs in domain records; package version belongs in the APM dependency pin. No policy, architecture decisions, or maintenance references belong in TOON.

Read-only repository brainstorming needs no unused live dependency. TOON parsing and contract checks validate the template and fixed policies; instructions guide approval behavior rather than providing a deterministic execution sandbox.

## 14. Internal fork and release policy

Record upstream repository/path, exact revision, license, required attribution, internal changes, maintenance owner, and compatibility for every fork. Verify reuse rights before importing content; inspiration does not authorize copying arbitrary published prose.

Preserve attribution and notices where required. Review upstream changes centrally; no automatic imports into project installs. Ship immutable, regression-tested releases with exact dependency resolution in lockfiles.

Avoid duplicating shared safety or domain logic in every fork. Generate small release-time shared fragments where appropriate, but validate the installed artifact and its references; do not rely on unbundled producer-only paths.

Validate all-workload coverage as a release gate, not an assumed property of importing an upstream Fabric skill collection.

## 15. Acceptance scenarios

| Scenario | Required result |
| --- | --- |
| A SKILL.md contains 200 words including metadata | Package validation fails |
| A forked specialist has an oversized SKILL.md | Same failure; no exemption |
| A deployed entry point references missing support files | Package validation fails |
| A PM directly invokes `/to-story` without `/brainstorm` | Works from supplied evidence; no compulsory sequence |
| A draft story leaves Spark versus Warehouse undecided | Affected implementation pauses for a decision |
| Existing story changed after preview | Revision conflict; reread and reapprove |
| Task creation succeeded but response timed out | Reconcile existing children; no blind duplicate |
| A required MCP tool is missing | Discover a safe equivalent or report blocked |
| An equivalent tool has broader mutation semantics | Do not substitute without an equivalent constrained contract |
| Raw sample rows contain sensitive values | Do not persist them as shared evidence |
| `/domain` conflicts with a reviewed business definition | Preserve it and surface conflict/provisional observation |
| `/brainstorm` creates a new finding | Non-destructive file creation is allowed; existing index edit is previewed |
| A brainstorm hypothesis fails reconciliation | Record refuted/inconclusive evidence; do not force a favorable result |
| A discovery experiment needs a scratch DEV artifact | Preview and approve creation/execution/cleanup within limits |
| Scratch cleanup fails | Report remaining artifacts and failure; no false cleanup success |
| A framework request uses `/approach` | Platform mode; no fabricated fact/dimension model |
| `/approach` discovers a duplicated key assumed unique | Interrogate one question at a time with a recommended answer; omit `build-ready` tag until resolved |
| `/approach` finishes with zero blockers and an agreed seam | Embed draft verification contract in story and apply `build-ready` |
| A before/after specification is published | Identify observed baseline and proposed state, not fictional deployment |
| `/to-tasks` is given a medallion story | Propose vertical end-to-end tracer bullets (never horizontal layer tasks) and quiz granularity one question at a time |
| Two engineers run `/implement` concurrently | Isolate live Fabric state via pre-created feature workspace or `<branch_slug>_` item/table prefixing in shared DEV |
| `/implement` starts a vertical slice | Run fast-feedback TDD against the approach seam (optimized query/parameter window) from Red to Green |
| An experiment is proposed | Hypothesis, limits, evidence, and approved cleanup, not production claims |
| `/implement` finds a dirty worktree | Preserve it; isolate selected work without destructive cleanup |
| PR automation could transition work-item state | Block conflicting publication pending human resolution |
| `/verify` runs on a story with an `/approach` contract | Reuse the approved seam and verification contract; only propose a new one if `/approach` was skipped |
| Separate reviewer unavailable | Report blocked; no same-context substitute claimed as independent |
| Static review passes; live tests were not run | Report only static result; do not claim execution passed |
| Commit or Fabric item changed after testing | Evidence marked stale; verify the new version |
| Evidence remains on one developer's machine | ADO summary says unpublished; no unusable local-path proof |
| A mutation targets UAT/PROD | Block even if requested by a skill or helper |
| Story/task appears complete | Report evidence; humans decide state closure |
| All workload families have skill names but no runtime evidence | Do not claim all-workload automated support |
| `/code-diff` inspects a completed PR after target branch moved | Use recorded PR review/merge context, not unrelated current tips |
| PR lineage or intent is unavailable | Label unknown; no invented downstream impact or benefit |
| A Markdown/Mermaid report was not rendered | Do not claim visual rendering was checked |
| `/status` finds the user's task under another owner's story | Include labeled related context, without changing personal scope |
| Current iteration is ambiguous | Ask for scope; do not use the configured creation iteration silently |
| Status history is truncated or partly inaccessible | Show limits/gaps; do not claim complete chronology |
| Phase is inferred from PR/task evidence | Label inference separately from actual ADO state |
| A report is generated without a save request | Keep it in the conversation; no automatic file/publication |
| Notebook authoring or story updates begin | Automatically consult relevant `/best-practices` artifact groups |
| A catalog has no optional artifact entry | Continue unobtrusively; do not claim nonexistent consultation |
| Catalog retrieval actually fails | Surface failure; distinguish it from an absent optional entry |
| A linked practice conflicts consequentially with required standards | Surface sources/scope and pause; shared safety cannot be weakened |
| A practice addition is proposed from a consumer project | Target central source PR/patch, not installed resources or local catalog |
| Central practice PR is accepted | Consumers remain pinned until explicitly updated |
| `/best-practices` consults its own catalog | No recursive self-invocation or bulk page loading |

Package checks should count complete skill files, verify links after scratch installation, validate project config fixtures, inspect forbidden mutation/closure paths, and exercise procedure fixtures including substitutions and failures. Use documented `apm install --dry-run --target copilot` and a scratch consumer installation to inspect placement; APM audit is additional install/content governance, not a substitute for behavioral tests. [S2-S5]

## 16. Implementation sequence

1. Build the internal source/provenance inventory and workload/operation matrix against a chosen Fabric documentation snapshot.
2. Implement configuration validation, shared reference conventions, central artifact-grouped guidance links, tool-discovery profiles, and approval/reconciliation procedures.
3. Author ten short entry points and progressively disclosed contracts/procedures; adapt/fork supporting expertise into the same constraints.
4. Prove ADO story/update/task/PR/comment behavior, personal sprint chronology, PR-baseline explanations, central catalog maintenance, and direct Fabric skill operations in authorized DEV environments, including partial-failure cases.
5. Validate a pinned package in a clean Copilot consumer, then release only the demonstrated capability claims.

This sequence is package development, not a mandatory end-user skill sequence.

## Sources and evidence

Official pages retrieved during this session; documentation is mutable. Pin source revisions and supported tool/APM versions when implementing the package.

- **S1:** APM overview: https://microsoft.github.io/apm/
- **S2:** First package, manifest fields, installation and consumer dependency: https://microsoft.github.io/apm/getting-started/first-package/
- **S3:** Skill structure, frontmatter, whole-folder deployment and Copilot paths: https://microsoft.github.io/apm/producer/author-primitives/skills/
- **S4:** Resource links and package-relative deployment: https://microsoft.github.io/apm/producer/package-relative-links/
- **S5:** Install-time governance, limitations, and runtime boundary: https://microsoft.github.io/apm/enterprise/governance-guide/
- **S6:** Fabric medallion guidance: https://learn.microsoft.com/en-us/fabric/onelake/onelake-medallion-lakehouse-architecture
- **S7:** Fabric CI/CD: https://learn.microsoft.com/en-us/fabric/cicd/cicd-overview
- **S8:** Fabric overview/workload catalog: https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview
- **S9:** Workflow inspiration, not the MAQ contract: https://www.aihero.dev/skills-to-spec
- **S10:** APM target matrix: https://microsoft.github.io/apm/reference/targets-matrix/

Tool-binding evidence: schemas inspected in-session for the named ADO and FabricIQ tools. No ADO/Fabric business data was queried or modified to create this blueprint.
