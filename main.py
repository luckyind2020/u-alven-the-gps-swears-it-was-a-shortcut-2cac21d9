"""The GPS Swears It Was a Shortcut -- make.fun entry.

The excuse itself lives in entry.txt as one line of plain text. This
program reads it, checks it fits the bounty gate (1-200 characters),
and hands it to the grader at /output/entry.txt.
"""

import os
import sys


def load_excuse() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as handle:
        return handle.read().strip()


def main() -> int:
    line = load_excuse()
    if not line or len(line) > 200:
        print("entry must be 1-200 characters", file=sys.stderr)
        return 1
    if "\n" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
