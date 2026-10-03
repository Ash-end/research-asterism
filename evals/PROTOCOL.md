# Evaluation protocol

This package has two distinct verification layers. Neither certifies novelty or research correctness across domains.

## Deterministic checks

Run `scripts/validate.py` and the standard-library tests. They check frontmatter, local links, Python syntax, case/label consistency, required release files, and safe package paths. They do not infer scientific quality from keywords or calculate an “innovation score.”

## Independent behavior and routing

Give a fresh independent agent only the entrypoint, needed references, and raw requests from `cases.json`. Do not give it sample answers, trigger labels, the author's conclusions, or suspected failure modes. Give it an isolated output directory and current resource restrictions. Ask it to perform each request as received, preserving case IDs and recording what was read and actually executed.

For routing, give the independent agent the skill's name/description and raw `triggers.json` requests. Ask for a semantic applicability decision with a brief reason. Keep `trigger-labels.json` withheld until grading. Routing classification is a proxy, not proof that the host's automatic loader will select the skill.

For a with/without comparison, send the same raw requests and resource restrictions to a separate fresh agent without the skill. Keep contexts and outputs separate. Do not label a rewritten author answer as a baseline.

For new runs, use a fresh context per case and condition, with the same response-budget instruction. Record actual lengths; a common ceiling does not match lengths. Mask condition labels as A/B with recorded seeded, balanced placement. A separate fresh comparator receives the reversed placement; do not give either comparator the mapping or the other's report. Supply original raw requests and actual outputs. Judge scientific correctness, decision usefulness, claim support, discriminating design and task constraints, citing concrete output content. Allow ties. Give no case-specific expected conclusions. Reveal the mapping after both reports are saved. Distinguish position sensitivity from disagreement between different comparators; reversal alone cannot isolate their causes.

Record the execution date, actual condition, model identity if exposed, source-reading scope, tool/resource limits, output files, failures, and whether evaluation was repeated. Keep unchanged negative results. A single model-family pass on six synthetic cases is a regression sample, not a statistically supported performance estimate or cross-domain benchmark.

For an actual run, retain the dispatch messages with only private path redaction, input/output SHA-256 fingerprints, available agent configuration, and the source revision or release fingerprint. Separate instructed and self-reported isolation from independently verified isolation. Unknown model settings and chronology remain unknown. See [the retained run record](RUN.md); it does not claim an access audit.

The earlier record keeps its original P/Q protocol and outputs; it was not retroactively rerun under these controls. The review-informed [scientific cases](scientific-cases.json) are development regression items, not held-out tests. See [the scientific revision record](SCIENTIFIC-REVIEW.md). The optional `tests/site-check.cjs` uses Playwright and a Chromium browser to test UI behavior and an explicit no-data display contract. It does not infer scientific validity from text matching. Browser dependencies are separate from the standard-library package checks.

If separate contexts or native agents are unavailable, mark behavior/with-without as **not run**; do not invent results. No paid provider call, training, external search, or real-project execution is required by this protocol.
