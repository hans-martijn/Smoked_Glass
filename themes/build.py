#!/usr/bin/env python3
"""
Smoked Glass Theme Builder

Builds a Home Assistant theme by concatenating all YAML source files in the
source/ directory in alphabetical order.

Usage:
    python build.py
    python build.py Smoked_Glass
    python build.py Smoked_Glass_Day
    python build.py Smoked_Glass_Night
"""

from pathlib import Path
import sys


SCRIPT_DIR = Path(__file__).resolve().parent
SOURCE_DIR = SCRIPT_DIR / "source"


def build_theme_name(filename: str) -> str:
    """Convert a filename into a Home Assistant theme name."""

    if filename.endswith(".yaml"):
        filename = filename[:-5]

    return filename.replace("_", " ")


def output_filename() -> str:
    """Determine the output filename."""

    if len(sys.argv) > 1:
        name = sys.argv[1]
        if not name.endswith(".yaml"):
            name += ".yaml"
        return name

    return "Smoked_Glass.yaml"


def main():

    output_file = output_filename()
    theme_name = build_theme_name(output_file)

    source_files = sorted(SOURCE_DIR.glob("*.yaml"))

    if not source_files:
        raise SystemExit("No source YAML files found.")

    with open(SCRIPT_DIR / output_file, "w", encoding="utf-8") as out:

        out.write(f"{theme_name}:\n\n")

        for source in source_files:

            with open(source, encoding="utf-8") as f:

                content = f.read()

                out.write(content)

                if not content.endswith("\n"):
                    out.write("\n")

                out.write("\n")

    print(f"✓ Built {output_file}")


if __name__ == "__main__":
    main()
