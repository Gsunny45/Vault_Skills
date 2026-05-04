---
type: skill
name: Vault Build Protocol
category: Structure
difficulty: beginner
tags:
  - skill
  - build
  - protocol
  - mandatory
---

# Vault Build Protocol

> **MANDATORY — Read before starting any vault build.**
> This protocol exists because the My_Music build failed by skipping skill notes and copying from a test vault instead. Every gap traced back to "didn't read the skill note first."
> See: `07 - Archive/My_Music Post-Mortem.md`

## How This Works

Building a vault is layered. Each layer maps to one or more skill notes. **You cannot build a layer without reading its skill note first.**

```
For each layer:
  1. READ the skill note (entirely — not a skim)
  2. USE copy-paste-ready examples when available
  3. BUILD the layer
  4. VERIFY the layer (checklist below)
  5. Only then move to next layer
```

If a layer has a "Copy-Paste Ready" example in the skill note, use it — don't recreate from memory or copy from another vault.

## Complexity Tiers

Not every vault needs all 7 layers. Check the vault's design doc for its tier:

| Tier | Layers | Skip |
|------|--------|------|
| **Lite** (phone, single-purpose) | 1 → 2 → 4 | Plugins, dashboards, kanban, polish |
| **Standard** (desktop, moderate) | 1 → 2 → 3 → 4 → 5 → 6 → 7 | Nothing |
| **Advanced** (AI, orchestration) | All + REST API + Git + AI plugins | Nothing |
| **Extreme** (multi-vault, monitoring) | All + external systems (Prometheus, Grafana, federation) | Nothing |

**Lite vaults:** Skip Layers 3, 5, 6, 7 entirely. No plugins, no Dataview, no kanban. Just folders + templates + content.

---

## Build Order

### Layer 1 — Vault Architecture
**Read:** [[Vault Architecture]]
**Output:** Folder structure, note type definitions, frontmatter schemas

**Verify:**
- [ ] Folders match note types (one folder per type, max 1 level deep)
- [ ] Frontmatter schemas defined for every note type (type, title, links, metadata)
- [ ] Inbox folder exists (e.g., `00 - Inbox/` or `inbox/`)
- [ ] Support folders exist (Templates/, Dashboard/ or equivalent)
- [ ] Naming convention documented (how files are named per type)
- [ ] Total vault size estimated (flag if >1 GB given 24 GB free disk)

### Layer 2 — Template Systems
**Read:** [[Template Systems]]
**Output:** Templates for each note type

**Verify:**
- [ ] Templates use `tp.system.suggester()` for controlled vocabulary — NOT `tp.system.prompt()`
- [ ] Templates use `tp.file.title` for title (derived from filename)
- [ ] Templates include ALL frontmatter fields from Layer 1 schemas
- [ ] Templater plugin configured: trigger on file creation ON, folder templates mapped
- [ ] QuickAdd capture template configured for rapid inbox capture
- [ ] **Lite tier exception:** If no Templater plugin, templates are raw YAML frontmatter blocks — still must match schemas

### Layer 3 — Plugins
**Read:** [[_Plugin Index]] for plugin list, then individual plugin notes for each plugin used
**Output:** Configured plugins with data.json

**Verify:**
- [ ] Plugin binaries installed (main.js + manifest.json + styles.css)
- [ ] data.json includes ALL fields (omitting fields causes crashes)
- [ ] Each plugin enabled in community-plugins.json
- [ ] Homepage configured via Obsidian UI (data.json cannot be pre-written)
- [ ] Linter installed and configured for frontmatter auto-format
- [ ] Commander installed if custom toolbar buttons needed
- [ ] **Advanced/Extreme tier:** REST API plugin installed + key configured
- [ ] **Advanced/Extreme tier:** Obsidian Git installed + remote configured
- [ ] **Extreme tier:** External system integration documented (Prometheus endpoints, Grafana datasources, multi-vault API bridge)

### Layer 4 — Data / Content
**Read:** [[Linking & Backlinks Strategy]]
**Output:** Seed data with correct cross-linking

**Verify:**
- [ ] All frontmatter links resolve (no broken `[[wikilinks]]`)
- [ ] Link direction follows convention (child → parent, not both ways unless intentional)
- [ ] File naming matches linking convention
- [ ] All notes of same type have identical frontmatter fields
- [ ] Orphan check: `LIST WHERE length(file.inlinks) = 0`
- [ ] **Advanced tier:** MOC hub notes use `type: moc`, not same schema as content notes
- [ ] **Extreme tier:** Cross-vault references documented (which vault links where)

### Layer 5 — Dashboards
**Read:** [[Dashboards]] AND [[Dataview Dashboard Patterns]]
**Output:** Live query dashboard(s)

