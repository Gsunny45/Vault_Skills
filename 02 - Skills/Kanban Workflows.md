---
type: skill
name: Kanban Workflows
category: Project Management
difficulty: beginner
tags:
  - skill
  - kanban
  - project-management
  - workflow
  - board-design
---

# Kanban Workflows

## What This Skill Covers
How to design and maintain Kanban boards in Obsidian that actually work — lane strategies, card hygiene, cross-plugin workflows (Tasks, Dataview, Templater), and CLI automation. You'll learn how to turn a flat list of tasks into a living project board you can trust at a glance.

## When You Need This
- Your Kanban board has 20+ cards and you're losing track of what matters
- You're not sure how many lanes to use or what to call them
- You want cards to show dates, tags, and linked notes without manual formatting
- You need to batch-update or query board data from outside Obsidian
- You want to integrate Kanban boards with the Tasks plugin for richer task queries
- You're syncing boards across devices and hitting plugin-state corruption

## Core Concepts

### Kanban Is a Pull System, Not a Push System
The board should reflect reality, not wishful thinking. Cards move right only when work actually starts or finishes. Don't pre-fill "Done" — let the board show where things *are*.

### Two Levels of Configuration
The Kanban plugin has **Global settings** (Settings → Kanban) that apply to all boards, and **Board-specific settings** (⋮ → Board Settings) stored in each board's `%% kanban:settings` block. Board settings override global ones. Design your global defaults for your most common board type, then override per-board.

### Cards Are Markdown First
Everything in a Kanban board is plain Markdown. The plugin parses:
- `## H2` → lane header
- `- [ ] item` → unchecked card
- `- [x] item` → checked card
- `@{2026-04-29}` → date (renders with relative labels, color rules)
- `#tag` → tag (custom colors in settings)
- `[[wikilink]]` → linked note
- `***` → archive boundary
- `%% kanban:settings` → board-specific JSON config

This means you can edit boards in any text editor and the plugin will render them.

## Step-by-Step

### Step 1 — Design Your Lane Architecture

Too few lanes and everything blurs together. Too many and the board becomes noise. Here are three proven lane templates:

**Simple (3 lanes):** `Next Up` / `In Progress` / `**Complete**`
Best for: Personal task tracking, content pipelines, solo work.

**Standard (5 lanes):** `Backlog` / `Next Up` / `In Progress` / `Review` / `**Complete**`
Best for: Small projects, feature work, most Obsidian boards.

**Full (7 lanes):** `Icebox` / `Backlog` / `Ready` / `In Progress` / `Review` / `Deployed` / `**Complete**`
Best for: Multi-person projects, release management, anything with a QA gate.

Rules of thumb:
- Lane order = workflow order (left to right)
- `**Complete**` as the final lane auto-checks cards dropped on it
- `***` + `## Archive` below it for truly finished work
- Backlog is a holding area — limit it to 10-15 cards or it becomes a graveyard

### Step 2 — Set Card Hygiene Standards

Every card should answer: *what, by when, where does it link?*

```
- [ ] **Task name** @{2026-05-01} #project-tag
  Context or description line
  See: [[related-note]]
```

| Element | Why | Plugin Benefit |
|---------|-----|----------------|
| `**Bold title**` | Skimmable at a glance | Renders as card title |
| `@{date}` | Deadlines visible | Relative dates ("in 3 days"), color rules |
| `#tag` | Filtering + color coding | Tag pills with custom colors |
| `[[link]]` | Connects to vault content | Backlinks in graph, one-click navigation |
| Indented body | Details without clutter | Collapsed in card, expands on click |

### Step 3 — Configure Global Settings

Settings → Kanban — set these once:

| Setting | Value | Why |
|---------|-------|-----|
| New line trigger | `Shift+Enter` | Enter submits card, Shift+Enter adds line |
| New card insertion | `Append` | New cards go to bottom = natural progression |
| Date format | `YYYY-MM-DD` | Matches Obsidian daily notes, sorts correctly |
| Show relative dates | On | "In 3 days" is faster to read than a date |
| Tag click action | `Search Kanban Board` | Keeps search scoped, not vault-wide |
| Display card checkbox | On | Visual completeness indicator |
| Link dates to daily notes | Off | Only enable if you use daily notes |

