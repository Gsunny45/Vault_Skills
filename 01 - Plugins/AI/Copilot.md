---
type: plugin
name: Copilot
category: AI
status: active
complexity: high
downloads: 1.2M+
last-verified: 2026-04-30
tags:
  - plugin
  - ai
  - chat
  - vault-qa
  - agent
---

# Copilot

> Plugin by Logan Yang — a full-featured AI assistant for Obsidian with chat, vault Q&A, and agentic modes. Supports 15+ AI providers including OpenAI, Anthropic, Google, Azure, Ollama, and LM Studio.

## What It Does

Copilot is one of the most capable AI plugins for Obsidian. Unlike ChatGPT MD (which stores chats as notes) or Local GPT (which focuses on text actions), Copilot provides a persistent chat sidebar with three distinct modes and deep vault integration.

Three modes:
- **Chat** — standard AI conversation in a sidebar, with optional context from selected notes
- **Vault QA** — uses a local vector index to answer questions about your entire vault ("What did I write about X?")
- **Copilot Plus (Agent)** — agentic mode that can read/write vault files, run commands, and take multi-step actions

**v3+ additional features:**
- **Agents System** — create reusable AI personas with custom system prompts, models, and temperature
- **Built-in web clipper** — clip web pages and YouTube transcripts
- **GitHub Copilot integration** — use your GitHub Copilot subscription

Supports 15+ providers: OpenAI, Anthropic Claude, Google Gemini, Azure OpenAI, Cohere, Groq, OpenRouter, Ollama (local), LM Studio (local), and more.

## When To Use It

- "Ask my vault" queries — find and synthesize information across many notes
- Long-form AI conversations with access to your notes as context
- Using local models (Ollama/LM Studio) with a polished chat UI
- Agent workflows: "Create a project note for X, link it to Y, add it to my task list"
- Comparing multiple AI providers without leaving Obsidian
- Vault Q&A: "Summarize everything I've written about Python" or "What decisions did I make last month?"

## Minimal Setup

### 1. Install
Community Plugins → search "Copilot" by Logan Yang → Install & Enable

### 2. Add at least one AI provider
Settings → Copilot → Model → Add Model:

**OpenAI:**
- Provider: OpenAI
- API Key: from [platform.openai.com](https://platform.openai.com/api-keys)
- Model: `gpt-4o-mini` (cheapest) or `gpt-4o`

**Anthropic (Claude):**
- Provider: Anthropic
- API Key: from [console.anthropic.com](https://console.anthropic.com)
- Model: `claude-haiku-4-5-20251001` (fast/cheap) or `claude-sonnet-4-6`

**Ollama (local/free):**
- Provider: Ollama
- Base URL: `http://localhost:11434`
- Model: any model you've pulled (e.g. `llama3.2:3b`)

### 3. Open the chat panel
- Left ribbon → Copilot icon, or
- Command Palette → "Copilot: Open Copilot Chat"

### 4. Set up Vault QA (optional but high value)
- Settings → Copilot → Vault QA → Indexing
- Click **Index Vault** — builds a local embedding index of all your notes
- Re-index periodically (or enable auto-indexing)
- Switch to "Vault QA" mode in the chat panel to query your vault

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Default model | (your preferred model) | Set to your daily-driver model |
| Default mode | Chat | Change to Vault QA once you've indexed your vault |
| Auto-save chat history | On | Saves conversations to a configurable folder |
| Chat history folder | `04 - Archive/Copilot Chats` | Keep chats out of your main vault structure |
| Temperature | `0.7` | Lower for factual tasks; higher for creative |
| Max tokens | `2000` | Increase for long outputs, decrease to save costs |
| Embedding model | `text-embedding-3-small` (OpenAI) | Cheaper than ada-002 with similar quality for vault indexing |
| Exclusion paths | `03 - Templates, 05 - Snippets` | Prevents template/snippet files from being indexed in Vault QA |
| Enable Copilot Plus | Off by default | Turn On when you want agentic features — read the permissions carefully |

## Vault QA Setup

Vault QA builds a vector embedding index of your notes and uses it to answer questions semantically — not just keyword search.

```
Settings → Copilot → Vault QA
├── Embedding provider: OpenAI (or Ollama with nomic-embed-text)
├── Embedding model: text-embedding-3-small
├── Exclusion patterns: 03 - Templates, 05 - Snippets, .obsidian
└── Click "Index Vault"
```

**For fully local/offline Vault QA:**
1. Install Ollama and pull: `ollama pull nomic-embed-text`
2. Settings → Copilot → Vault QA → Embedding provider: Ollama
3. Model: `nomic-embed-text`
4. Index your vault — no internet, no API costs, ~2-4GB RAM for indexing

## Example Interactions

**Vault QA:**
- "What are my notes about Dataview?" → synthesizes from all matching notes
- "Summarize my thoughts on productivity systems" → cross-vault synthesis
- "What plugins have I documented?" → queries your vault structure

**Chat with note context:**
1. Open a note
2. Command Palette → "Copilot: Add current note to context"
3. Ask "Summarize the key points" or "What's missing from this?"

**Agent mode (Copilot Plus):**
- "Create a new project note for [name], add it to my Kanban board, and link it from the dashboard"
- Copilot reads/writes files and runs commands to execute multi-step workflows

## Gotchas & Known Issues

- **Vault indexing takes time** — first-time indexing of a large vault (500+ notes) can take 5-15 minutes and uses significant API credits if using OpenAI embeddings. Use Ollama embeddings to avoid costs.
- **Re-indexing required after major vault changes** — new notes don't auto-index unless you enable background indexing. Stale index = worse Vault QA answers.
- **Copilot Plus is experimental** — the agentic mode can make unintended vault changes. Always have a git backup (Obsidian Git) before running agent workflows.
- **Chat history grows fast** — if auto-save is on, chats accumulate quickly. Set a dedicated archive folder and periodically clean up.
- **Local models give lower quality Vault QA** — embedding quality from Ollama models is lower than OpenAI's models. Acceptable for personal use; noticeable for large vaults.
- **Context window limits** — for large notes or many-note context, you can hit model limits. Copilot will warn but won't always trim gracefully.
- **Slow on i5 + integrated GPU with local models** — inference via Ollama is CPU-bound on your hardware. Use small models (≤3B) for acceptable speed.

## Works Well With

- [[Local GPT]] — Local GPT for quick inline text actions; Copilot for full chat and vault Q&A
- [[ChatGPT MD]] — ChatGPT MD stores conversations as notes; Copilot is a sidebar chat. Use both based on whether you want chat-as-notes or chat-as-tool.
- [[Smart Connections]] — Smart Connections finds related notes visually; Copilot queries them conversationally
- [[Obsidian Git]] — essential backup before using Copilot Plus agent mode
- [[Dataview]] — ask Copilot questions that Dataview queries would be too complex to express
- [[Homepage]] — add Copilot chat access from homepage via Commands on Open
- [[Omnisearch]] — Omnisearch for fast keyword search; Copilot for semantic Q&A
- [[REST API]] — Copilot Plus agent can use REST API for external tool access

## Related Skills

- [[AI Workflows in Obsidian]]
- [[Beta Testing Workflow]]

## Links

- [GitHub](https://github.com/logancyang/obsidian-copilot)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=copilot)
- [Official Docs](https://www.obsidiancopilot.com/en/docs)
