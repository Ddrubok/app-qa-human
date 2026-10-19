# Human error and recovery patterns

Select by journey risk, not every cell for every feature. For each selected pattern record setup, action, requirement/assumption, observed outcome and reset. Use synthetic data and existing authorization. Distinguish requirement violations from usability hypotheses; preserve acceptable alternative designs.

| Pattern | Exercise | Judge and preserve |
|---|---|---|
| Input boundaries | Leading/trailing spaces, empty/long values, supported emoji/special characters, paste, password visibility toggle | Use field-specific rules; passwords and free text may preserve spaces. Invalid input should have appropriate handling; do not require arbitrary Unicode support. Verify values survive save/reopen where promised. |
| Dirty state | Edit then Back, navigation, refresh or background/return | Confirm promised autosave/restore or an appropriate warning. No warning is not a defect when safe autosave/undo meets requirements. Do not persist sensitive inputs merely to avoid loss. |
| Duplicate action | Repeat submit during a controlled slow response, retry after ambiguous response | Inspect actual records/receipts or authorized sandbox outcome. Disabled buttons/debounce alone do not prove duplicate prevention. Do not trigger real payments. |
| Interruption | Keyboard, permission dialog, screen lock, background/restart; call only with suitable test tools | Distinguish resume from process recreation/session expiry. Observe data and session recovery. Do not claim real call/OS coverage from a browser tab switch. Restore device settings. |
| Destructive action | Inspect delete/reset/purchase consequence and confirmation path within authorization | Confirm clear scope, consequence and intentional commitment. Reauthentication, native confirmation or undo can be appropriate; no universal second-modal requirement. |
| Large text/keyboard | Actual supported OS text-size settings including large sizes; keyboard open, orientation, focus/navigation | Record exact device/settings; browser zoom is different from Dynamic Type. Check readable actions, reachable fields and recovery without assuming screenshot occlusion makes submission impossible. |
| Permission denial | Deny, revoke, limited access, retry via supported settings | Check explained limitation and supported alternatives; do not demand unrelated permissions. |
| Recovery and stale state | Offline/reconnect, expired session, stale tab, changed role | Verify actual outcome and data after retry; distinguish expected authorization denial from a broken flow. |

Do not use source-discovered hidden routes as first-time discoverability evidence. Keep good outcomes in the report; repeated failures must be reset between attempts rather than counted as independent causes.
