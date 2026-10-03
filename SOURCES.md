# Sources, authorship, and licensing

Reviewed 2026-10-03. Research Asterism is an independently created original implementation, maintained by its repository contributors. Attribution to Professor Peng Ming-Hui describes inspiration; it does not imply his participation, review, affiliation with this project, or endorsement. No upstream skill text, code, PDF, screenshots, or full handbook transcription is included. Popularity is not evidence of scientific quality or measured skill effectiveness.

## Handbook inspiration and attribution

The user attributes the supplied 14-page **科研学习手册** to **彭明輝 (Ming-Hui Peng / Ming-Hui Perng), National Tsing Hua University**. Independent public evidence supports the author's affiliation and his research-teaching approach: an [official NTU 2017 lecture notice](https://www.ntu.edu.tw/english/spotlight/2017/1269_20171114.html) identifies him as an emeritus professor at NTHU and describes literature-based understanding, critical assessment, and innovation. This confirms the person and broad approach, not the exact supplied PDF's edition or compiler.

The author's [2017 preface and contents page](https://mhperng.blogspot.com/2017/08/blog-post_15.html) and [ebook information page](https://mhperng.blogspot.com/2017/09/blog-post_17.html) are public source leads for **研究生完全求生手冊**. Search metadata located these pages, but full-page retrieval returned HTTP 429 during this build; their full text and any original download were not inspected. The published book and the shorter supplied PDF must not be treated as the same edition on this basis. An exact original public manuscript was not independently located and compared.

The Library's supported local materialization failed on Windows metadata handling. After separate authorization to inspect an existing local copy, the recorded local PDF was read: it has 14 pages and 1,057,875 bytes, matching the Library's recorded size. Its full page-by-page text matched the complete previously inspected extraction after whitespace normalization. Pages 4, 10, and 11 were rendered afresh from that local PDF and visually inspected. A local SHA-256 was recorded privately. Library supplied no content hash, so **byte identity to the Library item remains unverified and the Library materialization is not claimed successful**.

The inspected 14-page local PDF uses condensed, numbered summary sections, mixed script conventions, and reproduced diagrams. These features suggest an edited or summarized version; without comparison to a verified public original, **the compiler, completeness, exact edition, and derivative status remain unconfirmed**. The supplied author's name is attribution from the user, not proof that every rewritten sentence was authored by him.

General inspiration carried forward in original language: reason from the problem's important attributes and application needs; study method families and their evolution; understand assumptions and limits; alternate reading with retrieval; compare needs against capabilities; check proof conditions and logical dependencies.

New design in this package: three adaptive decision modes, explicit source-report/inference/hypothesis labels, tool capability detection, nearest-neighbor and novelty calibration, minimal rival-discriminating validation, null-result interpretation, optional output forms that reuse project records, synthetic behavior evaluation, and an original accessible showcase. Fixed paper counts, publication quotas, degree schedules, categorical shortcuts about proofs, and assurances of publication were not adopted.

No redistribution permission or open license for the handbook has been verified. Attribution does not grant permission. The handbook PDF, extracted text, diagrams, local identifiers, and private source locations are excluded from the release. MIT does not apply to the source handbook.

## Upstream designs checked

