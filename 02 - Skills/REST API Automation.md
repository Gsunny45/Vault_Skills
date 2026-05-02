---
type: skill
name: REST API Automation
category: Integration
difficulty: beginner
tags:
  - skill
  - automation
  - rest-api
  - scripting
---

# REST API Automation

## What This Skill Covers
How to use the Obsidian REST API plugin to automate your vault — inbox notes, search content, read files, and more — using ready-made scripts. No coding required.

## When You Need This
- You want to send notes into your vault from anywhere (terminal, AI agents, browser)
- You want to search your vault without opening Obsidian
- You want AI agents (Claude, GPT) to read/write your vault for you
- You want to batch-process or reorganize notes programmatically

## Core Concepts
- The REST API plugin runs a web server inside Obsidian on `http://127.0.0.1:27123`
- Every request needs an **API Key** (like a password) in the `Authorization: Bearer YOUR-KEY` header
- v3+ requires `Bearer` prefix — just the raw key returns 401
- You can read, write, search, and delete notes using HTTP requests
- The API **only works when Obsidian is open** with the plugin enabled

## Vaults Configured (MarsBase)

These vaults have the REST API plugin installed, HTTP enabled on port 27123, and keys saved:

| Vault | Path | Key in Scripts |
|---|---|---|
| Local-Network-Hub | `Documents/Local-Network-Hub` | ✅ (regenerated) |
| Gemini_Vault | `Documents/Gemini_Vault` | ✅ (regenerated) |
| Command_Vault | `Documents/Command_Vault` | ✅ (regenerated) |
| RAG_Vault | `Documents/RAG_Vault` | ✅ (regenerated) |
| Claude_Vault | `Documents/Claude_Vault` | ✅ (regenerated) |

**To switch vaults:** Close Obsidian, open the other vault. The scripts connect to whatever is running on port 27123.

## Step-by-Step

### Step 1 — Install plugin (one time per vault)
1. Open the vault in Obsidian → Community Plugins → search "REST API" → Install & Enable
2. Go to plugin Settings → make sure **"Enable Insecure Server" (port 27123) is ON**
3. Copy the **API Key** shown

### Step 2 — Save the key to the scripts
The scripts live in Vault_Skills (not in each vault). Open PowerShell:
```powershell
cd "C:\Users\MarsBase\Documents\Vault_Skills\05 - Snippets\Scripts"
.\rest-api.ps1 config
```
Type `y` to clear old config, then run any command to paste the new key.

Or manually save the key to `rest-config.json`:
```json
{ "ApiKey": "Bearer YOUR-KEY", "BaseUrl": "http://127.0.0.1:27123" }
```

### Step 3 — Close and reopen Obsidian
This loads the new key from disk.

### Step 4 — Verify it works
```powershell
.\rest-api.ps1 list
```

### Step 5 — Use the commands

**Inbox a quick note:**
```powershell
.\rest-api.ps1 inbox "Remember to buy milk"
```

**Inbox with a custom title:**
```powershell
.\rest-api.ps1 inbox "Meeting Notes::Discussed Q3 roadmap with team"
```

**Search your vault:**
```powershell
.\rest-api.ps1 search "Templater"
```

**Read a note:**
```powershell
.\rest-api.ps1 read "01 - Plugins/_Plugin Index.md"
```

**List everything:**
```powershell
.\rest-api.ps1 list
```

## Variations / Approaches

| Approach | Complexity | Best For |
|---|---|---|
| PowerShell script (`rest-api.ps1`) | Beginner | Daily use, quick inbox/search |
| CMD wrappers (`inbox.cmd`, `search.cmd`) | Beginner | Run from Run dialog (Win+R) or taskbar |
| Python script (see below) | Intermediate | AI agent integration, complex automation |
| Direct curl | Advanced | Debugging, one-off tests |

## Example (copy-paste ready)

### Python — AI agent that can read/write your vault
Save this as `obsidian_agent.py` — an AI agent or script can import and use it:

