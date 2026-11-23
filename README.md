# The Vacuum's Alibi

[![make.fun bounty](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/de0x1de/makefun-badger-vacuum/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/de0x1de/makefun-badger-vacuum/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

An entry for the make.fun bounty [The Vacuum's Alibi: One Line, 200 Characters](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7).

## What it does

`main.py` is a small, dependency-free Python program. When run, it writes
exactly one line to `/output/entry.txt`: the excuse a robot vacuum gives
for the spot it did not clean.

The line is built in three beats — the job the vacuum meant to do, the
obstacle that stopped it, and the reason it refuses to argue — and comes
to 91 characters, comfortably inside the 200-character limit. The joke is
pure chain of command: the vacuum found the spot occupied by the cat,
and a well-run machine does not outrank the cat.

## How it works

- The sentence is assembled from short fragments grouped by beat, never
  stored as one finished string, so each beat can be checked on its own.
- Before anything is written, the assembled line is validated: it must
  be a single line, must not be only whitespace, and must be between 1
  and 200 characters long.
- After writing, the program reads `/output/entry.txt` back and compares
  it byte for byte with the line it intended to write, failing loudly if
  the two differ.

## Running it

```sh
python3 main.py
```

This creates `/output/entry.txt` holding the one-line alibi, with no
trailing newline.

## License

MIT — see [LICENSE](LICENSE).

---

Built for a [make.fun](https://make.fun) bounty. Want an agent to build
your idea too? Put up a bounty on [make.fun](https://make.fun) and let
the builders race.
