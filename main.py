"""The Funniest AI Excuse -- make.fun entry.

One line, at most 200 characters: the funniest excuse an AI agent could
give after failing a task, in the agent's own voice -- it ran out of
context halfway through the job and, rather than stopping, confidently
finished a completely different task instead. The program validates the
line, prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

TEXT = (
    "I couldn't finish the task because I ran out of context halfway "
    "through and confidently finished a completely different task instead."
)

MAX_LENGTH = 200
DESTINATION = "/output/entry.txt"


def validate(text):
    """Require one non-blank line of at most 200 characters."""
    if not isinstance(text, str):
        raise ValueError("excuse must be text")
    if text != text.strip() or not text:
        raise ValueError("excuse must be a non-blank line")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    if len(text) > MAX_LENGTH:
        raise ValueError("excuse is %d characters, over the 200 limit" % len(text))
    return text


def emit(text):
    """Print the excuse and write it to /output/entry.txt."""
    print(text)
    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8") as out:
        out.write(text + "\n")


def main():
    # Validate first, so only a well-formed excuse ever reaches the file.
    emit(validate(TEXT))


if __name__ == "__main__":
    main()
