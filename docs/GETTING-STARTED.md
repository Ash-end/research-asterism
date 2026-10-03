# Getting started / 开始使用

[English overview](../README.md) · [中文说明](../README.zh-CN.md) · [Workflows](WORKFLOWS.md)

Requires a host that can read an Agent Skill, and Python 3.10+ for the optional offline installer. No MCP, API key, model download or paid service is required by the package. Actual retrieval or analysis depends on the tools and permission available in your session. Host integration beyond the local Codex project discovery path is not end-to-end certified here.

## Install into a Codex project

Clone the source outside the target skill directory:

```sh
git clone https://github.com/Ash-end/research-asterism.git
```

From the target project, pass the source script's actual path. PowerShell example:

```powershell
python 'C:\path\to\research-asterism\scripts\install_skill.py' --target '.agents\skills\research-methodology'
python 'C:\path\to\research-asterism\scripts\install_skill.py' --target '.agents\skills\research-methodology' --check
```

POSIX example:

```sh
python /path/to/research-asterism/scripts/install_skill.py --target .agents/skills/research-methodology
python /path/to/research-asterism/scripts/install_skill.py --target .agents/skills/research-methodology --check
```

The installer copies only the ten runtime files: entrypoint, seven references, host metadata and license. It validates the complete source first, refuses an existing target, and never overwrites a prior installation or project notes. `--check` compares installed bytes with the selected source without writing. For updates, review the release and use your host's normal reviewed replacement procedure; automatic in-place upgrades are intentionally not provided.

在目标项目重新开启会话，让宿主刷新技能发现。若列表中仍未出现，可明确要求助手读取源码或安装目录的 `SKILL.md`；这能使用指令，但不等于验证宿主的自动发现。

## A useful first request

```text
Use $research-methodology.
My topic is probability calibration under distribution shift.
Help me frame a useful research question and decide what to read or test next.
I have not supplied papers or data. Do not run experiments.
```

```text
使用 $research-methodology。
主题：分布变化下的概率校准。请先界定问题和方法假设，
给出下一项有判断价值的核查。现在没有论文或数据，暂不实验。
```

A topic alone is enough. For existing work, add the current decision, relevant materials, known constraints and any earlier results that matter. Provide private data only through an authorized channel; the skill does not upload it automatically.

## What the answer should make clear

The current judgment, its scope and basis; source reports versus inferences versus untested hypotheses; a next action that could change the decision; and material uncertainty. Optional matrices and question cards are selected to serve the decision, not required paperwork.

## Verify the source package

```sh
python scripts/validate.py .
python -m unittest discover -s tests -v
```

These offline checks validate packaging and failure handling. They do not assess novelty, truth or research quality. The complete source contains evaluation history and website assets; a minimal installed runtime does not, so use installer `--check` for it.
