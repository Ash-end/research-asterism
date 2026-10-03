# Three modes and a complete constructed example

Every label, timing and numeric value below is synthetic teaching material. No paper retrieval or experiment was performed. Use the example to inspect reasoning, not as evidence of a new scientific method.

## Field map: batch reading to a targeted route

Input: six abstract-level notes: direct scaling (2012, zero bias), zero reference (2016, timing undefined), refreshed zero reference (2020, critiques stale references), channel differencing (2013, relative only), robust aggregation of differences (2019), and a renamed neural method (2022, mechanism absent). Need: absolute recovery in a changing environment.

Actionable judgment: first study the reference-correction family and its reference timing; the differencing family offers a useful contrast for absolute versus relative information. Leave the named neural approach unclassified until its mechanism is available.

Group on operation/premise: scaling → reference correction → refresh within one related route; difference → robust aggregation within another. These are tentative relationships from supplied notes. The 2020 critique of stale references is an author report until checked. Read the clearest reference explanation first, then its definition of reference time, then the refresh procedure and cost. Update keywords around stale reference, bias tracking and absolute anchoring; there is no need to wait for a paper quota.

## Understanding: guess, check and correct

First question: does `(y-y0)/g` remove all drift in `y=gx+b_t`? The timing of `y0` is missing, so full cancellation is only conditional. Full-text definition later says `y0=b_0`, measured initially at a known zero signal. Corrected inference: error is `(b_t-b_0)/g`. It removes initial bias, and remains useful if later bias stays near it, but does not remove arbitrary drift. This is a derivation, not an observed experimental result.

## Two tables: method properties and application needs

| Synthetic method | Property under conditions | Support | Given design cost | Unknown |
| --- | --- | --- | --- | --- |
| A: `y/g` | Absolute recovery when `b=0`, known nonzero gain | Derivation | 2ms | Actual environment performance |
| B: `(y-z)/g` | Bias cancels if contemporaneous zero reference `z=b` | Derivation | 12ms | Reference noise and measured cost |
| C: channel difference | Common bias cancels; absolute anchor absent | Conditional derivation | Unknown | Timing and absolute anchor |

| Synthetic setting | Needed property | Threshold/basis | Current fit |
| --- | --- | --- | --- |
| S1: bias zero | Absolute output | 3ms limit, supplied | A fits the stated model and cost |
| S2: varying bias | Absolute output | 20ms limit, supplied | B fits if reference premise holds |

Provided costs are design inputs, not actual measurements. C's timing is unknown rather than poor. Neither table is an overall score. An established sufficient answer can finish here.

## Constructing a concrete candidate

New synthetic need: `y_t=x_t+b_t+noise`, arbitrary unknown `x_t`, slowly varying bias with possible jumps. Ordinary readings cost 2ms; a known-zero reference is extra and costs 20ms. Mean cost per ordinary reading must be ≤4ms.

Candidate: acquire a known-zero reference every K ordinary readings; update a stored bias estimate from the reference; subtract the latest estimate from subsequent ordinary readings; report the time since reference and invalidate or flag it beyond the chosen freshness rule. A periodic schedule avoids inferring bias from an arbitrary signal. Choose K≥10 to satisfy `2+20/K≤4`; use K=10 as the budget-feasible starting baseline, not a universal optimum. Fast drift and jumps can produce residual bias until the next reference; reference noise remains. Mean budget does not guarantee worst-case latency.

The retained advantage is an absolute anchor; the cause addressed is a stale reference. The conjecture is that refresh improves error sufficiently in the intended drift regime. This is a classical-looking conditional candidate; novelty has not been established. Avoid calling the procedure innovative simply because it is expressed as multiple modules.

Minimal check: analytically or in an authorized toy pilot compare initial-only correction, periodic refresh and a same-reference-budget alternative across constant bias, slow drift and jumps. Keep signal/noise information and resources matched. Examine residual bias, absolute error, reference budget and jump recovery delay; define a meaningful improvement before examining outcomes. A positive difference still needs a rival explanation and boundary check. An effective negative result can stop this parameterization without disproving all bias correction.

## Local result diagnosis

A constructed negative packet says delivery and independent predefined mediator checks were valid; predicted residual-bias reduction ≥0.10, observed reduction 0.002 with interval[-0.005,0.009], and no expected outcome gain. The interval contradicts that meaningful reduction under the stated conditions. Preserve this failure of the intervention-to-mediator prediction and stop or revise its premise; do not automatically call the test invalid or conclude every setting is impossible.

A local formula question may need only: `y/g-x=b/g`, so the estimate is exact when `b=0` (with known nonzero `g`). No full workflow is needed.

## Existing diagnostic examples

The [earlier synthetic examples](../examples/synthetic-examples.md) retain incomparable protocols, negative evidence and a counterexample to an overbroad theorem. They remain useful for diagnosis. Their presence does not substitute for constructive behavior assessment.
