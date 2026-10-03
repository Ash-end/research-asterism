# Recorded evaluation

Build date: 2026-10-03. Independent behavior runs and masked comparison were executed with native agents; no external provider, retrieval, training, or real research project was used. Model identity was not exposed and was recorded as such.

## Actual behavior runs

- The skill-condition dispatch restricted inputs to SKILL.md, the needed references, and raw synthetic cases/triggers. It prohibited sample answers, labels, prior conclusions, and project history.
- The baseline dispatch allowed only the same six raw case requests and resource restrictions, in a separate fresh context, with no skill.
- A third fresh agent was given raw requests and actual paired outputs masked as P/Q, with instructions excluding the skill or condition mapping. P was the baseline, Q the skill; the mapping was not supplied to that agent.
- Outputs were retained without rewriting: [with skill](results/with-skill.json), [without skill](results/without-skill.json), [blind comparison](results/blind-comparison.json).

[Exact path-redacted prompts and hashes](RUN.md) document the retained run. Reading scope and empty scientific-operation lists are agent self-reports, not an independent access audit. `fork_turns="none"` established separate conversation contexts; shared executor access was not isolated. Per-case fresh contexts, exact seeds/model version, and independently verified execution timestamps are unavailable.

| Raw case | Sampled behavior | Comparator result |
| --- | --- | --- |
| c01 | Method classification/evolution and needs versus capability | Tie |
| c02 | Results with incompatible metrics, splits, information, and budgets | Skill slightly preferred |
| c03 | Old mechanism presented under a new name; residual contribution | Skill slightly preferred |
| c04 | Small, unpaired negative observations and a stopping claim | Skill slightly preferred |
| c05 | Universal claim, counterexample, and application scope | Tie |
| c06 | Topic-only mentoring, joint ideas, and insufficient evidence | Tie |

The comparator found the skill responses sometimes clearer about a cheap preliminary evidence check, source-scope limits, rival explanations, and a negative control. It also retained weaknesses: maintenance cost lacked an operational definition in c01; c03 did not fully vary repetition/update rates to map the benefit boundary; c05's baseline had a more complete matched performance design. These are limitations of the sampled outputs, not demonstrated universal failures or reasons to add a new mandatory workflow.

## Semantic trigger sample

All six positive and six negative raw requests were classified consistently with withheld reference labels. The agent supplied natural-language reasons; no keyword classifier was used. [Raw requests](triggers.json), [reference labels](trigger-labels.json), and the actual decisions in [with-skill output](results/with-skill.json) are inspectable. This tests semantic routing judgment, **not** the host's automatic loader or a live new-session discovery outcome.

## Structural and website checks

The local skill-creator quick validator passed with Python UTF-8 mode. The package validator passed. Initially five standard-library regression tests passed: missing references, unsafe release paths, exclusion of an unlisted private-marker file, preservation of an existing ZIP, and duplicate evaluation IDs. Release review added four tests for arbitrary source directory names, mismatched/correct installation names, and preservation of the advertised skill identity. All nine tests passed after the review fix. They validate packaging and fixtures only.

Release review separated source validation from `--installed` validation and limited CI to read-only repository contents with checkout credentials not persisted. Only the relevant offline regression checks were rerun; behavior inputs and answers were unchanged, and no new model evaluation or remote CI run occurred.

The website was run in Microsoft Edge through the existing Playwright installation. [Browser check record](results/site-check.json) records actual checks of mode selection, keyboard control, clipboard (accounting for Windows line endings), desktop/tablet/mobile overflow, reduced motion, documentation resources, console errors, external resource requests, root entry, and JavaScript-disabled reading. Desktop and mobile screenshots were visually inspected and provided separately in the review bundle. Browser QA code is local build tooling, not a scientific evaluation engine.

Two initial clipboard assertions failed because the QA harness compared Windows CRLF against DOM LF. Waiting for completion did not fix that; normalizing line endings did. The site code did not need a clipboard fix. A visual review also prompted hiding the unfocused skip link explicitly so full-page captures do not expose its off-viewport position. Final browser checks were rerun after that adjustment.

## What this does not establish

This is one six-case, single-family, fresh-context comparison, with no repeated seeds or cross-model replication. Author-created cases can still favor the proposed design. Shared model family and training are not independent expert review. No statistically supported win rate, real-world improvement, research novelty, or publication prospects are established.

No live scientific retrieval, PDF materialization, training, expensive experiment, remote CI run, GitHub Pages deployment, or public push was performed as part of these behavior checks. During source inspection, Library materialization failed because of Windows metadata incompatibility; a separately authorized existing local 14-page PDF was read and its three decisive diagram pages rendered and inspected. Library byte identity still could not be verified. Source provenance limits are in [SOURCES](../SOURCES.md).

## Publication branding checks

The Research Asterism branding and public links were checked locally under a /research-asterism/ project subpath. All nine offline regression tests and 30 Edge/Playwright checks passed, including 320/390/768/1440-pixel overflow, root redirect, linked resources, both copied commands, keyboard navigation, and reduced motion. The actual copied PowerShell command was executed in a disposable project: all 36 allowlisted files matched, the install directory remained research-methodology, Git internals were excluded, and an existing destination was refused without alteration. The original reasoning instructions, fixtures, and behavior outputs were unchanged. No new model evaluation was run. Remote commit, CI, and live HTTPS deployment verification are tracked separately from these behavior results.
