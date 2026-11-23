"""Six Words, One Story — entry program.

Writes one original six-word story to /output/entry.txt.
The story: a lighthouse keeper whose one job is light, lighting
nothing on a given night — a whole life, and a whole mystery,
implied in six words.
"""

from pathlib import Path

STORY = "The lighthouse keeper lit nothing tonight."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate rejects non-UTF-8, >60 chars, or whitespace-only text,
    # so normalise once and validate before writing anything.
    story = " ".join(STORY.split())
    words = story.split()
    assert len(words) == 6, f"story must be exactly six words, got {len(words)}"
    assert 1 <= len(story) <= 60, f"story must be 1-60 chars, got {len(story)}"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(story, encoding="utf-8")
    print(f"Wrote {len(words)}-word story ({len(story)} chars) to {OUTPUT_PATH}")
    print(story)


if __name__ == "__main__":
    main()
