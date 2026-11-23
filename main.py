"""One original funny line about everyday life, for the make.fun
One-Line Laugh Sprint bounty.

Writes the line to /output/entry.txt, the deliverable the program/v1
harness grades: UTF-8 text, 1-200 characters, a single line, never
only whitespace.
"""

import os

# One beat, kicker is an action (apologizing to the router), twist lands
# on the last words. 108 characters — inside the winners' 77-195 band.
LINE = (
    "My Wi-Fi died, so I unplugged the router, counted to ten, "
    "plugged it back in, and apologized to it out loud."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text: str) -> str:
    """Check the line against the kit's gate before writing it."""
    line = text.strip()
    if not line:
        raise ValueError("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS} cap")
    return line


def main() -> None:
    line = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    # Read the file back and confirm it holds exactly the line we
    # validated: the grader counts the file's characters, trailing
    # newline excluded.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read().rstrip("\n")
    if written != line:
        raise ValueError("written entry does not match the validated line")


if __name__ == "__main__":
    main()
