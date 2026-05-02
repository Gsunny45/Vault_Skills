---
type: skill
name: Vault Architecture
category: Structure
difficulty: beginner
tags:
  - skill
  - structure
  - folder-design
  - naming
  - frontmatter
---

# Vault Architecture

## What This Skill Covers
How to design the folder structure, naming conventions, and frontmatter schemas for an Obsidian vault. A well-architected vault makes Dataview queries simpler, navigation faster, and maintenance easier over time.

## When You Need This
- Starting a new vault from scratch — get the structure right before adding content
- Your vault has grown disorganized — notes scattered across folders with inconsistent frontmatter
- You want to run Dataview queries but frontmatter fields are named differently across notes
- You're building a vault for a specific use case (music library, project management, knowledge base) and need a purpose-built structure

## Core Concepts

### Folder Structure Is Navigation, Not Taxonomy
Folders group notes by **where they live**, not what they are. Use folders for broad buckets (Songs, Albums, Playlists). Use frontmatter + tags for cross-cutting attributes (genre, mood, year).

```
Music Vault/
├── Songs/          ← all song notes live here
├── Albums/         ← all album notes live here
├── Playlists/      ← all playlist notes live here
├── Artists/        ← all artist notes live here
├── Templates/      ← reusable note templates
└── Dashboard/      ← query-driven dashboards
```

**Anti-pattern:** Nested folders by genre (`Songs/Rock/`, `Songs/Jazz/`). A song can have multiple genres — folders can't handle that. Use `#genre/rock` and `#genre/jazz` tags instead.

### Three-Tier Structure

| Tier | What | Example |
|------|------|---------|
| **Index** | Entry points, dashboards, MOCs | `Dashboard.md`, `Artists Index.md` |
| **Content** | The actual notes | Song notes, album notes, playlist notes |
| **Support** | Templates, scripts, attachments | `Templates/`, `Scripts/`, `Assets/` |

A minimal vault has all three. A complex vault may have multiple content folders.

### Frontmatter Schema Design

Frontmatter is the backbone of queryability. Define a schema per note type:

**Song note schema:**
```yaml
---
type: song
title: Come as You Are
artist: "[[Nirvana]]"
album: "[[Nevermind]]"
genre:
  - grunge
  - alternative
mood: melancholic
bpm: 120
year: 1991
rating: 5
duration: 3:39
---
```

**Rules:**
- Use `type:` to distinguish note types — makes Dataview filtering trivial
- Use arrays (`genre: [rock, blues]`) for multi-value fields
- Link related entities with `[[wiki links]]` in frontmatter
- Keep field names consistent across all notes of the same type
- Use lowercase-kebab-case for field names (`release-year` not `Release Year`)

## Step-by-Step

### Step 1 — Define the Purpose
One sentence. Example: "A vault to catalog my music collection — songs, albums, artists, and playlists — with browse-by-mood and playlist curation workflows."

### Step 2 — Identify Note Types
List every kind of note you'll create. For a music vault: `song`, `album`, `artist`, `playlist`, `genre`.

### Step 3 — Design Folders
Create one folder per note type at the root level. Add support folders:
```
Songs/
Albums/
Artists/
Playlists/
Genres/
Templates/
Dashboard/
```

### Step 4 — Define Frontmatter Schemas
For each note type, list the required and optional frontmatter fields. Keep required fields minimal — only fields you'll query against.

### Step 5 — Create Templates
Create a template note in `Templates/` for each note type with the frontmatter schema pre-filled. See [[Template Systems]] for how to set these up with Templater.

### Step 6 — Name Consistently
Use a consistent naming pattern for note titles:
- **Songs**: `Song Name (Artist)` — e.g., `Come as You Are (Nirvana)`
- **Albums**: `Album Name — Artist` — e.g., `Nevermind — Nirvana`
- **Artists**: Just the artist name — `Nirvana`
- **Playlists**: Descriptive name — `Late Night Jazz`, `Morning Run`

## Variations / Approaches

| Approach | Complexity | Best For |
|----------|------------|----------|
| **Flat** (all notes in one folder) | Beginner | Tiny vaults (<50 notes), quick capture |
| **By-type folders** (Songs/, Albums/, etc.) | Beginner | Medium vaults with clear note categories |
| **PARA** (Projects/Areas/Resources/Archives) | Intermediate | Task & project management vaults |
| **Zettelkasten** (atomic IDs, no folders) | Advanced | Pure knowledge management, lots of linking |
| **Hybrid** (type folders + tags for cross-cutting) | Intermediate | Most real-world vaults — the sweet spot |

## Example — Music Vault Folder Structure (Copy-Paste Ready)

```
Fat_Lady_Sings/
├── Songs/
├── Albums/
├── Artists/
├── Genres/
├── Playlists/
├── Templates/
├── Dashboard/
├── 00 - Inbox/
└── .obsidian/
```

## Common Mistakes
- **Nesting too deep** — `Songs/2025/Rock/` is hard to navigate and queries need longer `FROM` paths. Keep folders 1 level deep.
- **Inconsistent frontmatter** — `artist` in one note, `Artist` in another. Dataview treats these as different fields. Enforce with templates.
- **Mixing note types in one folder** — songs + albums + playlists in one folder means queries need extra filtering. Separate folders = clean `FROM` clauses.
- **No inbox** — new notes need a landing zone. Always include `00 - Inbox/` for uncategorized captures.

## Related Skills
- [[Template Systems]] — create templates that enforce frontmatter consistency
- [[Dashboards]] — query well-structured frontmatter for live dashboards
- [[Linking & Backlinks Strategy]] — link related entities across folders

## Related Plugins
- [[Templater]] — auto-fill frontmatter from templates on note creation
- [[QuickAdd]] — capture notes with preset frontmatter via quick capture
- [[Dataview]] — query frontmatter fields across your vault
- [[Linter]] — auto-format and validate frontmatter on save
