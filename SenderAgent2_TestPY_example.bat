@echo off
cd /d %~dp0
py SenderAgent2.py "--api=https://example.com" "--title=TestTitle" "--desp=TestDesp" "--url=http://ysht.me" --quiet
pause