---
type: plugin
name: ChatGPT MD
category: AI
status: active
complexity: medium
downloads: 900k+
last-verified: 2026-05-02
tags:
  - plugin
  - ai
---

# ChatGPT MD

## What It Does
Converse with AI models (OpenAI, OpenRouter, local LLMs) directly inside any Markdown note in your Obsidian vault. Conversations are stored as plain Markdown — every message is editable, and you can switch models mid-conversation.

**Key capabilities:**
- Multi-turn chats saved as `.md` files with `role:user` / `role:assistant` formatting
- Multi-provider support: OpenAI (GPT-4o, GPT-5), OpenRouter.ai (90+ models including Claude, Gemini, DeepSeek, Perplexity), Ollama (local/offline), and LM Studio
- **Web access models** — OpenAI `gpt-4o-search-preview` and Perplexity via OpenRouter for real-time web search
- Per-note YAML frontmatter overrides all global settings (model, temperature, system prompt, and per-service URLs)
- Agents system (v3.1.0) — reusable AI personas defined as Markdown files, created via AI Wizard
- Tool calling (v3.0.0) — privacy-first vault search, file reading, and web search (Brave API). Uses a **human-in-the-loop** architecture: AI requests → tool executes locally → you filter results before returning to the model
- Link context — AI reads `[[Note Name]]` links for vault-aware responses
- Comment blocks (`%% ... %%`) are excluded from AI context
- Smart Titles — auto-generates note titles from conversation content
- **Chat templates** — reusable frontmatter templates from the companion [chatgpt-md-templates](https://github.com/bramses/chatgpt-md-templates) repo
- **Privacy by design** — "only storing data locally in your vault, with zero tracking". No data leaves your machine except direct API calls to your chosen AI provider.
- **MIT license** — open source, 104 automated tests, active CI/CD via GitHub Actions

## When To Use It
- **Replace copy-pasting** — keep AI conversations natively in your vault instead of juggling browser tabs
- **Research & sensemaking** — chat with an AI that can reference your actual notes via wiki links
- **Local/private AI** — pair with Ollama for fully offline, private LLM usage
- **Multi-model exploration** — compare responses from different models (GPT-4o, Claude, Llama, etc.) in the same note
- **Templated workflows** — use chat templates for recurring tasks like meeting summaries, brainstorming, or code review
- **On-the-go** — works on mobile; Ollama supports mobile CORS with `OLLAMA_ORIGINS=app://obsidian.md*`

## Minimal Setup

### 1. Install
- Obsidian Settings → Community Plugins → Browse → search "ChatGPT MD" → Install → Enable

### 2. Configure an AI Provider (pick one)

**Option A — OpenAI (cloud, easiest):**
- Get an API key from [platform.openai.com](https://platform.openai.com/api-keys)
- Paste it in ChatGPT MD settings → OpenAI API Key

**Option B — OpenRouter (cloud, 90+ models):**
- Get an API key from [openrouter.ai/keys](https://openrouter.ai/keys)
- Paste it in ChatGPT MD settings → OpenRouter API Key

**Option C — Ollama (local, free, offline):**
- Install [Ollama](https://ollama.ai) and pull a model: `ollama pull llama3.2`
- Set Ollama URL in plugin settings to `http://localhost:11434`

### 3. Start Chatting
- `Ctrl+P` → `ChatGPT MD: Chat` (or assign a hotkey like `Ctrl+J`)

## Key Settings
| Setting | Recommended Value | Notes |
|---|---|---|
| OpenAI API Key | *(your key)* | Required for OpenAI models |
| OpenRouter API Key | *(your key)* | Required for OpenRouter models |
| Default Model | `gpt-4o-mini` or `openrouter@deepseek/deepseek-chat` | Prefix with `openrouter@`, `ollama@`, or `lmstudio@` to use other providers |
| Temperature | `0.7` | 0 = deterministic, 2 = creative |
| Max Tokens | `2048` | Per-response token limit |
| Stream Responses | `ON` | See output as it's generated |
| System Commands | `''` | Default system prompt — can be overridden per note |
| Ollama URL | `http://localhost:11434` | Only needed if using Ollama |
| OpenRouter URL | `https://openrouter.ai/api` | Only needed if using OpenRouter |
| Tool Calling | `OFF` | Enable in settings to allow vault search / file read / web search |

## Example Config / Usage

### Per-Note Frontmatter (override global defaults)

Every field in the settings can be overridden per-note via YAML frontmatter:

```yaml
---
model: openrouter@anthropic/claude-sonnet-4-20250514
system_commands: ['You are a research assistant. Be concise and cite sources.']
temperature: 0.3
max_tokens: 4096
stream: true
openaiUrl: https://oai.deployment.custom.com/v1  # optional: custom OpenAI endpoint
openrouterUrl: https://openrouter.ai/api           # optional: custom OpenRouter URL
ollamaUrl: http://localhost:11434                   # optional: custom Ollama URL
---
```

### Basic Conversation Format
```markdown
---
model: gpt-4o-mini
---

# Brainstorming Ideas

role:user
What are some creative ways to organize my Obsidian vault?

role:assistant
Here are a few approaches:

1. **PARA Method** — Projects, Areas, Resources, Archives
2. **Zettelkasten** — atomic notes with bidirectional links
3. **Folder-less / tags-only** — rely entirely on search and links
```

### Using Link Context
```markdown
# Meeting Notes

Based on [[Project Roadmap]] and [[Q1 Goals]], what are the next steps?

role:assistant
Looking at your Project Roadmap and Q1 Goals, here are the recommended next steps...
```

### Agents (v3.1.0+)
Create an agent by creating a Markdown file in your vault with frontmatter:

```yaml
---
agent_name: "Code Reviewer"
model: openrouter@anthropic/claude-sonnet-4-20250514
system_commands: ['You are a senior software engineer reviewing code. Be thorough but constructive.']
temperature: 0.2
---
```

Use the "AI Wizard" command or write these manually, then invoke them from any note.

### Command Reference

| Command | What It Does |
|---------|-------------|
| `ChatGPT MD: Chat` | Start a new chat in the current note (assign a hotkey like `Ctrl+J`) |
| `ChatGPT MD: New Chat from Template` | Create a new chat note from a frontmatter template |
| `ChatGPT MD: New Chat with Highlighted Text` | Start a chat with selected text as the first message |
| `ChatGPT MD: Infer Title` | Auto-generate a note title from conversation content |
| `ChatGPT MD: Add Comment Block` | Insert `%% ... %%` around selected text (excluded from AI context) |
| `ChatGPT MD: Select Model` | Choose a different model for the current conversation |
| `ChatGPT MD: Clear Chat` | Remove all messages (keeps frontmatter) |
| `ChatGPT MD: Stop Streaming` | Halt an in-progress AI response (desktop only) |
| `ChatGPT MD: Add Divider` | Insert `---` separator between conversation sections |

## Gotchas & Known Issues
- **API keys are stored in Obsidian's local data** — not in your vault. They won't sync via git.
- **Ollama mobile CORS** — on mobile, you must start Ollama with `OLLAMA_ORIGINS=app://obsidian.md* ollama serve`
- **Streaming off** — if responses feel slow, ensure streaming is ON in settings
- **Token usage** — long conversations consume tokens from your API key's quota. Consider shorter system prompts and lower `max_tokens`
- **Model naming** — always prefix non-OpenAI models: `openrouter@model-name`, `ollama@model-name`, `lmstudio@model-name`
- **Unclosed code blocks** — the plugin auto-closes unfinished code blocks from AI responses, but preview may look odd until the response finishes
- **Beta features** — use the BRAT plugin to test pre-release versions if needed

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| "Model not found" | Wrong provider prefix | Prefix non-OpenAI models: `openrouter@model`, `ollama@model`, `lmstudio@model` |
| No response / spinner hangs | API key missing or invalid | Check key in plugin settings. If using Ollama, verify `ollama serve` is running |
| AI doesn't see my note content | Link context not enabled | Use `[[wikilinks]]` in your message and ensure the linked note exists |
| Responses are slow | Streaming is OFF or token limit too high | Enable `Stream Responses` in settings; reduce `max_tokens` |
| "Tool call failed" | Tool calling not enabled in settings | Settings → ChatGPT MD → Tool Calling → ON |
| Mobile: "Failed to connect" to Ollama | CORS | Start Ollama with `OLLAMA_ORIGINS=app://obsidian.md* ollama serve` |
| Conversation lost after restart | Note not saved | ChatGPT MD auto-saves — but check the note is in a synced folder if using git |
| Agent not appearing in list | Agent file has wrong frontmatter | Verify frontmatter includes `agent_name:` and `model:` — both are required |

## Works Well With
- [[Ollama]] / [[Local GPT]] — fully offline local models via Ollama or LM Studio
- [[BRAT]] — beta testing upcoming ChatGPT MD features before stable release
- [[Templater]] — use with chat templates for repeatable AI workflows
- [[Copilot]] — complementary: ChatGPT MD for in-note chats stored as markdown, Copilot for persistent sidebar chat and Vault QA. Both can use the same local models via Ollama/LM Studio.
- [[Homepage]] — set a ChatGPT MD chat note as your homepage for an AI-first landing page
- [[REST API]] — feed AI responses into external scripts; or use external AI tools to write notes that ChatGPT MD can then reference
- [[Dataview]] — query frontmatter from ChatGPT MD chat notes to build conversation dashboards

## Related Skills
- [[AI Workflows in Obsidian]] — patterns combining ChatGPT MD, Copilot, Gemini Scribe, and Local GPT for multi-model AI workflows
- [[Template Systems]] — create chat template notes with Templater for recurring AI interactions
- [[Dashboards]] — build a Dataview dashboard that tracks your AI conversations by model, topic, or agent

## Links
- [GitHub](https://github.com/bramses/chatgpt-md)
- [Obsidian Plugin Page](https://obsidian.md/plugins?search=chatgpt%20md)
- [Chat Templates Repo](https://github.com/bramses/chatgpt-md-templates)
- [OpenRouter](https://openrouter.ai)
- [Ollama](https://ollama.ai)
