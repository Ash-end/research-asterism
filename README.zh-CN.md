# Research Asterism · 研究星群

把主题、论文、想法或结果转成有边界的研究问题和下一步判断。实际 skill 标识为 `$research-methodology`。

[English](README.md) · [展示页](site/index.html) · [构造示例](examples/synthetic-examples.md) · [来源与权利](SOURCES.md) · [科学修订记录](evals/SCIENTIFIC-REVIEW.md)

**版本 0.3.0 · 发布日期 2026-10-03。** [GitHub 仓库](https://github.com/Ash-end/research-asterism) · [公开展示页](https://ash-end.github.io/research-asterism/)。科学修订保留真实评估记录、分歧及局限。

## 怎么用

```text
使用 $research-methodology。我想研究预测器迁移到新群体后的概率校准。
请先界定主张和现有证据，再提出能够改变判断的下一步。
```

只有主题也可以。也可提供论文、设计、观察或已有项目笔记；知道当前决策、数据边界与资源约束时一并说明，不必先补齐长材料。

| 模式 | 解决的决策 |
| --- | --- |
| 领域与方法地图 | 比较机制、假设和演进；分开需求、证据状态与实测性能 |
| 想法评估与最小验证 | 比较最近邻和剩余贡献；提出区分解释的验证设计，并核查其能否回答问题 |
| 结果诊断与下一步 | 核查可比性、竞争解释、不确定性和继续／调整／停止条件 |

展示页把重加权、稳定表示和目标域适配标为“策略/机制”：这些策略可以组合，不构成互斥分类。“验证设计”提出待实施的核查，不保证其充分性。

支持导师提问与共同提出想法。先给可操作判断，再按需用问题卡、矩阵、假设或决策记录；复用现有文档。描述、预测、因果、测量、理论主张分别选择适合的证据与设计；定性研究和工程验证保留各自标准，不强制套统计实验。

## 本机调用

可以直接要求：“读取这个发布目录的 SKILL.md，并用于我的研究决策。”正式安装到 Codex 项目时，目标目录为 `.agents/skills/research-methodology/`；源目录可以叫 research-asterism 或其他名称，技能名与安装目录保持一致。在目标项目执行下列模板并替换源路径：

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

已有目标会停止，避免覆盖。仅复制发布清单，排除 `.git` 和未列文件。安装后在目标项目新开会话刷新发现；其他宿主使用其配置的搜索路径。安装与直接读取是不同操作；调用名和安装目录始终为 research-methodology。

## 验证与预览

Python 3.10 以上，只用标准库：

```console
python scripts/validate.py .
python -m unittest discover -s tests -v
python scripts/package_release.py . --output /absolute/path/research-methodology.zip
python -m http.server 8000 --bind 127.0.0.1
```

打开 `http://127.0.0.1:8000/site/`。网页没有构建依赖和外部资源请求。已安装副本可加 `--installed` 检查目录名。

结构校验与浏览器测试不证明科研结论、新颖性或技能效果。脚本不自动调用模型。旧答案及偏好保留在 [旧评估记录](evals/RESULTS.md)，并标明混杂因素；新运行见 [科学修订记录](evals/SCIENTIFIC-REVIEW.md)。审查启发的案例属于开发回归，不能称为严格留出盲测，偏好数量也不是普遍有效性证明。

## 使用边界与贡献

能核实什么取决于当次工具和授权。没有检索时可分析材料，但证据范围与新颖性未核实。引用存在不等于支撑结论，未找到不等于新颖，模块组合不等于贡献。不承诺顶会，不自动跑旧研究、训练、上传数据或付费服务。

保持短入口和按需参考，用合成案例检验失败，保存真实运行及负结果。MIT 只覆盖本包原创内容；手册 PDF、全文、图、私密项目历史均不进入发布候选，署名不表示来源作者参与或背书。
