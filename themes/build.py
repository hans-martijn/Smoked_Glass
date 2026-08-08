#!/usr/bin/env python3
"""
Smoked Glass Theme Builder

Builds one Home Assistant theme for every design variant.

Structure:

source/
├── variants/
│   ├── Day.yaml
│   ├── Night.yaml
│   └── OLED.yaml
│
├── 10_home_assistant.yaml
├── 20_material_design.yaml
├── 30_web_awesome.yaml
└── 40_legacy.yaml

generated/
    Smoked_Glass_Day.yaml
    Smoked_Glass_Night.yaml
    ...

"""

from pathlib import Path
import sys


SCRIPT_DIR = Path(__file__).resolve().parent
SOURCE_DIR = SCRIPT_DIR / "source"
VARIANT_DIR = SOURCE_DIR / "variants"
OUTPUT_DIR = SCRIPT_DIR / "generated"


# ---------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------

def discover_variants():
    """Return all available design variants."""

    if not VARIANT_DIR.exists():
        print("ERROR")
        print(f"Missing directory: {VARIANT_DIR}")
        sys.exit(1)

    variants = sorted(VARIANT_DIR.glob("*.yaml"))

    if not variants:
        print("ERROR")
        print("No variants found.")
        sys.exit(1)

    return variants


def discover_layers():
    """Return all numbered implementation layers."""

    layers = sorted(
        f
        for f in SOURCE_DIR.glob("*.yaml")
        if f.is_file()
    )

    if not layers:
        print("ERROR")
        print("No implementation layers found.")
        sys.exit(1)

    return layers


# ---------------------------------------------------------------------
# Naming
# ---------------------------------------------------------------------

def theme_name(variant: Path) -> str:
    return f"Smoked Glass {variant.stem}"


def output_name(variant: Path) -> str:
    safe = variant.stem.replace(" ", "_")
    return f"Smoked_Glass_{safe}.yaml"


# ---------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------

def build_theme(variant: Path, layers):

    OUTPUT_DIR.mkdir(exist_ok=True)

    outfile = OUTPUT_DIR / output_name(variant)

    print()
    print(f"Building {theme_name(variant)}")
    print("-" * 60)

    with outfile.open("w", encoding="utf-8") as out:

        out.write(f"{theme_name(variant)}:\n\n")

        print(f"  • {variant.relative_to(SCRIPT_DIR)}")

        out.write(variant.read_text(encoding="utf-8").rstrip())
        out.write("\n\n")

        # card-mod theme identity is generated from the variant name so that
        # shared implementation layers never need to hardcode a theme name.
        out.write("# ---------------------------------------------------------------------\n")
        out.write("# Generated theme identity\n")
        out.write("# ---------------------------------------------------------------------\n")
        out.write(f"  card-mod-theme: {theme_name(variant)}\n\n")

        for layer in layers:

            print(f"  • {layer.name}")

            out.write(layer.read_text(encoding="utf-8").rstrip())
            out.write("\n\n")

    print()
    print(f"✓ {outfile.relative_to(SCRIPT_DIR)}")


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main():

    print()
    print("=" * 60)
    print("Smoked Glass Builder")
    print("=" * 60)

    variants = discover_variants()
    layers = discover_layers()

    print(f"\nFound {len(variants)} variant(s)")
    print(f"Found {len(layers)} implementation layer(s)")

    for variant in variants:
        build_theme(variant, layers)

    print()
    print("=" * 60)
    print(f"Done ({len(variants)} theme{'s' if len(variants) != 1 else ''})")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
