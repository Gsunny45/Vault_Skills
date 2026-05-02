---
type: plugin
name: Local GPT
category: AI
status: active
complexity: medium
downloads: ~50k+
last-verified: 2026-04-29
tags:
  - plugin
  - ai
  - offline
  - ollama
---

# Local GPT

> Plugin by pfrankov — adds local AI chat and text actions inside Obsidian using Ollama or LM Studio (any OpenAI-compatible endpoint). All processing stays on your machine.

## What It Does

Local GPT brings an AI assistant directly into Obsidian that runs **entirely offline** using local LLMs via [Ollama](https://ollama.com) or [LM Studio](https://lmstudio.ai). It adds a floating chat panel, inline text actions (summarize, rewrite, fix grammar), and a context menu for AI-powered editing — all without sending your notes to any external server.

It works as a **frontend** to a local LLM runner: your text stays local, models run on your CPU, and you never need an API key or internet connection once the runner is installed.

**Requires two companion pieces:**
1. **A local LLM runner** — [Ollama](https://ollama.com) or [LM Studio](https://lmstudio.ai)
2. **AI Providers** (companion plugin, same author) — manages the connection to the runner

## When To Use It

- You want **privacy** — notes should never leave your machine
- You work **offline** frequently and still want AI assistance
- You want to **avoid API subscription costs** (no OpenAI/Claude bills)
- You need quick inline actions: summarize a note, rewrite a paragraph, fix spelling/grammar
- You want AI-powered drafting without switching to a browser tab

## Minimal Setup

### Step 1: Choose Your LLM Runner

**Option A — Ollama** (simpler CLI, good for downloading models quickly)
1. Download from [ollama.com/download](https://ollama.com/download) — native Windows, no WSL2
2. Run installer (one click, installs as background service)
3. Pull a model: `ollama pull gemma2:2b`
4. Verify: `ollama --version`

**Option B — LM Studio** (GUI, better for local GGUF files)
1. Download from [lmstudio.ai](https://lmstudio.ai)
2. Install & open → **Local Inference Server** tab
3. Load your model: e.g., `LiquidAI_LFM2-2.6B-Exp-Q6_K.gguf`
4. Click **Start Server** (default: `http://localhost:1234`)

### Step 2: Install AI Providers (companion plugin)

1. Obsidian → Settings → Community Plugins → Browse
2. Search for **"AI Providers"** by pfrankov
3. Install & Enable
4. In AI Providers settings:

   **For Ollama:**
   - Click **"Add provider"** → select **Ollama**
   - Base URL: `http://localhost:11434`
   - Click **"Fetch models"** → select your pulled model
   - Click **"Set as active"**

   **For LM Studio:**
   - Click **"Add provider"** → select **OpenAI**
   - Base URL: `http://localhost:1234/v1`
   - Model: enter your loaded model name (e.g., `LiquidAI_LFM2-2.6B-Exp-Q6_K`)
   - Click **"Set as active"**

### Step 3: Install Local GPT

1. Obsidian → Settings → Community Plugins → Browse
2. Search for **"Local GPT"** by pfrankov
3. Install & Enable
4. Open Local GPT settings → under **"AI Provider"**, select the Ollama provider you created
5. Configure hotkeys:
   - `Local GPT: Action Palette` → `Ctrl+J`
   - `Local GPT: Show context menu` → `Ctrl+M`

Done. Select text in any note, press `Ctrl+M`, and pick an action.

## Key Settings

### AI Providers Settings
| Setting | Recommended Value | Notes |
|---|---|---|
| Provider Type (Ollama) | Ollama | For Ollama runner |
| Base URL (Ollama) | `http://localhost:11434` | Default Ollama port |
| Provider Type (LM Studio) | OpenAI | LM Studio uses OpenAI-compatible API |
| Base URL (LM Studio) | `http://localhost:1234/v1` | Default LM Studio port |
| Model | per model | See guide below for your hardware |

### Local GPT Settings
| Setting | Recommended Value | Notes |
|---|---|---|
| AI Provider | (your Ollama provider) | Created in AI Providers plugin |
| Default Model | (same as provider) | Can override per-action |
| Stream Response | On | Shows text as it generates |
| Max Tokens | 2048 | Higher = longer responses, slower |
| Temperature | 0.7 | 0.0 = strict, 1.0 = creative |

## Hardware-Best Model Guide

Based on your hardware (Intel i5-1335U, 16GB RAM, Iris Xe):

| Model | Runner | Size | RAM Use | Speed | Quality | Disk |
|---|---|---|---|---|---|---|
| `Liquid LFM 2.6B` | LM Studio | 2.6B | ~3GB | ⚡ Fastest | Decent | ~1.6 GB |
| `gemma2:2b` | Ollama | 2B | ~2GB | ⚡ Fast | Basic | 1.4 GB |
| `phi3:mini` | Ollama | 3.8B | ~4GB | 🏃 Moderate | Good | 2.3 GB |
| `llama3.2:3b` | Ollama | 3B | ~3.5GB | 🏃 Moderate | Good | 2.0 GB |
| `qwen3:8b` | Ollama | 8.2B | ~6GB | 🐢 Slow (20-40s) | Best | 4.9 GB |
| `mistral` | Ollama | 7B | ~8GB | 🐢 Slow | Best | 4.1 GB |

**Recommendation for your setup:** Use **LM Studio with Liquid LFM 2.6B** for daily fast tasks. Keep **Ollama with qwen3:8b** for when you need better quality and can wait. Switch between providers in AI Providers settings.

## Example Config / Usage

### Common Runner Commands

**Ollama:**
```bash
ollama list              # List installed models
ollama pull <model>      # Download a model
ollama rm <model>        # Delete a model
ollama --version         # Check if running
```

**LM Studio:**
- Open LM Studio → **Local Inference Server** tab
- Load your `.gguf` model file, click **Start Server**
- Default endpoint: `http://localhost:1234/v1`
- Server status shown in LM Studio window

### In-Obsidian Actions
Once installed, select any text and:
1. **Press `Ctrl+M`** → context menu with actions:
   - Summarize
   - Continue writing
   - Fix spelling & grammar
   - Change tone (formal/casual/professional)
   - Make shorter/longer
   - Find action items

2. **Press `Ctrl+J`** → Action Palette for free-form AI prompts:
   - "Explain this concept"
   - "Turn this into bullet points"
   - "Write a conclusion for this draft"

3. **Chat Panel** → Click the Local GPT icon in the ribbon to open a persistent chat sidebar

### Custom Prompt Template
In Local GPT settings, you can add custom prompts under "Custom Actions":
```
Name: Simplify
Prompt: Rewrite the following text at a 5th grade reading level. Keep all key information but simplify the language.
```

## Gotchas & Known Issues

- **Ollama / LM Studio must be running first** — Local GPT won't work if the runner isn't running. Ollama auto-starts as a service; LM Studio needs manual Start Server click.
- **First response is slow** — The first AI action after starting takes 5-30s (model loads into RAM). Subsequent responses are faster while cached.
- **CPU-only is usable but slow** — Iris Xe GPU has only 128MB VRAM, so models run on CPU exclusively. Expect 2-5s for 2.6B models, 20-40s for 8B models.
- **AI Providers is required** — Local GPT doesn't connect to runners directly. AI Providers must be installed and configured.
- **Disk space adds up** — Each model is 1.5-5GB. Use `ollama list` / `ollama rm` to manage Ollama models. LM Studio models are `.gguf` files in `%userprofile%\.lmstudio\models\`.
- **No vault-wide RAG** — Local GPT works on the current note/selection only. For vault-wide semantic search, add Smart Connections.
- **Switching providers** — You can have multiple providers (e.g., Ollama + LM Studio) and switch between them in AI Providers settings depending on speed vs quality needs.

## Works Well With
- [[REST API]] — Script external AI workflows via the REST API
- [[ChatGPT MD]] — Use online models (Gemini/ChatGPT) alongside Local GPT for local-only tasks
- [[Copilot]] — More advanced AI chat with vault context (can also use Ollama)

## Related Skills
- [[AI Workflows in Obsidian]]

## Links
- [GitHub — pfrankov/obsidian-local-gpt](https://github.com/pfrankov/obsidian-local-gpt)
- [GitHub — pfrankov/obsidian-ai-providers](https://github.com/pfrankov/obsidian-ai-providers) (companion plugin)
- [Ollama — Download](https://ollama.com/download)
- [Ollama — Model Library](https://ollama.com/library)
- [LM Studio — Download](https://lmstudio.ai)
