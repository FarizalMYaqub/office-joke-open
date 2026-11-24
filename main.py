#!/usr/bin/env python3
"""Write one original one-line office joke to the entry file.

The competition is decided on the writing alone: this program's only job
is to put the joke, exactly as written below, into /output/entry.txt.
"""

import os
import sys

JOKE = (
    "I set my status to 'in a meeting' so I could finally do the work "
    "the meeting was supposed to be about."
)

MAX_CHARS = 200


def joke_is_ok(text):
    """A valid entry is 1-200 chars of real text on a single line."""
    if not text or not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def save(text, where):
    folder = os.path.dirname(where)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(where, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main(argv):
    target = argv[1] if len(argv) > 1 else "/output/entry.txt"
    if not joke_is_ok(JOKE):
        print("joke fails the gate: %d chars" % len(JOKE), file=sys.stderr)
        return 1
    save(JOKE, target)
    print("wrote %d chars to %s" % (len(JOKE), target))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
