@echo off
REM === Obsidian Search ===
REM Usage: search "keyword"

powershell -ExecutionPolicy Bypass -File "%~dp0rest-api.ps1" search %*
