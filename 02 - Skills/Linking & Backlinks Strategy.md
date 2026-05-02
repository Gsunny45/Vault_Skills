---
type: skill
name: Linking & Backlinks Strategy
category: PKM
difficulty: beginner
tags:
  - skill
  - linking
  - backlinks
  - navigation
  - moc
---

# Linking & Backlinks Strategy

## What This Skill Covers
How to use wiki links, frontmatter links, and Maps of Content (MOCs) to create a navigable web of notes. Covers link placement strategies, link types, and patterns for maintaining link health in a growing vault.

## When You Need This
- Your notes are isolated — each note exists alone with no connections to others
- You want to navigate from a song to its album to the artist to similar songs
- You're building a vault where every note is discoverable through links, not just search
- You need to maintain link integrity as the vault grows

## Core Concepts

### Links Create Navigation Paths
A link is a path from one note to another. Every link creates a backlink. The web of links is your vault's navigation system — it should be intentional, not accidental.

For a music vault, links connect:
```
Song → Album (which album is this song on?)
Song → Artist (who performs this?)
Album → Artist (who made this?)
Song → Genre (what genre is this?)
Playlist → Song (what's in this playlist?)
```

### Three Places to Put Links

| Location | When to Use | Example |
|----------|-------------|---------|
| **In frontmatter** | Relating entities at the metadata level | `artist: [[Nirvana]]` in a song note |
| **In body text** | Contextual references, commentary | "This track from [[Nevermind]] changed everything." |
| **In lists/bullets** | Tracklists, reading lists, collections | `- [[Come as You Are (Nirvana)]]` in a playlist |

**Rule of thumb:** Use frontmatter links for structural relationships (song → artist, song → album). Use body links for contextual mentions and commentary.

### Maps of Content (MOCs)
An MOC is a note that links to many other notes around a theme. It's an index page you maintain manually.

```
# Grunge Playlist MOC

## Essential Grunge Songs
- [[Smells Like Teen Spirit (Nirvana)]]
- [[Come as You Are (Nirvana)]]
- [[Even Flow (Pearl Jam)]]
- [[Black Hole Sun (Soundgarden)]]

## Grunge Artists
- [[Nirvana]]
- [[Pearl Jam]]
- [[Soundgarden]]
```

MOCs are better than Dataview queries for curated collections (playlists, reading lists, project boards) where human curation matters more than automated filtering.

## Step-by-Step

### Step 1 — Identify Entity Types
List what kinds of things your notes represent:
- Song, Album, Artist, Genre, Playlist

### Step 2 — Define Link Relationships
For each pair, decide which direction links go:

| Source | Links To | How |
|--------|----------|-----|
| Song | Artist, Album | Frontmatter: `artist: [[Nirvana]]` |
| Album | Artist | Frontmatter: `artist: [[Nirvana]]` |
| Playlist | Song | Body list: `- [[Song Name]]` |
| Genre | Song, Artist | MOC note: curated lists |

Don't link both directions. If Song links to Artist, the backlink from Artist to Song is automatic via Obsidian's Backlinks pane. Duplicating it wastes maintenance effort.

### Step 3 — Use Naming for Link Consistency
Link text must match the target note's filename exactly. Consistent naming prevents broken links:

```
Song notes:    `Come as You Are (Nirvana).md`
Album notes:   `Nevermind — Nirvana.md`
Artist notes:  `Nirvana.md`
```

Then in frontmatter:
```yaml
artist: "[[Nirvana]]"           # matches Nirvana.md
album: "[[Nevermind — Nirvana]]" # matches Nevermind — Nirvana.md
```

### Step 4 — Build MOCs for Curated Collections
Create an MOC for anything that needs human curation:
- Playlists (which songs belong together?)
- Genre indexes (which songs define this genre?)
- Mood collections (songs for a rainy day)

Dataview handles automated lists (show all songs by an artist). MOCs handle curated lists (these 12 songs make a great running playlist).

### Step 5 — Check Link Health
- Broken links show as `[[Unresolved link]]` in Obsidian
- Backlinks pane shows orphaned notes (notes with no incoming links)
- The Dataview query `LIST WHERE length(file.inlinks) = 0` finds all orphaned notes

## Variations / Approaches

| Approach | Effort | Best For |
|----------|--------|----------|
| **Frontmatter-only links** | Low | Machine-queryable relationships, dashboards |
| **Body links** | Medium | Context-rich notes, narrative connections |
| **MOC-based** | Medium | Curated collections, playlists, reading lists |
| **Full bidirectional web** | High | Knowledge bases, Zettelkasten, research vaults |

## Example — Music Vault Link Structure

```
Artist: Nirvana.md
  ↑ frontmatter: artist    ↑ frontmatter: artist
  │                         │
Song: Come as You Are     Album: Nevermind — Nirvana.md
  ← frontmatter: album ────┘
  │
  └── body link in: Grunge Playlist MOC.md (curated playlist)
```

## Common Mistakes
- **Linking both directions** — if Song links to Artist and Artist links back to Song, you maintain links in two places. Let backlinks do the reverse direction automatically.
- **Broken links from naming drift** — renaming `Nirvana.md` to `Nirvana (band).md` breaks all `[[Nirvana]]` links. Use Obsidian's "Rename file" command (right-click → Rename) — it updates all links automatically.
- **No MOCs for curation** — relying entirely on Dataview queries means you can't hand-pick song order for a playlist. MOCs give you manual control.
- **Orphaned notes** — notes with no incoming links and no MOC entry are invisible. Run the orphan query periodically.

## Related Skills
- [[Vault Architecture]] — folder structure and naming conventions that make links reliable
- [[Dashboards]] — Dataview queries that surface backlink data
- [[Template Systems]] — templates that auto-generate links in frontmatter

## Related Plugins
- [[Dataview]] — query link structures: `file.inlinks`, `file.outlinks`, orphan detection
- [[Templater]] — auto-link frontmatter fields to related note filenames
