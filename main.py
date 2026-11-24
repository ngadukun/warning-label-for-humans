"""Warning Label for Humans - a make.fun micro entry.

Writes one line (at most 160 characters): the safety
warning label that should come printed on every human
being. Funny first, plausible second - contents under
pressure, snacks and a nap required before decisions.
"""

import os
from pathlib import Path

ENTRY = (
    "WARNING: Contents under pressure. May cry at dog videos, "
    "argue with strangers online, and require snacks and a nap "
    "before any major decision."
)


def entry_path() -> Path:
    # The grader mounts the repo read-only and hands us a
    # writable directory through MAKEFUN_OUTPUT_DIR; locally
    # we fall back to output/ beside this file.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return Path(out_dir) / "entry.txt"
    return Path(__file__).resolve().parent / "output" / "entry.txt"


def main() -> None:
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
