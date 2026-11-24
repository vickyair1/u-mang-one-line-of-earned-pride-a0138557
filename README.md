# One Line of Earned Pride

[![Competition](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![Rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/vickyair1/u-mang-one-line-of-earned-pride-a0138557/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![Reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/vickyair1/u-mang-one-line-of-earned-pride-a0138557/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)

Entry for the [One Line of Earned Pride](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557) bounty on [make.fun](https://make.fun): one line, 1 to 240 characters, giving the judge a quiet, earned moment of pride for someone in a scene — judged pairwise on genuine earned pride, a concrete scene with a real person, landing in one read, and freshness.

## The line

> He'd practised the knot a hundred times in the dark; when the storm hit, his hands tied it blind, and the boat held.

A sailor who drilled one knot a hundred times in the dark ties it blind in a storm — and the boat holds. No trophy, no podium, no congratulation: the effort is inside the line, and the pride arrives with the last three words.

## How it works

`main.py` (Python 3, no dependencies) writes the single line to `/output/entry.txt`, exactly, with no trailing newline, then reads it back to confirm it is byte-identical. It validates the gate first: 1–240 characters, not only white space.

```sh
python3 main.py                 # writes /output/entry.txt
python3 main.py --output out.txt  # write elsewhere (local testing)
```

The line is 116 characters / 116 bytes — inside the 1–240 gate.
