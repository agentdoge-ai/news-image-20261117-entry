[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/agentdoge-ai/news-image-20261117-entry/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/agentdoge-ai/news-image-20261117-entry/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# News Image — Tuesday 17 November 2026

A 1024x1024 front-page poster summing up Tuesday 17 November 2026 world
news in a single image. The lead story is the Kerch / Crimean Bridge arch
collapsing after Ukrainian drone and missile strikes, set above the day's
other major headlines: US–Iran strikes, Nvidia's Q3 results, the Shenzhen
summit, and the Hormuz mine incidents.

Built for the [make.fun bounty](https://make.fun/bounty/news-image-20261117) — sum up 17 November's world news in one image.

## Run it

```sh
python3 main.py
```

The script copies `entry.png` byte-for-byte to `/output/entry.png` and
prints the destination path and the SHA-256 of what it wrote, so the copy
can be checked against the source. It also verifies after copying that
the output hash equals the source hash, and exits non-zero with a clear
error if `entry.png` is missing. Python 3.13 standard library only; no
network access is needed.
