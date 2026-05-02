---
type: plugin
name: Editing Toolbar
category: Writing & Editing
status: active
complexity: low
downloads: 1.3M+
last-verified: 2026-04-30
tags:
  - plugin
  - writing
  - editing
  - toolbar
  - formatting
---

# Editing Toolbar

> Plugin by cumany — adds a rich-text-style formatting toolbar to Obsidian's editor. Click buttons to apply bold, italic, headings, tables, code blocks, and dozens more formatting options without memorizing Markdown syntax.

## What It Does

Editing Toolbar adds a persistent or context-sensitive formatting bar to Obsidian, similar to toolbars in Word or Google Docs. Select text → toolbar buttons apply Markdown formatting to the selection instantly. Works in both Source and Live Preview modes.

Features:
- **50+ formatting commands** — bold, italic, strikethrough, highlight, headings (H1-H6), quote, code, code block, table insert, HR, links, comments, and more
- **Three toolbar positions**: top of editor, following cursor (floating), or fixed bottom
- **Custom buttons** — add any Obsidian command to the toolbar
- **Font selector** — quick font switching directly in the toolbar
- **Context menu commands** — right-click to apply formatting without reaching the toolbar
- **Mobile support** — works on mobile Obsidian with touch-friendly button sizing

## When To Use It

- You're new to Markdown and want visual formatting buttons
- You frequently format text with less common options (highlight, superscript, underline, comments)
- You prefer click-to-format over memorizing hotkeys
- Touchscreen use — tapping toolbar buttons is faster than reaching for a keyboard shortcut
- Quick table insertion with one click

## Minimal Setup

1. **Install**: Community Plugins → search "Editing Toolbar" by cumany → Install & Enable
2. The toolbar appears automatically at the top of the editor
3. Adjust position: Settings → Editing Toolbar → Toolbar Position → choose Top / Following cursor / Fixed bottom

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Toolbar position | Top | Persistent at editor top. "Following cursor" = appears near selected text only. |
| Enable mini toolbar | On | Shows a compact toolbar when text is selected, even with the main toolbar hidden |
| Show toolbar in reading mode | Off | Toolbar is for editing; unnecessary in reading mode |
| Font list | (add your fonts) | Fonts available in the toolbar's font selector dropdown |
| Enable context menu | On | Adds formatting options to right-click menu |

## Customizing the Toolbar

Settings → Editing Toolbar → Manage Toolbar Commands:
- Drag to reorder buttons
- Click the eye icon to hide buttons you don't use
- Click "+ Add command" to add any Obsidian command as a toolbar button
- Changes apply immediately

**Recommended lean toolbar** (remove rarely used items):
Keep: H1, H2, H3, Bold, Italic, Highlight, Strikethrough, Code, Code block, Quote, Bullet list, Numbered list, Table, Link, HR
Remove: Underline (not standard Markdown), superscript, subscript (unless you use them)

## Gotchas & Known Issues

- **Toolbar can overlap content on small screens** — with the "top" position on a narrow window, the toolbar may push the first line of content down. Use "following cursor" mode if this is an issue.
- **Custom command buttons require the command to exist** — if a plugin providing a custom command is disabled, its toolbar button will fail silently.
- **Font selector only changes CSS font class** — it doesn't embed font files. Only fonts installed on your system are available.
- **Some formatting commands duplicate hotkeys** — if you assign a hotkey to the same action as a toolbar button, both work independently.

## Works Well With

- [[Style Settings]] + [[Minimal Theme Settings]] — a well-configured theme makes the toolbar look polished
- [[Advanced Tables]] — click the table button to insert a table, then use Advanced Tables for editing it
- [[Dataview]] — quickly insert code blocks for Dataview queries via toolbar button

## Related Skills

- [[Vault Architecture]]

## Links

- [GitHub](https://github.com/cumany/obsidian-editing-toolbar)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=editing-toolbar)