**Verify:**
- [ ] Dashboard has `cssclass: dashboard-view` in frontmatter
- [ ] CSS snippet enabled (from `05 - Snippets/CSS/`)
- [ ] Queries scoped to specific folders (not `FROM ""` on large vaults)
- [ ] Quick stats section (DataviewJS for inline counts)
- [ ] Missing metadata section (find incomplete notes)
- [ ] Recently modified section
- [ ] Navigation section with jump links
- [ ] Homepage set to dashboard
- [ ] **Advanced/Extreme tier:** Vault health section (drift detection, schema violations)

### Layer 6 — Kanban & Workflows
**Read:** [[Kanban Workflows]]
**Output:** Kanban board(s) with full workflow

**Verify:**
- [ ] Tag colors configured per board context
- [ ] Cards have dates (`@{date}`)
- [ ] Cards have descriptions or linked notes
- [ ] Archive lane exists below `***` separator
- [ ] Card hygiene: bold title, date, tag, optional link
- [ ] **Extreme tier:** Task pipeline connects to external systems if applicable

### Layer 7 — Polish
**Read:** [[Linking & Backlinks Strategy]] (graph section)
**Output:** Theme, graph groups, final verification

**Verify:**
- [ ] Community theme selected (not empty `cssTheme`)
- [ ] Graph view color groups by note type
- [ ] All Dataview queries return expected results
- [ ] All cross-links resolve
- [ ] QuickAdd hotkey works
- [ ] **Advanced tier:** REST API responds to health check (`GET /`)
- [ ] **Extreme tier:** Prometheus metrics endpoint returns valid data
- [ ] **Extreme tier:** Multi-vault queries work across REST API bridge

---

## Domain-Specific Considerations

The layers above are domain-agnostic. Here are notes for specific vault types:

### Music Vaults (Lite or Standard)
- Note types: song, album, artist, playlist, genre
- Key queries: by mood, BPM range, rating, genre
- Kanban use: playlist curation (Discover → Try → In Rotation → Retired)
- See: `04 - Vault Designs/Fat_Lady_Sings.md`

### AI / Knowledge Graph Vaults (Advanced)
- Note types: knowledge (KNW-NNNN), task (TSK-NNNN), decision (DEC-NNNN), session (SES-*), moc
- Key systems: drift detection, token-aware briefing, agent session logs
- Requires: REST API, Git, Dataview, Templater, QuickAdd, Commander, Linter
- See: `04 - Vault Designs/Prompt & Context Engineering (Rebuild).md`

### Multi-Vault Orchestration (Extreme)
- Multiple vaults connected via REST API (port 27123, one at a time)
- Central hub vault routes queries to domain-specific vaults
- Prometheus exporter scrapes vault metrics (note counts, stale %, query health)
- Grafana dashboards visualize cross-vault health
- Scripts in `05 - Snippets/Scripts/` handle vault switching + API calls

### Phone / Low-Resource Vaults (Lite)
- No community plugins — Obsidian Mobile has limited plugin support
- Templates are raw YAML frontmatter (no Templater)
- No Dataview queries — use tags + search instead
- Folder structure must be thumb-navigable (short names, flat hierarchy)
- Sync via Remotely Save or Obsidian Sync (not Git — no CLI on phone)

---

## Failure Checklist

If a vault build produces wrong results, run this before blaming the tools:

1. Did you read the skill note for this layer? (If no → stop, read it)
2. Did you use a "Copy-Paste Ready" example from the skill note? (If no → try it first, then customize)
3. Did you copy from another vault instead of reading the skill? (If yes → undo and start from skill note)
4. Did you skip any verification step for this layer? (If yes → run verification now)
5. Is there a design doc for this vault in `04 - Vault Designs/`? (If no → create one first)
6. Did you check the complexity tier? (If building Lite, layers 3/5/6/7 should not exist)

## Root Cause Reference

From the My_Music post-mortem (`07 - Archive/My_Music Post-Mortem.md`):

> "The builder treated a test vault (Fat_Lady_Sings) as the reference implementation instead of reading the source skill notes."

Every gap traced to one cause: **didn't read the note first.** This protocol + CLAUDE.md is the cure.

## Related Skills
- [[Vault Architecture]] — Layer 1
- [[Template Systems]] — Layer 2
- [[Linking & Backlinks Strategy]] — Layer 4
- [[Dashboards]] — Layer 5
- [[Dataview Dashboard Patterns]] — Layer 5
- [[Kanban Workflows]] — Layer 6

## Related Notes
- [[_Skill Index]] — master list of all skills
- [[_Plugin Index]] — master list of all plugins with status
- [[REST API Automation]] — multi-vault API scripts
- [[AI Workflows in Obsidian]] — agent integration patterns
