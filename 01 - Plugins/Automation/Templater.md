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

## Vault Bootstrap Guide (Build From Scratch)

Use these steps when you're building a vault programmatically (e.g., from an AI agent
or script) and need Templater configured WITHOUT opening the Obsidian UI.

### Phase 1 — Download & Install

```bash
VAULT="path/to/your/vault"
TAG=$(curl -s https://api.github.com/repos/SilentVoid13/Templater/releases/latest | grep '"tag_name"' | head -1 | sed 's/.*"tag_name": "\(.*\)".*/\1/')
BASE="https://github.com/SilentVoid13/Templater/releases/download/$TAG"

mkdir -p "$VAULT/.obsidian/plugins/templater-obsidian"
for f in main.js manifest.json styles.css; do
  curl -sL "$BASE/$f" -o "$VAULT/.obsidian/plugins/templater-obsidian/$f"
done
```

### Phase 2 — Register in community-plugins.json

```bash
# If file doesn't exist yet, create with all plugins:
echo '["templater-obsidian"]' > "$VAULT/.obsidian/community-plugins.json"

# If file exists, add "templater-obsidian" to the array (preserve existing entries)
```

### Phase 3 — Write data.json

Copy the **complete** data.json from the Programmatic Configuration section above.
**Every one of the 17 fields is required** — omitting any causes a crash.

### Phase 4 — Create your templates folder and template files

```bash
mkdir -p "$VAULT/03 - Templates"
# Then create your .md template files inside
```

### Phase 5 — Verify

Open the vault in Obsidian. Check: Settings → Community Plugins → Templater should show as enabled.
Open command palette and type "Templater" — the insert template modal should appear.

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

## Programmatic Configuration (data.json)

To pre-configure Templater without manual UI setup, place this `data.json` in
`.obsidian/plugins/templater-obsidian/data.json`. **CRITICAL: Every field below MUST
be present.** Omitting any field causes `Cannot read properties of undefined`
crashes when Templater loads. All 17 fields are required.

```json
{
  "template_folder": "03 - Templates",
  "folder_templates": {},
  "startup_templates": [],
  "trigger_on_file_creation": true,
  "trigger_on_file_creation_ignore_folders": [],
  "auto_jump_to_cursor": true,
  "enable_system_commands": true,
  "shell_path": "",
  "user_scripts_folder": "05 - Snippets/Scripts",
  "enable_folder_templates": true,
  "enable_startup_templates": false,
  "template_hotkeys": {},
  "syntax_highlighting": true,
  "syntax_highlighting_mobile": false,
  "enabled_templates_hotkeys": [],
  "invalid_characters_replacement_mode": "replace",
  "overwrite_mode": false
}
```

| Field | Type | Purpose |
|---|---|---|
| `template_folder` | string | Path to templates folder (e.g., `"03 - Templates"`) |
| `folder_templates` | object | Map folder paths to template files for auto-trigger: `{"Songs/": "03 - Templates/Song Note.md"}` |
| `startup_templates` | array | Templates that run on every Obsidian launch (usually empty) |
| `trigger_on_file_creation` | bool | Auto-apply template when creating new note in a mapped folder |
| `trigger_on_file_creation_ignore_folders` | array | Folders to exclude from auto-trigger |
| `auto_jump_to_cursor` | bool | Jump cursor to `<% tp.file.cursor(0) %>` marker |
| `enable_system_commands` | bool | Allow `tp.system.prompt()` and `tp.system.suggester()` |
| `shell_path` | string | Custom shell for `tp.user` scripts (blank = OS default) |
| `user_scripts_folder` | string | Path to folder with `.js` scripts for `tp.user.*` |
| `enable_folder_templates` | bool | Master switch for per-folder auto-trigger |
| `enable_startup_templates` | bool | Master switch for startup templates |
| `template_hotkeys` | object | Map template paths to hotkey strings |
| `syntax_highlighting` | bool | Highlight `<% %>` tags in editor |
| `syntax_highlighting_mobile` | bool | Same, on mobile (usually off for performance) |
| `enabled_templates_hotkeys` | array | Which template hotkeys are active |
| `invalid_characters_replacement_mode` | string | How to handle invalid filename chars: `"replace"` or `"remove"` |
| `overwrite_mode` | bool | Overwrite existing files with same name (dangerous) |

## Gotchas & Known Issues

- **data.json MUST include every field** — omitting any field causes `Cannot read properties of undefined` crashes. See Programmatic Configuration above for the full 17-field schema.
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
