---
type: plugin
name: BRAT
category: AI
status: active
complexity: low
downloads: ~690k
last-verified: 2026-04-29
tags:
  - plugin
  - beta-testing
  - updates
  - dev-tools
---

# BRAT (Beta Reviewer's Auto-update Tool)

## What It Does
Installs and auto-updates **beta / unreleased / unlisted** Obsidian plugins and themes directly from GitHub repositories. Bypasses the official Community Plugin store so you can test bleeding-edge features before public release.

**Key capabilities:**
- Add any GitHub repo as a beta plugin or theme with one URL paste
- Auto-updates beta plugins at Obsidian startup (configurable)
- Pin (freeze) a plugin to a specific version tag
- Works with private repos via GitHub Personal Access Token
- Handles the full install lifecycle: download, extract, reload, enable

## When To Use It
- **Beta testing** — a developer asks you to test their plugin pre-release
- **Early access** — you want features before they hit the store
- **Plugins not in the store** — some plugins never get submitted to the official catalog
- **Pinning versions** — need to stay on a specific version for compatibility
- **Theme testing** — unreleased Obsidian themes from GitHub
- **Developer self-testing** — testing your own plugin across environments

**When NOT to use it:** For stable, published plugins already in the Community Plugin store — install those normally.

## Minimal Setup

### 1. Install BRAT
- Obsidian Settings → Community Plugins → Browse → search "BRAT" → Install → Enable
- A new "Obsidian42 - BRAT" section appears in Settings

### 2. Add a Beta Plugin
**Method A — Command Palette (fastest):**
- Copy the GitHub repo URL (e.g., `https://github.com/username/repo-name`)
- `Ctrl+P` → `BRAT: Add a beta plugin for testing`
- Paste URL → click **Add Plugin** → wait for confirmation

**Method B — Settings panel:**
- Settings → Obsidian42 - BRAT → **Add Beta plugin**
- Paste GitHub URL → optionally check **Enable after installing**
- Click **Add Plugin**

### 3. Enable the Beta Plugin
- Settings → Community plugins → **Refresh** button
- Find the new plugin → toggle **Enabled**
- Configure the plugin's own settings

## Key Settings
| Setting | Description |
|---|---|
| **Add Beta Plugin** | Paste a GitHub repo URL to add a beta plugin |
| **Add Beta Theme** | Same concept, for beta themes |
| **Plugin/Theme List** | All tracked plugins with name, version, refresh button, freeze dropdown, remove button |
| **Frozen Version** | Pin a plugin to a specific version tag to prevent auto-updates |
| **Auto-update plugins at startup** | Check for and apply updates on every Obsidian launch |
| **Auto-update themes at startup** | Same as above, for themes |
| **Show Ribbon Button** | Toggle the BRAT icon in the left ribbon bar |
| **GitHub PAT** | Personal Access Token for private repos (stored via SecretStorage) |

### Commands (Command Palette)
| Command | Action |
|---|---|
| `BRAT: Add a beta plugin for testing` | Install a beta plugin via GitHub URL |
| `BRAT: Add a beta theme for testing` | Install a beta theme via GitHub URL |
| `BRAT: Check for updates to all beta plugins and UPDATE` | Force-check and update all |

## Example Config / Usage

### Installing a beta plugin
1. Developer says: "Test my plugin at `https://github.com/someuser/obsidian-cool-plugin`"
2. `Ctrl+P` → `BRAT: Add a beta plugin for testing` → paste URL → Add Plugin
3. Settings → Community plugins → Refresh → Enable "Cool Plugin"
4. Plugin auto-updates when the developer publishes new releases

### Pinning to a specific version
1. In BRAT settings, find the plugin in the list
2. Click the version dropdown → select the version tag (e.g., `1.0.7-preview.1`)
3. Plugin is now frozen and will not auto-update

### Removing a beta plugin
1. Settings → Obsidian42 - BRAT → click **X** next to the plugin
2. Settings → Community plugins → **Disable** and **Remove**

### Testing BRAT itself (meta!)
Add `tfthacker/obsidian42-brat` as a beta plugin to test pre-release versions of BRAT.

## Gotchas & Known Issues
- **Trailing slash bug** — GitHub URLs with a trailing slash (`...repo/`) cause "Repository not found". Remove the trailing slash.
- **Release requirements** — BRAT requires GitHub **Releases** (not just git tags) with `main.js` + `manifest.json` as assets. If missing, install will fail.
- **Auto-enabled plugins may disable after restart** — re-enable manually or re-add via BRAT if this happens.
- **Version picker bug (v2.0.2)** — opening the version dropdown can auto-reinstall the current version. Workaround: use the "Edit" button to type a tag.
- **Token not synced** — GitHub PATs are stored in Obsidian's SecretStorage (not in settings files) and do NOT sync across devices.
- **Obsidian 1.11.4+ required** — BRAT v2.0.0+ requires this minimum version.
- **Duplicate plugin folders** — rare; check `.obsidian/plugins/` manually if sync issues occur.
- **Sandbox recommended** — test beta plugins in a separate vault first to avoid instability.

## Works Well With
- [[ChatGPT MD]] — install its beta versions via BRAT
- Any plugin with a public GitHub repo that publishes pre-releases
- Plugin developers using CI/CD with semantic-release workflows
- [[Obsidian Git]] — backup your vault before testing beta plugins

## Related Skills
- [[Beta Testing Workflow]]
- [[Plugin Development Setup]]

## Links
- [GitHub](https://github.com/TfTHacker/obsidian42-brat)
- [Author's Documentation](https://tfthacker.com/BRAT)
- [Obsidian Plugin Page](https://obsidian.md/plugins?search=brat)
