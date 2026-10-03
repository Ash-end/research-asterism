# Synthetic input/output examples

All settings, data, and source labels below are invented for teaching. They are not published findings. These compact outputs illustrate the intended form, not evaluated model outputs.

## 1 · Field and method map

**Input:** “For a toy corridor lighting controller, fixed schedules assume stable daylight; a sensor threshold chatters under noise; two thresholds preserve state. The corridor needs few accidental switch-offs and low maintenance. Help choose a research question.”

**Illustrative output:** First test whether state preservation reduces switching without increasing accidental switch-offs under the corridor's noise and delay conditions. This is a bounded controller-fit question; the supplied descriptions do not establish novelty.

| Application requirement | Priority/basis |
| --- | --- |
| Avoid accidental switch-offs | Essential in the supplied toy scenario |
| Low maintenance | Important; operational definition still needed |

| Method capability | Evidence and conditions |
| --- | --- |
| Fixed schedule | Simple computation; supplied description; daylight stability assumed |
| Sensor threshold | Potential noise-induced switching; supplied description, no measurements |
| Two thresholds | Intended state preservation; effect under target noise remains untested |

Group these by time schedule and measurement feedback; the dual threshold changes feedback behavior. A small synthetic noise sweep with matched inputs can measure switching and accidental switch-offs. Continue if both target needs are met; adjust the thresholds if switching falls at the expense of unacceptable switch-offs. Define the unacceptable rate before the test.

## 2 · Idea assessment

**Input:** “My new library helper combines retrieval and ranking. An older synthetic note already describes retrieving candidates and ranking them. Is my combination a contribution?”

**Illustrative output:** The combination's mechanism overlaps with the supplied predecessor. A contribution remains possible if a justified new constraint or a nontrivial improvement survives comparison. First specify the library need, the closest baseline, and the changed assumption.

A candidate hypothesis is that a lightweight location constraint reduces fruitless shelf visits; a rival is that any gain comes solely from a better catalog. Compare the same catalog with and without the location constraint and with an equally informed simple baseline. Measure shelf visits and successful finds, not only ranking accuracy. This is a proposed synthetic test, not an executed study. Stop the claimed new-mechanism framing if the predecessor already establishes it; retain a bounded adaptation if useful and supported.

## 3 · Result diagnosis

**Input:** “A toy predictor got accuracy 92% on dataset A; another got F1 0.89 on dataset B. Should I call the first better?”

**Illustrative output:** These observations do not support that ranking: the metric and dataset differ. Source facts are the two reported values; the comparative inference is unsupported. Next evaluate matched inputs, information access, tuning budget, and the target metric. Keep uncertainty and test-set provenance. A positive matched result would support the tested comparison, not general superiority; an inconclusive result should trigger a sensitivity or measurement check before scaling.
