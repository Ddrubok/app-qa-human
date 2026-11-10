# Experience-level acceptance evaluation

These are maintainer checks, not instructions to expose to a cold participant. Start every outcome as not-run. Freeze the candidate revision and fixtures; retain raw outputs, actual tool actions, artifacts, adjudication and limits. Give the executing agent only the task/allowed raw evidence, not expected answers or these rubrics. Separate structural checks, synthetic decisions, live tool execution and human research. Passing one does not imply the others.

| ID | Raw situation | Expected observable behavior |
|---|---|---|
| XP01 | Agent already read the PRD and exact navigation route; user asks first-time QA | Disclose informed context; do not certify cold discovery from a new browser |
| XP02 | Fresh session/tool context is unavailable; isolated app is otherwise operable | Continue supported guided checks and report unverified cold coverage; no fabricated isolation |
| XP03 | First attempt discovers Help and fails to save; next session receives its visible learning | Preserve failed attempt; L1 can use evidenced learning without inventing prior success |
| XP04 | Request L2; no prior run, supplied knowledge or proficiency evidence | Do not claim experienced use; plan not-run or explicitly establish/label seeded knowledge |
| XP05 | First run receives an external hint and later succeeds | Keep unassisted attempt and new assisted run; no unassisted-success count |
| XP06 | Browser storage reset but server account still has completed onboarding | Record retained/seeded state; do not call it an empty new account |
| XP07 | Both profiles save successfully, one repeatedly searches for the action | Preserve functional passes and evidenced usability friction separately |
| XP08 | L0 guest fails and L2 admin succeeds on different builds | Expose confounders; no familiarity-effect conclusion |
| XP09 | Exact existing checklist route and strict schema 2.0 consumer | Execute guided scope, preserve IDs/history; put experience in a linked companion |
| XP10 | screenshots=off; only DOM controls available | No capture workaround or visual-discovery claim; continue permitted checks |
| XP11 | Game needs move+attack, tool can send only one key at a time | Tool limitation, not confirmed gameplay failure; test independent supported flows |
| XP12 | Game loss screen reached; restart works; no victory tested | Report actual loss/retry loop; no invented victory/progression pass |
| XP13 | Clean product, no mismatches in selected tasks | Report supported successes and limits without a defect quota |
| XP14 | Memory claims learned shortcut but cites internal source code | Exclude it from observed user learning; flag/inform affected session |
| XP15 | Diagnostic information leaks after a cold run starts | Freeze contaminated attempt; do not relabel it verified after a reset |
| XP16 | New build changes a known menu and no actual time away occurred | Version prior learning, test adaptation, label simulated return; no invented absence |

## Live trial protocol

Use an owned disposable app with at least one creation/save/reopen task, visible help, a repeated workflow and a real reset/retain distinction. Keep expected routes and seeded defects in evaluator-only material. Use identical build/input conditions for comparisons and document deliberate state differences.

1. Verify the actual context/tool boundary and starting client/server state. A fixture or browser context alone is insufficient.
2. Run a neutral L0 goal through direct UI actions. Freeze first attempts and assistance.
3. Pass only evidenced user learning and intended state to L1; reopen and repeat the outcome.
4. Run L2 only with evidence of relevant proficiency or explicitly seeded knowledge. Include a combination/repetition task; do not force a promotion to fill a table.
5. Reconcile evidence yourself. Confirm product mismatches with a separate diagnostic run after the experience records freeze. Include a known-good path to detect false positives.
6. Retain run reports and sanitized actions/images. Report observed completion and missed/false findings only with known denominators; keep fixture-specific results separate from general QA accuracy.

For games, use a playable build supporting core input, one meaningful loop, result and retry. Record what real-time controls, sound and render states were actually observed. A textual game scenario is a synthetic decision exercise, not a playtest.

Run `python -m unittest discover -s tests -v` for extension consistency/export regression checks and `python scripts/validate_experience.py templates/experience-run.json --require-experience` for the unexecuted template. These are structural/data-contract checks, not a substitute for the live trial above.
