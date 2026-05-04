---
type: vault-design
name: "Prompt & Context Engineering (Rebuild)"
use-case: "Engineering knowledge graph for prompt-to-production pipeline"
complexity: extreme
tags:
  - vault-design
  - test2
  - rebuild-target
source_vault: "C:\\Users\\MarsBase\\Desktop\\Prompt & Context Engineering"
---

# Vault Design — Prompt & Context Engineering (Rebuild)

## Purpose & Use Case

A structured, machine-readable knowledge graph for five engineering domains:
Prompt Engineering, Context Engineering, DevOps, GitHub, and Build systems.
Designed for AI agents (Claude, Gemini, Copilot) to read, write, and navigate
as the primary knowledge backend. Graph View is the primary navigation interface.
Connected to Local-Network-Hub via REST API (port 27124).

## What's Good (KEEP)

- 78 atomic KNW notes (KNW-0008→KNW-0078) with dense cross-linking
- 6 MOC hub notes (one per domain + root)
- 5 session logs with agent attribution
- 9 tasks in structured TSK format
- Dashboard.md with 7 Dataview query sections + DataviewJS stats
- Template system (_templates/) with knowledge, task, decision, session, daily, weekly templates
- Decision ledger pattern (DEC-NNNN with rationale/alternatives)
- Drift detection system (_system/_drift_report.md)
- Token-aware briefing compiler (_system/_briefing.md)
- Prometheus exporter + Grafana monitoring
- Meta-bind button dashboard for one-click operations

## What's Broken (FIX)

### Critical
- Duplicate IDs: TSK-0001 and TSK-0002 both claim `id: TSK-0010`
- Duplicate IDs: _archive/KNW-0006 and "13 keyboard shortcuts.md" both claim `id: KNW-0006`
- TSK-0001.md and TSK-0002.md missing required fields (`title`, `domain`)

### High
- All 6 MOC notes missing required frontmatter fields (`subject`, `confidence`, `last_verified`)
- MOC notes should follow a different schema than KNW notes — they're hub/spoke aggregators, not atomic knowledge

### Medium (794 items)
- _archive/claude_vault_carryover/ contains stale cross-references to modified targets
- These are noise — should be silenced or excluded from drift scans

### Low
- Two Untitled.md/Untitled 1.md notes in root — uncategorized, likely inbox overflow

## Folder Structure

```
Prompt & Context Engineering/
├── CLAUDE.md              ← agent-warm-start briefing (read-first)
├── Dashboard.md           ← live Dataview dashboard w/ Meta-bind buttons
├── Task_Board.md          ← Kanban pipeline
├── Vault_Health.md        ← schema compliance & link health
├── README.md              ← human overview
├── _system/               ← schemas, briefings, drift reports, monitoring
│   ├── _briefing.md       ← token-budgeted warm-start
│   ├── _drift_report.md   ← stale refs & schema violations
│   └── _schemas.yaml      ← frontmatter type schemas
├── _templates/            ← Templater auto-templates per folder
│   ├── knowledge.md
│   ├── task.md
│   ├── decision.md
│   ├── session.md
│   ├── daily.md
│   ├── weekly.md
│   └── startup.md
├── _scripts/              ← User script functions
├── _archive/              ← Retired content (excluded from Graph View)
├── decisions/             ← DEC-NNNN — why choices were made
├── sessions/              ← SES-YYYY-MM-DD-NNN — session logs
├── knowledge/             ← KNW-NNNN + MOC-*.md hub notes
├── tasks/                 ← TSK-NNNN — cross-session work
└── inbox/                 ← Quick timestamped captures
```

## Frontmatter Schemas

### Knowledge Note (KNW-NNNN)
```yaml
type: knowledge
id: KNW-NNNN
subject: "topic title"
domain: "prompt-engineering | context-engineering | devops | github | build | cross-domain"
confidence: "verified | inferred | stale"
last_verified: YYYY-MM-DD
source: "citation string"
related: [KNW-XXXX, KNW-YYYY]
tags: [domain, topic, subtopic]
tokens: <estimate>
```

### MOC Hub Note (special — NOT same schema as KNW)
```yaml
type: moc
domain: "prompt-engineering | context-engineering | devops | github | build"
status: "populating | complete"
spokes_populated: <count>
spokes_total: <count>
tags: [moc, <domain>]
```
**Note:** MOC notes are NOT `type: knowledge`. They use `type: moc` with a
different schema to avoid drift report false positives.

