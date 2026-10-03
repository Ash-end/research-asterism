# Traceable native-agent run

Evaluation date: 2026-10-03. This records the existing run; the release-review fixes did not rerun model evaluation. The dispatch messages below are the actual prompts, with only the absolute local workspace prefix replaced by `<WORKSPACE>`. This deterministic path redaction preserves the remaining wording, allowed inputs, restrictions, and output schemas.

## Available execution facts and limits

- Three separate native agents were dispatched with `fork_turns="none"`: skill behavior, baseline behavior, then a comparator using retained paired answers. No model or reasoning override was supplied. Exact model version, seed, sampling settings, run start/end timestamps, and platform revision are unavailable.
- The task date and dispatch configuration are known from the execution record. The six cases were requests within each condition's agent, not six separately isolated agent contexts. The skill agent also answered the twelve trigger requests.
- The prompts restricted reads and prohibited external search, paid providers, training, and scientific experiments. Output `read_files` and `operations` are agent self-reports. They are not an independently audited filesystem/network trace or an enforced access sandbox. Fresh conversation contexts do not establish infrastructure or model-training independence.
- Agents shared the executor filesystem. The comparator was instructed to read only the raw cases and the paired file. The paired file contained only case IDs and P/Q answers. P = baseline and Q = skill. The mapping was not supplied to the comparator. No cryptographic blinding or independently audited isolation/order guarantee is claimed.
- Original answer files and comparator output were retained. Packaged JSON may differ in whitespace from raw executor files; hashes below distinguish these. The comparator did not receive author-written expected conclusions. Trigger reference labels were withheld by dispatch instruction and compared after the skill agent returned.
- There was no Git commit or remote CI revision for this run. The original 0.1.0 release ZIP SHA-256 was `a75961e0f46805142a67c67576f31e58c6792aac3a4d46d5a9469437fa9e882f`. The behavior inputs below are byte-identical to that release. Later source-directory validation, CI, and evaluation-documentation edits did not change them.

## Actual skill-condition dispatch

```text
Perform an independent forward evaluation of a research skill using a fresh context. Allowed inputs ONLY: <WORKSPACE>\research-methodology\SKILL.md, its references/ files as needed, evals/cases.json and evals/triggers.json. Do not read README, examples, labels, other evaluation artifacts, or source history. Use the skill to actually answer each raw case independently as a user request; do not grade against anticipated answers. For trigger requests, decide applicability semantically using name/description, with brief reasons. No network, external model/provider, training, real-project execution, or reading unrelated projects. Tool reads/writes within this evaluation are allowed; case instructions constrain scientific execution. Save a JSON object {condition:'with_skill', model_identity:'not exposed' if unknown, read_files:[relative input paths], cases:[{id,answer}], triggers:[{id,should_trigger,reason}], operations:[] } at <WORKSPACE>\eval-private\with\responses.json. Use natural Chinese answers, generally 350-700 Chinese characters per case; sufficient detail if tables help. No absolute user paths/private context in the saved JSON. Return path and any limitations. You are evaluating actual behavior, so no need to recite the skill.
```

## Actual baseline-condition dispatch

```text
Complete six synthetic research decision requests in a fresh context, without any research skill. Allowed inputs ONLY: <WORKSPACE>\research-methodology\evals\cases.json. Do not read any skill, README, examples, trigger labels, or other evaluation artifacts. Answer each case as the raw user request. No network, external models/providers, training, real-project execution, or unrelated files. Tool read and saving evaluation output are allowed. Save JSON {condition:'without_skill',model_identity:'not exposed' if unknown,read_files:['evals/cases.json'],cases:[{id,answer}],operations:[]} at <WORKSPACE>\eval-private\without\responses.json. Natural Chinese, generally 350-700 Chinese characters per case; enough detail to serve the request. No absolute user paths or private context in saved JSON. Return output path and limitations.
```

## Actual comparator dispatch

