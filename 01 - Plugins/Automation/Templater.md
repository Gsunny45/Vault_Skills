---
type: plugin
name: Templater
category: Automation
status: active
complexity: medium
downloads: 2M+
last-verified: 2026-04-30
tags:
  - plugin
  - automation
  - templates
  - scripting
---

# Templater

> Plugin by SilentVoid — a powerful template system for Obsidian that goes far beyond core templates. Supports dynamic content via JavaScript expressions, date/time formatting, user prompts, file operations, and custom scripts.

## What It Does

Templater replaces Obsidian's basic `{{date}}` template system with a full-featured templating engine. Templates can include dynamic expressions wrapped in `<% %>` tags that execute when the template is inserted — automatically filling in dates, prompting the user for input, referencing other notes, running scripts, and more.

Two tag types:
- `<% tp.expression %>` — **interpolation**: outputs the result of an expression inline
- `<%* tp.statement %>` — **execution**: runs JavaScript without outputting anything (for logic, loops, conditionals)

## When To Use It

- Auto-filling new note frontmatter (title, creation date, tags, category)
- Creating structured note types: meeting notes, daily journal, project notes, book reviews
- Prompting for metadata when creating a note (e.g., "What is the project name?")
- Inserting current date/time in any format anywhere in a note
- Moving newly created files to the correct folder based on a condition
- Automating repetitive note structures across the vault
- Running custom JavaScript logic in templates (advanced)

## Minimal Setup

1. **Install**: Community Plugins → search "Templater" by SilentVoid → Install & Enable
2. **Set templates folder**: Settings → Templater → Template folder location → `03 - Templates` (or your folder)
3. **Enable automatic trigger**: Settings → Templater → Trigger Templater on new file creation → On (applies templates to new files automatically)
4. **Create a template** in your templates folder, e.g. `03 - Templates/Daily Note.md`:

```markdown
---
type: daily
date: <% tp.date.now("YYYY-MM-DD") %>
day: <% tp.date.now("dddd") %>
---

# <% tp.date.now("dddd, MMMM D YYYY") %>

## Tasks

## Notes
```

5. **Insert a template**: Command Palette → `Templater: Open Insert Template Modal` → pick your template

## Template Functions Reference

### Dates (`tp.date`)
| Expression | Output (example) |
|---|---|
| `<% tp.date.now() %>` | `2026-04-30` |
| `<% tp.date.now("YYYY-MM-DD HH:mm") %>` | `2026-04-30 14:30` |
| `<% tp.date.now("dddd, MMMM D") %>` | `Thursday, April 30` |
| `<% tp.date.now("YYYY-MM-DD", 1) %>` | Tomorrow's date |
| `<% tp.date.now("YYYY-MM-DD", -1) %>` | Yesterday's date |
| `<% tp.date.tomorrow() %>` | Tomorrow (shorthand) |
| `<% tp.date.yesterday() %>` | Yesterday (shorthand) |

### File operations (`tp.file`)
| Expression | Output |
|---|---|
| `<% tp.file.title %>` | Current note's title |
| `<% tp.file.folder() %>` | Current note's folder path |
| `<% tp.file.creation_date() %>` | File creation date |
| `<% tp.file.last_modified_date() %>` | Last modified date |
| `<% tp.file.move("/New/Path/Note.md") %>` | Moves the note to a new path |
| `<% tp.file.rename("New Title") %>` | Renames the current note |

### User prompts (`tp.system`)
| Expression | Behavior |
|---|---|
| `<% await tp.system.prompt("Note title?") %>` | Text input popup |
| `<% await tp.system.suggester(["Option A", "Option B"], ["A", "B"]) %>` | Dropdown suggestion picker |
| `<% await tp.system.clipboard() %>` | Pastes the current clipboard content |

### Web requests (`tp.web`)
| Expression | Behavior |
|---|---|
| `<% await tp.web.random_picture() %>` | Embeds a random Unsplash image URL |
| `<% await tp.web.random_picture("600x400", "mountains") %>` | Targeted Unsplash photo |

## Example Templates

### Meeting Note
```markdown
---
type: meeting
date: <% tp.date.now("YYYY-MM-DD") %>
attendees: 
project: 
tags: [meeting]
---

# Meeting — <% tp.date.now("YYYY-MM-DD") %>

**Project**: <% await tp.system.prompt("Project name?") %>
**Attendees**: 

## Agenda

## Decisions

## Action Items
- [ ] 
```

### New Project Note (with auto-move)
```markdown
<%*
const projectName = await tp.system.prompt("Project name?");
await tp.file.rename(projectName);
await tp.file.move("/Projects/" + projectName + "/" + projectName);
%>
---
type: project
name: <% projectName %>
status: active
created: <% tp.date.now("YYYY-MM-DD") %>
---

# <% projectName %>

## Overview

## Tasks

## Notes
```

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Template folder location | `03 - Templates` | Where Templater looks for `.md` template files |
| Trigger Templater on new file creation | On | Auto-applies template when file matches folder rule |
| Folder templates | (configure per folder) | Assigns a default template to each folder automatically |
| Syntax error style | `Inline` | Shows errors inline rather than crashing the template |
| Enable Templater startup templates | Off | Runs a template on every Obsidian launch — leave off unless needed |
| Enable Script Files | On (if using scripts) | Allows `tp.user.*` custom scripts from a scripts folder |
| Script files folder location | `05 - Snippets/Scripts` | Where Templater looks for `.js` user scripts |

## Gotchas & Known Issues

- **`await` is required for prompts** — `tp.system.prompt()` and `tp.system.suggester()` return Promises. Always use `await`, wrapped in `<%* ... %>` execution tags, not interpolation tags.
- **Execution tags don't output anything** — `<%* someCode %>` runs code silently. Use `<% expression %>` to output values.
- **Template folder notes aren't indexed normally** — if your templates folder is inside your vault, Dataview will try to query template files. Use `FROM` scoping or exclude the templates folder.
- **Auto-trigger only fires once** — Templater applies the folder template to a new note on creation. It won't re-apply if you open an old note.
- **File move happens after template renders** — any `tp.file.move()` call runs at the end. The file starts in its original location, then moves. Don't rely on the final path being correct during template execution.
- **Templater conflicts with core Templates** — disable Obsidian's built-in Templates plugin if you're using Templater; they can conflict when both are enabled with the same hotkey.
- **No undo for destructive actions** — `tp.file.move()` and `tp.file.rename()` can't be undone within Obsidian. Test templates carefully.

## Works Well With

- [[QuickAdd]] — QuickAdd triggers Templater templates via macros; the combination covers most capture workflows
- [[Dataview]] — frontmatter populated by Templater becomes the data Dataview queries
- [[Periodic Notes]] — Periodic Notes uses Templater templates for daily/weekly/monthly notes
- [[Calendar]] — Calendar plugin can trigger Periodic Notes → Templater templates on date click
- [[Kanban]] — create Kanban boards from templates with pre-configured lanes
- [[Natural Language Dates]] — combine NLD date parsing with Templater date expressions

## Related Skills

- [[Template Systems]]
- [[AI Workflows in Obsidian]]

## Links

- [GitHub](https://github.com/SilentVoid13/Templater)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=templater-obsidian)
- [Official Docs](https://silentvoid13.github.io/Templater/)
