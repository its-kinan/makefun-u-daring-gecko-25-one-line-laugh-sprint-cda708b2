#!/usr/bin/env python3
"""One-Line Laugh Sprint entry: write one original funny line (<=200 chars)
on everyday life to /output/entry.txt.

The line: my houseplants have started giving me the same look as my gym
membership — paid for, ignored, quietly disappointed. The joke lands on a
single everyday image (neglected plants) colliding with a second one
(the unused gym membership) and resolves in a three-beat list that gets
shorter and sadder as it goes. No setup beyond the sentence itself, no
punchline tacked on after it — the list IS the punchline.
"""

import os

TEXT = (
    "My plants have started looking at me the way my gym membership does: "
    "paid for, ignored, quietly disappointed."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
