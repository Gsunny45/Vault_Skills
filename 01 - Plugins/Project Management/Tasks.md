---
type: plugin
name: Tasks
category: Project Management
status: active
complexity: medium
downloads: 3.3M+
last-verified: 2026-04-30
tags:
  - plugin
  - project-management
  - tasks
  - productivity
  - gtd
---

# Tasks

> Plugin by Clare Macrae (originally obsidian-tasks-group) — a comprehensive task management system for Obsidian. Track due dates, scheduled dates, priorities, recurrence, and completion across your entire vault with powerful query blocks.

## What It Does

Tasks turns Obsidian's native `- [ ]` checkboxes into rich task objects with metadata. Add emoji-based markers directly in task text to attach due dates, scheduled dates, start dates, priorities, recurrence rules, and more. Then query those tasks from any note using a `tasks` code block.

Key features:
- **Emoji metadata syntax** — `📅 2026-05-01` (due), `⏳ 2026-04-30` (scheduled), `🔺` (urgent priority), `🔁 every week` (recurrence)
- **Task queries** — filter, sort, and group tasks across the entire vault
- **Task editing modal** — click any task to open a GUI editor for all metadata fields
- **Recurrence** — automatically creates the next occurrence when a recurring task is completed
- **Global task filter** — optionally limit which checkboxes Tasks considers (useful if you use `- [ ]` for non-task purposes)

## When To Use It

- You need dates and priorities on tasks that span multiple notes and folders
- You want a "Today's tasks" view that pulls from everywhere in your vault
- Recurring tasks (weekly reviews, monthly billing, etc.)
- GTD or time-blocking workflows inside Obsidian
- You want task-editing without leaving the reading/editing context (modal editor)
- Reporting: "show me everything due this week, sorted by priority"

Not the right tool if you only use tasks inside a Kanban board — Kanban handles that better. Use both: Kanban for visual workflow, Tasks for date/priority tracking.

## Minimal Setup

1. **Install**: Community Plugins → search "Tasks" by Clare Macrae → Install & Enable
2. **Start adding metadata to tasks** in any note:
   ```markdown
   - [ ] Write plugin documentation 📅 2026-05-01 🔺
   - [ ] Review Q1 metrics ⏳ 2026-04-30 📅 2026-05-05
   - [ ] Weekly review 🔁 every monday 📅 2026-05-05
   ```
3. **Create a query note** to view all upcoming tasks:
   ````markdown
   ```tasks
   not done
   due before in two weeks
   sort by due
   sort by priority
   ```
   ````
4. That's it — Tasks indexes your entire vault automatically.

## Emoji Metadata Reference

| Emoji | Meaning | Format |
|---|---|---|
| 📅 | Due date | `📅 YYYY-MM-DD` |
| ⏳ | Scheduled date | `⏳ YYYY-MM-DD` |
| 🛫 | Start date | `🛫 YYYY-MM-DD` |
| ✅ | Done date | `✅ YYYY-MM-DD` (auto-added on completion) |
| ❌ | Cancelled date | `❌ YYYY-MM-DD` |
| 🔺 | Urgent priority | |
| ⏫ | High priority | |
| 🔼 | Medium priority | |
| 🔽 | Low priority | |
| ⏬ | Lowest priority | |
| 🔁 | Recurrence rule | `🔁 every week`, `🔁 every 2 days`, `🔁 every month on the 1st` |
| 🆔 | Task ID | `🆔 abc123` (for dependency tracking) |
| ⛔ | Depends on | `⛔ abc123` (blocked by another task) |

## Example Queries

### Today's focus (due today or overdue)
````markdown
```tasks
not done
due on or before today
sort by priority
sort by due
group by due
```
````

### This week's tasks
````markdown
```tasks
not done
due before in 7 days
not done
sort by due
sort by priority
```
````

### All high-priority tasks
````markdown
```tasks
not done
priority is high
sort by due
```
````

### Overdue tasks
````markdown
```tasks
not done
due before today
sort by due
```
````

### Completed today
````markdown
```tasks
done on today
sort by done
```
````

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Global task filter | (leave blank) | Set only if you use `- [ ]` for non-task purposes; e.g. `#task` to restrict Tasks to tagged items only |
| Remove global filter from description | On | Hides the filter tag from task display |
| Set created date on every added task | On | Adds 🏁 creation date automatically — useful for tracking |
| Use filename as Scheduled date for Daily Notes | On | If you work in daily notes, tasks without a scheduled date default to the note's date |
| Status types | (configure custom statuses) | Lets you define custom checkbox states beyond `[ ]` and `[x]` |
| Date format | `YYYY-MM-DD` | Must match your vault's date format |
| Recurrence | On | Enable to create next occurrence on task completion |

## Gotchas & Known Issues

- **Emoji must be on the same line as the task** — metadata emoji after a line break won't be recognized. Everything for one task must be on one line.
- **Completed tasks stay in the source file** — checking off a task in a query view marks it done in the source file but doesn't move it. Use "Archive" queries to hide done tasks.
- **Global filter changes affect all existing tasks** — if you add a global filter after you've been using Tasks for a while, existing tasks without the filter tag disappear from queries. Enable it from day one or leave it blank.
- **Recurrence creates the next task in the same file** — the new occurrence appears directly below the completed task in the source note, not in a separate file.
- **Query performance on large vaults** — Tasks scans the entire vault on every query render. With 1000+ notes, queries can take 1-3 seconds. Use `path includes` filters to narrow scope.
- **No subtasks** — Tasks doesn't support task hierarchies natively. Nested `- [ ]` lists work in notes but aren't treated as parent/child in queries.
- **Conflict with Dataview task queries** — both plugins can render task lists. Prefer Tasks for editing/dates, Dataview for complex cross-field queries.

## Works Well With

- [[Kanban]] — Kanban for visual board workflow, Tasks for date/priority metadata and cross-vault queries
- [[Dataview]] — combine Dataview queries with Tasks metadata for advanced reporting
- [[Calendar]] — view task due dates on a calendar
- [[Periodic Notes]] — add tasks to daily/weekly notes; Tasks queries aggregate them vault-wide
- [[Natural Language Dates]] — type dates in natural language, NLD converts them to `YYYY-MM-DD` format Tasks understands
- [[QuickAdd]] — quick-capture new tasks to an inbox note with a hotkey

## Related Skills

- [[Kanban Workflows]]
- [[Dashboards]]

## Links

- [GitHub](https://github.com/obsidian-tasks-group/obsidian-tasks)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=obsidian-tasks-plugin)
- [Official Docs](https://publish.obsidian.md/tasks/)
