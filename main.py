"""Entry point: draw the 26 November 2026 world-news infographic.

Writes entry.png to $MAKEFUN_OUTPUT_DIR (default /output).
Standard library only here; the drawing itself lives in render.py (Pillow).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from render import render  # noqa: E402


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    img = render()
    img.save(os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
