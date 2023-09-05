@echo off
cd /d %~dp0
SenderAgent2.exe "--api=https://example.com/?" "--title=测试标题TestTitle" "--desp=测试正文TestDesp" "--url=http://ysht.me" --quiet
pause