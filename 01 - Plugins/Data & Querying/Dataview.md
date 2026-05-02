---
type: plugin
name: Dataview
category: Data & Querying
status: active
complexity: high
downloads: 4M+
last-verified: 2026-04-30
tags:
  - plugin
  - data
  - querying
  - dashboard
  - automation
---

# Dataview

> Plugin by blacksmithgu — turns your Obsidian vault into a queryable database. Write queries against your notes' frontmatter, inline fields, tags, and file metadata using a SQL-like language or raw JavaScript.

## What It Does

Dataview lets you query notes like a database. Every note becomes a record; frontmatter keys and inline fields become columns. You write queries in fenced code blocks (` ```dataview `) and Dataview renders the results live whenever the note is open.

Four query types:
- **TABLE** — renders matching notes as a table with chosen columns
- **LIST** — renders a bullet list of matching notes
- **TASK** — renders checkboxes from across the vault, filterable
- **CALENDAR** — renders a calendar view of notes by a date field

Two syntax modes:
- **DQL** (Dataview Query Language) — SQL-like, no JavaScript required
- **DataviewJS** — full JavaScript with `dv.*` API, for complex logic and custom rendering

Dataview is **read-only** — it never modifies your notes. Results re-render on every file change.

## When To Use It

- Building dashboards that pull live data from multiple notes (project status, reading lists, task counts)
- Querying tasks across the vault with date/priority filters
- Auto-generating indexes of notes by tag, folder, or frontmatter field
- Creating MOC (Map of Content) notes that stay current automatically
- Reporting on vault metadata: notes created this week, notes missing a field, overdue items
- Anything you'd do with a spreadsheet if your data lived in markdown files

## Minimal Setup

1. **Install**: Community Plugins → search "Dataview" by blacksmithgu → Install & Enable
2. **Enable JavaScript queries** (recommended): Settings → Dataview → Enable JavaScript queries → On
3. **Enable inline queries** (optional): Settings → Dataview → Enable Inline Queries → On
4. Write a test query in any note:

```dataview
TABLE file.ctime AS "Created", status
FROM "01 - Plugins"
WHERE type = "plugin"
SORT file.name ASC
```

No further config required — Dataview starts indexing your vault immediately on install.

## Query Syntax Reference

### DQL Structure
```
[TABLE | LIST | TASK | CALENDAR] [fields]
FROM [source]
WHERE [condition]
SORT [field] [ASC|DESC]
LIMIT [n]
```

### Sources (`FROM`)
| Source | Example | What it matches |
|---|---|---|
| Folder | `FROM "01 - Plugins"` | All notes in that folder (recursive) |
| Tag | `FROM #plugin` | All notes with that tag |
| Incoming links | `FROM [[Note Name]]` | Notes that link to that note |
| Outgoing links | `FROM outgoing([[Note Name]])` | Notes that note links to |
| Combination | `FROM "Folder" AND #tag` | Intersection of sources |

### Built-in File Fields
| Field | Value |
|---|---|
| `file.name` | Note title (no extension) |
| `file.path` | Full vault path |
| `file.ctime` | Creation date |
| `file.mtime` | Last modified date |
| `file.size` | File size in bytes |
| `file.tags` | Array of all tags |
| `file.inlinks` | Notes linking to this note |
| `file.outlinks` | Notes this note links to |
| Any frontmatter key | Used directly by name |

### Inline Fields
Add metadata anywhere in a note body (not just frontmatter):
```
Status:: In Progress
Due:: 2026-05-15
Priority:: High
```
Reference as `Status`, `Due`, `Priority` in queries — behaves identically to frontmatter.

## Example Queries

### Plugin dashboard (TABLE)
```dataview
TABLE downloads, complexity, status AS "Status"
FROM "01 - Plugins"
WHERE type = "plugin" AND status != "active"
SORT downloads DESC
```

### Tasks due this week (TASK)
```dataview
TASK
FROM "Projects"
WHERE !completed AND due <= date(today) + dur(7 days)
SORT due ASC
```

### Recently modified notes (LIST)
```dataview
LIST file.mtime
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 20
```

### Calendar view of daily notes (CALENDAR)
```dataview
CALENDAR file.ctime
FROM "Journal"
```

### DataviewJS — custom table with logic
````markdown
```dataviewjs
const pages = dv.pages('"01 - Plugins"')
  .where(p => p.status === "documenting")
  .sort(p => p.downloads, "desc");

dv.table(
  ["Plugin", "Downloads", "Category"],
  pages.map(p => [p.file.link, p.downloads, p.category])
);
```
````

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Enable JavaScript queries | On | Required for DataviewJS blocks |
| Enable Inline Queries | On | Lets you write `` `= expression` `` inline in text |
| Inline Query Prefix | `` ` `` (default) | Wraps inline DQL expressions |
| JavaScript Inline Query Prefix | `` `$ `` | Wraps inline JS expressions |
| Render Null as | `-` | Cleaner than empty cells |
| Date format | `YYYY-MM-DD` | Match standard Obsidian date format |
| Date+time format | `YYYY-MM-DD HH:mm` | |
| Automatic View Refreshing | On | Re-renders when vault changes |
| Refresh interval | `2500` ms | Lower = more responsive; raise if CPU spikes |
| Primary column name | `File` | Column header for the note link column |

## Gotchas & Known Issues

- **Frontmatter must be valid YAML** — a bare colon or bad indentation breaks the entire note's metadata. Use the Linter plugin to auto-fix.
- **Queries are read-only** — Dataview never writes to notes. For editable task views, use the Tasks plugin; Dataview handles reporting.
- **DataviewJS can be slow on large vaults** — JS queries run on every refresh. Use `LIMIT` and scope `FROM` to a specific folder wherever possible.
- **Inline fields require "Enable Inline Queries" to be on** — `key:: value` syntax won't index otherwise.
- **`FROM ""` queries the entire vault** — can lag significantly on 500+ note vaults. Always scope with a folder path when possible.
- **Date comparisons need `date()` wrapper** — `WHERE due <= "2026-05-01"` fails silently. Use `WHERE due <= date("2026-05-01")` or `date(today)`.
- **Tags in FROM must include `#`** — `FROM "Projects"` is a folder path; `FROM #projects` is a tag.
- **Results don't persist** — Dataview only renders when the note is open. There's no cached output to read externally.
- **Plugin is in maintenance mode** — blacksmithgu has stepped back. Bug fixes are slow; the community fork **Dataview Fixes** (installable via BRAT) patches many known issues.

## Works Well With

- [[Homepage]] — pin a Dataview dashboard as your vault home screen
- [[Templater]] — auto-populate frontmatter fields that Dataview queries against
- [[QuickAdd]] — capture new notes with consistent frontmatter via QuickAdd, query them with Dataview
- [[Tasks]] — Tasks plugin handles task editing and recurring tasks; Dataview handles custom reporting queries
- [[Calendar]] — use CALENDAR queries alongside the Calendar plugin for dual date views
- [[Periodic Notes]] — query daily/weekly note data with Dataview TABLE queries
- [[Kanban]] — surface task metadata and counts alongside Kanban boards

## Related Skills

- [[Dashboards]]
- [[Dataview Dashboard Patterns]]

## Links

- [GitHub](https://github.com/blacksmithgu/obsidian-dataview)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=dataview)
- [Official Docs](https://blacksmithgu.github.io/obsidian-dataview/)
