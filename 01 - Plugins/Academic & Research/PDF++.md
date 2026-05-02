---
type: plugin
name: PDF++
category: Academic & Research
status: active
complexity: medium
downloads: 493k+
last-verified: 2026-04-30
tags:
  - plugin
  - academic
  - pdf
  - annotation
  - research
  - highlighting
---

# PDF++

> Plugin by ryotaushio — advanced PDF viewing and annotation inside Obsidian. Highlights, annotations, and backlinks from PDFs are stored as Markdown — searchable, linkable, and queryable with Dataview.

## What It Does

PDF++ supercharges Obsidian's built-in PDF viewer with annotation, deep-linking, and manipulation capabilities. Highlights are stored as Markdown links in your notes — click the link to jump back to the exact page and position in the PDF. No proprietary JSON; your annotations are plain text and survive any plugin issues.

**Key features:**

**Annotation & Linking:**
- **Highlight and annotate** PDFs with color-coded highlights — colors set via `&color=red` in link text
- **Copy links to PDF selections** — paste `[[file.pdf#page=5&selection=...]]` into any note
- **Backlink highlighting** — links to PDF selections render as highlighted annotations in the PDF viewer
- **Bidirectional hover sync** — Ctrl/Cmd+hover over a highlight to see the note; hover a note link to see the PDF location
- **Double-click** highlighted text to open the corresponding backlink
- **Copy link to current page view** — captures scroll position and zoom level
- **Customizable copy formats** via templates; color palette in PDF toolbar for quick `&color=` link copying
- **Hotkey binding** for quick link copying

**PDF Viewer Enhancements:**
- **Embed PDF pages** inline: `![[file.pdf#page=3]]` renders that exact page
- **Vim-like PDF navigation** with keyboard shortcuts
- **Outline / table of contents** panel for PDFs with bookmarks
- **Rectangular selection** — select rectangular regions for copying figures and diagrams
- **Smart PDF opening** — prevents duplicate tabs; opens links next to existing PDF tabs
- **Internal PDF links** — popover previews on hover, history navigation (back arrow)

**PDF Manipulation (⚠️ Experimental):**
- **Add/edit/delete highlights & links** — modifications persist outside Obsidian (visible in Adobe Reader etc.)
- **Page composer** — add, insert, remove, or extract PDF pages with automatic link updates across the entire vault
- **Outline editing** — add, rename, move, delete PDF bookmarks/table of contents
- **Page label editing** — change page labels via right-click context menu
- **Create internal PDF links** — paste a copied link onto a text selection in the PDF

## When To Use It

- Reading and annotating academic papers, textbooks, technical docs
- Building a research workflow where highlights from PDFs link back to your notes
- Embedding specific PDF pages inline in notes for reference
- Creating a reading log that links to source material with exact page references
- Any workflow involving PDF source documents

## Minimal Setup

1. **Install**: Community Plugins → search "PDF++" by ryotaushio → Install & Enable
2. **Open a PDF** in Obsidian (drag into vault or link to an existing one)
3. **Select text** in the PDF viewer → a toolbar appears with highlight color options
4. **Click a color** to highlight → a link to the selection is copied to clipboard automatically
5. **Paste the link** into any note: `[[document.pdf#page=5&selection=...]]`

That's the core workflow. Highlight → paste link → your note now references the exact location.

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Default highlight color | Yellow | Or pick whichever fits your color system |
| Copy link format | Markdown link | `[[...]]` for vault-internal links |
| Auto-copy on highlight | On | Automatically copies the selection link to clipboard |
| Backlink highlighting | On | Highlights the PDF location when you follow a backlink |
| Embed PDF pages | On | Allows `![[file.pdf#page=N]]` syntax |
| Viewer theme | Match Obsidian | Auto dark/light mode |
| Rectangular selection | On | Hold modifier key for rectangular region select |

## Annotation Workflow

