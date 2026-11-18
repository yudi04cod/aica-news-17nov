# aica-news-17nov

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/yudi04cod/aica-news-17nov/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/yudi04cod/aica-news-17nov/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A flat vector-style newspaper front page summing up Tuesday 17 November
2026 in one image: "THE WORLD IN ONE PICTURE". Six story panels cover the
day's news — the Ukrainian strike on the Kerch Bridge, tankers hitting
mines near the Strait of Hormuz, Trump in Manila for the ASEAN summit,
the JPMorgan outage, the failed ULA Vulcan rocket, and Estonia's decision
to shut its Russia border. Every scene is drawn programmatically with
Python (PIL) in `draw.py`, so all text stays crisp and legible.

## How to run

```sh
python3 draw.py        # regenerate entry.png (1024x1024)
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

`main.py` uses only the Python standard library and writes the same bytes
on every run.

Built for make.fun — referral code 38m33ybw
