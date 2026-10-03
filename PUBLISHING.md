# Publication scope and maintenance

Research Asterism is published in [Ash-end/research-asterism](https://github.com/Ash-end/research-asterism). The live showcase is [GitHub Pages](https://ash-end.github.io/research-asterism/). Its stable skill identifier and install directory are research-methodology.

Publish only this package's explicit [release manifest](release-files.json). A dedicated repository uses the package contents at its root; the ZIP retains a research-methodology/ prefix for installation compatibility. Never commit the enclosing skills collection or machine-specific discovery junction.

Included: original skill, progressive references, UI metadata, bilingual guides, synthetic examples and raw evaluation cases, deterministic scripts/tests, recorded synthetic evaluation output, source/license notes, and the original static showcase. The `.nojekyll` marker preserves the plain static files on branch-based GitHub Pages.

Excluded by construction: source handbook PDF/transcription/figures, user research, project histories, recovery materials, installed collections, credentials, Git internals, evaluation scratch files, browser profiles, and QA screenshots. The allowlist is reviewed scope, not an automatic secrets/copyright detector. MIT covers original package content only; source authors are not collaborators or endorsers by virtue of attribution.

## Build and verify

Run `python scripts/validate.py .` and `python -m unittest discover -s tests -v`, then build with `python scripts/package_release.py . --output /absolute/path/research-asterism.zip`. The builder rejects unsafe paths, symbolic links, an output inside the source, and overwriting an existing ZIP. Inspect entry names, CRC, and the SHA-256 manifest.

Source directory names may be research-asterism, research-asterism-main, or a custom checkout. Installed content must be placed in research-methodology; use `--installed` to check that directory name. Keep SKILL.md's name and agent invocation stable unless a separately reviewed compatibility change is intended.

CI validates the dedicated repository root with read-only contents permission and checkout credentials not persisted. Check the CI result for the exact pushed commit. Reasoning changes warrant a new real behavior evaluation; branding changes do not warrant invented or silently relabelled results. Preserve original evidence and limits.

## GitHub Pages

The approved public repository serves the complete main-branch root using GitHub Pages. The relative root redirect reaches site/ and all ../ documentation links stay within the project subpath. No build dependency, remote asset, private server, new paid service, or custom domain is required. Do not deploy site/ alone with its relative documentation links unchanged.

After a change, verify the exact remote commit, that commit's CI result, Pages build, the HTTPS root redirect, responsive layouts, copy commands, and linked documentation. Repository existence, a requested build, or a queued workflow alone does not establish successful deployment. Modify only this repository's Pages configuration.
