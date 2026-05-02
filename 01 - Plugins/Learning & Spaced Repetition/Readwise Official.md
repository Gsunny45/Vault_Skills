---
type: plugin
name: Readwise Official
category: Learning & Spaced Repetition
status: active
complexity: low
downloads: 217k+
last-verified: 2026-04-30
tags:
  - plugin
  - learning
  - readwise
  - highlights
  - sync
  - kindle
  - books
---

# Readwise Official

> Official Readwise plugin — automatically syncs your highlights from Kindle, Instapaper, Pocket, Twitter, web articles, and more into Obsidian as formatted Markdown notes.

## What It Does

Readwise aggregates reading highlights from many sources (Kindle, Instapaper, Pocket, web clipper, manual entry, etc.) into a unified library. The Readwise Official plugin syncs those highlights into your Obsidian vault as Markdown notes — one note per book, article, or source, with all your highlights inside.

Sync sources include: Kindle, Apple Books, Instapaper, Pocket, Twitter/X, Feedly, Matter, YouTube, PDFs, and more.

Key features:
- **Automated sync** — new highlights sync to Obsidian automatically (configurable interval)
- **Templated notes** — customize how each highlight note looks using Jinja2 templates
- **Metadata-rich frontmatter** — author, title, source URL, tags, category, date
- **Incremental sync** — only new/changed highlights sync after the first run
- **Filter by source** — sync only certain sources or books
- **Readwise Reader integration** — if you use Readwise Reader, all your reading flows into Obsidian

## When To Use It

- You use Kindle, Pocket, Instapaper, or Readwise Reader to read and highlight
- You want your book highlights, article annotations, and web clips in your PKM automatically
- Building a "literature notes from reading" system without manual copy-paste
- Creating a searchable library of your highlights with Dataview queries
- Connecting your reading habit to your note-taking system

**Requires a Readwise account** — free trial available; paid subscription ~$8/month.

## Minimal Setup

1. **Create a Readwise account**: [readwise.io](https://readwise.io) (free trial)
2. **Connect your reading sources** in Readwise (Kindle, Pocket, etc.) — done in the Readwise web app
3. **Install the plugin**: Community Plugins → search "Readwise Official" → Install & Enable
4. **Authenticate**: Settings → Readwise → Connect → paste your Readwise API token (from readwise.io/access_token)
5. **Set sync folder**: `Reference/Readwise` (or your preference)
6. **Initiate sync**: Command Palette → "Readwise: Initiate sync" — first sync imports all your existing highlights

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Readwise API token | (from readwise.io/access_token) | Required |
| Sync folder | `Reference/Readwise` | Where highlight notes are created |
| Sync interval (hours) | `1` | How often to check for new highlights |
| Sync on startup | On | Syncs when Obsidian opens |
| Template (book) | (customize) | Nunjucks template for book highlight notes |
| Template (article) | (customize) | Template for article/web clip notes |
| Filename date format | `YYYY-MM-DD` | How dates appear in filenames |

## Default Note Structure

Each synced source gets its own note:
```markdown
---
id: 12345678
updated: 2026-04-30T12:00:00+00:00
title: "Atomic Habits"
author: "James Clear"
source: kindle
category: books
num_highlights: 47
last_highlight_at: 2026-04-28
tags: [readwise, books]
---

# Atomic Habits
## Metadata
- Author: James Clear
- Category: books

## Highlights

### Chapter 1: The Surprising Power of Atomic Habits

> You do not rise to the level of your goals. You fall to the level of your systems.

**Note:** This is the core thesis. Focus on building systems, not goals.

---

> Every action you take is a vote for the type of person you wish to become.

---
```

## Gotchas & Known Issues

- **Requires paid Readwise subscription** — free trial available but the plugin requires a Readwise account to function after the trial.
- **Sync overwrites existing notes** — if you edit a synced note and Readwise re-syncs that source, your edits may be overwritten. Add your own notes in a separate section that the template preserves (use a `## My Synthesis` section after the highlights).
- **Large libraries take time on first sync** — syncing 500+ highlighted books generates a lot of files. Let the first sync complete without interrupting.
- **Privacy consideration** — your highlights are uploaded to Readwise's servers. If vault content is sensitive, evaluate accordingly.
- **Kindle notes need Wi-Fi** — Kindle highlights sync to Readwise only when the Kindle is connected to Wi-Fi and has synced with Amazon.

## Works Well With

- [[Dataview]] — query all your synced books: `FROM "Reference/Readwise" WHERE category = "books"` for a reading dashboard
- [[Spaced Repetition]] — turn important highlights into flashcards for active recall
- [[Smart Connections]] — Smart Connections will find semantic links between your highlights and your own notes
- [[Zotero Integration]] — Zotero for academic papers; Readwise for books and articles

## Related Skills

- [[AI Workflows in Obsidian]]
- [[Linking & Backlinks Strategy]]

## Links

- [GitHub](https://github.com/readwiseio/obsidian-readwise)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=readwise-official)
- [Readwise](https://readwise.io)
