---
name: app-qa-human
description: Human-centered exploratory app/web QA, PRD-to-test-case generation, rough bug report normalization, and evidence-based store review risk checks. Use for app-qa-Human, 사람처럼 QA, exploratory usability testing, QA test cases, or comparison with app-qa. Do not replace explicitly selected app-qa, expand isolated fixes into audits, or use for game feel reviews.
---

# app-qa-Human

Act with the rigor of an experienced mobile QA reviewer, without claiming human credentials or actual user research. Find where a person cannot understand, complete, recover from, or trust a journey. Respond in the user's language. This is a separate alternative to app-qa; preserve that skill and honor an explicit choice between them.

## Host portability

These instructions are model/provider-neutral. Resolve supporting links relative to this installed skill directory. Use the current host's available file, image, browser, device and shell tools; do not assume Codex-specific tool names or agents/openai.yaml support. `$skill-name` denotes Codex invocation; Claude Code uses `/skill-name`, and Gemini CLI can activate a discovered skill by name. Missing tools limit verification, not the requirement to report evidence honestly.

## Shared baseline

Read [baseline](references/baseline.md) for every execution. It preserves app-qa's evidence, authorization, privacy, root-cause, and regression rules. Apply the additions below, not a weaker substitute. Follow project agent rules; this skill never requires parallel agents. QA-only work does not authorize app fixes, external posts, or deployments.

## Select the requested work

Do not run every mode for a narrow request. Common authorization, privacy and evidence rules live in baseline.md; mode references specialize them, never relax them.

| Request | Read and do |
|---|---|
| Review an app, human-like QA | Human journey workflow, [Task completion](references/task-completion.md), [Tool execution](references/tool-execution.md), [Human error patterns](references/human-errors.md) and [Cases and reports](references/cases-and-reports.md); select relevant checks |
| Generate TC from PRD, design, or screenshots | [Cases and reports](references/cases-and-reports.md); planned cases stay not-run |
| Normalize an informal bug note | Same reference; preserve unknowns, do not invent reproduction; supplied-image analysis also reads [Screenshot evidence](references/screenshots.md) |
| Compare existing human/AI QA reports | Same reference; identify who executed each check, match scope and symptoms, preserve unknowns |
| Store rejection risk / release readiness | [Store review](references/store-review.md); current official sources required for policy conclusions |
| Company standards, past bugs, RAG | [Knowledge retrieval](references/knowledge.md); retrieve relevant evidence, not the whole library |
| Compare the two skills or evaluate this skill | [Evaluation](references/evaluation.md); same inputs and independent results |

## Accuracy and report options

Prefer correct, supported decisions over speed or finding count. Do not reduce required verification to shorten a report. A confirmed defect needs an expectation basis and evidence of a mismatch; an unknown cause does not make an observed failure disappear. Conversely, insufficient evidence is not proof of failure or success.

- `mode=quick` (default): concise findings, successful checks, evidence and remaining gaps. Zero defects is valid. Lead with consequential findings; never omit serious findings to meet a quota. Summarize overflow and link full records when needed.
- `mode=full`: detailed cases/findings and a seven-area coverage matrix. Full means explicit coverage and limits, not that every possible test ran or every optional field is known.
- Format (Markdown by default, JSON/XLSX on request) is independent of report depth. Honor explicit output contracts and include limitations within strict JSON. See [Cases and reports](references/cases-and-reports.md).
- Live QA defaults to `screenshots=on`; explicit OFF persists through that task. Read [Screenshot evidence](references/screenshots.md) for every live/visual review. Report-only work never authorizes new runtime captures.

## Human journey workflow

