"""
Report Export Module for TradingAgents CLI

Handles saving reports in various formats (Markdown, HTML)
"""

import os
from pathlib import Path
from datetime import datetime


def save_reports(english_report, chinese_report, formats, output_dir, ticker, date, t_func=None):
    """
    Save trading reports in specified formats

    Args:
        english_report: English report content (Markdown)
        chinese_report: Chinese report content (Markdown) or None
        formats: List of format strings ["md"], ["html"], or ["md", "html"]
        output_dir: Output directory path
        ticker: Stock ticker symbol
        date: Analysis date
        t_func: Translation function from i18n (optional)

    Returns:
        List of saved file paths
    """
    saved_files = []

    # Ensure output directory exists
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save English reports
    if "md" in formats:
        en_md_path = save_markdown_report(english_report, output_dir, ticker, date, "en")
        saved_files.append(en_md_path)

    if "html" in formats:
        en_html_path = save_html_report(english_report, output_dir, ticker, date, "en")
        saved_files.append(en_html_path)

    # Save Chinese reports if available
    if chinese_report:
        if "md" in formats:
            zh_md_path = save_markdown_report(chinese_report, output_dir, ticker, date, "zh")
            saved_files.append(zh_md_path)

        if "html" in formats:
            zh_html_path = save_html_report(chinese_report, output_dir, ticker, date, "zh")
            saved_files.append(zh_html_path)

    return saved_files


def save_markdown_report(content, output_dir, ticker, date, language):
    """
    Save report as Markdown file

    Args:
        content: Report content in Markdown
        output_dir: Output directory path
        ticker: Stock ticker symbol
        date: Analysis date
        language: "en" or "zh"

    Returns:
        Path to saved file
    """
    # Add timestamp to filename to avoid conflicts
    timestamp = datetime.now().strftime('%H%M%S')
    filename = f"{ticker}_{date}_{timestamp}_report_{language}.md"
    filepath = Path(output_dir) / filename

    with open(filepath, "w", encoding="utf-8") as f:
        # Add header
        f.write(f"# TradingAgents Analysis Report\n\n")
        f.write(f"**Ticker:** {ticker}  \n")
        f.write(f"**Analysis Date:** {date}  \n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
        f.write(f"**Language:** {'English' if language == 'en' else '中文'}  \n\n")
        f.write("---\n\n")
        f.write(content)

    return str(filepath)


def save_html_report(content, output_dir, ticker, date, language):
    """
    Save report as HTML file with professional styling

    Args:
        content: Report content in Markdown
        output_dir: Output directory path
        ticker: Stock ticker symbol
        date: Analysis date
        language: "en" or "zh"

    Returns:
        Path to saved file
    """
    try:
        import markdown
    except ImportError:
        # Fallback: save as plain HTML if markdown library not available
        print("Warning: markdown library not found. Installing...")
        import subprocess
        subprocess.check_call(["pip", "install", "markdown"])
        import markdown

    # Convert Markdown to HTML
    html_content = markdown.markdown(
        content,
        extensions=['tables', 'fenced_code', 'nl2br']
    )

    # Generate HTML template
    html_template = generate_html_template(html_content, ticker, date, language)

    # Add timestamp to filename to avoid conflicts
    timestamp = datetime.now().strftime('%H%M%S')
    filename = f"{ticker}_{date}_{timestamp}_report_{language}.html"
    filepath = Path(output_dir) / filename

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_template)

    return str(filepath)


