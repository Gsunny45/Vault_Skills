---
type: plugin
name: Natural Language Dates
category: Core Enhanced
status: active
complexity: low
downloads: 1M+
last-verified: 2026-04-30
tags:
  - plugin
  - core-enhanced
  - dates
  - natural-language
  - tasks
---

# Natural Language Dates

> Plugin by argenos — parses natural language date strings and converts them to formatted dates. Type "next Monday" or "in 3 weeks" and get `2026-05-11` inserted automatically.

## What It Does

Natural Language Dates (NLD) lets you type dates the way you think them. Instead of looking up tomorrow's date and typing it manually, you type `@tomorrow` or `@next friday` and the plugin inserts the correct formatted date.

Two usage modes:
- **Trigger character** (`@` by default) — type `@` anywhere in a note to open a date suggestions popup
- **Command palette** — "Natural Language Dates: Insert date" with a prompt

Powered by the `chrono-node` parsing library, which handles a wide range of English date expressions.

## When To Use It

- Adding due dates to Tasks plugin tasks without knowing the exact date
- Inserting dates in journal entries, meeting notes, or project notes naturally
- Any note that requires a date and you don't want to switch to a calendar or lookup
- Pairs with Tasks: type `📅 @next monday` → date resolves to `📅 2026-05-04`

## Minimal Setup

1. **Install**: Community Plugins → search "Natural Language Dates" by argenos → Install & Enable
2. **Type `@` anywhere in a note** — a suggestion popup appears
3. Start typing a date expression: `@tomorrow`, `@next week`, `@in 3 days`
4. Press Enter or click the suggestion to insert the formatted date

That's the full setup. No configuration needed to start using it.

## Date Expression Reference

| Expression | Inserts |
|---|---|
| `@today` | `2026-04-30` |
| `@tomorrow` | `2026-05-01` |
| `@yesterday` | `2026-04-29` |
| `@next monday` | `2026-05-04` |
| `@last friday` | `2026-04-24` |
| `@next week` | `2026-05-04` (start of next week) |
| `@in 3 days` | `2026-05-03` |
| `@in 2 weeks` | `2026-05-14` |
| `@end of month` | `2026-04-30` |
| `@may 15` | `2026-05-15` |
| `@2026-06-01` | `2026-06-01` (passthrough) |

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Date format | `YYYY-MM-DD` | Standard ISO format; matches Tasks, Dataview, Periodic Notes |
| Time format | `HH:mm` | 24-hour format |
| Trigger phrase | `@` | Character that opens the date picker popup |
| Insert date and time | Off (toggle per use) | Use the command "Insert date and time" when you need both |
| Locale | `en-US` | Affects day-of-week interpretation ("next Monday") |

## Gotchas & Known Issues

- **English only** — chrono-node parses English expressions. Non-English date phrases won't resolve.
- **"Next week" ambiguity** — "next week" returns the Monday of next week (or Sunday in US locale). If you want a specific day, say "next monday" explicitly.
- **End-of-month edge cases** — "end of month" on the last day of the month returns today, not next month's end. Use "end of next month" if needed.
- **No time zone handling** — dates are inserted without time zone info. All dates are treated as local.
- **Popup may not appear in all editors** — the `@` trigger works in Source and Live Preview modes. It may not work inside certain plugin panels (Kanban cards, etc.).

## Works Well With

- [[Tasks]] — NLD inserts due dates in the format Tasks expects (`📅 YYYY-MM-DD`); the combination makes task capture much faster
- [[QuickAdd]] — use NLD inside QuickAdd capture formats; type `@tomorrow` and it resolves before the capture inserts
- [[Periodic Notes]] — quickly jump to a date's daily note by typing the date expression in the date field
- [[Templater]] — complement: Templater handles programmatic date logic; NLD handles interactive date entry

## Related Skills

- [[Template Systems]]
- [[Kanban Workflows]]

## Links

- [GitHub](https://github.com/argenos/nldates-obsidian)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=nldates-obsidian)
