# Technical Debt

## Design Tokens

- [ ] Move remaining literal colours, RGBA values, shadows and radii from `10_home_assistant.yaml` to `00_design_tokens.yaml`.

## Home Assistant

- [ ] Review duplicated Home Assistant variable mappings.

## Build System

- [ ] Validate that generated `Smoked_Glass_2.0.yaml` is functionally identical to the manually maintained version before switching the source of truth.

## Material Design

- [ ] Replace remaining literal colours, RGBA values, shadows and radii in `20_material_design.yaml` with semantic design tokens from `00_design_tokens.yaml`.

## Legacy Compatibility

- [ ] Review legacy compatibility variables (`paper-*`) and determine whether remaining literal colours should become semantic design tokens or remain documented exceptions.
