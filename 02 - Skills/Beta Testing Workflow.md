---
type: skill
name: Beta Testing Workflow
category: AI
difficulty: intermediate
tags:
  - skill
  - beta-testing
  - brat
  - plugin-dev
---

# Beta Testing Workflow

## What This Skill Covers
How to safely install, test, manage, and remove beta/unreleased Obsidian plugins and themes using BRAT (Beta Reviewer's Auto-update Tool). Includes sandboxing strategy, version pinning, bug reporting workflow, and cleanup.

## When You Need This
- A plugin developer asks you to test their pre-release plugin or theme
- You want early access to features before public release
- You need to pin a plugin to a specific version to avoid breaking changes
- You develop your own plugins and need to test across vaults
- You want to evaluate a plugin not yet in the Community Store

## Core Concepts

### How BRAT Works
BRAT sidesteps the official Community Plugin store. Given a GitHub repo URL, it:
1. Fetches the latest **GitHub Release** (not git tag — must be an actual Release with assets)
2. Downloads `main.js`, `manifest.json`, `styles.css` from the release assets
3. Places them in `.obsidian/plugins/<repo-name>/`
4. On startup, checks for newer releases and auto-updates (configurable)

### Beta vs. Stable
| Aspect | Stable Plugin | Beta Plugin |
|---|---|---|
| Source | Community Store | GitHub repo via BRAT |
| Review | Passed Obsidian review | May be unreviewed, unstable |
| Updates | Manual or via community plugin updater | Auto-update at startup (optional) |
| Risk | Low | Moderate — could break vault |
| Support | Plugin author + community | Plugin author directly |

### GitHub Release Requirements
BRAT requires GitHub Releases with assets attached. Not all repos publish releases correctly:
- `manifest.json` — **required** (plugin metadata, version, minAppVersion)
- `main.js` — **required** (compiled plugin code)
- `styles.css` — **optional** (plugin styling)

## Step-by-Step

### Step 1 — Sandbox first (recommended)
Never test beta plugins in your main vault. Use a separate test vault:

1. Create a dedicated test vault: `Vault_BetaTesting` or similar
2. Install **only** BRAT in that vault initially
3. Install beta plugins there first, verify stability
4. Only promote to your main vault after basic confidence check

Testing in your main vault is risky — beta plugins can corrupt settings, conflict with existing plugins, or cause startup crashes.

### Step 2 — Install BRAT
If not already installed:
- Settings → Community Plugins → Browse → search "BRAT" → Install → Enable
- New section "Obsidian42 - BRAT" appears in Settings

### Step 3 — Add a beta plugin
**Method A — Command Palette (fastest):**
1. Copy the GitHub repo URL (e.g., `https://github.com/username/obsidian-plugin-name`)
2. `Ctrl+P` → `BRAT: Add a beta plugin for testing`
3. Paste URL → click **Add Plugin**
4. Wait for confirmation — BRAT downloads and extracts

**Method B — Settings:**
1. Settings → Obsidian42 - BRAT → **Add Beta plugin**
2. Paste GitHub URL → optionally check **Enable after installing** (starts disabled by default in BRAT v2+)
3. Click **Add Plugin**

### Step 4 — Enable and configure
1. Settings → Community plugins → click **Refresh** button
2. Find the new plugin in the list → toggle **Enabled**
3. Configure the plugin's native settings as needed
4. If the plugin doesn't appear, check `.obsidian/plugins/` folder exists and has the right contents

### Step 5 — Test systematically
- **Test basic functionality** — does it load without errors? Do core features work?
- **Test edge cases** — empty vault, vault with many notes, with your plugin stack
- **Test corner cases** — what happens when other plugins conflict?
- **Test disable/re-enable cycle** — toggle the plugin off and on
- **Test across restarts** — reopen Obsidian, confirm plugin loads and works
- **Report issues** — see Bug Reporting section below

### Step 6 — Pin a version (if needed)
If a new release breaks something or changes behavior you rely on:
1. Settings → Obsidian42 - BRAT → find the plugin in the list
2. Click the version dropdown → select a specific version tag (e.g., `1.0.7-preview.1`)
3. Plugin is now **frozen** — no auto-updates until you unpin

### Step 7 — Remove a beta plugin
When testing is complete or the plugin is no longer needed:
1. Settings → Obsidian42 - BRAT → click **X** next to the plugin to remove from BRAT
2. Settings → Community plugins → **Disable** the plugin
3. Settings → Community plugins → **Remove** the plugin (trashes the folder)
4. (Optional) Manually delete `.obsidian/plugins/<plugin-name>/` if remove fails

## Beta Testing Workflows

### Workflow A: Quick Test (single plugin, short eval)
```
1. Sandbox vault → install BRAT
2. Add beta plugin → enable → test core features (15 min)
3. Report findings or approve promotion to main vault
4. Remove from sandbox when done
```

### Workflow B: Multi-Plugin Test Suite (beta batch)
```
1. Sandbox vault → install BRAT
2. Add ALL beta plugins at once
3. Enable one at a time, test isolation
4. Test interactions with all enabled (stress test)
5. Document per-plugin findings
6. Promote stable ones, drop unstable ones
```

### Workflow C: Version Pinning (production stability)
```
1. Install beta plugin in main vault (after sandbox clearance)
2. Pin to current working version
3. Wait for stable release
4. Unpin → update to stable → remove from BRAT
```

### Workflow D: Self-Testing (plugin developer)
```
1. Create a `.obsidian/plugins/<your-plugin>/` folder with symlinks to your build output
2. Or use BRAT to install from your GitHub releases during CI
3. Test across environments (Windows/Mac, different plugin stacks)
4. Use `BRAT: Check for updates to all beta plugins and UPDATE` to pull latest build
```

## Bug Reporting Template

When reporting issues to plugin developers, include:

```
**Plugin:** [name + version]
**Obsidian:** [version]
**OS:** [Windows 11 / macOS / Linux]
**BRAT version:** [e.g., 2.0.2]

**Steps to reproduce:**
1.

**Expected behavior:**

**Actual behavior:**

**Screenshot/Log:** [if applicable]
**Does disabling other plugins fix it?** [yes/no — indicates conflict]
```

Developer console logs: `Ctrl+Shift+I` → Console tab. Look for red errors. Screenshot them.

## Common Mistakes

- **Trailing slash in URL** — `https://github.com/username/repo/` fails with "Repository not found". Remove trailing slash.
- **Git tags not enough** — BRAT requires GitHub **Releases** with assets, not just git tags. If `main.js` + `manifest.json` aren't release assets, install fails.
- **Skipping sandbox** — testing beta plugins in your main vault risks data loss or vault corruption. Always sandbox first.
- **Not refreshing plugin list** — after adding via BRAT, you must click **Refresh** in Community Plugins to see the new plugin.
- **Auto-enabled plugins may disable** — some beta plugins disable after restart. Re-enable manually or re-add via BRAT.
- **Version picker bug (BRAT v2.0.2)** — opening the version dropdown can auto-reinstall the current version. Use the "Edit" button to type a tag instead.
- **Forgot to backup** — take a vault backup before testing any beta plugin. Use Obsidian Git or manual copy.
- **Token not synced** — GitHub PATs for private repos are stored in Obsidian SecretStorage and do NOT sync across devices.

## Related Skills
- [[Plugin Development Setup]]

## Related Plugins
- [[BRAT]]
- [[Obsidian Git]]
- [[Importer]]
