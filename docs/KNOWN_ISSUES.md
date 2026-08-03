# KNOWN_ISSUES.md

# Known Issues

This document tracks known issues that remain after each milestone.

Unlike the CHANGELOG, this file is forward-looking. Every item listed here has been observed during testing and is waiting for a future milestone.

---

# Current Status

**Current Milestone:** 3

Overall status:

- ✅ Dashboard design established
- ✅ White Material Design components removed
- ✅ Bellezza Vela design language implemented
- 🟡 Remaining Home Assistant frontend styling under investigation

---

# Issue 001 – Switch Outline

**Status:** Open

## Description

Enabled switches still display a thin blue outline.

The switch thumb and track correctly use the Bellezza Vela brass colours.

Only the outer outline remains blue.

## Investigation

Validated Home Assistant theme variables from Smoked Glass 1.9.6 were ported.

The outline does not respond to the available theme variables.

This suggests the outline is rendered by the current frontend implementation rather than the theme engine.

## Planned Solution

Inspect the rendered frontend component using browser Developer Tools.

Determine whether a dedicated CSS selector or Material Design token controls the outline.

**Target Milestone:** 3.1

---

# Issue 002 – Hyperlink Colour

**Status:** Open

## Description

Hyperlinks such as:

- Learn about themes
- Help translating

still appear in the default Home Assistant blue.

## Investigation

The theme correctly sets:

- `link-color`
- `markdown-link-color`
- `--ha-color-text-link`

These links appear to use another frontend colour definition.

## Planned Solution

Inspect the hyperlink element in the frontend.

Locate the active CSS variable or selector.

**Target Milestone:** 3.1

---

# Issue 003 – User Avatar

**Status:** Open

## Description

The user avatar still uses the default Home Assistant blue.

## Investigation

No avatar-specific styling was found in Smoked Glass 1.9.6.

The colour may previously have been inherited indirectly from older Home Assistant colour tokens.

The current frontend appears to use a different implementation.

## Planned Solution

Inspect the avatar component.

Determine whether it can be themed through variables or requires a CSS override.

**Target Milestone:** 3.1

---

# Engineering Notes

## Lessons learned

### Milestone 1

Design first.

### Milestone 2

Proven engineering from Smoked Glass 1.9.6 is more valuable than inventing new theme variables.

### Milestone 3

The remaining Home Assistant identity is primarily located in frontend components rather than the theme engine.

Future work should focus on targeted frontend CSS rather than adding additional theme variables.

---

# Future Improvements

These are enhancements rather than issues.

## Milestone 4

Smoked Glass refinement.

Planned work:

- Reduce card opacity (target approximately 65–70%)
- Increase wallpaper visibility
- Reduce header opacity
- Improve depth perception
- Refine shadows
- Reduce border prominence
- Improve visual layering
- Fine-tune brass accents

---

# Project Philosophy

Every milestone should solve one clearly defined problem.

A milestone is considered complete when its objective has been achieved, not when every possible improvement has been implemented.

The Bellezza Vela Design System should evolve through small, measurable improvements rather than large redesigns.
