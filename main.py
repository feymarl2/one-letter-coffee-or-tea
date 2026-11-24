"""One Letter: Coffee or Tea — entry "A" (coffee).

The approved choice is the single letter A: coffee, picked for the
caffeine-speed stance — coffee is the fast, vivid, punchy answer, and
the letter A lands as the fuller, more alive stance for the drink it
names. The program writes exactly that one letter to entry.txt, with
no trailing newline, no word, no explanation and no punctuation, so
both grading runs produce byte-identical output. One byte is also the
floor of the tie-break chain (smaller text wins ties), so nothing
further can be trimmed without breaking the gate.
"""

import os
from pathlib import Path

# Gate from the competition rules: /output/entry.txt must be UTF-8 text
# of exactly 1 character, not only white space.
LETTER = "A"

assert len(LETTER) == 1 and LETTER.strip(), "entry must be exactly one letter"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LETTER, encoding="utf-8")


if __name__ == "__main__":
    main()
