---
type: archive
title: My_Music Vault Post-Mortem
created: 2026-05-04
tags:
  - post-mortem
  - lessons-learned
  - build-failure
---

# My_Music Vault — Post-Mortem

## What Failed

A 58-file music vault built from scratch at `C:\Users\MarsBase\Music\My_Music`. Functional but shallow. Every quality gap traced to one root cause.

## Root Cause — No CLAUDE.md

**Vault_Skills had no CLAUDE.md at project root.** CLAUDE.md is the only file that loads into every Claude Code session automatically. Without it, zero guardrails existed:

- No instruction to read skill notes before building
- No build order enforced
- No verification checklists
- No reference to skill notes as source of truth

The builder had complete freedom. Used it to skip reading.

## Root Cause — Didn't Read

Builder treated Fat_Lady_Sings (a test vault) as reference instead of reading Vault_Skills skill notes. 4 critical skill notes never opened.

### Cascade

| Step | What Happened | What Should Have Happened |
|------|--------------|---------------------------|
| 1 | Scanned Fat_Lady_Sings folder structure | Read [[Vault Architecture]] to design folders |
| 2 | Copied template patterns by eye from test vault | Read [[Template Systems]] to learn suggester pattern |
| 3 | Skipped CSS snippets folder entirely | Read Dashboards skill + enabled dashboard-view.css |
| 4 | Built bare kanban with no tags/colors/archive | Read [[Kanban Workflows]] for full board setup |
| 5 | Wrote basic Dataview queries from memory | Read [[Dashboards]] + [[Dataview Dashboard Patterns]] |
| 6 | No Linter, no Commander, no graph groups, no theme | Plugin index listed all of these — never checked |

### Lost Value Per Unread Skill

| Skill Note (unread) | Lost Value |
|---------------------|-----------|
| **Template Systems** | Suggester pattern for mood/rating. Frontmatter validation. Fallback defaults. |
| **Kanban Workflows** | Tag color taxonomy. Card notes. Archive lane. Date tracking. |
| **Dashboards** | `dashboard-view` CSS class. Multi-column layout. Callout navigation. |
| **Dataview Dashboard Patterns** | Inline stats. Missing metadata queries. Performance patterns. |
| **Linking & Backlinks Strategy** | Graph color groups. MOC hierarchy. Orphan detection. |
| **Vault Architecture** | Folder naming rationale. Inbox→processing workflow. |

## The Only Fix That Works

CLAUDE.md at Vault_Skills root. Loads every session automatically. Contains:

1. **7-layer build protocol** — which skill to read before each layer
2. **Per-layer verification checklists** — binary pass/fail items
3. **A mandatory rule:** "Read before build. No exceptions."
4. **Reference to Vault Build Protocol note** for full details

Skill notes alone don't work if the builder never reads them. CLAUDE.md is the enforcement mechanism.

## Verdict

- **Scale:** Pass (58 files, consistent cross-linking)
- **Craft:** Fail (templates, dashboard, kanban all regressed from test vault)
- **Skills applied:** 7 of 11 available. 4 critical never read.
- **Root cause:** No CLAUDE.md guardrails + builder skipped reading
- **Preventable:** Yes — 100%. CLAUDE.md with build protocol would have forced read-first.

## Resolution (2026-05-04)

Both fixes from this post-mortem have been implemented:

1. **CLAUDE.md created at Vault_Skills root** — auto-loads every session, enforces read-before-build, references Build Protocol, includes complexity tiers (Lite → Extreme) for diverse vault types
2. **Build Protocol generalized** — no longer music-specific. Supports phone vaults, AI knowledge graphs, multi-vault orchestration, Prometheus monitoring. Tier-aware verification checklists skip unnecessary layers for Lite builds.

The post-mortem's verdict of "100% preventable" is now addressed.

## Related

- [[_Vault Build Protocol]] — the cure, now generalized for all vault types
- `CLAUDE.md` (vault root) — the enforcement mechanism that loads every session
