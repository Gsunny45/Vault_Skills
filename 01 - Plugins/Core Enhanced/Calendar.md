---
type: plugin
name: Calendar
category: Core Enhanced
status: active
complexity: low
downloads: 2.6M+
last-verified: 2026-04-30
tags:
  - plugin
  - core-enhanced
  - calendar
  - daily-notes
  - periodic-notes
---

# Calendar

> Plugin by liamcain — adds a monthly calendar view to Obsidian's sidebar. Click any date to open or create the corresponding daily note. Integrates tightly with Periodic Notes and Dataview.

## What It Does

Calendar adds a compact monthly calendar widget to the right sidebar. Each day cell represents a potential daily note — clicking a cell opens that note (or creates it if it doesn't exist). Cells with existing notes are visually distinct from empty cells.

Additional visual indicators:
- **Dot indicators** — shows how many words or tasks are in each daily note (configurable)
- **Week numbers** — optional column showing ISO week numbers, clickable to open weekly notes
- **Today highlight** — current date is always visually marked

Calendar doesn't create any note structure itself — it relies on Obsidian's core Daily Notes plugin or the Periodic Notes plugin for note creation and templating.

## When To Use It

- You maintain daily or weekly notes and want visual calendar navigation
- Checking which days have notes without searching
- Jumping to any past date quickly
- Reviewing weekly patterns in your note-taking habit
- Using Periodic Notes and wanting one-click access to any day's note

## Minimal Setup

1. **Install**: Community Plugins → search "Calendar" by liamcain → Install & Enable
2. **Verify Daily Notes is configured**: Settings → Core plugins → Daily notes → On, and set your notes folder + date format
3. **Open the calendar**: Ribbon → Calendar icon, or Command Palette → "Calendar: Open Calendar"
4. The calendar appears in the right sidebar. Click today to open today's daily note.

**For full functionality, pair with Periodic Notes** (see below) — it handles templates and multiple note periods (weekly, monthly).

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Start week on | Monday | Personal preference; Monday is standard in most countries |
| Show week numbers | On | Adds a clickable week column; opens weekly note on click |
| Dot type | Word count | Shows word count as dot size per day; helps see active vs. light days |
| Confirm before creating new note | Off | Skip confirmation dialog for faster daily note creation |

## Integration with Periodic Notes

Calendar's real power comes from pairing it with Periodic Notes:

| Calendar action | Periodic Notes integration |
|---|---|
| Click a day cell | Opens/creates daily note using Periodic Notes template |
| Click a week number | Opens/creates weekly note using Periodic Notes template |
| Click an empty cell | Creates note with the date-specific Templater template |

Setup:
1. Install Periodic Notes
2. Settings → Periodic Notes → Daily Notes → Template: `03 - Templates/Daily Note.md`
3. Settings → Periodic Notes → Weekly Notes → Template: `03 - Templates/Weekly Review.md`
4. Calendar will now use these templates when creating notes

## Gotchas & Known Issues

- **Calendar uses Daily Notes OR Periodic Notes, not both** — if Periodic Notes is installed and configured, Calendar defers to it. Disable Obsidian's core Daily Notes plugin if you're using Periodic Notes to avoid conflicts.
- **Week number clicks only work if weekly notes are configured** — clicking a week cell without Periodic Notes weekly notes configured does nothing.
- **Dot indicators reflect word count, not note quality** — a note with one long paragraph looks the same as one with many short tasks.
- **Calendar doesn't support monthly/quarterly note creation** — that's Periodic Notes' territory. Calendar only handles day and week navigation.
- **Mobile sidebar behavior** — on mobile, the calendar panel may be hidden by default. Enable it via the sidebar toggle.

## Works Well With

- [[Periodic Notes]] — the core companion plugin; handles templates and note creation logic for daily/weekly/monthly notes
- [[Templater]] — Periodic Notes uses Templater templates that Calendar triggers on date click
- [[Dataview]] — use a CALENDAR query in Dataview alongside the Calendar plugin for a notes-based calendar view
- [[Tasks]] — view task due dates on the Dataview calendar; use Calendar for daily note navigation
- [[Natural Language Dates]] — type dates in notes naturally; Calendar provides the visual navigation layer

## Related Skills

- [[Dashboards]]
- [[Template Systems]]

## Links

- [GitHub](https://github.com/liamcain/obsidian-calendar-plugin)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=calendar)
