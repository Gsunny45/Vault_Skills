---
type: plugin
name: Commander
category: UI & Navigation
status: active
complexity: low
downloads: 468k+
last-verified: 2026-04-30
tags:
  - plugin
  - ui
  - navigation
  - customization
  - commands
---

# Commander

> Plugin by phibr0 — lets you add any Obsidian command as a custom button to any UI location: ribbon, toolbar, status bar, file menu, editor context menu, or title bar.

## What It Does

Commander maps Obsidian commands to custom UI buttons. Any command accessible from the Command Palette can be assigned a custom icon and placed in:
- **Left ribbon** (icon bar on left edge)
- **Editor toolbar** (top of the editor)
- **Status bar** (bottom bar)
- **File menu** (right-click context menu on files)
- **Editor context menu** (right-click in editor)
- **Title bar** (macOS only, menu bar buttons)
- **Workspace page header** (above the note)

Buttons can be conditionally visible: show only in reading mode, only on mobile, only for certain note types, etc.

## When To Use It

- Adding one-click access to frequently used commands without a hotkey
- Putting "Open today's daily note", "New Excalidraw drawing", or "Run QuickAdd" in the ribbon
- Cleaning up the ribbon by removing default icons and replacing with your actual workflow
- Mobile: large touch targets for common actions
- Matching UI buttons to your specific workflow rather than Obsidian's defaults

## Minimal Setup

1. **Install**: Community Plugins → search "Commander" by phibr0 → Install & Enable
2. **Add a button**: Settings → Commander → choose a location (e.g., "Ribbon") → click "+ Add command"
3. **Search for the command** you want (any Command Palette command) → select it
4. **Set an icon** from the Lucide icon set → save
5. The button appears immediately in the chosen UI location

## Example Configurations

### Ribbon buttons to add
| Command | Icon | Notes |
|---|---|---|
| Periodic Notes: Open today's daily note | `calendar-days` | One-click daily note |
| QuickAdd: Run QuickAdd | `zap` | Opens QuickAdd menu |
| Obsidian Git: Create backup | `git-commit` | Manual backup trigger |
| Excalidraw: Create new drawing | `pencil` | New drawing instantly |
| Advanced Canvas: Create new canvas | `layout-dashboard` | New canvas |
| Copilot: Open Copilot Chat | `bot` | Open AI chat panel |

### Ribbon buttons to remove (Obsidian defaults you may not need)
- Graph view (if you don't use it)
- Publish changes (if you don't use Obsidian Publish)
- Sync status (if you don't use Obsidian Sync)

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Hide ribbon commands without icons | Off | Shows all ribbon commands regardless of icon state |
| Visibility | (per button) | Each button has individual visibility: always, mobile only, desktop only, reading mode, editing mode |

## Gotchas & Known Issues

- **Commands from disabled plugins disappear** — if you add a Commander button for a plugin command then disable that plugin, the button silently does nothing. Remove stale buttons after disabling plugins.
- **Icon set is limited to Lucide** — you can't use custom SVG icons, only Lucide icon names.
- **Ribbon order is Commander + Obsidian default** — Commander buttons add to the ribbon alongside Obsidian's default icons. You can't fully control the order of all ribbon items (only Commander-added ones).
- **Some commands need context** — commands that require an active file (like "Lint current file") will fail if triggered from the ribbon when no note is open.

## Works Well With

- [[QuickAdd]] — assign your QuickAdd choices as individual ribbon buttons
- [[Periodic Notes]] — one-click daily note creation in the ribbon
- [[Obsidian Git]] — manual backup button in the status bar
- [[Excalidraw]] — new drawing button always accessible

## Related Skills

- [[Vault Architecture]]
- [[Dashboards]]

## Links

- [GitHub](https://github.com/phibr0/obsidian-commander)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=cmdr)
