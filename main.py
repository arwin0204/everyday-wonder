"""Everyday Wonder: write one surprising sentence about a small everyday moment."""

from pathlib import Path

ENTRY = (
    "My neighbour waters a dead geranium every evening, "
    "as if loyalty alone could talk the roots back into believing in spring."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(text: str) -> str:
    """Return the entry stripped, or raise if it breaks the gate."""
    cleaned = text.strip()
    if not cleaned or cleaned.isspace():
        raise ValueError("entry must not be empty or only whitespace")
    if not 1 <= len(cleaned) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(cleaned)}")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    # Exactly one sentence: one terminal mark, at the very end.
    terminals = sum(cleaned.count(mark) for mark in (".", "!", "?"))
    if terminals != 1 or cleaned[-1] not in ".!?":
        raise ValueError("entry must be exactly one sentence")
    return cleaned


def write_entry(text: str, path: Path = OUTPUT_PATH) -> Path:
    """Validate the entry, then write it as UTF-8 with no trailing newline."""
    cleaned = validate_entry(text)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(cleaned, encoding="utf-8")
    return path


def main() -> None:
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
