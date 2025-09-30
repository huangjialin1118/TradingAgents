"""
Internationalization (i18n) module for TradingAgents CLI
Supports English and Chinese languages
"""

TRANSLATIONS = {
    "en": {
        # Welcome and branding
        "welcome_title": "Welcome to TradingAgents",
        "welcome_subtitle": "Multi-Agents LLM Financial Trading Framework",
        "welcome_description": "TradingAgents: Multi-Agents LLM Financial Trading Framework - CLI",
        "workflow_steps": "Workflow Steps:",
        "workflow_description": "I. Analyst Team → II. Research Team → III. Trader → IV. Risk Management → V. Portfolio Management",
        "built_by": "Built by [Tauric Research](https://github.com/TauricResearch)",

        # Step titles
        "step1_ticker_title": "Step 1: Ticker Symbol",
        "step1_ticker_prompt": "Enter the ticker symbol to analyze",
        "step2_date_title": "Step 2: Analysis Date",
        "step2_date_prompt": "Enter the analysis date (YYYY-MM-DD)",
        "step3_analysts_title": "Step 3: Analysts Team",
        "step3_analysts_prompt": "Select your LLM analyst agents for the analysis",
        "step4_depth_title": "Step 4: Research Depth",
        "step4_depth_prompt": "Select your research depth level",
        "step5_provider_title": "Step 5: LLM Provider",
        "step5_provider_prompt": "Select which service to talk to",
        "step6_thinking_title": "Step 6: Thinking Agents",
        "step6_thinking_prompt": "Select your thinking agents for analysis",
        "step7_translation_title": "Step 7: Report Translation",
        "step7_translation_prompt": "Do you want to translate the report to Chinese?",
        "step8_translation_llm_title": "Step 8: Translation Model",
        "step8_translation_llm_prompt": "Select the LLM for translation",
        "step9_save_title": "Step 9: Save Report",
        "step9_save_prompt": "Do you want to save the report?",
        "step10_format_title": "Step 10: Report Format",
        "step10_format_prompt": "Select report format(s)",

        # Language selection
        "language_selection_title": "Language Selection / 语言选择",
        "language_selection_prompt": "Please select your preferred language:",
        "language_english": "English",
        "language_chinese": "中文 (Chinese)",

        # Translation options
        "translation_yes": "Yes, translate to Chinese (Recommended: GPT-5 Mini)",
        "translation_no": "No, keep English report only",

        # Save options
        "save_yes": "Yes, save report",
        "save_no": "No, don't save",

        # Format options
        "format_markdown": "Markdown (.md)",
        "format_html": "HTML (.html)",
        "format_both": "Both Markdown and HTML",

        # Research depth
        "depth_shallow": "Shallow - Quick research, few debate and strategy discussion rounds",
        "depth_medium": "Medium - Middle ground, moderate debate rounds and strategy discussion",
        "depth_deep": "Deep - Comprehensive research, in depth debate and strategy discussion",

        # Analyst names
        "analyst_market": "Market Analyst",
        "analyst_social": "Social Media Analyst",
        "analyst_news": "News Analyst",
        "analyst_fundamentals": "Fundamentals Analyst",

        # Agent status
        "status_pending": "Pending",
        "status_in_progress": "In Progress",
        "status_completed": "Completed",

        # Messages
        "selected_analysts": "Selected analysts:",
        "selected_ticker": "Selected ticker:",
        "analysis_date": "Analysis date:",
        "analyzing": "Analyzing",
        "translation_in_progress": "Translating report to Chinese...",
        "translation_completed": "Translation completed!",
        "saving_report": "Saving report...",
        "report_saved": "Report saved successfully!",
        "report_saved_at": "Report saved at:",

        # Report sections
        "report_market": "Market Analysis Report",
        "report_sentiment": "Sentiment Analysis Report",
        "report_news": "News Analysis Report",
        "report_fundamentals": "Fundamentals Analysis Report",
        "report_investment": "Investment Research Report",
        "report_trader": "Trading Decision",
        "report_final": "Final Portfolio Decision",

        # Errors
        "error_no_ticker": "No ticker symbol provided. Exiting...",
        "error_no_date": "No date provided. Exiting...",
        "error_no_analysts": "No analysts selected. Exiting...",
        "error_no_depth": "No research depth selected. Exiting...",
        "error_no_provider": "No LLM provider selected. Exiting...",
        "error_no_shallow": "No quick-thinking LLM selected. Exiting...",
        "error_no_deep": "No deep-thinking LLM selected. Exiting...",
        "error_translation_failed": "Translation failed, showing English report only.",
    },

    "zh": {
        # Welcome and branding
        "welcome_title": "欢迎使用 TradingAgents",
        "welcome_subtitle": "多智能体 LLM 金融交易框架",
        "welcome_description": "TradingAgents：多智能体 LLM 金融交易框架 - CLI",
        "workflow_steps": "工作流程：",
        "workflow_description": "I. 分析师团队 → II. 研究团队 → III. 交易员 → IV. 风险管理 → V. 投资组合管理",
        "built_by": "由 [Tauric Research](https://github.com/TauricResearch) 构建",

        # Step titles
        "step1_ticker_title": "步骤 1：股票代码",
        "step1_ticker_prompt": "请输入要分析的股票代码",
        "step2_date_title": "步骤 2：分析日期",
        "step2_date_prompt": "请输入分析日期（格式：YYYY-MM-DD）",
        "step3_analysts_title": "步骤 3：分析师团队",
        "step3_analysts_prompt": "选择您的 LLM 分析师代理",
        "step4_depth_title": "步骤 4：研究深度",
        "step4_depth_prompt": "选择研究深度级别",
        "step5_provider_title": "步骤 5：LLM 提供商",
        "step5_provider_prompt": "选择要使用的服务",
        "step6_thinking_title": "步骤 6：思考代理",
        "step6_thinking_prompt": "选择用于分析的思考代理",
        "step7_translation_title": "步骤 7：报告翻译",
        "step7_translation_prompt": "是否将报告翻译成中文？",
        "step8_translation_llm_title": "步骤 8：翻译模型",
        "step8_translation_llm_prompt": "选择用于翻译的 LLM",
        "step9_save_title": "步骤 9：保存报告",
        "step9_save_prompt": "是否保存报告？",
        "step10_format_title": "步骤 10：报告格式",
        "step10_format_prompt": "选择报告格式",

        # Language selection
        "language_selection_title": "Language Selection / 语言选择",
        "language_selection_prompt": "请选择您偏好的语言：",
        "language_english": "English",
        "language_chinese": "中文 (Chinese)",

        # Translation options
        "translation_yes": "是，翻译成中文（推荐使用 GPT-5 Mini）",
        "translation_no": "否，仅保留英文报告",

        # Save options
        "save_yes": "是，保存报告",
        "save_no": "否，不保存",

        # Format options
        "format_markdown": "Markdown 格式（.md）",
        "format_html": "HTML 格式（.html）",
        "format_both": "Markdown 和 HTML 两种格式",

        # Research depth
        "depth_shallow": "浅度 - 快速研究，较少的辩论和策略讨论轮次",
        "depth_medium": "中度 - 中等水平，适度的辩论轮次和策略讨论",
        "depth_deep": "深度 - 全面研究，深入的辩论和策略讨论",

        # Analyst names
        "analyst_market": "市场分析师",
        "analyst_social": "社交媒体分析师",
        "analyst_news": "新闻分析师",
        "analyst_fundamentals": "基本面分析师",

        # Agent status
        "status_pending": "等待中",
        "status_in_progress": "进行中",
        "status_completed": "已完成",

        # Messages
        "selected_analysts": "已选择的分析师：",
        "selected_ticker": "已选择的股票代码：",
        "analysis_date": "分析日期：",
        "analyzing": "正在分析",
        "translation_in_progress": "正在将报告翻译成中文...",
        "translation_completed": "翻译完成！",
        "saving_report": "正在保存报告...",
        "report_saved": "报告保存成功！",
        "report_saved_at": "报告已保存至：",

        # Report sections
        "report_market": "市场分析报告",
        "report_sentiment": "情绪分析报告",
        "report_news": "新闻分析报告",
        "report_fundamentals": "基本面分析报告",
        "report_investment": "投资研究报告",
        "report_trader": "交易决策",
        "report_final": "最终投资组合决策",

        # Errors
        "error_no_ticker": "未提供股票代码，退出中...",
        "error_no_date": "未提供日期，退出中...",
        "error_no_analysts": "未选择分析师，退出中...",
        "error_no_depth": "未选择研究深度，退出中...",
        "error_no_provider": "未选择 LLM 提供商，退出中...",
        "error_no_shallow": "未选择快速思考 LLM，退出中...",
        "error_no_deep": "未选择深度思考 LLM，退出中...",
        "error_translation_failed": "翻译失败，仅显示英文报告。",
    }
}


