---
type: skill
name: Dashboards
category: UI & Navigation
difficulty: intermediate
tags:
  - skill
  - dashboard
  - dataview
  - homepage
  - navigation
  - css
  - layout
---

# Dashboards

## What This Skill Covers
How to design, build, and maintain effective Obsidian dashboards — live views that surface your vault's data at a glance. You'll learn to combine Dataview queries, structured frontmatter, CSS styling, the Homepage plugin, and intentional layout design to create dashboards that are both useful and maintainable.

## When You Need This
- You open Obsidian and don't know what to work on — a dashboard gives you a mission-control view
- You want to see recent notes, open tasks, project status, and stats without digging through folders
- Your vault has 100+ notes and you're losing visibility into what's happening
- You want a consistent landing page that orients you every time Obsidian starts
- You maintain multiple projects and want a single pane-of-glass view across all of them
- You're building a vault for others (team, family, clients) and need guided navigation

## Core Concepts

### A Dashboard Is a View, Not a Folder
A dashboard is a single note that aggregates data from across your vault. It doesn't contain the data itself — it queries it live. When your notes change, the dashboard updates automatically. This means:

- **Dashboard is read-only** — queries display data; you edit the source notes
- **Dashboard refreshes on open** — Dataview re-renders every time you view the dashboard
- **Dashboard structure is layout + queries** — headings, dividers, and CSS provide the structure; Dataview blocks provide the data

### Three Layers of a Dashboard

| Layer | What | Tools |
|-------|------|-------|
| **Data** | Structured metadata in your notes | Frontmatter, inline fields (`Key:: Value`) |
| **Query** | Live queries that fetch and display data | Dataview DQL, DataviewJS |
| **Presentation** | Layout, styling, navigation | Headings, CSS snippets, callouts, links |

A good dashboard gets all three layers right. Weak frontmatter = nothing to query. Poor query design = slow or wrong results. No styling = hard to scan.

### Two Query Approaches

| Approach | When to Use | Trade-offs |
|----------|-------------|------------|
| **DQL** (Dataview Query Language) | Simple tables, lists, task queries | No custom formatting, but fast and portable |
| **DataviewJS** | Custom rendering, calculated fields, nested layouts | Full JS power, but slower and more complex |

Start with DQL. Only reach for DataviewJS when DQL can't produce the exact output you need.

## Step-by-Step

### Step 1 — Define Your Dashboard's Purpose

Before writing a single query, decide what your dashboard is *for*. A dashboard that tries to show everything shows nothing well.

**Common dashboard purposes:**

| Purpose | Example Questions It Answers |
|---------|------------------------------|
| **Vault Overview** | How many notes? Recent changes? Missing metadata? |
| **Project Tracker** | What's active? What's blocked? What's due this week? |
| **Task Hub** | What tasks are overdue? What's on deck? |
| **Writing Dashboard** | What's in draft? Last edited? Word counts? |
| **Learning Tracker** | What am I studying? Spaced repetition queue? |
| **Plugin Reference** | Which plugins are documented? What's missing? |

Pick **one** primary purpose. You can build multiple dashboards — one per purpose — and link them together.

### Step 2 — Structure Your Frontmatter for Queryability

Dashboards are only as good as the metadata they query. Standardize frontmatter across related notes.

**Plugin notes** (already using this schema):
```yaml
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
---
```

**Project notes** (example schema to add):
```yaml
---
type: project
name: Q3 Roadmap
status: active  # active | paused | done | archived
priority: high  # high | medium | low
due: 2026-09-30
tags:
  - project
---
```

**Consistency is more important than completeness.** A dashboard can query notes where `type = "plugin"` — but only if every plugin note actually has `type: plugin` in its frontmatter.

If you need metadata *without* frontmatter (e.g., inside body text), use inline fields:
```
Status:: In Progress
Priority:: High
Due:: 2026-06-15
```

Inline fields and frontmatter fields are interchangeable in Dataview queries.

### Step 3 — Write the Data Layer (Dataview Queries)

Build your dashboard section by section. Each section is a heading + one or more Dataview blocks.

**Section: Quick Stats** (DataviewJS for calculated aggregates)
````markdown
### Vault Stats

```dataviewjs
// Total plugin notes
const plugins = dv.pages('"01 - Plugins"').where(p => p.type === "plugin");
const documented = plugins.where(p => p.status === "active");
const documenting = plugins.where(p => p.status === "documenting");

dv.span(`
**${plugins.length}** plugins total ·
**${documented.length}** documented ·
**${documenting.length}** in progress
`);
```
````

