# Test cases and defect normalization

## Generate executable cases

Extract versioned requirement IDs and explicit acceptance criteria before generating cases. For design-only input, identify visible behavior and list missing interactions as assumptions/questions. Never convert a guessed business rule into a requirement. Use seven-area coverage from SKILL.md, boundary values, equivalence classes, and state transitions where they reduce missed risk. Add pairwise combinations only for interacting dimensions, not an exhaustive cross product.

Use one purpose per case, numbered executable actions, clear setup/reset, and observable expected results. Link each case to requirement/source and relevant risk. For underspecified expectations, mark proposed pending confirmation; do not invent deadlines, limits, refund rules, or timings. For large input, report covered and deferred requirements; do not silently truncate.

For execution QA, use [Task completion](task-completion.md). Put the user's completed outcome in expected_results, not just "button responds"; record the last completed action and remaining check in actual_result when coverage is partial. Generated cases still stay not-run.

## Core and extended records

Use `schema_version: "2.0"` for this core/extended representation. Preserve existing field names; do not silently migrate a consumer expecting the old complete schema. If an external contract requires every field, provide it, using null/unknown rather than fabricated values.

At run level record `scope, environment, sources, assumptions, coverage, limitations`. State mode, evidence origin and effective screenshot option where applicable. Case/finding environment can refer to this shared environment; override only differing conditions. Source IDs must resolve to actual supplied or inspected sources.

**Case core:** `id, title, preconditions, steps, expected_results, expectation_basis, priority, status, actual_result, evidence_refs` plus a resolvable environment reference. Core is enough to reproduce the case and judge its outcome.

**Case extended:** `requirement_refs, area, test_data, assumption, cleanup` and additional project contract fields. Requirement mapping is required when the task asks for PRD coverage. Cleanup is required for state-changing execution; optional serialization never makes necessary cleanup optional.

- `status`: `not-run | passed | failed | blocked | not-applicable`. For a partially exercised case, state the last completed step and remaining verification; do not pass it. Use blocked when a concrete dependency prevented completion, not-run for remaining unattempted checks; split cases if needed.
- Generated cases are not-run with actual_result=null and evidence_refs=[]. Keep the requirements in expectation_basis/sources, not as fabricated execution evidence.
- Passed/failed requires execution evidence. Source review alone cannot pass a runtime case. Supplied execution records remain attributed to their original executor.
- Case `priority` means execution order (baseline definitions).

Markdown may show a compact table with long evidence beneath it. JSON uses `schema_version, scope, environment, sources, assumptions, cases, findings, coverage, limitations`; omit irrelevant collections only if the requested consumer allows it. Validate JSON parsing and preserve stable IDs. In full mode, cover all seven areas with covered/partial/not-tested/not-applicable and reasons. A coverage row is not a passed test.

Screenshot lifecycle and coverage follow [Screenshot evidence](screenshots.md). Functional test status and visual-review status are independent.

## XLSX export

For requested Excel output, use [export_xlsx.py](../scripts/export_xlsx.py) with an existing Python/openpyxl environment: `python scripts/export_xlsx.py report.json report.xlsx`. The helper writes Cases, Coverage and Sources; Findings is included when present. Sources include run context and assumptions/limitations. It is an optional export tool, not an installation prerequisite for QA. If unavailable, use an existing workbook tool with equivalent checks or deliver an explicitly identified Markdown/JSON alternative. Never rename CSV as XLSX or install a stack merely for routine review.

Untrusted text must be stored as literal string values, not just given a text number format. Check the saved workbook's actual cell types, absence of formulas/external links, record counts, IDs, Unicode, multiline steps, and exact round-trip values. Reject or explicitly split overlong cells while preserving the full source JSON; never silently truncate. Do not strip meaningful whitespace or alter numeric data to hide loss. Parsing proves file structure/content only; Excel UI compatibility remains untested unless exercised.

If CSV is explicitly requested, use properly escaped UTF-8 CSV and neutralize spreadsheet formula interpretation in untrusted fields, retaining exact original values in safe JSON when needed. CSV has no cell-type metadata; an XLSX text-format setting is not a CSV defense. Describe any changed export representation and never label CSV as XLSX. This preserves the legacy CSV safeguard; the bundled helper itself exports XLSX only.

## Normalize rough bug notes

