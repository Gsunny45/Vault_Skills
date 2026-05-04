---
type: skill
name: Dataview Dashboard Patterns
category: Data
difficulty: advanced
tags:
  - skill
  - dataview
  - dataviewjs
  - dashboard
  - queries
---

# Dataview Dashboard Patterns

## What This Skill Covers
Advanced Dataview techniques for dashboard queries — DQL vs DataviewJS tradeoffs, performance patterns, calculated fields, inline stats, and query debugging. Designed as a companion to [[Dashboards]] (which covers layout and CSS).

## When You Need This
- Your dashboard has 10+ queries and it's getting slow
- DQL can't produce the exact output you need (nested layouts, calculated aggregates)
- You need to debug a query that silently returns nothing
- You want inline stats ("14 plugins · 3 documenting") without full tables
- You're building a dashboard for a vault with 500+ notes

## Core Concepts

### DQL vs DataviewJS

| Aspect | DQL | DataviewJS |
|--------|-----|------------|
| **Syntax** | SQL-like `TABLE/WHERE/SORT` | JavaScript `dv.pages().where()...` |
| **Speed** | Faster (cached query engine) | Slower (full JS execution per block) |
| **Aggregates** | `GROUP BY` + `length(rows)` | `dv.array().groupBy()` |
| **Inline output** | Not possible | `dv.span()` and `dv.paragraph()` |
| **Custom formatting** | No | Full JS (badges, colors, progress bars) |
| **Error visibility** | Silent failures | Console errors in DevTools |

**Rule:** Start with DQL. Switch to DataviewJS only when DQL can't produce the output you need.

### Performance Rules

| Problem | Cause | Fix |
|---------|-------|-----|
| Dashboard takes 5+ seconds to render | Too many `FROM ""` queries | Scope to specific folders |
| Obsidian freezes on keystroke | Dataview re-runs all queries on every change | Increase refresh interval to 5000ms |
| DataviewJS block shows nothing | JS error in the block | Check DevTools Console (`Ctrl+Shift+I`) |
| DQL query returns empty | Wrong field name or folder path | Test query in isolation in a scratch note |

## Step-by-Step

### Step 1 — Inline Stats with DataviewJS

For quick counts that read like a badge bar, use `dv.span()`:

```dataviewjs
const songs = dv.pages('"Songs"').where(p => p.type === "song");
const albums = dv.pages('"Albums"').where(p => p.type === "album");
const artists = dv.pages('"Artists"').where(p => p.type === "artist");

dv.span(`
**${songs.length}** songs ·
**${albums.length}** albums ·
**${artists.length}** artists
`);
```

### Step 2 — Missing Metadata Query

Find notes with empty frontmatter fields:

```dataview
TABLE file.folder AS "Folder", file.mtime AS "Last Modified"
FROM ""
WHERE type != null AND (mood = null OR mood = "")
SORT file.mtime DESC
```

### Step 3 — Grouped Counts

Count notes by type:

```dataview
TABLE length(rows) AS "Count"
FROM ""
WHERE type != null
GROUP BY type
SORT length(rows) DESC
```

### Step 4 — Date Comparisons

Common date patterns:

```dataview
TABLE title, rating, bpm
FROM "Songs"
WHERE bpm >= 120 AND type = "song"
SORT bpm ASC
```

```dataview
TABLE file.mtime AS "Modified"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 10
```

### Step 5 — Link Queries

Find orphaned notes (no incoming links):

```dataview
LIST
FROM ""
WHERE type != null AND length(file.inlinks) = 0 AND file.name != "Dashboard"
```

### Step 6 — Debugging Silent Failures

When a DQL query returns nothing:

1. **Check field names** — `mood` vs `Mood` vs `"mood"` are different in Dataview. Frontmatter fields are lowercase, inline fields preserve case.
2. **Check folder paths** — `FROM "Songs"` vs `FROM "songs"` — case-sensitive on some OS.
3. **Check type filter** — `WHERE type = "song"` requires every song note to have `type: song` in frontmatter.
4. **Test in isolation** — Create a scratch note, paste one query, verify it returns data.
5. **Check DevTools** — `Ctrl+Shift+I` → Console. Dataview logs errors there.

## Variations / Approaches

| Approach | Complexity | Best For |
|----------|------------|----------|
| **DQL table queries** | Beginner | Simple data display, sorted lists |
| **DQL grouped counts** | Intermediate | Stats sections, "by category" breakdowns |
| **DataviewJS inline stats** | Intermediate | Quick stat bars, badge-style counts |
| **DataviewJS calculated fields** | Advanced | Custom columns, derived values |
| **Multi-query dashboard** | Advanced | Complex layouts with mixed DQL + JS |

## Common Mistakes
- **FROM "" on large vaults** — queries everything. Scope to folder.
- **Silent null results** — Dataview doesn't error on missing fields, it returns nothing. Verify field names in frontmatter match query.
- **Too many DataviewJS blocks** — each is a full JS execution. Replace with DQL where possible.
- **Forgetting date syntax** — Use `date(today)` not `today()` in DQL. Use `dv.date.now()` in DataviewJS.
- **Case-sensitive field access** — Frontmatter `bpm:` is accessed as `bpm` in queries. Inline field `BPM::` is accessed as `BPM`.

## Related Skills
- [[Dashboards]] — layout, CSS, and dashboard design (companion to this note)
- [[Vault Architecture]] — frontmatter schema design for queryability
- [[Template Systems]] — consistent frontmatter makes queries reliable

## Related Plugins
- [[Dataview]] — the query engine
- [[Templater]] — for consistent frontmatter creation
- [[Linter]] — auto-format frontmatter to prevent query failures
