# Verify the user's completed task

Use this reference for execution QA. It supplements the shared baseline; it does not authorize effects outside the current task. For document-only work, propose these checks and keep them not-run.

## Define completion before interacting

Turn a screen or manual section into a user goal: for example, "download a customer list and read its Korean names" or "change a setting and find the same value after reopening." Record the expected outcome and its source. A control's presence is a separate check from the action it promises.

Follow a requested manual sequence. For each relevant section, record the task, actions actually taken, completion evidence, and remaining stage. Group related screens into one journey when appropriate; do not inflate coverage by counting each screenshot as a completed task. Do not add unsupported requirements such as persistence for a counter intended to reset.

## Use the interaction being evaluated

Use visible navigation and normal browser/device input. Browser automation is valid when it produces the relevant pointer, keyboard, or touch interaction. A script that invokes a handler, changes state, or opens a hidden route may support setup or diagnosis; it cannot establish that a person could perform the same step.

When relevant, move the pointer onto the target and inspect hover text/contrast before clicking; try the actual keyboard and focus path; use the device keyboard for input-format problems. DOM text being present does not prove that it is readable on screen. An injected hyphen does not prove that a numeric phone keyboard permits the user to enter it. Report limitations when the required input device is unavailable.

## Check the outcome beyond the button

Select checks that match the chosen task and its risks. This table is not a required matrix for every feature.

| Task | Evidence needed for completion |
|---|---|
| Download/export | Obtain the actual file; check its format/content rather than its extension alone, relevant rows/columns, and representative Korean text. Open it in the intended reader when available. If only a parser was used, report that limit; do not claim spreadsheet compatibility. An HTML/login response saved with a CSV name is not a successful export. |
| Save/edit a value | Submit an authorized test change, then reopen or reload the relevant record and compare the value. If the task promises the value on another screen or role, check that destination when available. A toast or local preview alone does not prove persistence. |
| Upload an image | Use a permitted test file; inspect the immediate preview and the stored image after reopening. Check the receiving screen if that is part of the task. Existing images elsewhere do not verify a new upload. |
| First-use notice/onboarding | Follow the specified first-use and return conditions, including restart or relogin when relevant. Do not invent how long dismissal must persist when the requirement is unknown. |
| Password/account change | With an authorized test account and a recovery path, check the promised result through the relevant authentication flow. An empty-form validation check does not verify a completed change. Never expose credentials in evidence. |
| Submit with validation or confirmation | Enter representative permitted values and complete the applicable steps. If an error occurs, record the exact last action and stage. If a supplied note omits the stage, keep it unknown instead of adding a Save click or confirmation step. |

Record the observed failure even when its cause is unknown. Do not continue dependent actions as if a failed save or upload had succeeded.

## Execute allowed checks; isolate real blockers

Apply the baseline's environment and side-effect checks. Existing authorization remains valid. When an action is in scope and the affected test data/services are verified, perform the check and its agreed cleanup; do not silently reduce it to viewing a form because it writes data.

A dev label or test login alone does not establish an isolated database, recipient list, payment provider, or notification service. If one of these boundaries is unresolved, pause only the affected operation. State the missing condition and the exact step it blocks, use an authorized isolated alternative if available, and continue independent checks. Do not repeatedly request permission already given. Do not treat approval to edit this skill as standing approval for future app actions.

## Compare equivalent states and preserve usable evidence

For manual/report comparisons, align the build/date, role, record, screen/tab, filter, scroll/loading state, and environment as far as evidence allows. Compare the same UI element: a table column, summary metric, and filter tab are different things. If a control is found elsewhere, test the visible navigation path; this can resolve an absence claim while leaving a discoverability concern. A different account or build does not disprove the original report.

Distinguish a documented limitation from a regression or a missing requirement. A UI label that says an integration is unavailable establishes what the screen communicates, not independently verified backend behavior.

Follow the Screenshot option in SKILL.md: live QA defaults to ON; OFF forbids new capture, including recapture. With ON, preserve the starting/result states and defect evidence for each tested case, then open the saved images and verify that the relevant state is legible. Recapture unusable evidence when possible and permitted. Otherwise retain any supported textual observation and explicitly mark the visual evidence missing or disabled. A white image alone does not identify whether capture failed or the app rendered a blank screen; keep that cause unknown until the UI or capture process supplies evidence. Manual/example screenshots are reference images, not proof of the current run. Redact sensitive data without hiding the detail needed to assess the finding.

In the report, use `task | expected completion | actions performed | observed result | status | evidence | remaining check`. Keep existing case statuses: `passed` needs completion evidence, `failed` needs an observed mismatch, and `blocked`/`not-run` need a reason. Describe partial coverage in actions and remaining checks; never roll it up as a pass. Report task counts separately from screen counts, with explicit denominators if numbers are useful.
