#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one houseplant out-of-office auto-reply (1-120 UTF-8 chars)
to /output/entry.txt. Stdlib only; never deletes the output directory itself.
"""
import os

LABEL = "I am away from my desk, slowly dying in the corner by the window. Please water the fern; it saw everything."


def main():
    if not 1 <= len(LABEL) <= 120 or not LABEL.strip():
        raise SystemExit("label fails the 1-120 char gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
