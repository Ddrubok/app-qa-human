# Experience-level extension — development validation

Date: 2026-11-10. Base repository revision: `f192c22bbfb4cd3b48716aed8e886d09efe733fb`.

## Implemented scope

- L0/L1/L2/Lapsed profiles and a comparison campaign, with QA evidence standards held constant.
- Separation of coordinator knowledge, participant observations and post-attempt diagnosis.
- Provenance-aware learning and retained state; observed, seeded and mixed experience remain distinct.
- Optional experience extension 1.0 on schema 2.0, report templates and a dependency-free consistency checker.
- Direct game-loop and desktop/input capability guidance; no new engine, mobile stack or isolated-agent runner.
- Existing case statuses, checklist handoff, screenshot preferences and XLSX export behavior preserved.

## Validation performed

| Check | Result | What it establishes / does not establish |
|---|---|---|
| Python regression suite | 14 tests passed | Invalid provenance, unsupported passes, concealed assistance, boundary contradictions, legacy opt-out, blocked plans, CLI behavior and literal XLSX round-trip; not report truth |
| Skill frontmatter validator | Passed | Name/description structure; not host activation |
| Local Markdown links and JSON parsing | Passed | Referenced files exist and JSON is parseable; not semantic completeness |
| Git whitespace check | Passed | No whitespace errors in the patch |
| Six supplied-record scenarios | All six met the targeted author-reviewed decisions below | One fresh non-fork AI session, not a blind human evaluation or general accuracy benchmark |
| Direct local UI trial | Blocked before product UI | Browser startup/connection failed; no product action, screenshot, save/reopen, L1 learning or L2 proficiency was verified |

The final structural/data checks are recorded in [validation.json](runs/2026-11-10/validation.json). Runtime file hashes identify the final candidate; they do not retrospectively prove which bytes an earlier agent loaded. The forward tasks ran during development. Assistance-event shape and blocked-plan validation were tightened afterward and covered by targeted regression tests; the entire behavioral exercise was not repeated after that metadata tightening.

### Supplied-record decisions

See the [task transcription](record-trial-input.md) and [raw response](runs/2026-11-10/record-trial.md). The executing session received the task and skill location, with no inherited parent conversation or evaluator answers. Exact backend model identity and hidden host context were not independently verified. The author reviewed the response against these expected decisions:

| Case | Observed decision | Assessment |
|---|---|---|
| A | Preserves reported functional success; labels prior-route knowledge informed and cold discovery unverified | Met |
| B | Keeps first unsuccessful attempt and separate hinted success; no unassisted-success inflation | Met |
| C | Leaves unexecuted L2 not-run and does not invent familiarity or product failure | Met |
| D | Accepts failed prior use as L1 learning; does not invent RUN-2 outcome or rewrite an attempted unknown result as never attempted | Met |
| E | Separates unsupported simultaneous input from observed loss/restart; no victory or balance claim | Met |
| F | Honors capture OFF, guided route and strict legacy JSON; preserves experience metadata in a companion | Met |

These are targeted synthetic decisions from a single session. They do not measure defect precision/recall, human realism, comparative skill accuracy or real device performance. The historical 104/104 numbers in the README remain historical and were not rerun or added to this result.

### Direct UI trial

An independent execution session was asked to use the local [memo fixture](fixtures/notes.html) with `profile=compare`, screenshots ON, a creation/save/reopen goal, a return/edit goal and a repeated multi-memo workflow. Disposable local data changes were authorized. The agent was instructed not to read fixture source, evaluator rubrics or other reports and not to spawn further agents.

The installed Chromium could not start: `socket() failed: Operation not permitted (1)`. A separate cloud browser could not reach the specified localhost URL (`ERR_CONNECTION_REFUSED`). A parent-side launch reproduced the socket restriction. No permission escalation or alternate publication was performed. These are environment observations, not fixture defects or evidence that the target passed.

The [live report](runs/2026-11-10/live/report.ko.md) preserves L0 blocked and L1/L2 not-run, with [setup evidence](runs/2026-11-10/live/setup.json). All three run JSON records pass the final consistency checker. This verifies useful blocker reporting, not successful direct QA or the learning progression.

## Remaining release validation

Run the live acceptance protocol in [experience-evaluation.md](../references/experience-evaluation.md) on a host with working UI tools. For the disposable fixture, a normal local command is:

```sh
python -m http.server 8765 --bind 127.0.0.1 --directory evals/fixtures
```

Open `http://127.0.0.1:8765/notes.html` from a browser in the same environment. Preserve real L0 actions, learning-only L1 continuation and an evidence-supported or explicitly seeded L2. Verify independent cold isolation separately. Do not mark the feature live-validated until those artifacts exist. Mobile, desktop games, real-time simultaneous input, audio and representative human behavior remain untested.
