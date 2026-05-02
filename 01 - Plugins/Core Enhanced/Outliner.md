---
type: plugin
name: Outliner
category: Core Enhanced
status: active
complexity: low
downloads: 1.2M+
last-verified: 2026-04-30
tags:
  - plugin
  - core-enhanced
  - outlining
  - lists
  - editing
---

# Outliner

> Plugin by vslinko — enhances Obsidian's bullet list editing to behave like a proper outliner (Workflowy, Roam, Logseq). Adds fold/unfold, drag-and-drop reordering, and smart list movement hotkeys.

## What It Does

Obsidian's default list editing is basic — you can Tab to indent, but that's about it. Outliner adds the editing behavior you'd expect from a dedicated outliner app:

- **Fold/unfold lists** — collapse nested bullet points to see only top-level items
- **Move items up/down** — reorder list items with keyboard shortcuts
- **Move items in/out** — increase/decrease indentation level with hotkeys
- **Drag-and-drop** — drag bullet items to reorder or re-nest with mouse/touch
- **Smart Enter behavior** — pressing Enter at end of a bullet creates a new sibling; at the start it inserts above
- **Zoom in** — focus on a specific bullet point and hide all others ("zoom to heading" equivalent for lists)

## When To Use It

- You heavily use nested bullet lists for notes, outlines, or brainstorming
- You want to reorder list items without cut/paste
- Building hierarchical structures (project breakdowns, mind-map-style notes, meeting agendas)
- Anyone who uses Workflowy, Roam, or Logseq-style outlining workflows

## Minimal Setup

1. **Install**: Community Plugins → search "Outliner" by vslinko → Install & Enable
2. That's it — enhanced list behavior activates automatically
3. Assign or verify the hotkeys: Settings → Hotkeys → search "Outliner"

## Hotkeys

| Action | Default Hotkey |
|---|---|
| Move list item up | `Ctrl+Shift+Up` |
| Move list item down | `Ctrl+Shift+Down` |
| Indent list item (increase level) | `Tab` (inside list) |
| Unindent list item (decrease level) | `Shift+Tab` (inside list) |
| Fold list | `Ctrl+Shift+.` |
| Unfold list | `Ctrl+Shift+,` |
| Fold all lists | (assign in Hotkeys) |
| Unfold all lists | (assign in Hotkeys) |

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Stick cursor to content | On | Cursor snaps to text content, not leading spaces |
| Enhanced Tab behavior | On | Tab/Shift+Tab indent/unindent within lists |
| Fold on click on bullet | On | Click the bullet dot to toggle fold/unfold |
| Draw vertical indentation lines | On | Visual guide lines connecting parent to child items |
| Vertical indentation line click action | Fold | Click the line to collapse the whole branch |
| Drag-and-drop | On | Enable mouse drag reordering of list items |
| Debug mode | Off | |

## Example Usage

A raw outline:
```markdown
- Project Alpha
  - Planning
    - Define scope
    - Identify stakeholders
  - Development
    - Backend API
    - Frontend UI
  - Review
    - QA testing
    - Stakeholder demo
```

With Outliner active:
- Click the bullet next to "Planning" → collapses to show only "Planning" (children hidden)
- `Ctrl+Shift+Down` on "Planning" → moves "Planning" block below "Development"
- Drag "Frontend UI" above "Backend API" → reorders without cut/paste

## Gotchas & Known Issues

- **Fold state doesn't persist across sessions** — all lists open unfolded when you reopen a note. There's no "remember fold state" feature.
- **Drag-and-drop can be finicky on small targets** — precise clicking on the tiny drag handle is required. Works better with mouse than touchscreen for small items.
- **Tab behavior may conflict with other plugins** — if Advanced Tables or another plugin also uses Tab, they can conflict in certain contexts. Priority goes to whichever plugin is listed first in community plugins.
- **Doesn't add links between items** — this is not Roam/Logseq. There are no block references or backlinking on individual bullet points. For that, you'd need block-level referencing (not available in standard Obsidian).

## Works Well With

- [[Templater]] — create outline templates with pre-structured bullet hierarchies
- [[QuickAdd]] — quick-capture a bullet to a note, then organize with Outliner
- [[Dataview]] — Dataview queries results as lists; Outliner enhances editing of manually written lists

## Related Skills

- [[Vault Architecture]]
- [[Template Systems]]

## Links

- [GitHub](https://github.com/vslinko/obsidian-outliner)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=obsidian-outliner)
