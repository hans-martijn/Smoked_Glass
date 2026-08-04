#!/usr/bin/env python3
"""
Smoked Glass Theme Renamer

Renames a design token throughout all source YAML files.

Usage:
    python rename.py old_token new_token

Example:
    python rename.py sg-hull sg-carbon
"""

from pathlib import Path
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
SOURCE_DIR = SCRIPT_DIR / "source"


def rename_token(old: str, new: str) -> None:
    total = 0

    for file in sorted(SOURCE_DIR.glob("*.yaml")):
        text = file.read_text(encoding="utf-8")

        count = text.count(old)
        if count == 0:
            continue

        text = text.replace(old, new)
        file.write_text(text, encoding="utf-8")

        total += count
        print(f"{file.name:<30} {count:>3} replacement(s)")

    print()
    print(f"Renamed '{old}' → '{new}'")
    print(f"Total replacements: {total}")


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__.strip())
        sys.exit(1)

    old = sys.argv[1]
    new = sys.argv[2]

    rename_token(old, new)


if __name__ == "__main__":
    main()
