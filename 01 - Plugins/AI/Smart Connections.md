---
type: plugin
name: Smart Connections
category: AI
status: active
complexity: medium
downloads: 1M+
last-verified: 2026-04-30
tags:
  - plugin
  - ai
  - semantic-search
  - embeddings
  - knowledge-graph
---

# Smart Connections

> Plugin by Brian Petro — uses AI embeddings to find semantically related notes in your vault. Shows a persistent panel of notes that are conceptually related to what you're currently reading or writing, even if they share no keywords or links.

## What It Does

Smart Connections builds a local vector embedding index of your vault. When you open any note, the Smart Connections panel shows the most semantically similar notes — related by meaning, not just keywords. You can also chat with your vault using the Smart Chat feature.

Two main features:
- **Smart Connections panel** — always-on sidebar showing related notes ranked by similarity score
- **Smart Chat** — conversational Q&A over your vault using embeddings to retrieve relevant context

Supports local embeddings (no API, fully private) and cloud embeddings (OpenAI). Local mode uses a built-in model that runs on CPU.

## When To Use It

- Discovering forgotten notes that relate to what you're currently writing
- Finding connections between ideas you didn't explicitly link
- Researching a topic across your vault without knowing exact keywords
- "What else do I have about X?" — faster than search for conceptual matches
- Building a second brain that surfaces related context automatically
- Chat: "What have I written about productivity?" → synthesized answer from your vault

**Difference from Copilot Vault QA**: Smart Connections runs its panel passively as you read; Copilot Vault QA requires you to ask explicit questions. Use both for complementary coverage.

## Minimal Setup

### Local (free, offline, recommended for your hardware)
1. **Install**: Community Plugins → search "Smart Connections" by Brian Petro → Install & Enable
2. **Open the panel**: Ribbon → Smart Connections icon (or Command Palette → "Smart Connections: Open Smart Connections")
3. **Let it index** — first run builds an embedding index of all your notes. On your i5 with a mid-size vault, expect 1-5 minutes.
4. Open any note — the panel automatically shows related notes with similarity scores.

**No API key needed for local mode.** Smart Connections ships with a built-in local embedding model.

### Cloud (OpenAI, higher quality)
1. Settings → Smart Connections → Embedding Model → `text-embedding-3-small`
2. Settings → Smart Connections → API Key → paste your OpenAI key
3. Click **Re-index vault** after changing models

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Embedding model | Local (default) | Free, private, runs on CPU. Switch to `text-embedding-3-small` for better quality if you have OpenAI credits. |
| API Key | (only for cloud models) | Leave blank for local-only mode |
| Excluded folders | `03 - Templates, 05 - Snippets` | Prevents template/snippet files from polluting results |
| Maximum related notes | `10` | How many related notes to show in the panel |
| Minimum similarity score | `0.5` | Filter out weak matches. Lower = more results, more noise. |
| Show full file path | Off | Cleaner display; turn On if you have many same-named notes |
| Smart Chat model | `gpt-4o-mini` or local | The LLM used for Smart Chat conversations |
| Re-index on startup | Off | Only needed if your vault changes heavily between sessions |

## Example Config / Usage

### Smart Connections Panel
- Open any note → the panel populates automatically
- Each result shows: note title, similarity score (0-1), a brief excerpt
- Click any result to open that note
- Results update in real-time as you type or switch notes

### Smart Chat
- Ribbon → Smart Chat icon (speech bubble), or Command Palette → "Smart Connections: Open Smart Chat"
- Ask questions about your vault:
  - "What are my thoughts on Zettelkasten?"
  - "Summarize my notes on AI tools"
  - "What projects am I currently tracking?"
- Smart Chat retrieves relevant notes via embeddings, then sends them as context to the LLM

### Filtering results
In the panel, use the filter icon to:
- Limit results to a specific folder
- Show only notes with certain tags
- Adjust minimum similarity threshold on-the-fly

## Gotchas & Known Issues

- **First index is slow** — local embedding on CPU takes significant time for large vaults. 100 notes ≈ 30 seconds; 1000 notes ≈ 5-10 minutes on your i5. Run it overnight if needed.
- **Local model quality is lower than OpenAI** — local embeddings work well for obvious connections but miss subtle conceptual links that `text-embedding-3-small` would catch. Acceptable for personal PKM use.
- **Index doesn't update automatically on every save** — Smart Connections re-indexes periodically, not on every keystroke. Very recent edits may not appear in results immediately.
- **Excluded folders matter a lot** — including your templates folder in the index pollutes results with template structure noise. Always exclude `Templates` and `Snippets`.
- **High RAM usage during indexing** — local embedding can use 2-4GB RAM during the initial index build. Avoid running other memory-heavy tasks simultaneously.
- **Smart Chat requires an LLM provider** — the panel works offline, but Smart Chat needs either an OpenAI key or a local Ollama model to generate responses.
- **Similarity scores are relative** — a score of 0.7 doesn't mean "70% related" in an absolute sense. Scores are comparable within one vault but not across vaults.

## Works Well With

- [[Copilot]] — Copilot for explicit Q&A; Smart Connections for passive discovery while you work
- [[Dataview]] — use Dataview to query vault structure; Smart Connections to find semantic clusters
- [[Local GPT]] — Local GPT for text actions on current note; Smart Connections for surfacing related vault context
- [[Linking & Backlinks Strategy]] — Smart Connections helps you discover unlinked notes that should be linked

## Related Skills

- [[AI Workflows in Obsidian]]
- [[Linking & Backlinks Strategy]]

## Links

- [GitHub](https://github.com/brianpetro/obsidian-smart-connections)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=smart-connections)
