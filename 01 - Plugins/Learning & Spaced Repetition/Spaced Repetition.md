---
type: plugin
name: Spaced Repetition
category: Learning & Spaced Repetition
status: active
complexity: medium
downloads: 482k+
last-verified: 2026-04-30
tags:
  - plugin
  - learning
  - flashcards
  - spaced-repetition
  - sm2
  - memorization
---

# Spaced Repetition

> Plugin by st3v3nmw — adds Anki-style spaced repetition flashcard reviews directly inside Obsidian. Flashcards live in your notes as Markdown; the plugin schedules reviews using the SM-2 algorithm.

## What It Does

Spaced Repetition turns your Obsidian notes into a flashcard review system. You define cards using a simple syntax inside any note, and the plugin tracks review history, schedules future reviews using the SM-2 spaced repetition algorithm, and presents cards in a dedicated review panel.

Card types:
- **Single-line cards** (`Q::A` or `Q?A`) — question on front, answer on back
- **Multi-line cards** — multi-paragraph Q&A separated by `?`
- **Cloze deletion** — `==highlighted text==` becomes a cloze card
- **Deck system** — cards tagged with `#flashcards` (or custom tags) form decks

Cards are stored in your notes as regular Markdown. No separate database — everything lives in your vault.

## When To Use It

- Learning a new topic (programming, language, concepts) using active recall
- Memorizing definitions, formulas, code syntax, or terminology
- Converting your notes into reviewable material (turn summaries into flashcard decks)
- Long-term retention without a separate Anki installation
- Building a PKM system where learning and notes are unified

## Minimal Setup

1. **Install**: Community Plugins → search "Spaced Repetition" by st3v3nmw → Install & Enable
2. **Create flashcards** in any note. Default syntax:
   ```markdown
   #flashcards
   
   What is Dataview? :: A plugin that turns Obsidian into a queryable database using DQL
   
   What does SM-2 stand for? :: SuperMemo 2 — the spaced repetition algorithm
   
   The plugin for git backup in Obsidian is called ==Obsidian Git==
   ```
3. **Start a review**: Ribbon → Spaced Repetition icon, or Command Palette → "Spaced Repetition: Open review panel"
4. Review cards: rate each card as "Hard", "Good", or "Easy" after seeing the answer

## Card Syntax Reference

| Syntax | Card type |
|---|---|
| `Question :: Answer` | Basic front/back card |
| `Question?Answer` | Alternative separator |
| `==text to hide==` | Cloze deletion |
| Multi-line with `?` separator | Multi-line card |

### Multi-line example
```markdown
What are the 4 Dataview query types?
?
1. TABLE
2. LIST
3. TASK
4. CALENDAR
```

### Cloze example
```markdown
Dataview uses ==DQL== (Dataview Query Language) for SQL-like queries.
```
→ Card shows: "Dataview uses _____ (Dataview Query Language) for SQL-like queries."

### Deck organization via tags
```markdown
#flashcards/obsidian     ← sub-deck "obsidian"
#flashcards/programming  ← sub-deck "programming"
```

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Flashcard tags | `#flashcards` | Tags that mark notes as containing flashcard decks |
| Single-line separator | `::` | Separator between question and answer |
| Multi-line separator | `?` | Line that separates front and back of multi-line cards |
| Single-line reversed | `:::` | Creates a reversed card (both Q→A and A→Q) |
| Card display order | Random | Prevents order memorization |
| Review timeout | `10 seconds` | Time before auto-moving to next card |
| Show context | On | Shows the note title and surrounding text during review |
| Next day cutoff | `04:00` | Hour at which "today" rolls over to next day |

## Gotchas & Known Issues

- **Cards are in-note, not in a database** — review state (ease factor, next review date) is stored in HTML comments in your notes: `<!--SR:!2026-05-10,3,250-->`. This is invisible in preview but visible in source mode.
- **Editing card text after creation resets review state** — changing the wording of a card treats it as a new card.
- **No sync with Anki** — this is not an Anki bridge. Cards are Obsidian-only; no import/export to Anki.
- **Large decks slow the review panel** — if a tag has 500+ cards due, the review panel can lag on first load. Break large decks into sub-decks with nested tags.
- **Multi-line cards need exact syntax** — the `?` separator must be on its own line, with a blank line before and after the separator in some edge cases.
- **Cloze vs highlights** — `==text==` is Obsidian's highlight syntax AND Spaced Repetition's cloze syntax. This can cause visual clutter if you use highlights throughout a note and then add `#flashcards` to it.

## Works Well With

- [[Dataview]] — query notes by due date: `WHERE contains(file.frontmatter, "SR")` to find all notes with spaced repetition cards
- [[Periodic Notes]] — add a spaced repetition review session to your daily note template
- [[Templater]] — create "study note" templates with pre-formatted card sections

## Related Skills

- [[Template Systems]]

## Links

- [GitHub](https://github.com/st3v3nmw/obsidian-spaced-repetition)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=obsidian-spaced-repetition)
- [Documentation](https://www.stephenmwangi.com/obsidian-spaced-repetition/)
