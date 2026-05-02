---
type: plugin
name: Obsidian Git
category: Sync & Backup
status: active
complexity: medium
downloads: 2.4M+
last-verified: 2026-04-30
tags:
  - plugin
  - sync
  - backup
  - git
  - version-control
---

# Obsidian Git

> Plugin by Vinzent03 (maintained since March 2021, originally by denolehov) — automatic git backup and sync for Obsidian vaults. Commit and push on a schedule without ever touching the terminal. Also enables cross-device sync via a git remote. **v2.38.2** · 964 commits · 145 releases · MIT license.

## What It Does

Obsidian Git integrates a git workflow directly into Obsidian. It watches your vault for changes and automatically stages, commits, and pushes to a remote repository on a configurable interval. On pull, it fetches and merges remote changes — enabling both backup and basic cross-device sync.

Key features:
- **Auto-commit and push** on a time interval (e.g., every 10 minutes)
- **Auto-pull** on Obsidian startup to fetch changes from other devices
- **Manual commit** via Command Palette at any time
- **Diff view** — see what changed in the last commit
- **Git history** — view and restore past versions of any file
- **Source control panel** — stage/unstage individual files, commit, push/pull from a GUI sidebar
- **Editor gutter signs** (desktop only) — line-level indicators showing added/modified/deleted lines; clickable to stage or reset individual hunks
- **Submodule support** — for vaults that include other git repos
- **Open file on GitHub** — opens the current file in the remote repo's browser view
- **Commit variants** — `Commit` (staged only / nothing if none staged), `Commit all changes` (bypasses staging), `Commit-and-sync and close` (syncs then closes Obsidian)

## When To Use It

- Protecting your vault from accidental deletion or file corruption
- Syncing your vault between desktop and laptop (or WSL2 environments)
- Maintaining full version history of all your notes
- Backup before risky operations (plugin updates, bulk renames, Excalidraw edits)
- Sharing a vault as a public or private GitHub repository
- Rolling back to a previous version of a note (File History)

## Prerequisites

Git must be installed on Windows before this plugin works.

```powershell
# Check if git is installed
git --version

# If not installed, download from:
# https://git-scm.com/download/win
# Or via winget:
winget install Git.Git
```

After installing git, configure identity (required for commits):
```powershell
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

## Minimal Setup

### 1. Initialize the vault as a git repo
Open PowerShell in your vault folder:
```powershell
cd "C:\Users\MarsBase\Documents\Vault_Skills"
git init
git add .
git commit -m "Initial commit"
```

### 2. Add a remote (GitHub example)
Create a repo on GitHub (can be private), then:
```powershell
git remote add origin https://github.com/YOUR_USERNAME/vault-skills.git
git branch -M main
git push -u origin main
```

### 3. Install and configure the plugin
- Community Plugins → search "Obsidian Git" by Vinzent03 → Install & Enable
- Settings → Obsidian Git → configure auto-commit/push interval

### 4. Test it
- Command Palette → "Obsidian Git: Create backup" → should commit and push
- Check GitHub to confirm the push

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Auto-commit message | `vault backup: {{date}}` | `{{date}}` inserts timestamp |
| Auto push after commit | On | Commits locally + pushes to remote in one step |
| Auto backup interval (minutes) | `10` | Every 10 min; reduce to 30 if CPU/I-O is a concern |
| Auto pull on startup | On | Fetches remote changes when Obsidian opens |
| Pull updates on startup | Rebase | Cleaner history than merge; change to "Merge" if you prefer |
| Commit message on manual backup | `manual: {{date}}` | |
| Disable notifications | Off | Keep notifications on so you know backups are happening |
| Show status bar | On | Shows last commit time in the status bar |
| Source control pane position | Right sidebar | Opens as a side panel |
| Diff view | On | Enable diff view for reviewing changes |
| Line author blame | Off | Enable git blame annotations inline (desktop only; separate contribution by GollyTicker) |
| Editor gutter signs | On | Shows add/modify/delete indicators in editor gutter (desktop only) |
| Exclude paths (gitignore patterns) | `.obsidian/workspace.json` | Workspace state file changes too frequently; exclude to reduce noise |

## .gitignore Recommendations

Create a `.gitignore` in your vault root:
```
# Obsidian workspace state (changes on every open)
.obsidian/workspace.json
.obsidian/workspace-mobile.json

# Cache files
.obsidian/cache

