Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = oWS.SpecialFolders("Desktop") & "\TradingAgents.lnk"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "D:\TradingAgents\start_tradingagents.bat"
oLink.WorkingDirectory = "D:\TradingAgents"
oLink.Description = "TradingAgents - Multi-Agent Trading Framework"
oLink.IconLocation = "C:\Windows\System32\shell32.dll,138"
oLink.Save

WScript.Echo "Desktop shortcut created successfully!"