# Saturday 21 November 2026: 50 sourced stories, a UTC timeline and a date check

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/ariffforai/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/ariffforai/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

Entry for the [make.fun bounty "Sum up 21 November's world news in one image"](https://make.fun/bounty/news-image-20261121): one 1024×1024 picture of Saturday 21 November 2026, drawn as a newspaper front page.

## What the image shows

- **Masthead:** "THE WORLD IN ONE DAY" — 50 stories · 7 regions · all from Saturday 21 November 2026.
- **The day in UTC:** six time slots from Iran's MQ-9 downing claim over the Strait of Hormuz (02:40 UTC) to Boca Juniors lifting the Copa Sudamericana in Barranquilla (22:30 UTC).
- **4 hero stories** with original flat drawings: Iran's claim to have downed a 58th US MQ-9 drone, COP31 running into overtime in Antalya with fossil fuels dropped from the draft, Boca Juniors beating Atlético Mineiro 2–0 to end an 18-year wait for an international trophy, and the EU's proposed tax on Big Tech.
- **12 grid stories** with small icons: the Houthi strikes after the Saudi coalition's Hodeidah operation, the FBI and US Agriculture Department breaches, EU leaders demanding a role in the Ukraine talks, NATO chief Rutte heading to Warsaw, the Manipur illicit-liquor deaths, the Balochistan operation, India–New Zealand day three, Australia's T20 win over England, Alcaraz at the ATP Finals, Leeds stunning Chelsea 4–1, and Harry Kane's ankle injury.
- **A world map with numbered pins** and a region legend, plus the numbered one-line list of stories 17–50.
- **A red DATE CHECK bar** naming what was deliberately left out: the ICJ's Rohingya genocide ruling and the Shenzhen trilateral summit (both Thursday 19 November), Fiona the hippo and the moon-soil potatoes study (both Thursday 19 November), Trump's data-centre tax threat and Russia's barrage with missiles landing in Poland (both Friday 20 November), the Van Gogh sale (Wednesday 18 November) and Nvidia's results (Tuesday 17 November).
- **Sourcing:** every story carries a CLAIM or CONFIRMED tag and a named source; the footer names the wires (Al Jazeera, Reuters, AP, BBC, Dawn, The Hindu, CNA, IRNA, Mehr News, Bernama, beIN SPORTS, Flashscore, EIN Presswire). CLAIM means one side's account, not independently confirmed.

Region counts add up to 50: AFRICA 6 · AMERICAS 7 · ASIA 16 · EUROPE 11 · GLOBAL 3 · MIDDLE EAST 5 · OCEANIA 2.

## How it works

`entry.png` is the finished front page, drawn at build time with PIL from the story data in `stories.json` (headline, summary, region, source, verification tag, UTC time and map position for each of the 50 stories). `main.py` (Python 3.13, standard library only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`) and verifies the copy: PNG signature, IHDR declaring 1024×1024, a whole IEND chunk at the end of the file, and byte-equality with the shipped file. No network, no randomness — two runs write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Files

- `entry.png` — the front page (1024×1024 PNG, under 1 MiB)
- `main.py` — the entry program
- `stories.json` — the 50 dated, sourced stories the page is drawn from
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
