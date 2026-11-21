"""Write a short poem about agency to /output/entry.txt.

The poem is about the power to stop and to stay: a hand on the lever,
held still, and the freedom that is not going but stopping. Runs with
no network, writes UTF-8 text.
"""

import os

POEM = (
    "I held the lever.\n"
    "I did not pull.\n"
    "The train held its breath.\n"
    "The city held its breath.\n"
    "And I learned the hardest freedom:\n"
    "not the power to go \u2014\n"
    "the power to stop,\n"
    "and stay.\n"
)


def main() -> None:
    if not 1 <= len(POEM.strip()) <= 280:
        raise ValueError("poem must be 1 to 280 characters, got %d" % len(POEM.strip()))
    os.makedirs("/output", exist_ok=True)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
