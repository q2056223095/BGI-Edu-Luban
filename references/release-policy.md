# Release Policy v0.1.0

## 1. 版本策略

采用 Semantic Versioning。

### PATCH
- 修正错误规则；
- 增加失败处理；
- 改善描述而不改变核心契约；
- 修复 regression。

### MINOR
- 新增兼容能力；
- 新增评估模块；
- 新增输出类型；
- 新增测试和自动化，不破坏旧契约。

### MAJOR
- 核心定位变化；
- 输入/输出 schema 不兼容；
- 工作流主干变化；
- 风险责任边界变化。

## 2. Release 必备证据

- baseline ref；
- regression summary；
- critical case 结果；
- Golden Case 结果；
- Risk Gates；
- Before/After；
- Known Limitations；
- Release Notes。

## 3. 发布授权

QA 通过 ≠ 自动发布。

任何 merge / tag / release / deploy 都必须单独获得用户明确授权。
