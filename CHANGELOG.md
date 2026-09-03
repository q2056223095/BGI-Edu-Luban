# Changelog

## 0.1.0 - 2026-09-03

### Why

深圳市华大教育中心正在形成多类 AI Skill / Agent / Workflow，需要从“能用”进入“可验证、可复用、可维护”的资产治理阶段。

### Added

- BGI Edu Luban 核心 `SKILL.md`；
- BGI Edu 十维 100 分质量模型；
- G0–G4 Risk Gates；
- EXPERIMENTAL / INTERNAL CANDIDATE / READY FOR INTERNAL USE / READY FOR EXTERNAL RELEASE 状态模型；
- Baseline Freeze 规范；
- Regression / Golden / Adversarial Case 规范与模板；
- Before/After 与独立验收规则；
- QA Card 与 Release Notes 模板；
- Skill 资产结构检查脚本；
- `BGI_science_hotspots_skill` 首个试点方案。

### Known limitations

- v0.1.0 只定义治理协议和静态仓库检查，不自动调用模型批量跑测试；
- 没有统一的机器可读 eval schema；
- 没有 Registry / Dashboard；
- 没有自动 GitHub Actions 回归流水线；
- QA 阈值属于首版建议值，需要通过真实试点校准。

### Next

优先用 `BGI_science_hotspots_skill` 做首轮真实校准，再决定 v0.2.0 是否加入自动回测 runner 和统一 eval JSON schema。
