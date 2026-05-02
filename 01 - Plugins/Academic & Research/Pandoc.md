---
type: plugin
name: Pandoc
category: Academic & Research
status: active
complexity: medium
downloads: 482k+
last-verified: 2026-04-30
tags:
  - plugin
  - academic
  - export
  - pandoc
  - word
  - latex
  - pdf
---

# Pandoc

> Plugin by Oliver Balfour — exports Obsidian notes to Word (.docx), PDF, LaTeX, ePub, HTML, and other formats via the Pandoc document converter. Requires Pandoc installed on your system.

## What It Does

The Pandoc plugin adds export commands to Obsidian that convert your Markdown notes to other document formats using the [Pandoc](https://pandoc.org/) universal document converter. Write your content in Obsidian, export to Word when someone needs a .docx, or to PDF for sharing.

Supported output formats (depends on Pandoc version installed):
- **Word (.docx)** — for sharing with people who use Microsoft Word
- **PDF** — via LaTeX (requires a LaTeX distribution) or wkhtmltopdf
- **HTML** — standalone HTML file
- **LaTeX (.tex)** — for academic publishing
- **ePub** — for ebooks
- **ODT** — OpenDocument for LibreOffice
- **RTF** — rich text format
- **PowerPoint (.pptx)** — slide deck export

## When To Use It

- Sharing notes with non-Obsidian users in Word or PDF format
- Academic writing: draft in Markdown, export to LaTeX for journal submission
- Creating a clean PDF from a note without needing a dedicated PDF plugin
- Converting notes to ePub for e-reader publishing
- Building documents that need Word's tracking changes and commenting features

## Prerequisites

**Pandoc must be installed on Windows before the plugin works:**
```powershell
# Install via winget
winget install JohnMacFarlane.Pandoc

# Or download from pandoc.org/installing
# Verify installation:
pandoc --version
```

**For PDF export** (optional):
```powershell
# Option A: MiKTeX (LaTeX, smaller install)
winget install MiKTeX.MiKTeX

# Option B: wkhtmltopdf (HTML-based PDF, no LaTeX needed)
# Download from https://wkhtmltopdf.org/downloads.html
```

## Minimal Setup

1. **Install Pandoc on Windows** (see prerequisites above)
2. **Install the plugin**: Community Plugins → search "Pandoc" by Oliver Balfour → Install & Enable
3. **Set Pandoc path** (if not on PATH): Settings → Pandoc → Pandoc path → `C:\Users\MarsBase\AppData\Local\Pandoc\pandoc.exe` (or wherever Pandoc installed)
4. **Export**: With a note open → Command Palette → "Pandoc: Export as Word document (.docx)"

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Pandoc path | (auto-detected or set manually) | Usually `pandoc` if on PATH; full path if not |
| Export folder | Same folder as note | Exports to the same location as the source note |
| Extra Pandoc arguments | `--standalone` | Produces a complete document with proper headers |
| Export as Word | (via command) | Most common export |
| Reference doc | (optional .docx) | A Word template to apply styles to the exported .docx |
| PDF engine | `xelatex` or `wkhtmltopdf` | xelatex for full LaTeX; wkhtmltopdf if no LaTeX installed |

## Custom Word Styles (Reference Doc)

To apply your organization's Word template styles:
1. Open Word → format headings, body text, etc. to your preferred styles
2. Save the file as `reference.docx`
3. Settings → Pandoc → Extra Pandoc arguments → `--reference-doc=C:/path/to/reference.docx`

Pandoc will apply your template's styles to the exported content.

## Gotchas & Known Issues

- **Pandoc must be in PATH or manually specified** — if the plugin can't find Pandoc, exports fail silently or with a cryptic error. Test `pandoc --version` in PowerShell first.
- **Obsidian-specific syntax doesn't convert** — `[[wikilinks]]`, Dataview blocks, Excalidraw embeds, and callout syntax aren't standard Markdown and won't convert correctly. Pandoc exports the raw syntax as-is.
- **PDF export requires a LaTeX distribution** — LaTeX takes ~2GB to install. If disk space is a concern (you only have ~24GB free), use wkhtmltopdf instead.
- **Images need to be accessible** — embedded images using vault-relative paths may not resolve correctly in some export formats. Use absolute paths or ensure images are in the export folder.
- **Complex tables may lose formatting** — Markdown tables with merged cells or complex alignment sometimes degrade in Word export.
- **Plugin is no longer actively maintained** — check GitHub for the current maintenance status and known issues with recent Obsidian versions.

## Works Well With

- [[Linter]] — clean up notes with Linter before exporting to ensure consistent formatting
- [[Editing Toolbar]] — format the note correctly in Obsidian; Pandoc handles the conversion
- [[Templater]] — create export-ready note templates with proper heading structure

## Related Skills

- [[Template Systems]]

## Links

- [GitHub](https://github.com/OliverBalfour/obsidian-pandoc)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=obsidian-pandoc)
- [Pandoc Official](https://pandoc.org/)
