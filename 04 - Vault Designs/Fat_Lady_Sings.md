---
type: vault-design
name: Fat_Lady_Sings
use-case: Music playlist management — catalog songs, albums, artists, and curate playlists
complexity: low
tags:
  - vault-design
  - music
  - playlist
---

# Vault Design — Fat_Lady_Sings

> Test vault built from Vault_Skills skill notes. Purpose: verify that the skill notes can bootstrap a real vault.

## Purpose & Use Case
A personal music catalog vault for logging songs, organizing by album/artist/genre/mood, and curating playlists. Browse by mood, BPM range, rating, or genre. Maintain curated playlists as Maps of Content.

## Layered Build Plan

### Layer 1 — Vault Architecture (Skill: [[Vault Architecture]])
- Create folder structure: Songs/, Albums/, Artists/, Genres/, Playlists/, Templates/, Dashboard/, 00 - Inbox/
- No deep nesting — all content folders are flat

### Layer 2 — Templates (Skill: [[Template Systems]])
- Song template with frontmatter: type, title, artist, album, genre[], mood, bpm, year, rating, duration
- Album template: type, title, artist, year, genre[]
- Playlist template: type, title, mood, genre[], created
- Use Templater for dynamic prompts (mood suggester, date auto-fill)

### Layer 3 — Plugin Configuration
- Install & configure: Dataview, Templater, QuickAdd, Homepage, Kanban
- Dataview: Enable JavaScript queries, inline queries
- Templater: Set template folder, enable trigger on new file
- QuickAdd: Capture shortcut for rapid song entry
- Homepage: Point to Dashboard.md
- Kanban: Template for playlist curation board

### Layer 4 — Seed Data (3 albums, 10+ songs, 3 playlists)
- Album: "Kind of Blue" — Miles Davis (jazz, 1959)
- Album: "Dummy" — Portishead (trip-hop, 1994)
- Album: "Random Access Memories" — Daft Punk (electronic/funk, 2013)
- Playlists: "Late Night Jazz", "Morning Run", "Rainy Day"

### Layer 5 — Dashboards (Skill: [[Dashboards]])
- Dashboard.md with sections:
  - Songs by mood (Dataview TABLE grouped by mood)
  - Songs by BPM range (filtered for running vs chill)
  - Highest rated songs
  - Recently added songs
  - Open tasks (songs needing mood/BPM filled in)

### Layer 6 — Kanban Curation (Skill: [[Kanban Workflows]])
- Playlist track curation board: Discover → Try → In Rotation → Retired

### Layer 7 — Homepage & Polish
- Set Dashboard.md as homepage
- Verify all links resolve
- Verify Dataview queries return results
- Test QuickAdd capture

## Folder Structure
```
Fat_Lady_Sings/
├── 00 - Inbox/           ← QuickAdd capture landing zone
├── Songs/                ← Individual song notes
├── Albums/               ← Album notes with tracklist links
├── Artists/              ← Artist biography/notes
├── Genres/               ← Genre MOC notes
├── Playlists/            ← Curated playlist MOCs
├── Templates/            ← Templater templates (tpl-song.md, etc.)
├── Dashboard/            ← Dataview query dashboards
└── Kanban/               ← Kanban boards for playlist curation
```

## Required Plugins
| Plugin | Role | Skill Reference |
|--------|------|----------------|
| Dataview | Query songs by mood, genre, BPM, rating | [[Dashboards]] |
| Templater | Dynamic song/album/playlist templates | [[Template Systems]] |
| QuickAdd | Rapid song capture with preset frontmatter | [[Template Systems]] |
| Homepage | Dashboard as landing page | [[Dashboards]] |
| Kanban | Playlist curation board | [[Kanban Workflows]] |

## Optional Plugins
| Plugin | Role |
|--------|------|
| Linter | Auto-format frontmatter on save |
| Style Settings | Theme customization |

## Key Templates Used
- `Templates/tpl-song.md` — from [[Template Systems]]
- `Templates/tpl-album.md`
- `Templates/tpl-playlist.md`

## Core Workflows
1. **Quick capture**: `Ctrl+Shift+S` → enter song name + artist → lands in Inbox
2. **Full catalog**: Templater song template with mood suggester, BPM entry
3. **Browse by mood**: Dashboard query showing songs grouped by mood
4. **Curate playlist**: MOC note with hand-picked tracklist + Kanban board for rotation stages

## Frontmatter Schemas

### Song
```yaml
type: song
title: Come as You Are
artist: "[[Nirvana]]"
album: "[[Nevermind — Nirvana]]"
genre: [grunge, alternative]
mood: melancholic
bpm: 120
year: 1991
rating: 5
duration: 3:39
created: 2026-05-02
```

### Album
```yaml
type: album
title: Nevermind
artist: "[[Nirvana]]"
year: 1991
genre: [grunge, alternative]
rating: 5
created: 2026-05-02
```

### Playlist
```yaml
type: playlist
title: Late Night Jazz
mood: calm
genre: [jazz]
created: 2026-05-02
songs: []
```

## Key Dataview Queries

### Songs by mood
```dataview
TABLE mood, bpm, year, rating
FROM "Songs"
WHERE type = "song"
SORT mood ASC, rating DESC
```

### Running playlist (BPM 120-160)
```dataview
TABLE bpm, mood, rating
FROM "Songs"
WHERE type = "song" AND bpm >= 120 AND bpm <= 160
SORT bpm ASC
```

### Recently added
```dataview
TABLE artist, year, rating
FROM "Songs"
WHERE type = "song"
SORT created DESC
LIMIT 10
```

### Songs needing metadata
```dataview
TABLE artist, mood, bpm
FROM "Songs"
WHERE type = "song" AND (mood = null OR bpm = null)
```

## Setup Steps
1. Create folder structure (Layer 1)
2. Create templates (Layer 2)
3. Install and configure plugins (Layer 3)
4. Seed data — create artist → album → song notes (Layer 4)
5. Build Dashboard.md with Dataview queries (Layer 5)
6. Create Kanban curation board (Layer 6)
7. Set homepage, test everything (Layer 7)

## Test Criteria
- [ ] Dashboard loads without errors
- [ ] All Dataview queries return rows
- [ ] Song templates prompt for mood/BPM
- [ ] QuickAdd capture lands in Inbox
- [ ] Links resolve: Song → Album → Artist
- [ ] Kanban board renders with columns

## Notes & Gotchas
- This vault tests whether Vault_Skills skill notes are sufficient to bootstrap a real vault from scratch
- Fat_Lady_Sings is a separate vault at `C:\Users\MarsBase\Music\Fat_Lady_Sings`
- Use the skill notes as reference during each layer, not just this design doc

## Related Vault Designs
- (none yet — this is the first)
