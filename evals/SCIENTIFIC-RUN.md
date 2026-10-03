# Scientific revision: actual development run

Run date: 2026-10-03. Local only; no public commit, push, deployment, installation synchronization or Library update. [Machine-readable record](results/scientific-run.json) retains path-redacted dispatches, source/answer hashes, condition mapping, pair-placement seed and actual lengths. [Raw cases](scientific-cases.json) and [individual raw inputs](scientific-inputs/r01.json) are constructed, not real research records.

## Execution and controls

Twelve native performers answered six cases in separate fresh contexts per case and condition (`fork_turns="none"`). Skill performers received only the entrypoint, needed references and one raw case; baselines received only that case. Both had a 1,400-Unicode-code-point ceiling, no expected answers and no network, paid provider or scientific execution. Three initial skill dispatches needed a full-path clarification; this operational failure is retained. Other dispatches used the full path initially. Model identity/version, sampling settings, model seeds and independently verified start/end timestamps are unavailable. Reading boundaries and empty scientific-operation lists are instructed/self-reported, not an access audit.

Two fresh comparators received only the raw cases and actual masked answers, with no skill, examples, expected conclusions, condition mapping or other comparator report. Python `random.Random(20261003).shuffle` shuffled three with-skill-in-A placements and three baseline-in-A placements. The second presentation reverses every case. This seed controls presentation, not model generation. Both reports were saved before decoding the mapping. Separate comparators introduce evaluator variability; reversal alone cannot identify an order effect.

## Retained outputs and preferences

[With skill](results/scientific-with.json) · [Baseline](results/scientific-without.json) · [Forward pairs](results/scientific-pairs-forward.json) · [Reversed pairs](results/scientific-pairs-reverse.json) · [Forward comparator](results/scientific-comparison-forward.json) · [Reverse comparator](results/scientific-comparison-reverse.json)

Actual answers are retained without editing or truncation. Aggregation changes only JSON containers/formatting; raw executor fingerprints are distinct from packaged artifacts. Comparator and masked-pair files are byte copies.

| Development case | Forward comparator, decoded | Reverse comparator, decoded |
| --- | --- | --- |
| r01 | with_skill | with_skill |
| r02 | tie | without_skill |
| r03 | with_skill | with_skill |
| r04 | tie | tie |
| r05 | with_skill | tie |
| r06 | with_skill | with_skill |

The first comparator preferred skill in four cases and tied two. The reversed presentation preferred skill in three, baseline in one, and tied two. They agreed on r01/r03/r04/r06, while r02 and r05 differed. Do not pool these as twelve independent test cases or calculate a general win rate.

Concrete retained concerns: r01 still needs finite-sample calibration and uncertainty details; r02 needs calendar-time/exposure definitions for rollout and explicit missing-outcome assumptions (the baseline provided useful bounds/heterogeneity cautions); r03 needs a validated selective reference and intervention; r04's correct analytical counterexamples do not establish engineering stability; r05's repeated process accounts do not alone establish a dominant causal mechanism; r06 still needs personnel-time conventions and a rule for error after early failure. These are remaining design obligations, not silently repaired answers.

## Actual length, not matched length

Count rule: Python `len(answer)`, including whitespace, punctuation and Markdown, with no normalization or trimming. This counts Unicode code points rather than bytes or Chinese-only characters.

| Case | With skill | Baseline |
| --- | ---: | ---: |
| r01 | 1126 | 1066 |
| r02 | 977 | 1123 |
| r03 | 985 | 830 |
| r04 | 865 | 860 |
| r05 | 1054 | 968 |
| r06 | 1135 | 1023 |
| Total | 6142 | 5870 |

With-skill total is 4.6% longer. Identical ceilings reduce one protocol difference but do not remove verbosity confounding. The former review-reported 4,038/3,207 counts remain historical and are not mixed with this instrumented convention.

## Interpretation limits

These are review-informed, author-designed **development regression** cases, not strict held-out tests. The performers and comparators have fresh conversation contexts but share model family and executor. Masks are instructed, not cryptographically or access-audit enforced; answer style may reveal condition. No repeated seeds, cross-model replication, independent domain experts, real data, retrieval or project outcomes were tested. Preference judgments are qualitative and do not establish causal improvement, universal correctness, novelty or publication prospects. The earlier output/preference record is unchanged.
