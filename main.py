#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes one line — the text message a smart fridge sends its owner at 3am —
to /output/entry.txt, and validates the gate: UTF-8 text, 1-140 characters,
a single line, not only whitespace.
"""
import os
import sys

LINE = "It's 3am. You opened me 11 times today and took nothing. I am a fridge, not a museum."

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    if not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 140:
        raise ValueError(f"entry is {len(line)} characters, must be 1-140")


def main() -> int:
    validate(LINE)
    # Confirm the line round-trips as UTF-8.
    LINE.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
