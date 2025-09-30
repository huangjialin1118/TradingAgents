import os

# OpenAI Model Recommendations (2025):
#
# Deep Thinking (Reasoning-focused):
#   - "o3-pro"       : Most intelligent, longest thinking time, best for complex reasoning (Premium)
#   - "o3"           : High-performance reasoning model for math, science, coding
#   - "o4-mini"      : Fast, cost-efficient reasoning (Recommended for testing)
#
# Quick Thinking (Fast response):
#   - "gpt-5"        : Latest flagship model, best overall performance (Released Aug 2025)
#   - "gpt-5-mini"   : Balanced performance and cost
#   - "gpt-5-nano"   : Most cost-efficient, good for simple tasks
#   - "gpt-5-chat-latest" : Latest conversational model
#   - "gpt-4o"       : Previous generation, still powerful
#   - "gpt-4o-mini"  : Cost-effective for simple tasks
#
# Legacy Models (Still supported):
#   - "gpt-4.1", "gpt-4.5", "gpt-4-turbo"

DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
    "data_dir": "/Users/yluo/Documents/Code/ScAI/FR1-data",
    "data_cache_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "dataflows/data_cache",
    ),
    # LLM settings
    "llm_provider": "openai",
    "deep_think_llm": "o4-mini",      # Reasoning model for complex analysis
    "quick_think_llm": "gpt-5-mini",  # Fast model for quick tasks (Updated to GPT-5)
    "backend_url": "https://api.openai.com/v1",
    # Debate and discussion settings
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "max_recur_limit": 100,
    # Tool settings
    "online_tools": True,
}