```python
"""obsidian_agent.py — Use this from any Python script or AI agent."""
import requests
from datetime import date

class ObsidianVault:
    def __init__(self, api_key, base_url="http://127.0.0.1:27123"):
        self.base = base_url
        # v3+ requires "Bearer " prefix
        if not api_key.startswith("Bearer "):
            api_key = "Bearer " + api_key
        self.headers = {"Authorization": api_key}
        self.json_headers = {"Authorization": api_key, "Content-Type": "application/json"}

    def inbox(self, title, content):
        """Add a note to the inbox."""
        path = f"03-Inbox/{requests.utils.quote(title)}.md"
        note = f"""---
created: {date.today()}
source: ai-agent
---

# {title}

{content}
"""
        r = requests.put(f"{self.base}/vault/{path}",
                        json={"content": note}, headers=self.json_headers)
        return r.ok

    def read(self, path):
        """Read a note by its relative path (returns raw markdown)."""
        encoded = "/".join(requests.utils.quote(p) for p in path.split("/"))
        r = requests.get(f"{self.base}/vault/{encoded}", headers=self.headers)
        return r.text if r.ok else None  # returns raw markdown, not JSON

    def search(self, query):
        """Search for notes containing text."""
        r = requests.post(f"{self.base}/search/simple/?query={requests.utils.quote(query)}",
                         headers=self.headers)
        return r.json() if r.ok else []  # returns array of {filename, score, matches}

    def list_files(self):
        """List all files in the vault."""
        r = requests.get(f"{self.base}/vault/", headers=self.headers)
        if r.ok:
            data = r.json()
            return data.get("files", [])
        return []


# ─── Usage example ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    KEY = input("Enter your REST API key: ")
    vault = ObsidianVault(KEY)

    # Inbox a note
    vault.inbox("AI Agent Note", "This was written by a Python script via the REST API.")

    # Search for something
    results = vault.search("Dataview")
    for r in results:
        print(f"Found: {r['filename']} (score: {r['score']})")

    # Read a file
    content = vault.read("CLAUDE.md")
    if content:
        print(f"CLAUDE.md:\n{content[:200]}...")
```

### Quick CMD usage (no PowerShell needed)
```cmd
:: From any command prompt or Win+R:
inbox "Quick thought"
search "keyword"
```

## Troubleshooting

### "Regenerate" button blacks out the settings screen
Known bug in v3.6.1. Fix it by editing the config file directly:
1. Close Obsidian completely
2. Open `[vault]/.obsidian/plugins/obsidian-local-rest-api/data.json` in a text editor
3. Change the `"apiKey"` value to a new random string (any text works)
4. Save and reopen Obsidian
5. Update the key in `rest-config.json` to match (with `Bearer ` prefix)

### "Authorization required" / 401 errors
Most likely the `Bearer ` prefix is missing. The raw key alone doesn't work in v3+. Both the PowerShell and Python scripts add it automatically.

### "Unknown or invalid Content-Type" / 400 errors
Wrong Content-Type header. PUT with JSON body = `application/json`. Simple search = no Content-Type needed.

## Common Mistakes
- **Forgot API key**: You need Obsidian open + REST API plugin enabled. Always check that first.
- **API key was exposed**: If you accidentally shared your key (in a message, screenshot, etc.), **regenerate it immediately** in Obsidian settings.
- **Missing `Bearer` prefix**: v3+ of the plugin requires `Authorization: Bearer YOUR-KEY`. The raw key alone returns 401. Both the PowerShell and Python scripts handle this automatically.
- **Wrong Content-Type**: PUT/POST requests need the right Content-Type header. JSON bodies need `application/json`. Search doesn't need it. Wrong type = 400 error.
- **File not found errors**: Spaces in paths must use `%20`. The PowerShell script handles this automatically; curl does not.
- **PUT overwrites without warning**: Always read a file first if you want to modify it, don't just write over it.

## Related Skills
- [[REST API]] — full plugin reference note

## Related Plugins
- [[REST API]]
- [[Local GPT]]
- [[QuickAdd]]
