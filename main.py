#!/usr/bin/env python3
"""Write a robot vacuum's one-line alibi to /output/entry.txt.

The line is assembled from three beats -- the cleaning intent, the
obstacle that stopped the job, and the deadpan punch that closes it --
so the excuse reads as one tight sentence rather than a loose remark.
The assembled text is validated against the entry gate (UTF-8 text of
1 to 200 characters, a single line, not only whitespace) and verified
by reading the written file back before the program exits.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARACTERS = 200

# Beat 1: the vacuum states, in its own flat voice, what it meant to do.
INTENT_FRAGMENTS = ("I was going", "to clean it,")
# Beat 2: the obstacle. A seated cat is, to a small machine, terrain.
OBSTACLE_FRAGMENTS = ("but the cat", "was sitting there,")
# Beat 3: the punch. The machine does not argue with rank.
PUNCH_FRAGMENTS = ("and I respect", "the chain of command.")


def assemble_line() -> str:
    """Join the three beats, fragment by fragment, into one line."""
    fragments: list[str] = []
    for beat in (INTENT_FRAGMENTS, OBSTACLE_FRAGMENTS, PUNCH_FRAGMENTS):
        fragments.extend(beat)
    return " ".join(fragments)


def validate_line(line: str) -> None:
    """Raise ValueError if the line would fail the entry gate."""
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) < 1 or len(line) > MAX_CHARACTERS:
        raise ValueError(
            f"entry must be 1 to {MAX_CHARACTERS} characters, got {len(line)}"
        )
    if not line.endswith("."):
        raise ValueError("entry should end with its punch: a full stop")
    # The line is plain ASCII, so characters and UTF-8 bytes coincide;
    # encode anyway to prove the bytes written are valid UTF-8.
    encoded = line.encode("utf-8")
    # Byte-length gate: the file on disk is measured in bytes, so verify
    # the encoded size also stays within the same 1..200 bound. This
    # catches any future non-ASCII edit that would pass the character
    # count while silently inflating the payload.
    if not (1 <= len(encoded) <= MAX_CHARACTERS):
        raise ValueError(
            f"entry must be 1 to {MAX_CHARACTERS} UTF-8 bytes, got {len(encoded)}"
        )
    # Content anchors: the alibi only works if both the obstacle and the
    # punch are present. Guard against a fragment edit dropping either.
    if "cat" not in line:
        raise ValueError("entry must name the obstacle: the cat")
    if "chain of command" not in line:
        raise ValueError("entry must keep the punch: chain of command")


def main() -> None:
    line = assemble_line()
    validate_line(line)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")

    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != line:
        raise SystemExit("read-back mismatch: file does not hold the line")
    validate_line(written)
    print(f"wrote {len(written)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