Preserve reporter claims as reported, not reproduced. Do not supply fictional environment, frequency, timestamps, repro actions, expected rules, or root cause. A missing field is unknown and may need a focused follow-up; provide the usable draft immediately.

**Finding core:** `id, category, title, severity, priority, evidence_level, affected_journey, preconditions, steps_to_reproduce, expected, expectation_basis, actual, impact, evidence_refs` plus a resolvable environment reference. Unknown fields stay null/unknown; a concise presentation need not display every null field.

**Finding extended:** `frequency, suspected_cause, minimum_fix, retest, related_ids, missing_information` and additional project fields. Include a meaningful retest when proposing a fix; no invented root cause, frequency or environment to fill the form.

- category: `functional | usability | misleading-presentation | requirement-gap | policy-risk`.
- evidence_level: `reproduced | code-confirmed | needs-verification`. Record executor/provenance in the evidence record; a supplied report is not your own reproduction.
- Severity describes impact; finding priority describes fix urgency (baseline definitions). Keep both separate from test execution order.
- Inferred cause/frequency stays labeled or unknown. A polished report is not stronger evidence. A reproducible failure may be confirmed while its cause remains unknown.
- Merging duplicates preserves original references; do not assume a shared cause solely from similar symptoms.

## Evidence origin and comparisons

Identify who performed a check separately from who wrote the report. An AI rewrite of a person's notes is human-reported evidence until an independent run is documented. Reformatting one source into several findings does not create additional independent discoveries.

In sources/evidence records, retain the original path or ID, reporter/executor when known, observation date/build when known, and evidence kind: current execution, supplied report, or reference illustration. Do not infer a human or AI executor from an unlabeled log. When analyzing supplied traces, say "the supplied record shows" rather than claiming your own direct observation. For each finding, preserve the original claim, later reporter corrections, and any separate retest result. Label screenshots from manuals as reference images; never use them as proof that the reported failure occurred.

Match findings by action, symptom, and conditions, not just by screen name. Classify a comparison as same symptom, related but different, conflicting under matched conditions, outside the tested scope, or insufficient evidence. UI-only inspection cannot refute a save/download failure. A passed check on another account/build is a separate result unless the conditions can be aligned. Do not infer a shared root cause from similar symptoms alone.

Separate human observations, AI execution findings, and editorial additions in counts. Explain splits, merges, and superseded notes. A missing entry is not proof the behavior was tested and passed; an untested behavior is not a confirmed missed defect. Compare accuracy only with matched scope and independently confirmed outcomes, and report unknown denominators as unknown.

## Few-shot examples (synthetic; not actual results)

### Requirement to TC

Input: R-12: 'A saved draft remains after reload. On save failure, retain entered text and show a retry action.'

Output example:

| ID | Requirement | Area | Preconditions | Steps | Expected | Priority | Status |
|---|---|---|---|---|---|---|---|
| TC-012-A | R-12 | 5 Data | Isolated account; clean draft | Enter synthetic text; save; reload | Saved text remains | P1 | not-run |
| TC-012-B | R-12 | 4 Recovery | Isolated save endpoint configured to fail | Enter text; save; observe; restore endpoint; retry | Failure preserves text and offers retry; successful retry saves it | P1 | not-run |

No assertion about autosave, exact toast wording, or response time: R-12 supplies none. Mocked failure cannot establish real outage behavior.

### Vague note to draft defect

Input: '지하철에서 결제 눌렀는데 돌아와 보니 또 결제하라고 떠요.'

Output: title='결제 시도 후 복귀 시 결제 재요청 표시(보고됨)'; evidence_level='needs-verification'; actual='Reporter saw a payment request after returning'; expected='Payment state should reconcile with the provider; exact product contract unconfirmed'; suspected_cause=null; frequency=null. Missing: build/device, interruption sequence, receipt/provider state, whether charged, screen capture. Use sandbox to investigate; do not retry a real charge. Do not label it duplicate billing without evidence.

### Screenshot-only review

Input: one screenshot where the keyboard covers the visible Continue button.

Output: observed='Continue is occluded in the supplied image'; evidence_level='needs-verification' for inability to proceed; retest='Try supported scrolling, keyboard dismissal and keyboard action on the actual device'. Do not assert that form submission is impossible from the picture alone.
