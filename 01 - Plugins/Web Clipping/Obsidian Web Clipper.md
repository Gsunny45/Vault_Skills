---
type: plugin
name: Obsidian Web Clipper
category: Web Clipping
status: active
complexity: low
downloads: ~300k
last-verified: 2026-04-30
tags:
  - plugin
  - web-clipping
  - browser-extension
  - capture
  - reading
---

# Obsidian Web Clipper

> Official Obsidian browser extension — clips web pages, articles, and selected text directly into your Obsidian vault as clean Markdown notes. Available for Chrome, Firefox, Safari, and Edge.

## What It Does

Obsidian Web Clipper is a browser extension (not an Obsidian plugin) that captures web content and sends it to your Obsidian vault. Click the extension icon while browsing → pick a template → the page is saved as a Markdown note.

Key features:
- **Full page clip** — converts entire web pages to Markdown (reader mode)
- **Selection clip** — clip only selected text from a page
- **Highlight mode** — highlight text on pages and clip highlights with context
- **Template system** — define templates for different clip types (article, recipe, resource, etc.)
- **Inline filtering** — strip ads, navigation, and clutter via reader mode conversion
- **Metadata extraction** — automatically captures title, author, URL, date, description
- **Vault targeting** — choose which vault and folder to clip into

## When To Use It

- Saving articles for later reading inside Obsidian (instead of Pocket/Instapaper)
- Building a research collection from the web
- Capturing documentation pages, recipes, or references alongside related notes
- Replacing browser bookmarks with actual Markdown notes that are searchable
- Clipping highlighted quotes from articles with source attribution

## Minimal Setup

1. **Install the browser extension**:
   - Chrome: [Chrome Web Store — Obsidian Web Clipper](https://chrome.google.com/webstore/detail/obsidian-web-clipper/)
   - Edge: Available in Chrome Web Store (use Chrome extensions in Edge)
2. **Obsidian must be running** — the extension uses the REST API or a local connection to send content to your vault. Enable Settings → General → "Local REST API" or use the Obsidian URI protocol.
3. **Click the extension icon** on any webpage
4. **Configure the clip**: edit title, choose template, choose destination folder
5. **Click Clip** — the page is saved to your vault

## Configuration in the Extension

Set defaults in the extension popup → Settings:
| Setting | Recommended Value |
|---|---|
| Default vault | `Vault_Skills` (or your active vault) |
| Default folder | `Reference/Web Clips` |
| Default template | Article (built-in) |
| Properties | Title, URL, Author, Date, Tags |
| Clip mode | Reader (cleaner) or Source (full HTML) |

## Template Variables

The extension supports dynamic properties in templates:

| Variable | Value |
|---|---|
| `{{title}}` | Page title |
| `{{url}}` | Page URL |
| `{{author}}` | Author (if available) |
| `{{date}}` | Date clipped |
| `{{published}}` | Article publish date |
| `{{description}}` | Page meta description |
| `{{content}}` | Full page Markdown content |
| `{{highlights}}` | Any text you highlighted on the page |

### Example article template
```markdown
---
title: "{{title}}"
url: {{url}}
author: {{author}}
date-clipped: {{date}}
published: {{published}}
tags: [web-clip]
type: article
---

# {{title}}

Source: [{{title}}]({{url}})

{{highlights}}

---

{{content}}
```

## Gotchas & Known Issues

- **Obsidian must be open** — the extension requires Obsidian to be running to receive clips. If Obsidian is closed, clips may queue or fail depending on configuration.
- **Anti-clipping on some sites** — paywalled sites (NYT, Medium behind paywall, etc.) clip what's visible but not the full article.
- **JavaScript-heavy pages may not convert cleanly** — single-page applications and highly dynamic pages sometimes clip incorrectly. Use the selection clip mode for specific text.
- **Large pages create large files** — a 10,000-word article creates a large Markdown file. Consider whether you need the full content or just the highlights.
- **Not the same as Readwise** — Readwise syncs ongoing highlights from many sources automatically; Web Clipper is manual, one-clip-at-a-time from the browser.

## Works Well With

- [[Readwise Official]] — Readwise for automated sync from Kindle/apps; Web Clipper for one-off web captures
- [[Omnisearch]] — Web Clipper saves articles; Omnisearch indexes and searches their full text
- [[Dataview]] — query all web clips by date, tag, or author: `FROM #web-clip`
- [[Templater]] — Templater can post-process clipped notes with additional frontmatter automation

## Related Skills

- [[AI Workflows in Obsidian]]
- [[Linking & Backlinks Strategy]]

## Links

- [Official Page](https://obsidian.md/clipper)
- [GitHub](https://github.com/obsidianmd/obsidian-clipper)
- [Chrome Extension](https://chrome.google.com/webstore/detail/obsidian-web-clipper/)
