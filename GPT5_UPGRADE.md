# GPT-5 Model Upgrade (2025)

## ✅ 升级完成

TradingAgents 已升级支持 OpenAI 2025 最新模型系列。

## 🎯 主要更新

### 1. CLI 模型选择更新
在 CLI 中现在可以选择以下新模型：

**Quick-Thinking (快速响应):**
- GPT-5 系列: `gpt-5`, `gpt-5-mini` (推荐), `gpt-5-nano`, `gpt-5-chat-latest`
- GPT-4 系列 (Legacy): `gpt-4o`, `gpt-4o-mini`, `gpt-4.1-nano`, `gpt-4.1-mini`

**Deep-Thinking (深度推理):**
- o3 系列: `o3-pro`, `o3`, `o4-mini` (推荐)
- GPT-5 系列: `gpt-5`, `gpt-5-mini`
- Legacy: `o1`, `gpt-4o`, `gpt-4.1-mini`, `gpt-4.1-nano`

### 2. 默认配置更新
- Deep Think: `o4-mini` (快速推理)
- Quick Think: `gpt-5-mini` (从 `gpt-4o-mini` 升级)

## 🚀 如何使用

### 方式1: CLI 交互式选择（推荐）
```bash
python -m cli.main
```
或双击桌面快捷方式，然后在界面中选择您想要的模型。

### 方式2: 代码中自定义
```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()
config["deep_think_llm"] = "o3"          # 选择推理模型
config["quick_think_llm"] = "gpt-5"      # 选择快速模型
config["max_debate_rounds"] = 3          # 调整辩论轮数

ta = TradingAgentsGraph(debug=True, config=config)
_, decision = ta.propagate("NVDA", "2024-05-10")
```

## 💡 推荐配置

**生产环境（最佳性能）:**
- Deep: `o3` 或 `o3-pro`
- Quick: `gpt-5`
- 成本: 高 | 质量: 最佳

**日常使用（推荐）:**
- Deep: `o4-mini`
- Quick: `gpt-5-mini`
- 成本: 中等 | 质量: 很好

**测试开发（省钱）:**
- Deep: `o4-mini`
- Quick: `gpt-5-nano`
- 成本: 低 | 质量: 良好

## 📝 注意事项

1. GPT-5 和 o3 模型比旧版本更贵
2. 建议先用便宜的模型测试
3. 可以通过减少 `max_debate_rounds` 来降低成本
4. 所有旧模型仍然可用（向后兼容）

## 📚 更多信息

- 完整架构文档: `CLAUDE.md`
- OpenAI 官方文档: https://platform.openai.com/docs/models