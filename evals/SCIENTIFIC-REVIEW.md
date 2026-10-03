# Scientific review and development evaluation

Release context: v0.3.0, dated 2026-10-03. The review and behavior runs below were completed before publication. Their original inputs, answers, preferences, hashes and execution limitations are preserved. Private review bundles are not distributed with the public release.

## Confirmed defects in the published version

- The showcase's performance matrix put a suitability assumption and a pending-measurement note in performance cells. Those were not performance measurements. This contradicted its own requirements/performance distinction.
- Maintenance burden lacked an operational definition. Switching count had no demonstrated link to maintenance labor and could not substitute for it.
- Existing instructions included several appropriate boundaries but did not sufficiently connect claim type to an executable design choice, units, validation, and uncertainty.
- The commercial-style showcase and domestic example did not clearly explain a scientific question, object, protocol or evidential judgment.

The local revision separates requirements, assumptions, evidence state and actual performance, uses no-data entries where there are no measurements, and replaces the page with original research-documentation layout and explicit constructed scenarios. These content choices are assessed manually and in behavior evaluation; DOM checks do not establish scientific correctness.

## Original behavior record: unchanged result, narrower interpretation

The original six-case outputs and preferences are unchanged. Independent review counted 4,038 characters with skill versus 3,207 baseline (about 26% more); the counting convention was not retained, so these are reviewer-reported counts, not a reconstructed instrumented metric. Each condition answered all six cases sequentially in one context, and P was always baseline while Q was always skill. Length, presentation order, and context carryover are potential confounders. The apparent three slight preferences and three ties are one qualitative development regression, not evidence that the skill causes an improvement. The prompts also made several rules and desired cautions explicit, limiting what the old cases tested.

## New development run

The new raw cases concern prediction under deployment shift, causal service evaluation, measurement/negative evidence, a theoretical derivative claim, qualitative explanation, and an explicit assumption/proxy/selected-success matrix regression. They are author-designed development cases informed by review, **not held-out blind benchmark items**. Performers receive raw materials and, for the skill condition, the skill/references; no expected answers, examples, author conclusions or prior outputs. Each case uses its own fresh native-agent context in each condition. Both conditions receive the same answer-size instruction. Preserve actual output lengths rather than trimming answers.

Comparison uses masked pairs with a recorded seeded order and a second presentation reversing left/right positions, given to separate fresh comparators. They receive the raw cases and outputs, not author's expected answers. Even with these controls, small author-designed samples, shared model family, self-reported access boundaries and unknown sampling settings limit interpretation. Record failures and disagreements; do not turn preference counts into a claim of general scientific effectiveness. Structural/browser validation is separate.

The actual 12 answers, two masked comparisons, path clarification failures, source/answer fingerprints and decoded preferences are retained in [SCIENTIFIC-RUN.md](SCIENTIFIC-RUN.md). Forward: four skill preferences and two ties. Reversed: three skill preferences, one baseline preference and two ties. Two cases differ between comparators. The same answer ceiling produced 6,142 versus 5,870 Unicode code points (+4.6% with skill); verbosity remains a possible confounder. These results are qualitative development observations, not proof of improvement.

## Local structural and browser verification

The local skill-creator validator, package validator and 11 standard-library regression tests passed. Two added regression tests detect aggregate/per-case drift and duplicate scientific case IDs; they check fixture integrity only. The new optional [browser harness](../tests/site-check.cjs) passed 41 checks in Microsoft Edge via Playwright, covering local root/subpath routing, separate assumptions/requirements/performance displays, explicit no-data estimates, tabs and keyboard navigation, both clipboard operations and denied-clipboard fallback, four viewport widths for landing/docs, disclosures, relative resources, absence of external assets/browser errors, reduced motion and reading without JavaScript. [Actual browser record](results/scientific-site-check.json) is retained. Desktop and mobile screenshots were visually inspected; they are outside the release allowlist.

Two initial harness assertions used different wording from the page's existing disclaimer/fallback text and failed. They were corrected against the observed page text; no product change was required for those failures. The explicit matrix contract guards the confirmed UI defect but does not certify scientific truth. The original nine boundary regressions remain, and old browser records are historical.

Optional browser reproduction: serve the package parent, then run `node tests/site-check.cjs http://127.0.0.1:8000/research-methodology /absolute/path/outside-package-qa`. Install Playwright and its Chromium browser separately, or set `PLAYWRIGHT_MODULE` to an existing module path and `BROWSER_EXECUTABLE` to an existing compatible Chromium executable. No browser or model dependency is needed for the standard-library checks.

## Scientific acceptance: precise wording fixes

After an independent scientific acceptance review, the first showcase table now says “策略/机制” and explicitly states that strategies can be combined and are not mutually exclusive categories. The second mode heading now says “验证设计”; it does not promise sufficiency. English/Chinese guides and adjacent documentation use the same meaning. Nine targeted browser checks passed for these labels, disclaimers, docs and mobile overflow, with current desktop/mobile screenshots visually inspected. The prior 41-check full browser run, 11-test regression and copied-install evidence remain historical runs before these wording edits, not claimed reruns. Behavior inputs, cases, answers and comparisons are byte-unchanged; model evaluation was not rerun. This records the acceptance-stage candidate. Publication of v0.3.0 was subsequently authorized; the scientific behavior records were not rewritten or rerun for the publication-status change.
