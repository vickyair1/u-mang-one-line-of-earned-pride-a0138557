#!/usr/bin/env python3
"""Write one line of earned pride to /output/entry.txt.

Bounty: u-mang-one-line-of-earned-pride-a0138557 — "One Line of Earned Pride".
Gate: /output/entry.txt must be UTF-8 text of 1 to 240 characters, not only
white space. The line is written exactly, with no trailing newline, so the
byte count equals the character count.
"""

import argparse
import os
import sys

# The entry: a small person doing something hard, a long effort landing.
# A sailor who practised one knot a hundred times in the dark ties it blind
# in a storm — and the boat holds. Quiet, earned, concrete, fresh.
LINE = "He'd practised the knot a hundred times in the dark; when the storm hit, his hands tied it blind, and the boat held."


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the one-line entry to /output/entry.txt."
    )
    parser.add_argument(
        "--output",
        default="/output/entry.txt",
        help="Path to write the entry to (default: /output/entry.txt).",
    )
    args = parser.parse_args(argv)

    # Gate check, mirroring the sealed scorer: 1-240 chars, not only white space.
    if not 1 <= len(LINE) <= 240:
        print(f"entry is {len(LINE)} characters, must be 1-240", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be only white space", file=sys.stderr)
        return 1

    directory = os.path.dirname(args.output)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(args.output, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Self-check: read the file back and confirm it is byte-identical.
    with open(args.output, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        print("written file does not match the entry", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
