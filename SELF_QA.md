# BGI Edu Luban v0.1.0 — Self QA Snapshot

Date: 2026-09-03

## Scope

本次只完成**静态仓库检查**，没有把 v0.1.0 自己宣称为已经通过真实模型回归的生产版本。

## Static repository check

- Required files: PASS
- Recommended structure: PASS
- Frontmatter: PASS
- Regression case definitions: 3 present
- Adversarial case definitions: 1 present
- Obvious secret-pattern scan: PASS
- Human-approved Golden Cases: **0 — WARN**

## Current status

`INTERNAL PROTOTYPE / EXPERIMENTAL`

原因：

1. 还没有人工确认的 BGI Edu Luban Golden Case；
2. 3 个 Regression Case 目前只是测试规格，尚未在多个 runtime / 模型上完成正式执行；
3. 十维阈值还没有经过真实 BGI Skill 试点校准。

## Promotion path

建议用 `BGI_science_hotspots_skill` 完成首个真实试点后：

1. 运行 R-001 ~ R-003；
2. 形成第一份真实 QA Report；
3. 人工确认至少一个 Golden QA Output；
4. 根据试点结果校准 80 / 88 分阈值；
5. 再考虑 v0.1.1 或 v0.2.0。
