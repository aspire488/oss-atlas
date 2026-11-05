# Visual identity

<sub>OSS ATLAS / DESIGN SYSTEM</sub>

## Direction

**Editorial field journal for engineering evidence.** The repository should feel like a carefully typeset research publication: restrained, confident, legible, and deliberately structured. Avoid generic dashboard chrome, gradients, cyberpunk motifs, emoji-heavy headings, and badge walls.

## Tokens

| Role | Token | Value |
|:--|:--|:--|
| Paper | Background | `#F7F4EE` |
| Ink | Primary text | `#171715` |
| Vermilion | Accent | `#F04424` |
| Stone | Secondary text | `#716D64` |
| Rule | Borders/grid | `#D8D0C3` |
| Blue | Active / in-review | `#386B83` |
| Green | Accepted / merged | `#36745B` |
| Amber | Closed / historical | `#B36A2F` |

## Typography

- Display: bold grotesk sans-serif, tight tracking, large scale.
- Editorial copy: system sans-serif for predictable GitHub rendering.
- Technical material: monospace.
- Use whitespace and thin rules to create hierarchy; avoid ornamental cards unless they encode real structure.

## Information hierarchy

1. Identity and purpose
2. Current, dated ledger snapshot
3. Selected upstream outcomes
4. Curated navigation
5. Evidence model and operating rules

## GitHub rendering constraints

- Use self-contained SVG assets with explicit dimensions and accessible labels.
- Keep the README useful when images fail to load.
- Avoid external image hosts for core identity assets.
- Do not rely on CSS, JavaScript, or unsupported HTML.
- Dashboard graphics must be generated from canonical metadata, not manually edited snapshots.

## Maintenance

The README and library landing pages share the same editorial vocabulary. The dashboard generator is the source for generated chart colors; change its palette rather than hand-editing generated SVGs.
