@echo off
cd /d %~dp0
rd /S /Q dist
pyinstaller --noconsole SenderAgent2.py
del /F /Q SenderAgent2.spec
rd /S /Q build