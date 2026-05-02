---
type: plugin
name: Gemini Scribe
category: AI
status: active
complexity: medium
downloads: ~10k
last-verified: 2026-04-30
tags:
  - plugin
  - ai
  - gemini
  - google
  - writing
---

# Gemini Scribe

> Plugin by Allen Hutchison — integrates Google Gemini AI models (or local Ollama models) into Obsidian for text generation, rewriting, vault agent tasks, and summarization. 995+ commits, actively maintained.

## What It Does

Gemini Scribe connects Obsidian to Google's Gemini models (Gemini 1.5 Flash, Gemini 1.5 Pro, Gemini 2.0 Flash, etc.) for AI-powered text actions. Select text in a note and apply AI operations via the command palette or context menu.

**Key capabilities (v4.7.0):**
- **Two providers** — Google Gemini (cloud, API key) or Ollama (local, free, no API key needed)
- **Selection-based actions** — select text → apply AI transformation (summarize, rewrite, fix grammar)
- **Custom prompts** — define reusable prompt templates that appear as commands
- **Sidebar chat panel** — persistent AI conversation alongside your notes
- **Agent Mode** — AI tool calling: search vault, read/create/edit/move/delete files, web search, deep research with citations
- **Projects** (v4.7.0) — scope agent sessions to a folder with custom instructions, permissions, and skill filters
- **Scheduled Tasks** — recurring AI prompts on daily, weekly, or interval schedules
- **IDE-style completions** — inline AI suggestions after 750ms typing pause, accept with Tab
- **Smart summarization** — one-sentence summaries auto-stored in document frontmatter
- **Experimental semantic vault search** — meaning-based retrieval across notes
- **MCP server integration** — connect external tools via Model Context Protocol
- **Agent Skills** — extensible skill packages (agentskills.io spec)
- **Granular permissions** — per-tool controls with presets: Read Only, Cautious, Edit Mode, YOLO
- **Session recall** — agent searches past conversations for context
- **Binary file awareness** — read_file handles images, audio, video, PDFs
- **File diff review** — see proposed changes before applying
- **Free API tier** — Gemini API has a generous free tier (unlike OpenAI)
- **Large context window** — Gemini 1.5 Pro supports 1M tokens, good for long notes

## When To Use It

