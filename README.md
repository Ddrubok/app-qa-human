# app-qa-Human

[English](README.md) | [한국어](README.ko.md)

**An AI agent skill for reviewing an app through a person's goals, mistakes, interruptions, and recovery.**

This is a separate alternative to [app-qa](https://github.com/Ddrubok/app-qa). It keeps the original evidence standards and adds exploratory journeys, requirement-linked test cases, bug report normalization, and store review risk checks. Both skills can be installed so you can compare them explicitly.

A skill is instructions for an agent, not a standalone QA service. It does not simulate real research participants or automatically connect to your app, company knowledge base, or issue tracker.

## What it does

| Capability | Result |
|---|---|
| Human-centered exploration | Checks whether a user can find an action, predict its result, understand feedback, and recover |
| PRD/design to test cases | Requirement-linked cases with setup, steps, expectations, and execution status |
| Informal bug notes to reports | Structured reports with missing facts explicitly marked unknown |
| Store review risk | Applicable current official policies connected to implementation evidence |
| Company knowledge retrieval | Source/version-aware retrieval of standards and past defects |
| Comparison with app-qa | Same-condition evaluation guidance and 16 additional synthetic cases |

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

For a single project use `.claude/skills/app-qa-human` or Gemini's `--scope workspace`. The `# app-qa-Human

[English](README.md) | [한국어](README.ko.md)

**An AI agent skill for reviewing an app through a person's goals, mistakes, interruptions, and recovery.**

This is a separate alternative to [app-qa](https://github.com/Ddrubok/app-qa). It keeps the original evidence standards and adds exploratory journeys, requirement-linked test cases, bug report normalization, and store review risk checks. Both skills can be installed so you can compare them explicitly.

A skill is instructions for an agent, not a standalone QA service. It does not simulate real research participants or automatically connect to your app, company knowledge base, or issue tracker.

## What it does

| Capability | Result |
|---|---|
| Human-centered exploration | Checks whether a user can find an action, predict its result, understand feedback, and recover |
| PRD/design to test cases | Requirement-linked cases with setup, steps, expectations, and execution status |
| Informal bug notes to reports | Structured reports with missing facts explicitly marked unknown |
| Store review risk | Applicable current official policies connected to implementation evidence |
| Company knowledge retrieval | Source/version-aware retrieval of standards and past defects |
| Comparison with app-qa | Same-condition evaluation guidance and 16 additional synthetic cases |

The default seven areas cover functionality, usability/accessibility, interruptions, exceptions/recovery, data/permissions/privacy, compatibility/performance, and distribution/operations. Supplied company categories take precedence.

 examples below are Codex examples; use Claude's slash command or Gemini's natural-language activation instead. Plain chat websites, Claude uploads, and Antigravity/agy discovery are separate host integrations and are not certified by these CLI checks.

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

For JSON or Excel, request the format explicitly. Actual XLSX creation requires available workbook tooling; the skill must not rename CSV to XLSX. Store review requires current official sources and the target store/region/build.

## Evidence and limits

- Runtime reproduction, code confirmation, and issues needing verification remain distinct.
- A screenshot cannot prove an interaction or accessibility behavior; generated test cases are not test results.
- Store risks are conditional findings, not approval guarantees or rejection probabilities. HIG/Material design guidance is not automatically a rejection policy.
- QA alone does not authorize app changes, deployments, live purchases, or messages. External ticket/chat updates require task authorization.
- RAG infrastructure, vector databases, bots, and integrations are not installed by this repository. Small document sets can use ordinary file search.
- No human QA comparison or live-app behavioral benchmark has been completed for this skill. Structural validation and reference checks passed during local creation; synthetic case outcomes remain not-run.

## Files

- [SKILL.md](SKILL.md): workflow and routing.
- [agents/openai.yaml](agents/openai.yaml): discovery metadata.
- [Baseline](references/baseline.md): preserved app-qa standards, included for a self-contained installation.
- [Cases and reports](references/cases-and-reports.md): output contracts and synthetic examples.
- [Store review](references/store-review.md): policy applicability and currency.
- [Knowledge retrieval](references/knowledge.md): provenance, conflicts, and feedback records.
- [Evaluation](references/evaluation.md) and [baseline cases](references/baseline-evaluation-cases.md): maintainer checks.
