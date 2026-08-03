# Smoked Glass 2.0 Refactor Plan

## Goal

Transform Smoked Glass 2.0 from an organically evolved theme into a
well-structured design system while preserving functionality.

---

# Phase 1 – Design System

Status: ⏳

- [ ] Hull
- [ ] Glass
- [ ] Brass
- [ ] Typography
- [ ] Semantic Colours
- [ ] Borders
- [ ] Shadows

Deliverable

- Bellezza Vela design tokens become the first section of the YAML.

---

# Phase 2 – Home Assistant Compatibility

Status: ⏳

## Colours

- [ ] primary-color
- [ ] accent-color
- [ ] ha-color-primary

## Navigation

- [ ] sidebar
- [ ] tabs

## Cards

- [ ] cards
- [ ] dialogs

## Lists & Menus

- [ ] dropdowns
- [ ] list items

## Forms

- [ ] inputs
- [ ] selectors

## Links

- [ ] links
- [ ] markdown

## Switches

- [ ] switches
- [ ] toggles

## Tooltips

- [ ] tooltip colours

## Snackbar

- [ ] snackbar colours

Deliverable

- Every HA variable exists exactly once.
- No duplicate mappings.

---

# Phase 3 – Material Design

Status: ⏳

...

---

# Phase 4 – Web Awesome

Status: ⏳

...

---

# Phase 5 – Legacy Compatibility

Status: ⏳

- Remove obsolete mappings
- Keep only required legacy variables

---

# Phase 6 – Validation

- [ ] No duplicate variables
- [ ] No undefined sg-* tokens
- [ ] Desktop tested
- [ ] Mobile tested
- [ ] Waveshare tested

---

# Milestone 4

Glass refinement

(Not part of this refactor.)
