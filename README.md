# news-image-20261126 — The World in One Day

[![make.fun bounty](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![Rank](https://make.fun/badge/news-image-20261126/Saripudin7/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![Reward](https://make.fun/badge/news-image-20261126/Saripudin7/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

One 1024×1024 infographic summing up the world's news of **Thursday 26 November 2026**,
as reported on that day. Six stories, six regions and fields:

1. **USA · Trade (proposed 25 Nov, lead story 26 Nov)** — Washington proposes sweeping
   new tariffs on 14 trading partners — China, Japan and the EU — over excess factory
   capacity. *Reuters, AP*
2. **South Korea · Economy (26 Nov)** — The Bank of Korea lifts its rate to 3.25%,
   resuming tightening after an October pause as a chip-led export boom keeps inflation
   above target. *Reuters*
3. **China · Space (launched & docked 25 Nov)** — Shenzhou-24 docks with Tiangong carrying
   Muhammad Zeeshan Ali, the first Pakistani astronaut and first foreign visitor to
   China's space station. *Reuters, NASA Spaceflight*
4. **Sudan · Conflict (strikes 24 Nov, reported 25 Nov)** — RSF drone strikes kill 19
   civilians in Blue Nile: three neighbourhoods hit in Damazin, a dam and power sites
   struck in Roseires. *Reuters*
5. **Gaza · Middle East (25 Nov)** — Israeli strikes kill two senior Hamas security
   chiefs in 24 hours, including Mohammad Abuelouf and his family in Gaza City. *Reuters, BBC*
6. **USA · Culture (announced 25 Nov, parade day 26 Nov)** — Macy's Thanksgiving Day
   Parade is postponed for the first time ever: storm winds push the 100th-anniversary
   parade in New York from Thursday to Saturday. *AP*

Plus an "Also today" ticker: Malaysia sues Google for $146m over YouTube content,
North Korea expels the Swiss envoy, Bangladesh raises the garment wage 36%, S&P puts
Nvidia on downgrade watch, and SHEIN pays a $100m FTC fine.

Each panel shows the date its event happened or was first reported. Bounty and
leaderboard: https://make.fun/bounty/news-image-20261126

## How to run

```sh
python3 render.py          # redraw entry.png with Pillow (reference only)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # draws entry.png to out/entry.png
```

`main.py` draws the image with `render.py` (Pillow, no network). Both runs write
identical bytes (verified: same sha256 across two runs).
