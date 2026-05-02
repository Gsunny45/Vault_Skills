---
type: skill
name: Canvas Visual Mapping
category: Visual & Diagrams
difficulty: intermediate
tags:
  - skill
  - canvas
  - visual-thinking
  - diagrams
  - mind-mapping
---

# Canvas Visual Mapping

## What This Skill Covers
How to use Obsidian Canvas (with or without Advanced Canvas) for visual thinking — mind maps, flowcharts, system diagrams, presentations, and vault navigation maps. You'll learn when to reach for Canvas vs. Excalidraw vs. plain notes.

## When You Need This
- You're designing a system or process and need to see relationships spatially
- You want to build a visual vault homepage or navigation map
- You need to present ideas from your notes as a slideshow without leaving Obsidian
- You're planning a vault architecture and want to map folder/note relationships before building
- You have a complex idea with branching logic that's hard to express linearly

## Core Concepts

### Canvas vs. Excalidraw vs. Plain Notes

| Tool | Best For | Avoid When |
|---|---|---|
| **Canvas** | Structured diagrams, flowcharts, presentations, vault navigation | Freehand drawing, rough sketches, artistic diagrams |
| **Excalidraw** | Hand-drawn style sketches, wireframes, whiteboard sessions, visual notes | Structured/organizational diagrams with connectors |
| **Plain Notes** | Deep content, long-form writing, searchable text | Any situation where spatial relationships matter |

### Canvas as a Layer on Top of Your Vault
Canvas doesn't replace notes — it *surfaces* them. A canvas typically contains:
- **File nodes** (links to existing notes) — the canvas is a viewport into your vault
- **Text nodes** — annotations, questions, temporary ideas
- **Edges** (arrows/lines) — relationships between notes

This means a canvas is disposable. You can delete a canvas without losing any note content.

## Canvas Creation Workflow (Systematic)

A repeatable process for building vault maps. Follow these steps in order.

### Step 1 — Survey the Vault
Before placing a single node, understand what you're mapping:
1. **Read the vault's CLAUDE.md or README** — identifies domains, structure, relationships
2. **List all folders** — each folder = a potential group or abstraction
3. **Identify MOC/hub notes** — these are the abstraction layer; you map MOCs, not individual notes
4. **Count notes per domain** — determines the abstraction level needed (see decision tree below)
5. **Map stated relationships from the source** — e.g., vault README may say "A ↔ B → C"

### Step 2 — Choose Canvas Type & Layout Pattern

| Canvas Type | Use Case |
|---|---|
| **Mind Map** | Central idea in the middle, branch out with related notes |
| **Flowchart / Pipeline** | Linear or branching process with decisions |
| **Vault Map** | Key notes arranged spatially as a navigable homepage |
| **Presentation Deck** | Nodes connected by arrows in slide order |
| **System Diagram** | Architecture diagram showing components and connections |

### Step 3 — Choose Abstraction Level

| Vault Size | Approach | Example |
|---|---|---|
| < 10 notes | Direct file nodes for everything | A small project with 8 notes |
| 10–50 notes | MOC/hub nodes as abstraction | 5 MOC nodes representing 5 domain clusters |
| 50+ notes | MOC hubs + portals to sub-canvases | Domain thumbnails linking into sub-maps |
| Mixed sizes | MOC hubs for dense areas, direct nodes for sparse ones | 3 domain MOCs + 4 standalone notes |

**Rule**: If a canvas would have 15+ file nodes, step up one abstraction level. Canvases are for relationships, not exhaustive listings.

### Step 4 — Design the Grid (Coordinate Planning)

Standard spacing for readable canvases (1200–1400px wide):

| Element | Size | Spacing |
|---|---|---|
| Title text node | 400×50 | Center top, y=20 |
| Section label text node | 200×28 | 10px above its group |
| MOC/file node | 200×80 | 240px horizontal gap between columns |
| Dashboard/ops file node | 170×60 | 20px horizontal gap |
| Ecosystem text node | 400×65 | Centered in its row |
| Task/note file node | 260×55 | Standard size for action items |
| Row height | — | 130–150px between row centers |

**Coordinate formula for a pipeline layout with N nodes:**
```
x_n = margin + (n * column_width)     // margin=50, column_width=240
y_row = 100 + (row_index * 130)       // row 0=100, row 1=260, row 2=370, row 3=480
width = 200 (file) or 28 (text label) // label sits above its file node
```