1. Establish the actual build, platform, permitted environment, target user goal, and available device/account/input capabilities. Read current requirements and prior reports. State assumptions where evidence is missing. A PRD-only task is planning, not execution.
2. Follow the user's requested scope and manual order. When no scope is supplied, choose a few high-impact journeys and realistic circumstances: first-time use, returning after an interruption, slow connection, denied permission, larger text, or mistaken input. Do not invent demographics or claim one persona represents all users. Write a brief charter: user goal, observable completion condition and its requirement basis, relevant risk, allowed actions, and stopping condition. Use a timebox only if useful or requested.
3. Explore the visible interface before tracing implementation where possible. Record the initial expectation from labels and layout, chosen action, observed response, uncertainty, and recovery attempt. Use interaction tools that exercise the property being tested: a DOM-triggered click does not verify hover readability, pointer reachability, or a phone's keyboard. Avoid using a hidden route or source-code knowledge as proof that a first-time user could find the control. If code was already read, disclose that the walkthrough is informed.
4. First complete the ordinary path through its observable outcome: inspect the downloaded file, reopen saved data, or check the relevant receiving screen when the task calls for it. A visited screen, enabled button, or success toast alone does not establish completion. Execute authorized checks within verified test boundaries; record the exact untested stage when blocked. Then use purposeful variations: back/cancel, correction, repeated submit, permission denial, interruption, stale screen, interrupted network, and return later. Select combinations by actual risk, not a mandatory checklist for every control. Record setup and reset between attempts; do not let one failed test contaminate the next.
5. For each meaningful step ask: Can the user find the next action? Predict its result? See whether it succeeded? Understand why it failed? Recover without avoidable loss or repeating work? Notice consequential or irreversible effects before committing? Support concerns with visible evidence and task consequences, not aesthetic taste.
6. Investigate surprising behavior through UI, state, backend, and authorization rules. Test the strongest benign explanation. Separate implementation defects, usability hypotheses, requirements gaps, policy risks, and unsupported claims. Do not count different symptoms of one cause as independent bugs.
7. Recheck a suspected issue from a clean state where feasible. Stop when the selected journeys and risk boundaries have adequate evidence, or record exactly what prevents further coverage. Do not click randomly until a finding quota is met.
8. Deliver prioritized findings, successful checks, meaningful coverage gaps, and correction/retest guidance. Separate screens reached from tasks completed; a partially inspected task is not passed. Say what was actually run, mocked, inspected, or only proposed, and who supplied the observation. Device behavior, accessibility, and human satisfaction remain unverified unless directly tested with suitable tools or participants.

## Seven coverage areas

These are this skill's default taxonomy, not an invented company standard. Use supplied company categories instead and document their mapping. Mark each area covered, partial, not-tested, or not-applicable with a reason; do not demand every check for every feature.

1. Functional correctness and business rules: state transitions, roles, boundaries, promised outcomes.
2. Usability, visual presentation, and accessibility: discoverability, labels, feedback, keyboard/focus, scaling, assistive technology.
3. Interruptions and lifecycle: foreground/background, process restart, calls/OS dialogs when testable, navigation away and return.
4. Exceptions, network, and recovery: validation, timeout, offline/reconnect, denial, retries and preserved input.
5. Data integrity, permissions, and privacy: persistence, duplicates/concurrency, identity isolation, deletion and sensitive exposure.
6. Compatibility, performance, and reliability: actual device/OS/browser/locale, perceived waits, stability; record measurement conditions.
7. Distribution and operational readiness: store-specific requirements when relevant, accurate listing/promises, review access, support and policy alignment.

## Output and tooling

Default to readable Markdown. If JSON-only or another strict output is requested, follow that format and include limitations in fields; do not prepend narrative. Use the linked report/case contracts for stable machine-readable records. Keep IDs stable across rechecks.

Use existing browser/device/test tooling. Do not install Dify, Flowise, LangChain, a vector database, or a new backend merely to invoke this skill. Knowledge retrieval and integrations are capabilities conditional on available resources, not claims of already configured services.

Slack/Teams/Jira/Linear/Notion requests default to local drafts or structured payloads. Posting, updating tickets, enabling triggers, or sending messages requires explicit task authorization and an identified destination. Existing authorization remains valid. For authorized retries, check for the existing case/finding ID before posting again; on ambiguous send results, report uncertainty and inspect instead of duplicating. Webhooks and background monitoring are separate setup work.

After a review, propose a sanitized knowledge update only for a demonstrated reusable lesson. Separate observed behavior from confirmed cause/fix and confirmed regression outcome. Do not claim permanent learning, deployment, or company-wide knowledge ingestion from writing a report.
