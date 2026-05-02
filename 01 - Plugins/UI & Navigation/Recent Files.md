---
type: plugin
name: Recent Files
category: UI & Navigation
status: active
complexity: low
downloads: 987k+
last-verified: 2026-04-30
tags:
  - plugin
  - ui
  - navigation
  - recent
---

# Recent Files

> Plugin by tgrosinger — adds a sidebar panel showing your most recently opened or modified files. One-click access to the last N files you worked on.

## What It Does

Recent Files adds a persistent list of recently accessed notes in the sidebar. Unlike Obsidian's built-in Quick Switcher (which searches by name), Recent Files just shows what you had open — ordered by last access time.

Simple and low-friction: no configuration required, one-click navigation.

## When To Use It

- Jumping back to a note you were editing 5 minutes ago without searching
- Working across multiple notes in a session and needing quick context switches
- Replacing the "recently opened" pattern you'd get from a traditional file manager
- Low-RAM alternative to keeping many tabs open

## Minimal Setup

1. **Install**: Community Plugins → search "Recent Files" by tgrosinger → Install & Enable
2. **Open the panel**: Ribbon → clock icon, or Command Palette → "Recent Files: Open Recent Files panel"
3. The panel shows your last N files automatically — no configuration needed

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Maximum number of recent files | `20` | Default 10; raise if you switch between many files |
| Open on startup | On | Keeps the panel available from session start |

## Gotchas & Known Issues

- **List resets on Obsidian restart (partially)** — recent files are persisted, but the order may differ slightly after restart depending on what Obsidian auto-opens.
- **Shows all file types** — images, PDFs, and canvas files appear alongside notes. Scroll past them if you only want markdown notes.
- **Doesn't filter by vault** — if you have multiple vaults, the list is per-vault already (Obsidian is vault-scoped), so no issue there.

## Works Well With

- [[Homepage]] — homepage as the landing page, Recent Files as the quick-navigation panel
- [[Omnisearch]] — Recent Files for last-accessed notes; Omnisearch for content search

## Related Skills

- [[Vault Architecture]]

## Links

- [GitHub](https://github.com/tgrosinger/recent-files-obsidian)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=recent-files-obsidian)
