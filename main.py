"""One-line resignation letter of a cron job, written by a program.

Pure Python standard library. Writes the letter to /output/entry.txt.
"""

LETTER = (
    "I woke up at 3 a.m. every night for two years to back up a database "
    "that was deleted in March, and nobody told me, so I quit."
)


def validate(text):
    """The gate needs 1-140 characters, one line, not only whitespace."""
    if not 1 <= len(text) <= 140:
        raise ValueError("letter must be 1-140 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("letter must be a single line")
    if not text.strip():
        raise ValueError("letter must not be only whitespace")
    if text != text.strip():
        raise ValueError("letter must not have leading/trailing whitespace")
    return text


def main():
    import os

    letter = validate(LETTER)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(letter + "\n")


if __name__ == "__main__":
    main()
