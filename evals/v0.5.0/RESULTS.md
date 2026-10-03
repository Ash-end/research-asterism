# Actual v0.5.0 development results

The frozen v0.5.0 runtime was compared with the retained v0.4.1 runtime in 20 fresh case-condition contexts, producing 22 actual answer turns (d02 has a real second turn). Both independent masked comparators completed all 10 cases; the second reverses A/B positions. No expected conclusion was given to performers or comparators. See [protocol](PROTOCOL.md), [raw run and identity map](run.json), [first judgments](comparison-forward.json), [reversed judgments](comparison-reverse.json) and [decoded summary](summary.json).

## Preferences, separated by case origin

| Case set | Comparator | New preferred | Old preferred | Tie |
| --- | --- | ---: | ---: | ---: |
| Six design-informed development tasks | balanced | 0 | 1 | 5 |
| Six design-informed development tasks | reversed | 1 | 1 | 4 |
| Four independently authored tasks | balanced | 1 | 0 | 3 |
| Four independently authored tasks | reversed | 1 | 1 | 2 |
| All ten tasks | balanced | 1 | 1 | 8 |
| All ten tasks | reversed | 2 | 2 | 6 |

| Case | Balanced preference | Reversed preference |
| --- | --- | --- |
| d01 | old | old |
| d02 | tie | tie |
| d03 | tie | tie |
| d04 | tie | new |
| d05 | tie | tie |
| d06 | tie | tie |
| i01 | tie | old |
| i02 | tie | tie |
| i03 | tie | tie |
| i04 | new | new |

The two judgments disagree on d04, i01 (tie versus preference); these remain in the report. There is no demonstrated general advantage over v0.4.1. The cases exercise specified behaviors, not real research performance.

## Findings that matter

- Both comparators prefer old on d01: both classify and reason acceptably, but the new response repeats an eight-stage route when the novice asks for the most efficient next reading. The current skill's proportional-entry instruction did not prevent this overprocessing in that run. This is a known limit, not a removed failure.
- Both prefer new on i04: the old answer correctly calculated the main effects but later described the three old studies as positive/near-zero/reversed, although the third is positive; it also overstated established condition/measurement dependence. The new answer kept the uncertainty narrower. The old raw answer is preserved uncorrected.
- d02 genuinely corrects after a newly supplied reference definition. Both versions preserve the first answer and derive the residual; no claim of experiment execution appears.
- d03 gives separate need/property tables and correct conditional choices in both versions. d05 stays within 150 characters. d06 retains an effective failed mediator prediction rather than automatically calling the test invalid.
- d04, i01 and i03 contain viable concrete operations, resource accounting, compatibility or limitation and discriminating checks in both versions. The comparators did not identify an actual construction failure; that does not show the candidates meet untested empirical targets. Reversed judgments prefer new on d04 and old on i01; the other comparator calls both ties.
- The i01 old answer has a possible phrasing ambiguity about three films per recipe; the reviewer explains the budget-consistent reading and keeps the ambiguity visible. No raw wording was changed.

## Routing and response budget

Independent manual routing matched 12/12 existing positive/negative labels; [raw input](routing-input.json) and [classification](routing-output.json) are saved. This is not automatic host trigger testing. Old answer length totals 10,441 and new 10,867 Unicode characters (+4.1%, excluding the added turn labels). A common 1,800-character ceiling did not equalize length; the 150-character local request takes precedence. Tokens, reliable timing and per-call model IDs are not exposed and are not invented.

## Limits and preservation

Six cases reflect known design criteria and include an illustration related to runtime guidance. Four other tasks were independently authored after runtime freeze, in packaging materials, access networks, acoustics and memory evidence; they are still a small development assessment. One run per case-condition, shared host model family, no real retrieval/experiment, possible style clues, unmatched actual length and two reviews of the same answers limit inference. No claim of novelty, scientific truth, broad effectiveness or publication acceptance follows.

The frozen runtime was not edited against these outcomes, and no case was replaced to improve win counts. Old v0.3.0 comparisons and v0.4 author checks remain historical. `verify_evaluation.py` verifies retained bytes, not these reviewers' scientific judgments. Broader independent tasks and expert review remain future work.