class I18n:
    """Internationalization handler"""

    def __init__(self, language="en"):
        """
        Initialize with a language code

        Args:
            language: "en" for English, "zh" for Chinese
        """
        self.language = language if language in TRANSLATIONS else "en"

    def t(self, key):
        """
        Translate a key to the current language

        Args:
            key: The translation key

        Returns:
            Translated string, or the key itself if not found
        """
        return TRANSLATIONS[self.language].get(key, key)

    def set_language(self, language):
        """
        Change the current language

        Args:
            language: "en" for English, "zh" for Chinese
        """
        if language in TRANSLATIONS:
            self.language = language

    def get_language(self):
        """Get current language code"""
        return self.language


# Global instance
_i18n_instance = None


def init_i18n(language="en"):
    """
    Initialize the global i18n instance

    Args:
        language: "en" for English, "zh" for Chinese
    """
    global _i18n_instance
    _i18n_instance = I18n(language)
    return _i18n_instance


def get_i18n():
    """Get the global i18n instance"""
    global _i18n_instance
    if _i18n_instance is None:
        _i18n_instance = I18n("en")
    return _i18n_instance


def t(key):
    """
    Convenience function to translate a key

    Args:
        key: The translation key

    Returns:
        Translated string
    """
    return get_i18n().t(key)