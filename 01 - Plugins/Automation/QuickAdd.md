---
type: plugin
name: QuickAdd
category: Automation
status: active
complexity: medium
downloads: 1M+
last-verified: 2026-04-30
tags:
  - plugin
  - automation
  - capture
  - macros
  - workflow
---

# QuickAdd

> Plugin by chhoumann — a fast capture and automation system for Obsidian. Create macros, template-based note creation, and quick-capture workflows accessible from a single command or hotkey.

## What It Does

QuickAdd gives you a command palette entry that triggers configurable **choices** — each choice is a mini-workflow that can capture text, create a note from a template, run a macro, or chain multiple actions together. It's the glue layer between Templater, Dataview, and your actual workflow.

Four choice types:
- **Template** — creates a new note from a Templater template (with optional folder routing and naming logic)
- **Capture** — appends or prepends text to an existing note (great for inbox/log patterns)
- **Macro** — chains multiple choices and JavaScript commands into a single action
- **Multi** — groups multiple choices under one named menu

## When To Use It

- Quick-capturing ideas/tasks to an inbox note without opening a full new note
- Creating structured notes (meeting notes, book notes, project notes) from a single hotkey
- Routing new notes to the right folder automatically based on template choice
- Building daily capture flows: "Log a task", "Add a book", "Save a link"
- Running multi-step workflows triggered by a single command
- Anything you'd otherwise do by: open folder → new note → rename → add frontmatter → move

## Minimal Setup

1. **Install**: Community Plugins → search "QuickAdd" by chhoumann → Install & Enable
2. **Open QuickAdd settings**: Settings → QuickAdd → Manage Macros and Choices
3. **Create your first Capture choice** (inbox example):
   - Click **Add Choice** → name it "📥 Inbox" → select type **Capture** → click ⚙️ (configure)
   - File name: `00 - Inbox.md` (or your inbox note path)
   - Capture format: `- [ ] {{VALUE}} — {{DATE:YYYY-MM-DD}}`
   - Enable: "Capture to active file" = Off; "Prepend to file" = On
4. **Add it to the command palette**: Click the lightning bolt ⚡ next to the choice
5. **Assign a hotkey**: Settings → Hotkeys → search "QuickAdd: Run QuickAdd" → assign e.g. `Ctrl+Shift+A`

Run it: press the hotkey → type a task → Enter → it appends to your inbox.

## Choice Configuration Reference

### Template Choice Settings
| Option | What it does |
|---|---|
| Template path | The `.md` file in your templates folder to use |
| File name format | Name for the new note (supports `{{VALUE}}`, `{{DATE}}`, `{{NAME}}`) |
| Create in folder | Where to put the new note |
| Open new note | Whether to open the created note immediately |
| Increment file name | Auto-appends a number if the file already exists |

### Capture Choice Settings
| Option | What it does |
|---|---|
| File name | Path of the note to append/prepend to (supports `{{DATE}}` for daily notes) |
| Capture format | The text to insert. Use `{{VALUE}}` for user input, `{{DATE}}` for today |
| Prepend vs Append | Whether to add to the top or bottom of the file |
| Capture to active file | Inserts into whatever note is currently open |
| Task | Wraps the captured text in `- [ ] ` automatically |

### Template Variables
| Variable | Output |
|---|---|
| `{{VALUE}}` | Prompts the user for input |
| `{{VALUE:<default>}}` | Prompt with a pre-filled default |
| `{{DATE}}` | Today's date (default: `YYYY-MM-DD`) |
| `{{DATE:format}}` | Date with custom format e.g. `{{DATE:dddd, MMMM D}}` |
| `{{NAME}}` | The choice name |
| `{{CLIPBOARD}}` | Current clipboard contents |

## Example Choices

### Daily log capture
- Type: Capture
- File: `Journal/{{DATE:YYYY-MM-DD}}.md` (appends to today's daily note)
- Format: `- {{VALUE}}`
- Append: On

### New book note
- Type: Template
- Template: `03 - Templates/Book Note.md`
- File name: `{{VALUE}}` (prompts for book title)
- Folder: `Reference/Books/`
- Open: On

### Macro: New meeting note + open + focus
- Type: Macro
- Steps: Template choice (meeting template) → Wait → Open file → Focus editor

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Sort choices | (drag to order) | Top choices appear first in the QuickAdd menu |
| Format syntax | `{{VALUE}}`, `{{DATE}}` | Built-in; Templater syntax also works inside templates |
| Ask before clearing | On | Safety prompt before running destructive macro steps |

## Gotchas & Known Issues

- **Capture to daily note requires the file to exist** — if the daily note doesn't exist yet, Capture will create it (without your Periodic Notes template). Use Periodic Notes + Templater to create daily notes first, then Capture into them.
- **`{{VALUE}}` only prompts once** — if you use `{{VALUE}}` multiple times in a format string, each usage gets the same value. Use a Macro with separate prompts for multiple distinct inputs.
- **Template path is case-sensitive** — make sure the path in QuickAdd matches the exact folder/file casing in your vault.
- **Lightning bolt adds to command palette only** — the ⚡ button registers a `QuickAdd: <choice name>` command. You still need to bind a hotkey to it separately.
- **Macros can run JS** — powerful but easy to break things. Test macros in a dummy vault first.
- **Order matters in Multi choices** — choices in a Multi menu run in the order you arrange them. Drag to reorder.

## Works Well With

- [[Templater]] — QuickAdd triggers Templater templates; together they cover almost all note creation workflows
- [[Dataview]] — capture notes with consistent frontmatter via QuickAdd, query them with Dataview
- [[Periodic Notes]] — QuickAdd capture flows that write into daily/weekly notes
- [[Kanban]] — add cards to a Kanban board via QuickAdd capture
- [[Tasks]] — quick-capture tasks into a centralized task note

## Related Skills

- [[Template Systems]]
- [[Kanban Workflows]]

## Links

- [GitHub](https://github.com/chhoumann/quickadd)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=quickadd)
- [Official Docs](https://quickadd.obsidian.guide/)
