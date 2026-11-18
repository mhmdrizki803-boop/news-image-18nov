"""Copy entry.png into the make.fun output directory."""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENTRY = HERE / "entry.png"


def output_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> None:
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ENTRY, out / "entry.png")


if __name__ == "__main__":
    main()
