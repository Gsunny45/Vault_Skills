---
type: plugin
name: Smart Connections
category: AI
status: active
complexity: medium
downloads: 1M+
last-verified: 2026-05-04
tags:
  - plugin
  - ai
  - semantic-search
  - embeddings
  - knowledge-graph
  - v4
---

# Smart Connections

> Plugin by Brian Petro — uses AI embeddings to find semantically related notes in your vault. v4 streamlined the core plugin: install, enable, AI connections just work. Smart Chat spun out into its own plugin. Pro tier adds advanced features.

## What It Does

Smart Connections builds a local vector embedding index of your vault. When you open any note, the sidebar panel shows semantically similar notes — related by meaning, not just keywords.

**v4 redesign:** Core plugin refocused on the connections panel. Smart Chat moved to a separate plugin ([[Smart Chat]]). Advanced features moved to **Connections Pro** paid tier.

### Core (Free) Features — v4

- **Connections sidebar** — always-on panel showing related notes ranked by similarity
- **Pause Connections** — freeze results so you can browse while keeping connections to a specific note
- **Pin Connections** — keep certain results always visible per note
- **Copy Connections as Links** — right-click results → copy all links to clipboard
- **Smart Context** (briefcase icon) — copy all connection content as AI-ready context bundles. Add/remove items before copying.
- **Drag-to-link & hover preview** — drag results into notes to create links
- **Footer connections** — related notes at bottom of notes (mobile-friendly)
- **Smart Lookup** — question-first semantic search ("search by meaning, not keywords")
- **Events & Notifications** — notification modal for indexing complete, reimports after model changes, exclusion warnings. Access via Smart Env in status bar.
- **Local embeddings** — zero-setup, offline-capable, no API key required
- **Mobile compatible** (iOS/Android)

### Connections Pro (Paid)

- **Inline editor badges** — related blocks surface inside the editor
- **Footer connections update as you type** — live relevance while writing
- **Advanced ranking** — configurable scoring/ranking algorithms
- **Bases integration** — `score_connection`, `list_connections` functions
- **Duplicate & near-duplicate block detection**
- **Smart Graph** — landscape/visual view of connections
- **Performance index** for larger vaults

## Smart Environment

Shared local core powering all Smart Plugins. Handles indexing, embeddings, and cross-plugin configuration. Single settings panel for model providers and embedding models.

## When To Use It

- Discovering forgotten notes related to current note
- Finding connections between ideas you didn't explicitly link
- Researching across vault without knowing exact keywords
- Building second brain that surfaces related context automatically
- Sending connection bundles to AI chat (Smart Context)

**vs Copilot Vault QA:** Smart Connections panel runs passively as you read; Copilot needs explicit questions. Complementary.

## Minimal Setup

1. **Install**: Community Plugins → "Smart Connections" by Brian Petro → Install & Enable
2. **Open the panel**: Ribbon → Smart Connections icon (or Command Palette → "Smart Connections: Open Smart Connections")
3. **Let it index** — first run builds embedding index. On i5 with mid-size vault, expect 1-5 minutes.
4. Open any note — panel shows related notes with similarity scores.

**No API key needed.** Built-in local embedding model.

### Smart Chat (separate plugin, v4+)
Smart Chat is no longer bundled. Install [[Smart Chat]] separately if you want conversational Q&A over your vault.

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Embedding model | Local (default) | Free, private, CPU. Switch to cloud models for better quality. |
| API Key | (leave blank) | Only needed for cloud embedding models |
| Excluded folders | `03 - Templates, 05 - Snippets` | Prevents template noise in results |
| Maximum related notes | `10` | Panel result count |
| Minimum similarity score | `0.5` | Lower = more results, more noise |
| Show full file path | Off | Cleaner display |
| Re-index on startup | Off | Only if vault changes heavily between sessions |

## v4 New Features Summary

| Feature | Core/Pro | What It Does |
| --- | --- | --- |
| Pause Connections | Core | Freeze panel results while browsing other notes |
| Pin Connections | Core | Keep specific results always visible |
| Smart Context | Core | Bundle connections as AI chat context |
| Copy as Links | Core | Right-click → copy all result links |
| Events & Notifications | Core | Alerts for indexing, reimports, errors |
| Inline editor badges | Pro | Related blocks inside the editor |
| Live footer updates | Pro | Connections update as you type |
| Advanced ranking | Pro | Custom scoring algorithms |

## Gotchas & Known Issues

- **First index is slow** — local embedding on CPU: 100 notes ≈ 30s, 1000 notes ≈ 5-10 min on i5
- **Local model quality < OpenAI** — local catches obvious connections, misses subtle ones
- **Index updates periodically, not on every keystroke** — recent edits may not appear immediately
- **Exclude Templates & Snippets** — otherwise results fill with structural noise
- **RAM usage during indexing** — 2-4GB during initial build
- **v4 change: Smart Chat is now separate** — if you upgrade and lose chat, install the new [[Smart Chat]] plugin
- **Similarity scores are relative** — comparable within one vault, not across vaults
- **Pro is paid** — Connections Pro is a subscription tier. Core remains free.

## Works Well With

- [[Copilot]] — explicit Q&A; Smart Connections for passive discovery
- [[Dataview]] — query vault structure; Smart Connections for semantic clusters
- [[Local GPT]] — text actions on current note; Smart Connections for related vault context
- [[Linking & Backlinks Strategy]] — discover unlinked notes that should be linked
- [[Smart Chat]] — separate plugin for conversational vault Q&A (v4+)

## Related Skills

- [[AI Workflows in Obsidian]]
- [[Linking & Backlinks Strategy]]

## Links

- [GitHub](https://github.com/brianpetro/obsidian-smart-connections)
- [Official Site](https://smartconnections.app/smart-connections/)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=smart-connections)
