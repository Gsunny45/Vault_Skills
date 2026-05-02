---
type: plugin
name: Omnisearch
category: UI & Navigation
status: active
complexity: low
downloads: 1.4M+
last-verified: 2026-04-30
tags:
  - plugin
  - ui
  - navigation
  - search
  - full-text-search
---

# Omnisearch

> Plugin by Simon Cambier — a full-text search engine for Obsidian using BM25 ranking. Finds notes by content instantly, with better relevance ranking than Obsidian's built-in search. Also indexes PDF files and images (via OCR).

## What It Does

Omnisearch replaces or supplements Obsidian's default search with a faster, smarter engine. It uses the BM25 algorithm (the same approach as Elasticsearch and modern search engines) to rank results by relevance, not just recency.

Key features:
- **Instant results** — results appear as you type with no delay
- **BM25 relevance ranking** — more relevant notes appear first, not just recent ones
- **PDF indexing** — searches inside embedded PDF files
- **Image OCR** — optionally extracts and searches text from images (requires Tesseract)
- **In-note search** — search within the current note
- **Keyboard navigation** — full keyboard control, no mouse required
- **HTTP API** — external tools can query Omnisearch via REST

## When To Use It

- Your vault has grown to 200+ notes and Obsidian's built-in search feels slow or imprecise
- You embed PDFs and want to search their contents
- You want results ranked by relevance (not just "does it contain the word")
- Jumping to specific content quickly without knowing which note it's in
- Using the HTTP API to integrate vault search into external scripts (pairs well with REST API plugin)

## Minimal Setup

1. **Install**: Community Plugins → search "Omnisearch" by Simon Cambier → Install & Enable
2. **Open Omnisearch**: `Ctrl+Shift+O` (default hotkey), or Command Palette → "Omnisearch: Open Omnisearch"
3. Start typing — results appear instantly
4. Arrow keys to navigate results; Enter to open

That's the entire setup for basic use. Omnisearch indexes your vault automatically on install.

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Show Omnisearch in ribbon | On | Adds search icon to left ribbon |
| Hotkey | `Ctrl+Shift+O` | The main trigger; change if it conflicts |
| Fuzziness | `0` (off) | `0` = exact match only; `1` or `2` = allows typos. Start at 0. |
| Ignore diacritics | On | Treats "é" same as "e" — useful for multilingual vaults |
| Restrict to currently open note | Separate hotkey | "In-note search" searches only the active file |
| PDF indexing | On (if you use PDFs) | Indexes text layer of embedded PDFs |
| OCR on images | Off (default) | Requires Tesseract installed. Only enable if you need image text search. |
| HTTP server | Off | Enable only if you use the REST API integration |
| HTTP port | `51361` | Default port if HTTP server is enabled |
| Excluded folders | (set as needed) | Paths to exclude from indexing (templates, snippets) |

## Search Syntax

| Query | Matches |
|---|---|
| `dataview plugin` | Notes containing both words |
| `"dataview plugin"` | Exact phrase match |
| `dataview -plugin` | Notes with "dataview" but not "plugin" |
| `path:01 - Plugins dataview` | Search only within a folder path |
| `#plugin dataview` | Notes with `#plugin` tag containing "dataview" |

## Gotchas & Known Issues

- **Index builds on first install** — indexing a large vault takes 30-120 seconds on first run. Obsidian may feel sluggish during this period. Normal.
- **OCR requires Tesseract** — image text search won't work without installing Tesseract on Windows (`winget install Tesseract-OCR.Tesseract`). Only enable if you need it.
- **PDF indexing only works on PDFs with a text layer** — scanned PDFs without OCR layers won't return text results.
- **Fuzziness can cause false positives** — setting fuzziness to 2 matches too liberally for short words. Keep at 0 for precision.
- **HTTP API is localhost only by default** — external network access requires additional config. Good pairing with REST API plugin for local scripts.

## Works Well With

- [[REST API]] — pair Omnisearch's HTTP API with REST API scripts for combined search and note access
- [[Dataview]] — Omnisearch for finding notes; Dataview for structured queries on their metadata
- [[Homepage]] — add an Omnisearch shortcut to your dashboard

## Related Skills

- [[Vault Architecture]]

## Links

- [GitHub](https://github.com/scambier/obsidian-omnisearch)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=omnisearch)
