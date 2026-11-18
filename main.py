"""Entry point for the news-image-20261117 competition.

Copies the pre-drawn front-page image (entry.png, built by draw.py) to
the output directory as entry.png. Standard library only, no network,
and fully deterministic: the same bytes are written on every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        raise FileNotFoundError("entry.png is missing next to main.py")
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
