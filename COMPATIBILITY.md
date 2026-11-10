# Compatibility evidence

Experience-profile extension, 2026-11-10: the L0/L1/L2/Lapsed workflow is host-neutral guidance. A host must provide suitable interaction and observation tools; independently cold sessions also need inspectable knowledge/context isolation. No bundled isolated-agent runner or native desktop driver was added. See [development validation](evals/2026-11-10-experience.md) for tested behavior; the historical host checks below do not certify the new workflow.

Checked on 2026-10-07.

| Host | Evidence | Limit |
|---|---|---|
| Codex | Installed skills discovered in the maintainer session; structural validator passed | No guarantee for every host version |
| Claude Code 2.1.107 | Local CLI version/help checked; frontmatter, relative references, installation and slash invocation reviewed against official documentation | No authenticated skill activation or task run performed |
| Gemini CLI 0.59.0 | Both skills copied to a test workspace's .gemini/skills and listed as Enabled by gemini skills list | Discovery only; no model inference, activation or task-quality test |

Gemini's existing Unity MCP endpoint was offline during discovery. This was unrelated to these instruction-only skills and did not prevent their discovery. Neither skill requires Unity MCP, a particular model/provider, paid API credentials, or an orchestration runner. Available browser/device/image/workbook tools determine actual coverage.

## Host-neutral execution

Read references relative to the installed SKILL.md directory, not the project working directory. Use the host's own file, image, browser and shell tools. If a capability is unavailable, report the missing verification rather than claiming execution. Optional Codex UI metadata does not change the core instructions. A discovered skill is not a successfully executed review.

## Official sources

- [Claude Code skills](https://code.claude.com/docs/en/skills): SKILL.md, personal/project directories and slash invocation.
- [Gemini CLI skill management](https://geminicli.com/docs/cli/using-agent-skills/): installation, discovery and activation management.

These checks concern Claude Code and Gemini CLI. Gemini web/Gems, Claude web uploads and Antigravity/agy have separate installation and tool capabilities; support is not implied by model family. No hosted services or account settings were changed.
