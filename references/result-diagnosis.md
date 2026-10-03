# Result diagnosis and next step

Start at the relevant dependency; do not force a complete literature workflow onto a local result question. For an effective negative test, distinguish undelivered intervention, delivered intervention with an absent predicted mediator, and changed mediator with an absent outcome using independent predefined checks. A valid absent-mediator result may challenge the intervention → mechanism link; it is not automatically an invalid test. Preserve the observation and failed prediction. A positive result calls for the strongest rival and a useful boundary. Return to the cause at learning-path step 7, or the requirement choice at step 6, only when the evidence warrants it. See [learning path](learning-path.md).


Use for unexpected, conflicting, positive, or negative findings, and for a proof or counterexample affecting the research decision.

## Establish what happened

Identify the intended claim, actual observation, provenance, protocol, and uncertainty. Distinguish the user's report from artifacts inspected and from your interpretation. Check metric direction, units, denominators, dataset/version, splits, information access, resource and tuning budget, seed/repetition structure, and missing or selectively reported runs where these could change the judgment. Do not launch existing scripts merely because they are present.

Before ranking results, ask whether they estimate the same quantity under comparable conditions. A larger number across different splits, metrics, budgets, or populations is not comparative evidence. Keep each observation with its protocol and propose a matched comparison. Avoid converting incompatible results into a leaderboard.

Identify the claim type before diagnosing it; use the relevant [design branch](claim-design.md). Distinguish assignment, independent sampling and measurement units. A result across repeated readings of one sample need not generalize to independently produced samples; a validation split across rows need not assess new participants or sites. Check how this affects both the target and uncertainty. An estimate and interval do not overcome invalid controls, selection, confounding or information unavailable at use time.

Inspect which configurations, subgroups and outcomes were tried and selected, as well as failed, timed-out, missing and excluded observations. An interval computed after selecting the best configuration/subgroup may not cover the selection process. Assess whether the claim needs a fresh assessment set, selection-aware analysis or narrower exploratory wording. Specify whether reported uncertainty covers samples, entities, sites, initialization or another source of variation; they are not interchangeable.

## Build competing explanations

Connect the phenomenon to a dependency chain: input and measurement → mechanism and assumptions → expected outcome → observed outcome. Identify where evidence supports the chain and where it does not.

Consider explanations relevant to the case, such as violated assumptions, implementation or measurement error, resource confounding, leakage, sampling variation, insufficient sensitivity, or a false mechanism. Treat them as hypotheses with discriminating predictions. Do not select a root cause merely because it is common.

Pick the cheapest check that distinguishes consequential explanations. A fixed-budget baseline, a negative control, a boundary-condition sweep, or inspecting a decisive log may be more useful than increasing model size or training duration. Include what to do if the check is itself inconclusive.

## Calibrate positive and negative evidence

An improvement supports the tested comparison and conditions; it does not automatically identify the mechanism or demonstrate generality. Use ablations and independent settings when those claims matter.

A null or adverse result restricts the particular intervention, protocol, and effect range studied. Report effect estimates and precision if available. Failure to reject a null is not proof of equivalence, absence, or impossibility. A small, noisy run may be inconclusive. Adequately sensitive evidence can justify stopping the tested formulation without rejecting an entire research direction.

To claim equivalence, justify a margin for the actual scientific/application quantity before inspecting the result and use an appropriate interval/test procedure. Instrument repeatability alone does not define a scientifically negligible effect. If effect size or precision is unavailable, request the relevant analysis or design information rather than manufacture an interval or imply that extra repetitions must solve the problem.

If a method's apparent gain disappears after controlling a confounder, update the claim and decision. Preserve negative observations instead of dropping them to rescue a story. A new failure or boundary is only a candidate contribution until reproducibility and existing knowledge have been assessed.

## For theoretical results

Write the statement, domain, quantifiers, and conditions precisely. Map each inference to an established premise, proved lemma, or explicitly open obligation. Check circularity, hidden regularity assumptions, and illicit interchange of operations or quantifiers. Distinguish sufficient, necessary, and necessary-and-sufficient claims.

Actively test small and limiting counterexamples. A valid counterexample within the stated domain disproves a universal claim; it does not invalidate every restricted variant. A counterexample outside the domain does not refute the theorem, but may expose why the application violates its assumptions. Numerical agreement cannot certify a universal proof. If a dependency cannot be inspected, leave that obligation unverified.

## Make the next step explicit

Give a bounded judgment: continue the tested claim, revise assumptions or protocol, stop this formulation, or seek evidence because the result is inconclusive. Identify the discriminating check and revisit condition. Fit any record to the project's existing format and do not create extra logs unless requested.
