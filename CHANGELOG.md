# CHANGELOG

All notable changes to **Smoked Glass 2.0** will be documented in this file.

The format is inspired by *Keep a Changelog*, but adapted for an iterative design project where every milestone has a clear objective.

---

# Milestone 1 – Foundation

**Status:** ✅ Complete

**Objective**

Create the first implementation of the Bellezza Vela design language.

### Added

- Complete Smoked Glass colour palette
- Hull / Glass / Brass material system
- Typography hierarchy
- Semantic colours
- Sidebar styling
- Card styling
- Navigation styling
- Controls
- Dialog styling
- Fallback variables
- Extensive documentation throughout the YAML

### Result

The dashboard received its own visual identity.

The overall appearance shifted away from the default Home Assistant theme towards a calmer, yacht-inspired interface.

### Known Issues

- Material form controls remained white.
- Several Material dialogs ignored theme variables.
- Home Assistant accent blue still appeared in multiple locations.
- Cards remained slightly too opaque.
- Header still visually dominant.

---

# Milestone 2 – White Elimination

**Status:** ✅ Complete

**Objective**

Remove white Material Design controls and menus without changing the overall design language.

### Changed

- Reused proven Home Assistant theme variables from Smoked Glass 1.9.6.
- Replaced experimental variables with verified implementations.
- Improved support for Material Design form components.
- Improved menu styling.
- Improved selector styling.
- Improved text field colours.
- Improved dropdown styling.
- Improved dialog background handling.
- Reduced dashboard card opacity to improve wallpaper visibility.
- Reduced application header opacity.

### Result

The remaining white menus and selectors were successfully removed.

The Settings pages now visually match the dashboard far more closely.

### Remaining Issues

- Some popup dialogs still use the default Material styling.
- Home Assistant accent blue is still visible in several controls.
- User avatar still uses the default colour.
- Some links still use the default Home Assistant accent colour.

---

# Upcoming Milestones

## Milestone 3 – Blue Elimination

Objective:

Remove the remaining Home Assistant accent blue.

Focus:

- Switches
- Links
- Avatar
- Checkboxes
- Radio buttons
- Focus colours
- Accent colours

---

## Milestone 4 – Glass Refinement

Objective:

Refine the Bellezza Vela visual identity.

Planned work:

- Increase transparency of glass cards
- Fine-tune shadows
- Reduce visual weight of the top app bar
- Improve layering
- Improve glass depth
- Fine-tune brass accents

---

## Milestone 5 – Craftsmanship

Objective:

Final polish before the first public release.

Planned work:

- Consistency review
- Accessibility review
- Performance review
- Documentation review
- Theme cleanup
- Remove obsolete variables

---

# Release 2.0.0

Release criteria:

- No remaining Home Assistant blue.
- No white Material controls.
- Consistent glass appearance throughout Home Assistant.
- Complete documentation.
- Stable on current Home Assistant release.
- Ready for publication.

# Milestone 3 – Home Assistant Exorcism

**Status:** 🟡 Mostly Complete

**Objective**

Remove the remaining Home Assistant visual identity while preserving the Bellezza Vela design language.

### Changed

- Added validated Home Assistant 2026 design tokens.
- Improved switch styling using proven mappings from Smoked Glass 1.9.6.
- Improved Material Design accent colour handling.
- Improved tooltip styling.
- Improved snackbar styling.
- Unified Home Assistant accent colours with the Bellezza Vela brass palette.
- Simplified and cleaned interaction colour mappings.

### Result

Most remaining Home Assistant accent colours were successfully replaced.

The Settings pages now visually belong to the same design language as the dashboard.

### Engineering Findings

During this milestone it became clear that the remaining blue interface elements are no longer controlled by the Home Assistant theme engine alone.

Current Home Assistant versions style several interface elements directly through frontend components rather than theme variables.

This means future improvements will require a combination of theme variables and targeted frontend CSS.

### Remaining Issues

- Blue outline around enabled switches.
- Blue hyperlinks in selected settings pages.
- Default avatar colour.
- A few isolated frontend components that ignore theme variables.

---

# Milestone 4 – Smoked Glass Refinement

**Status:** 🔄 Planned

**Objective**

Transform the technically complete theme into a refined Bellezza Vela user experience.

### Planned Work

- Reduce card opacity to approximately 65–70% to reveal more of the wallpaper.
- Make the application header almost completely transparent.
- Improve visual layering of cards.
- Fine-tune shadows to create more depth.
- Reduce border visibility.
- Improve the perception of smoked glass.
- Refine brass accents where necessary.
- Balance contrast between dashboard and wallpaper.
- Improve readability without sacrificing transparency.

### Success Criteria

The interface should quietly disappear behind the content.

Cards should feel like lightly smoked glass floating above the wallpaper rather than opaque panels.

The user should notice the boat before noticing the interface.

