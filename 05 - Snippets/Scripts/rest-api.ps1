<#
.SYNOPSIS
  Obsidian REST API toolkit — inbox, search, read, list notes
.DESCRIPTION
  Run from PowerShell. First run will ask for your API key and save it.
  Usage examples:
    .\rest-api.ps1 inbox "Quick thought here"
    .\rest-api.ps1 inbox "Title::Note content goes here"
    .\rest-api.ps1 search "keyword"
    .\rest-api.ps1 read "path/to/note"
    .\rest-api.ps1 list
    .\rest-api.ps1 config
#>

param(
    [Parameter(Position=0)]
    [string]$Command,

    [Parameter(Position=1, ValueFromRemainingArguments=$true)]
    [string[]]$Args
)

# ─── Config ─────────────────────────────────────────────────────────────────
$configPath = Join-Path $PSScriptRoot "rest-config.json"
$baseUrl = "http://127.0.0.1:27123"

# Load or prompt for API key
function Get-ApiKey {
    if (Test-Path $configPath) {
        $cfg = Get-Content $configPath | ConvertFrom-Json
        return $cfg.ApiKey
    }
    Write-Host ""
    Write-Host "First time setup - enter your REST API key." -ForegroundColor Cyan
    Write-Host "Find it in Obsidian: Settings -> REST API -> copy the key." -ForegroundColor Yellow
    Write-Host ""
    $key = Read-Host "API Key"
    if (-not $key) {
        Write-Host "No key entered. Exiting." -ForegroundColor Red
        exit 1
    }
    # Add Bearer prefix if missing (REST API v3+ requires it)
    if (-not ($key -match "^Bearer ")) {
        $key = "Bearer $key"
    }
    $cfg = @{ ApiKey = $key; BaseUrl = $baseUrl } | ConvertTo-Json
    $cfg | Out-File $configPath -Encoding UTF8
    Write-Host "Saved to $configPath" -ForegroundColor Green
    Write-Host ""
    return $key
}

$apiKey = Get-ApiKey
$headers = @{ Authorization = $apiKey }
$jsonHeaders = @{ Authorization = $apiKey; "Content-Type" = "application/json" }

# ─── Helper ─────────────────────────────────────────────────────────────────

function UrlEncodePath {
    param([string]$Path)
    $parts = $Path -split '/'
    $encoded = @()
    foreach ($p in $parts) {
        $encoded += [System.Uri]::EscapeDataString($p)
    }
    return $encoded -join '/'
}

# ─── Functions ──────────────────────────────────────────────────────────────

function Invoke-Inbox {
    param([string]$RawText)
    if (-not $RawText) {
        Write-Host "Usage: .\rest-api.ps1 inbox ""Your note text""" -ForegroundColor Yellow
        return
    }

    # Parse "Title::Content" format, otherwise auto-title
    if ($RawText -match "^(.*?)::(.*)$") {
        $title = $matches[1].Trim()
        $content = $matches[2].Trim()
    } else {
        $title = "Inbox - $(Get-Date -Format 'yyyy-MM-dd HHmm')"
        $content = $RawText
    }

    $filename = "$title.md" -replace '[<>:"/\\|?*]', '_'
    $filepath = "00%20-%20Inbox/$([System.Uri]::EscapeDataString($filename))"

    $now = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $today = Get-Date -Format "yyyy-MM-dd"

    $noteBody = @"
---
created: $today
source: rest-api-inbox
---

# $title

$content

Inboxed at: $now
"@

    $body = @{ content = $noteBody } | ConvertTo-Json
    $url = "$baseUrl/vault/$filepath"

    try {
        $null = Invoke-RestMethod -Uri $url -Method Put -Headers $jsonHeaders -Body $body
        Write-Host "[OK] Inboxed: $title" -ForegroundColor Green
    } catch {
        Write-Host "[FAIL] $_" -ForegroundColor Red
    }
}

