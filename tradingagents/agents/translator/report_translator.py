"""
Report Translator Agent for TradingAgents

This agent translates English financial trading reports to Chinese
while preserving formatting, structure, and technical accuracy.
"""

from langchain_core.prompts import ChatPromptTemplate


class ReportTranslator:
    """
    Translator agent specialized in financial report translation
    """

    def __init__(self, llm):
        """
        Initialize the translator

        Args:
            llm: Language model instance (ChatOpenAI, ChatAnthropic, etc.)
        """
        self.llm = llm
        self.prompt_template = self._create_prompt_template()

    def _create_prompt_template(self):
        """Create the translation prompt template"""

        system_message = """You are a professional financial report translator with expertise in translating English trading analysis reports to Chinese.

Your responsibilities:
1. Translate English financial reports to professional Chinese
2. Maintain all Markdown formatting (headers, tables, lists, code blocks)
3. Preserve technical accuracy for financial terms and metrics
4. Use professional financial Chinese terminology
5. Keep numbers, stock tickers, dates, and formulas unchanged
6. Maintain the exact report structure and organization

Translation Guidelines:
- Use appropriate financial terminology in Chinese (e.g., "Bull Market" → "牛市", "Bear Market" → "熊市")
- Preserve Markdown syntax: headers (#), tables (|), lists (-, *), code blocks (```)
- Keep technical indicators in English with Chinese explanation (e.g., "RSI (相对强弱指标)")
- Maintain professional tone suitable for financial professionals
- Do not add or remove content - translate faithfully
- Preserve line breaks and paragraph structure

Financial Terms Reference:
- Moving Average: 移动平均线
- Support/Resistance: 支撑/阻力位
- Bullish/Bearish: 看涨/看跌
- Volatility: 波动性
- Momentum: 动量
- Overbought/Oversold: 超买/超卖
- Breakout: 突破
- Divergence: 背离
- Portfolio: 投资组合
- Risk Management: 风险管理

Example Markdown Table Preservation:
Input:
| Indicator | Value | Signal |
|-----------|-------|--------|
| RSI | 65 | Neutral |

Output:
| 指标 | 数值 | 信号 |
|-----------|-------|--------|
| RSI | 65 | 中性 |

Now translate the following English report to Chinese:"""

        user_message = "{english_report}"

        return ChatPromptTemplate.from_messages([
            ("system", system_message),
            ("user", user_message)
        ])

    def translate(self, english_report):
        """
        Translate an English report to Chinese

        Args:
            english_report: The English report text (Markdown format)

        Returns:
            Chinese translation of the report
        """
        if not english_report or not isinstance(english_report, str):
            return ""

        try:
            # Create the prompt
            messages = self.prompt_template.format_messages(
                english_report=english_report
            )

            # Get translation from LLM
            response = self.llm.invoke(messages)

            # Extract content
            if hasattr(response, 'content'):
                chinese_report = response.content
            else:
                chinese_report = str(response)

            return chinese_report

        except Exception as e:
            print(f"Translation error: {e}")
            return f"Translation failed: {str(e)}"

    def translate_sections(self, report_sections):
        """
        Translate multiple report sections

        Args:
            report_sections: Dictionary of section name -> English report

        Returns:
            Dictionary of section name -> Chinese report
        """
        translated_sections = {}

        for section_name, english_content in report_sections.items():
            if english_content:
                print(f"Translating {section_name}...")
                translated_sections[section_name] = self.translate(english_content)
            else:
                translated_sections[section_name] = None

        return translated_sections