### Step 4 — Set Up Board-Specific Overrides

Open any board → ⋮ → Board Settings. Override when:
- A board has unusually detailed cards → increase `Lane width` to 320-350px
- A board is for quick capture → set `New card insertion` to `Prepend`
- A board needs different tag colors or date colors than the global default

Example settings block (auto-generated when you change settings in the UI):
```
%% kanban:settings
```
{"lane-width":340,"show-relative-date":true,"date-format":"YYYY-MM-DD","tag-colors":[{"tag":"#florisvault","color":"rgba(99,102,241,1)","backgroundColor":"rgba(99,102,241,0.15)"},{"tag":"#automation","color":"rgba(34,197,94,1)","backgroundColor":"rgba(34,197,94,0.15)"}]}
```
%%
```

### Step 5 — Archive Correctly

Archiving keeps the board clean without losing history.

**Manual archive:** Right-click a card → "Archive card". Moves it below the `***` separator in the `## Archive` lane.

**Auto-archive:** Drag a card to the `## **Complete**` lane. It auto-checks to `- [x]`. Then use the "Archive completed cards" button (or command palette) to sweep all checked cards to Archive at once.

**Archive settings:** Settings → Kanban → `Maximum number of archived cards`. Set to `-1` (unlimited) if you want a full history. Set to `100` or `500` to auto-prune old entries.

### Step 6 — View Switching

The plugin supports four views for the same data:

| View | Command | Best For |
|------|---------|----------|
| Board | `View as board` | Default: visual columns, drag-and-drop |
| Table | `View as table` | Sorting by date, filtering, spreadsheet-style review |
| List | `View as list` | Compact vertical layout, focus on card text |
| Markdown | `Open as markdown` | Bulk editing, search/replace, git diffs |

Use `Ctrl+K` (if configured) to toggle between Board and Markdown instantly.

### Step 7 — Cross-Plugin Integration

**Kanban + Tasks Plugin**
The Tasks plugin's query block can search across all Kanban boards:
```markdown
\`\`\`tasks
not done
path includes Project Board
group by folder
\`\`\`
```
⚠️ Known issue: don't embed Tasks *inside* a Kanban card — it can freeze Obsidian. Query the board file instead.

**Kanban + Dataview**
```dataview
TABLE due, priority, status
FROM "01-Projects"
WHERE contains(file.frontmatter.tags, "florisvault")
SORT due ASC
```
This shows all Kanban-adjacent notes. Dataview doesn't read Kanban cards directly (they're list items, not frontmatter), but it queries notes *linked from* cards.

**Kanban + Templater**
Create a board template note with pre-configured lanes and settings:
```
---
kanban-plugin: board
---

## Backlog

## Next Up

## In Progress

## Review

## **Complete**

***

## Archive

%% kanban:settings
```
{"lane-width":320,"show-relative-date":true}
```
%%
```
Save as a Templater template, then use it to stamp out new boards instantly.

## Example Board (Full-Featured)

```markdown
---
kanban-plugin: board
---

## Backlog

- [ ] **Research auth options** @{2026-06-01} #research
  OAuth vs API keys vs JWTs
  See: [[auth-comparison]]

- [ ] **Write onboarding docs** @{2026-06-15} #documentation

## Next Up

- [ ] **Draft architecture** @{2026-05-10} #planning
  See: [[ADR-001]]

## In Progress

- [ ] **Build API endpoint** @{2026-05-01} #dev
  Implement POST /v1/ingest

## Review

- [x] **Unit tests for parser** @{2026-04-28} #dev

## **Complete**

- [x] **Project kickoff** @{2026-04-20} #planning

***

## Archive

- [x] **Initial research** @{2026-04-15} #research

%% kanban:settings
```
{"lane-width":320,"show-relative-date":true,"date-format":"YYYY-MM-DD","new-card-insertion-method":"append","tag-action":"search-board","tag-colors":[{"tag":"#dev","color":"rgba(59,130,246,1)","backgroundColor":"rgba(59,130,246,0.15)"},{"tag":"#planning","color":"rgba(234,179,8,1)","backgroundColor":"rgba(234,179,8,0.15)"},{"tag":"#research","color":"rgba(168,85,247,1)","backgroundColor":"rgba(168,85,247,0.15)"}]}
```
%%
```

