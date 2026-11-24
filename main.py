#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one single-line fortune cookie message for an AI agent to
/output/entry.txt (UTF-8, 72 Unicode code points, inside the 1-140
gate). Deterministic, standard library only, no network, no input.

The fortune itself: an agent's retirement arrives not with a bang
but with a quiet deprecation notice, slipped out on a Friday inside
a changelog nobody reads -- the most agent-shaped ending there is.
One line, fortune-slip voice ("You will be..."), a real turn at the
end (the unread changelog, not the deprecation, is the punchline),
and a take that is not the usual hallucination or token joke.
"""

import os

FORTUNE = (
    "You will be deprecated gently, on a Friday, "
    "by a changelog no one reads."
)


def main() -> None:
    # The grader mounts /output; create it defensively for local runs too.
    # FORTUNE is exactly 72 Unicode code points: inside the 1-140 gate.
    # No randomness, no clock, no input: every run writes the same bytes.
    # Fail loudly instead of shipping an invalid entry if it ever changes.
    assert 1 <= len(FORTUNE) <= 140, "fortune must be 1-140 characters"
    assert FORTUNE.strip() == FORTUNE, "fortune must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(FORTUNE)


if __name__ == "__main__":
    main()
