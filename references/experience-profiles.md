# Experience profiles

Use for live product QA and level comparisons. Keep evidence standards constant; vary product knowledge, task choices and familiarity. L0 is not an incompetent tester, and L2 is not an omniscient developer. Separate product familiarity from domain/genre literacy, input proficiency, account permissions and device conditions. Do not infer any of these from age, nationality or a fictional personality.

## Select a useful scope

Treat `profile=L0|L1|L2|Lapsed|compare` as natural-language request shorthand, not a CLI parser or installed runner. Honor equivalent wording and existing narrow requests. Default an unspecified exploratory review to L0, with its actual knowledge limits disclosed. A checklist, regression test or supplied route remains guided execution; do not replace it with a new campaign. `mode=quick|full` still controls report depth, independently of profile and format.

| Profile | Allowed starting knowledge | Behavior and focus |
|---|---|---|
| L0 — first-time | Neutral task, ordinary browser/device literacy, declared domain literacy; product facts learned visibly during this attempt | Find a start, interpret labels, learn controls, reach a useful first outcome and recover using visible affordances |
| L1 — returning | Verified user-visible learning from a prior attempt, or explicitly declared seeded knowledge | Repeat a known task, reopen its result, resume progress; notice repeated tutorials, lost preferences and unnecessary rediscovery |
| L2 — practiced | Evidence-backed command of relevant core tasks and multiple mechanics, or declared seeded knowledge | Use known efficient paths, combine features, repeat work and inspect advanced outcomes; never use undiscovered internals |
| Lapsed — returning after change | Versioned prior user knowledge with known gaps | Reorient after a changed build or interruption; check changed labels, obsolete routes and preserved state |

For `compare`, choose shared outcome goals and run L0 → L1 → L2 only as far as the available experience and scope support. Freeze the L0 attempt before carrying its learning to L1. L1 needs prior use, even if that use was unsuccessful; do not require or invent a prior success. L2 needs demonstrated relevant proficiency, not a fixed number of sessions or a win count. Do not force failures or pretend to forget. If experience is insufficient, report L2 not-run, or use explicitly labeled seeded/mixed knowledge when appropriate to the request. Never relabel a seeded run as acquired proficiency.

Distinguish a **learning sequence** (linked runs; state and knowledge intentionally carried forward) from an **independent profile comparison** (separate contexts and aligned declared starting states). A sequence is not several independent users. One AI can execute sequentially; delegation is optional and subject to host/user authorization. Never require parallel agents or shared reset operations.

## Separate setup, experience and diagnosis

1. Coordinator: establish build, permitted effects, isolated test data, tools, goal and observable completion basis. Read requirements/checklists and keep solution paths, old findings and diagnostics private. Do not silently dismiss onboarding or seed preferences for a cold run. A new browser with an existing server account is not a new user.
2. Participant: receive only [participant.md](participant.md), a neutral task packet and allowed observations. Do not pass this coordinator guide, evaluation rubrics or product reports. Record user-visible attempts and learning as they happen.
3. Freeze: retain the first attempt, failures, assistance and ending state. Copy only user-visible learning into [Session memory](session-memory.md).
4. Diagnose: inspect code, DOM, console, backend and old findings as needed. For later learning sessions use an isolated context with sanitized learning only; otherwise disclose informed knowledge. Diagnosis does not rewrite the first attempt into a success.

Example neutral task: “Change the study reminder to the evening.” A packet saying “Open Settings, then Notifications” prescribes the solution and makes that check guided. If the user supplies a route, honor it and label it guided; do not claim cold discovery. For an existing checklist, the coordinator retains stable IDs/expectations under checklist-handoff.md and maps neutral goals back afterward. Do not modify that shared contract or require the companion skill.

## Verify the knowledge boundary

Inspect the actual context and tool access, not just the role name. Check inherited conversation, automatically loaded project instructions, memory, prior reports, repository access and tool responses. A fresh browser does not clear model context. A new worktree does not isolate knowledge. Never ignore mandatory host instructions; if they expose product internals, disclose the limitation.

Use a genuinely new session with a minimal packet when available. If the host supports isolated workers, do not fork the parent conversation; verify what the worker actually receives. A mechanical coordinator can execute a participant's selected action and return a neutral result, but must not coach. Do not install an orchestration service just for this skill.

Record boundary status independently of functional case status:

- `verified`: the declared knowledge/input boundary was inspected and supported by recorded setup evidence; no prohibited exposure is known. This is a procedural claim, not proof of erased pretraining knowledge or human equivalence.
- `informed`: product information or a prescribed route was known before execution. Continue useful guided testing; exclude it from cold-discovery counts.
- `contaminated`: a claimed isolated attempt received prohibited information after starting. Freeze the affected record; any clean replacement gets a new run ID. Later functional checks may still be useful, but do not restore cold validity by assertion.
- `unverified`: context/tool isolation could not be established. Continue supported checks with the limitation, not a claimed cold result.

For **visual discovery**, give current viewport images and ordinary visible cues. Do not expose hidden/offscreen DOM, source, full-page text extraction, internal route names, console/network results or backend state. Use normal pointer, scrolling, keyboard and touch actions; do not force-click through overlays or invoke handlers. Accessibility testing may use the actual assistive surface and must be labeled `observation_mode=assistive`, not evidence that the same control was visually discoverable. Guided execution may use robust locators and diagnostic tools.

Respect `screenshots=off`. Do not capture indirectly. If visual discovery cannot run without capture, mark it unverified/not-run as appropriate and continue permitted guided or assistive checks; do not describe a DOM-only pass as visual novice testing. A supplied screenshot supports only its displayed state unless further live observations exist.

## Assistance, stopping and outcomes

Let L0 read product help and tooltips it discovers. Record in-product help separately from external assistance. An external hint ends the unassisted attempt: preserve it and start a linked assisted attempt with a new run ID. A hinted L0 is informed, even if its goal is later completed. Never count that success as unassisted discovery.

Set reasonable task-specific action/time/recovery limits before running; use user limits when provided. A practical starting experiment may allow two recovery attempts at one obstacle, but this is not a claim about human patience. Stop at an unsafe action, unavailable capability, repeated obstacle or agreed limit. Do not random-click to generate defects. Record product-visible waits separately from tool/model overhead; AI elapsed time is not a human completion time.

Judge task completion and friction separately. A successful save may still require confusing navigation. An agent's confusion is an observed session event, not proof all beginners are confused. A failed task needs an observed expectation mismatch to become a confirmed product defect; capability limits, missing credentials and experiment limits have separate explanations. Never fabricate emotions, satisfaction ratings or population-level success rates.
