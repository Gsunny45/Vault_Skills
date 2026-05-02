---
type: plugin
name: Linter
category: Writing & Editing
status: active
complexity: low
downloads: 1M+
last-verified: 2026-04-30
tags:
  - plugin
  - writing
  - formatting
  - linting
  - yaml
  - markdown
---

# Linter

> Plugin by platers — automatically formats and cleans Markdown files on save. Fixes YAML frontmatter, normalizes heading levels, enforces consistent spacing, sorts tags, and over 50 other configurable rules.

## What It Does

Linter is an auto-formatter for Obsidian notes. When triggered (on save, on command, or via hotkey), it applies a configurable set of formatting rules to the current note. Think of it as Prettier/ESLint but for Markdown.

50+ configurable rules across categories:
- **YAML/Frontmatter** — sort keys, fix type errors, add missing fields, normalize date formats
- **Headings** — enforce heading levels, capitalize headings, add/remove file name as H1
- **Whitespace** — remove trailing spaces, normalize line endings, consistent blank lines
- **Content** — fix blockquote syntax, normalize list markers, format code blocks
- **Footnotes** — sort and re-number footnotes
- **Markdown** — fix emphasis markers (consistent `**` vs `__`), normalize link syntax
- **Paste** — auto-format text pasted from external sources

## When To Use It

- Maintaining consistent frontmatter across all notes in a vault (especially after Importer bulk imports)
- Enforcing formatting standards (especially for team/shared vaults)
- Auto-fixing YAML that Dataview can't parse due to syntax errors
- Cleaning up notes pasted from the web or other apps
- Ensuring all notes have required frontmatter fields (type, date, tags)

## Minimal Setup

1. **Install**: Community Plugins → search "Linter" by platers → Install & Enable
2. **Configure rules**: Settings → Linter → browse rules by category, toggle what you want
3. **Test on one note first**: Command Palette → "Linter: Lint the current file"
4. **Enable on save** (optional): Settings → Linter → Lint on save → On

**Start conservatively** — enable Lint on save only after you've verified the rules behave correctly on your notes. Some rules can destructively change content if misconfigured.

## Key Rules to Enable

| Rule | Category | Recommended Setting | Notes |
|---|---|---|---|
| Trailing spaces | Whitespace | On | Removes trailing whitespace from all lines |
| Remove multiple blank lines | Whitespace | On, max 1 | Prevents double-blank-line gaps |
| YAML title alias | YAML | On | Adds `alias:` from H1 title |
| YAML timestamp | YAML | `date-modified` | Updates a `modified:` frontmatter field on save |
| Sort YAML arrays | YAML | On | Alphabetically sorts tag arrays |
| Capitalize headings | Heading | Off (personal pref) | Capitalizes all heading words — turn off if you use sentence case |
| Header increment | Heading | On | Flags jumps from H1 → H3 (skipping H2) |
| Remove empty lines around code fences | Whitespace | On | Cleans up extra blank lines before/after ``` |
| Consecutive blank lines | Whitespace | On, max 1 | |
| Emphasis style | Content | `**` for bold | Normalizes bold to `**` not `__` |

## Rules to Avoid (potentially destructive)
- **Remove trailing punctuation in headings** — off unless your vault style has no punctuation in headings
- **File name heading** — adds the file name as H1; can conflict with existing H1s
- **Move tags to YAML** — moves inline `#tags` to frontmatter; irreversible if you rely on inline tags for display

## Custom Rules with Regular Expressions

Settings → Linter → Custom Regex Rules → Add:
```
Find:    (\s{2,})$
Replace: 
Flags:   gm
Description: Remove multiple trailing spaces
```

## Gotchas & Known Issues

- **"Lint on save" can be slow on large notes** — complex regex rules on a 500-line note add 100-500ms per save. Disable rules you don't need to keep it fast.
- **YAML timestamp rule creates a field on first lint** — if your notes don't have a `modified:` field, Linter adds it on first lint. Expected behavior, but can create surprising diffs in git.
- **Rule order matters** — rules run in the order they appear in the config. If a rule generates content that another rule then modifies, results may be unexpected.
- **Sort YAML arrays changes tag order** — if you manually order tags for semantic reasons, sorting will reorder them alphabetically.
- **Custom regex rules can break content** — test regex rules on a copy of a note before enabling globally.
- **Linter and Templater can conflict on new file creation** — if both are configured to run on new file creation, they may trigger in an unexpected order. Set Templater to run first.

## Works Well With

- [[Dataview]] — Linter fixes frontmatter that Dataview can't parse; run Linter after Importer imports
- [[Importer]] — always run Linter after a bulk import to normalize frontmatter
- [[Templater]] — Templater creates notes with correct frontmatter structure; Linter maintains it going forward
- [[Obsidian Git]] — use git diff to verify Linter changes before committing

## Related Skills

- [[Vault Architecture]]
- [[Template Systems]]

## Links

- [GitHub](https://github.com/platers/obsidian-linter)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=obsidian-linter)
- [Rules Documentation](https://platers.github.io/obsidian-linter/)
