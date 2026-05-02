---
type: plugin
name: Day Planner
category: Project Management
status: active
complexity: medium
downloads: 760k+
last-verified: 2026-05-01
tags:
  - plugin
  - project-management
  - time-blocking
  - planning
  - calendar
---

# Day Planner

## What It Does
Editable timeline and multi-day planner views inside Obsidian with time-blocking, calendar integration (Google/iCloud/Outlook via ICS), Tasks plugin support, and experimental time tracking. Merges tasks from daily notes, Tasks plugin queries, and external calendars into a unified visual timeline. Requires **Dataview** plugin — it's mandatory.

**Key capabilities:**
- **Timeline sidebar** — vertical timeline of your day with drag-and-drop reschedule
- **Multi-day planner** — horizontal overview across several days
- **Mini-timeline** — upcoming 3 hours shown in the status bar as colored blocks
- **Calendar integration** — Google Calendar, iCloud, Outlook via ICS links
- **Tasks plugin support** — tasks with `scheduled` dates appear on timeline
- **Time tracking** — experimental clock for recording time spent (right-click → Start clock)

## When To Use It
- Time-blocking your day with a visual timeline alongside your daily note
- Seeing schedule gaps and over-booking before the day starts
- Combining external calendar events with Obsidian tasks in one view
- Multi-day planning across the work week
- Quick glance at next 3 hours from the status bar
- Logging actual time spent on tasks (experimental)

