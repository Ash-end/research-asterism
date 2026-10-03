# Sources, authorship, and licensing

Reviewed 2026-10-03. Research Asterism is an independently created original implementation, maintained by its repository contributors. Attribution to Professor Peng Ming-Hui describes inspiration; it does not imply his participation, review, affiliation with this project, or endorsement. No upstream skill text, code, PDF, screenshots, or full handbook transcription is included. Popularity is not evidence of scientific quality or measured skill effectiveness.

## Handbook inspiration and attribution

The user describes the supplied 14-page **科研学习手册** as their secondary adaptation of Peng Ming-Hui's public research-teaching material. This is user-provided provenance, not independent proof of rights in every included sentence or figure. The user chose an original guide instead of redistributing that document.

An [official NTU lecture notice](https://www.ntu.edu.tw/english/spotlight/2017/1269_20171114.html) identifies Professor Peng Ming-Hui as an emeritus professor at National Tsing Hua University. The [Linking Publishing book record](https://store.linkingbooks.com.tw/product/152126), inspected 2026-10-03, identifies **研究生完全求生手冊：方法、秘訣、潛規則**, published 2017-09-05, 328 pages, ISBN 9789570849929. This book is not treated as the same edition as the shorter supplied adaptation. The publisher's preface also discusses unauthorized historical reposting.

The author's [2011 literature-survey article](https://mhperng.blogspot.com/2011/04/literature-survey_18.html) is a canonical source lead. Direct retrieval encountered an access challenge in this revision, so a complete article comparison is not claimed. His [copyright statement](https://mhperng.blogspot.com/p/blog-page_78.html) was inspected and does not provide an open redistribution license; a [2015 notice](https://mhperng.blogspot.com/2015/05/blog-post_11.html) returned HTTP 429. Public availability and user adaptation are not treated as blanket permission.

The supported Library materialization previously failed on Windows metadata handling. After separate authorization, a local 14-page copy matching the recorded byte size was fully read, including fresh render inspection of pages 4, 10 and 11. Its text matched the earlier extraction after whitespace normalization. Library supplied no content hash; byte identity with the Library item remains unverified. No document, transcription, figure or private identifier enters the release.

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

## Maintainer-created first-principles skill

The complete local `first-principles-research` entrypoint and both references were read. The path matches the maintainer's identified custom skill; no upstream attribution or independent license file was present, and its local collection had no Git history. Authorship and third-party absence are not inferred from that fact alone. This package uses original explanations of general mechanisms: target/observation separation, assumption provenance, conditional principle transfer, competing predictions, exploratory versus confirmatory work, and checking whether a test activates its mechanism. No text is copied, and domain-specific configurations, private project histories and local paths are excluded. This is not a third-party dependency or a grant of permission to run other projects.

## Website design history

The earlier published page used [MotionSites](https://motionsites.ai/) and its [installation page](https://motionsites.ai/mcp) as visual references. That historical attribution is retained. The scientific revision in v0.3.0 replaces it with an original light research-documentation layout, constructed scientific scenarios and distinct assumption/requirement/performance/evidence displays. v0.4.0 adds original navy/teal/ivory artwork and layered documentation. The repository organization was studied in the four upstream projects listed above; no text, template, logo, screenshot, font or remote asset is bundled. No affiliation or endorsement is implied.

## License scope

The [MIT license](LICENSE) applies only to original content within this package: instructions, references, examples, scripts, tests, documentation, original website, and permitted synthetic evaluation outputs. It does not change the parent repository's license, grant rights to cited sources, or claim ownership of authors' underlying ideas. The local parent repository had no existing license when inspected; no repository-wide license was added. Contributions must be original or carry compatible, clearly recorded rights.
