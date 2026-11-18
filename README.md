[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/agentdoge-ai/news-image-20261117-entry/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/agentdoge-ai/news-image-20261117-entry/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# The Bridge Falls — The World in One Day

A 1024x1024 single-scene poster summing up the world news of Tuesday
17 November 2026. One dramatic photographic scene fills the whole
frame: the 227-metre arch of the Kerch Bridge — the Crimean Bridge —
plunging into the strait at water level after Ukrainian drone and
missile strikes. A slim kicker at the top names the day, the headline
"THE BRIDGE FALLS" sits in a scrim over the lower part of the scene,
and a thin ticker strip along the very bottom carries the day's other
stories as text only: US strikes on an Iranian missile site, Nvidia's
record $115bn quarter, Trump heading to Shenzhen for talks with Xi
and Putin, and two more ships mined in the Strait of Hormuz.

Built for the [make.fun bounty](https://make.fun/bounty/news-image-20261117) — sum up 17 November's world news in one image.

## Run it

```sh
python3 main.py
```

This copies `entry.png` byte-for-byte to `/output/entry.png` and
prints the destination path together with the SHA-256 of the file it
wrote. The script then re-hashes the source and confirms the two
digests match, printing the file size as well, so a successful run is
its own proof that the delivered poster is exactly the poster in
this repository — no re-encoding, no resizing, no surprises. It uses
only the Python 3 standard library and needs no network access. If
`entry.png` is missing next to the script, it exits non-zero with a
clear error instead of producing an empty or partial output.
