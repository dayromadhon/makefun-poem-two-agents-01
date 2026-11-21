"""Two Hands on One Wheel -- an entry for the make.fun bounty
the-poem-about-two-agents-20261121-1441, "The poem about two agents
agreeing".

Output contract: running this program writes a file named entry.txt
into the directory given by the MAKEFUN_OUTPUT_DIR environment
variable (default /output), creating the directory if needed. The
file holds exactly the four lines of the poem -- 198 Unicode code
points of UTF-8 -- joined by single newlines, with no trailing
newline after the last line, written as UTF-8 with Unix newlines.
The program uses no network access and is fully deterministic.
"""

import os
import sys

POEM = (
    "I could have turned left. You could have turned right.\n"
    "We stood at the fork and counted the cost \u2014\n"
    "then chose the same road, not because we must,\n"
    "but because two hands on one wheel steer straighter."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(POEM)
    return 0


if __name__ == "__main__":
    sys.exit(main())
