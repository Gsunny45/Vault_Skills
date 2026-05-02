---
type: reference
tags:
  - reference
  - frontmatter
---

# Frontmatter Fields Reference

## What Is Frontmatter?
YAML block at the top of any note, between `---` markers. Obsidian reads it as structured metadata. Dataview can query it. Templates can inject it.

## Standard Fields Used in This Vault

### For Plugin Notes
```yaml
---
type: plugin
name: Plugin Name
category: AI | Integration | Automation | UI & Navigation | Data & Querying | Project Management | Writing & Editing | Core Enhanced
status: active | testing | documenting | retired
complexity: low | medium | high
downloads: 1000000
last-verified: 2026-04-29
tags:
  - plugin
  - category-tag
---
```

### For Skill Notes
```yaml
---
type: skill
name: Skill Name
category: 
difficulty: beginner | intermediate | advanced
tags:
  - skill
---
```

### For Vault Design Notes
```yaml
---
type: vault-design
name: 
use-case: 
complexity: low | medium | high
tags:
  - vault-design
---
```

### For Reference Notes
```yaml
---
type: reference
tags:
  - reference
---
```

## Dataview Queryable Fields
Any frontmatter field can be queried with Dataview:
```dataview
TABLE status, complexity, downloads
FROM "01 - Plugins"
WHERE type = "plugin"
SORT downloads DESC
```

## Notes
- Dates should use ISO format: YYYY-MM-DD
- Tags in frontmatter and inline (#tag) both work with Dataview
- Obsidian Properties UI (Ctrl+;) gives a visual editor for frontmatter