- You want a free cloud AI option with a generous free tier (Gemini)
- You want a local AI option via Ollama with agent capabilities (unlike ChatGPT MD's simple local chat)
- You use Google Workspace / prefer staying in the Google ecosystem
- Large-context tasks — summarizing very long notes or documents (Gemini 1.5 Pro handles more tokens than GPT-4o)
- You need scheduled AI tasks, IDE-style autocomplete, or agent skills
- A lighter alternative to Copilot if you just need text rewriting/summarizing

**Note**: For a more general-purpose AI chat plugin, consider [[ChatGPT MD]] (supports Gemini via OpenRouter, stores chats as notes) or [[Copilot]] (supports Gemini natively, better vault QA) — both offer more conversation features. Gemini Scribe excels at agent tasks, scheduled automation, and large-context work.

## Minimal Setup

1. **Install**: Community Plugins → search "Gemini Scribe" → Install & Enable

2. **Configure an AI provider** (pick one):

   **Option A — Google Gemini (cloud, free tier):**
   - Get a free API key from [aistudio.google.com](https://aistudio.google.com/app/apikey)
   - Settings → Gemini Scribe → Provider → `Google Gemini` → paste API key
   - Recommended model: `gemini-2.0-flash` (fast, free, 15 requests/minute)

   **Option B — Ollama (local, free, offline, no API key):**
   - Install [Ollama](https://ollama.ai) and pull a model: `ollama pull llama3.2`
   - Settings → Gemini Scribe → Provider → `Ollama` → set URL to `http://localhost:11434`
   - Note: Some Gemini-only features (semantic search, web search) won't be available

3. **Test it**: Select any text in a note → `Ctrl+P` → "Gemini Scribe: Summarize selection" → verify output appears

4. **Assign hotkeys (optional)**: Settings → Hotkeys → search "Gemini Scribe" → assign shortcuts (e.g., `Ctrl+Shift+S` for summarize)

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Provider | `Google Gemini` or `Ollama` | Switch between cloud (Gemini) and local (Ollama) |
| API Key | (your Gemini API key) | Only needed for Google Gemini provider |
| Model | `gemini-2.0-flash` | Flash = fast and free; Pro = higher quality, lower rate limits |
| Temperature | `0.7` | Lower (0.1–0.3) for factual; higher (0.8–1.0) for creative |
| Max output tokens | `2048` | Increase to `4096` or `8192` for long-form generation |
| System prompt | (optional) | Default instruction prepended to all requests |
| Custom prompts | (configure in-plugin) | Define reusable prompt templates (see examples below) |
| Agent Mode | Off | Enable for tool-calling (search, read, create, edit, delete files) |
| Agent permissions | `Cautious` | Presets: Read Only, Cautious, Edit Mode, YOLO — Cautious prompts before each tool action |
| Scheduled Tasks | (configure per-task) | Recurring AI prompts: daily, weekly, or custom intervals |
| Completions | Off | Enable for IDE-style inline suggestions after 750ms typing pause |
| Smart summarization | Off | Auto-generates one-sentence summaries stored in file frontmatter |
| Semantic search index | (build on first use) | Experimental vault search — needs indexing pass |

## Free Tier Limits (as of 2026)

| Model | Free RPM | Free TPM | Notes |
|---|---|---|---|
| Gemini 1.5 Flash | 15 | 1M | More than enough for personal use |
| Gemini 1.5 Pro | 2 | 32k | Very limited free tier; burst use only |
| Gemini 2.0 Flash | 15 | 1M | Best free option for current tasks |

## Example Config / Usage

### Quick Text Actions (No Config Needed)

After setup, these commands are available immediately via `Ctrl+P`:

| Command | What It Does | Best Hotkey |
|---------|-------------|-------------|
| `Gemini Scribe: Summarize selection` | Condenses selected text to key points | `Ctrl+Shift+S` |
| `Gemini Scribe: Rewrite selection` | Rephrases selected text (same meaning, different wording) | `Ctrl+Shift+R` |
| `Gemini Scribe: Fix grammar/spelling` | Proofreads selected text | `Ctrl+Shift+G` |
| `Gemini Scribe: Continue text` | Extends the selection with AI-written continuation | — |
| `Gemini Scribe: Chat` | Opens sidebar chat panel | `Ctrl+Shift+C` |
| `Gemini Scribe: Ask AI about selection` | Sends selection as context for a Q&A prompt | — |

### Custom Prompts Configuration

In plugin settings, define reusable custom prompts. These appear alongside built-in commands:

```
Prompt Name: TL;DR
Prompt: Summarize this in 3 bullet points. Use simple language.

Prompt Name: Make More Formal
Prompt: Rewrite this text in a professional, formal tone. Keep the same meaning.

Prompt Name: Extract Action Items
Prompt: Extract all action items, owners, and deadlines from this text. Format as a table.

Prompt Name: Explain Like I'm 5
Prompt: Explain the concept in this text to a complete beginner. Use simple analogies.
```

After saving, these appear in the command palette as `Gemini Scribe: TL;DR`, `Gemini Scribe: Make More Formal`, etc.

### Agent Mode (Experimental)

Enable in Settings → Agent Mode → On. Then use the command palette:

`Gemini Scribe: Ask AI to...` — describe a multi-step task in natural language:

> "Find all notes in the Inbox folder that are older than 7 days, summarize each one, and add a summary frontmatter field."

Agent Mode can search, read, and modify vault files. Always use [[Obsidian Git]] before running agent commands.

### Using with Long Notes

Gemini 1.5 Pro's 1M token context window makes it uniquely suited for large documents:

1. Open a long research note or meeting transcript (10k+ words)
2. Set the note's frontmatter to use the larger model:
   ```yaml
   ---
   model: gemini-1.5-pro
   max_tokens: 8192
   temperature: 0.3
   ---
   ```
3. Use `Summarize selection` on different sections, or use `Chat` to ask questions about the full document context

## Gotchas & Known Issues

- **API key usage policy** — the free Gemini API key may be used to train Google's models. If vault content is private/sensitive, use a local model instead (Local GPT + Ollama).
- **Rate limits on free tier** — 15 RPM is fine for interactive use but will hit limits in bulk operations.
- **Agent Mode is experimental** — tool-calling can make unintended vault changes. Back up via Obsidian Git before using agent features.
- **Semantic search requires indexing** — experimental vault search needs an initial indexing pass and re-indexing after vault changes.
- **No vault-wide context** — standard chat works on selections, not your whole vault. Use Agent Mode or Copilot for vault Q&A.
- **Ollama mode limits** — switching to Ollama provider disables Gemini-only features (semantic search, web search, Gemini-specific models). You can switch providers in settings at any time.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| "API key not valid" / 403 | Key is missing, wrong, or expired | Regenerate key at [aistudio.google.com](https://aistudio.google.com/app/apikey) and paste in settings |
| No response when selecting text | Plugin not enabled or model misconfigured | Check plugin is enabled in Community Plugins. Verify model name is correct in settings |
| "Rate limit exceeded" | Exceeded free RPM | Wait 1 minute. Consider upgrading to paid tier or switching to `gemini-1.5-flash` (higher rate limit) |
| Agent Mode makes wrong changes | Experimental feature, imprecise tool-calling | Always use [[Obsidian Git]] before agent commands. Review diffs before applying |
| Text actions do nothing | No text selected | Select text *before* running the command. Commands operate on the current selection |
| Semantic search returns nothing | Index not built | Run indexing command once, then re-index after adding/changing notes |
| "Model not available" | Model name changed or deprecated | Update to latest model name: `gemini-1.5-flash`, `gemini-2.0-flash`, or `gemini-1.5-pro` |

## Works Well With

- [[ChatGPT MD]] — ChatGPT MD supports Gemini via OpenRouter and may offer more control over model selection
- [[Copilot]] — Copilot supports Gemini natively with better vault integration and Vault QA mode
- [[Local GPT]] — local alternative when you need privacy; complements Gemini Scribe's cloud capabilities
- [[REST API]] — Agent Mode can use REST API for external tool calling
- [[Obsidian Git]] — backup before using Agent Mode's vault-modifying capabilities
- [[Homepage]] — set a Gemini Scribe chat note as your AI-assisted homepage
- [[Templater]] — combine with Templater templates for AI-powered note generation on creation

## Related Skills

- [[AI Workflows in Obsidian]] — patterns combining Gemini Scribe, ChatGPT MD, Copilot, and Local GPT
- [[Template Systems]] — create Templater templates that auto-invoke Gemini Scribe for AI-generated content

## Links

- [GitHub — allenhutchison/obsidian-gemini](https://github.com/allenhutchison/obsidian-gemini)
- [Obsidian Plugin Page](https://obsidian.md/plugins?search=gemini+scribe)
- [Google AI Studio](https://aistudio.google.com)
