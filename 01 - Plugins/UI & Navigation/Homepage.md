---
type: plugin
name: Homepage
category: UI & Navigation
status: active
complexity: low
downloads: 1M+
last-verified: 2026-05-01
tags:
  - plugin
  - ui
  - navigation
  - dashboard
  - landing-page
---

# Homepage

## What It Does
Opens a specified note, canvas, workspace, daily note, or random note every time Obsidian starts — instead of restoring your last open tabs. Gives you a consistent landing page every launch. Also provides an `Open homepage` command + ribbon button to return from anywhere in the vault.

**Key capabilities:**
- **8 homepage types**: File, Canvas, Workspace, Random Note, Graph View, Daily Note, Periodic Note, Nothing
- **Tab management**: Keep existing tabs, replace last tab, or close all on startup
- **View modes**: Reading, Source, Live Preview, or Default — with optional auto-revert
- **Commands on open**: Execute any Obsidian command after homepage loads
- **Mobile separate config**: Different homepage for mobile vs desktop
- **Ribbon icon**: One-click return to homepage

## When To Use It
- You want a consistent landing page every time Obsidian opens
- Your daily workflow starts at a Kanban board, Dataview dashboard, or daily note
- You're building a vault for others and want a guided entry point
- You want a keyboard shortcut to return to a home view from anywhere
- You use workspaces and want one to load on startup

## Minimal Setup
1. **Install**: Community Plugins → search "Homepage" by mirnovov → Install → Enable
2. **Create your home note** — e.g. `Dashboard.md`, a Kanban board, or a `.canvas` file
3. **Set the homepage**: Settings → Homepage → Homepage → type the exact note name (without `.md`)
4. **Toggle "Open on startup"**: On
5. **Test it**: Command Palette → "Homepage: Open Homepage" — or restart Obsidian

## Key Settings

| Setting | Options | Description |
|---|---|---|
| **Homepage type** | File / Canvas / Workspace / Random / Graph View / Daily Note / Periodic Note / Nothing | What kind of thing opens on startup |
| **Homepage** | (note name) | The specific note, canvas, or workspace to open |
| **Open on startup** | On / Off | Opens homepage when Obsidian launches |
| **Open when empty** | On / Off | Opens homepage when all tabs are closed |
| **Opening method** | Replace last tab / Keep existing tabs / Close all tabs | What happens to tabs from previous session |
| **View mode** | Reading / Source / Live Preview / Default | How the homepage note renders |
| **Revert view on navigation** | On / Off | Switch back to default view when opening other notes |
| **Pin homepage tab** | On / Off | Prevent the homepage tab from being closed |
| **Revert on close** | On / Off | Reset homepage tab if you navigate away |
| **Commands on open** | (list of commands) | Obsidian commands to run after homepage loads |
| **Ribbon icon** | On / Off | Show home icon in left ribbon |
| **Mobile settings** | Separate homepage config | Different note/behavior for mobile |

### Homepage Types Detail

| Type | Requires | Notes |
|---|---|---|
| **File** | — | Any `.md` note. Enter name without extension |
| **Canvas** | — | Any `.canvas` file. Enter name without extension |
| **Workspace** | Core Workspaces plugin | Opens a saved workspace layout |
| **Random File** | — | Opens a random note each startup |
| **Graph View** | — | Opens the global graph view |
| **Daily Note** | Core Daily Notes plugin | Opens today's daily note |
| **Periodic Note** | Periodic Notes plugin | Opens a weekly/monthly/quarterly note |
| **Nothing** | — | Opens a blank page on startup |

### Tab Handling Methods

| Method | Behavior | Best For |
|---|---|---|
| **Replace last tab** | Replaces the most recent tab with homepage | Single homepage, quick access |
| **Keep existing tabs** | Adds homepage as new tab alongside previous tabs | You want session restore + homepage |
| **Close all tabs** | Clears all previous tabs, opens only homepage | Clean slate every launch |

