# Architecture and maintenance

[Entrypoint](../SKILL.md) · [Contributing](../CONTRIBUTING.md) · [Sources](../SOURCES.md)

The host discovers `research-methodology` from metadata. It reads the short entrypoint, selects a current decision mode, and loads relevant references. Capabilities are detected from the actual session: retrieval, reading, analysis and execution remain optional. A missing tool creates an explicit evidence boundary, not a fabricated completed operation.

```text
research-methodology/
  SKILL.md                 routing and shared reasoning
  agents/openai.yaml       Codex display metadata
  references/              seven resources loaded by need
  docs/                    human-facing guide and maintenance notes
  examples/                synthetic input/output examples
  evals/                   raw fixtures, historical runs and limits
  scripts/                 offline validation, bounded install, packaging
  tests/                   structural and browser regressions
  assets/                  original diagrams and repository banner
  site/                    static Pages showcase and deep documentation
```

The first-principles reference supplements the three modes; it does not introduce a fourth compulsory pipeline. Claim design chooses the evidence obligation. Evidence-tools distinguishes source support from retrieval success. Output-forms offers optional records without duplicating a project's established system.

`release-files.json` is the only publication allowlist; `runtime_files` is its installation subset. Packaging uses a stable `research-methodology/` prefix and refuses to overwrite an existing ZIP. The installer refuses an existing target and does not pull dependencies or make remote calls. `.gitattributes` preserves source bytes because historical evaluation fingerprints include their original line endings.

The website uses local assets, system fonts and a small script for accessible tabs and copy controls. It contains no analytics, remote font, model endpoint or embedded private file. Tables report missing measurements explicitly. Scientific validity is assessed through claim support and human review, separately from these technical checks.

The public repository is a dedicated export of this skill. Parent collections, machine paths, recovery material, private source identifiers and domain-specific project histories are excluded. MIT covers only original, authorized repository material.
