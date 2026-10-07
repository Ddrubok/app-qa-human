# Test cases and defect normalization

## Generate executable cases

Extract versioned requirement IDs and explicit acceptance criteria before generating cases. For design-only input, identify visible behavior and list missing interactions as assumptions/questions. Never convert a guessed business rule into a requirement. Use seven-area coverage from SKILL.md, boundary values, equivalence classes, and state transitions where they reduce missed risk. Add pairwise combinations only for interacting dimensions, not an exhaustive cross product.

Use one purpose per case, numbered executable actions, clear setup/reset, and observable expected results. Link each case to requirement/source and relevant risk. For underspecified expectations, mark proposed pending confirmation; do not invent deadlines, limits, refund rules, or timings. For large input, report covered and deferred requirements; do not silently truncate.

Canonical case fields:

`id, requirement_refs[], area, title, priority, preconditions[], test_data, steps[], expected_results[], expectation_basis, assumption, status, actual_result, evidence_refs[], environment, cleanup`

- status: `not-run | passed | failed | blocked | not-applicable`.
- actual_result and evidence_refs remain null/empty for generated cases.
- passed/failed require execution evidence. Code-only review does not pass a runtime TC.
- priority means execution order; it is not defect severity.
- use null/unknown explicitly; preserve source facts and user wording where relevant.

For Markdown use `ID | Requirement | Area | Preconditions | Steps | Expected | Priority | Status`, with long evidence beneath the table. For JSON return `schema_version, scope, sources, assumptions, cases, coverage, limitations` with these case records. Validate JSON parsing before delivery.

For Excel, use available workbook tools to create a genuine .xlsx, with Cases, Coverage, and Sources sheets. Format cells as text for untrusted text starting with =, +, -, or @; avoid formula/link execution. Reopen the file and check sheet names, row count, Unicode, IDs and multiline steps. If no workbook tool is available, say so and deliver Markdown/JSON or explicitly labeled UTF-8 CSV; never rename a CSV to .xlsx. Escape CSV quotes/newlines and neutralize spreadsheet formulas while retaining the original in safe JSON when needed.

## Normalize rough bug notes

Preserve reporter claims as reported, not reproduced. Do not supply fictional environment, frequency, timestamps, repro actions, expected rules, or root cause. A missing field is unknown and may need a focused follow-up; provide the usable draft immediately.

Canonical finding fields:

`id, category, title, severity, priority, evidence_level, environment, affected_journey, preconditions, steps_to_reproduce, expected, expectation_basis, actual, impact, frequency, evidence_refs, suspected_cause, minimum_fix, retest, related_ids, missing_information`

- category: `functional | usability | misleading-presentation | requirement-gap | policy-risk`.
- evidence_level: `reproduced | code-confirmed | needs-verification`.
- baseline P1/P2/P3 priorities apply when no project convention exists. Explain impact separately from urgency.
- inferred cause/frequency stays labeled or unknown. A polished report is not stronger evidence.
- merging duplicates preserves original report references and distinguishes genuinely separate causes.

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