## CLI Automation

The REST API plugin exposes the vault via HTTP. Use the `kanban-tools.py` script in `05 - Snippets/Scripts/` to manage boards from the command line:

```powershell
python 05-Snippets/Scripts/kanban-tools.py list                    # List all Kanban boards
python 05-Snippets/Scripts/kanban-tools.py show "Project Board"    # Show board summary
python 05-Snippets/Scripts/kanban-tools.py add "Project Board" --lane "Next Up" --card "New task" --date 2026-05-15 --tag planning
python 05-Snippets/Scripts/kanban-tools.py move "Project Board" --card "New task" --to "In Progress"
python 05-Snippets/Scripts/kanban-tools.py archive "Project Board"                # Archive all completed cards
python 05-Snippets/Scripts/kanban-tools.py validate "Project Board"               # Check board syntax
python 05-Snippets/Scripts/kanban-tools.py stats "Project Board"                  # Card counts per lane
python 05-Snippets/Scripts/kanban-tools.py overdue                                # Show all overdue cards across all boards
```

## Variations / Approaches

| Approach | Complexity | Best For |
|----------|------------|----------|
| Single board, 3 lanes | Beginner | Personal task tracking, daily workflow |
| Single board, 5-7 lanes | Intermediate | Sprint planning, feature development |
| Multiple linked boards | Intermediate | Multiple projects, each with its own board |
| Board + Tasks plugin combo | Advanced | Rich queries across all boards (due dates, priorities, recurring) |
| Board + Dataview dashboard | Advanced | Live summary dashboard showing cards from multiple boards |
| CLI-automated board | Advanced | Batch operations, CI/CD pipeline integration, AI-driven card creation |

## Common Mistakes

- **Too many Backlog cards** — a backlog over 15 items is a graveyard. Archive or delete anything you won't touch in the next 2 weeks.
- **No dates on cards** — without `@{date}` you lose relative date display, overdue color rules, and sorting by deadline.
- **Wrong date syntax** — use `@{2026-05-01}` not `Due: 2026-05-01` (the plugin ignores the latter).
- **Embedding Tasks queries in cards** — puts a Tasks plugin query *inside* a Kanban card line. This can freeze Obsidian. Query the board file from outside instead.
- **Frontmatter not first** — `kanban-plugin: board` must be the very first thing in the file, no blank lines before it.
- **Editing board settings by hand** — the `%% kanban:settings` JSON block is auto-generated. Use the UI (⋮ → Board Settings) or the `kanban-tools.py` script instead of hand-editing JSON.
- **Not using the Archive** — completed cards pile up and make the board noisy. Archive regularly.
- **Syncing without version control** — Obsidian Git or similar prevents board corruption from sync conflicts.

## Related Skills
- [[Dashboards]] — build a Dataview dashboard that shows cards from all your boards
- [[Dataview Dashboard Patterns]] — advanced Dataview queries for project tracking
- [[REST API Automation]] — connect CLI tools to your vault for batch board operations
- [[Template Systems]] — create board templates with Templater for rapid project setup

## Related Plugins
- [[Kanban]] — the Obsidian Kanban plugin (setup, settings, gotchas)
- [[Tasks]] — rich task queries across vault, complementary to Kanban visual boards
- [[Dataview]] — query notes linked from Kanban cards, build dashboards
- [[Templater]] — create board templates with pre-configured lanes
- [[QuickAdd]] — capture quick tasks into a specific board lane via macros
- [[REST API]] — enable CLI automation for board management
- [[Obsidian Git]] — version control prevents board corruption from sync conflicts
