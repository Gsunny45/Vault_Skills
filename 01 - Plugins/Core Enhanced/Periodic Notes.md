---
type: plugin
name: Periodic Notes
category: Core Enhanced
status: active
complexity: low
downloads: 1M+
last-verified: 2026-04-30
tags:
  - plugin
  - core-enhanced
  - daily-notes
  - weekly-notes
  - journaling
  - periodic
---

# Periodic Notes

> Plugin by liamcain — extends Obsidian's core Daily Notes plugin to support weekly, monthly, quarterly, and yearly notes. Works in tandem with Templater for templated note creation and Calendar for visual navigation.

## What It Does

Periodic Notes replaces Obsidian's core Daily Notes plugin with a more powerful alternative that supports five note periods:
- **Daily** — one note per day
- **Weekly** — one note per week (ISO week numbering)
- **Monthly** — one note per month
**Quarterly** — one note per quarter
- **Yearly** — one note per year

Each period type gets its own template, folder path, and filename format. The Calendar plugin integrates directly with Periodic Notes to open/create these notes on date/week clicks.

## When To Use It

- Daily journaling with a consistent template (tasks, gratitude, notes, reflections)
- Weekly review notes (what I did, what's next, blockers)
- Monthly retrospectives
- Replacing Obsidian's core Daily Notes for better template and multi-period support
- Any time-based note-taking system (GTD, PARA with time layer, etc.)

**Disable core Daily Notes** when using Periodic Notes — they conflict.

## Minimal Setup

1. **Disable core Daily Notes**: Settings → Core plugins → Daily notes → Off
2. **Install**: Community Plugins → search "Periodic Notes" by liamcain → Install & Enable
3. **Configure daily notes**: Settings → Periodic Notes → Daily Notes:
   - Format: `YYYY-MM-DD`
   - Folder: `Journal/Daily` (or your folder)
   - Template: `03 - Templates/Daily Note.md`
4. **Create a daily note**: Command Palette → "Periodic Notes: Open today's daily note"

### Optional weekly notes
Settings → Periodic Notes → Weekly Notes:
- Enable: On
- Format: `YYYY-[W]WW` (e.g., `2026-W18`)
- Folder: `Journal/Weekly`
- Template: `03 - Templates/Weekly Review.md`

## Recommended Templates

### Daily Note template (`03 - Templates/Daily Note.md`)
```markdown
---
type: daily
date: <% tp.date.now("YYYY-MM-DD") %>
day: <% tp.date.now("dddd") %>
tags: [daily]
---

# <% tp.date.now("dddd, MMMM D, YYYY") %>

## 🎯 Top 3 Today
- 
- 
- 

## 📝 Notes

## ✅ Tasks
```tasks
not done
scheduled on <% tp.date.now("YYYY-MM-DD") %>
```

## 📓 Journal

```

### Weekly Review template (`03 - Templates/Weekly Review.md`)
```markdown
---
type: weekly
week: <% tp.date.now("YYYY-[W]WW") %>
date-start: <% tp.date.now("YYYY-MM-DD", 0, "YYYY-MM-DD", "isoWeek") %>
tags: [weekly]
---

# Week <% tp.date.now("WW") %> Review

## ✅ Completed This Week

## 🔄 In Progress

## ⏭️ Next Week

## 💡 Insights & Learnings

## 📊 Metrics

```

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Daily Notes → Format | `YYYY-MM-DD` | ISO date format; sorts chronologically by filename |
| Daily Notes → Folder | `Journal/Daily` | Keep separate from main notes |
| Daily Notes → Template | `03 - Templates/Daily Note.md` | Requires Templater installed |
| Daily Notes → Open on startup | Off | Use Homepage plugin for startup behavior instead |
| Weekly Notes → Format | `YYYY-[W]WW` | e.g., `2026-W18` |
| Weekly Notes → Start week on | Monday | Set to match Calendar plugin setting |
| Monthly Notes → Format | `YYYY-MM` | e.g., `2026-04` |

## Gotchas & Known Issues

- **Must disable core Daily Notes** — both plugins compete for the same "open today's note" command. Core Daily Notes wins if both are enabled, ignoring Periodic Notes' config.
- **Calendar plugin must be configured to use Periodic Notes** — Calendar automatically detects Periodic Notes if both are installed. No extra config needed, but if Calendar still uses core Daily Notes, check that core Daily Notes is disabled.
- **Date format in filename must be unique** — if your daily note format is `YYYY-MM-DD` and monthly is `YYYY-MM`, a monthly note `2026-04` could conflict with a daily note if you had one named that way. Use `YYYY-MM-DD` for daily and include more specificity for other periods.
- **Quarterly notes** — not all versions support quarterly notes equally well. Check the GitHub release notes for your version.
- **Template execution requires Templater** — Periodic Notes triggers Templater templates on creation. Without Templater, template syntax won't be evaluated.

## Works Well With

- [[Templater]] — provides the template engine that Periodic Notes triggers on note creation
- [[Calendar]] — click any date to open/create the daily note; click week numbers for weekly notes
- [[Dataview]] — query periodic notes by date range: `FROM "Journal/Daily" WHERE date >= date(today) - dur(7 days)`
- [[Tasks]] — add task queries to daily/weekly templates that pull from the vault; use Periodic Notes as the frame
- [[QuickAdd]] — capture to today's daily note with a QuickAdd capture choice pointing to `{{DATE:YYYY-MM-DD}}.md`

## Related Skills

- [[Dashboards]]
- [[Template Systems]]

## Links

- [GitHub](https://github.com/liamcain/obsidian-periodic-notes)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=periodic-notes)
