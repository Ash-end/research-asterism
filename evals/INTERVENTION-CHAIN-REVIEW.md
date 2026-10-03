# v0.4.1 intervention-chain precision review

A review identified an overly broad statement that could treat every absent mechanism response as an invalid test. The patch distinguishes undelivered treatment from a delivered intervention whose predicted mediator does not change, and from changed mediator with absent outcome response. Operational checks must be independent and predefined; outcome success is not their definition.

[Raw synthetic case](intervention-chain-case.json) · [Actual author response](results/intervention-chain-author-run.json)

The author read the revised guidance and answered the three-branch case on 2026-10-03, then manually reviewed the reasoning. A remains an unperformed intervention test; B can challenge the intervention-to-mechanism prediction under valid measurement and adequate precision; C can challenge the specified outcome prediction while preserving causal-identification limits. No real experiment was run.

This is targeted development regression, with the author serving as respondent and reviewer. It is not independent blind evidence or a new effectiveness score. The four v0.4.0 author responses and all v0.3.0 independent comparison artifacts remain unchanged. See [evaluation limits](../docs/EVALUATION.md).

The recorded source SHA refers to the [v0.4.1 runtime snapshot](snapshots/v0.4.1/SKILL.md), retained before v0.5.0 rewriting.
