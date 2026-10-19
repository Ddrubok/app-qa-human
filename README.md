# app-qa-Human

[English](README.md) | [한국어](README.ko.md)

**An AI agent skill for reviewing an app through a person's goals, mistakes, interruptions, and recovery.**

This is a separate alternative to [app-qa](https://github.com/Ddrubok/app-qa). It keeps the original evidence standards and adds exploratory journeys, requirement-linked test cases, bug report normalization, and store review risk checks. Both skills can be installed so you can compare them explicitly.

A skill is instructions for an agent, not a standalone QA service. It does not simulate real research participants or automatically connect to your app, company knowledge base, or issue tracker.

## What it does

| Capability | Result |
|---|---|
| Human-centered exploration | Checks whether a user can find an action, predict its result, understand feedback, and recover |
| Task completion | Opens downloaded files, reopens saved data, and checks the actual input method |
| Screenshot evidence | Captures tested states by default; supports `screenshots=on` / `screenshots=off` |
| PRD/design to test cases | Requirement-linked cases with setup, steps, expectations, and execution status |
| Informal bug notes to reports | Structured reports with missing facts explicitly marked unknown |
| Store review risk | Applicable current official policies connected to implementation evidence |
| Company knowledge retrieval | Source/version-aware retrieval of standards and past defects |
| Comparison with app-qa | Same-condition evaluation guidance and focused synthetic cases |

The default seven areas cover functionality, usability/accessibility, interruptions, exceptions/recovery, data/permissions/privacy, compatibility/performance, and distribution/operations. Supplied company categories take precedence.

## Codex, Claude Code, and Gemini CLI

The core uses standard `SKILL.md` frontmatter (name/description), Markdown instructions, and relative references. `agents/openai.yaml` is optional Codex UI metadata, not a dependency of the workflow.

| Host | Personal installation | Invocation |
|---|---|---|
| Codex | Existing supported skill directory; see installation below | `$app-qa-human` |
| Claude Code | `~/.claude/skills/app-qa-human` | `/app-qa-human` |
| Gemini CLI | `~/.gemini/skills/app-qa-human` | Ask Gemini to activate `app-qa-human`; inspect with `/skills list` |

Claude Code installation:

```sh
git clone https://github.com/Ddrubok/app-qa-human.git ~/.claude/skills/app-qa-human
```

Gemini CLI installation (may ask for installation consent):

```sh
gemini skills install https://github.com/Ddrubok/app-qa-human --scope user
gemini skills list
```

For a single project use `.claude/skills/app-qa-human` or Gemini's `--scope workspace`. The `$app-qa-human` examples below are Codex examples; use Claude's slash command or Gemini's natural-language activation instead. Plain chat websites, Claude uploads, and Antigravity/agy discovery are separate host integrations and are not certified by these CLI checks.

See [compatibility evidence and limits](COMPATIBILITY.md).

## Install

Clone into one skill location recognized by your agent:

```sh
git clone https://github.com/Ddrubok/app-qa-human.git ~/.agents/skills/app-qa-human
```

For project-scoped use, use `<project>/.agents/skills/app-qa-human`. If your installation already discovers skills from `~/.codex/skills`, use that location instead. Avoid duplicate installations. Check the skill selector after installation and restart the session if discovery has not refreshed. Display name: `app-qa-Human`; invocation: `$app-qa-human`.

## Use

```text
$app-qa-human Review signup and the first successful booking as a new user.
Include denied permissions, interrupted requests, and recovery.
Separate observed defects, code-confirmed findings, and open questions.
```

```text
$app-qa-human Generate test cases from this PRD in Markdown.
Link every case to its requirement and mark unexecuted cases not-run.
```

```text
$app-qa-human Turn these rough bug notes into draft Jira reports.
Preserve unknown details and do not publish them.
```

### Screenshots: ON by default

Live app/web QA captures the relevant starting state and result of each tested screen/case, including successful checks and observed defects. When an image viewer is available, saved images are inspected and linked beside the matching report items. Without a viewer, label the artifact `Image file created (unverified visually by agent)` and continue supported DOM/text checks. Saving an image is not visual verification.

```text
$app-qa-human screenshots=on Review this app and include screenshot evidence.
$app-qa-human screenshots=off Review this app without taking screenshots.
```

These are request options, not shell commands. With no option, live QA uses ON. OFF also excludes tools that automatically take screenshots; use available text/DOM tools and report visual limits. The latest choice stays active while continuing the same QA task. A separate task defaults to ON unless a broader preference was requested. Changing to OFF preserves earlier evidence files.

Missing capture tools or unsafe sensitive content are recorded as evidence gaps. Planned captures are not-run until executed. Rewriting notes or comparing existing reports does not start live QA or generate new screenshots; supplied/manual images retain their source labels.

For JSON or Excel, request the format explicitly. Actual XLSX creation requires available workbook tooling; the skill must not rename CSV to XLSX. Store review requires current official sources and the target store/region/build.

## Report depth and exports

Use `mode=quick` (default) for a concise report or `mode=full` for detailed records and the seven-area coverage matrix. These control report depth, not how much verification is required. Zero defects is a valid result; serious findings must not be omitted to meet a quota. Markdown, JSON, and XLSX are separate format choices.

```text
$app-qa-human mode=quick Review signup and recovery.
$app-qa-human mode=full screenshots=off Compare this implementation with the PRD.
```

Cases and findings separate Core and Extended fields. Severity describes impact; finding priority describes fix urgency, and case priority describes execution order. Human-error checks cover repeated submission, unfinished forms, interruptions, larger text, and keyboard obstruction. Tool guidance covers Playwright, ADB, Maestro, Appium, and iOS Simulator, subject to the host's capabilities.

The optional [XLSX helper](scripts/export_xlsx.py) requires Python and an available `openpyxl` installation; it does not install dependencies. It stores strings as literal text, checks saved values and workbook structure, and rejects oversized cells or an existing output path instead of silently losing data. See the [input contract and usage](references/cases-and-reports.md). CSV has separate safety requirements; this helper exports XLSX only.

## Update validation — 2026-10-19

| Version | First run | Second run | Total rubric passes |
|---|---:|---:|---:|
| Previous local version | 52/52 | 52/52 | 104/104 |
| Improved comparison candidate | 52/52 | 52/52 | 104/104 |

This was a synthetic decision comparison: 40 existing scenarios and 12 targeted additions, repeated twice. Each version/run used a fresh context with the same inherited model and reasoning configuration; the exact backend model identifier was unavailable. The second round reversed case order. Evaluators did not receive expected answers. Independent AI judges graded anonymized responses against frozen criteria; no human adjudication was performed. Cases shared a context within each run and partly overlap.

Both versions met all criteria in this sample. **An accuracy improvement was not demonstrated.** These results are not live-app accuracy, precision/recall, or proof of reliable behavior on other models. No fair speed comparison was performed.

After the comparison, the final version restored one CSV safeguard paragraph in `references/cases-and-reports.md`. Two additional synthetic XLSX/CSV decisions on that final text met coordinator-reviewed criteria; the full comparison was not rerun on the exact final text. The unchanged XLSX helper passed nine actual execution tests covering literal strings, Unicode and length limits, invalid input, existing-file protection, empty reports, and CLI round-trips. YAML, local references, and Git whitespace checks also passed. Actual browser/device QA, Excel UI behavior, and host activation of this update remain unverified. See [evaluation guidance](references/evaluation.md) and the dated [host compatibility record](COMPATIBILITY.md).

## Evidence and limits

- Runtime reproduction, code confirmation, and issues needing verification remain distinct.
- A screenshot cannot prove an interaction or accessibility behavior; generated test cases are not test results.
- Store risks are conditional findings, not approval guarantees or rejection probabilities. HIG/Material design guidance is not automatically a rejection policy.
- QA alone does not authorize app changes, deployments, live purchases, or messages. External ticket/chat updates require task authorization.
- RAG infrastructure, vector databases, bots, and integrations are not installed by this repository. Small document sets can use ordinary file search.
- Structural validation, reference checks, and selected synthetic decision exercises have been performed. These are not a live-app benchmark, a human-versus-AI accuracy score, or execution of every case in the evaluation catalog.

## Files

- [SKILL.md](SKILL.md): workflow and routing.
- [agents/openai.yaml](agents/openai.yaml): discovery metadata.
- [Baseline](references/baseline.md): preserved app-qa standards, included for a self-contained installation.
- [Cases and reports](references/cases-and-reports.md): output contracts and synthetic examples.
- [Task completion](references/task-completion.md): actual interactions, persisted results, downloads, and usable evidence.
- [Store review](references/store-review.md): policy applicability and currency.
- [Knowledge retrieval](references/knowledge.md): provenance, conflicts, and feedback records.
- [Evaluation](references/evaluation.md) and [baseline cases](references/baseline-evaluation-cases.md): maintainer checks.

- [Screenshot evidence](references/screenshots.md): capture and visual inspection states.
- [Human error patterns](references/human-errors.md): realistic variations and recovery checks.
- [Tool execution](references/tool-execution.md): platform actions, waits, evidence, and fallback.
- [XLSX helper](scripts/export_xlsx.py): optional safe workbook export.
