import questionary
from typing import List, Optional, Tuple, Dict

from cli.models import AnalystType

ANALYST_ORDER = [
    ("Market Analyst", AnalystType.MARKET),
    ("Social Media Analyst", AnalystType.SOCIAL),
    ("News Analyst", AnalystType.NEWS),
    ("Fundamentals Analyst", AnalystType.FUNDAMENTALS),
]


def get_ticker() -> str:
    """Prompt the user to enter a ticker symbol."""
    ticker = questionary.text(
        "Enter the ticker symbol to analyze:",
        validate=lambda x: len(x.strip()) > 0 or "Please enter a valid ticker symbol.",
        style=questionary.Style(
            [
                ("text", "fg:green"),
                ("highlighted", "noinherit"),
            ]
        ),
    ).ask()

    if not ticker:
        console.print("\n[red]No ticker symbol provided. Exiting...[/red]")
        exit(1)

    return ticker.strip().upper()


def get_analysis_date() -> str:
    """Prompt the user to enter a date in YYYY-MM-DD format."""
    import re
    from datetime import datetime

    def validate_date(date_str: str) -> bool:
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
            return False
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    date = questionary.text(
        "Enter the analysis date (YYYY-MM-DD):",
        validate=lambda x: validate_date(x.strip())
        or "Please enter a valid date in YYYY-MM-DD format.",
        style=questionary.Style(
            [
                ("text", "fg:green"),
                ("highlighted", "noinherit"),
            ]
        ),
    ).ask()

    if not date:
        console.print("\n[red]No date provided. Exiting...[/red]")
        exit(1)

    return date.strip()


def select_analysts() -> List[AnalystType]:
    """Select analysts using an interactive checkbox."""
    choices = questionary.checkbox(
        "Select Your [Analysts Team]:",
        choices=[
            questionary.Choice(display, value=value) for display, value in ANALYST_ORDER
        ],
        instruction="\n- Press Space to select/unselect analysts\n- Press 'a' to select/unselect all\n- Press Enter when done",
        validate=lambda x: len(x) > 0 or "You must select at least one analyst.",
        style=questionary.Style(
            [
                ("checkbox-selected", "fg:green"),
                ("selected", "fg:green noinherit"),
                ("highlighted", "noinherit"),
                ("pointer", "noinherit"),
            ]
        ),
    ).ask()

    if not choices:
        console.print("\n[red]No analysts selected. Exiting...[/red]")
        exit(1)

    return choices


def select_research_depth() -> int:
    """Select research depth using an interactive selection."""

    # Define research depth options with their corresponding values
    DEPTH_OPTIONS = [
        ("Shallow - Quick research, few debate and strategy discussion rounds", 1),
        ("Medium - Middle ground, moderate debate rounds and strategy discussion", 3),
        ("Deep - Comprehensive research, in depth debate and strategy discussion", 5),
    ]

    choice = questionary.select(
        "Select Your [Research Depth]:",
        choices=[
            questionary.Choice(display, value=value) for display, value in DEPTH_OPTIONS
        ],
        instruction="\n- Use arrow keys to navigate\n- Press Enter to select",
        style=questionary.Style(
            [
                ("selected", "fg:yellow noinherit"),
                ("highlighted", "fg:yellow noinherit"),
                ("pointer", "fg:yellow noinherit"),
            ]
        ),
    ).ask()

    if choice is None:
        console.print("\n[red]No research depth selected. Exiting...[/red]")
        exit(1)

    return choice