## Prerequisites
- **Dataview plugin** — must be installed and enabled (plugin won't load without it)
- **Daily Notes** (core) or **Periodic Notes** (community) — required for daily note integration

## Minimal Setup
1. **Install**: Community Plugins → search "Day Planner" by Ivan Lednev → Install → Enable
2. **Verify prerequisites**: Dataview + Daily Notes (or Periodic Notes) active
3. **Open timeline**: Ribbon → Day Planner icon, or Command Palette → `Show Timeline`
4. **Add tasks to your daily note** under a `# Day Planner` heading:
   ```markdown
   # Day Planner

   - [ ] 09:00 - 09:30 Morning review
   - [ ] 09:30 - 11:00 Deep work: Project Alpha
   - [ ] 11:00 - 11:15 BREAK
   - [ ] 11:15 - 12:00 Team standup
   - [ ] 14:00 - 15:00 1:1 with manager
   ```
5. **Optional — add calendar**: Settings → Day Planner → paste ICS link(s)

## Key Settings

| Setting | Description |
|---|---|
| **Internet Calendars** | Paste ICS URLs (one per line) — Google, iCloud, Outlook |
| **Show time tracker column** | Toggle experimental time tracking clock column in timeline |
| **Now marker** | Current time line indicator on the timeline |
| **Start / End hour** | First/last hour shown on the timeline (e.g., `7` / `20`) |
| **Timeline zoom** | Higher = more vertical space per hour |
| **Show completed tasks** | Grey out completed tasks on timeline |

### ICS Link Sources
| Service | How to Get ICS Link |
|---|---|
| Google Calendar | Settings → Integrate calendar → Public address in iCal format |
| iCloud Calendar | Share → Public calendar → Copy ICS link |
| Outlook | Settings → Calendar → Shared calendars → Publish → ICS |

## Task Format

### Daily Note Tasks
Place under a `# Day Planner` heading (exact, level-1) in your daily note:
```markdown
# Day Planner

- [ ] 09:00 - 09:30 Morning standup
- [ ] 09:30 - 11:00 Deep work: project X
  - [ ] Subtask 1
  - [ ] Subtask 2
- [ ] 11:00 - 11:15 BREAK
- [ ] 11:15 - 12:30 Code review
```

Rules:
- Format: `- [ ] HH:MM - HH:MM Task description`
- 24-hour time, dash separator with spaces (`HH:MM - HH:MM`)
- Must be under a `# Day Planner` heading (level-1, exact text)
- Subtasks supported via nested `- [ ]` below a timed task
- Untimed gaps treated as breaks

### Tasks Plugin Integration
Tasks from anywhere in your vault with a `scheduled` property appear on the timeline:
```markdown
- [ ] #task 08:00 - 10:00 Design review ⏳ 2026-05-01
```

Supported scheduled formats:
- `⏳ 2026-05-01` (Tasks shorthand)
- `[scheduled:: 2026-05-01]` (Dataview-style)
- `(scheduled:: 2026-05-01)` (parenthetical Dataview)

### Mode Comparison

| Mode | Source | Best For |
|---|---|---|
| **Daily Note** | `# Day Planner` heading in daily note | Quick daily time-blocking |
| **Tasks Plugin** | Any file, `#task` + `scheduled` + time range | Cross-vault task planning |
| **Internet Calendar** | ICS feed | External events on timeline |
| **Time Tracking** | Right-click task → Start clock | Logging actual time (experimental) |

## Views

| View | How to Open | What It Shows |
|---|---|---|
| **Timeline** | Ribbon icon or `Show Timeline` command | Single-day vertical timeline, drag-and-drop editable |
| **Multi-Day Planner** | Second ribbon icon or `Show multi-day planner` | Horizontal multi-day overview |
| **Mini-Timeline** | Status bar (always visible) | Upcoming 3 hours as colored blocks |

## Time Tracking (Experimental)

⚠️ **Experimental** — may break or change without warning.

1. Right-click a task in the editor → **Start clock**
2. Work on task — elapsed time shown in sidebar
3. Right-click active clock → **Stop** (records time) or **Cancel** (discards)
4. Clock time blocks appear as read-only entries in the timeline column

All actions available as commands for hotkey binding.

## Gotchas & Known Issues

- **Dataview is mandatory** — plugin errors on load if Dataview isn't enabled. Not optional.
- **`# Day Planner` heading must be exact** — level-1 heading, exactly `# Day Planner`. Different text or level breaks task detection.
- **Time format strict** — `HH:MM - HH:MM` with spaces around the dash. `09:00-10:00` (no spaces) may not parse correctly.
- **v0.7.0+ was a full rewrite** — completely changed UI/UX from the original James Lynch version. If you want the classic behavior (Pomodoro, simpler timeline), use the OG fork via BRAT: `ebullient/obsidian-day-planner-og`.
- **ICS links must end with `.ics`** — otherwise events won't load. If your provider gives a different URL, see GitHub issue #395 for workarounds.
- **Time tracking is read-only in timeline** — clock blocks can't be edited or resized yet.
- **Multi-day planner updates can lag** — may need a manual view refresh after editing tasks.
- **No Pomodoro timer** — removed in the modern version. OG fork still has it.
- **Drag-and-drop modifies the source note** — dragging a task on the timeline changes the time text in your note. Intentional but can surprise.
- **No time-zone support** — all times are local. Remote schedules need manual adjustment.
- **Plugin ID same as original** — `obsidian-day-planner` now points to Ivan Lednev's rewrite, not James Lynch's original.

## Works Well With
- [[Dataview]] — required dependency, powers task queries internally
- [[Tasks]] — rich task management, scheduled tasks feed into Day Planner timeline
- [[Periodic Notes]] — alternative to core Daily Notes for daily note creation
- [[BRAT]] — install the OG fork if you prefer the original classic version
- [[Calendar]] — visual daily note navigation alongside Day Planner
- [[Kanban]] — daily planning + kanban board for week-level sprint tracking
- [[Templater]] — pre-populate daily note template with a `# Day Planner` skeleton

## Related Skills
- [[Template Systems]] — daily note templates with pre-built schedule sections
- [[Kanban Workflows]] — connect daily time-blocking to weekly board planning

## Links
- [GitHub](https://github.com/ivan-lednev/obsidian-day-planner)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=obsidian-day-planner)
