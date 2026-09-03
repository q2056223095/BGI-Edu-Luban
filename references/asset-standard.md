# BGI Edu AI Asset Standard v0.1.0

## 推荐最小结构

```text
asset-name/
├── SKILL.md
├── README.md
├── VERSION
├── CHANGELOG.md
├── references/
├── examples/
├── tests/
│   ├── regression/
│   ├── golden/
│   └── adversarial/
└── tools/ or scripts/
```

## 最小内容要求

### SKILL.md
- 定位；
- 触发条件；
- 输入契约；
- 工作流；
- 输出契约；
- 失败处理；
- Stop Gates；
- 反例。

### README.md
- 谁使用；
- 什么时候用；
- 交付什么；
- 如何触发；
- 示例；
- 限制；
- 验证方式。

### tests/regression
至少覆盖真实高频任务和历史失败。

### tests/golden
只存人工认可的黄金样例；AI 自己选的不算。

### CHANGELOG
每版写 Why + Evidence，不要只写“优化效果”。