function Invoke-Search {
    param([string]$Query)
    if (-not $Query) {
        Write-Host "Usage: .\rest-api.ps1 search ""keyword""" -ForegroundColor Yellow
        return
    }
    try {
        $resp = Invoke-RestMethod -Uri "$baseUrl/search/simple/?query=$([System.Uri]::EscapeDataString($Query))" -Method Post -Headers $headers
        if ($resp.Count -eq 0) {
            Write-Host "No matches for '$Query'" -ForegroundColor Yellow
            return
        }
        Write-Host ""
        Write-Host "=== Results for '$Query' ===" -ForegroundColor Cyan
        foreach ($r in $resp) {
            Write-Host "  [FILE] $($r.filename)" -ForegroundColor White
            Write-Host "         Score: $($r.score)" -ForegroundColor DarkGray
            if ($r.match) {
                Write-Host "         Match: $($r.match)" -ForegroundColor Gray
            }
        }
        $count = $resp.results.Count
        Write-Host "($count results)" -ForegroundColor Cyan
        Write-Host ""
    } catch {
        Write-Host "[FAIL] Search failed: $_" -ForegroundColor Red
    }
}

function Invoke-ReadNote {
    param([string]$Path)
    if (-not $Path) {
        Write-Host "Usage: .\rest-api.ps1 read ""path/to/note""" -ForegroundColor Yellow
        return
    }
    $encoded = UrlEncodePath $Path
    $url = "$baseUrl/vault/$encoded"

    try {
        $resp = Invoke-RestMethod -Uri $url -Method Get -Headers $headers
        Write-Host ""
        Write-Host "=== $Path ===" -ForegroundColor Cyan
        Write-Host $resp -ForegroundColor White
    } catch {
        Write-Host "[FAIL] Could not read '$Path': $_" -ForegroundColor Red
    }
}

function Invoke-ListVault {
    try {
        $resp = Invoke-RestMethod -Uri "$baseUrl/vault/" -Method Get -Headers $headers
        Write-Host ""
        Write-Host "=== Vault Files ===" -ForegroundColor Cyan
        $count = 0
        foreach ($item in $resp.files) {
            Write-Host "  $item" -ForegroundColor DarkGray
            $count++
        }
        Write-Host "($count items)" -ForegroundColor Cyan
        Write-Host ""
    } catch {
        Write-Host "[FAIL] Could not list vault: $_" -ForegroundColor Red
    }
}

function Show-Config {
    Write-Host ""
    Write-Host "=== REST API Config ===" -ForegroundColor Cyan
    Write-Host "  Config file: $configPath"
    $short = $apiKey.Substring(0, [Math]::Min(16, $apiKey.Length))
    Write-Host "  API Key: $short..."
    Write-Host ""
    $reset = Read-Host "Clear config and re-enter key? (y/N)"
    if ($reset -eq "y") {
        Remove-Item $configPath -Force -ErrorAction SilentlyContinue
        Write-Host "Config cleared. Run any command to re-enter API key." -ForegroundColor Yellow
    }
}

# ─── Dispatch ───────────────────────────────────────────────────────────────

switch ($Command) {
    "inbox"  { Invoke-Inbox  ($Args -join " ") }
    "search" { Invoke-Search ($Args -join " ") }
    "read"   { Invoke-ReadNote ($Args -join " ") }
    "list"   { Invoke-ListVault }
    "config" { Show-Config }
    default {
        Write-Host @"
Usage: .\rest-api.ps1 <command> [arguments]

Commands:
  inbox "text"          Inbox a quick note
  inbox "Title::text"   Inbox with custom title
  search "keyword"      Search vault content
  read "path/to/note"   Read a note's content
  list                  List all vault files
  config                View/update settings

Examples:
  .\rest-api.ps1 inbox "Great idea for a plugin"
  .\rest-api.ps1 inbox "Meeting Notes::Discussed Q3 roadmap"
  .\rest-api.ps1 search "Local GPT"
  .\rest-api.ps1 read "01 - Plugins/_Plugin Index.md"
"@ -ForegroundColor Cyan
    }
}