def select_shallow_thinking_agent(provider) -> str:
    """Select shallow thinking llm engine using an interactive selection."""

    # Define shallow thinking llm engine options with their corresponding model names
    SHALLOW_AGENT_OPTIONS = {
        "openai": [
            # GPT-5 Series (2025 - Latest)
            ("GPT-5 - Latest flagship model, best overall performance", "gpt-5"),
            ("GPT-5 Mini - Balanced performance and cost (Recommended)", "gpt-5-mini"),
            ("GPT-5 Nano - Most cost-efficient for simple tasks", "gpt-5-nano"),
            ("GPT-5 Chat Latest - Latest conversational model", "gpt-5-chat-latest"),
            # GPT-4 Series (Legacy)
            ("GPT-4o - Previous generation, still powerful", "gpt-4o"),
            ("GPT-4o-mini - Cost-effective legacy model", "gpt-4o-mini"),
            ("GPT-4.1-nano - Ultra-lightweight legacy model", "gpt-4.1-nano"),
            ("GPT-4.1-mini - Compact legacy model", "gpt-4.1-mini"),
        ],
        "anthropic": [
            ("Claude Haiku 3.5 - Fast inference and standard capabilities", "claude-3-5-haiku-latest"),
            ("Claude Sonnet 3.5 - Highly capable standard model", "claude-3-5-sonnet-latest"),
            ("Claude Sonnet 3.7 - Exceptional hybrid reasoning and agentic capabilities", "claude-3-7-sonnet-latest"),
            ("Claude Sonnet 4 - High performance and excellent reasoning", "claude-sonnet-4-0"),
        ],
        "google": [
            ("Gemini 2.0 Flash-Lite - Cost efficiency and low latency", "gemini-2.0-flash-lite"),
            ("Gemini 2.0 Flash - Next generation features, speed, and thinking", "gemini-2.0-flash"),
            ("Gemini 2.5 Flash - Adaptive thinking, cost efficiency", "gemini-2.5-flash-preview-05-20"),
        ],
        "openrouter": [
            ("Meta: Llama 4 Scout", "meta-llama/llama-4-scout:free"),
            ("Meta: Llama 3.3 8B Instruct - A lightweight and ultra-fast variant of Llama 3.3 70B", "meta-llama/llama-3.3-8b-instruct:free"),
            ("google/gemini-2.0-flash-exp:free - Gemini Flash 2.0 offers a significantly faster time to first token", "google/gemini-2.0-flash-exp:free"),
        ],
        "ollama": [
            ("llama3.1 local", "llama3.1"),
            ("llama3.2 local", "llama3.2"),
        ]
    }

    choice = questionary.select(
        "Select Your [Quick-Thinking LLM Engine]:",
        choices=[
            questionary.Choice(display, value=value)
            for display, value in SHALLOW_AGENT_OPTIONS[provider.lower()]
        ],
        instruction="\n- Use arrow keys to navigate\n- Press Enter to select",
        style=questionary.Style(
            [
                ("selected", "fg:magenta noinherit"),
                ("highlighted", "fg:magenta noinherit"),
                ("pointer", "fg:magenta noinherit"),
            ]
        ),
    ).ask()

    if choice is None:
        console.print(
            "\n[red]No shallow thinking llm engine selected. Exiting...[/red]"
        )
        exit(1)

    return choice


def select_deep_thinking_agent(provider) -> str:
    """Select deep thinking llm engine using an interactive selection."""

    # Define deep thinking llm engine options with their corresponding model names
    DEEP_AGENT_OPTIONS = {
        "openai": [
            # o-Series Reasoning Models (2025 - Latest)
            ("o3-pro - Maximum intelligence, best for high-stakes decisions", "o3-pro"),
            ("o3 - High-performance reasoning for math, science, coding", "o3"),
            ("o4-mini - Fast, cost-efficient reasoning (Recommended)", "o4-mini"),
            # GPT-5 Series (2025)
            ("GPT-5 - Latest flagship model, best overall performance", "gpt-5"),
            ("GPT-5 Mini - Balanced performance and cost", "gpt-5-mini"),
            # Legacy Models
            ("o1 - Premier reasoning model (legacy)", "o1"),
            ("GPT-4o - Standard model with solid capabilities", "gpt-4o"),
            ("GPT-4.1-mini - Compact legacy model", "gpt-4.1-mini"),
            ("GPT-4.1-nano - Ultra-lightweight legacy model", "gpt-4.1-nano"),
        ],
        "anthropic": [
            ("Claude Haiku 3.5 - Fast inference and standard capabilities", "claude-3-5-haiku-latest"),
            ("Claude Sonnet 3.5 - Highly capable standard model", "claude-3-5-sonnet-latest"),
            ("Claude Sonnet 3.7 - Exceptional hybrid reasoning and agentic capabilities", "claude-3-7-sonnet-latest"),
            ("Claude Sonnet 4 - High performance and excellent reasoning", "claude-sonnet-4-0"),
            ("Claude Opus 4 - Most powerful Anthropic model", "	claude-opus-4-0"),
        ],
        "google": [
            ("Gemini 2.0 Flash-Lite - Cost efficiency and low latency", "gemini-2.0-flash-lite"),
            ("Gemini 2.0 Flash - Next generation features, speed, and thinking", "gemini-2.0-flash"),
            ("Gemini 2.5 Flash - Adaptive thinking, cost efficiency", "gemini-2.5-flash-preview-05-20"),
            ("Gemini 2.5 Pro", "gemini-2.5-pro-preview-06-05"),
        ],
        "openrouter": [
            ("DeepSeek V3 - a 685B-parameter, mixture-of-experts model", "deepseek/deepseek-chat-v3-0324:free"),
            ("Deepseek - latest iteration of the flagship chat model family from the DeepSeek team.", "deepseek/deepseek-chat-v3-0324:free"),
        ],
        "ollama": [
            ("llama3.1 local", "llama3.1"),
            ("qwen3", "qwen3"),
        ]
    }
    
    choice = questionary.select(
        "Select Your [Deep-Thinking LLM Engine]:",
        choices=[
            questionary.Choice(display, value=value)
            for display, value in DEEP_AGENT_OPTIONS[provider.lower()]
        ],
        instruction="\n- Use arrow keys to navigate\n- Press Enter to select",
        style=questionary.Style(
            [
                ("selected", "fg:magenta noinherit"),
                ("highlighted", "fg:magenta noinherit"),
                ("pointer", "fg:magenta noinherit"),
            ]
        ),
    ).ask()

    if choice is None:
        console.print("\n[red]No deep thinking llm engine selected. Exiting...[/red]")
        exit(1)

    return choice

