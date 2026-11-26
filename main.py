#!/usr/bin/env python3
"""Funniest Lost Sock Status Update.

Writes a single status update, in the voice of a lost sock, to
``<MAKEFUN_OUTPUT_DIR>/entry.txt``. The update must be 1-120 characters
of UTF-8 text, so the line is checked before it is written.

Stdlib only; no network, no randomness, no clock: the same line every run.

The written file ends with one trailing newline (a plain-text convention);
the status update itself is 112 characters, inside the 1-120 gate.
"""

import os

# The sock's status update. It has ended up somewhere it should not be
# (inside the vacuum cleaner) and it has something to say about it:
# a new life, a promotion, and a message for the partner it left behind.
# The twist is the partner: instead of pining for the missing mate, the
# sock has moved on and is doing better than ever without them.
LINE = (
    "Status update: I've moved into the vacuum cleaner. "
    "The dust bunnies made me mayor. "
    "Tell my partner I'm thriving."
)

MAX_CHARS = 120


def build_line() -> str:
    """Return the status update, guarding the competition's length gate."""
    text = LINE.strip()
    if not text:
        raise ValueError("status update must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "status update is %d chars, over the %d-char limit"
            % (len(text), MAX_CHARS)
        )
    return text


def output_dir() -> str:
    """The directory the entry is written to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    text = build_line()
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    main()
