---
type: plugin
name: Minimal Theme Settings
category: Writing & Editing
status: active
complexity: low
downloads: 1.5M+
last-verified: 2026-04-30
tags:
  - plugin
  - writing
  - themes
  - minimal-theme
  - customization
---

# Minimal Theme Settings

> Plugin by kepano — a dedicated settings panel for the Minimal theme. Provides hotkeys, presets, and Minimal-specific toggles that go beyond what Style Settings exposes. Requires the Minimal theme to be active.

## What It Does

Minimal Theme Settings is a companion plugin specifically for the Minimal Obsidian theme (also by kepano). It provides:
- **One-click color scheme switching** via hotkeys
- **Image width controls** (widen/narrow images with hotkeys)
- **Preset system** for quickly switching between reading, writing, and focused modes
- **Additional toggles** not available in Style Settings

This plugin and Style Settings are complementary — both are useful if you run Minimal. Style Settings handles granular CSS variable controls; Minimal Theme Settings handles Minimal-specific shortcuts and presets.

## When To Use It

- You use the Minimal theme (the most popular Obsidian theme)
- You want keyboard shortcuts to switch between light/dark schemes or presets
- You work in multiple contexts (reading, coding, writing) with different visual preferences
- You want fine control over image display width without touching CSS

## Minimal Setup

1. **Install Minimal theme**: Settings → Appearance → Themes → search "Minimal" → Install and Use
2. **Install this plugin**: Community Plugins → search "Minimal Theme Settings" → Install & Enable
3. Settings → Minimal Theme Settings → configure your preferred defaults
4. Assign hotkeys to color scheme switching (optional but useful)

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Color scheme | Default (auto dark/light) | Follows Obsidian's light/dark mode setting |
| Active color scheme (light) | Default or Nord | Choose what you find easy on the eyes |
| Active color scheme (dark) | Default or Everforest | |
| Preset | Default | Other presets: "Cards", "Atom", "Minimal", etc. |
| Readable line width | On | Recommended — limits reading width to ~80 characters |
| Image width | 100% | Override per-note with YAML if needed |
| Text font | iA Writer Quattro or system-ui | Choose your preferred reading font |
| Monospace font | Fira Code or Cascadia Code | For code blocks |

## Hotkeys

After installing, assign these in Settings → Hotkeys:

| Action | Suggested Hotkey |
|---|---|
| Cycle color schemes | `Ctrl+Shift+C` |
| Toggle light/dark mode | (use Obsidian's built-in) |
| Increase image width | `Ctrl+Shift+=` |
| Decrease image width | `Ctrl+Shift+-` |
| Reset image width | `Ctrl+Shift+0` |

## Color Schemes Available

Minimal includes many built-in color schemes selectable via this plugin:
Default · Atom · Ayu · Catppuccin · Dracula · Everforest · Flexoki · Gruvbox · Monokai · Night Owl · Nord · Notion · Rosé Pine · Solarized · Things

## Gotchas & Known Issues

- **Only works with the Minimal theme** — settings have no effect with any other theme active.
- **Works alongside Style Settings** — both can be active simultaneously. Style Settings handles fine-grained CSS variables; this plugin handles presets and hotkeys.
- **Color scheme is separate from Obsidian's light/dark toggle** — switching to dark mode in Obsidian doesn't switch your Minimal color scheme; they're independent.

## Works Well With

- [[Style Settings]] — use both together for full Minimal customization
- [[Editing Toolbar]] — Minimal + Editing Toolbar is a clean writing setup

## Related Skills

- [[Vault Architecture]]

## Links

- [GitHub](https://github.com/kepano/obsidian-minimal-settings)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=obsidian-minimal-settings)
- [Minimal Theme](https://minimal.guide/)
