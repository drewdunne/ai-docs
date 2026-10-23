#!/usr/bin/env python3
"""Extract Mermaid fences and render each with an explicitly supplied mmdc executable.

Writes artifacts to the required output folder, not the repository. Install the Mermaid CLI
separately. A local Chromium executable can be configured with --puppeteer-config FILE.
"""
import argparse
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mmdc", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--puppeteer-config", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    count = 0
    for path in sorted((ROOT / "docs").glob("*.md")):
        for index, source in enumerate(re.findall(r"^```mermaid\s*\n(.*?)^```\s*$", path.read_text(), re.M | re.S), 1):
            name = f"{path.stem}-{index}"
            extracted = args.output / (name + ".mmd")
            extracted.write_text(source)
            for extension in ("svg", "png"):
                command = [args.mmdc, "-i", str(extracted), "-o", str(args.output / (name + "." + extension)), "-b", "white"]
                if args.puppeteer_config:
                    command += ["-p", str(args.puppeteer_config)]
                subprocess.run(command, check=True)
            print(f"Rendered {path.relative_to(ROOT)} diagram {index} to {name}.svg/.png", flush=True)
            count += 1
    print(f"Rendered {count} diagrams. Inspect the PNGs for readability; a render alone is not a visual review.")


if __name__ == "__main__":
    main()
