#!/usr/bin/env python3
"""
Smoked Glass Audit Tool

Scans all YAML source files and reports hard-coded values that may be
candidates for promotion to design tokens.

Usage:
    python audit.py
"""

from collections import defaultdict
from pathlib import Path
import re

SCRIPT_DIR = Path(__file__).resolve().parent
SOURCE_DIR = SCRIPT_DIR / "source"

LINE_RE = re.compile(r'^\s*([A-Za-z0-9_-]+):\s*"([^"]+)"')

IGNORE = {
    "transparent",
}


def interesting(value: str) -> bool:
    """Return True if this looks like a hard-coded literal."""

    if value in IGNORE:
        return False

    return (
        value.startswith("#")
        or value.startswith("rgb(")
        or value.startswith("rgba(")
        or value.endswith("px")
        or value.endswith("rem")
        or value.endswith("%")
    )


def main():

    occurrences = defaultdict(list)

    for file in sorted(SOURCE_DIR.glob("*.yaml")):
        
        if file.name == "00_design_tokens.yaml":
            continue
        with open(file, encoding="utf-8") as f:

            for lineno, line in enumerate(f, start=1):

                match = LINE_RE.match(line)

                if not match:
                    continue

                variable = match.group(1)
                value = match.group(2)

                if interesting(value):
                    occurrences[value].append(
                        (file.name, lineno, variable)
                    )

    print()
    print("Remaining hard-coded values")
    print("=" * 80)

    for value, locations in sorted(
        occurrences.items(),
        key=lambda item: (-len(item[1]), item[0]),
    ):

        print()
        print(f"{len(locations):>3} × {value}")

        current_file = None

        for filename, lineno, variable in locations:

            if filename != current_file:
                current_file = filename
                print(f"\n    {filename}")

            print(f"      {lineno:>4}  {variable}")


if __name__ == "__main__":
    main()
