---
type: plugin
name: Hover Editor
category: UI & Navigation
status: active
complexity: medium
downloads: 464k+
last-verified: 2026-04-30
tags:
  - plugin
  - ui
  - navigation
  - hover
  - preview
  - editing
---

# Hover Editor

> Plugin by nothingislost — upgrades Obsidian's hover preview popups into fully interactive, editable mini-windows. Instead of a read-only preview on link hover, you get a floating editor you can type in, scroll, and pin.

## What It Does

Obsidian's native hover preview shows a read-only preview of a linked note when you hold `Ctrl` and hover over a link. Hover Editor replaces this with a floating **editable pane** — a full Obsidian editor in a popup window.

Key capabilities:
- **Editable hover panes** — modify linked notes without leaving the current note
- **Pinnable popups** — pin a hover pane to keep it open while you work elsewhere
- **Full editor features** — live preview, source mode, embedded queries, all plugins work inside hover panes
- **Resize and drag** — move and resize the popup freely
- **Snap to edges** — pin panes to corners/edges of the screen
- **Stack mode** — multiple hover panes stack as tabs

## When To Use It

- Referencing a note while writing without switching tabs
- Making a quick edit to a linked note without losing your place
- Cross-referencing: reading note A while editing note B simultaneously
- Building networked notes where you frequently jump between connected ideas
- Working with Dataview/Tasks results — click a link in a query result to edit that note in a hover pane

## Minimal Setup

1. **Install**: Community Plugins → search "Hover Editor" by nothingislost → Install & Enable
2. **Use it**: Hold `Ctrl` and hover over any `[[wikilink]]` — the hover pane opens as an editable popup instead of a read-only preview
3. **Pin it**: Click the pin icon in the hover pane header to keep it open
4. **Drag to reposition**: Drag the pane header to move it anywhere on screen

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Trigger delay (ms) | `300` | How long to hold before the popup opens; lower = faster |
| Default view mode | Live Preview | Matches your main editor mode |
| Initial height | `400px` | Starting popup height |
| Initial width | `500px` | Starting popup width |
| Snap to edges | On | Pane snaps to screen edges when dragged near them |
| Use Ctrl key | On | Default — hold Ctrl to trigger hover |
| Pin by default | Off | Off = popup closes when you move away; On = stays open always |
| Show header | On | Shows the note title and controls in the pane header |

## Gotchas & Known Issues

- **Can slow down Obsidian on older hardware** — hover panes are full editors; opening many simultaneously uses significant memory and CPU. Your i5 should handle 2-3 pinned panes without issue; beyond that, close unused ones.
- **Plugin is unmaintained** — nothingislost has been inactive. The plugin works well on current Obsidian versions but may break on future updates. Check GitHub issues before relying on it.
- **Conflicts with some themes** — some themes style hover previews in ways that break Hover Editor's UI. Pure CSS themes (no JS) are generally fine.
- **Scroll lock in hover panes** — sometimes the hover pane scroll locks to the current scroll position. Click inside the pane to refocus.
- **Stacked panes can get buried** — if you open many panes, earlier ones can be obscured. Use Alt+click to cycle through stacked panes.

## Works Well With

- [[Dataview]] — click Dataview query results to edit linked notes in hover panes
- [[Smart Connections]] — open related notes in hover panes while staying in the current note
- [[Kanban]] — hover-edit cards that link to full notes without leaving the board

## Related Skills

- [[Linking & Backlinks Strategy]]
- [[Vault Architecture]]

## Links

- [GitHub](https://github.com/nothingislost/obsidian-hover-editor)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=obsidian-hover-editor)