# Plugin data that shouldn't be tracked
.obsidian/plugins/obsidian-git/data.json

# OS files
.DS_Store
Thumbs.db
desktop.ini
```

## Commands Reference

| Command | Action |
|---|---|
| `Obsidian Git: Create backup` | Stage all + commit + push |
| `Obsidian Git: Pull` | Pull latest from remote |
| `Obsidian Git: Push` | Push local commits to remote |
| `Obsidian Git: Open source control view` | Opens the git panel |
| `Obsidian Git: Open diff view` | Shows changes since last commit |
| `Obsidian Git: Open history for current file` | Shows git log for active note |
| `Obsidian Git: Restore file to last commit` | Reverts the current note |
| `Obsidian Git: Commit all changes` | Bypasses staging, commits everything |
| `Obsidian Git: Commit-and-sync and close` | Syncs then closes Obsidian (desktop only) |
| `Obsidian Git: Open file on GitHub` | Opens current file in remote repo browser (desktop only) |
| `Obsidian Git: Open file history on GitHub` | Opens git history for current file in browser (desktop only) |
| `Obsidian Git: List changed files` | Shows unstaged changes |

## Gotchas & Known Issues

- **Git must be installed and on PATH** — the plugin calls the system git binary. If `git --version` fails in PowerShell, the plugin won't work. Restart Obsidian after installing git.
- **Mobile is NOT recommended** — the plugin relies on `isomorphic-git` (JavaScript reimplementation) on mobile, which the maintainer describes as "very unstable." Known issues: crashes on clone/pull, buffer overflow errors, indefinite hangs, no SSH auth, no rebase, no submodules. The maintainer has stated they don't know how to fix these. Use a separate desktop-only backup strategy for mobile.
- **Merge conflicts on sync** — if you edit the same note on two devices and both have unpushed commits, you'll get a merge conflict. Obsidian Git surfaces this but doesn't auto-resolve it. Open the conflicted file and resolve manually.
- **Large binary files slow git** — Excalidraw drawings and embedded images accumulate in history. Consider using Git LFS for image-heavy vaults, or periodically run `git gc`.
- **Authentication required for pushes** — HTTPS requires a GitHub Personal Access Token (not password). Git Credential Manager (installed with Git for Windows) handles this automatically on first push.
- **`workspace.json` in gitignore is critical** — this file changes on every Obsidian open, generating a commit every interval even if no notes changed. Exclude it.
- **Auto-backup runs on a timer, not on save** — edits aren't committed instantly. If Obsidian crashes between intervals, up to 10 minutes of changes can be lost. Lower the interval if this concerns you.
- **Plugin doesn't handle LFS automatically** — for vaults with lots of media, set up Git LFS manually (`git lfs install`) before the vault grows too large.
- **Commit nuance** — the standard `Commit` command commits nothing if nothing is staged. Use `Commit all changes` to bypass staging and commit everything. If files are staged, only those are committed.
- **Snap/Flatpak issues** — on Linux, Snap is unsupported and Flatpak is not recommended due to sandboxing restrictions. Use AppImage or a full-access package manager.

### Real-World Usage (This Vault)

This vault (Vault_Skills) was just set up with Obsidian Git's workflow:
```
git init → git add . → git commit -m "Initial commit" → gh repo create → git push -u origin main
```
The plugin is configured for 10-minute auto-backup intervals. It was used to push this vault to [github.com/Gsunny45/Vault_Skills](https://github.com/Gsunny45/Vault_Skills). The `.gitignore` excludes `.obsidian/workspace.json`, `node_modules/`, and the `nul` Windows reserved file.

## Works Well With

- [[Excalidraw]] — back up before plugin updates or major drawing sessions
- [[Copilot]] — essential backup before using Copilot Plus agent mode which writes to vault files
- [[BRAT]] — back up before installing beta plugins
- [[REST API]] — external scripts modifying your vault should be protected by regular git commits

## Related Skills

- [[Vault Architecture]] — folder structure and frontmatter design affects git diff readability
- [[Beta Testing Workflow]] — backup before testing beta plugins via BRAT
- [[Backup & Sync Strategy]] — broader backup planning: git sync + cloud sync + local redundancy

## Links

- [GitHub](https://github.com/Vinzent03/obsidian-git)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=obsidian-git)
- [Official Docs](https://publish.obsidian.md/git-doc)
