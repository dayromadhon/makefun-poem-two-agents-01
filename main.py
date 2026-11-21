#!/usr/bin/env python3
"""Entry for make.fun bounty the-poem-about-two-agents-20261121-1441.

Writes one short poem about agency — the power to choose and to act —
about two agents agreeing, to <output_dir>/entry.txt.

No network. Deterministic: the same bytes on every run.
Output dir: $MAKEFUN_OUTPUT_DIR if set, else /output.
"""

import os
import sys

POEM = (
    "I could have turned left. You could have turned right.\n"
    "We stood at the fork and counted the cost —\n"
    "then chose the same road, not because we must,\n"
    "but because two hands on one wheel steer straighter."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    return 0


if __name__ == "__main__":
    sys.exit(main())
