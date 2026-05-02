---
type: plugin
name: Style Settings
category: Writing & Editing
status: active
complexity: low
downloads: 2.2M+
last-verified: 2026-04-30
tags:
  - plugin
  - writing
  - themes
  - customization
  - css
---

# Style Settings

> Plugin by mgmeyers — exposes GUI settings for themes and plugins that use CSS custom properties. Lets you tweak colors, fonts, spacing, and layout of your Obsidian theme without touching CSS directly.

## What It Does

Style Settings is a settings panel that reads specially formatted CSS comment blocks from themes and plugins, then generates a visual settings UI from them. Instead of editing raw CSS variables, you get sliders, color pickers, toggles, and dropdowns.

It only provides controls for themes/plugins that explicitly support it — a theme must include `/* @settings */` comment blocks with configuration metadata. Most major Obsidian themes (Minimal, AnuPpuccin, Things, Blue Topaz, etc.) support Style Settings.

This plugin doesn't do anything on its own — it's a UI layer for theme authors to expose customization options.

## When To Use It

- You use a theme that supports Style Settings (most popular themes do)
- You want to customize colors, fonts, or layout without editing CSS files
- Trying different accent colors, heading sizes, or sidebar widths
- Toggling theme-specific features (e.g., Minimal's "Colorful headings", readable line width, focus mode)
- Building a consistent visual environment across multiple Obsidian instances

## Minimal Setup

1. **Install**: Community Plugins → search "Style Settings" by mgmeyers → Install & Enable
2. **Install a compatible theme**: Settings → Appearance → Themes → browse and install (Minimal is recommended)
3. **Open Style Settings**: Settings → Style Settings — the panel shows all available options for your active theme
4. Adjust to taste — changes apply live

If Style Settings shows "No settings found", your current theme doesn't support it. Switch to a theme like Minimal or AnuPpuccin.

## Key Settings

There are no plugin-level settings — the entire plugin is the settings panel it generates from themes.

**What you'll typically find for a supported theme:**

| Category | Example Options |
|---|---|
| Colors | Accent color, background color, heading colors, link color |
| Typography | Base font, monospace font, heading sizes (H1-H6), line height |
| Layout | Readable line width on/off, max line width (px), sidebar width |
| Features | Colorful headings, image grid, focus mode, table alternating rows |
| Mobile | Separate mobile font sizes, touch target sizes |

## Example: Minimal Theme Settings

With the Minimal theme + Style Settings installed, you can configure:
- **Color scheme**: Default, Atom, Ayu, Catppuccin, Dracula, Everforest, Gruvbox, Nord, Rosé Pine, Solarized
- **Active line highlight**: On/Off
- **Readable line width**: On (recommended — limits line length to ~80ch for readability)
- **Image grid**: Auto-formats multiple embedded images into a grid
- **Colorful headings**: Each heading level gets a distinct color

## Gotchas & Known Issues

- **Requires a compatible theme** — the plugin does nothing if your theme has no `/* @settings */` block.
- **Settings reset on theme change** — switching to a different theme clears your Style Settings for the old theme (the new theme's settings load instead). Settings are stored per-theme.
- **Some settings require Obsidian restart** — font changes in particular may need a restart to take full effect.
- **Minimal Theme Settings plugin is separate** — if you use the Minimal theme, there's also a dedicated "Minimal Theme Settings" plugin that works alongside Style Settings with Minimal-specific shortcuts.
- **CSS snippets override Style Settings** — if you have a CSS snippet that sets a variable Style Settings also controls, the snippet wins (CSS specificity).

## Works Well With

- [[Minimal Theme Settings]] — Minimal-specific companion plugin with theme presets and shortcuts
- [[Editing Toolbar]] — visual editing tools that look better with a well-configured theme
- Any major Obsidian theme: Minimal, AnuPpuccin, Things, Blue Topaz, ITS Theme

## Related Skills

- [[Vault Architecture]]

## Links

- [GitHub](https://github.com/mgmeyers/obsidian-style-settings)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=obsidian-style-settings)
