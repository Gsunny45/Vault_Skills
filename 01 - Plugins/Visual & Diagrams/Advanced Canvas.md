---
type: plugin
name: Advanced Canvas
category: Visual & Diagrams
status: active
complexity: medium
downloads: 493k+
last-verified: 2026-04-29
tags:
  - plugin
  - canvas
  - diagrams
  - visual
  - presentations
---

# Advanced Canvas

## What It Does
Supercharges Obsidian's native Canvas with flowchart shapes, customizable edges, presentation mode, collapsible groups, portals (nested canvases), and CSS-driven node styling. Turns Canvas from a basic whiteboard into a full diagramming and presentation tool — while keeping full compatibility with Obsidian's graph view and backlinks.

## When To Use It
- Building flowcharts, decision trees, and process diagrams inline in your vault
- Creating slide decks for presentations directly from canvas nodes
- Designing system architecture or mind maps with professional-looking connectors
- Embedding canvases inside other canvases (portals) for modular visual thinking
- Adding visual style metadata to nodes via CSS (e.g., color-coded approval states)
- Replacing external tools like draw.io, Miro, or PowerPoint for Obsidian-native visual work

## Minimal Setup
1. **Install**: Community Plugins → Advanced Canvas → Install & Enable
2. **Open a canvas**: Create a new `.canvas` file or open an existing one
3. **Explore the new context menus**: Right-click any node or edge to see Advanced Canvas options (shapes, borders, colors, arrows)
4. **Customize settings**: Settings → Advanced Canvas — disable any features you don't need

## Key Settings

| Setting Group | Key Options | Notes |
|---|---|---|
| General | Double-click behavior (text vs file node), grid alignment, default node sizes | Set double-click to your most common action |
| Node Defaults | Default alignment, border style, rounded vs square corners | Saves time if you use consistent styling |
| Readonly Mode | Disable popups, lock position, lock zoom | Useful for shared/presented canvases |
| Export | PNG/SVG transparency, privacy mode, show logo | Privacy mode hides filenames in exports |
| Presentation | Arrow key navigation, remote compatibility | Works with presentation clickers |

## Features Reference

### Node Shapes (8 Types)
| Shape | Looks Like | Best For |
|---|---|---|
| Terminal | Rounded rectangle | Start/end points |
| Process | Rectangle | Standard action step |
| Decision | Diamond | Yes/no branches |
| Input/Output | Parallelogram | Data I/O |
| On-page Reference | Circle with connector | Cross-reference |
| Predefined Process | Rectangle with side bars | Sub-process / subroutine |
| Document | Rectangle with wavy bottom | Document or file reference |
| Database | Cylinder | Data storage |

### Edge Customization
- **Path styles**: Solid, Dotted, Short-dashed, Long-dashed
- **Arrow styles**: Triangle, Triangle Outline, Halved Triangle, Thin Triangle, Diamond, Diamond Outline, Circle, Circle Outline, Blunted
- **Pathfinding**: Default, Straight, Squared, A* (A-star pathfinding for clean auto-routing)
- **Floating edges**: Auto-adjust to the most suitable connection side
- **Flip edge**: Reverse direction with one click

### Presentation Mode
1. Connect nodes with arrows to define slide order
2. Right-click → Start Presentation (or assign a hotkey)
3. Navigate: Arrow keys / PageUp / PageDown / presentation remotes
4. Press `Escape` to exit

### Portals
Embed one canvas inside another. Create edges to/from the portal as if it were a regular node. Great for:
- Breaking complex diagrams into modular sub-canvases
- Reusing a diagram in multiple parent canvases
- Keeping canvas file sizes manageable

### Collapsible Groups
- Group nodes → collapse minimizes the group to a single box
- Expand/collapse via context menu or hotkey
- Keeps large canvases navigable

### Focus Mode
Select a node → Focus Mode blurs all other nodes. Helps audiences focus on one element during presentations or detailed work.

### Encapsulate Selection
Select nodes → right-click → Encapsulate Selection. Moves selected nodes to a new canvas file and replaces them with a portal link. Keeps your main canvas clean.

## Example Config: Presentation Deck

```
(create a canvas and connect nodes with arrows)

[Slide 1: Title] ──→ [Slide 2: Problem] ──→ [Slide 3: Solution]
                                                      │
                                                      ▼
                                              [Slide 4: Demo]
                                                      │
                                                      ▼
                                              [Slide 5: Q&A]
```

Assign a hotkey to "Advanced Canvas: Start Presentation" and you have a PowerPoint replacement inside Obsidian.

## CSS Custom Node Styles

Create a CSS snippet to add custom style attributes to nodes:

```css
/* Adds a dropdown in node context menu */
/* @advanced-canvas-node-style
key: priority
label: Priority
options:
  - label: None    value: null     icon: circle-off
  - label: Low     value: low      icon: circle-1
  - label: Medium  value: medium   icon: circle-2
  - label: High    value: high     icon: circle-3
  - label: Urgent  value: urgent   icon: circle-4
*/

.canvas-node[data-priority="high"] .canvas-node-content {
  border-color: #e74c3c;
  border-width: 3px;
}

.canvas-node[data-priority="urgent"] .canvas-node-content {
  border-color: #c0392b;
  border-width: 4px;
  animation: pulse-border 2s infinite;
}
```

## Gotchas & Known Issues

- **Performance on large canvases**: Canvases with 100+ nodes may lag, especially with A* pathfinding enabled on many edges. Disable A* or simplify the canvas.
- **Not all themes style Advanced Canvas nodes**: Some themes only style native Canvas. You may need CSS snippets for consistent appearance.
- **Presentation mode requires arrow-connected nodes**: If nodes aren't linked by arrows, they won't appear in the slide sequence.
- **Portal canvases open separately**: Clicking a portal opens the embedded canvas in a new tab — it doesn't render inline.
- **No mobile presentation mode**: Presentation mode works on desktop only (as of 2025).
- **Canvas files are JSON**: `.canvas` files are plain JSON under the hood. You can edit them with external tools, but manual edits risk breaking the format.
- **Changes require canvas refresh**: Some CSS node styles need the canvas to be closed and reopened to appear.

## Works Well With
- [[Excalidraw]] — Advanced Canvas for structured diagrams, Excalidraw for hand-drawn/freeform sketches
- [[Dataview]] — Dataview queries in canvas file nodes to show dynamic content
- [[Homepage]] — Use a canvas as your vault homepage for visual navigation

## Related Skills
- [[Vault Architecture]] — designing vault layouts that use canvas for visual navigation
- [[Canvas Visual Mapping]] — techniques for visual thinking with Advanced Canvas

## Links
- [GitHub](https://github.com/Developer-Mike/obsidian-advanced-canvas)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=advanced-canvas)