**Section: Recent Activity**
```dataview
TABLE file.mtime AS "Last Modified", file.folder AS "Folder"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 10
```

**Section: Open Tasks**
```dataview
TASK
FROM ""
WHERE !completed AND contains(tags, "#project")
SORT due ASC
LIMIT 20
```

**Section: Missing Metadata** (find notes that need frontmatter fixes)
```dataview
TABLE file.folder AS "Folder"
FROM ""
WHERE type = null AND file.name != "Dashboard"
SORT file.mtime DESC
LIMIT 15
```

**Section: Quick Navigation**
```markdown
## Quick Links

- [[_Plugin Index.md|📦 All Plugins]]
- [[_Skill Index.md|🧠 All Skills]]
- [[_Repo Index.md|📡 Plugin Repos]]
- [[00 - Inbox/|📥 Inbox (unsorted)]]
```

### Step 4 — Organize the Layout

A dashboard reads top-to-left-to-right — like a newspaper. Most important info goes top-left.

**Proven layout template:**

```
┌─────────────────────────────────────────────────┐
│  # Dashboard Name (title)                        │
├──────────────────┬──────────────────────────────┤
│  Quick Stats     │  Navigation / Quick Links     │
│  (aggregates)    │  (manual links, tag index)   │
├──────────────────┴──────────────────────────────┤
│  Recent Activity                                 │
│  (last 10 modified notes, any folder)            │
├──────────────────┬──────────────────────────────┤
│  Open Tasks      │  Due This Week                │
│  (all incomplete)│  (tasks with nearby deadlines)│
├──────────────────┴──────────────────────────────┤
│  Notes Needing Attention                         │
│  (missing metadata, stale notes)                 │
├──────────────────┬──────────────────────────────┤
│  Stats by Tag    │  Stats by Category            │
│  (grouped counts)│  (grouped counts)             │
└──────────────────┴──────────────────────────────┘
```

Create this layout by using `## H2` headings for each section, with `---` horizontal rules or `> [!info]` callout blocks as visual dividers. Dataview blocks auto-size to their content width.

#### Multi-Column Layouts

Obsidian renders content in a single column by default. To get side-by-side sections, use one of these approaches:

