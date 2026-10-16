# 明察 Pro Max（Ming Cha Pro Max）

> **明察秋毫，Max 级主动。**
> 主动式深度研究中枢：主动预判 + 单 Agent 轻量研究 + 多 Agent 并行深挖，三合一一条流水线。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)]()

## 这是什么

「明察 Pro Max」是一套 **AI Agent 技能（Skill）**，把三个能力熔成一个入口：

```
        ┌─ 主动预判（Proactive Agent）
        │   交付完顺手想到下一步，不等人开口
        │
你说一句 → ┼─ 轻量档（明察Pro 单 Agent 8 阶段）
        │   15-20 轮搜索出结构化报告
        │
        └─ 重量档（多 Agent 并行引擎）
            拆 shard 并行取证 + Red Team 攻击
            双产物：Markdown 报告 + 交互 HTML 网页
```

**与普通搜索的区别**：普通搜索给十条链接；明察 Pro Max 给一份结论固化、来源可溯、矛盾明示、还主动替你想好下一步的报告。

## 三个技能融合来源

| 原技能 | 贡献什么 |
|---|---|
| Proactive Agent | 行为内核：任务交付后主动预判下一步，不连环追问 |
| 明察Pro（Ming Cha Pro） | 轻量档引擎：单 Agent 8 阶段深度研究流水线 |
| Mingcha Multi Agent Deep Research | 重量档引擎：多 Agent 并行 + 多专家视角 + Red Team |

## 核心能力

- **智能选档**：按用户语气自动分流——快速/概览走基础档，研究/查一下走标准档，深度/尽调走重量档
- **8 阶段研究流水线**：问题解构 → 搜索策略 → 原子搜索 → 信源分级 → 交叉验证 → 迭代反思 → 结论输出 → 报告生成
- **多 Agent 并行（重量档）**：OrganizerAgent 拆 2-4 个 shard，每个 Subagent 端到端负责，真正并行
- **多专家视角 + Red Team**：4-6 个专家视角并行，反方主动攻击结论，列证伪信号
- **置信度标注**：每条结论标高（>90%）/ 中（70-90%）/ 低（<70%）
- **矛盾清单**：多来源打架必须进清单，不抹平
- **单文件交互式 HTML 报告**：SVG/ECharts 图表、时间线、置信度徽章、矛盾表格；深浅色自适应、多端响应式
- **主动预判**：交付后主动问"要不要导 PDF / 做图表 / 导 Excel / 出 PPT 大纲"，选最可能的直接做

## 适用场景

行业研究、企业尽调、竞品分析、技术调研、学术综述、舆情分析、市场调研、政策解读、产品分析、投资研究、事件复盘、人物背景调查……凡是需要"把一件事查清楚还顺便把后续收拾了"的场景，都是它的主场。

## 仓库结构

```
mingcha-pro-max/
├── SKILL.md                       # 技能主文件（触发条件 + 决策路由 + 工作流 + 红线）
├── README.md                      # 本文件
├── LICENSE                        # MIT
├── .gitignore
├── references/                    # 参考手册
│   ├── search-playbook.md          # 轻量档：搜索战术
│   ├── methodology.md              # 轻量档：方法论
│   ├── detailed-playbook.md        # 轻量档：执行颗粒度
│   ├── report-standards.md         # 轻量档：报告规范
│   ├── case-walkthrough.md        # 轻量档：小米尽调实例
│   ├── research-orchestration.md   # 重量档：问题树与编排
│   ├── expert-playbooks.md        # 重量档：专家角色表
│   ├── evidence-and-citation.md   # 重量档：证据分级
│   └── html-report-standard.md     # 重量档：HTML 研报规范
├── assets/
│   └── report-template.html        # 交互式 HTML 报告骨架
└── scripts/
    └── assemble_report.py          # 拼接 parts/ 为 report.md
```

## 安装

把整个文件夹放到你的 AI Agent 的 skills 目录下即可。常见路径：

- Claude Code: `~/.claude/skills/`
- Cursor: `~/.cursor/skills/`
- 豆包/其他 Agent: 对应 skills 目录

## License

MIT
