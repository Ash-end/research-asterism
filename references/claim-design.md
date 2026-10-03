# Match evidence to the claim

Fit these obligations to the current learning or construction node; a short local derivation does not require every branch below. For a concrete candidate, connect the intended claim to its procedure or relation and the smallest distinguishing check. A classic method can satisfy the actual need even when a novel contribution remains absent. See [learning path](learning-path.md).


Use the relevant branch when designing a study or assessing what a result establishes. This is a decision aid, not a universal taxonomy or a checklist to print on every task. A study can support one kind of claim without supporting another.

## Choose the claim and target

State the object, domain/population, conditions or time, target quantity or interpretation, and comparison. Separate the research question from a favored answer. Turn a hypothesis into a prediction or logical consequence that differs from a credible alternative. If the alternatives cannot be separated by the proposed observation, redesign the question or test.

| Claim | What needs definition | Evidence that addresses it | Common mismatch |
| --- | --- | --- | --- |
| Descriptive | Attribute, pattern, population and measurement | Sampling/coverage and an estimate or traceable interpretation of that pattern | A selected sample described as a population; association described as cause |
| Predictive | Outcome, decision time, available inputs, target population and use loss | Evaluation on units/times/settings matching the intended generalization, with model selection separated from assessment | Random rows reused across people/sites/time; later information treated as available at use |
| Causal | Interventions or exposures being contrasted, outcome, horizon, target population and effect | A design and assumptions that identify the contrast; appropriate randomized or observational controls | Adjusting a convenient regression treated as identification; treatment selection or a co-occurring change ignored |
| Measurement | Measurand or construct, observation model, reference and conditions | Calibration/validation, bias and uncertainty relevant to the claimed property | Repeatable proxy readings treated as valid measurement of a different construct |
| Theoretical | Domain, quantifiers, premises and exact conclusion | A valid dependency chain or an in-domain counterexample | Pointwise information used for uniform claims; limits or operators exchanged without justification |

For qualitative work, define what accounts, practices, or processes are being interpreted and why the cases can illuminate them. Trace claims to material, examine rival interpretations and discrepant cases, and account for researcher position and selection. Theme recurrence is not population prevalence or causal identification by itself. For engineering work, distinguish demonstrated artifact capability under constraints from a general scientific or mechanism claim.

## Empirical units, controls and validation

An assignment unit, a biological/physical sampling unit, and a repeated instrument reading may differ. Identify what supplies independent information for the intended inference. Replicate readings do not create new specimens, batches, participants or sites. Use blocking, pairing, aggregation or a dependence-aware model/resampling scheme when justified; do not automatically resample rows. Report which population or variation the uncertainty represents.

A dependence-aware analysis cannot manufacture missing independent replication or separate a treatment perfectly confounded with a batch/instrument session. In that situation, a different design may be needed rather than a more elaborate statistical model.

Choose a comparator addressing the question: a credible existing method with matched access/resources for performance; a reference/blank/alternative measurement for validity; or an intervention contrast for causation. A matched protocol specifies the target outcome, conditions, information timing, selection/tuning, units, and relevant resources. A negative control or ablation helps only if its predicted behavior separates the explanations.

Distinguish performance at a fixed resource budget from resources needed to attain a specified outcome; these require different comparisons. Account for failures, timeouts and excluded runs rather than reporting cost or capability only among successes. Low fitting error need not identify model parameters: examine whether distinct parameter values generate the same observable behavior before comparing optimizers.

For prediction, split according to the deployment claim: new people, new sites, future time, or a combination. Learn transforms and tune choices within permitted development data; keep assessment data out of those choices. Specify any authorized unlabeled target adaptation separately. Grouped or temporal validation does not itself establish validity under arbitrary distribution shift. For reweighting, for example, overlap and a suitable relation between source and target outcome mechanisms require scrutiny.

For causal questions, specify the counterfactual contrast before choosing an adjustment set. Consider treatment selection, time alignment, confounding, missingness and interference where relevant. Observational identification commonly needs well-defined interventions, consistency, exchangeability and positivity; these are assumptions, not conclusions of a significance test. Avoid automatic adjustment for descendants of treatment or selection variables. Randomization also requires attention to assignment level, attrition and outcome measurement.

## Precision, negative results and scope

When quantitative evidence is available, report the effect or error in meaningful units with an uncertainty assessment matched to the design. Distinguish measurement uncertainty, sampling variability, model assumptions and coverage of new settings. An interval cannot repair confounding, leakage or an invalid measurement model.

Failure to detect a difference may reflect a small effect, poor precision, insensitive measurement or an invalid protocol. Equivalence needs a scientifically justified margin and a procedure capable of assessing it; derive the margin from the research/application decision, not merely instrument repeatability or the observed data. A conclusion remains bounded to the population, outcome and conditions assessed. Do not request endless replication if a cheaper design or source check resolves the uncertainty.

For theory, uncertainty can be an unproved obligation or unexamined condition, not a sampling error. Distinguish a proof failure from a false proposition. Derive an in-domain counterexample or identify the missing premise; then assess a restricted statement independently. Qualitative evidence may warrant revising an interpretation through contrasting cases rather than adding a numerical threshold.

Pointwise and uniform statements have different obligations. A theorem's assumptions and conclusion also differ from numerical stability or practical gain in an application. Not finding a counterexample does not prove the claim; an unfinished proof review does not establish falsity.

## Methodological source notes

These original instructions draw on verified primary guidance: [NIST experimental design](https://www.itl.nist.gov/div898/handbook/pri/section3/pri3.htm) and [blocking](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm), [NIST measurement uncertainty](https://www.nist.gov/pml/nist-technical-note-1297), [scikit-learn validation](https://scikit-learn.org/stable/modules/cross_validation.html) and [leakage guidance](https://scikit-learn.org/stable/common_pitfalls.html), [Hernán's account of observational identification](https://hsph.harvard.edu/profile/miguel-hernan/), and the [ASA statement summary](https://www.amstat.org/asa/files/pdfs/P-ValueStatement.pdf). They support the cited areas, not every branch or a universal workflow. Their text, code, figures and full documents are not bundled. Qualitative and theoretical advice here is original reasoning guidance, not a claimed certification by those sources.

[Lazic and colleagues](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2005282) support the distinction between biological, experimental and observational units in biological designs. [Cawley and Talbot](https://jmlr.org/papers/v11/cawley10a.html) support the concern about fitting model selection criteria and biased performance evaluation; the inspected abstract does not certify a specific correction for every selection procedure.
