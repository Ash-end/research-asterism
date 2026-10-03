![Research Asterism: frame questions, examine assumptions, choose an informative test](assets/banner.svg)

[![Validate package](https://github.com/Ash-end/research-asterism/actions/workflows/validate.yml/badge.svg)](https://github.com/Ash-end/research-asterism/actions/workflows/validate.yml) [![MIT](assets/license.svg)](LICENSE) [![Version 0.4.0](assets/version.svg)](https://github.com/Ash-end/research-asterism/releases/tag/v0.4.0)

# Research Asterism · 科研判断技能

把主题、论文、想法、证明或结果，转成**有意义、可检验的研究问题和下一步决策**。输出先给当前判断，再说明依据、范围和哪项证据能够改变它。

[English](README.md) · [网站](https://ash-end.github.io/research-asterism/) · [安装](docs/GETTING-STARTED.md) · [原创指南](docs/HANDBOOK.md) · [评估](docs/EVALUATION.md) · [来源](SOURCES.md)

## 从什么材料开始

| 当前材料 | 要解决的决策 | 可选交付 |
| --- | --- | --- |
| 只有主题，或已有阅读材料 | 该理解什么、接下来读什么？ | 问题卡、方法家族与阅读路线 |
| 想法、机制或贡献主张 | 值不值得做，最先验证什么？ | 假设、最近邻差异、竞争预测与最小验证 |
| 阳性、阴性或矛盾结果 | 结果支持什么，下一步是什么？ | 有效性核查、竞争解释与继续/调整/停止条件 |
| 证明或定性解释 | 哪项条件或解释需要检查？ | 逻辑依赖、反例或材料支持的竞争叙述 |

不要求先凑齐论文、候选或实验。沿用已有项目记录，按决策选择表格和问题卡，不铺设另一套强制文档体系。

## 三分钟开始

```sh
git clone https://github.com/Ash-end/research-asterism.git
```

在目标项目中运行，替换实际源码路径。离线辅助脚本需要 Python 3.10+：

```powershell
python 'C:\path\to\research-asterism\scripts\install_skill.py' --target '.agents\skills\research-methodology'
python 'C:\path\to\research-asterism\scripts\install_skill.py' --target '.agents\skills\research-methodology' --check
```

安装器先校验完整源码，只复制十个运行文件；目标已存在就停止，不覆盖安装或项目笔记，不访问网络或调用模型。重新开启宿主会话刷新发现。其他宿主可以明确读取 `SKILL.md`，但未宣称自动集成已经逐一验证。[详细安装说明](docs/GETTING-STARTED.md)。

```text
使用 $research-methodology。
主题是分布变化下的概率校准，目前没有论文或数据。
请界定问题、比较方法假设，给出下一项有判断价值的核查。
暂不运行实验。
```

## 三种模式，共用一条证据循环

![问题→假设与机制→具体限制→竞争预测→区分验证→判断；阅读检索可循环](assets/workflow.svg)

| 模式 | 实际工作 | 完整合成示例 |
| --- | --- | --- |
| 领域与方法地图 | 比较机制、假设与时间演进；分开需求和实际性能 | [群体变化](site/workflows.html#map) |
| 想法评估与最小验证 | 检查主张、近邻与竞争解释，选择能改变判断的设计 | [不可比报告](site/workflows.html#idea) |
| 结果诊断与下一步 | 核查测量、机制是否生效、精度及正负证据范围 | [不稳定差异](site/workflows.html#result) |

**第一性原理作为按需推理工具：**拆开目标与观测，说明前提和约束的来源；跨领域迁移携带成立条件；产生不同预测；核查测试是否触及机制。它与文献和实验配合，不凭“本质”宣告事实，不强迫所有学科还原成物理或数学公理。[原创方法指南](docs/HANDBOOK.md)。

## 一个简短示例

**合成输入：**“处处可导就能推出导数连续吗？多画几个数值例子可以证明吗？”

**示范判断：**不能。全称命题需要证明，而且这项说法缺少更强前提时是假的。令 `f(0)=0`，非零时 `f(x)=x² sin(1/x)`；零点导数存在且为零，但非零点导数为 `2x sin(1/x) − cos(1/x)`，趋近零时没有极限。下一步应修订定理条件、追踪证明依赖，而不是扩充数值表。

这是分析示例，不是新的实证发现。[更多输入输出](examples/synthetic-examples.md)。

## 可信判断的边界

- 区分来源报告、推断、待验证假说；引用存在不等于支持当前条件下的结论。
- 需求、方法假设、证据状态、实际性能分别呈现；没测量就写无数据，不把不可比结果排成名次。
- 描述、预测、因果、测量、理论与定性工作有不同证据义务；预测提升不识别因果，不显著不等于等效。
- 查最近邻与旧思想；未检索到和模块组合都不证明新颖。
- 检测当次工具能力。没有检索就标注暂定；数据、实验、费用与公开范围遵循本轮授权。

不自动恢复旧研究、训练或公开材料，不承诺论文录用。[主张与设计](references/claim-design.md) · [结构说明](docs/ARCHITECTURE.md)。

## 评估必须可以检查

历史 `v0.3.0` 使用六个开发案例，with/without 逐题新上下文、相同回答上限；匿名比较与位置反转分别有 **4/6、3/6** 偏好技能，反转比较一次偏好基线，两题评判不一致。实际字符总量有技能多 4.6%。这不是留出效果证明，也不能代表跨领域科研能力。

`v0.4.0` 新增假设拆解指引；新的作者运行检查单独记录，**本版本尚无新的独立 with/without 比较**。旧原始回答、掩码、判断和指纹不改写；旧入口保存版本快照。[完整结果与限制](docs/EVALUATION.md)。

```sh
python scripts/validate.py .
python -m unittest discover -s tests -v
```

这些命令检查结构和回归，不判断科学真伪或新颖性。可选浏览器验证需要 Playwright 和可用浏览器，不调用模型 API。

## 文档与参与

[开始使用](docs/GETTING-STARTED.md) · [工作模式](docs/WORKFLOWS.md) · [原创指南](docs/HANDBOOK.md) · [维护结构](docs/ARCHITECTURE.md) · [贡献方式](CONTRIBUTING.md) · [隐私与安全](SECURITY.md) · [版本记录](CHANGELOG.md) · [软件引用](CITATION.cff)

原创指令、代码、文档与图示采用 MIT。指南借鉴彭明輝的研究教学与维护者自建技能的通用思想，以独立结构和原创表达重写；署名不表示原作者参与或背书。旧十四页二次整理稿、原图、大量原文和私人项目记录均不进入发行包。其他技能仓库仅借鉴组织和评估设计，未复制其文本代码，包括非商业许可证材料。详见[来源与许可](SOURCES.md)。
