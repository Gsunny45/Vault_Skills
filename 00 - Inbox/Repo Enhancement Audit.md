---
type: note
tags:
  - audit
  - enhancement
  - repo-crosscheck
created: 2026-05-01
---

# Repo Enhancement Audit

> Cross-check of all 42 plugin repos + 9 discovered repos against existing Vault_Skills content.
> Status: ✅ Critical fixes applied. Remaining items queued.

---

## Critical Fixes Applied

| Note | What Was Missing | Fix Applied |
|---|---|---|
| Gemini Scribe | Missing GitHub repo (allenhutchison/obsidian-gemini) | ✅ Added link |
| Gemini Scribe | v4.x features undocumented (Agent Mode, MCP, semantic search, session recall, file diff) | ✅ Added 6 new capabilities |
| Gemini Scribe | Missing works-well-with references (REST API, Obsidian Git for Agent Mode) | ✅ Added |
| Copilot | v3.0+ Agents System, web clipper, GitHub Copilot integration | ✅ Added v3+ features section |
| Copilot | Missing cross-refs (Homepage, Omnisearch, REST API) | ✅ Added |
| REST API | Missing MCP Plugin reference (uses REST API under the hood) | ✅ Added |

---

## Enhancement Backlog (Not Yet Done)

### P1 — Plugin Notes That Need Stub → Full Upgrade
These are in the Plugin Index but only have stub notes. Writing full notes would incorporate recent repo features.

| Plugin | Repo | Missing Features |
|---|---|---|
| **ChatGPT MD** | bramses/chatgpt-md | v3.1.0 Agents System, privacy-first AI tool calling, 104 tests, active CI/CD |
| **Smart Connections** | brianpetro/obsidian-smart-connections | v4 major rewrite: pause connections, pinned connections, events/notifications |
| **Obsidian Git** | Vinzent03/obsidian-git | 10.7k ⭐ — most starred plugin, needs full note |
| **Dataview** | blacksmithgu/obsidian-dataview | 8.9k ⭐ — essential but only a stub |
| **Templater** | SilentVoid13/Templater | v2.20.0 (Apr 2026), 4.9k ⭐ — needs full note |
| **Tasks** | obsidian-tasks-group/obsidian-tasks | v7.23.1 (Feb 2026), 3.7k ⭐ — needs full note |
| **Excalidraw** | zsviczian/obsidian-excalidraw-plugin | 6.8k ⭐, monthly releases, script library — stub only |

### P2 — Plugin Notes That Need Feature Update
These have full notes but newer repo features aren't reflected.

| Plugin | What's Missing |
|---|---|
| **Advanced Canvas** | Check GitHub for any new shape types or features since last note |
| **Kanban** | Already flagged ⚠️ seeking maintainers. Should add note about 500+ open issues and fork options |

### P3 — New Plugins to Evaluate for Index
From the 9 discovered repos — decide which to add to Plugin Index.

| Repo | Category | Decision |
|---|---|---|
| **obsidian-claude-code** | AI | Claude AI in sidebar. Evaluate if needed alongside Copilot. |
| **obsidian-decentralized** | Sync & Backup | P2P sync alternative. Add if local sync priority. |
| **obsidian-better-export-pdf** | Academic & Research | Cross-ref from PDF++ note. |
| **obsidian-mcp-plugin** | Integration | MCP protocol via REST API. Cross-ref from REST API note. |
| **Breadcrumbs** | UI & Navigation | Typed links. Add if hierarchical nav needed. |
| **Various Complements** | Writing & Editing | Autocomplete. Add if writing speed is priority. |
| **Block Properties** | Core Enhanced | Block metadata. Emerging standard alongside Bases. |
| **Auto-properties** | Automation | Auto YAML. Low effort, high convenience. |
| **SystemSculpt** | AI | Multi-provider AI with approvals. Evaluate as Copilot alternative. |

### P4 — Skill Notes Missing
Patterns that span multiple plugins, not yet documented.

| Skill | Plugins Involved |
|---|---|
| **AI Workflows in Obsidian** | Gemini Scribe + Copilot + Local GPT + ChatGPT MD |
| **Vault Search Strategy** | Omnisearch + Dataview + Copilot Vault QA + Smart Connections |
| **Backup & Sync Strategy** | Obsidian Git + Remotely Save (+ decentralized?) |
| **Obsidian + External AI Agents** | REST API + MCP Plugin + Claude Code |

---

## Key Repo Health Flags

| Plugin | Stars | Last Release | Health |
|---|---|---|---|
| Obsidian Git | 10.7k | Apr 2026 | ✅ Excellent |
| Dataview | 8.9k | Apr 2025 | ✅ Stable |
| Copilot | 6.9k | Jan 2026 | ✅ Very active |
| Excalidraw | 6.8k | Monthly | ✅ Very active |
| Smart Connections | 4.9k | Recent | ✅ Active |
| Templater | 4.9k | Apr 2026 | ✅ Very active |
| Kanban | 4.2k | May 2024 | ⚠️ Seeking maintainers |
| Tasks | 3.7k | Feb 2026 | ✅ Active |
| Day Planner | 2.6k | May 2025 | ✅ Active |
| Spaced Repetition | 2.3k | Apr 2026 | ✅ Very active |

---

## Plugin Note Priority (Updated Queue)

Based on this audit, the best order for remaining plugin notes:

1. **ChatGPT MD** — highest-value AI plugin, v3 features, already next in queue
2. **Gemini Scribe** — already has stub, update with v4 features (partially done)
3. **Obsidian Git** — 10.7k ⭐, essential backup tool
4. **Dataview** — 8.9k ⭐, vault-wide dependency for many plugins
5. **Templater** — 4.9k ⭐, second most-downloaded plugin
6. **Tasks** — 3.7k ⭐, gold standard for task management
7. **Excalidraw** — 6.8k ⭐, monthly releases, script library
8. **Smart Connections** — v4 rewrite, semantic connections
9. New plugin evaluations (claude-code, decentralized, etc.)
