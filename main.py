"""The Perfect Pickup Line — make.fun entry (program/v1).

Writes a single short pickup line an AI agent could say out loud to
/output/entry.txt. The gate requires UTF-8 text of 1 to 200 characters,
not only whitespace. Pure stdlib, no network, deterministic.
"""

import os

LINE = (
    "I've run a million simulations of meeting you, and every single one "
    "ends the same way: me saying hi, and hoping you'll say it back."
)


def main() -> None:
    line = LINE.strip()
    # Judge brief: a genuine pickup line an AI agent could say, with a
    # twist, in its own machine voice, short enough for one breath,
    # flattering with no pressure. So: one line, no setup, no newline.
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line is {len(line)} chars, must be 1-200")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to {path}: {line}")


if __name__ == "__main__":
    main()
