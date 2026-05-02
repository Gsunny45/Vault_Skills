---
type: plugin
name: Importer
category: Core Enhanced
status: active
complexity: low
downloads: 1.2M+
last-verified: 2026-04-30
tags:
  - plugin
  - core-enhanced
  - import
  - migration
  - evernote
  - notion
---

# Importer

> Official Obsidian plugin — imports notes from Evernote, Notion, Bear, HTML files, Roam Research, Logseq, and other formats into your Obsidian vault as Markdown files.

## What It Does

Importer is the official migration tool for bringing notes from other apps into Obsidian. It converts various export formats into clean Markdown files while preserving as much structure as possible (headings, lists, links, images, attachments).

Supported import sources:
- **Evernote** (`.enex` export files)
- **Notion** (HTML export or CSV)
- **Bear** (`.bear2bk` backup)
- **HTML files** (generic HTML → Markdown conversion)
- **Roam Research** (JSON export)
- **Logseq** (graph folder)
- **Microsoft OneNote** (via Microsoft Graph API)
- **Google Keep** (via Takeout JSON)
- **Day One** (JSON export)
- **Markdown files** (with frontmatter cleanup)
- **Text files** (`.txt`, `.rtf`)

## When To Use It

- Migrating from Evernote, Notion, or Bear to Obsidian
- Converting a folder of HTML files to Markdown notes
- Importing Google Keep notes to your vault
- One-time bulk import of external content — not for ongoing sync

## Minimal Setup

1. **Install**: Community Plugins → search "Importer" (by Obsidian) → Install & Enable
   - Note: this is an official plugin, may also be available under Core plugins in some versions
2. **Export your data from the source app** (required first):
   - Evernote: File → Export → All notes as ENEX
   - Notion: Settings → Export → Export all workspace content → Markdown & CSV
   - Google Keep: [takeout.google.com](https://takeout.google.com) → Keep → Export
3. **Run Importer**: Command Palette → "Importer: Open Importer"
4. **Select format** from the dropdown and locate your export file/folder
5. **Choose destination folder** in your vault
6. Click **Import**

## Import Notes by Source

### Evernote
- Export all notebooks as a single `.enex` file (or one per notebook)
- Attachments (PDFs, images) are extracted to an `attachments/` subfolder
- Tags become Obsidian tags in frontmatter
- Notebook structure isn't preserved as folders — all notes land in the destination folder

### Notion
- Export as "Markdown & CSV" from Notion workspace settings
- Sub-pages become sub-files, but the hierarchy may flatten depending on export depth
- Notion's database properties become frontmatter fields
- Inline images and embeds are extracted to an attachments folder

### HTML
- Any `.html` file or folder of HTML files
- Good for converting exported web pages, bookmarks, or OneNote HTML exports
- Link conversion is best-effort — internal links may not resolve correctly

### Roam Research
- Export as JSON from Roam settings
- Block references become plain text (no block ref IDs preserved)
- Page links convert to `[[wikilinks]]`

## Gotchas & Known Issues

- **Import is one-way** — Importer brings data into Obsidian but doesn't keep source apps in sync
- **Image/attachment paths may break** — complex nested attachment structures sometimes produce broken links. Check a sample of notes after import.
- **Formatting fidelity varies by source** — Notion → Markdown conversion preserves less than Evernote → Markdown. Expect some manual cleanup.
- **Large imports take time** — a 10,000-note Evernote vault import can take 10-30 minutes. Don't close Obsidian during import.
- **Duplicate imports** — running Importer twice imports the same notes twice. Check your destination folder before re-running.
- **Evernote ENEX quirks** — Evernote's HTML-in-XML format doesn't map perfectly to Markdown. Tables, code blocks, and colored text often need manual fixes.

## Works Well With

- [[Linter]] — run Linter after import to fix frontmatter, normalize headers, and clean up formatting inconsistencies
- [[Dataview]] — after importing, use Dataview to audit the imported notes (find ones missing tags, check title formats, etc.)
- [[Obsidian Git]] — commit the vault before and after a large import so you can roll back if something goes wrong

## Related Skills

- [[Vault Architecture]]

## Links

- [GitHub](https://github.com/obsidianmd/obsidian-importer)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=obsidian-importer)