### Step 5 — Build the Structure
1. Create a new `.canvas` file (CMD/Ctrl+N → Canvas) or write the JSON directly for programmatic creation
2. **Place title first** — center at top, sets the canvas scope
3. **Place section labels** — small text nodes above each group
4. **Place file nodes** — MOCs, dashboards, tasks
5. **Add text nodes** — for system descriptions, annotations, ecosystem vaults
6. **Connect edges** — wire up the relationships you mapped in Step 1

### Step 6 — Apply Visual Hierarchy

| Technique | How | Best For |
|---|---|---|
| **Color-coded nodes** | Set `"color": "1"` through `"6"` in the node JSON | Domain differentiation (match Graph View colors) |
| **Color-coded edges** | Set `"color"` on edge objects | Highlighting cross-domain or non-obvious connections |
| **Labeled edges** | Set `"label"` on edge objects | Explaining *what kind* of relationship |
| **Text labels above groups** | Small text node above a file node row | Section headers without group borders |
| **Spacing clusters** | Group related nodes with 20px gaps, unrelated with 80px+ gaps | Spatial proximity implies relationship |

**Color convention (from vault_config.yaml-style domain mapping):**
```
1 = blue/purple    → Prompt Engineering
2 = teal/cyan      → Context Engineering
3 = orange         → DevOps
4 = green          → GitHub / active tasks
5 = red            → Build
6 = gray           → System / infrastructure
```

### Step 7 — Edge Routing Convention

Edges are the thinking. Route them consistently:

| Connection Type | From Side | To Side | When to Use |
|---|---|---|---|
| **Forward flow** | right | left | Left-to-right pipeline (domains, stages, timeline) |
| **Cross-connection** | top | top | Non-adjacent nodes with a relationship (use distinct edge color) |
| **Hierarchical** | bottom | top | Parent→child, container→contained, operational layer |
| **Ecosystem link** | right | left | External vaults or services |
| **Action link** | bottom | top | Task → its context or parent |

**Edge label style**: Short phrases, noun-verb format: `"triggers automation"`, `"produces artifacts"`, `"deploy at scale"`. Avoid full sentences.

### Step 8 — Validate

Before calling it done:
- [ ] Every file node references an existing file (check paths)
- [ ] Every edge connects two real nodes (check IDs match)
- [ ] The canvas fits its intended viewport (max ~1400px wide for standard monitors)
- [ ] Color usage is consistent (same color = same semantic meaning)
- [ ] The canvas has at least one incoming link from a vault note

### Step 9 — Make It Navigable
- Link from a note to a canvas: `[[My Canvas.canvas|Canvas Name]]`
- Link to a specific node: `[[My Canvas.canvas#node-id]]` (copy from right-click menu in Advanced Canvas)
- Use a canvas as your [[Homepage]] for vault-level navigation
- Add a **Vault Navigation** section to `Dashboard.md` with a direct link
- **For AI-operated vaults**: mention the canvas in CLAUDE.md so agents know it exists

## Layout Pattern Library

Reusable blueprints for common vault structures.

### Pipeline (Left-to-Right Flow)
Best for: processes, domain chains, stage-based workflows

```
[TITLE]
  │
[Step 1 label]  [Step 2 label]  [Step 3 label]  [Step 4 label]
[  Node A   ] → [  Node B   ] → [  Node C   ] → [  Node D   ]
                                        │
                              [   Cross-connection   ]
                                        │
                              [  Stakeholder Node   ]

Grid specs: margin=50, column_width=240, row_height=130
Edge style: right→left with labels
```

### Hub-and-Spoke (Radial)
Best for: central dashboard, topic with subtopics, reference hubs

```
          [Spoke 1]          ── possible only with
              │                Advanced Canvas or
     [Spoke 2]─[HUB]─[Spoke 3]  careful native layout
              │
          [Spoke 4]

Grid specs: hub at center (500,200), spokes at 200px radius
Native Canvas limitation: true radial requires manual angle math
Alternative: use a vertical hierarchical layout instead
```

### Layered (Top-to-Bottom)
Best for: system architecture, stack diagrams, organizational charts

```
[Title / System Name]
       │
┌──────────────────────────────┐
│  Layer 1: User/Interface      │
│  [Note A]  [Note B]          │
├──────────────────────────────┤
│  Layer 2: Processing          │
│  [Note C] → [Note D]         │
├──────────────────────────────┤
│  Layer 3: Storage             │
│  [Note E]                     │
└──────────────────────────────┘

Grid specs: layer_width=600, layer_height=100, vertical_gap=40
Use horizontal text nodes as layer boundaries
```

