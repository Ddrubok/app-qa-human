# Test cases and defect normalization

## Generate executable cases

Extract versioned requirement IDs and explicit acceptance criteria before generating cases. For design-only input, identify visible behavior and list missing interactions as assumptions/questions. Never convert a guessed business rule into a requirement. Use seven-area coverage from SKILL.md, boundary values, equivalence classes, and state transitions where they reduce missed risk. Add pairwise combinations only for interacting dimensions, not an exhaustive cross product.

Use one purpose per case, numbered executable actions, clear setup/reset, and observable expected results. Link each case to requirement/source and relevant risk. For underspecified expectations, mark proposed pending confirmation; do not invent deadlines, limits, refund rules, or timings. For large input, report covered and deferred requirements; do not silently truncate.

For execution QA, use [Task completion](task-completion.md). Put the user's completed outcome in expected_results, not just "button responds"; record the last completed action and remaining check in actual_result when coverage is partial. Generated cases still stay not-run.

Canonical case fields:

`id, requirement_refs[], area, title, priority, preconditions[], test_data, steps[], expected_results[], expectation_basis, assumption, status, actual_result, evidence_refs[], environment, cleanup`

- status: `not-run | passed | failed | blocked | not-applicable`.
- actual_result and evidence_refs remain null/empty for generated cases.
- passed/failed require execution evidence. Code-only review does not pass a runtime TC.
- priority means execution order; it is not defect severity.
- use null/unknown explicitly; preserve source facts and user wording where relevant.

For Markdown use `ID | Requirement | Area | Preconditions | Steps | Expected | Priority | Status`, with long evidence beneath the table. For JSON return `schema_version, scope, sources, assumptions, cases, coverage, limitations` with these case records. Validate JSON parsing before delivery.

For live QA reports, record the effective `screenshots` option (`on` or `off`) in scope and any mid-task changes. Record screenshot coverage separately as `complete | partial | unavailable | disabled | not-run`; use `not-applicable` for document-only work. Complete requires saved, inspected images; a future capture plan is not-run. Under ON, link/embed the verified captures beside their case/finding and keep image paths in evidence_refs. Under OFF, record text/log/file evidence and any limits of visual verification instead; absence of screenshots does not itself fail a functional test. List each missing required capture and its reason instead of implying complete image coverage.

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
