# Vault_Skills — Agent Guardrails

> **This file auto-loads every Claude Code session. It is the enforcement layer.**
> Without it, builders skip skill notes, copy from test vaults, and produce shallow output.
> See `07 - Archive/My_Music Post-Mortem.md` for the failure that created this file.

---

## Rule Zero

**Read before build. No exceptions.**

Every vault layer has a skill note. You MUST read the skill note BEFORE building that layer. Do not copy from another vault. Do not build from memory. Do not paraphrase what you think the skill says. Open it, read it, follow it.

---

## What This Repo Is

Vault_Skills is a **domain-agnostic Obsidian vault-building knowledge base**. It contains plugin docs, skill notes, templates, snippets, and vault design blueprints that can bootstrap ANY Obsidian vault — from a lightweight phone music catalog to a multi-vault AI orchestration system with Prometheus monitoring.

**Location:** `C:\Users\MarsBase\Documents\Vault_Skills\`

## Vault Complexity Tiers

Not every vault needs every layer. Match the tier to the use case:

| Tier | Target | Layers Used | Example |
|------|--------|-------------|---------|
| **Lite** | Phone, low-resource, single-purpose | 1-2-4 (architecture + templates + seed data) | Music catalog on mobile, daily journal |
| **Standard** | Desktop, moderate complexity | 1-2-3-4-5-6-7 (full 7-layer) | Music library with dashboards + kanban |
| **Advanced** | Multi-plugin orchestration, AI workflows | Full 7-layer + REST API + Git + AI plugins | Knowledge graph with agent access |
| **Extreme** | Multi-vault federation, monitoring, scraping | Full 7-layer + REST API + external systems | Prometheus exporter, Grafana dashboards, multi-vault sync |

**Lite vaults skip plugins, dashboards, and kanban entirely.** Don't install Dataview on a phone vault that just needs templates and folders.

---

## Mandatory Build Protocol

**Reference:** `02 - Skills/_Vault Build Protocol.md` — the full protocol with per-layer checklists.

### The 7 Layers (read the skill note BEFORE each layer)

| Layer | Skill Note to Read | Output |
|-------|-------------------|--------|
| 1 — Architecture | `Vault Architecture` | Folders, note types, frontmatter schemas |
| 2 — Templates | `Template Systems` | Templater templates per note type |
| 3 — Plugins | `_Plugin Index` + individual plugin notes | Configured plugins with data.json |
| 4 — Content | `Linking & Backlinks Strategy` | Seed data with correct cross-linking |
| 5 — Dashboards | `Dashboards` + `Dataview Dashboard Patterns` | Live query dashboards |
| 6 — Kanban | `Kanban Workflows` | Workflow boards with tags/colors/archive |
| 7 — Polish | `Linking & Backlinks Strategy` (graph section) | Theme, graph groups, final verification |

### Per-Layer Contract

```
For each layer:
  1. READ the skill note (entirely — not a skim)
  2. USE copy-paste-ready examples from the skill note when available
  3. BUILD the layer
  4. VERIFY against the checklist in _Vault Build Protocol
  5. Only then proceed to next layer
```

### Lite Vault Shortcut

For Lite-tier vaults (phone, minimal):
1. Read `Vault Architecture` → build folders + schemas
2. Read `Template Systems` → build templates (skip Templater plugin — use raw YAML)
3. Create seed content
4. Done. No plugins, no dashboards, no kanban.

---

## Vault Design Documents

Every vault build starts with a design doc in `04 - Vault Designs/`. The design doc specifies:
- Purpose & use case (one sentence)
- Complexity tier (Lite / Standard / Advanced / Extreme)
- Folder structure
- Frontmatter schemas per note type
- Required plugins (with skill references)
- Seed data plan
- Build phases
- Test criteria

**Template:** `03 - Templates/Vault Design.md`

If no design doc exists for the vault you're building, **create one first** before touching any files.

---

## Key Paths

| What | Path |
|------|------|
| Skill notes | `02 - Skills/` |
| Skill index | `02 - Skills/_Skill Index.md` |
| Build protocol | `02 - Skills/_Vault Build Protocol.md` |
| Plugin index | `01 - Plugins/_Plugin Index.md` |
| Templates | `03 - Templates/` |
| Vault designs | `04 - Vault Designs/` |
| CSS snippets | `05 - Snippets/CSS/` |
| Dataview snippets | `05 - Snippets/Dataview/` |
| Templater snippets | `05 - Snippets/Templater/` |
| REST API scripts | `05 - Snippets/Scripts/` |
| Reference docs | `06 - Reference/` |
| Archive | `07 - Archive/` |

---

## Hardware Context

All vaults target this machine unless the design doc says otherwise:

- **Device:** DESKTOP-SH8JARJ
- **CPU:** Intel i5-1335U (1.3 GHz base) — CPU-bound, no discrete GPU
- **RAM:** 16 GB (15.6 usable)
- **GPU:** Intel Iris Xe (128 MB) — integrated only
- **Storage:** ~24 GB free of 477 GB SSD — **critically low**
- **OS:** Windows 11 64-bit, touchscreen

**Implications:**
- Local AI (Ollama/LM Studio): max ~8B parameter models, CPU inference only
- Heavy plugins (Excalidraw, Smart Connections): monitor RAM; don't stack 3+ AI plugins
- Storage: every vault build must estimate total size upfront; flag if >1 GB
- Phone/Lite vaults: assume Obsidian Mobile with no community plugins unless specified

---

## REST API Multi-Vault Network

These vaults have REST API on port 27123 (only one open at a time):

| Vault | Purpose |
|-------|---------|
| Local-Network-Hub | Central hub for cross-vault queries |
| Gemini_Vault | Gemini AI integration |
| Command_Vault | Command & automation patterns |
| RAG_Vault | Retrieval-augmented generation |
| Claude_Vault | Claude AI integration |

Scripts in `05 - Snippets/Scripts/` auto-connect to whichever vault is open.

---

## Known Gotchas (Learned the Hard Way)

1. **Homepage plugin data.json cannot be pre-written** — causes `Cannot read properties of undefined`. Must configure via Obsidian UI after first open.
2. **Plugin data.json must include EVERY field** — omitting any field crashes the plugin on load. Use complete schemas from plugin notes.
3. **`Bearer ` prefix required** for REST API v3+ — raw key returns 401.
4. **MOC notes need a different schema than content notes** — using `type: knowledge` on MOCs causes false drift positives. Use `type: moc`.
5. **Don't nest folders deeper than 1 level** for content — `Songs/Rock/2025/` breaks clean Dataview `FROM` clauses.
6. **Community plugin IDs must be exact** — `active-deadline-mode` is not a real plugin and corrupted core-plugins.json.

---

## Failure Checklist (When Output Is Wrong)

Before blaming tools, run this:

1. Did you read the skill note for this layer? → If no, stop and read it.
2. Did you use the copy-paste-ready example? → If no, try it first.
3. Did you copy from another vault instead? → If yes, undo and use the skill note.
4. Did you verify against the layer checklist? → If no, run it now.
5. Is there a design doc for this vault? → If no, create one first.

---

## Session Startup Sequence

When starting any vault-building session:

```
1. Read this file (CLAUDE.md) — you're doing this now
2. Read the vault's design doc in 04 - Vault Designs/
3. If no design doc exists → create one using 03 - Templates/Vault Design.md
4. Read 02 - Skills/_Vault Build Protocol.md
5. Identify the complexity tier → skip layers not needed for that tier
6. Begin Layer 1 — read its skill note FIRST
```
