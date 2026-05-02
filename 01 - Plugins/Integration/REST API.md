---
type: plugin
name: REST API
category: Integration
status: active
complexity: high
downloads: 400k+
last-verified: 2026-04-29
tags:
  - plugin
  - integration
  - api
  - automation
  - external-access
---

# REST API

## What It Does
Exposes your Obsidian vault via a secure, authenticated REST API. Gives scripts, browser extensions, and AI agents a direct line into your vault — read notes, write notes, run commands, search, and more from any external tool that can make HTTP requests.

## When To Use It
- Connecting external AI agents (Claude, ChatGPT, custom scripts) to read/write your vault
- Building browser extensions or web clippers that save directly into Obsidian
- Automating note creation from external sources (RSS feeds, email, task managers)
- Writing sync scripts between Obsidian and other tools
- Triggering Obsidian commands from hotkey daemons, phone automation (Tasker, Shortcuts), or cron jobs
- Building custom dashboards or tools that display/query vault data externally
- Programmatic bulk operations — rename, retag, reorganize hundreds of notes

## Minimal Setup
1. **Install**: Community Plugins → REST API → Install & Enable
2. **Generate API key**: Settings → REST API → "Regenerate API Key" → copy immediately
3. **Note the port**: Default is `27123` — change only if there's a conflict
4. **Test the connection** (in PowerShell/CMD):
   ```powershell
   curl -H "Authorization: Bearer YOUR-API-KEY" http://127.0.0.1:27123/
   ```
   You should get a JSON response with vault info.
5. **Allow through firewall** (Windows): Windows Defender may prompt on first start — allow private networks.

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| API Key | (generate unique key) | Keep private — this is your vault password. Regenerate if exposed. |
| Port | `27123` (default) | Change only if port conflict. Must restart plugin after changing. |
| HTTPS | Off (localhost only) | Enable ONLY if exposing to other devices on your network. Requires certificate setup. |
| Allowed IPs | `127.0.0.1` (default) | Add other IPs (e.g. `192.168.1.0/24`) if accessing from other devices on LAN. Leave on localhost for security. |

## API Endpoints Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Vault info — name, file count, plugin version |
| `GET` | `/vault/` | List all files and folders in the vault |
| `GET` | `/vault/{path}` | Read a specific file's content (returns raw markdown) |
| `PUT` | `/vault/{path}` | Write/create a file. Body: `{ "content": "..." }` with `Content-Type: application/json` |
| `DELETE` | `/vault/{path}` | Delete a file |
| `POST` | `/search/simple/?query=term` | Simple text search across all notes (no special Content-Type needed) |
| `POST` | `/search/` | Advanced search: Dataview DQL or JsonLogic (requires specific Content-Type headers) |
| `GET` | `/active/` | Get the currently active file info |
| `POST` | `/commands/{commandId}/` | Execute an Obsidian command by its command ID |
| `GET` | `/tags/` | List all tags with usage counts |
| `POST` | `/open/{path}` | Open a file in the Obsidian UI |

> **Path encoding**: Spaces and special chars in paths must be URL-encoded. Use `%20` for spaces. E.g. `/vault/01%20-%20Plugins/Integration/REST%20API.md`

## Ready-Made Scripts (use these instead of curl)

Skip the curl commands. Use the pre-built scripts in `05 - Snippets/Scripts/`:

| Script | What It Does |
|---|---|
| `rest-api.ps1` | All-in-one PowerShell tool — inbox, search, read, list |
| `inbox.cmd` | Quick inbox from CMD: `inbox "your note"` |
| `search.cmd` | Quick search from CMD: `search "keyword"` |

**First run:**
```powershell
cd "C:\Users\MarsBase\Documents\Vault_Skills\05 - Snippets\Scripts"
.\rest-api.ps1 list
```

It will ask for your API key once, save it locally, and list your vault files.

**Quick inbox:**
```powershell
.\rest-api.ps1 inbox "Great idea for a plugin"
.\rest-api.ps1 inbox "Meeting Notes::Discussed Q3 roadmap"
```

**Search and read:**
```powershell
.\rest-api.ps1 search "Dataview"
.\rest-api.ps1 read "01 - Plugins/_Plugin Index.md"
```

See [[REST API Automation]] for full documentation and the Python AI agent library.

## Gotchas & Known Issues

- **Auth needs `Bearer` prefix**: v3+ requires `Authorization: Bearer YOUR-KEY`, not just the raw key. The PowerShell script adds this automatically.
- **Content-Type matters**: PUT requests with JSON body need `Content-Type: application/json`. Simple search uses no special Content-Type. The wrong Content-Type will give 400 errors.
- **Plugin must be running**: The API only works when Obsidian is open with the plugin enabled. No Obsidian = no API.
- **Save your API key immediately**: Generate the key and store it somewhere safe (password manager). The key disappears from the settings UI after you close it and cannot be recovered — you can only regenerate a new one.
- **Windows Firewall**: First API call may be silently blocked. Check Windows Defender Firewall → Allow an app through firewall → find Obsidian.
- **Path encoding is strict**: Spaces, parentheses, and special characters in file paths *must* be URL-encoded. This is the #1 source of "file not found" errors.
- **PUT overwrites without warning**: Using PUT on an existing file overwrites it completely. There is no undo. Consider using GET first to read existing content, merge, then PUT.
- **No built-in rate limiting**: If you have many automated writers, you can overwhelm the plugin. Add your own delays (e.g. `time.sleep(0.5)`) in scripts.
- **No WebSocket / real-time events**: The API is request-response only. You can't subscribe to file change events. Polling required for real-time-aware tools.
- **HTTPS cert is self-signed**: If you enable HTTPS, your client will need to accept a self-signed certificate. Add `--insecure` to curl or `verify=False` in Python requests (not recommended for production use).
- **Large responses may lag**: Requesting the full vault listing or a broad search on a 1000+ note vault can take a few seconds.

## Works Well With
- [[Local GPT]] — AI agent can read/write vault notes via REST API
- [[ChatGPT MD]] — complementary (ChatGPT MD is in-vault AI, REST API is external)
- [[QuickAdd]] — QuickAdd for in-app captures, REST API for external captures
- [[Templater]] — REST API can trigger Templater templates via commands
- **MCP Plugin** — uses REST API under the hood to let AI assistants (Claude, GPT) read/write your vault via the Model Context Protocol
- **Obsidian Web Clipper** — can clip directly to vault via REST API instead of the official clipper

## Related Skills
- [[REST API Automation]] — full guide for building automation scripts around the API

## Links
- [GitHub](https://github.com/coddingtonbear/obsidian-local-rest-api)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=obsidian-local-rest-api)
