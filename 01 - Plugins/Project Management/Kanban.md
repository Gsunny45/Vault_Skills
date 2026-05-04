---
type: plugin
name: Kanban
category: Project Management
status: active
complexity: low
downloads: 2.2M+
last-verified: 2026-04-29
tags:
  - plugin
  - project-management
  - kanban
  - board
  - workflow
---

# Kanban

## What It Does
Turns any Markdown file into a visual Kanban board with drag-and-drop columns and cards. Boards are stored as plain Markdown — no proprietary format, no external service. Each board is a single `.md` file with YAML frontmatter that the plugin renders as interactive lanes and cards. Switch between the visual board view and raw Markdown at any time with Ctrl+K.

## When To Use It
- Tracking task progress through stages (To Do → In Progress → Done)
- Sprint planning or project milestone tracking
- Personal workflow management (content pipeline, writing stages, learning queues)
- Visualizing any sequential or parallel process with columns
- Lightweight project management without leaving Obsidian

## Minimal Setup
1. **Install**: Community Plugins → search "Kanban" by mgmeyers → Install & Enable
2. **Create a board**: Command Palette → "Kanban: Create new board" → name your file
3. **Add columns**: Click "+" at the right of the board → name your lane
4. **Add cards**: Click "+" at the bottom of a lane → type your card content
5. **Toggle view**: `Ctrl+K` (default) switches between Kanban view and Markdown source

**Alternative — manual board creation:**
Create a `.md` file with this frontmatter (must be the very first thing in the file):
```yaml
---
kanban-plugin: board
---
```
Then open the file, click the ⋮ menu → "Open as Kanban".

## Key Settings

Settings operate at two levels: **Global** (Settings → Kanban, applies to all boards) and **Board-specific** (⋮ → Board Settings, overrides global for that board).

| Setting | Recommended Value | Notes |
|---|---|---|
| New line trigger | `Shift+Enter` | Prevents accidental card submission when you want a new line |
| New card insertion | Append (bottom) | New cards appear at bottom of lane — more natural progression |
| Lane width | `272px` (default) | Increase to `320px–350px` for boards with detailed cards |
| Show card count | On | Shows count per lane header |
| Date format | `YYYY-MM-DD` | Consistent with Obsidian date format |
| Show relative dates | On | Shows "2 days ago" / "in 3 days" — useful at a glance |
| Date trigger | `@` (default) | Type `@` (or configured trigger) in a card to open the date picker |
| Link dates to daily notes | Off | On = dates become `[[2026-04-29]]` links |
| Display card checkbox | On | Renders `- [ ]` as clickable checkboxes; Ctrl+click archives the card |
| Move tags to footer | Off | Tags inline with body text is more natural |
| Tag click action | Search board | Keeps search scoped rather than searching entire vault |
| Max archive size | `-1` (unlimited) | Archive stores completed/stale cards without deleting |
| Archive with date | On | Adds date stamp when archiving |
| New note template | (path to template) | Template used when creating a note from a card |
| New note folder | (vault folder) | Default folder for notes created from cards |

### Board-Specific Override Example
In the board's Markdown source, settings are stored in a JSON code block below the frontmatter:
```
---
kanban-plugin: board
---

%% kanban:settings
```
{"lane-width": 320, "show-checkboxes": true, "hide-card-count": false}
```
%%
```
Open the board → ⋮ → Board Settings to edit these visually.

## Example Board Structure

**Markdown source of a simple board:**
```markdown
---
kanban-plugin: board
---

## To Do

- [ ] Research authentication options @{2026-05-15} #research
- [ ] Draft architecture document @{2026-05-20} #planning
- [ ] Set up CI/CD pipeline

## In Progress

- [ ] Build API endpoint @{2026-05-01} #dev
- [ ] Write unit tests #testing

## Done

- [x] Project kickoff meeting
- [x] Requirements gathering
```

**How the plugin interprets this:**
- `## H2 headings` → column/lane headers
- `- ` bullet lists → cards
- `- [ ]` / `- [x]` → checkable task cards
- `@{YYYY-MM-DD}` → date metadata (displayed in card footer with relative labels)
- `#tag` → tag (with custom color if configured)
- `[[wikilinks]]` → linked notes (shows backlinks in graph view)

## Board CSS Classes

Add to frontmatter to change layout:

```yaml
---
kanban-plugin: board
cssclass: kanban-plugin__vertical
---
```

| Class | Effect |
|---|---|
| `kanban-plugin__vertical` | Stacks columns vertically instead of scrolling horizontally |
| `collapse-horizontal` | Collapses column headers horizontally |
| `collapse-vertical` | Collapses column headers vertically |

## Custom CSS Snippets

Create a CSS snippet (Settings → Appearance → CSS snippets) to override styles:

```css
/* Card styling */
.kanban-plugin__item {
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

/* Wider lanes */
.kanban-plugin {
  --lane-width: 320px;
}
```

### Tag Colors (No CSS Needed)
Settings → Kanban → Tag colors — assign custom background/text colors per tag (e.g., `#urgent` → red).

## Gotchas & Known Issues

- **Plugin is seeking maintainers**: The repo has 500+ open issues and the original maintainer (mgmeyers) has stepped back. Development is slow. See the GitHub repo for maintainer status.
- **Dataview inline field `due` not recognized**: The inline field `[due::...]` doesn't render in card footers. Use the simpler `due:` syntax instead. (GitHub issue #1080)
- **Keyboard shortcuts may break after switching views**: Switching from Kanban to Markdown view can leave keyboard shortcuts blocked. Reload Obsidian to fix. (GitHub issue #1132)
- **Avoid embedding Tasks plugin queries in cards**: Embedding a `not done` Tasks query inside a Kanban card can freeze the UI. Use file embedding (`![[Search]]`) instead.
- **Plugin loading order matters**: If Kanban loads before some other plugins, link-clicking may break. Edit `community-plugins.json` so Kanban loads last if you see conflicts.
- **Board may render as list after updates**: Can happen after plugin updates or cross-device sync conflicts. Re-enable the plugin or restore community plugin settings to fix.
- **No built-in swimlanes or board embedding**: These are frequently requested features that don't exist yet. Consider using inline filters or linked boards as a workaround.
- **Cards are individual items, not separate notes**: By default, cards live inside the board file. Use "Create note from card" (right-click) to promote a card to its own note.
- **Frontmatter must be first**: The `kanban-plugin: board` frontmatter must be the very first thing in the file — no blank lines, no text before it, or the plugin won't recognize the board.

## Works Well With
- [[Tasks]] — Tasks plugin for rich task queries across your vault; Kanban for visual organization
- [[Templater]] — Create board templates with pre-configured lanes and card templates
- [[Dataview]] — Use Dataview queries to surface tasks and metadata alongside your boards
- [[QuickAdd]] — Capture quick tasks into a specific board lane via macros
- [[Homepage]] — Pin your main Kanban board as a homepage view
- [[Copilot]] — Ask AI to read/project plan based on board content

## Related Skills
- [[Kanban Workflows]] — lane design, card hygiene, cross-plugin integration, CLI automation with kanban-tools.py

## Links
- [GitHub](https://github.com/mgmeyers/obsidian-kanban)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=obsidian-kanban)
- [Official Documentation](https://obsidian-kanban.vercel.app/)
