"""One-line fridge roast for make.fun's 'One Line, One Laugh: Roast Your Fridge'.

Writes the chosen roast to entry.txt in the output directory
($MAKEFUN_OUTPUT, else /output). Python 3.13 standard library only.
"""

import os

ROAST = (
    "The crisper drawer turns lettuce into liquid on day two, which "
    "technically makes it the world's worst slow cooker\u2014congratulations."
)


def check_gate(text: str) -> None:
    """Enforce the bounty gate: 1-200 chars, one line, not only whitespace."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("roast is empty or only whitespace")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("roast must be a single line")
    if not 1 <= len(stripped) <= 200:
        raise ValueError(f"roast is {len(stripped)} chars, must be 1-200")


def main() -> None:
    check_gate(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the line, no trailing newline: the gate counts the file.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    print(f"Wrote {len(ROAST)}-character roast to {path}")


if __name__ == "__main__":
    main()
