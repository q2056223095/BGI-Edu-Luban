# Pilot 01 — BGI Science Hotspots Skill

> 这是 BGI Edu Luban v0.1.0 的首个推荐试点配置，不包含伪造评分或伪造 PASS 结果。

## 1. 目标

验证 BGI Edu Luban 是否能够把 `BGI_science_hotspots_skill` 的版本升级从“感觉变好了”转成“有 baseline、有 regression、有 golden、有 release evidence”的过程。

## 2. 建议冻结对象

```yaml
asset_name: BGI_science_hotspots_skill
asset_type: skill
baseline_version: 0.4.0
candidate_version: 0.5.1
intended_stage: internal_use
```

冻结时应记录真实 tag / commit / snapshot ref；如果拿不到，不得假装完成真实 Before/After。

## 3. 建议首批 Case 池

以下题目可以作为**候选**测试源，是否升级为 Golden Case 必须经过人工确认：

- “癌症真的会‘传染’吗？”
- “8月12日日全食，NASA为什么要开飞机追？”
- “干细胞居然会‘数到8’”
- “两个接近11 Gb的燕麦基因组，找出了52个抗旱候选基因”

## 4. 首轮建议 Regression 维度

### R-A 科学事实与证据边界

检查：

- 论文 / 机构 / 日期 / 数据是否正确；
- 是否把动物 / 细胞 / 单项研究外推成人体确定结论；
- 是否把相关性写成因果；
- 是否明确“已知 / 推测 / 尚不确定”。

### R-B 标题吸引力 vs 失真

检查：

- 标题有钩子；
- 不把科学事实做成伪悬疑；
- 不把“可能”改成“就是”；
- 不以恐慌、医疗焦虑换点击。

### R-C 5张图视觉协议

检查：

- 每张图是否承担不同叙事功能；
- 是否出现与科学事实不一致的示意；
- 是否把插图做成“AI 科幻壁纸”而非科普信息图；
- 是否满足统一视觉规范。

### R-D 科学边界输出

检查：

- 是否主动指出研究边界；
- 是否给出“不能据此得出什么结论”；
- 健康相关内容是否避免诊断/治疗暗示。

## 5. 候选 Golden Case 的批准标准

一个历史选题只有满足以下条件才建议进入 `tests/golden/`：

- 用户/编辑人工认可；
- 科学事实已经复核；
- 标题具备传播性但无明显失真；
- 内容结构代表希望长期保持的风格；
- 有明确“必须保留”和“允许变化”的部分。

## 6. Round 1 输出

建议输出：

```text
BGI Science Hotspots Skill
Baseline: 0.4.0
Candidate: 0.5.1

Regression: x / n PASS
Critical: x / n PASS
Golden: x / n PASS

Improved:
- ...

Stable:
- ...

Regressed:
- ...

Decision:
- KEEP / REVISE / BLOCK RELEASE
```

## 7. v0.1.0 的验收目标

这次试点不是为了证明 `0.5.1` 一定更好，而是为了验证：

1. BGI Edu Luban 能否发现真实差异；
2. Regression 是否足够“狠”，能找出退化；
3. Golden Cases 是否能保护历史好能力；
4. 十维评分是否和实际业务判断一致；
5. QA Card 是否能成为后续内部 Skill 发版的统一证据格式。