### Decision Note (DEC-NNNN)
```yaml
type: decision
id: DEC-NNNN
title: "decision title"
date: YYYY-MM-DD
status: "proposed | accepted | superseded"
context: "why this decision matters"
alternatives: ["option A", "option B"]
rationale: "why this choice"
supersedes: DEC-NNNN  (optional)
tags: [decision, <domain>]
```

### Task Note (TSK-NNNN)
```yaml
type: task
id: TSK-NNNN
title: "task description"
status: "open | in_progress | blocked | done"
created: YYYY-MM-DD
domain: "prompt-engineering | context-engineering | devops | github | build | cross-domain"
priority: "normal | high | critical"
assigned_session: SES-YYYY-MM-DD-NNN  (optional)
tags: [task, <domain>]
```

### Session Note (SES-YYYY-MM-DD-NNN)
```yaml
type: session
id: SES-YYYY-MM-DD-NNN
date: YYYY-MM-DD
agent: "claude-opus | claude-sonnet | gemini | copilot | human"
status: "active | closed | interrupted"
domain: "<primary domain>"
files_read: [path, path]
files_written: [path, path]
decisions_made: ["decision summary"]
tokens_used: <estimate>
summary: "one-line summary"
tags: [session, <domain>]
```

## Required Plugins

| Plugin | Role | Required |
|--------|------|----------|
| **Dataview** | Live query engine (Dashboard, vault stats, drift detection) | YES |
| **Templater** | Auto-template on note creation (per-folder templates) | YES |
| **QuickAdd** | Quick capture, new-task macro, new-decision macro | YES |
| **Commander** | Custom button macros on Dashboard | YES |
| **Kanban** | Task_Board.md visual pipeline | YES |
| **Linter** | Schema enforcement on save | YES |
| **Obsidian Git** | Version control & backup | YES |
| **Local REST API** | External agent access bridge (port 27124) | YES |
| **Calendar** | Date-based navigation | Optional |
| **Periodic Notes** | Daily/weekly notes | Optional |
| **Tasks** | Task management (supplements Kanban) | Optional |
| **Excalidraw** | Visual diagrams | Optional |
| **Smart Connections** | Semantic note discovery | Optional |
| **ChatGPT MD** | In-note AI chat | Optional |

## Plugin Config Patterns

All programmatic configurations MUST use the complete data.json schemas
documented in the individual plugin notes:

- **Templater**: 17 required fields → [[Templater#Programmatic Configuration (data.json)]]
- **Dataview**: 16 required fields → [[Dataview#Programmatic Configuration (data.json)]]
- **QuickAdd**: All migration keys + ai object → [[QuickAdd#Programmatic Configuration (data.json)]]

## Rebuild Tasks

### Phase 1 — Schema Fixes (no content loss)
1. Fix duplicate IDs: renumber TSK-0001, TSK-0002, and _archive KNW-0006
2. Add missing `title` and `domain` to TSK-0001.md and TSK-0002.md
3. Convert MOC notes from `type: knowledge` to `type: moc` with proper schema
4. Add `subject`, `confidence`, `last_verified` to MOC notes (or drop those fields for MOC schema)

### Phase 2 — Cleanup
5. Exclude _archive/ from drift scans (add path filter in _system/_schemas.yaml)
6. Move Untitled.md and Untitled 1.md to inbox/ with proper names
7. Verify all 78 KNW notes pass drift scan without non-_archive issues

### Phase 3 — Plugin Health
8. Verify all 18 plugins load without errors
9. Rebuild Dashboard meta-bind buttons if any reference missing commands
10. Test QuickAdd choices: qa-new-task, qa-inbox
11. Verify Templater folder templates trigger on new note creation

### Phase 4 — Git
12. Push vault to GitHub remote (TSK-0009)
13. Configure Obsidian Git auto-commit

## Notes & Gotchas

- **MOC notes use a DIFFERENT schema than KNW notes** — they are hubs, not atoms. Using `type: knowledge` on MOC notes causes false drift positives.
- **_archive/ must be excluded from drift scans** — stale references in archived notes are expected and not actionable.
- **Homepage plugin data.json cannot be pre-written** — causes `Cannot read properties of undefined` on load. Must configure via Obsidian UI.
- **Decision Ledger** and **Drift Detector** appear to be custom or community plugins — verify they still work with current Obsidian version.

## Related Vault Designs

- [[Fat_Lady_Sings]] — simpler test vault, same plugin stack (Templater + Dataview + QuickAdd + Kanban)
