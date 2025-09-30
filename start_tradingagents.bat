@echo off
chcp 65001 >nul
title TradingAgents - Multi-Agent Trading Framework

echo ========================================
echo   TradingAgents CLI Launcher
echo ========================================
echo.

cd /d D:\TradingAgents

echo Starting TradingAgents...
echo.

python -m cli.main

echo.
echo TradingAgents has been closed.
pause