| Work and exact inspected files | Observed license | Design inspiration and boundary |
| --- | --- | --- |
| K-Dense: [scientific-brainstorming](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-brainstorming/SKILL.md), [literature-review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/literature-review/SKILL.md), [brainstorming tests](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/tests/scientific-brainstorming/test_scripts.py), [literature tests](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/tests/literature-review/test_scripts.py) | [MIT](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/LICENSE.md) | Evidence-aware ideation, claim/source support checks, and offline package tests; no bundled external CLI or copied procedure |
| Orchestra: [brainstorming-research-ideas](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/main/21-research-ideation/brainstorming-research-ideas/SKILL.md), [rigor-reviewer](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/main/22-agent-native-research-artifact/rigor-reviewer/SKILL.md) | [MIT](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/main/LICENSE) | Problem framing and semantic assessment of claim support; no imported ARA registry, grade system, or mandatory topology |
| Imbad0202: [academic-research-suite router](https://github.com/Imbad0202/academic-research-skills-codex/blob/main/skills/academic-research-suite/SKILL.md) | [CC BY-NC 4.0](https://github.com/Imbad0202/academic-research-skills-codex/blob/main/LICENSE) | Considered routing boundaries and distinction between structural checks and model effectiveness; **no text/code adapted, copied, or relicensed** |
| Anthropic: [skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | [Apache-2.0 for this skill](https://github.com/anthropics/skills/blob/main/skills/skill-creator/LICENSE.txt) | Real with/without execution and masked output comparison; no copied prompts, evaluator, or scripts |

These URLs refer to mutable upstream branches; the review date is not a pinned snapshot. No star counts are used to validate methodology. Upstream license observations describe the inspected files and are not a legal opinion about unrelated contents.

## Scientific revision: supporting sources and limits

Checked 2026-10-03 as primary-source support for selected design cautions. These references support the specified points; they do not validate this skill or every instruction. Original explanations are used, with no copied implementation or extended quotation.

| Source inspected | Supported scope and limit |
| --- | --- |
| [ASA summary of the p-value statement](https://www.amstat.org/asa/files/pdfs/P-ValueStatement.pdf) | A p-value is not an effect-size measure or a sufficient decision rule. The inspected three-page summary is not the full journal statement. It does not by itself specify equivalence margins. |
| [scikit-learn cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) and [common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | Prediction validation for grouped/time-dependent data and keeping learned preprocessing within training. These software docs do not identify causal effects or prescribe all scientific designs. |
| [NIST experimental design](https://www.itl.nist.gov/div898/handbook/pri/section3/pri3.htm), [randomized blocks](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm) | Controls, randomization and blocking for experiments where applicable; not universal requirements for theory or qualitative research. |
| [NIST TN 1297](https://www.nist.gov/pml/nist-technical-note-1297), [uncertainty components](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-2-classification-components-uncertainty) | Measurement uncertainty and its components. This does not establish construct validity or an application-specific meaningful-effect margin. |
| [Lazic et al., What exactly is ‘N’ in cell culture and animal experiments?](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2005282) | Experimental versus observational units and pseudoreplication in biological research; inspected abstract/introduction. Survey percentages are not generalized across fields. |
| [Cawley and Talbot, 2010](https://jmlr.org/papers/v11/cawley10a.html) | Model-selection overfitting can affect performance evaluation. The landing-page abstract was inspected, not a full-paper derivation. |
| [Miguel Hernán's Harvard profile](https://hsph.harvard.edu/profile/miguel-hernan/) | Well-defined causal questions and explicit observational assumptions. A historical book URL redirected here; the full Causal Inference book was not inspected for this revision. |

The theory and qualitative branches are original methodological guidance. They are not presented as validated by the software/statistical sources above. A mathematical proof, qualitative interpretation, metrological validity and predictive score each require support appropriate to their claim.

## Website design history

The earlier published page used [MotionSites](https://motionsites.ai/) and its [installation page](https://motionsites.ai/mcp) as visual references. That historical attribution is retained. The scientific revision in v0.3.0 replaces it with an original light research-documentation layout, constructed scientific scenarios and distinct assumption/requirement/performance/evidence displays. No upstream template, logo, screenshot, font or remote asset is bundled. No affiliation or endorsement is implied.

## License scope

The [MIT license](LICENSE) applies only to original content within this package: instructions, references, examples, scripts, tests, documentation, original website, and permitted synthetic evaluation outputs. It does not change the parent repository's license, grant rights to cited sources, or claim ownership of authors' underlying ideas. The local parent repository had no existing license when inspected; no repository-wide license was added. Contributions must be original or carry compatible, clearly recorded rights.
