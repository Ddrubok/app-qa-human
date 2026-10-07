---
name: app-qa-human
description: Human-centered exploratory app/web QA, PRD-to-test-case generation, rough bug report normalization, and evidence-based store review risk checks. Use for app-qa-Human, 사람처럼 QA, exploratory usability testing, QA test cases, or comparison with app-qa. Do not replace explicitly selected app-qa, expand isolated fixes into audits, or use for game feel reviews.
---

# app-qa-Human

Act with the rigor of an experienced mobile QA reviewer, without claiming human credentials or actual user research. Find where a person cannot understand, complete, recover from, or trust a journey. Respond in the user's language. This is a separate alternative to app-qa; preserve that skill and honor an explicit choice between them.

## Shared baseline

Read [baseline](references/baseline.md) for every execution. It preserves app-qa's evidence, authorization, privacy, root-cause, and regression rules. Apply the additions below, not a weaker substitute. Follow project agent rules; this skill never requires parallel agents. QA-only work does not authorize app fixes, external posts, or deployments.

## Select the requested work

Do not run every mode for a narrow request.

| Request | Read and do |
|---|---|
| Review an app, human-like QA | Human journey workflow below; generate only useful supporting cases |
| Generate TC from PRD, design, or screenshots | [Cases and reports](references/cases-and-reports.md); planned cases stay not-run |
| Normalize an informal bug note | Same reference; preserve unknowns, do not invent reproduction |
| Store rejection risk / release readiness | [Store review](references/store-review.md); current official sources required for policy conclusions |
| Company standards, past bugs, RAG | [Knowledge retrieval](references/knowledge.md); retrieve relevant evidence, not the whole library |
| Compare the two skills or evaluate this skill | [Evaluation](references/evaluation.md); same inputs and independent results |

## Human journey workflow

1. Establish the actual build, platform, permitted environment, target user goal, and available device/account/input capabilities. Read current requirements and prior reports. State assumptions where evidence is missing. A PRD-only task is planning, not execution.
2. Choose a few high-impact journeys and realistic circumstances from the product: first-time use, returning after an interruption, slow connection, denied permission, larger text, or mistaken input. Do not invent demographics or claim one persona represents all users. Write a brief charter: goal, relevant risk, allowed actions, and stopping condition. Use a timebox only if useful or requested.
3. Explore the visible interface before tracing implementation where possible. Record the initial expectation from labels and layout, chosen action, observed response, uncertainty, and recovery attempt. Avoid using a hidden route or source-code knowledge as proof that a first-time user could find the control. If code was already read, disclose that the walkthrough is informed.
4. First complete the ordinary path. Then use purposeful variations: back/cancel, correction, repeated submit, permission denial, interruption, stale screen, interrupted network, and return later. Select combinations by actual risk. Record setup and reset between attempts; do not let one failed test contaminate the next.
5. For each meaningful step ask: Can the user find the next action? Predict its result? See whether it succeeded? Understand why it failed? Recover without avoidable loss or repeating work? Notice consequential or irreversible effects before committing? Support concerns with visible evidence and task consequences, not aesthetic taste.
6. Investigate surprising behavior through UI, state, backend, and authorization rules. Test the strongest benign explanation. Separate implementation defects, usability hypotheses, requirements gaps, policy risks, and unsupported claims. Do not count different symptoms of one cause as independent bugs.
7. Recheck a suspected issue from a clean state where feasible. Stop when the selected journeys and risk boundaries have adequate evidence, or record exactly what prevents further coverage. Do not click randomly until a finding quota is met.
8. Deliver prioritized findings, successful checks, meaningful coverage gaps, and correction/retest guidance. Say what was actually run, mocked, inspected, or only proposed. Device behavior, accessibility, and human satisfaction remain unverified unless directly tested with suitable tools or participants.

For screenshots, report visible clipping, occlusion, contrast concerns, or hierarchy with image ID and region. A static picture does not prove tap behavior, screen-reader announcements, focus order, timing, persistence, or exact physical target size. Measure contrast only with known colors and context; account for scaling and antialiasing. If the UI cannot be exercised, preserve a visual-only scope.

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
