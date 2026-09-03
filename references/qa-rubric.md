# BGI Edu QA Rubric v0.1.0

## 1. 十维评分

| # | 维度 | 权重 | 满分证据特征 |
|---|---|---:|---|
| 1 | 任务价值 | 8 | 有真实使用者、高频任务、明确节省或风险收益 |
| 2 | 输入契约 | 7 | 输入结构、必填/选填、缺失与冲突处理清晰 |
| 3 | 工作流 | 12 | 步骤、检查点、工具、暂停点、输出契约清晰 |
| 4 | 领域与科学准确性 | 15 | 关键事实可追溯、科学边界明确、无过度外推 |
| 5 | 教育与表达质量 | 10 | 目标受众、学习目标、认知负荷与表达适配 |
| 6 | 品牌与合规 | 10 | 机构口径、承诺、公开边界、审核责任明确 |
| 7 | 失败处理与 Stop Gates | 10 | 缺材料、失败、冲突、高风险时有明确动作 |
| 8 | 可复现与资源整合 | 10 | 同事可复跑、资源版本明确、依赖可获得 |
| 9 | Regression 与证据 | 13 | 有 baseline、真实 case、回归、Before/After |
| 10 | 交付可用性 | 5 | 输出可直接进入下一业务步骤 |

## 2. 分数解释

每个维度按该维权重独立评分：

- 90%–100%：成熟，有真实证据；
- 70%–89%：可用但有清晰缺口；
- 50%–69%：依赖人工兜底；
- 1%–49%：关键结构缺失；
- 0：完全缺失或存在反向证据。

## 3. Evidence Confidence

### High
主要结论由真实运行、真实历史数据、人工认可 Golden Cases 或可复现测试支撑。

### Medium
仓库证据较完整，有测试但真实业务数据有限。

### Low
主要依赖 dry run / inferred，不能用于生产就绪宣称。

## 4. 状态门槛

### EXPERIMENTAL
- <70；或
- 有 BLOCK Gate；或
- 无可冻结 baseline；或
- 无 regression。

### INTERNAL CANDIDATE
- ≥70；
- 无 BLOCK；
- 有 baseline；
- ≥3 regression cases；
- P0/P1 已明确。

### READY FOR INTERNAL USE
- ≥80；
- G0–G3 无 BLOCK；
- critical regression 全通过；
- ≥3 regression cases；
- ≥1 人工确认 Golden Case；
- 关键输出存在 tested / observed_real 证据；
- Known Limitations 已记录。

### READY FOR EXTERNAL RELEASE
- ≥88；
- 已满足 READY FOR INTERNAL USE；
- Golden Cases 全通过；
- 对外品牌/合规人工审核完成；
- 安装/使用说明可复现；
- CHANGELOG / Release Notes 完整；
- G4 获明确授权。

## 5. Critical Override

以下情况无论总分多少都不得 READY：

- 科学事实重大错误；
- 医疗/健康越界造成明显误导；
- 未成年人安全风险；
- 密钥或个人信息泄露；
- 未授权代表机构对外发布；
- 新版本出现 critical regression。