**Option A — Callout-based grid system (no plugins needed)**
Install the community CSS snippet from the [Obsidian Forum grid snippet](https://forum.obsidian.md/t/css-snippet-to-display-markdown-in-grids-without-html/95117), or adapt the CSS snippet below. Then build columns using callouts:
```markdown
> [!grid-2]
> > [!info] Recent Notes
> > ```dataview
> > TABLE file.mtime FROM "" SORT file.mtime DESC LIMIT 5
> > ```
>
> > [!warning] Open Tasks
> > ```dataview
> > TASK FROM "" WHERE !completed LIMIT 5
> > ```
```

**Option B — Modular CSS Layout (MCL)** ⭐ Recommended
Install the [Modular CSS Layout](https://github.com/efemkay/obsidian-modular-css-layout) snippet collection — the community-standard layout system. It provides:
- **Multi-column callouts** — `> [!multi-column]` wraps child callouts into columns
- **List grids/cards** — add `#mcl/list-grid` or `#mcl/list-card` to lists
- **Float callouts** — `> [!info|right-medium]` for sidebar-style annotations
- **Wide page views** — `cssClass: wide-page` for full-width dashboards

MCL is theme-compatible and removes the need to write CSS yourself. Download `mcl.css` + `mcl-*.css` from GitHub, drop into your snippets folder, and enable them.

### Step 5 — Style with CSS Snippets

CSS snippets make dashboards skimmable. Default Obsidian renders Dataview tables in plain markdown style — fine for data entry, not great for a dashboard you look at 20 times a day.

Create `dashboard-cards.css` in your snippets folder:

```css
/* ─── Dashboard card containers ─── */
.dashboard-view .callout {
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}

/* ─── Dataview table styling ─── */
.dashboard-view .dataview.table-view-table {
  font-size: 0.9em;
}

.dashboard-view .dataview.table-view-table thead th {
  background: var(--background-secondary);
  font-weight: 600;
  padding: 6px 12px;
  border-bottom: 2px solid var(--background-modifier-border);
}

.dashboard-view .dataview.table-view-table tbody tr:hover {
  background: var(--background-primary-alt);
}

/* ─── Task list styling ─── */
.dashboard-view .dataview.task-list-item {
  padding: 2px 0;
}

/* ─── Quick stats badges ─── */
.dashboard-view .badge {
  display: inline-block;
  background: var(--interactive-accent);
  color: var(--text-on-accent);
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 0.85em;
  font-weight: 600;
  margin: 0 2px;
}

/* ─── Link grid for navigation ─── */
.dashboard-view .link-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 8px;
}

.dashboard-view .link-grid a {
  display: block;
  padding: 8px 12px;
  background: var(--background-secondary);
  border-radius: 6px;
  text-decoration: none;
  font-weight: 500;
  transition: background 0.15s;
}

.dashboard-view .link-grid a:hover {
  background: var(--background-secondary-alt);
}
```

Then in your dashboard note, add the CSS class:
```markdown
---
cssclass: dashboard-view
---

# My Dashboard
```

Enable the snippet: Settings → Appearance → CSS Snippets → click reload → toggle `dashboard-cards.css` on.

#### Quick Win: Cupertino `.cards` View

If you use the Cupertino theme (or install its cards CSS snippet), add `cssclass: cards` to your frontmatter and Dataview tables automatically render as visual card grids instead of rows:

```yaml
---
cssclass: cards cards-cols-3
---
```

Add `cards-cols-2` through `cards-cols-8` to control column count. Works with any Dataview TABLE query — no CSS writing required.

### Step 6 — Set as Homepage or Use Dashboard Navigator (Optional)

**Option A: Homepage Plugin** — open your custom dashboard note on launch:
1. Install Homepage (if not done)
2. Settings → Homepage → Homepage type → `File`
3. Homepage → enter your dashboard note name (e.g., `Dashboard`)
4. Open on startup → On
5. Opening method → `Replace last tab` (clean launch) or `Keep existing tabs` (restore session)

For a quick return key: Settings → Hotkeys → search "Homepage: Open Homepage" → assign `Alt+Home`.

**Option B: Dashboard Navigator** — a purpose-built dashboard plugin instead of writing queries:
Dashboard Navigator (by Bernardo Pires) gives you an auto-generated homepage panel with recent files by type, files by day/week/month, and search — without writing any Dataview queries. Install from Community Plugins. It works as a standalone alternative to a Dataview dashboard if you prefer a ready-made solution.

You can also combine both: use Dashboard Navigator as your landing page for quick access, and keep a Dataview dashboard note for deeper vault analysis.

### Step 7 — Maintain and Test Your Dashboard

Dashboards degrade over time as vault structure changes. Schedule maintenance:

- **Weekly**: Check that all queries still return the expected data. Did a folder name change?
- **Monthly**: Review frontmatter consistency. Are all project notes using the same status values?
- **Quarterly**: Remove queries you don't look at. Add queries for new patterns you've adopted.

#### Testing Your Dashboard

Before relying on a dashboard, validate each query independently:

**1. Test queries in isolation**
Create a scratch note and paste one query at a time. Verify:
- Does the query return results at all? (An empty result could mean no matching data or a broken query)
- Are the column values correct? (e.g., `status` column showing "active" when you expected "done")
- Are the date comparisons working? (`due <= date(today)` vs `due < date(today)` — off-by-one errors are common)

**2. Check for silent failures**
Dataview fails silently — a bad query renders an empty table with no error. Common silent failures:
```dataview
TABLE status, due
FROM "01 - Plugins"
WHERE status "active"    ← missing `=`: returns nothing, no error
```
Fix by reading the Dataview console output: `Ctrl+Shift+I` → Console tab. Dataview logs errors there.

**3. Verify performance under load**
Open your dashboard and watch the render time. If it takes more than 2-3 seconds to fully render:
- Open Developer Tools (`Ctrl+Shift+I`) → Console — look for Dataview timing logs
- Use `Ctrl+Shift+I` → Performance tab to identify slow queries
- Mitigate: scope `FROM` tighter, add `LIMIT`, replace DataviewJS with DQL

**4. Test with a fresh vault state**
Restart Obsidian and open the dashboard. If it breaks:
- Did a plugin update change Dataview syntax? (rare but happens)
- Did you rename a folder used in a `FROM` clause?
- Is the Dataview plugin enabled and indexing? Check Settings → Dataview → Index Status

**5. Cross-browser test (if using Obsidian Publish)**
If your dashboard is published, test in Chrome, Firefox, and Edge. Dataview rendering can differ in the Publish context — some CSS snippets may not apply.

#### Performance Notes

Dataview re-runs all queries when *any* note changes. If your dashboard has 10+ complex DataviewJS blocks on a 500+ note vault, it will lag. Mitigations:
- Use `FROM "specific/folder"` instead of `FROM ""`
- Add `LIMIT` to every query
- Replace DataviewJS with plain DQL where possible
- Split into multiple specialized dashboards instead of one mega-dashboard
- Consider setting a higher Dataview refresh interval: Settings → Dataview → Refresh interval → `5000`ms

## Variations / Approaches

| Approach | Complexity | Best For |
|----------|------------|----------|
| **Manual dashboard** (links only, no queries) | Beginner | Simple navigation hub, static vault map |
| **Dashboard Navigator plugin** (auto-generated panel) | Beginner | Ready-made homepage replacement, no queries needed |
| **Single DQL dashboard** (TABLE + LIST + TASK queries) | Beginner | Simple vault overview, personal dashboards |
| **Multi-section dashboard** (DQL + callouts + CSS/MCL) | Intermediate | Project tracking, team vaults, daily driver |
| **DataviewJS dashboard** (custom rendering, badges, progress bars) | Advanced | Complex reports, visual-heavy dashboards |
| **Charts dashboard** (DataviewJS + Charts plugin) | Advanced | Data visualization: line charts, Sankey diagrams, bar graphs |
| **Multiple linked dashboards** (one per domain) | Advanced | Large vaults (500+ notes), distinct workspaces |
| **Canvas dashboard** (visual nodes, not queries) | Advanced | Visual thinkers, mind-map style overviews |

## Example — Full Vault Dashboard (copy-paste ready)

Create a new note called `Dashboard.md` and paste this:

```markdown
---
cssclass: dashboard-view
---

# 📊 Vault Dashboard

> Last refreshed automatically by Dataview.

---

## Quick Stats

```dataviewjs
const all = dv.pages("");
const plugins = dv.pages('"01 - Plugins"').where(p => p.type === "plugin");
const skills = dv.pages('"02 - Skills"').where(p => p.type === "skill");
const inbox = dv.pages('"00 - Inbox"');
const activePlugins = plugins.where(p => p.status === "active");
const documenting = plugins.where(p => p.status === "documenting");

dv.span(`
<span class="badge">${all.length}</span> total notes ·
<span class="badge">${plugins.length}</span> plugins ·
<span class="badge">${activePlugins.length}</span> active ·
<span class="badge">${documenting.length}</span> documenting ·
<span class="badge">${skills.length}</span> skills ·
<span class="badge">${inbox.length}</span> in inbox
`);
```

---

## Quick Navigation

> [!tip] Jump to...
> - [[_Plugin Index.md|📦 Plugin Index]]
> - [[_Skill Index.md|🧠 Skill Index]]
> - [[_Repo Index.md|📡 Repo Index]]
> - [[00 - Inbox/|📥 Inbox]]
> - [[02 - Skills/_Skill Index.md#Difficulty Key|🎯 Skill Difficulty Guide]]

---

## Recently Modified

```dataview
TABLE file.mtime AS "Modified", file.folder AS "Folder"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 12
```

---

## Open Tasks

```dataview
TASK
FROM ""
WHERE !completed
SORT due ASC
LIMIT 20
```

---

## Due This Week

```dataview
TASK
FROM ""
WHERE !completed AND due AND due <= date(today) + dur(7 days)
SORT due ASC
```

---

## Documentation Gaps

```dataview
TABLE file.folder AS "Folder", file.mtime AS "Last Modified"
FROM "01 - Plugins"
WHERE type = "plugin" AND status = "documenting"
SORT file.mtime ASC
```

---

## Vault by Folder

```dataview
TABLE length(rows) AS "Notes"
FROM ""
GROUP BY file.folder
SORT length(rows) DESC
```

---

## Daily Note

> [!abstract] Today
> `= date(today)`
>
> [[Daily Notes/`= date(today).toFormat("yyyy-MM-dd")` |Open today's note →]]
>
> **Notes created today:**
> ```dataview
> LIST
> FROM ""
> WHERE file.cday = date(today)
> SORT file.ctime ASC
> ```
```

## Dashboard Templates by Purpose

### Minimalist Task Dashboard
```markdown
# Today's Focus

## Overdue
```dataview
TASK
FROM ""
WHERE !completed AND due < date(today)
SORT due ASC
```

## Today
```dataview
TASK
FROM ""
WHERE !completed AND due = date(today)
```

## This Week
```dataview
TASK
FROM ""
WHERE !completed AND due > date(today) AND due <= date(today) + dur(7 days)
SORT due ASC
```

## No Due Date
```dataview
TASK
FROM ""
WHERE !completed AND !due
LIMIT 15
```
```

### Plugin Documentation Dashboard
```markdown
# Plugin Documentation

## Documented (Active)
```dataview
TABLE category, downloads, complexity
FROM "01 - Plugins"
WHERE type = "plugin" AND status = "active"
SORT downloads DESC
```

## Needs Documentation
```dataview
TABLE category, downloads
FROM "01 - Plugins"
WHERE type = "plugin" AND status != "active" AND status != "documenting"
SORT downloads DESC
```

## In Progress
```dataview
TABLE category, downloads
FROM "01 - Plugins"
WHERE type = "plugin" AND status = "documenting"
SORT downloads DESC
```
```

### Project Health Dashboard
```markdown
# Project Overview

## Active Projects
```dataview
TABLE priority, due, file.mtime AS "Last Updated"
FROM ""
WHERE type = "project" AND status = "active"
SORT priority ASC, due ASC
```

## Stale Projects (no update in 14 days)
```dataview
TABLE priority, due, file.mtime AS "Last Updated"
FROM ""
WHERE type = "project" AND status = "active" AND file.mtime < date(today) - dur(14 days)
SORT file.mtime ASC
```

## Completed
```dataview
TABLE priority, due
FROM ""
WHERE type = "project" AND status = "done"
SORT due DESC
LIMIT 10
```
```

## Common Mistakes

- **Dashboard tries to show everything** — 20+ queries on one page is overwhelming. If nothing stands out, the dashboard is noise. Split into purpose-specific dashboards.
- **No consistent frontmatter** — queries return partial results because half the notes are missing the `status` field. Use the Linter plugin to auto-enforce frontmatter, or run periodic missing-metadata queries.
- **`FROM ""` on 500+ note vaults** — queries the entire vault on every keystroke. Always scope to a folder when possible.
- **Too many DataviewJS blocks** — each one runs as a full JS execution. Replace with DQL where you can. DQL is cached more aggressively.
- **No CSS styling** — raw Dataview tables are functional but visually dense. Even 10 lines of CSS (rounded corners, hover states, font sizing) dramatically improves scanability.
- **Forgetting about mobile** — Dataview tables don't shrink well on mobile screens. Either create a simplified mobile dashboard, or accept that dashboards are desktop-first.
- **No maintenance schedule** — a folder rename or frontmatter schema change silently breaks queries. Review dashboard queries after any vault restructuring.
- **All queries in one block** — if one query is slow (e.g., a complex DataviewJS aggregation), it blocks all other queries from rendering. Break into separate code blocks.
- **Not testing queries in isolation** — a missing `=` or wrong folder path silently returns nothing. Test each query alone in a scratch note before adding it to the dashboard.
- **Ignoring query ordering** — `SORT due ASC` puts null/missing dates first, not last. Use `SORT due ASC` with a `WHERE due` filter if you want dates-only, or flip to `DESC` to push nulls to the bottom.
- **Reinventing the wheel with CSS** — before writing custom CSS, check if MCL (multi-column/cards) or Cupertino `.cards` already does what you need. The community has solved most layout problems.

## Related Skills
- [[Dataview Dashboard Patterns]] — advanced Dataview techniques for complex dashboard queries
- [[Vault Architecture]] — structuring folders and frontmatter for queryability
- [[Template Systems]] — creating dashboard templates with Templater for rapid setup
- [[Kanban Workflows]] — combine Kanban boards with dashboard overviews
- [[Canvas Visual Mapping]] — visual canvas-based alternative to query dashboards
- [[REST API Automation]] — fetch dashboard data from external scripts

## Related Plugins
- [[Dataview]] — the query engine that powers live dashboards
- [[Homepage]] — set your dashboard as the Obsidian landing page
- **Dashboard Navigator** — auto-generated homepage panel (recents, files by day, search). Install from Community Plugins.
- **Charts** (obsidian-charts) — data visualization plugin. Use with DataviewJS to render line charts, bar graphs, Sankey diagrams from query data.
- **QueryDash** — enhances Dataview tables with interactive filtering, sorting, and pagination. Drop-in replacement for ` ```dataview ` blocks.
- [[Templater]] — create dashboard templates with dynamic content
- [[QuickAdd]] — capture notes with consistent frontmatter that feeds dashboard queries
- [[Style Settings]] — theme-level dashboard styling
- [[Linter]] — auto-format and validate frontmatter for reliable queries
- [[Tasks]] — rich task data for task-focused dashboard sections
- [[Calendar]] — calendar views of dashboard data
- [[Periodic Notes]] — link dashboards to daily/weekly review notes

### Community CSS (No Plugin Needed)
- **Modular CSS Layout (MCL)** — [GitHub](https://github.com/efemkay/obsidian-modular-css-layout) — multi-column callouts, list grids/cards, float callouts. Download and enable as CSS snippets.
- **Cupertino Cards** — theme or standalone snippet that adds `.cards` class support for Dataview tables. Transforms rows into visual card grids.
