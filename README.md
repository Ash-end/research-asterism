# Research Asterism

Research Asterism is a portable research judgment skill, invoked as `$research-methodology`. It turns a topic, paper, idea or result into a bounded research question and a useful next decision.

[中文说明](README.zh-CN.md) · [Showcase](site/index.html) · [Constructed examples](examples/synthetic-examples.md) · [Sources and rights](SOURCES.md) · [Scientific revision record](evals/SCIENTIFIC-REVIEW.md)

**Version 0.3.0 · Release date 2026-10-03.** [GitHub repository](https://github.com/Ash-end/research-asterism) · [Public showcase](https://ash-end.github.io/research-asterism/). The scientific revision preserves the original evaluation evidence and its limitations.

## Use

```text
Use $research-methodology. I want to study probability calibration
when a predictor moves to a new population. Help me frame the claim,
identify the evidence gaps, and design the next informative check.
```

Input can be a topic alone, supplied papers, a design, observations or existing project notes. State the current decision and known constraints when possible. Mentoring and joint ideation work across three modes:

| Mode | Decision support |
| --- | --- |
| Field and method map | Compare mechanisms, assumptions and evolution; keep requirements, evidence state and measured performance distinct |
| Idea assessment and minimal validation | Examine closest work and residual contribution; propose a discriminating validation design and assess whether it can answer the question |
| Result diagnosis and next step | Check comparison validity, rival explanations, uncertainty and continue/adjust/stop conditions |

The showcase labels reweighting, stable representations and target adaptation as **strategies/mechanisms**: they can be combined and are not mutually exclusive families. **Validation design** introduces a proposed check, not a guarantee of sufficiency.

Start with an actionable judgment, then use only the useful output forms. Reuse existing project records. Descriptive, predictive, causal, measurement and theoretical claims need different support; qualitative interpretation and engineering validation retain their own standards. The host's tools determine what can be checked. No particular MCP, external account or paid service is required for reasoning over supplied materials.

## Local setup

Read this release's `SKILL.md` directly for immediate use. To install a reviewed version in Codex, copy its manifest contents to `.agents/skills/research-methodology/` in the target project. Preserve the skill name even when the source checkout is named `research-asterism` or something else. Open a new conversation in that project to refresh discovery. Other hosts use their configured discovery paths.

In PowerShell, run this from the target project after replacing the source placeholder with this release or another reviewed source directory:

```powershell
$source = 'C:\path\to\research-asterism'
$target = Join-Path (Get-Location) '.agents\skills\research-methodology'
if (Test-Path -LiteralPath $target) { throw 'Target already exists' }
$files = (Get-Content -LiteralPath (Join-Path $source 'release-files.json') -Raw | ConvertFrom-Json).files
foreach ($file in $files) {
    $destination = Join-Path $target $file
    New-Item -ItemType Directory -Force -Path (Split-Path $destination) | Out-Null
    Copy-Item -LiteralPath (Join-Path $source $file) -Destination $destination
}
```

The command refuses an existing destination; it copies only the allowlist, excluding Git internals and unlisted local files. Installing a release is a separate action from reading it. Keep the invocation and installation directory `research-methodology`.

## Verify and preview

Python 3.10+, standard library only:

```console
python scripts/validate.py .
python -m unittest discover -s tests -v
python scripts/package_release.py . --output /absolute/path/research-methodology.zip
python -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/site/`. The original static page has no build dependencies or external resource requests. Check an installed copy with `python scripts/validate.py /absolute/path/.agents/skills/research-methodology --installed`.

Structure and browser checks do not validate scientific truth or novelty. Model evaluation is explicitly dispatched, never launched by these scripts. [The old record](evals/RESULTS.md) is preserved with its limitations; [the scientific revision record](evals/SCIENTIFIC-REVIEW.md) reports the new development regression. Review-informed cases are not a held-out benchmark, and preferences do not establish general effectiveness.

## Contribute and rights

Keep the entrypoint short and branch details in references. Add synthetic failure cases, preserve negative findings and actual run evidence, and avoid expanding every task into a checklist. Do not include private records, copyrighted full texts, credentials or guaranteed-publication claims. The MIT license covers original content in this package only. Referenced authors are not contributors or endorsers; the handbook and upstream skills are not bundled.
