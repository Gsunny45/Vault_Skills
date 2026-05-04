---
name: vault-sync
description: >
  Sync, triage, and maintain the Claude_Vault system — the AI operational layer at
  C:\Users\MarsBase\Documents\Claude_Vault. Bridges external task sources (Linear, GitHub Issues,
  email, Slack) into the vault's native TSK-NNNN frontmatter format, triages stale tasks,
  bootstraps and enriches the memory/ directory, and resolves drift issues flagged by the
  drift-detector plugin. Use this skill whenever the user mentions: vault sync, vault maintenance,
  vault health, vault triage, stale tasks, update vault, sync tasks, refresh memory, fix drift,
  vault cleanup, "what's stale", "what needs attention", memory bootstrap, enrich memory,
  glossary update, or any reference to maintaining or updating Claude_Vault. Also trigger when the
  user asks about their tasks, open items, or vault state — this skill knows the vault's schema
  and should be preferred over generic task-management for anything touching Claude_Vault.
---

# Vault Sync

Keep Claude_Vault healthy: sync external work into it, triage what's gone stale, and fill gaps in
the memory system. This skill speaks the vault's native schema — TSK-NNNN tasks, KNW-NNNN
knowledge entries, DEC-NNNN decisions — so everything stays consistent with what the Obsidian
plugins (context-compiler, drift-detector, decision-ledger) expect.

## Vault Location

`C:\Users\MarsBase\Documents\Claude_Vault`

In the bash sandbox this maps to:
`/sessions/intelligent-great-maxwell/mnt/Claude_Vault/`

## The Three Modes

When the user invokes this skill, determine which mode(s) to run based on context. Multiple modes
can chain in a single session. If the user just says "sync the vault" or "vault maintenance", run
all three in order.

---

### Mode 1: Task Sync (external sources → TSK-NNNN)

Pull tasks from connected external tools and reconcile against existing `tasks/TSK-*.md` files.

#### Step 1: Discover available sources

Check which MCP connectors are available:

- **Linear** — search for issues assigned to the user (`list_issues` with assignee filter)
- **GitHub** — check repos for assigned issues
- **Gmail** — search for action-item emails (flagged, starred, or containing "action required")
- **Google Calendar** — pull upcoming events that imply prep work

If no external connectors are available, skip to Mode 2 and note which connectors would be useful.

#### Step 2: Fetch and compare

For each external source:
1. Fetch open/in-progress items assigned to the user
2. Read all existing `tasks/TSK-*.md` files and extract their titles + statuses
3. Fuzzy-match external items against existing tasks (match on title similarity, not exact match)

Build a diff table:

| External Item | Vault Match | Action |
|---|---|---|
| Found externally, no vault match | — | Offer to create TSK-NNNN |
| Found externally, matches existing TSK | TSK-NNNN | Skip (already tracked) |
| In vault as open, completed externally | TSK-NNNN | Offer to mark done |
| In vault as open, not found externally | TSK-NNNN | Flag as potentially stale |

#### Step 3: Create new tasks

For each item the user confirms, create a new `tasks/TSK-NNNN.md` file using the next available ID.

To find the next ID, scan existing filenames in `tasks/` for the highest number and increment:

```
Highest existing: TSK-0010 → next: TSK-0011
```

Use this exact frontmatter template:

```yaml
---
type: task
id: TSK-NNNN
title: "Title from external source"
status: open
created: YYYY-MM-DD
assigned_session:
depends_on: []
outcome: ""
source: "linear/ISSUE-123"  # or "github/repo#45", "gmail/thread-id"
---
```

Body structure:

```markdown
## Objective

[Description from external source]

## Acceptance Criteria

- [ ] [Extracted from external item, or ask user]

## Progress

- Synced from [source] on [date]
```

#### Step 4: Mark completed tasks

For tasks confirmed as done, update their frontmatter:
- Set `status: done`
- Add `completed: YYYY-MM-DD`
- Add `outcome:` with a brief summary

---

### Mode 2: Stale Task Triage

Review every open/in_progress/blocked task and surface what needs attention.

#### Step 1: Read all tasks

Read every file in `tasks/` and parse frontmatter. Build a list of non-done tasks.

#### Step 2: Flag issues

For each task, check:

- **Age**: Created more than 30 days ago and still open? Flag it.
- **Blocked without progress**: Status is `blocked` but no recent session references it? Flag it.
- **Missing context**: No `depends_on`, no `assigned_session`, vague title? Flag it.
- **Stale retargets**: Has a `retargeted` field but hasn't been worked since? Flag it.
- **Overdue**: Has a `due` field in the past? Flag it.

