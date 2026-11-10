# Session memory and repeat use

Use for L1, L2, Lapsed and profile comparisons. Memory is a sanitized artifact, not permanent model learning or a backend service. Prefer the project's QA location; otherwise use `qa-runs/<campaign-id>/<run-id>/`. Preserve existing run files. Store no credentials, cookies, private account data or full diagnostic logs here.

## Keep three different records

| Record | Contents | May the participant receive it? |
|---|---|---|
| User learning | Observed controls, labels, visible rules, completion/recovery experience, unresolved misunderstandings | Yes, according to the profile |
| Product state | Account/role reference, save/progress, preferences, onboarding state, build and reset/retain method | Only normal user-visible facts and necessary setup |
| QA diagnosis | Source paths, internal routes, causes, test oracles, known defects and fixes | No for a cold or learning-only participant |

Record knowledge entries as `id, claim, origin, source_refs, learned_in_run, build`. `origin` is `observed` or `provided`. Use `source_refs` resolving to actual screenshot/action evidence for observed entries, or attributed supplied instructions for provided entries. Unknown build remains null. `learned_in_run` identifies the observation's run; provided knowledge uses null. Record misunderstandings/unknowns separately, rather than silently turning guesses into correct facts. Corrections retain their prior entry/reference.

## Run the sequence

1. Assign stable campaign/run IDs and keep case IDs stable across attempts. Give each attempt a separate logical record; several records may share one Markdown file or table. Separate JSON files are optional unless the consumer requires them. Never flatten different outcomes into one case status.
2. For L0 declare the starting user/data state: fresh, retained, seeded or unknown. Preserve intended first-use onboarding. A seeded demonstration is not an empty new account. Never clear a real user's storage or server data to manufacture a cold state.
3. After the attempt freezes, write `knowledge_after` with newly encountered user-visible learning. Include only evidence-backed facts; preserve unresolved misunderstandings separately. Record completed and incomplete tasks and the state left behind.
4. For L1 import selected prior learning as `knowledge_before` and link the prior report in `previous_run_refs`. Reopen the product and verify actual saved state; a memory file does not prove the product saved anything. Prior use may have failed: record that history honestly.
5. For L2 state why the relevant proficiency is supported (completed core tasks, mechanics used, recovered errors). Do not promote based only on elapsed time/session count. If absent, leave the L2 attempt not-run or declare seeded knowledge. Use `experience_basis=observed|seeded|mixed|none`; `none` is appropriate to L0 or an unexecuted plan, not an executed experienced profile.
6. When builds change, retain old knowledge with its build and check whether it still applies. Use Lapsed for the adaptation question. Do not claim real elapsed absence unless known; a simulated return is labeled as such.
7. Align build, goal, role, input/device and environment for a comparison; list intentional state differences and uncontrolled differences. Do not compare an admin's success against a guest's failure as a familiarity effect. Report dependent learning sequences separately from independent sessions.

Reopen records by ID when resuming interrupted QA. Append a new attempt for a changed build, hint or retest; do not overwrite the failure that motivated it. If only source inspection is possible, prepare not-run records and state the exact live steps unavailable.

## Experience extension 1.0

Keep report `schema_version: "2.0"` and existing case statuses unchanged. Attach one optional top-level `experience` object to each run report:

- `contract_version: "1.0"`, `campaign_id`, `run_id`, `profile` (`L0|L1|L2|Lapsed`). `compare` selects a campaign, not a per-run profile.
- `experience_basis`: `none|observed|seeded|mixed`; `previous_run_refs`: source IDs resolving to prior reports.
- `knowledge_boundary`: `status` (`verified|informed|contaminated|unverified`), `observation_mode` (`visual|assistive|guided`), `basis_refs` (setup evidence), `exposures` (known information leaks).
- `state`: `setup` (`fresh|retained|seeded|unknown`), `description`, `evidence_refs`.
- `assistance`: `external` (boolean matching the events), `events` (`kind: in-product|external`, `step_id`, `evidence_refs`). External assistance requires a new linked attempt.
- `knowledge_before`, `knowledge_after`: knowledge entries above; `unresolved`: remaining questions or misunderstandings.
- Optional `metrics`: observed action/backtrack/retry counts and separate product wait/tool overhead measurements. Unknown measurements are null, never zero by default.

Keep actual task outcomes and their evidence in `cases`; do not introduce a conflicting second pass/fail status. Map findings to the run/profile through the report and optional related run IDs. A strict legacy consumer receives the extension as a companion record linked by run/case ID, not unexpected keys.

Use [experience-run.json](../templates/experience-run.json) as an unexecuted example and [experience-report.md](../templates/experience-report.md) for readable reporting. Replace placeholders; never present example IDs or planned evidence as actual execution. The optional `scripts/validate_experience.py` checks record consistency, not whether tool execution or isolation really happened.
