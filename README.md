![Research Asterism: frame questions, examine assumptions, choose an informative test](assets/banner.svg)

[![Validate package](https://github.com/Ash-end/research-asterism/actions/workflows/validate.yml/badge.svg)](https://github.com/Ash-end/research-asterism/actions/workflows/validate.yml) [![MIT](assets/license.svg)](LICENSE) [![Version 0.4.0](assets/version.svg)](https://github.com/Ash-end/research-asterism/releases/tag/v0.4.0)

# Research Asterism

A portable **research-methodology** Agent Skill for framing questions, comparing methods, developing testable ideas and interpreting results. It starts with an actionable judgment, the evidence boundary and the next informative step.

[中文](README.zh-CN.md) · [Website](https://ash-end.github.io/research-asterism/) · [Quick start](docs/GETTING-STARTED.md) · [Original guide](docs/HANDBOOK.md) · [Evaluation](docs/EVALUATION.md) · [Sources](SOURCES.md)

## What you can bring

| Starting point | Useful decision | Possible output |
| --- | --- | --- |
| A topic or reading collection | What should I understand or read next? | Question framing, method families and a focused reading route |
| A proposed idea or mechanism | Is this worth testing, and how? | Assumptions, nearest neighbors, competing predictions and a minimal test |
| Positive, negative or conflicting results | What is supported, and what next? | Rival explanations, validity checks and continue/adjust/stop conditions |
| A proof or qualitative interpretation | Which dependency or interpretation needs scrutiny? | Conditions, counterexamples or material-grounded rival readings |

A topic alone is enough. Existing project records are reused. No fixed paper count, candidate quota, scoring system or agent topology is imposed.

## Start in three minutes

Clone the source, then install into a target Codex project. Python 3.10+ is needed only for the offline helpers.

```sh
git clone https://github.com/Ash-end/research-asterism.git
```

From the target project, use the source's actual path:

```powershell
python 'C:\path\to\research-asterism\scripts\install_skill.py' --target '.agents\skills\research-methodology'
python 'C:\path\to\research-asterism\scripts\install_skill.py' --target '.agents\skills\research-methodology' --check
```

The installer validates the source, copies ten runtime files and refuses an existing target. It makes no network or model calls. Open a new host session to refresh discovery; other hosts can read `SKILL.md`, but automatic integration is not certified here. [Installation details and POSIX command](docs/GETTING-STARTED.md).

```text
Use $research-methodology.
My topic is calibration under distribution shift. I have no papers or data yet.
Help me frame the question, compare assumptions and choose what to check next.
Do not run experiments.
```

## Three modes, one evidence loop

![Question → assumptions → limit → hypotheses → validation → decision, with iterative reading and retrieval](assets/workflow.svg)

| Mode | What it does | Detailed example |
| --- | --- | --- |
| Field and method map | Organizes mechanisms, assumptions and historical changes; separates needs from measured performance | [Population shift](site/workflows.html#map) |
| Idea assessment and minimal test | Examines the claim, nearest neighbors, competing explanations and a decision-changing validation | [Incomparable reports](site/workflows.html#idea) |
| Result diagnosis and next step | Checks measurement, mechanism activation, uncertainty and the scope of positive or negative evidence | [Unstable differences](site/workflows.html#result) |

**First-principles reasoning** is optional support within these modes: separate targets from observations; trace assumptions and constraints; transfer principles only with their conditions; derive competing predictions; check whether the test activated its mechanism. It complements literature and experiments. It does not turn intuition into fact or force every field into physics or mathematical axioms.

## A compact example

**Constructed input:** “Everywhere-differentiable functions have continuous derivatives. Can a few numerical examples prove this?”

**Illustrative judgment:** No. Finite examples cannot prove a universal claim, and the claim is false without stronger premises. Let `f(0)=0` and `f(x)=x² sin(1/x)` for `x≠0`. The derivative at zero exists and is zero, while the derivative for nonzero `x` is `2x sin(1/x) − cos(1/x)`, which has no limit at zero. The next useful step is to revise the theorem's assumptions and trace its proof obligations, rather than expand the numerical table.

This is an analytical example, not a new empirical finding. [More synthetic inputs and outputs](examples/synthetic-examples.md) · [Original guide](docs/HANDBOOK.md).

## Evidence and execution boundaries

- Label source reports, inferences and untested hypotheses. A citation must support the specific claim and conditions.
- Keep requirements, assumptions, evidence status and actual performance separate. No measurement means no data; incompatible protocols do not establish a ranking.
- Use the relevant evidence obligation for descriptive, predictive, causal, measurement, theoretical and qualitative work. Prediction does not identify causality; a null result does not establish equivalence.
- Search nearest neighbors, including older equivalent ideas. A failed search or module combination does not establish novelty.
- Detect the tools available now. Missing retrieval yields a provisional plan with explicit uncertainty. Data, experiments, paid tools and publication require the current task's authority.

The skill does not resume old research, train models or disclose materials automatically, and makes no publication acceptance promise. [Claim design](references/claim-design.md) · [Architecture](docs/ARCHITECTURE.md).

## Inspect the evaluation

The historical v0.3.0 six-case development run used fresh with/without contexts and the same answer ceiling. Two masked comparators, with positions reversed, preferred the skill in **4/6 and 3/6** cases; the reverse comparison preferred the baseline once. They disagreed on two cases. These are development regressions, not held-out effectiveness evidence; actual lengths differed by +4.6% with the skill.

v0.4.0 adds assumption-led guidance. Its new author-run sanity checks are explicitly separate; **no new independent with/without comparison has been run**. Historical raw outputs and fingerprints are preserved, with the former entrypoint versioned. [Results, limitations and reproducible records](docs/EVALUATION.md).

```sh
python scripts/validate.py .
python -m unittest discover -s tests -v
```

These commands check package structure and regressions, not scientific novelty or truth. Optional browser checks need Playwright and a compatible browser; no model API is used.

## Read, adapt and contribute

- [Getting started](docs/GETTING-STARTED.md): installation, invocation and tool expectations.
- [Workflows](docs/WORKFLOWS.md): three modes and synthetic decisions.
- [Original research guide](docs/HANDBOOK.md): problem framing, assumptions, reading, ideas and discriminating validation, in Chinese.
- [Architecture](docs/ARCHITECTURE.md): progressive loading, runtime boundaries and maintenance.
- [Contributing](CONTRIBUTING.md), [security and privacy](SECURITY.md), [changelog](CHANGELOG.md), [software citation](CITATION.cff).

## Authorship and license

Original implementation and artwork by this repository's contributors, MIT-licensed. General inspiration includes Peng Ming-Hui's research teaching and the maintainer's custom first-principles research skill. The original guide uses independent organization and wording. The supplied 14-page secondary adaptation, source figures, full transcription and private project records are excluded. Attribution does not imply the source authors' participation or endorsement.

Upstream skill repositories were studied for organization and evaluation design; popularity is not evidence of research quality. No upstream skill text or code is copied, including noncommercial material. [Exact source, retrieval and license boundaries](SOURCES.md).
