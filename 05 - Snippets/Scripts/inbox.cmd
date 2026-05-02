@echo off
REM === Obsidian Quick Inbox ===
REM Usage: inbox "Note text here"
REM        inbox "Title::Note content"
REM
REM First time: run and it will ask for your REST API key.
REM Need to set execution policy? Run this once in PowerShell as Admin:
REM   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

powershell -ExecutionPolicy Bypass -File "%~dp0rest-api.ps1" inbox %*
