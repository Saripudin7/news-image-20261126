"""Copy the pre-rendered news infographic to the output directory.

Standard library only, no network. The image entry.png lives in this
repository next to this program; both runs write identical bytes.

The image was rendered at build time from render.py (Pillow) and committed
here so the dev run needs no third-party packages.
"""
import os
import shutil

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(OUTPUT_DIR, "entry.png")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(src, dst)
    print("wrote", dst)


if __name__ == "__main__":
    main()
