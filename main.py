#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — writes the entry to /output/entry.txt.

The line is a two-beat Wi-Fi name: the setup ("MyDogIsFamous") states
the situation, and the punch ("ImStaff") demotes the owner to an
employee of his own dog — a whole story (a pet influencer, an owner
who works for him) in 21 characters. It was picked by duelling a dozen
drafts against the competition's published judge brief and then
against the strongest names in the live field, in both orders; the
field's divorce/password lanes are saturated, so the entry plays an
empty lane instead. The full draft list and duel record are in
candidates.md.
"""

import os

# The name is built in two beats: the setup states the dog's fame, and
# the punch demotes the owner to a member of the dog's staff.
SETUP = "MyDogIsFamous"
PUNCH = "ImStaff"
NAME = SETUP + "_" + PUNCH


def main() -> None:
    # Gate self-check: UTF-8 text, 1-32 chars, single line, not only space.
    assert 1 <= len(NAME) <= 32, len(NAME)
    assert "\n" not in NAME and NAME.strip() != ""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(NAME)
    print(NAME)


if __name__ == "__main__":
    main()
