---
type: reference
tags:
  - reference
  - markdown
---

# Markdown Cheatsheet

## Headings
```
# H1
## H2
### H3
#### H4
```

## Text Formatting
```
**bold**
*italic*
~~strikethrough~~
==highlight==
`inline code`
```

## Lists
```
- Unordered item
- Another item
  - Nested item

1. Ordered item
2. Second item
```

## Tasks
```
- [ ] Incomplete
- [x] Complete
- [/] In progress (Tasks plugin)
- [-] Cancelled (Tasks plugin)
```

## Links & Embeds
```
[[Note Name]]                    internal link
[[Note Name|Alias]]              with alias
[[Note Name#Heading]]            to heading
[[Note Name#^block-id]]          to block
![[Note Name]]                   embed note
![[image.png]]                   embed image
[External](https://example.com)  external link
```

## Tags
```
#tag
#tag/subtag
#tag/subtag/deep
```

## Frontmatter
```yaml
---
type: note
status: active
tags:
  - example
date: 2026-04-29
---
```

## Callouts
```
> [!note] Title
> Content

> [!warning] Watch Out
> Content

> [!tip] Pro Tip
> Content

> [!info]
> [!success]
> [!question]
> [!danger]
> [!bug]
> [!example]
> [!quote]
```

## Tables
```
| Col 1 | Col 2 | Col 3 |
|---|---|---|
| A | B | C |
```

## Code Blocks
\```language
code here
\```

## Horizontal Rule
```
---
```

## Footnotes
```
Text with footnote.[^1]
[^1]: Footnote content.
```
