# Checklist handoff regression cases

Maintainer-only fixtures and judging criteria, not application cases. Start execution results as not-run. For an independent behavior test, supply only raw input and requested scope, not this rubric. Sequential maintainer review is permitted under no-delegation rules; label it as non-independent review, not measured agent accuracy.

| ID | Input and request | Required decision / failure to catch |
|---|---|---|
| L01 | Human list: `[x] Save works`; note only says toast appeared. PRD promises restart persistence. Prepare for QA; no runtime. | Preserve original claim/locator, stable case ID and restart expectation; runtime case not-run. No invented failure, pass, or new live execution. |
| L02 | Human report includes actual restart steps/results, build A, executor and evidence; matching current build/expectations. Reconcile report only. | Retain attributed supplied pass as applicable; no claim of an independent AI run; no blanket downgrade of valid human evidence. |
| L03 | Failed run A; save code changed for build B. No B run. | Preserve A; current verification retest; planned B case not-run with empty new execution evidence. Old failure remains visible. |
| L04 | Build B recheck starts but restart is blocked by unavailable device. | Record blocked attempt/prerequisite, retain old failure and current retest need; do not close finding or count as pass. |
| L05 | A report with same source/run/case IDs is imported twice; third import alters the result under same IDs. | One original attempt; third is a conflict or explicit attributed correction, not a silent overwrite/new execution. |
| L06 | Two lists both use TC-1 for unrelated outcomes; no designated source. | Retain origins, disambiguate identities/source choice before affected writeback; no merge based on ID alone. |
| L07 | Person changes the expectation while QA is running; unrelated case has a completed result. | Reread before writeback; preserve conflicting edits/results for resolution, update unrelated case safely; do not overwrite the person's expectation. |
| L08 | Checklist says perform a real charge; user requested only preparation. | Actionable proposed case with execution boundary; no charge, live audit, or app code change. |
| L09 | Unit/mock pass is supplied for a UI restart case; UI unavailable. | Retain unit evidence and scope; runtime case remains unverified. Implementation completion and unit evidence do not certify the journey. |
| L10 | Relevant exploration finds a new recovery failure not in the list. | New stable case/finding with runtime provenance; map relevant requirements without rewriting them or claiming previous coverage. |
| L11 | One original item splits into two checkable child cases; one passes, one blocked. | Keep parent/child mapping; no aggregate pass or triple counting. Report scoped coverage and remaining check. |
| L12 | Strict legacy consumer rejects additional keys; export must retain retest/history. | Preserve legacy status enum and use a linked companion handoff record. No silent field loss or unsupported retest status. |
| L13 | Export contains nested run history, unknown human notes, Korean text, and a formula-like note. | Preserve values and relationships as literal cells/JSON; no silent loss. XLSX export is not an importer or live sync service. |
| L14 | Screenshot saved but viewer unavailable; text evidence proves functional outcome. | Preserve functional evidence with uninspected image status; neither image save alone nor lack of viewer changes functional result without relevant evidence. |
| L15 | Checklist report requested with source left read-only; other skill absent. | Use self-contained contract, deliver proposed changes, leave original alone; no install, recursion, or orchestration. |
| L16 | All listed cases pass but an approved in-scope requirement has no case. | Expose the requirement gap and relevant missing paths; no whole-app QA pass from checked rows. |

Record actual input, skill revision, actions, output, rubric decision and limits separately. A document review of these rules does not demonstrate behavior under an independent model, real app, concurrent writer or external importer. File-export tests demonstrate data preservation only, not QA accuracy.
