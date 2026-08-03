# Smoked Glass 2.0 -- Engineering Roadmap

> Transform Smoked Glass from a single evolving YAML file into a
> modular, maintainable design system that generates one canonical
> theme.

## Engineering Principles

### Source vs. Artifact

-   The modular source files are the source of truth.
-   `Smoked_Glass_2.0.yaml` is generated.
-   Never edit the generated YAML directly.

### Refactoring

A refactor must **never change the appearance**.

Allowed: - Better structure - Better documentation - Better grouping -
Deduplication - Maintainability

Not allowed: - Visual changes - New colours - Glass refinements

### Documentation

Record engineering discoveries once (for example: `ha-*` theme keys use
no `--`).

## Repository Layout

``` text
themes/
    source/
        00_design_tokens.yaml
        10_home_assistant.yaml
        20_material_design.yaml
        30_web_awesome.yaml
        40_legacy.yaml
        build.py

    Smoked_Glass_2.0.yaml
```

## Phase 1 -- Design Tokens

Goal: - Hull - Glass - Brass - Typography - Semantic Colours - Borders -
Shadows

Definition of Done: - All `sg-*` tokens grouped. - No duplicates. -
Documentation improved. - Appearance unchanged.

## Phase 2 -- Home Assistant

Group: - Colours - Navigation - Cards - Lists & Menus - Forms - Links -
Switches - Radio Buttons - Sliders - Tooltips - Snackbar - Accessibility

Definition of Done: - Every HA mapping exists once. - `ha-*` uses no
`--`. - Appearance unchanged.

## Phase 3 -- Material Design

Group MD/MDC mappings. Definition of Done: - One location. - No
duplicates.

## Phase 4 -- Web Awesome

Group WA mappings. Definition of Done: - One location. - Fully
documented.

## Phase 5 -- Legacy Compatibility

Remove obsolete mappings. Keep only required compatibility.

## Phase 6 -- Build System

Create `build.py` that combines all source files into the canonical
theme and validates duplicate keys.

## Phase 7 -- Validation

-   No duplicate variables.
-   No undefined `sg-*` references.
-   Desktop tested.
-   Mobile tested.
-   Waveshare tested.

## Milestone 4

Glass refinement starts only after all engineering phases are complete.
