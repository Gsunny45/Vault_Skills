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

> Plugin by blacksmithgu — turns your Obsidian vault into a queryable database. Write queries against your notes' frontmatter, inline fields, tags, and file metadata using a SQL-like language or raw JavaScript. **v0.5.70** · 806 commits · MIT license.

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

**Security note:** DQL queries are sandboxed and **read-only** — they cannot modify your notes. DataviewJS runs with full plugin-level access and **can** modify, delete, or create files and make network calls. Only enable DataviewJS if you trust the queries you run. Results re-render on every file change.

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

## Vault Bootstrap Guide (Build From Scratch)

Use these steps when you're building a vault programmatically and need Dataview
configured WITHOUT opening the Obsidian UI.

### Phase 1 — Download & Install

```bash
VAULT="path/to/your/vault"
TAG=$(curl -s https://api.github.com/repos/blacksmithgu/obsidian-dataview/releases/latest | grep '"tag_name"' | head -1 | sed 's/.*"tag_name": "\(.*\)".*/\1/')
BASE="https://github.com/blacksmithgu/obsidian-dataview/releases/download/$TAG"

mkdir -p "$VAULT/.obsidian/plugins/dataview"
for f in main.js manifest.json styles.css; do
  curl -sL "$BASE/$f" -o "$VAULT/.obsidian/plugins/dataview/$f"
done
```

### Phase 2 — Register in community-plugins.json

```bash
# Add "dataview" to the community-plugins.json array alongside other plugins
```

### Phase 3 — Write data.json

Copy the **complete** data.json from the Programmatic Configuration section above.
**Every one of the 16 fields is required** — omitting any causes a crash.

### Phase 4 — Verify

Open the vault in Obsidian. Create a test note with this query block:
````markdown
```dataview
TABLE file.ctime
FROM ""
LIMIT 5
```
````
You should see a table of your 5 newest notes. If you see a blank block or an error,
re-check data.json for missing fields.

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

**Hidden inline fields** wrap the key in parentheses to suppress display while keeping it queryable:
```
(priority:: high)
(draft:: true)
```
These won't show in Reading view but are fully indexable by Dataview queries.

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

## Programmatic Configuration (data.json)

To pre-configure Dataview without manual UI setup, place this `data.json` in
`.obsidian/plugins/dataview/data.json`. **CRITICAL: Every field below MUST
be present.** Omitting any field causes `Cannot read properties of undefined`
crashes when Dataview loads. All 16 fields are required.

```json
{
  "enableJavaScriptQueries": true,
  "enableInlineQueries": true,
  "inlineQueryPrefix": "=",
  "javascriptInlineQueryPrefix": "$=",
  "renderNullAs": "\\-",
  "dateFormat": "yyyy-MM-dd",
  "dateTimeFormat": "yyyy-MM-dd HH:mm",
  "automaticViewRefreshing": true,
  "refreshInterval": 2500,
  "primaryColumnName": "File",
  "enableDataviewJs": true,
  "enableInlineJsQueries": true,
  "warnOnEmptyResult": false,
  "taskCompletionTracking": false,
  "taskCompletionText": "completion",
  "taskCompletionDateFormat": "yyyy-MM-dd"
}
```

| Field | Type | Purpose |
|---|---|---|
| `enableJavaScriptQueries` | bool | Master switch for `` ```dataviewjs `` blocks |
| `enableInlineQueries` | bool | Master switch for inline `` `= field` `` expressions |
| `inlineQueryPrefix` | string | Prefix character for inline DQL (default: `"="`) |
| `javascriptInlineQueryPrefix` | string | Prefix for inline JS (default: `"$="`) |
| `renderNullAs` | string | String shown for empty/null values (use `"\\-"` for dash) |
| `dateFormat` | string | Display format for dates in query results |
| `dateTimeFormat` | string | Display format for date+time values |
| `automaticViewRefreshing` | bool | Auto re-render queries when vault files change |
| `refreshInterval` | number | Milliseconds between refresh checks (2500 = 2.5s) |
| `primaryColumnName` | string | Header label for the File link column in TABLE queries |
| `enableDataviewJs` | bool | Enable JavaScript execution in dataviewjs blocks |
| `enableInlineJsQueries` | bool | Enable inline JavaScript queries with `$=` prefix |
| `warnOnEmptyResult` | bool | Show a warning when a query returns zero results |
| `taskCompletionTracking` | bool | Whether Dataview tracks task completion dates |
| `taskCompletionText` | string | Tag used for completion (e.g., `"completion"`) |
| `taskCompletionDateFormat` | string | Date format for completion timestamps |

## Gotchas & Known Issues

- **data.json MUST include every field** — omitting any field causes `Cannot read properties of undefined` crashes. See Programmatic Configuration above for the full 16-field schema.
- **Frontmatter must be valid YAML** — a bare colon or bad indentation breaks the entire note's metadata. Use the Linter plugin to auto-fix.
- **DQL is read-only; DataviewJS is NOT** — DQL queries are sandboxed and safe. DataviewJS has full plugin-level access — it can read, write, and delete files. Only copy-paste DataviewJS from sources you trust.
- **DataviewJS can be slow on large vaults** — JS queries run on every refresh. Use `LIMIT` and scope `FROM` to a specific folder wherever possible.
- **Inline fields require "Enable Inline Queries" to be on** — `key:: value` syntax won't index otherwise.
- **Date comparisons need `date()` wrapper** — `WHERE due <= "2026-05-01"` fails silently. Use `WHERE due <= date("2026-05-01")` or `date(today)`.
- **Tags in FROM must include `#`** — `FROM "Projects"` is a folder path; `FROM #projects` is a tag.
- **Results don't persist** — Dataview only renders when the note is open. There's no cached output to read externally.
- **Slow bug fixes** — blacksmithgu has stepped back from active development; occasional releases still happen (v0.5.70, Apr 2025). 630+ open issues. The community fork **Dataview Fixes** (installable via BRAT) patches many known issues but isn't an official replacement.

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
