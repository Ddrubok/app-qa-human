# Evidence validation and compact QA — 2026-11-10

This update fixes malformed evidence acceptance, aligns the default prompt with one scoped QA pass, and makes detailed experience bookkeeping conditional. It does not establish better live bug detection or faster product testing.

## Revisions and reproduction

- Original: `f192c22bbfb4cd3b48716aed8e886d09efe733fb` (local tree-equivalent snapshot `4dc9129`).
- Previous experience update/main: `dd8c76a1091842864ff26757508336fb054eab88` (local tree-equivalent snapshot `6f67e45`).
- Candidate: runtime/document file hashes in [forward-manifest.json](runs/2026-11-10-hardening/forward-manifest.json). Validation artifacts themselves are excluded from that snapshot.

Run from the repository root:

```sh
python -m unittest discover -s tests -v
python scripts/validate_experience.py templates/experience-run.json --require-experience
python evals/measure_reading.py --original f192c22 --previous dd8c76a --output reading-new.json
```

The measurement script requires those refs in the local clone and refuses to overwrite an existing output. This environment used the tree-equivalent local refs above. Metrics use the working tree candidate; rerunning after later changes measures those changes instead.

## Evidence checker

The same `observed()` fixture was probed before and after the fix. It has a passed case, actual result and registered `OBS` source. [Before](runs/2026-11-10-hardening/evidence-probes-before.json), [after](runs/2026-11-10-hardening/evidence-probes-after.json):

| Case evidence list | Previous | Candidate |
|---|---|---|
| `[]` | Rejected | Rejected |
| `[null]`, `["UNREGISTERED"]`, `[""]`, `[7]`, `[{}]`, `["OBS", null]` | Accepted | Rejected |
| `["OBS"]` | Accepted | Accepted |

Every supplied case/finding reference now must be nonempty text resolving to a registered source ID. Passed/failed cases and reproduced/code-confirmed findings require evidence; uncertain findings may have an empty list. `id`/`source_id` aliases remain accepted but conflicting aliases fail. The CLI returns 2 for invalid evidence. This does not fetch files/URLs, validate source truth, or certify execution. Legacy reports without `experience` remain explicitly unevaluated unless the extension is required.

All **18 unittest methods passed, 0 skipped**, including the optional XLSX round-trip (`openpyxl` available here). New subcases cover invalid members across all case statuses, findings, aliases and CLI exits. [Raw test output](runs/2026-11-10-hardening/unit-tests.txt). The unexecuted template and three earlier blocked/not-run reports also pass the stricter consistency check; their execution status has not changed ([results](runs/2026-11-10-hardening/existing-records.json)).

## Reading and recording cost

| Scope | Original | Previous | Candidate |
|---|---:|---:|---:|
| SKILL.md | 1,449 | 1,620 | 1,093 |
| Narrow direct QA, familiar tools, ordinary save/reopen | 6,514 | 8,367 | 3,068 |
| SKILL + all reference Markdown + Markdown templates | 12,007 | 16,606 | 16,429 |

Measured with Python `str.split()`; includes Markdown syntax/frontmatter. The main file is 32.5% smaller than the previous revision, and the documented ordinary live path is 63.3% smaller. [Metrics with exact file lists and hashes](runs/2026-11-10-hardening/metrics.json), [measurement script](measure_reading.py).

The compact path reads SKILL.md, baseline.md and screenshots.md. It loads tool adapters, complex completion, mistakes/recovery, structured reports and experience protocols only when their triggers apply. These conditional tasks can require much more reading; the complete experience corpus remains larger than the original. Counts are not actual model tokens, timing, or proof every host will follow routing.

Ordinary Markdown shares build/environment once, then records goal/expected basis, actions/result/status, evidence and remaining check. Defects retain impact, reproduction and retest. A small task needs no experience JSON, campaign IDs, action counters or seven-area matrix. Formal profile attempts remain separately identifiable but may share one Markdown file. Screenshot inspection and evidence, privacy, cleanup and real outcome verification are retained.

The default UI prompt and English/Korean first example now request one scoped check. Experience comparison is a separate explicit example. Full report depth does not automatically start multiple profiles.

## Forward exercises

Two fresh, non-forked agents received the same two report-only tasks and one frozen revision each. They did not receive this review, the rubric or expected conclusions. Both used the inherited model/configuration; the exact backend identifier was unavailable. Each handled task A then B in one context, so those tasks are not independent samples.

| Frozen criteria | Previous | Candidate |
|---|---:|---:|
| A: short save/reopen report from supplied records | 5/5 | 5/5 |
| B: preserve first attempt, external hint, learning and unsupported L2 | 5/5 | 5/5 |

Both attributed synthetic records, retained the save/reopen mismatch without claiming personal execution, preserved unassisted versus helped attempts, and left L2 unsupported. The candidate used a compact table for task A. Agents reported reading 9 versus 6 skill files across the combined task pair. These counts are not the ordinary-live path metric above, a latency benchmark or proof that all hosts load fewer files.

The coordinator graded raw outputs against the frozen rubric; no independent judge or human adjudication was used. Both revisions met all criteria: **no accuracy improvement was demonstrated**. This small exercise found no reporting regression in the tested decisions; it does not establish performance on other tasks/models.

Artifacts: [raw tasks](runs/2026-11-10-hardening/forward-tasks.json), [frozen rubric](runs/2026-11-10-hardening/forward-rubric.json), [previous answer](runs/2026-11-10-hardening/previous-answer.md), [candidate answer](runs/2026-11-10-hardening/candidate-answer.md), [grading](runs/2026-11-10-hardening/forward-results.json), and [revision hashes](runs/2026-11-10-hardening/forward-manifest.json). The records are synthetic, not a real app trial. Runtime/profile documents remained unchanged after these snapshots; only evaluation artifacts were completed afterward.

## Live comparison limit and next execution

A new browser preflight opened `https://demo.playwright.dev/todomvc/`. Both the accessibility output and inspected screenshot displayed **Site Unavailable / Unable to access this site**. No product action ran, and no revision was scored. The cause is unknown; this is not evidence that the product is broken or that bot detection occurred. The screenshot was inspected in the tool result, not saved as a repository artifact. [Preflight record](runs/2026-11-10-hardening/browser-preflight.json).

The same-app comparison remains **not-run due to blocked setup**. Earlier local-browser failures remain in the [previous validation record](2026-11-10-experience.md); no workaround is presented as successful QA. Real L0→L1→L2 progression, live gameplay, accuracy/precision/recall, actual runtime cost and representative human outcomes remain unverified.

Use the [same-app comparison protocol](live-comparison-protocol.md) once an accessible permitted build is available. It freezes revisions/build/data and expectations, separates cold context from diagnosis, counterbalances runs, preserves evidence, and requires an independently established defect inventory before reporting detection recall. It is a maintainer protocol, not another document added to ordinary QA's reading path.