#### Step 3: Present triage menu

For each flagged task, present options:
- **Keep open** — still relevant, no change needed
- **Update** — rewrite title/objective to reflect current reality
- **Move to done/cancelled** — no longer relevant
- **Add context** — flesh out acceptance criteria, add dependencies

Apply changes the user confirms. Always update frontmatter fields when touching a task.

---

### Mode 3: Memory Enrichment

Fill gaps in the `memory/` directory and keep it current.

#### Step 1: Audit current memory

Read all files under `memory/`:
- `memory/glossary.md` — terms, acronyms, services
- `memory/context/` — API budgets, registries, etc.
- `memory/projects/` — project details
- `memory/people/` — (likely empty, needs bootstrapping)

Note what exists vs. what's thin or missing.

#### Step 2: Extract entities from vault content

Scan recent sessions, tasks, decisions, and knowledge entries for:
- **People** mentioned by name (full names, nicknames, handles)
- **Projects** referenced by codename
- **Terms/acronyms** used without definition
- **Services/tools** mentioned

Cross-reference against `memory/glossary.md`. Track what's already defined vs. unknown.

#### Step 3: Interactive decode

For unknown entities, ask the user:

```
I found references in your vault that aren't in memory yet:

1. "Hostinger" (from TSK-0007) — hosting provider? What's the account status?
2. "OpenClaw" (from TSK-0007) — what is this project?
3. "Mars" — this is you, right? Any details for the profile?

Which of these should I add to memory?
```

#### Step 4: Write memory files

**For people** — create/update `memory/people/[name].md`:
```markdown
# [Full Name]
- Role: [role]
- Contact: [preferred channel]
- Context: [how they relate to the vault/projects]
```

**For projects** — create/update `memory/projects/[project].md`:
```markdown
# [Project Name]
- Status: [active/paused/completed]
- Goal: [one-liner]
- Key links: [repo, docs, board]
- Related tasks: [[TSK-NNNN]]
```

**For terms** — append to `memory/glossary.md` in the appropriate table.

**For context updates** — update `memory/context/api-budgets.md` if any service statuses have
changed (expired trials, depleted credits, new keys).

#### Step 5: Staleness check on existing memory

For entries already in memory, check if they're still accurate:
- API budgets: any trials expired? Credits depleted? (Pinecone $300 credit was expiring ~May 4)
- Project statuses: any projects completed or abandoned since last update?
- People: anyone's role changed?

Flag stale entries and offer updates.

---

## Drift Resolution (Bonus Mode)

If the user mentions "drift" or "fix drift", or if Mode 2 reveals widespread issues, also address
items from `_system/_drift_report.md`:

#### Schema violations
Read the drift report. For each "missing required field" violation:
- Read the offending file
- Add the missing frontmatter fields with sensible defaults
- Ask the user to confirm values you're unsure about

#### Stale references
For each stale reference (source verified before target was modified):
- Read the source file
- Update its `last_verified` field to today if the content is still accurate
- If the content has drifted, flag it for the user

#### Orphan notes
For notes with no inbound links:
- Assess whether they should be linked from somewhere (a related task, knowledge entry, or session)
- Offer to add links or archive the orphan

---

## Post-Sync Report

After running any combination of modes, produce a summary:

```
## Vault Sync Complete — [date]

### Tasks
- Synced: +N new from [sources]
- Triaged: N tasks reviewed, M updated, K closed
- Still open: N tasks

### Memory
- Added: N new entries (X people, Y terms, Z projects)
- Updated: N stale entries refreshed
- Gaps remaining: [list any unresolved unknowns]

### Drift
- Fixed: N schema violations, M stale references
- Remaining: [any issues that need user input]
```

---

## Important Conventions

- **Never delete files** without explicit user confirmation.
- **Always use the vault's ID scheme**: TSK-NNNN, KNW-NNNN, DEC-NNNN (4-digit zero-padded).
- **Always include proper frontmatter** matching `_system/_schemas.yaml`.
- **Update `last_verified` or `created` dates** on every file you touch.
- **Estimate tokens**: set the `tokens` frontmatter field (content length / 4) on notes you create.
- **Respect vault boundaries**: if something belongs in Command_Vault, Local-Network-Hub, or
  RAG_Vault, say so rather than putting it in Claude_Vault.
