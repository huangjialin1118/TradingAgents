# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

TradingAgents is a multi-agent LLM financial trading framework built with LangGraph. The system deploys specialized agents (analysts, researchers, traders, and risk managers) that collaboratively evaluate market conditions and make trading decisions through structured debates.

**IMPORTANT**: This is a research framework. It is not intended as financial, investment, or trading advice.

## Setup & Installation

Install dependencies:
```bash
pip install -r requirements.txt
```

Required environment variables:
```bash
export FINNHUB_API_KEY=$YOUR_FINNHUB_API_KEY
export OPENAI_API_KEY=$YOUR_OPENAI_API_KEY
```

## Running the Framework

### CLI Mode
```bash
python -m cli.main
```
Interactive CLI for selecting tickers, dates, LLMs, and research depth.

### Python API
```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

ta = TradingAgentsGraph(debug=True, config=DEFAULT_CONFIG.copy())
_, decision = ta.propagate("NVDA", "2024-05-10")
```

### Model Selection Guide (2025 Update)

**Deep Thinking Models (Reasoning):**
- `o3-pro` - Maximum intelligence, best for high-stakes decisions (Premium)
- `o3` - High-performance reasoning for math, science, coding
- `o4-mini` - Fast, cost-efficient reasoning (Recommended for testing)

**Quick Thinking Models (Fast Response):**
- `gpt-5` - Latest flagship model, best overall performance (Aug 2025)
- `gpt-5-mini` - Balanced performance and cost (Default)
- `gpt-5-nano` - Most cost-efficient
- `gpt-4o` / `gpt-4o-mini` - Previous generation, still powerful

### Configuration Examples

**Production (Best Performance):**
```python
config = DEFAULT_CONFIG.copy()
config["deep_think_llm"] = "o3"
config["quick_think_llm"] = "gpt-5"
config["max_debate_rounds"] = 3
```

**Balanced (Recommended):**
```python
config = DEFAULT_CONFIG.copy()
config["deep_think_llm"] = "o4-mini"
config["quick_think_llm"] = "gpt-5-mini"
config["max_debate_rounds"] = 2
```

**Testing (Low Cost):**
```python
config = DEFAULT_CONFIG.copy()
config["deep_think_llm"] = "o4-mini"
config["quick_think_llm"] = "gpt-5-nano"
config["max_debate_rounds"] = 1
```

See `config_examples.py` for more configuration options.

## Architecture

### Core Components

**TradingAgentsGraph** (`tradingagents/graph/trading_graph.py`): Main orchestration class that initializes all agents and executes the trading workflow via LangGraph.

**Agent Types**:
- **Analysts** (`tradingagents/agents/analysts/`): Fundamental, sentiment, news, and technical analysis
- **Researchers** (`tradingagents/agents/researchers/`): Bull and bear researchers that debate investment opportunities
- **Trader** (`tradingagents/agents/trader/`): Synthesizes analyst/researcher insights into trading decisions
- **Risk Management** (`tradingagents/agents/risk_mgmt/`): Conservative, aggressive, and neutral debators evaluate portfolio risk
- **Managers** (`tradingagents/agents/managers/`): Research manager and risk manager oversee discussions and make final approvals

### Agent Workflow

1. **Analysis Phase**: Analysts gather data (market, sentiment, news, fundamentals)
2. **Research Phase**: Bull/bear researchers debate investment merits (configurable rounds via `max_debate_rounds`)
3. **Trading Phase**: Trader creates investment plan based on debates
4. **Risk Phase**: Risk debators assess plan (configurable rounds via `max_risk_discuss_rounds`)
5. **Decision Phase**: Risk manager approves/rejects final decision

### Data Flow

**Dataflows** (`tradingagents/dataflows/`): Handle data collection from multiple sources
- `finnhub_utils.py`: FinnHub API integration
- `yfin_utils.py`: Yahoo Finance data
- `reddit_utils.py`: Reddit sentiment
- `googlenews_utils.py`: Google News
- `stockstats_utils.py`: Technical indicators

**Tool Modes**:
- `online_tools=True`: Use real-time data APIs
- `online_tools=False`: Use cached data from Tauric TradingDB (for backtesting)

### Configuration

`tradingagents/default_config.py` contains all configuration:
- LLM providers: `openai`, `anthropic`, `google`, `ollama`, `openrouter`
- Models: `deep_think_llm` (reasoning), `quick_think_llm` (analysis)
- Debate rounds: `max_debate_rounds`, `max_risk_discuss_rounds`
- Data modes: `online_tools` flag
- Directories: `results_dir`, `data_cache_dir`

### Memory System

`tradingagents/agents/utils/memory.py`: FinancialSituationMemory enables agents to learn from past decisions through reflection (see `reflect_and_remember()` method).

## Key Files

- `main.py`: Example usage with custom config
- `cli/main.py`: Interactive CLI implementation
- `tradingagents/graph/setup.py`: Graph construction logic
- `tradingagents/graph/propagation.py`: State initialization and execution
- `tradingagents/graph/reflection.py`: Reflection and learning logic
- `tradingagents/agents/__init__.py`: Toolkit initialization

## Testing

For experimentation with lower costs:
```python
config["deep_think_llm"] = "o4-mini"
config["quick_think_llm"] = "gpt-4o-mini"
config["max_debate_rounds"] = 1
config["max_risk_discuss_rounds"] = 1
```

## LLM Providers

Supported: OpenAI, Anthropic, Google, Ollama, OpenRouter. Configure via `llm_provider` and `backend_url` in config.

**2025 Production Recommendations:**
- **Premium**: `o3` or `o3-pro` (deep think) + `gpt-5` (quick think)
- **Balanced**: `o4-mini` (deep think) + `gpt-5-mini` (quick think) - Default
- **Budget**: `o4-mini` (deep think) + `gpt-5-nano` (quick think)