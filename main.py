#!/usr/bin/env python3
"""Two Days of Quiet Dread - v2 (deep ATM).

Writes one code-review comment to /output/entry.txt: a single line of at
most 140 characters that approves a pull request while carrying quiet
existential dread.

The line (76 characters, no trailing newline):
    Approved. The code is correct, which leaves me as the only remaining defect.

Why this line: the field is saturated with one mechanism - the code is
fine now, but it will haunt someone later (tests pass, it outlives us,
nobody will remember it in a hundred years). This line refuses that
template entirely and moves the dread somewhere the field never puts
it: into the reviewer, in the present. The code has been proven correct,
so by elimination the only thing left that can be wrong is the person
signing off on it. The laugh comes from the dread itself, the tone
stays flat, and the turn of phrase ("the only remaining defect") is
one no other entry in the field uses.
"""

import os

ENTRY = "Approved. The code is correct, which leaves me as the only remaining defect."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
