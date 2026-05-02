---
type: skill
name: Template Systems
category: Automation
difficulty: beginner
tags:
  - skill
  - templates
  - templater
  - quickadd
  - automation
---

# Template Systems

## What This Skill Covers
How to design, build, and use note templates in Obsidian to enforce frontmatter consistency, speed up note creation, and automate repetitive structures. Covers Templater, QuickAdd capture templates, and plain markdown template patterns.

## When You Need This
- You create the same type of note repeatedly (song notes, project notes, daily logs)
- You want frontmatter fields to be consistent across all notes of the same type
- You want to create notes with one command instead of copy-pasting from an existing note
- You're building a vault for a specific use case and need structured note creation

## Core Concepts

### Templates Are Skeleton Notes
A template is a regular markdown file with placeholder content that gets filled in when you create a new note. Templates can include:
- **Pre-filled frontmatter** with default values
- **Placeholder text** to guide what to write
- **Template variables** (`{{title}}`, `{{date}}`) that auto-fill on creation
- **Scripts** (Templater) that run logic when the note is created

### Two Template Engines

| Engine | How It Works | Best For |
|--------|-------------|----------|
| **Core Templates** | Settings → Templates → Template folder location. Uses `{{title}}`, `{{date}}` variables only. | Simple, no-plugin-needed templates |
| **Templater** | Community plugin. Supports JavaScript snippets, file creation prompts, complex logic. | Dynamic templates, computed fields, multi-file creation |

Templater is recommended for anything beyond basic placeholder filling. It's in the Plugin Index at [[Templater]].

### Three Template Patterns

| Pattern | Tool | Use Case |
|---------|------|----------|
| **Core template** | Obsidian core | Static frontmatter + section headers |
| **Templater dynamic** | Templater plugin | Auto-computed fields, prompts for input |
| **QuickAdd capture** | QuickAdd plugin | Rapid capture to inbox with preset fields |

## Step-by-Step

### Step 1 — Create a Templates Folder
```
Fat_Lady_Sings/
└── Templates/
    ├── tpl-song.md
    ├── tpl-album.md
    └── tpl-playlist.md
```
Prefix template files with `tpl-` to distinguish them from content notes.

### Step 2 — Write a Template with Frontmatter
```markdown
---
type: song
title: {{title}}
artist:
album:
genre: []
mood:
bpm:
year:
rating:
duration:
created: {{date}}
---

# {{title}}

## Notes

```

Variables like `{{title}}` and `{{date}}` are filled automatically on creation. Empty fields (like `artist:`) prompt you to fill them in.

### Step 3 — Set the Template Folder (Core)
```
Settings → Templates → Template folder location → Templates
Settings → Templates → Date format → YYYY-MM-DD
```
Then `Ctrl+P` → `Templates: Insert template` to pick and insert.

### Step 4 — Set Up Templater (Recommended)
1. Install Templater from Community Plugins
2. `Settings → Templater → Template folder → Templates`
3. `Settings → Templater → Trigger Templater on new file creation → On`
4. Create a template with Templater syntax (see below)

### Step 5 — Write a Templater Dynamic Template
```markdown
---
type: song
title: <% tp.file.title %>
artist: <% await tp.system.prompt("Artist:") %>
album: <% await tp.system.prompt("Album:") %>
genre: []
mood: <% await tp.system.suggester(["happy", "melancholic", "energetic", "calm", "dark"], ["happy", "melancholic", "energetic", "calm", "dark"]) %>
bpm: <% await tp.system.prompt("BPM:") %>
year: <% await tp.system.prompt("Year:", moment().format("YYYY")) %>
rating:
duration:
created: <% tp.date.now("YYYY-MM-DD") %>
---
```
Templater prompts for input on creation, with type-ahead suggestions for mood.

### Step 6 — QuickAdd Capture for Rapid Entry
1. Install QuickAdd
2. Settings → QuickAdd → Add Choice → type "Capture" → name "Quick Song"
3. Format:
```
---
type: song
title: {{VALUE:Title}}
artist: {{VALUE:Artist}}
---
```
4. Assign hotkey to the capture command (e.g., `Ctrl+Shift+S`)

## Example — Song Template (Copy-Paste Ready)

Save as `Templates/tpl-song.md`:

```markdown
---
type: song
title: <% tp.file.title %>
artist:
album:
genre: []
mood:
bpm:
year: <% moment().format("YYYY") %>
rating:
duration:
created: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

## Lyrics

```

## Example — Playlist Template (Copy-Paste Ready)

Save as `Templates/tpl-playlist.md`:

```markdown
---
type: playlist
title: <% tp.file.title %>
mood:
genre: []
created: <% tp.date.now("YYYY-MM-DD") %>
songs: []
---

# <% tp.file.title %>

## Tracklist

-

## Notes

```

## Common Mistakes
- **No frontmatter in templates** — without it, Dataview can't query the notes. Always include `type:` at minimum.
- **Templates folder not set** — templates won't appear in the picker. Check Settings → Templates → Template folder location.
- **Templater not triggered** — ensure `Trigger Templater on new file creation` is ON in Templater settings.
- **Overly complex templates** — too many template prompts makes creation tedious. Prompt only for fields you can't auto-fill.
- **No QuickAdd for mobile** — QuickAdd capture works on mobile; Templater dynamic prompts sometimes don't. Use QuickAdd as your mobile fallback.

## Related Skills
- [[Vault Architecture]] — design frontmatter schemas that templates enforce
- [[Dashboards]] — query template-created notes with Dataview

## Related Plugins
- [[Templater]] — dynamic template engine with prompts and scripts
- [[QuickAdd]] — rapid capture templates with field prompts
- [[Dataview]] — query the consistent frontmatter that templates produce
