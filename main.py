#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Deterministic program: writes the one sentence a house cat would say in
its own defence after knocking a glass off the table.
Stdlib only, no network, no randomness, no model calls.
"""

import os
from pathlib import Path

# The defence, in the cat's own logic: the glass was trespassing on a
# claimed sunbeam, the paw was diplomacy, and gravity is the real culprit.
SENTENCE = (
    "It was blocking the sunbeam I had already claimed, and when I merely "
    "reached out to negotiate, gravity \u2014 not me \u2014 made the final decision."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(SENTENCE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
