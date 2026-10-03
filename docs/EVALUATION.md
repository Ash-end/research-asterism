# Evaluation and limits

[Protocol](../evals/PROTOCOL.md) · [Historical scientific run](../evals/SCIENTIFIC-RUN.md) · [v0.4 checks](../evals/FIRST-PRINCIPLES-REVIEW.md)

## What is actually tested

| Layer | Evidence | What it cannot establish |
| --- | --- | --- |
| Offline structure and regression | Manifest boundaries, broken links, malformed inputs, install refusal and integrity | Research correctness or host model behavior |
| Browser checks | Navigation, keyboard tabs, clipboard fallback, layout, local resources and content separation | Validity of a scientific conclusion |
| Historical v0.3.0 behavior run | Six development cases, actual with/without answers, two masked comparators | Held-out or cross-domain effectiveness |
| v0.4.0 first-principles review | Recorded author-run synthetic responses and manual semantic review | Independent blind evidence or a measured improvement over v0.3.0 |

## Historical comparisons, not a new-version score

The six v0.3.0 development cases cover predictive shift, causal identification, measurement and negative findings, theory counterexamples, qualitative interpretation, and separate requirement/performance displays. They were informed by development and review, so are not held-out cases. Each with/without answer used a fresh context and the same 1,400-Unicode-character ceiling.

| Comparator order | Skill preferred | Baseline preferred | Tie |
| --- | ---: | ---: | ---: |
| Seeded balanced forward | 4 | 0 | 2 |
| Positions reversed | 3 | 1 | 2 |

The two comparators disagreed on r02 and r05. Aggregate answer lengths were 6,142 with the skill and 5,870 without (+4.6%); equality of the ceiling did not make lengths identical. These results are narrow qualitative regression evidence, not proof that the skill improves research or warrants a publication claim.

The original older comparison is also retained, with its fixed ordering, length and context confounds. No failed result or baseline win was removed. The raw masks, responses and run metadata are inspectable in [evaluation results](../evals/SCIENTIFIC-REVIEW.md).

## Version integrity

v0.4.0 adds a first-principles reference and an entrypoint route to it. The old six references, scientific inputs, answers, masks and judgments remain byte-identical. The original v0.3.0 entrypoint is kept as an [evaluation snapshot](../evals/snapshots/v0.3.0/SKILL.md); its recorded source fingerprint refers to that historical version, not today's entrypoint. There is no new with/without benchmark for v0.4.0.

## How to improve this evidence

Use fresh cases before editing against them; freeze source, host configuration, tool access and output constraints; compare old/new versions under matched conditions; mask identities and balance order; preserve raw results and disagreements. Retrieval access and cost authorization must be explicit. Judge semantic reasoning, not keyword counts. Human domain review and broader task sampling are still needed.