def generate_html_template(html_content, ticker, date, language):
    """
    Generate complete HTML document with styling

    Args:
        html_content: Converted HTML content from Markdown
        ticker: Stock ticker symbol
        date: Analysis date
        language: "en" or "zh"

    Returns:
        Complete HTML document string
    """
    lang_label = "English" if language == "en" else "中文"
    font_family = "'Segoe UI', Arial, sans-serif" if language == "en" else "'Microsoft YaHei', '微软雅黑', 'SimHei', sans-serif"

    template = f"""<!DOCTYPE html>
<html lang="{language}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradingAgents Report - {ticker} - {date}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: {font_family};
            line-height: 1.6;
            color: #333;
            background-color: #f5f5f5;
            padding: 20px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 40px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            border-radius: 8px;
        }}

        .header {{
            border-bottom: 3px solid #2c3e50;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}

        .header h1 {{
            color: #2c3e50;
            font-size: 2.5em;
            margin-bottom: 15px;
        }}

        .meta-info {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            background-color: #ecf0f1;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 30px;
        }}

        .meta-item {{
            padding: 10px;
        }}

        .meta-item strong {{
            display: block;
            color: #34495e;
            margin-bottom: 5px;
            font-size: 0.9em;
            text-transform: uppercase;
        }}

        .meta-item span {{
            color: #2c3e50;
            font-size: 1.1em;
            font-weight: 500;
        }}

        .content h1 {{
            color: #2c3e50;
            font-size: 2em;
            margin-top: 40px;
            margin-bottom: 20px;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }}

        .content h2 {{
            color: #34495e;
            font-size: 1.5em;
            margin-top: 30px;
            margin-bottom: 15px;
        }}

        .content h3 {{
            color: #7f8c8d;
            font-size: 1.2em;
            margin-top: 20px;
            margin-bottom: 10px;
        }}

        .content p {{
            margin-bottom: 15px;
            text-align: justify;
        }}

        .content table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}

        .content table th {{
            background-color: #3498db;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: 600;
        }}

        .content table td {{
            padding: 10px 12px;
            border-bottom: 1px solid #ddd;
        }}

        .content table tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}

        .content table tr:hover {{
            background-color: #ecf0f1;
        }}

        .content ul, .content ol {{
            margin-left: 30px;
            margin-bottom: 15px;
        }}

        .content li {{
            margin-bottom: 8px;
        }}

        .content code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            color: #e74c3c;
        }}

        .content pre {{
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 15px 0;
        }}

        .content pre code {{
            background-color: transparent;
            color: inherit;
            padding: 0;
        }}

        .content blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 20px;
            margin: 20px 0;
            color: #7f8c8d;
            font-style: italic;
        }}

        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #ecf0f1;
            text-align: center;
            color: #7f8c8d;
            font-size: 0.9em;
        }}

        .footer a {{
            color: #3498db;
            text-decoration: none;
        }}

        .footer a:hover {{
            text-decoration: underline;
        }}

        @media print {{
            body {{
                background-color: white;
                padding: 0;
            }}

            .container {{
                box-shadow: none;
                padding: 20px;
            }}

            .content h1 {{
                page-break-before: always;
            }}

            .content h1:first-of-type {{
                page-break-before: avoid;
            }}
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 20px;
            }}

            .header h1 {{
                font-size: 1.8em;
            }}

            .meta-info {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 TradingAgents Analysis Report</h1>
            <p style="color: #7f8c8d; font-size: 1.1em;">Multi-Agent LLM Financial Trading Framework</p>
        </div>

        <div class="meta-info">
            <div class="meta-item">
                <strong>Ticker Symbol</strong>
                <span>{ticker}</span>
            </div>
            <div class="meta-item">
                <strong>Analysis Date</strong>
                <span>{date}</span>
            </div>
            <div class="meta-item">
                <strong>Generated</strong>
                <span>{datetime.now().strftime('%Y-%m-%d %H:%M')}</span>
            </div>
            <div class="meta-item">
                <strong>Language</strong>
                <span>{lang_label}</span>
            </div>
        </div>

        <div class="content">
            {html_content}
        </div>

        <div class="footer">
            <p>Generated by <a href="https://github.com/TauricResearch/TradingAgents" target="_blank">TradingAgents</a></p>
            <p>Built by <a href="https://tauric.ai/" target="_blank">Tauric Research</a></p>
            <p style="margin-top: 10px; font-size: 0.85em;">⚠️ This is a research framework. Not intended as financial, investment, or trading advice.</p>
        </div>
    </div>
</body>
</html>"""

    return template