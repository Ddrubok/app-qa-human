# Screenshot evidence

Use baseline privacy/evidence rules. Live QA defaults to screenshots=on; accept equivalent user wording. State the effective option at the start and in the report. The latest explicit choice applies from the next action through that task. A separate task defaults ON unless a broader preference was explicit. Switching OFF does not delete earlier files; label their capture period if referenced.

## ON

Capture relevant start/result states for every tested case, including passes, failures and partial checks. Preserve a defect before leaving the state and capture recovery/retest when exercised. Reuse genuinely identical state evidence; do not capture each keystroke. Prefer the project's evidence layout, otherwise `run-id/screenshots/{case_id}_{step}_{state}.png`, for example `TC-012_03_after-save.png`. Use stable IDs, no personal data in filenames, and avoid overwriting prior runs.

Check capability separately: capture available? saved-file image inspection available? safe data/capture region available? Prefer synthetic data and pre-persistence exclusion/redaction. If sensitive information cannot be excluded, omit that capture and record why even when ON. A missing image viewer does not relax privacy requirements.

When inspection is available, open the saved file and check state, legibility and relevance before describing its visual content. Blank/loading/wrong-screen/over-redacted images require replacement or an explicit gap. A white file alone does not establish whether the app or capture process failed.

When a safe capture is saved but image inspection is unavailable, retain its path with `visual_review=unavailable` and label **Image file created (unverified visually by agent)**. It may be linked as an uninspected artifact, never as visual proof. Continue DOM/accessibility/text/log/file checks. Block or leave untested only the visual-dependent portion; do not fail an otherwise verified functional outcome because no viewer exists. Do not claim visibility, clipping, contrast or appearance from DOM text alone.

Record per image: `path, case_ids, step, capture_status, visual_review, evidence_origin, proves, limitations`.
- capture_status: saved / unavailable / not-run / disabled.
- visual_review: verified / unavailable / not-run / unusable.
- Run screenshot coverage: complete / partial / unavailable / disabled / not-run; document-only work is not-applicable. Complete requires all required saved images to be inspected and usable. Saved-but-uninspected images are partial, not complete. A capture plan is not-run.

## OFF

No new screenshot/capture calls, including automatic image-return workarounds. Use DOM/accessibility/text/file evidence. If the only tool unavoidably captures, defer only dependent steps. Existing supplied images may be analyzed if requested; this does not permit new capture. Record visual limits without turning missing screenshots into functional failures.

## Evidence limits

Document-only planning, report rewriting or report comparison does not authorize runtime capture. Attribute supplied/manual images accurately. A static image cannot establish tap behavior, keyboard access, focus order, announcements, persistence, timing or exact physical target size. Contrast measurements require actual colors/context and attention to scaling. No viewer means no visual verification; DOM availability is not a replacement for it.
