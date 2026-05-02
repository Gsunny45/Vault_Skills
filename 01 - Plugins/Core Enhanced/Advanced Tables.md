---
type: plugin
name: Advanced Tables
category: Core Enhanced
status: active
complexity: low
downloads: 2.7M+
last-verified: 2026-04-30
tags:
  - plugin
  - core-enhanced
  - tables
  - markdown
  - editing
---

# Advanced Tables

> Plugin by tgrosinger — makes Markdown table editing tolerable. Auto-formats tables as you type, handles column alignment, and adds navigation hotkeys so you never have to count pipe characters manually.

## What It Does

Obsidian's native table support requires you to manually align pipe characters and manage column widths. Advanced Tables fixes this: every time you press Tab or Enter inside a table, the plugin auto-formats all columns to consistent widths. It also adds a table toolbar and formula support.

Key features:
- **Auto-format on Tab/Enter** — columns snap to consistent widths automatically
- **Tab navigation** — Tab moves to the next cell; Shift+Tab moves back; Enter goes to the next row
- **New row/column insertion** — Command Palette commands to insert rows and columns
- **Column alignment** — set left, center, or right alignment per column
- **Sort by column** — sort table rows alphabetically or numerically
- **Formula support** — basic spreadsheet-style formulas in cells (`@SUM`, `@AVERAGE`, etc.)
- **Toolbar** — floating toolbar with table operations when cursor is in a table

## When To Use It

- Editing any Markdown table (it's active whenever you're in a table cell)
- Building the plugin index, skill index, or any structured table in your vault
- Sorting lists by a column without manually rearranging rows
- Light calculations in table cells (totals, averages)

This plugin activates automatically whenever your cursor enters a Markdown table — no manual trigger needed.

## Minimal Setup

1. **Install**: Community Plugins → search "Advanced Tables" by tgrosinger → Install & Enable
2. That's it — the plugin activates automatically when your cursor is inside any `|table|` row
3. **Test it**: create a table, press Tab — columns should auto-align

```markdown
| Plugin | Downloads | Status |
|---|---|---|
| Dataview | 4M+ | active |
```
Press Tab inside the table and it reformats to aligned widths automatically.

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Enable table editor | On | Master toggle — leave on |
| Pad cell width | On | Aligns all columns to equal width for readability |
| Align columns | On | Respects `:---:` alignment markers |
| Show icon in toolbar | On | Adds table icon to Obsidian's toolbar |

## Navigation Hotkeys

| Key | Action |
|---|---|
| `Tab` | Next cell (auto-creates new row at end of table) |
| `Shift+Tab` | Previous cell |
| `Enter` | New row below current row |
| `Ctrl+Shift+D` | Open table control sidebar |

## Table Control Sidebar Commands

Open via Command Palette → "Advanced Tables: Open Table Control" or the toolbar icon:

| Command | Action |
|---|---|
| Align left / center / right | Set column alignment |
| Insert row above | Add row above cursor |
| Insert row below | Add row below cursor |
| Insert column left | Add column to the left |
| Insert column right | Add column to the right |
| Delete row | Remove current row |
| Delete column | Remove current column |
| Sort ascending / descending | Sort all rows by current column |
| Evaluate formulas | Run `@FORMULA` cells |
| Format table | Re-format all columns to aligned widths |

## Formula Syntax

Advanced Tables supports basic spreadsheet formulas in cells:

| Formula | Result |
|---|---|
| `@SUM(@above)` | Sum of all cells in column above current cell |
| `@AVERAGE(@above)` | Average of column above |
| `@MIN(@above)` / `@MAX(@above)` | Min/max of column |
| Cell references | `@R1C2` = Row 1, Column 2 |

Example:
```
| Item | Cost |
|---|---|
| Bread | 2.50 |
| Milk | 1.80 |
| Eggs | 3.20 |
| **Total** | @SUM(@above) |
```
Command Palette → "Advanced Tables: Evaluate formulas" → replaces `@SUM(@above)` with `7.50`.

## Gotchas & Known Issues

- **Live Preview vs Source mode** — Advanced Tables works in both Live Preview and Source mode. Behavior is slightly different in each; Source mode gives the most predictable Tab navigation.
- **Formula evaluation is manual** — formulas don't auto-recalculate. You must run "Evaluate formulas" after changing values.
- **Large tables format slowly** — a 50+ column table may have a brief lag on Tab. Not a common scenario but worth noting.
- **Conflicts with Vim mode** — if you use Obsidian's Vim key binding mode, Tab in insert mode may conflict. Check hotkey settings.
- **Tables must use pipe syntax** — the plugin only works with standard Markdown pipe tables (`| col |`). HTML tables or special formats aren't supported.

## Works Well With

- [[Dataview]] — Dataview renders query results as tables; Advanced Tables helps you build and edit static tables alongside
- [[Linter]] — Linter can auto-format tables too; Advanced Tables is more interactive, Linter is more thorough on save
- [[Editing Toolbar]] — Editing Toolbar includes a table insertion button that Advanced Tables then takes over for editing

## Related Skills

- [[Vault Architecture]]

## Links

- [GitHub](https://github.com/tgrosinger/advanced-tables-obsidian)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=table-editor-obsidian)
