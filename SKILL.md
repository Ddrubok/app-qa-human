---
name: app-qa-human
description: Direct, evidence-based QA for apps, websites, desktop products and games, with optional first-time/returning/practiced-user comparisons. Use for app-qa-Human, 사람처럼 QA, functional or exploratory QA, experience-level playtests, checklist execution, PRD test cases, bug reports or store review risk. Preserve explicitly selected app-qa and narrow requests; do not claim representative human research or subjective enjoyment without suitable evidence.
---

# app-qa-Human

Operate the product through available tools, verify the user's outcome, and report supported findings in the user's language. Keep QA rigor constant when varying product familiarity. Do not invent human credentials, feelings or a finding quota; zero defects is valid.

## Choose scope before loading product knowledge

Default to one scoped QA pass, not a profile campaign. An ordinary request such as “check saving” uses the compact workflow below. A first-use perspective does not certify an independently cold participant. Only explicit experience/learning questions require the detailed profile protocol; `mode=full` alone does not request multiple profiles.

Read [baseline](references/baseline.md) for evidence, permissions, privacy, diagnosis and severity. For live/visual work also read [screenshots](references/screenshots.md): live capture defaults ON, explicit OFF persists, and report-only work never authorizes new captures. Do not recursively load every linked file. Read additional references only at the matching trigger:

| Request or need | Additional reference |
|---|---|
| First-time discoverability, named profile, or experience-level claim | [Experience profiles](references/experience-profiles.md); select the knowledge boundary before reading PRD/code/old reports. A cold participant gets only [participant protocol](references/participant.md) and a neutral task packet. |
| Repeated-use learning, L1/L2/Lapsed or `profile=compare` | Also [Session memory](references/session-memory.md). Preserve observed versus seeded knowledge and independent versus linked attempts. |
| Game journey | [Gameplay](references/gameplay.md); core input, meaningful loop, result and retry. |
| Complex completion check: export/upload, multiple destinations or lifecycle persistence | [Task completion](references/task-completion.md). Simple save/reopen follows the compact workflow. |
| Unfamiliar input/device tool or uncertain capability | [Tool execution](references/tool-execution.md). Existing familiar tooling needs no adapter reread. |
| Mistake/interruption/recovery is in scope | [Human error patterns](references/human-errors.md); choose relevant variations only. |
| Existing human or development checklist | [Checklist handoff](references/checklist-handoff.md); preserve IDs, expectations, history and supplied routes. Do not create a competing audit. |
| JSON/XLSX, full coverage, PRD test cases, bug-note normalization or report comparison | [Cases and reports](references/cases-and-reports.md); generated cases remain not-run and supplied evidence stays attributed. |
| Store/release policy risk | [Store review](references/store-review.md); current official sources required for policy conclusions. |
| Company standards or past-bug retrieval | [Knowledge retrieval](references/knowledge.md); do not expose diagnostics to a cold participant. |
| Evaluate this skill or compare revisions | [Evaluation](references/evaluation.md); maintainers additionally use [Experience evaluation](references/experience-evaluation.md) for profile changes. |

These are Markdown instructions, not a bundled automation server or CLI argument parser. Resolve references relative to the skill. Use the host's available browser/device/native/image/shell tools; missing capabilities limit claims. Honor project instructions and delegation restrictions; this skill never requires parallel agents.

## Compact direct QA

1. Identify target/build, goal, expected outcome and its basis, environment, permitted effects and necessary tools. Reuse established authorization. State important unknowns. If the requested check needs a cold participant, take the profile branch above before inspecting product internals; if isolation cannot be established, continue useful checks labeled informed/unverified.
2. Follow the requested scope and sequence. Choose actions from the visible interface and normal input. A prescribed route is guided testing. Record the relevant initial state; a source-discovered route or injected handler does not demonstrate user discoverability or input reachability.
3. Execute the ordinary path through its real result: for a save, reopen/reload and compare the value when persistence is promised. For a download, inspect the actual file. A button, screen visit, HTTP success or toast alone does not prove completion. If blocked, retain the last completed stage and exact remaining check; continue independent authorized work.
4. Select only useful edge/recovery checks. Preserve setup/reset between attempts and evidence before leaving a failure. Capture relevant start/result states when ON and inspect saved images when possible. Missing/uninspected images limit visual claims, not automatically functional outcomes.
5. Record the observed attempt before diagnosis. Test the strongest benign explanation and reproduce where feasible. Distinguish functional defects, usability friction, requirements gaps, policy risks and unknowns. Keep first failures and helped retries; a later success does not erase them. Do not claim a cause, frequency or changed behavior without evidence.
6. Report supported outcomes, consequential findings, successful checks, evidence and gaps. Keep a practical retest for each proposed correction. A code-confirmed issue is not your runtime reproduction; an AI rewrite is not an independent discovery. Do not expand QA-only scope into fixes, deployments or external posts.

## Report proportional to the task

- `mode=quick` (default): concise Markdown. State build/environment and screenshot limits once, then use `goal / expected basis | actions and actual outcome / status | evidence | remaining check`. For a defect add its impact, reproducible steps, expected/actual mismatch and retest. Keep important findings even when the report is short.
- Ordinary one-off QA needs no campaign IDs, learning ledger, experience JSON, seven-area table or action counters. A relevant note about prior knowledge or a hint is enough; it must not be promoted into a cold/learning claim. Preserve evidence and required cleanup regardless of presentation length.
- `mode=full`: explicit coverage and detailed findings through the case/report reference; it does not imply all tests ran. Output format is independent of depth. Honor strict JSON without surrounding prose and preserve existing schema/status contracts.
- Profile/learning comparisons: use the optional [experience report](templates/experience-report.md) and [JSON example](templates/experience-run.json) only as needed. A single Markdown file can hold separately identified attempts. Preserve knowledge basis, state, assistance and first attempts; no fake experience to fill a level. Keep task completion separate from usability friction and cold validity. Never infer human timings, satisfaction or population success rates from AI sessions.

For full coverage use these seven default areas, or the user's mapped categories: functionality/business rules; usability/visual/accessibility; interruptions/lifecycle; exceptions/network/recovery; data/permissions/privacy; compatibility/performance/reliability; distribution/operations. Mark covered, partial, not-tested or not-applicable with reasons. A coverage row is not a passed test.

## Tooling and delivery

Use existing tools; do not install a QA stack, engine, RAG service or backend merely to invoke this skill. `screenshots=off` also prohibits indirect or automatic capture workarounds. Separate tool failures from product failures.

Write a substantial review to the project's report location; a small review may be inline. Keep IDs stable on rechecks and preserve prior evidence. External tickets/messages default to drafts; posting requires an identified destination and task authorization. For authorized retries inspect existing IDs before reposting. Propose reusable knowledge only from supported lessons, separating observation, cause, fix and verified regression. Do not claim permanent learning or deployment from writing a report.