### Mixed (Most Common for Real Vaults)
Best for: real-world vaults with multiple concerns

```
[TITLE]                           ← center top
                                   │
[PE] → [CE] → [DevOps] → [GitHub] → [Build]   ← pipeline row
                    │
[Dashboard] [TaskBoard] [Health] [_system_]    ← ops row
                    │
[Ecosystem Vault A] ── [Ecosystem Vault B]    ← ecosystem row
                    │
[Open Task 1] [Open Task 2]                   ← action row

This is the pattern used for the Prompt & Context Engineering vault map.
Each row is a different concern, connected by sparse edges between layers.
```

## Variations / Approaches

| Approach | Complexity | Best For |
|---|---|---|
| Pure native Canvas | Beginner | Simple mind maps, quick idea capture |
| Canvas + Advanced Canvas | Intermediate | Flowcharts, presentations, system diagrams |
| Canvas + Advanced Canvas + CSS styling | Advanced | Branded presentations, styled node states |
| Canvas as Homepage | Intermediate | Vault-level visual navigation |

## Example: Vault Navigation Map

Create a canvas that serves as a visual landing page for your vault:

```
                    ┌──────────────────────┐
                    │     VAULT HUB         │ (Text node — title)
                    └──────────┬───────────┘
                               │
            ┌──────────────────┼──────────────────┐
            ▼                  ▼                  ▼
    ┌───────────────┐  ┌───────────────┐  ┌───────────────┐
    │  Daily Notes   │  │   Projects    │  │   Reference   │
    │  (file node)   │  │  (file node)  │  │  (file node)  │
    └───────────────┘  └───────────────┘  └───────────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
            ┌───────────────┐    ┌───────────────┐
            │  Active Sprint │    │    Backlog    │
            │  (file node)   │    │  (file node)  │
            └───────────────┘    └───────────────┘
```

## Canvas JSON Reference

Canvas files are plain JSON (`.canvas` extension). You can write them directly — useful for AI agents, scripts, or template-based creation.

### Node Entry Template
```json
{
  "id": "unique-node-id",
  "type": "text" | "file" | "group",
  "x": 50,
  "y": 100,
  "width": 200,
  "height": 80,
  "text": "Display text here",     // for text/group nodes
  "file": "path/to/note.md",      // for file nodes (relative to vault root)
  "color": "1"                    // optional: "1" through "6" (also "3" is the default)
}
```

### Edge Entry Template
```json
{
  "id": "e-unique-id",
  "fromNode": "source-node-id",
  "fromSide": "right" | "left" | "top" | "bottom",
  "toNode": "target-node-id",
  "toSide": "right" | "left" | "top" | "bottom",
  "label": "relationship label",   // optional — keep under 30 chars
  "color": "1"                     // optional — use for cross-connections
}
```

### Color Reference
| Value | Color | Use For |
|---|---|---|
| `"1"` | Red (warm) | Critical path, domain 1 |
| `"2"` | Orange | Domain 2, secondary flow |
| `"3"` | Yellow (default) | Standard connections |
| `"4"` | Green | Success, completed, domain 4 |
| `"5"` | Cyan | Domain 5, system |
| `"6"` | Purple/violet | Ecosystem, external |

### File Existence Checklist (for scripted creation)
Before writing a canvas file, validate all file paths:
```
vault_root/
├── knowledge/MOC-prompt-engineering.md   ← exists
├── Dashboard.md                           ← exists
└── tasks/TSK-9999.md                      ← DOES NOT EXIST — skip or flag
```

## From Practice: Building a Real Vault Map

Built: **Prompt & Context Engineering vault** — 71 knowledge entries, 5 domains, 3-vault ecosystem.

### What Went Well

| Practice | Why |
|---|---|
| Read CLAUDE.md first | Revealed the domain flow: `PE ↔ CE ↔ DevOps → GitHub → Build` which became the core edge pattern |
| Used MOC hubs as abstraction | 5 MOC nodes represented 71 KNW entries — the canvas stayed readable |
| Color-coded to match Graph View | Domain colors from `vault_config.yaml` mapped directly to canvas color slots 1–5 |
| Created a discovery path | Added a "Vault Navigation" callout in `Dashboard.md` so the canvas is findable |
| Validated file references | Caught one path typo before the canvas was done |

### What I'd Do Differently

