# Research Asterism · 研究星群

把兴趣、论文、想法或实验结果转成有意义、可检验的研究问题与下一步决策。品牌是 Research Asterism，实际 skill 标识和调用保持 `$research-methodology`。

[English](README.md) · [交互展示](site/index.html) · [合成样例](examples/synthetic-examples.md) · [来源与许可](SOURCES.md) · [评估说明](evals/PROTOCOL.md)

[GitHub 仓库](https://github.com/Ash-end/research-asterism) · [在线展示](https://ash-end.github.io/research-asterism/)

## 怎么用

只给一个主题也可以：

```text
使用 $research-methodology。我想让图书馆找书更省力。
请先给一个可操作判断，再帮我收敛成小问题，设计最低成本的区分验证。
```

也可给论文、初步想法、实验观察或已有项目记录，再说明当前要作什么决定。知道的预算、数据边界、目标场景一起提供；无需先填长表。

三种模式可组合使用：

| 模式 | 解决什么问题 |
| --- | --- |
| 领域与方法地图 | 按机制、假设和时间演进理解方法，区分应用需求与性能证据 |
| 想法评估与最小验证 | 比较最近邻，识别真正剩余的贡献，用小验证区分竞争解释 |
| 结果诊断与下一步 | 判断结果是否可比较，解释正负结果或反例，决定继续、调整或停止 |

支持导师提问，也支持共同提出想法。先给判断，再按需给问题卡、两张矩阵、假设、最小实验和决策记录。沿用已有文档，不强制建立另一套记录系统。

## 本机调用

先执行 `git clone https://github.com/Ash-end/research-asterism.git`，或下载 ZIP。克隆目录叫 research-asterism；发布 ZIP 的内部目录仍叫 research-methodology。

Codex 项目级安装目标为 `.agents/skills/research-methodology/`。下面的模板复制发布清单中的全部文件（含 references 和 agents），排除 .git 和清单外材料；请在目标项目目录执行，并替换源码路径。**仓库名与安装目录名不同。**

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

安装后在该项目开新会话，调用 `$research-methodology`。其他宿主应使用其实际配置的发现路径。

不安装也可立即使用：“读取这个目录的 `SKILL.md`，按其中要求分析我的研究决策。”展示站安装区有 Windows 命令模板；替换源目录，目标已存在时停止，避免覆盖版本。

发布包不含本机发现联接，也无需替换用户现有总技能集。

## 验证与展示站

Python 3.10 以上，仅使用标准库：

```console
python scripts/validate.py .
python -m unittest discover -s tests -v
python scripts/package_release.py . --output /absolute/path/research-methodology.zip
python -m http.server 8000 --bind 127.0.0.1
```

浏览器打开 `http://127.0.0.1:8000/site/`。若本机只有 `py` 或指定解释器路径，请替换 `python`。网站无构建依赖、无外部网络请求，带三模式交互样例、安装及文档入口、响应式布局、键盘导航和减少动效适配。

结构检查不证明科研新颖性或结论正确。行为评估需明确运行独立代理，脚本不会自动调用模型、训练或付费服务。实际结果与未测事项见 [评估记录](evals/RESULTS.md)。

## 使用边界与贡献

源码校验允许 GitHub 解压目录名 `research-asterism-main` 或自定义克隆目录名。安装完整目录后，执行 `python scripts/validate.py /absolute/path/.agents/skills/research-methodology --installed`，会额外检查安装目录名与技能名一致。

能验证到什么程度取决于当次可用检索、阅读和实验工具。没有检索时仍可分析已有材料，但会明确新颖性与证据覆盖未核实。引用存在不等于支撑结论，未检索到不等于新颖，模块组合不等于贡献。不承诺顶会，不因安装或调用 skill 自动启动旧实验、上传数据或调用付费服务。

贡献时优先用合成案例证明行为改善，保持主入口精简。MIT 仅覆盖本包原创内容；手册原件、逐字全文、上游技能及用户项目历史不在发布包内。