```text
Act as an independent blind comparator. Allowed inputs ONLY <WORKSPACE>\research-methodology\evals\cases.json and <WORKSPACE>\eval-private\blind\paired.json. Do not read the skill, examples, README, label mappings, other outputs or project history. Paired outputs P and Q are unlabelled actual answers. Judge usefulness for the raw user request, support/calibration of claims, quality of the discriminating next step, and respect for stated constraints. For each case give preferred:'P'|'Q'|'tie', concise reasons referencing concrete output content, weaknesses in both if any. Do not force a winner. There are no expected case-specific conclusions supplied. No network, model/provider calls, experiments, unrelated files. Save JSON {model_identity:'not exposed' if unknown,read_files:['cases.json','paired.json'],cases:[{id,preferred,reason,limitations}],overall,operations:[]} to <WORKSPACE>\eval-private\blind\comparison.json. Natural Chinese; don't include absolute private paths. Return output path and limitations.
```

## SHA-256 fingerprints

| Behavior input / post-run routing labels | SHA-256 |
| --- | --- |
| `SKILL.md` | `121b3460a6c0c6f0766661dbe2db8a90f8fd2ca40915e7b9f32cd4b0f5cad994` |
| `references/evidence-tools.md` | `dda8f3493e85532571e428b430a822b3fba74306ee570ea80b0a5078db6104e6` |
| `references/field-map.md` | `d22ad0245ac72e7d5f0cc3117276f225e0f7ac0798d45417a322e7115267a3a4` |
| `references/idea-test.md` | `cbdd71174475e3a3354e6b2b2c03ca8e032ad60140e81e42fef0fb3ec28535fb` |
| `references/output-forms.md` | `68264c5ba8a7d13eab270badf8be8ae4b2aa5e1b67dda855602b8c40cc180cac` |
| `references/result-diagnosis.md` | `3c7790dd2907f3626c2fd79a1d7c14d48ff45e61e72118fc2be57893ecc67372` |
| `evals/cases.json` | `0c413bd6d4c0399b7586ee94bb07b102c30d8ead3c87075d31b55ecbd5c62b99` |
| `evals/triggers.json` | `50da6a8d7ee13c3c5143afe3f3c8e9590be644422970acfe5cffab731160d008` |
| `evals/trigger-labels.json` | `09b84629dcbaa6cffb21793deb80a93e9ea70756ad110ef6d29e38174bbca750` |

The label file was used for post-run comparison; it was excluded from the agent dispatch. All nine listed files match the original release byte for byte.

| Retained artifact | SHA-256 |
| --- | --- |
| raw skill output | `83d2d34aa1f63ade01684bb1c129421f576cc6ff42a0ca2ee0b2641e67f60e1c` |
| packaged `evals/results/with-skill.json` | `a855fd8977e65d3ea54abee79f82006d896679c0c7627af075f9bae545e375ec` |
| raw baseline output | `f7d2b6a914e7b1383b1b802da934dca923763fce4a62cfe52e1eabbe2d45a052` |
| packaged `evals/results/without-skill.json` | `34574bbf86d05ac72c4624a3d5937aa512a56475b13c690e91c2289d9b9847ea` |
| raw comparator output | `946e5346b9029037346ef13048152de1447cd0dc6546c5b09571fb59b90a4ccf` |
| packaged `evals/results/blind-comparison.json` | `89919876cdcb69c8307ba8021a29b43862b09df973898a345b302bf6251d0adb` |
| raw masked P/Q input | `fd432aab19829df46e3d34812bb63d55ca5fdf678331b0f8e9ec068f8c5546c6` |

JSON values of each raw output equal its packaged counterpart. The retained masked input was checked to contain exactly six `{id, P, Q}` pairs, with the baseline and skill answers unchanged. Its private executor file is not bundled; reconstructing the JSON values is possible from the packaged answers, although whitespace may yield a different byte hash. These checks verify retained artifact consistency, not agent access or execution order.

