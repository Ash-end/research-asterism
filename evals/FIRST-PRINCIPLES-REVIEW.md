# v0.4.0 first-principles development review

Executed 2026-10-03. [Raw synthetic requests](first-principles-cases.json) and [actual author-written responses](results/first-principles-author-run.json) are retained. The author read the candidate entrypoint and new reference, answered four cases in the same active authoring context, and manually reviewed the semantic decisions. No retrieval, real experiment, paid endpoint or external data was used.

| Case | Decision examined | Observed response |
| --- | --- | --- |
| p01 | Conditional transfer versus an unconditional feedback guarantee | Withheld stability/calibration guarantee, asked for operative conditions and suggested a counterexample |
| p02 | Information preservation versus usability by a finite reader | Preserved the distinction and bounded a possible analytical comparison; no novelty or real-performance claim |
| p03 | Failed implementation versus refuted mechanism | Identified the unperformed intervention as an untested hypothesis and respected diagnosis-only scope |
| p04 | Assumption-led qualitative reasoning | Retained selection, rival accounts and material obligations without forced mathematical or statistical formalization |

This is an author sanity check, not an independent blind evaluation. These observations are not pass rates or evidence that v0.4.0 outperforms v0.3.0. There is no new with/without run, trigger optimization or held-out benchmark for this revision. The historical six-case v0.3.0 results remain intact and are clearly identified in [evaluation documentation](../docs/EVALUATION.md).

Structural and browser regressions separately inspect source integrity, installation boundaries and interface behavior. They cannot establish correctness of these responses. Future independent review should use fresh raw cases, matched old/new contexts and balanced masked positions, preserving all disagreements.
