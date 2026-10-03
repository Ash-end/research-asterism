# Research Asterism

Research Asterism (研究星群) is a portable research judgment skill, invoked as `$research-methodology`: turn a topic, paper, idea, or result into a testable question and a useful next decision.

[简体中文](README.zh-CN.md) · [Interactive showcase](site/index.html) · [Examples](examples/synthetic-examples.md) · [Sources and licensing](SOURCES.md) · [Evaluation](evals/PROTOCOL.md)

[GitHub repository](https://github.com/Ash-end/research-asterism) · [Live showcase](https://ash-end.github.io/research-asterism/)

## Use

Ask a compatible agent to read this folder's `SKILL.md`, or install this folder in the host's skill search path and invoke:

```text
Use $research-methodology. I want to make finding library books easier.
Help me identify a meaningful question and the cheapest informative check.
```

Input can be a topic alone, supplied papers, an idea, experimental observations, or existing project records. Include the decision and constraints when known; a long project dossier is unnecessary.

- **Field and method map:** organize mechanisms and their evolution; separate needs from performance.
- **Idea assessment and minimal test:** assess the closest prior work, residual contribution, and discriminating predictions.
- **Result diagnosis:** inspect comparison validity, rival explanations, counterexamples, and continue/adjust/stop conditions.

Mentoring and joint ideation work across all modes. Outputs adapt to the decision; forms and persistent records are optional. The host's available retrieval, reading, and execution tools determine what can be verified. No MCP, external account, or paid service is required for reasoning over supplied materials.

## Local setup

Clone this repository with `git clone https://github.com/Ash-end/research-asterism.git`, or download its ZIP. The clone is named research-asterism; a packaged release preserves its research-methodology folder prefix.

In Codex, the installation path is `.agents/skills/research-methodology/`. Copy the complete release-manifest contents into that path in your target project, preserving references and UI metadata and excluding Git internals. **The repository brand does not rename the skill or installation directory.** Restart/open a new conversation in that project to refresh discovery, then invoke `$research-methodology`. Follow your host's configured search paths for other agents.

For immediate use without installing: “Read `/absolute/path/research-asterism/SKILL.md` and apply it to this research decision.” The showcase's installation tab offers a Windows command template. Replace its source path and refuse an existing destination instead of overwriting a different version.

In PowerShell, run this from your target project and replace the source placeholder with the actual cloned repository path:

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

The manifest copies the released files and excludes .git and unlisted local material. The ZIP does not include a machine-specific discovery junction. Existing user-level skill collections do not need to be replaced.

## Verify and preview

Python 3.10+; standard library only:

```console
python scripts/validate.py .
python -m unittest discover -s tests -v
python scripts/package_release.py . --output /absolute/path/research-methodology.zip
python -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/site/` for the website and adjacent source documentation. Replace `python` with your working Python 3 command where needed. The site is plain HTML/CSS/JavaScript, works without a build, and makes no external requests.

Validation checks structure and release boundaries, not novelty or scientific truth. Behavioral evaluation is an explicit independent-agent exercise; it is not launched by the scripts. Read [the protocol](evals/PROTOCOL.md) and [the recorded result](evals/RESULTS.md) for actual execution and limits.

Source validation accepts checkout names such as `research-asterism-main`. After copying the whole folder to its installation path, run `python scripts/validate.py /absolute/path/.agents/skills/research-methodology --installed` to also verify that the installation directory matches the skill name.

## Contribute

Keep the entrypoint short and mode-specific detail in references. Prefer observable decision improvements over longer checklists. Add synthetic cases for failures, preserve negative observations, and report real evaluation runs honestly. Do not add private research records, copyrighted full texts, credentials, or claims of guaranteed publication.

The MIT license applies to this package's original content. Referenced works retain their own rights; the source handbook and upstream skills are not bundled.
