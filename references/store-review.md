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
