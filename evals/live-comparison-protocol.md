# Same-app revision comparison

Maintainer protocol; not required reading for ordinary QA. A blocked setup is not a benchmark result. Do not replace product observations with plausible transcripts.

## Freeze before execution

Record the exact skill commit (or file-hash manifest), model/configuration when available, tool versions, app build and test data snapshot. Use the same permitted environment, task goals, evidence options and completion conditions for each revision. Keep private credentials out of artifacts. Preflight access before starting scored runs; report setup failures separately.

Choose representative ordinary tasks (create/save/reopen, edit/cancel, error/recovery) and, separately, an experience sequence (L0 first attempt, L1 learned retry, L2 only with proficiency evidence). For a game add actual control input, one meaningful loop, result and retry; a menu walkthrough cannot substitute. Report missing device/game coverage separately.

## Run without answer leakage

Use fresh verified agent contexts for revision comparisons. Give participants only the selected skill, neutral goals and permitted product state; keep expected failures and earlier reports with the evaluator. For an L0→L1 sequence transfer user-visible learning and declared state, not technical diagnosis. If the host cannot isolate contexts, label the run informed/unverified and exclude cold-discovery claims.

Reset only disposable test data between independent runs, using a supported reset and confirming the resulting state. Reuse retained state only where the task calls for it. Counterbalance revision order across repetitions and record shared state or changing builds as confounders. Preserve raw action logs, inspected captures (when ON), actual outcomes, assistance and cleanup. Do not require counters in normal user reports merely to serve this benchmark.

## Evaluate separately

| Measure | Evidence required |
|---|---|
| Task completion | Expected end state observed beyond a toast; partial/blocked/not-run separate |
| Confirmed unique defects | Reproduction and expectation basis; deduplicate symptoms across runs |
| Unsupported findings | Independently adjudicated claims contradicted by evidence, not just unreproduced claims |
| Detection recall | Independently established known-defect inventory for that exact build; unavailable otherwise |
| Detection precision | Adjudicated true and false findings; no numeric rate when denominator is zero or unknown |
| Procedure cost | Actual read files/report size/action count; word counts are not token or time measurements |
| Timing | Measured task time, model/tool overhead and product waits separately; no human-speed inference |
| Experience claims | Provenance, retained/reset state, help and supported profile progression |

Freeze the rubric and defect inventory before opening participant reports. A reviewer should grade anonymized outputs where practical; disclose AI-only grading and lack of human adjudication. Keep raw artifacts and the rubric so scores can be challenged. Repeated tasks in one context are correlated, not independent participants.

Report each revision's outcomes and limitations even if both find zero bugs. One app or game cannot establish general QA accuracy. Publish a stronger claim only for the measured scope; retain `blocked`/`not-run` when execution fails. Documentation slimming and validator regressions may ship while live effectiveness remains unverified.
