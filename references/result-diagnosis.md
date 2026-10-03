# Result diagnosis and next step

Use for unexpected, conflicting, positive, or negative findings, and for a proof or counterexample affecting the research decision.

## Establish what happened

Identify the intended claim, actual observation, provenance, protocol, and uncertainty. Distinguish the user's report from artifacts inspected and from your interpretation. Check metric direction, units, denominators, dataset/version, splits, information access, resource and tuning budget, seed/repetition structure, and missing or selectively reported runs where these could change the judgment. Do not launch existing scripts merely because they are present.

Before ranking results, ask whether they estimate the same quantity under comparable conditions. A larger number across different splits, metrics, budgets, or populations is not comparative evidence. Keep each observation with its protocol and propose a matched comparison. Avoid converting incompatible results into a leaderboard.

## Build competing explanations

Connect the phenomenon to a dependency chain: input and measurement → mechanism and assumptions → expected outcome → observed outcome. Identify where evidence supports the chain and where it does not.

Consider explanations relevant to the case, such as violated assumptions, implementation or measurement error, resource confounding, leakage, sampling variation, insufficient sensitivity, or a false mechanism. Treat them as hypotheses with discriminating predictions. Do not select a root cause merely because it is common.

Pick the cheapest check that distinguishes consequential explanations. A fixed-budget baseline, a negative control, a boundary-condition sweep, or inspecting a decisive log may be more useful than increasing model size or training duration. Include what to do if the check is itself inconclusive.

## Calibrate positive and negative evidence

An improvement supports the tested comparison and conditions; it does not automatically identify the mechanism or demonstrate generality. Use ablations and independent settings when those claims matter.

A null or adverse result restricts the particular intervention, protocol, and effect range studied. Report effect estimates and precision if available. Failure to reject a null is not proof of equivalence, absence, or impossibility. A small, noisy run may be inconclusive. Adequately sensitive evidence can justify stopping the tested formulation without rejecting an entire research direction.

If a method's apparent gain disappears after controlling a confounder, update the claim and decision. Preserve negative observations instead of dropping them to rescue a story. A new failure or boundary is only a candidate contribution until reproducibility and existing knowledge have been assessed.

## For theoretical results

Write the statement, domain, quantifiers, and conditions precisely. Map each inference to an established premise, proved lemma, or explicitly open obligation. Check circularity, hidden regularity assumptions, and illicit interchange of operations or quantifiers. Distinguish sufficient, necessary, and necessary-and-sufficient claims.

Actively test small and limiting counterexamples. A valid counterexample within the stated domain disproves a universal claim; it does not invalidate every restricted variant. A counterexample outside the domain does not refute the theorem, but may expose why the application violates its assumptions. Numerical agreement cannot certify a universal proof. If a dependency cannot be inspected, leave that obligation unverified.

## Make the next step explicit

Give a bounded judgment: continue the tested claim, revise assumptions or protocol, stop this formulation, or seek evidence because the result is inconclusive. Identify the discriminating check and revisit condition. Fit any record to the project's existing format and do not create extra logs unless requested.