| Problem | Fix for Next Time |
|---|---|
| **Manual coordinate math** — calculated every x,y by hand for 21 nodes | Use the coordinate formula from Step 4. For AI agents: emit JSON directly with the formula. |
| **No coordinate template** — started from blank canvas with no reference frame | Keep the coordinate table (Step 4) open as a reference while building. Pre-calculate the grid. |
| **Edge side guessing** — chose edge sides by intuition, then had to adjust | Apply the edge routing convention (Step 7) before placing edges. Forward flow = right→left, always. |
| **Canvas size guessing** — estimated 1400px but nodes only spanned 1250px | Calculate `total_width = margin + (n_nodes * column_width) + margin` before placing. |
| **No canvas maintenance plan** — no process for keeping it fresh when the vault grows | Add a "Last Reviewed" date in the canvas title. Check against MOC hub last_updated dates. |
| **No automation** — hand-crafted every node and edge | Next time: script the canvas JSON from vault data (MOC listings, task statuses, folder structure). |

### Key Insight
*"A canvas is a **view**, not a store."* The Prompt & Context Engineering map doesn't contain any content — every single node is a link to an existing note or a transient label. If the canvas were deleted, zero information would be lost. This is the defining property of good canvas usage.

## Maintenance & Freshness

Canvases go stale. Set a refresh cadence:

| Canvas Type | Refresh Trigger | Action |
|---|---|---|
| Vault Architecture Map | New domain added or MOC reorganized | Re-layout: add/remove domain nodes, rewire edges |
| Task Pipeline | Task status changes | Update task file nodes: add new, gray out completed |
| System Diagram | Infrastructure changes | Update ecosystem/component text nodes |
| Presentation Deck | Content drift | Re-verify each slide node still says what you need |
| Quick mind map | Session ends | Archive or delete — these are disposable |

**Freshness check**: Before a session that references a canvas:
1. Read the canvas JSON (it's plain text)
2. Spot-check 3–5 file node paths — do they still exist?
3. Check edge labels — are the relationships still accurate?
4. Update the canvas title date if refreshed

## Automation Ideas

Canvases are JSON. This makes them scriptable.

### Auto-generate from MOC files
```python
# Pseudocode — read all MOC files, generate a vault map canvas
mocs = find_all_files("knowledge/MOC-*.md")
nodes = []
for i, moc in enumerate(mocs):
    nodes.append({
        "id": f"moc-{i}",
        "type": "file",
        "x": 50 + i * 240,
        "y": 130,
        "width": 200,
        "height": 80,
        "file": moc.path
    })
write_canvas("Vault Architecture Map.canvas", nodes, edges)
```

### Dataview-assisted node discovery
````dataviewjs
// Find all MOC notes to determine what should be on the map
const mocs = dv.pages('"knowledge"').where(p => p.type === "moc");
dv.table(["MOC", "Domain", "Spokes"], mocs.map(m => [
  m.file.link, m.domain, m.spokes_populated || "?"
]));
````

### Integration with vault monitoring
If your vault has drift detection (like the Prompt & Context Engineering vault does):
- Add a drift rule that checks if file nodes on the canvas still exist
- Flag the canvas as stale when MOC hubs are updated but the canvas isn't

## Common Mistakes

- **Putting content IN canvas instead of linking to notes**: Canvas nodes aren't full notes. Write content in markdown files, link to them from canvas. Your canvas is a view, not storage.
- **Overcrowding**: If a canvas would have 15+ file nodes, step up one abstraction level (MOC hubs or sub-canvases).
- **Forgetting edges have meaning**: A canvas full of unconnected nodes is just a grid of icons. The arrows and lines ARE the thinking.
- **Treating canvas as permanent**: Canvases are cheap. Delete them when the thinking is done and the real notes are linked.
- **Skipping the validation step**: A file node referencing a deleted path renders as a broken link. Validate before publishing.
- **No discovery path**: A canvas that isn't linked from any note is invisible. Always add a link from Dashboard.md, README, or a relevant MOC.
- **Using Advanced Canvas features without testing the viewport**: Complex shapes and CSS may look different on mobile or with different themes.

## Related Skills
- [[Vault Architecture]] — using canvas to design vault structure before building
- [[Dashboards]] — combining canvas with Dataview for live-updating visual dashboards
- [[REST API Automation]] — generating canvas JSON from external scripts via REST API

## Related Plugins
- [[Advanced Canvas]]
- [[Excalidraw]]
- [[Homepage]]
- [[Dataview]] — query vault data to decide what goes on the canvas