def select_llm_provider() -> tuple[str, str]:
    """Select the OpenAI api url using interactive selection."""
    # Define OpenAI api options with their corresponding endpoints
    BASE_URLS = [
        ("OpenAI", "https://api.openai.com/v1"),
        ("Anthropic", "https://api.anthropic.com/"),
        ("Google", "https://generativelanguage.googleapis.com/v1"),
        ("Openrouter", "https://openrouter.ai/api/v1"),
        ("Ollama", "http://localhost:11434/v1"),        
    ]
    
    choice = questionary.select(
        "Select your LLM Provider:",
        choices=[
            questionary.Choice(display, value=(display, value))
            for display, value in BASE_URLS
        ],
        instruction="\n- Use arrow keys to navigate\n- Press Enter to select",
        style=questionary.Style(
            [
                ("selected", "fg:magenta noinherit"),
                ("highlighted", "fg:magenta noinherit"),
                ("pointer", "fg:magenta noinherit"),
            ]
        ),
    ).ask()
    
    if choice is None:
        console.print("\n[red]no OpenAI backend selected. Exiting...[/red]")
        exit(1)
    
    display_name, url = choice
    print(f"You selected: {display_name}\tURL: {url}")

    return display_name, url


def select_language():
    """Select interface language using interactive selection."""
    from rich.console import Console
    console = Console()

    # Define language options
    LANGUAGE_OPTIONS = [
        ("English", "en"),
        ("中文 (Chinese)", "zh"),
    ]

    choice = questionary.select(
        "Language Selection / 语言选择:",
        choices=[
            questionary.Choice(display, value=value)
            for display, value in LANGUAGE_OPTIONS
        ],
        instruction="\n- Use arrow keys to navigate / 使用方向键导航\n- Press Enter to select / 按回车选择",
        style=questionary.Style(
            [
                ("selected", "fg:cyan noinherit"),
                ("highlighted", "fg:cyan noinherit"),
                ("pointer", "fg:cyan noinherit"),
            ]
        ),
    ).ask()

    if choice is None:
        console.print("\n[red]No language selected. Defaulting to English...[/red]")
        return "en"

    return choice


def select_translation_option(t_func):
    """
    Ask if user wants to translate report to Chinese

    Args:
        t_func: Translation function from i18n

    Returns:
        True if user wants translation, False otherwise
    """
    from rich.console import Console
    console = Console()

    TRANSLATION_OPTIONS = [
        (t_func("translation_yes"), True),
        (t_func("translation_no"), False),
    ]

    choice = questionary.select(
        t_func("step7_translation_prompt"),
        choices=[
            questionary.Choice(display, value=value)
            for display, value in TRANSLATION_OPTIONS
        ],
        instruction="\n- Use arrow keys to navigate\n- Press Enter to select",
        style=questionary.Style(
            [
                ("selected", "fg:yellow noinherit"),
                ("highlighted", "fg:yellow noinherit"),
                ("pointer", "fg:yellow noinherit"),
            ]
        ),
    ).ask()

    if choice is None:
        console.print(f"\n[yellow]{t_func('translation_no')}[/yellow]")
        return False

    return choice


