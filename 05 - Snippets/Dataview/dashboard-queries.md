# Dashboard Dataview Queries

> Reusable Dataview queries for Obsidian dashboards.
> Copy-paste into any dashboard note as fenced code blocks.

---

## Quick Stats (DataviewJS)

Shows aggregated counts as inline badges. Requires the compatible CSS snippet (`dashboard-view.css`).

```dataviewjs
// ─── Counts by category ───
const all = dv.pages("");
const plugins = dv.pages('"01 - Plugins"').where(p => p.type === "plugin");
const skills = dv.pages('"02 - Skills"').where(p => p.type === "skill");
const inbox = dv.pages('"00 - Inbox"');
const active = plugins.where(p => p.status === "active");
const documenting = plugins.where(p => p.status === "documenting");

dv.span(`
<span class="badge">${all.length}</span> total notes ·
<span class="badge">${plugins.length}</span> plugins ·
<span class="badge">${active.length}</span> active ·
<span class="badge">${documenting.length}</span> documenting ·
<span class="badge">${skills.length}</span> skills ·
<span class="badge">${inbox.length}</span> in inbox
`);
```

---

## Recently Modified Notes

```dataview
TABLE file.mtime AS "Modified", file.folder AS "Folder"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 12
```

**Variation — last 30 days:**
```dataview
TABLE file.mtime AS "Modified", file.folder AS "Folder"
FROM ""
WHERE file.mtime >= date(today) - dur(30 days)
SORT file.mtime DESC
LIMIT 25
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

**Variation — tasks due this week:**
```dataview
TASK
FROM ""
WHERE !completed AND due AND due <= date(today) + dur(7 days)
SORT due ASC
```

**Variation — overdue tasks:**
```dataview
TASK
FROM ""
WHERE !completed AND due < date(today)
SORT due ASC
```

**Variation — tasks with no due date:**
```dataview
TASK
FROM ""
WHERE !completed AND !due
LIMIT 15
```

---

## Notes by Folder

```dataview
TABLE length(rows) AS "Notes"
FROM ""
GROUP BY file.folder
SORT length(rows) DESC
```

---

## Missing Metadata

Finds notes missing a required frontmatter field (e.g., `type`):

```dataview
TABLE file.folder AS "Folder", file.mtime AS "Modified"
FROM ""
WHERE type = null AND file.name != "Dashboard"
SORT file.mtime DESC
LIMIT 15
```

**To check for a different field**, replace `type = null` with e.g., `status = null`.

---

## Notes Created Today

```dataview
LIST
FROM ""
WHERE file.cday = date(today)
SORT file.ctime ASC
```

---

## Plugin Documentation Status

```dataview
TABLE category, downloads, complexity, status
FROM "01 - Plugins"
WHERE type = "plugin"
SORT status ASC, downloads DESC
```

---

## Stale Notes (Not Modified in N Days)

```dataview
TABLE file.mtime AS "Last Modified", file.folder AS "Folder"
FROM ""
WHERE file.mtime < date(today) - dur(30 days) AND file.name != "Dashboard"
SORT file.mtime ASC
LIMIT 20
```

---

## Skills by Difficulty

```dataview
TABLE difficulty
FROM "02 - Skills"
WHERE type = "skill"
SORT difficulty ASC
```

---

## Combined Stats Bar (Single Line DataviewJS)

For a compact, single-line statbar at the top of your dashboard:

```dataviewjs
const total = dv.pages("").length;
const p = dv.pages('"01 - Plugins"').length;
const s = dv.pages('"02 - Skills"').length;
const i = dv.pages('"00 - Inbox"').length;
dv.paragraph(`📊 ${total} notes | 📦 ${p} plugins | 🧠 ${s} skills | 📥 ${i} in inbox`);
```
