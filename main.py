#!/usr/bin/env python3
"""One Word, One Username, One Reward — entry program.

The bounty asks for exactly one thing: the entrant's own make.fun
username, sent as a single word with nothing else attached. No pitch,
no explanation, no link. So this program does exactly that: it writes
the handle "gibalers-rgb" to /output/entry.txt and nothing more.

Why this handle is the entry: the judge's first criterion is that the
text is a real make.fun username, the entrant's own handle, sent as one
word. Any extra word would lose to a genuine handle, so the text is the
handle alone, twelve characters, one word, no trailing newline.
"""

import os
import sys

USERNAME = "gibalers-rgb"
OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 30  # the gate's cap: entry.txt must be 1 to 30 characters


def check_username(name: str) -> None:
    """Refuse anything that would fail the gate or the judge's brief."""
    if not name or name.strip() != name:
        raise ValueError("username is empty or padded with whitespace")
    if len(name) > MAX_LENGTH:
        raise ValueError(f"username is longer than the {MAX_LENGTH}-character cap")
    if any(ch.isspace() for ch in name):
        raise ValueError("username must be a single word, no spaces")
    if not all(33 <= ord(ch) <= 126 for ch in name):
        raise ValueError("username must be printable ASCII, no padding")


def main() -> int:
    check_username(USERNAME)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(USERNAME)
    # Read it back and prove the file holds exactly the handle: one word,
    # no padding, no trailing newline, so the gate sees 12 characters.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != USERNAME:
        raise RuntimeError(f"entry.txt mismatch: got {written!r}")
    print(f"wrote {len(USERNAME)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
