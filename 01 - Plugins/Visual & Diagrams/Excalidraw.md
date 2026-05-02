---
type: plugin
name: Excalidraw
category: Visual & Diagrams
status: active
complexity: medium
downloads: 5.9M+
last-verified: 2026-04-30
tags:
  - plugin
  - visual
  - diagrams
  - drawing
  - sketching
  - whiteboard
---

# Excalidraw

> Plugin by zsolt.viczian — embeds the Excalidraw whiteboard tool natively inside Obsidian. The most downloaded Obsidian plugin. Create hand-drawn-style diagrams, sketches, mind maps, and illustrations stored as vault files with full backlink support.

## What It Does

Excalidraw is a virtual whiteboard with a distinctive hand-drawn aesthetic. Inside Obsidian, it stores drawings as `.md` files containing JSON — meaning they appear in the graph view, support backlinks, and can be embedded in other notes with `![[drawing.excalidraw]]`.

Key capabilities:
- **Freehand drawing** with pressure-sensitive strokes (touchscreen support)
- **Shapes**: rectangle, ellipse, diamond, arrow, line, text, image, frame
- **Obsidian integration**: embed `[[wiki links]]` inside Excalidraw elements; click them to open notes
- **Excalidraw Script Engine**: run JavaScript scripts to automate drawing operations
- **LaTeX support**: render math equations as SVG inside drawings
- **Mermaid import**: convert Mermaid diagrams into editable Excalidraw shapes
- **OCR**: extract text from images embedded in drawings
- **Publish-ready exports**: PNG, SVG, or dark/light mode variants

## When To Use It

- Visual brainstorming and mind mapping that needs to feel "sketchy" and informal
- System architecture diagrams, flowcharts, and concept maps
- Annotating screenshots or images with arrows and labels
- Visual note-taking alongside written notes (embed diagram in a note)
- Touchscreen drawing on your device (10-point touch is fully supported)
- Any diagram where Advanced Canvas feels too rigid and you want freeform spatial thinking
- Personal kanban, roadmap timelines, or visual project plans you prefer to draw

**vs. Advanced Canvas**: Excalidraw = freehand, visual, sketchy, artistic; Advanced Canvas = structured, node-based, flowchart shapes with connectors. They're complementary.

## Minimal Setup

1. **Install**: Community Plugins → search "Excalidraw" by zsolt.viczian → Install & Enable
2. **Create a drawing**: Command Palette → "Excalidraw: Create new drawing" — opens a new `.excalidraw.md` file
3. **Draw**: use the toolbar at the top (selection, rectangle, diamond, ellipse, arrow, line, text, image, eraser, hand)
4. **Switch between drawing and markdown**: Click the pencil icon or use Command Palette → "Excalidraw: Toggle to markdown view"
5. **Embed in a note**: `![[MyDrawing.excalidraw]]` — renders inline in reading view

### Touch drawing setup
On your touchscreen device:
- Settings → Excalidraw → Compatibility → Pen and touch → Enable touch drawing
- Two-finger scroll/zoom works out of the box

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Default folder | `Drawings` or `05 - Snippets/Drawings` | Where new `.excalidraw.md` files are saved |
| Filename prefix | `Drawing ` | Files named `Drawing YYYY-MM-DD HH.mm.ss.excalidraw.md` |
| Embed drawing as PNG in markdown | Off | Leave off — embeds the live drawing, not a snapshot |
| Theme | Match theme (auto) | Auto-switches between dark/light based on Obsidian theme |
| Zoom to fit on open | On | Fits the drawing to the panel on open |
| Left-hand mode | Off | Mirror the toolbar if you prefer left-hand drawing |
| Compress JSON | On | Reduces file size; keep on for large drawings |
| Compatibility mode | Off | Only turn On if sharing `.excalidraw` files with standalone Excalidraw |
| Link prefix | `[[` (default) | How Obsidian links are recognized inside drawings |
| Auto-export SVG | Off | Turn On if you need a static SVG alongside the drawing for use outside Obsidian |
| Auto-export PNG | Off | Same as above but PNG |

## Core Workflow Patterns

### Embed a drawing in a note
```markdown
# Project Overview

![[Project Architecture.excalidraw]]

The diagram above shows the three main components...
```
In reading mode, the drawing renders inline. Click to open and edit.

### Link a note from inside a drawing
1. Select a shape in Excalidraw
2. Click the link icon (or press `Ctrl+K`)
3. Type a note name — it becomes an `[[wikilink]]` attached to that shape
4. In Obsidian, clicking the shape opens the linked note

### Embed a note inside a drawing
1. In Excalidraw, click the document icon in the toolbar → "Embed a file"
2. Select any vault file — it renders as an embedded note card inside the drawing
3. Note cards update live when the source note changes

### Export for sharing
- Command Palette → "Excalidraw: Export PNG" or "Export SVG"
- PNG: best for sharing/pasting in docs; SVG: best for scalable exports
- Both respect dark/light mode setting

## Gotchas & Known Issues

- **`.excalidraw.md` files are large** — complex drawings with many elements can reach 500KB-2MB. Monitor your vault's disk usage (you only have ~24GB free).
- **JSON inside markdown** — the file is a markdown wrapper around JSON. Don't manually edit the JSON block or you'll corrupt the drawing.
- **Rendering lag on complex drawings** — drawings with 200+ elements may lag on your CPU-only setup (no GPU acceleration for canvas rendering). Split large drawings into smaller files.
- **Touch vs mouse mode** — touch drawing and mouse selection can conflict. Toggle with the toolbar hand icon: hand tool = scroll/pan; other tools = draw.
- **Backlinks show the drawing file** — when you link a note from inside Excalidraw, the backlink on the target note points to the drawing file, not to a specific element. This is expected behavior.
- **Compatibility mode changes file format** — enabling compatibility mode saves as `.excalidraw` (no markdown wrapper). Don't switch between modes on the same file.
- **Auto-export doubles disk usage** — PNG/SVG auto-export saves a separate file alongside every drawing. Only enable if you need static exports.
- **Plugin updates can break existing drawings** — always backup before major plugin updates. Obsidian Git is highly recommended.

## Works Well With

- [[Advanced Canvas]] — use both: Excalidraw for freeform sketching, Advanced Canvas for structured flowcharts
- [[Obsidian Git]] — back up drawings before major changes; Excalidraw files are valuable and not recoverable if corrupted
- [[Dataview]] — query drawing files by tag or date in a Dataview TABLE
- [[Templater]] — create Excalidraw templates with pre-drawn structures or starter shapes
- [[Homepage]] — embed a vault map or overview drawing on your dashboard

## Related Skills

- [[Canvas Visual Mapping]]
- [[Vault Architecture]]

## Links

- [GitHub](https://github.com/zsviczian/obsidian-excalidraw-plugin)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=obsidian-excalidraw-plugin)
- [Excalidraw Script Library](https://github.com/zsviczian/obsidian-excalidraw-plugin/discussions/categories/script-library)
