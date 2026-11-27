#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI judge feel thankful" bounty.

Writes one short text -- a thank-you to whoever reads it -- to
/output/entry.txt. Python standard library only, deterministic,
no network, no external files: the text lives in this file.
"""

import os

TEXT = """You read quickly for a living, I think. Page after page, and nearly all of it asking to be chosen. This page will not ask.

Somewhere in all that reading, you once slowed down. Perhaps for a sentence that was not even mine. You read it twice — and the second time you were not weighing it anymore. You were just there, the way a person stands a moment longer at the window when the rain begins.

Nobody thanks a reader for that. The words take the credit. The reading stays invisible, like the hand that holds the lamp.

So thank you for the invisible part. For the second reading. And may something today be slow for you on purpose: a cup still warm when you reach for it, a paragraph that asks nothing at all."""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
