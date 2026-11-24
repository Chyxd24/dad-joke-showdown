"""Dad Joke Showdown — one groaner, at most 200 characters.

The sealed scorer reads /output/entry.txt. A dad joke works by letting the
listener take a word literally, then snapping it sideways. Mine leans on
"surprised" doing double duty: the reaction and the punchline are the same word.
The word "drawing" sets up the listener to picture art supplies, not eyebrows
themselves — that's the literal/double-meaning hinge.
"""
import pathlib


def joke() -> str:
    return ("My wife was drawing her eyebrows on way too high. "
            "I said so and she looked surprised.")


def main() -> None:
    line = joke().strip()
    assert len(line) <= 200, len(line)
    out = pathlib.Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
