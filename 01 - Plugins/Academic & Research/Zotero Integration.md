---
type: plugin
name: Zotero Integration
category: Academic & Research
status: active
complexity: medium
downloads: ~200k
last-verified: 2026-04-30
tags:
  - plugin
  - academic
  - zotero
  - citations
  - research
  - bibliography
---

# Zotero Integration

> Plugin by mgmeyers — syncs Zotero reference manager data into Obsidian. Import papers, books, and sources as notes with full citation metadata, annotations, and highlights.

## What It Does

Zotero Integration connects Obsidian to [Zotero](https://www.zotero.org/) (a free, open-source reference manager). When you find a paper in Zotero, you can import it into Obsidian as a structured note containing the citation metadata, abstract, PDF annotations, and your highlights — all in Markdown.

Key features:
- **Import citations** — pull any Zotero item into Obsidian as a formatted note
- **Template-based import** — use Templater or Nunjucks templates to control the note structure
- **Annotation import** — extract PDF highlights and annotations from Zotero into the note
- **Citation formats** — generate formatted citations (APA, MLA, Chicago, etc.) for any source
- **Quick search** — fuzzy search your entire Zotero library from within Obsidian

## When To Use It

- Academic research workflows where you manage sources in Zotero
- Building a literature notes system (Zettelkasten-style) from your reading
- Keeping annotated bibliographies in Obsidian with source metadata
- Extracting your PDF highlights from Zotero into searchable Markdown notes
- Writing papers where you need formatted citations from your Zotero library

## Prerequisites

1. **Zotero must be installed**: [zotero.org/download](https://www.zotero.org/download/)
2. **Better BibTeX for Zotero** plugin installed in Zotero:
   - Zotero → Tools → Add-ons → search "Better BibTeX" → Install
   - This provides the citation key system the plugin uses

## Minimal Setup

1. **Install the plugin**: Community Plugins → search "Zotero Integration" by mgmeyers → Install & Enable
2. **Open Zotero** (must be running for the connection to work)
3. **Configure in Obsidian**: Settings → Zotero Integration:
   - Note import location: `Reference/Papers/` (or your research folder)
   - Template: create a template file (see below)
4. **Import a paper**: Command Palette → "Zotero Integration: Import notes" → search your Zotero library → select a paper

## Basic Import Template

Create a Nunjucks template at `03 - Templates/Zotero Paper.md`:

```markdown
---
title: "{{title}}"
authors: [{% for creator in creators %}{{creator.lastName}}{% if not loop.last %}, {% endif %}{% endfor %}]
year: {{date | truncate(4, true, "")}}
journal: {{publicationTitle}}
citekey: {{citekey}}
doi: {{DOI}}
tags: [literature-note, {{itemType}}]
type: literature-note
---

# {{title}}

**Authors**: {{authors}}
**Year**: {{date}}
**Journal**: {{publicationTitle}}
**DOI**: {{DOI}}

## Abstract

{{abstractNote}}

## Key Points

## My Notes

## Annotations

{% for annotation in annotations %}
> {{annotation.annotatedText}}

*{{annotation.comment}}*

{% endfor %}
```

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Note import location | `Reference/Papers` | Where imported paper notes are saved |
| Import format | Nunjucks template | More flexible than the default format |
| Template file | `03 - Templates/Zotero Paper.md` | Your custom template |
| Image import location | `Reference/Images` | Where imported PDF figures are saved |
| Citation style | (your preferred style) | APA, MLA, Chicago, etc. |
| Citekey format | `authoryear` | e.g., `smith2023` — matches Better BibTeX default |

## Gotchas & Known Issues

- **Zotero must be running** — the plugin connects to Zotero's local API. If Zotero isn't open, imports fail.
- **Better BibTeX is required** — without it, citation keys won't be consistent and the import may not work.
- **Annotation import requires ZotFile or built-in annotations** — Zotero 6+ has built-in PDF annotation; older workflows using ZotFile for PDF management may need adjustments.
- **Template changes don't retroactively update existing notes** — updating your import template only affects newly imported papers. Existing notes keep their old format.
- **Works with Zotero 6+** — Zotero 5 and earlier versions have limited API support.

## Works Well With

- [[PDF++]] — PDF++ for annotating PDFs directly in Obsidian; Zotero Integration for importing annotations from Zotero's managed PDFs
- [[Dataview]] — query all literature notes by author, year, or topic in a reading dashboard
- [[Templater]] — extend the import template with Templater expressions for more dynamic formatting
- [[Obsidian Git]] — version-control your growing literature note library

## Related Skills

- [[Linking & Backlinks Strategy]]
- [[Dashboards]]

## Links

- [GitHub](https://github.com/mgmeyers/obsidian-zotero-integration)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=obsidian-zotero-integration)
- [Zotero](https://www.zotero.org/)
- [Better BibTeX](https://retorque.re/zotero-better-bibtex/)