def select_translation_llm(provider, t_func):
    """
    Select LLM for translation (fast models recommended)

    Args:
        provider: LLM provider name
        t_func: Translation function from i18n

    Returns:
        Selected model name
    """
    from rich.console import Console
    console = Console()

    # Define translation LLM options (fast models only)
    TRANSLATION_LLM_OPTIONS = {
        "openai": [
            ("GPT-5 Mini - Balanced performance and cost (Recommended)", "gpt-5-mini"),
            ("GPT-5 Nano - Most cost-efficient", "gpt-5-nano"),
            ("GPT-4o-mini - Cost-effective legacy model", "gpt-4o-mini"),
            ("GPT-5 - Best quality (higher cost)", "gpt-5"),
        ],
        "anthropic": [
            ("Claude Haiku 3.5 - Fast and efficient (Recommended)", "claude-3-5-haiku-latest"),
            ("Claude Sonnet 3.5 - Higher quality", "claude-3-5-sonnet-latest"),
        ],
        "google": [
            ("Gemini 2.0 Flash - Fast and efficient (Recommended)", "gemini-2.0-flash"),
            ("Gemini 2.0 Flash-Lite - Most economical", "gemini-2.0-flash-lite"),
        ],
        "openrouter": [
            ("Meta: Llama 3.3 8B - Fast and free", "meta-llama/llama-3.3-8b-instruct:free"),
            ("Google Gemini 2.0 Flash - Free tier", "google/gemini-2.0-flash-exp:free"),
        ],
        "ollama": [
            ("llama3.2 local", "llama3.2"),
            ("llama3.1 local", "llama3.1"),
        ]
    }

    choice = questionary.select(
        t_func("step8_translation_llm_prompt"),
        choices=[
            questionary.Choice(display, value=value)
            for display, value in TRANSLATION_LLM_OPTIONS[provider.lower()]
        ],
        instruction="\n- Use arrow keys to navigate\n- Press Enter to select",
        style=questionary.Style(
            [
                ("selected", "fg:cyan noinherit"),
                ("highlighted", "fg:cyan noinherit"),
                ("pointer", "fg:cyan noinherit"),
            ]
        ),
    ).ask()

    if choice is None:
        console.print(f"\n[red]{t_func('error_no_shallow')}[/red]")
        exit(1)

    return choice


def select_save_report(t_func):
    """
    Ask if user wants to save the report

    Args:
        t_func: Translation function from i18n

    Returns:
        True if user wants to save, False otherwise
    """
    from rich.console import Console
    console = Console()

    SAVE_OPTIONS = [
        (t_func("save_yes"), True),
        (t_func("save_no"), False),
    ]

    choice = questionary.select(
        t_func("step9_save_prompt"),
        choices=[
            questionary.Choice(display, value=value)
            for display, value in SAVE_OPTIONS
        ],
        instruction="\n- Use arrow keys to navigate\n- Press Enter to select",
        style=questionary.Style(
            [
                ("selected", "fg:green noinherit"),
                ("highlighted", "fg:green noinherit"),
                ("pointer", "fg:green noinherit"),
            ]
        ),
    ).ask()

    if choice is None:
        return False

    return choice


def select_report_format(t_func):
    """
    Select report save format(s)

    Args:
        t_func: Translation function from i18n

    Returns:
        List of format strings: ["md"], ["html"], or ["md", "html"]
    """
    from rich.console import Console
    console = Console()

    FORMAT_OPTIONS = [
        (t_func("format_markdown"), ["md"]),
        (t_func("format_html"), ["html"]),
        (t_func("format_both"), ["md", "html"]),
    ]

    choice = questionary.select(
        t_func("step10_format_prompt"),
        choices=[
            questionary.Choice(display, value=value)
            for display, value in FORMAT_OPTIONS
        ],
        instruction="\n- Use arrow keys to navigate\n- Press Enter to select",
        style=questionary.Style(
            [
                ("selected", "fg:green noinherit"),
                ("highlighted", "fg:green noinherit"),
                ("pointer", "fg:green noinherit"),
            ]
        ),
    ).ask()

    if choice is None:
        return ["md"]  # Default to markdown

    return choice