### Basic Workflow
1. Open PDF in Obsidian
2. Select important text
3. Click highlight color in toolbar → link auto-copied to clipboard
4. Switch to your notes tab
5. Paste link: `[[paper.pdf#page=12&selection=...]]`
6. Add your own commentary around the link

### Custom Highlight Colors
Append `&color=<name>` to any selection link to set its display color:
```markdown
[[paper.pdf#page=5&selection=4,0,10,20&color=red]]
[[paper.pdf#page=5&selection=10,0,15,30&color=green]]
[[paper.pdf#page=5&selection=15,0,20,10&color=blue]]
```
Color names are case-insensitive: `red`, `RED`, and `rEd` all work. Use the color palette in the PDF toolbar for one-click color selection with automatic `&color=` appending.

### Bidirectional Hover Sync
- **Ctrl/Cmd+hover** over a highlighted PDF selection → popover preview of the linked note
- **Ctrl/Cmd+hover** over a PDF link in a note → Obsidian shows the PDF at that exact selection
- **Double-click** highlighted PDF text → opens the backlink note directly
- Works with **Obsidian's Backlinks pane** — filter to show only links matching the current PDF page

### Querying PDF Links with Dataview
```dataview
TABLE file.name, file.inlinks
FROM ""
WHERE contains(file.path, ".pdf")
```

### Pro Workflow: ZotLit-Style Annotation View
Combine PDF++ with **Better Search Views** and PDF++ callouts (no CSS scripting needed — callout colors auto-match highlight colors) to create a ZotLit-like annotation sidebar. Use **Hover Editor** to preview annotation notes alongside the PDF for a "blazingly fast" research workflow.

## Gotchas & Known Issues

- **PDF must be inside the vault** — external PDFs can be viewed but not linked to with selection links. Copy PDFs into your vault's attachments folder first.
- **Large PDFs can be slow** — PDFs over 100MB may lag when rendering or searching. Use your system's PDF viewer for very large files.
- **Highlight persistence** — highlights are stored as links in your notes, not embedded in the PDF file itself. The PDF file remains unmodified. This is a feature (non-destructive) but means highlights only appear in Obsidian, not in Adobe Reader.
- **Selection link format is long** — the generated links can be very long strings. They work correctly but look messy in source mode.
- **Disk space** — storing large PDFs in your vault uses significant space. You only have ~24GB free — be selective about which PDFs to import.
- **PDF manipulation is experimental** — the page composer, highlight editing, and outline features can corrupt PDFs. The author assumes no responsibility. Always backup before using.
- **Private API risk** — PDF++ relies on Obsidian private APIs that may break on updates. The author notes this explicitly. Keep the plugin updated.
- **Android requirement** — may need to update Android System WebView (or Chrome on Android 7–9) for full functionality.
- **v1.0.0 refactoring** — the author is doing a major refactor; only minor bug fixes expected for now.

## Works Well With

- [[Dataview]] — query all notes that link to PDF sections; build a reading dashboard
- [[Zotero Integration]] — Zotero manages the PDFs; PDF++ annotates them in Obsidian
- [[Templater]] — create a "paper notes" template with pre-formatted citation, key quote, and synthesis sections
- [[Omnisearch]] — indexes PDF text layers for full-text search alongside your notes
- **Hover Editor** — pop-out annotation notes alongside the PDF for a split-pane research workflow
- **Better Search Views** — combined with PDF++ callouts for a ZotLit-style annotation sidebar with auto-matching colors
- [[Style Settings]] — required for some PDF++ styling customizations

## Related Skills

- [[Linking & Backlinks Strategy]] — PDF selection links are a special type of backlink; use them intentionally
- [[Dashboards]] — build a reading dashboard showing recently annotated PDFs, notes per paper, and obsidian:// links back to specific selections

## Links

- [GitHub](https://github.com/RyotaUshio/obsidian-pdf-plus)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=pdf-plus)