### Commands on Open
A powerful feature — execute any Obsidian command after the homepage loads. Example uses:
- `Dataview: Refresh all views` — refresh dynamic dashboards
- `Templater: Open today's daily note` — auto-create daily note
- `QuickAdd: Run capture macro` — prompt for quick capture on startup

Add multiple commands (one per line) in the settings field.

## Example Config / Usage

### Dataview dashboard as homepage
Create a note with Dataview queries for a live vault dashboard:
```markdown
# Dashboard

## Recent Notes
```dataview
TABLE file.cday as Created, file.mtime as Modified
SORT file.mtime DESC
LIMIT 10
```

## Open Tasks
```dataview
TASK
WHERE !completed
LIMIT 15
```

## Quick Links
- [[Kanban Board]]
- [[Today's Note]]
```
Settings → Homepage → Homepage → `Dashboard`

### Canvas as vault map homepage
1. Create a `.canvas` file with your vault structure as a visual map
2. Settings → Homepage type → File → Homepage → (canvas filename without extension)
3. Every launch opens the visual vault map

### Workspace as homepage
1. Set up a multi-pane workspace (e.g., dashboard + Kanban + calendar)
2. Settings → Homepage type → Workspace → Homepage → pick your workspace
3. Obsidian restores the full layout on launch

### Return to homepage hotkey
- Settings → Hotkeys → search "Homepage: Open Homepage" → assign `Alt+Home` or `Ctrl+Shift+H`

### Command-triggered startup macro
Settings → Commands on open:
```
Dataview: Refresh all views
QuickAdd: Capture to Inbox
```
Runs both commands automatically after every homepage load.

## Mobile Config
Homepage has a separate section in settings for mobile. You can set a different note, behavior, or disable it entirely on mobile. Useful because:
- Mobile screens don't suit dashboards the same way
- Workspace homepages can break sidebar rendering on mobile
- Can use a simpler note (e.g., just a Recents list) on phone

## Gotchas & Known Issues

- **Note name must be exact** — fuzzy matching exists but fails with similar names. Use full path (e.g., `00 - Dashboard/Home`) if ambiguous.
- **"Open on startup" overrides session restore** — tabs from last session won't restore. Set `Opening method` to `Keep existing tabs` if you want both.
- **No daily note auto-creation** — Homepage won't create a daily note if it doesn't exist. Use Periodic Notes + Templater for that.
- **Workspace homepage breaks mobile sidebar** — confirmed issue. Use a simpler homepage on mobile.
- **Conflicts with obsidian-tabs plugin** — can cause blank startup screen or view mode overrides. Disable auto-refresh in the Tabs plugin as workaround.
- **Canvas homepage silently fails** — if the canvas file is deleted or renamed, Homepage falls back to last open note with no warning.
- **"Open when empty" can conflict with workspace restore** — test carefully if you use both workspaces and homepage.
- **Commands on open timing** — commands run after the note renders. If your command depends on the note being fully loaded (e.g., Dataview refresh), small race conditions can occur.
- **High workspace count breaks dropdown** — GitHub issue #53: 30+ workspaces may cause the dropdown to show files instead of workspaces.
- **Pin is soft** — pinned homepage tab still lets you navigate away within that tab. It just prevents closing.

## Works Well With
- [[Dataview]] — Dataview dashboard is the ideal homepage for structured vaults
- [[Kanban]] — pin a Kanban board as homepage for project-first workflow
- [[Advanced Canvas]] — visual vault map as entry point
- [[Periodic Notes]] — link from homepage to today's daily note
- [[Calendar]] — pair with a homepage that includes a Dataview CALENDAR query
- [[Templater]] — auto-create daily note from homepage commands on open
- [[QuickAdd]] — run capture macros on startup via commands on open

## Related Skills
- [[Dashboards]] — designing effective homepage dashboards with Dataview
- [[Vault Architecture]] — structuring vaults around a homepage entry point

## Links
- [GitHub](https://github.com/mirnovov/obsidian-homepage)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=homepage)
