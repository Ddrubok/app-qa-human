# Store review risk, not approval prediction

Use only when store/distribution checks are relevant. Establish platform, store, distribution channel, app category/audience, target regions, build/version, and features involved. A web-only prototype is not automatically subject to native store requirements.

Official entry points, checked for routing on 2026-10-06 (not an offline policy snapshot):

- Apple App Review Guidelines: https://developer.apple.com/app-store/review/guidelines/
- Google Play Developer Policy Center: https://play.google/developer-content-policy/
- Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
- Material Design: https://m3.material.io/

At review time open the current official section relevant to each claim, including linked exceptions and effective dates. Record URL, section/title, retrieval date, policy effective date if available, applicability, and the build evidence. If inaccessible, label policy currency unverified and give conditional verification items; cached knowledge alone cannot justify a current definite violation.

HIG and Material are design guidance; they do not automatically establish a store rejection rule. Cite the actual review/distribution policy for rejection risk. Do not treat a Material style difference, rounded card, or one screenshot as a policy violation. Requirements can vary by region, category, payment route, and distribution program; do not universalize one platform's rule.

Select applicable topics: app completeness/reviewer access, accurate listing and promises, privacy disclosures versus data collection, permission purpose and denial, account lifecycle, digital purchases/subscriptions, user-generated content controls, children/age rating, ads/SDK behavior. This is a topic index, not a frozen list of mandatory requirements.

Risk record:
`id, store, region, build, feature, policy_url, section, retrieved_at, effective_at, applicability, implementation_evidence, evidence_level, risk(high/medium/low/unknown), rationale, proposed_action, verification_needed`

Risk describes documented exposure, not a numerical rejection probability. Separate code gaps, runtime findings, and unknown operational processes. Do not guarantee approval or rejection. Do not claim App Store Connect/Play Console declarations match implementation without inspecting authorized evidence. Do not submit an app or change listings, billing, privacy disclosures, or account settings under a review-only request.

## Conditional policy checks

The following are starting questions, not a frozen 2026 rejection checklist or a claim about rejection frequency. Reopen the current official page before concluding applicability; record retrieval/effective dates and exceptions. Offline cached guidance supports conditional questions only.

| Topic | Check | Avoid this false rule | Official section |
|---|---|---|---|
| Apple account deletion | Account-creating apps offer an in-app initiation path; inspect completion, processing notice, legally retained data and subscription implications | Every account and all data must disappear instantly; support confirmation is forbidden even in regulated exceptions | https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion |
| Google account deletion | Applicable apps provide an in-app path and external web request resource; inspect associated data handling, retained-data reasons and reasonable processing expectations | Only native instant deletion qualifies, or no external request path is needed | https://support.google.com/googleplay/android-developer/answer/13327111?hl=en |
| AI-generated content | For applicable Google AI apps inspect restricted-content prevention and in-app report/flag flow; inspect user-generated sharing/blocking separately | Every AI feature requires the same user-blocking UI regardless of interaction model | https://support.google.com/googleplay/android-developer/answer/13985936?hl=en |
| AI labeling | Check applicable regulations and asset declarations in relevant Play Console content flows, independently of in-app disclosure obligations | Store-asset labeling guidance automatically mandates identical badges on every in-app AI output | https://support.google.com/googleplay/android-developer/answer/17262077?hl=en |
| Photo/video access | For Android scoped permissions, compare core functionality with minimum-scope alternatives; inspect declarations and limited/denied access behavior | READ_MEDIA_IMAGES always violates policy, including a gallery needing broad access; Android rules are identical on iOS | https://support.google.com/googleplay/android-developer/answer/16935362?hl=en |
| Subscriptions | Before enrollment check actual price/period, renewal, trial conversion and cancellation disclosure; inspect reachable management/cancellation | An arbitrary layout is a universal store requirement, or fine print elsewhere necessarily resolves misleading purchase copy | https://support.google.com/googleplay/android-developer/answer/9900533?hl=en and https://developer.apple.com/app-store/review/guidelines/#subscriptions |

Do not exercise production deletion or charges merely to inspect compliance. Policy conformity requires both applicable rules and actual implementation evidence; an excerpt alone does not establish an app passes review.
