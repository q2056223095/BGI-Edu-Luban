# BGI Edu Luban v0.1.0

> 华生 · AI 工作流质检工坊
>
> 把“AI 能跑的工作流”，打磨成“华大教育中心敢用、能复用、可验收、可迭代”的标准化 AI 资产。

**当前状态：Internal Prototype / 内部原型。** 本仓库是面向深圳市华大教育中心场景设计的首版质量治理框架，不代表已完成组织层面的正式制度审批。

## 它解决什么问题

当内部 Skill / Agent 越来越多，真正的难题会从“怎么写提示词”变成：

- 谁判断一个 Skill 是否真的值得保留？
- 新版本到底比旧版本好在哪里？
- 科学内容有没有因为追求传播而失真？
- 同事换一个输入后还能不能稳定复现？
- 出现隐私、未成年人、健康、品牌或外发风险时会不会自动停？
- 什么时候可以进入内部使用？什么时候可以对外发布？

BGI Edu Luban 用 **Risk Gates + 十维评分 + Baseline + Regression + Golden Cases + 独立验收 + Release Discipline** 回答这些问题。

## v0.1.0 的边界

首版只做“质检与发版治理”，不承担从零创建 Skill。

适合：

- 科学热点 / 科普内容 Skill；
- 课程开发 Agent；
- 课程上架、详情页、GEO 数据工作流；
- 公众号 / 招生 / 产品资料工作流；
- 视觉和排版 Skill；
- 内部脚本型 Agent。

不适合：

- 单次普通问答；
- 一段文案润色；
- 普通代码 Review；
- 无任何可验证标准的“纯灵感型”任务。

## 快速开始

把 `SKILL.md` 加载到支持 Skill / Project Instructions / Agent Instructions 的运行环境，然后说：

```text
用 BGI Edu Luban 检查这个 Skill：<路径 / GitHub 仓库 / SKILL.md>
```

常用触发语：

```text
给这个 Agent 做一次 BGI Edu QA
冻结 0.4.0 和 0.5.1，跑 Before/After
给这个 Skill 建第一批 regression cases
跑 Regression Round 2
这个 Skill 能不能进入内部使用？
准备发版，给我 QA Card 和 Release Readiness
```

## 核心流程

```text
立项
 ↓
资产盘点
 ↓
Baseline 冻结
 ↓
Risk Gates
 ↓
BGI Edu 十维评分
 ↓
P0 / P1 / P2
 ↓
有边界改动
 ↓
Regression + Golden + Adversarial
 ↓
独立验收
 ↓
Internal / External Release Readiness
 ↓
回炉
```

## BGI Edu 十维质量模型

| 维度 | 权重 |
|---|---:|
| 任务价值 | 8 |
| 输入契约 | 7 |
| 工作流 | 12 |
| 领域与科学准确性 | 15 |
| 教育与表达质量 | 10 |
| 品牌与合规 | 10 |
| 失败处理与 Stop Gates | 10 |
| 可复现与资源整合 | 10 |
| Regression 与证据 | 13 |
| 交付可用性 | 5 |
| **合计** | **100** |

评分不是唯一门槛。科学、教育/未成年人、隐私、安全、品牌和外部发布等 Gate 可以直接阻断上线。

## 状态

- `EXPERIMENTAL`
- `INTERNAL CANDIDATE`
- `READY FOR INTERNAL USE`
- `READY FOR EXTERNAL RELEASE`

详见 `references/qa-rubric.md`。

## 文件结构

```text
BGI-Edu-Luban-v0.1.0/
├── SKILL.md
├── README.md
├── VERSION
├── CHANGELOG.md
├── LICENSE
├── THIRD_PARTY_NOTICE.md
├── references/
│   ├── qa-rubric.md
│   ├── stop-gates.md
│   ├── release-policy.md
│   └── asset-standard.md
├── templates/
│   ├── regression-case.md
│   ├── golden-case.md
│   ├── qa-report.md
│   ├── qa-card.md
│   └── release-notes.md
├── examples/
│   └── bgi-science-hotspots-pilot.md
├── tests/
│   ├── regression/README.md
│   ├── golden/README.md
│   └── adversarial/README.md
└── tools/
    └── check_bgi_skill.py
```

## 首个推荐试点

`BGI_science_hotspots_skill`。

建议把已有历史版本、Regression Round 1 / Round 2 和人工认可的科学热点案例导入本框架，生成第一张真实的 BGI Edu QA Card。

## 设计来源

本项目的方法论受到 LearnPrompt 的 `luban-skill` 启发，尤其借鉴了“先判断价值、外部对标、冻结基线、验证门、真实回测、独立验收与发版纪律”的思想；BGI Edu 版本重新面向教育中心内部 AI 资产治理，增加科学准确性、教育/未成年人、品牌合规、Golden Cases 和内部/外部发布状态模型。

详见 `THIRD_PARTY_NOTICE.md`。
