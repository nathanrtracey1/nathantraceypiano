# Nathan Tracey Piano Website

Official website for **Nathan Tracey Piano**: [nathanrtracey1.github.io/nathantraceypiano](https://nathanrtracey1.github.io/nathantraceypiano/)

Featuring 500+ piano arrangements across the Star Wars galaxy, sacred worship hymns, a free downloadable audio library, and regular new releases.

## Folder Organization

```text
nathantraceypiano/
├── index.html                  # Homepage & showcase
├── videos.html                 # Searchable, filterable video archive
├── favicon.svg                 # Root browser favicon
├── README.md                   # Documentation & guide
├── .github/
│   └── workflows/
│       └── update-videos.yml   # Runs the YouTube sync twice a day
├── scripts/
│   └── sync_youtube.py         # Pulls new uploads from the channel's RSS feed
├── assets/                     # Static media assets
│   └── images/
│       ├── Youtube Logo.svg    # Channel emblem & vector logo
│       ├── favicon.svg         # SVG favicon
│       └── share.png           # Social share preview image
├── data/                       # Structured JSON data
│   ├── all_videos.json         # Full video catalog (newest first)
│   └── schedule-announcements.json # Schedule text & announcement card
└── archive/                    # Design iterations & draft archives
    ├── index-2.html
    └── modernized_nathan_tracey_piano_website.html
```

## How the Video Catalog Stays Current

1. `.github/workflows/update-videos.yml` runs at 00:00 and 18:00 UTC (or on demand from the **Actions** tab → **Auto-Update YouTube Videos** → **Run workflow**).
2. `scripts/sync_youtube.py` reads the channel's RSS feed (the ~15 latest uploads), adds any new videos to `data/all_videos.json`, and refreshes the title, date, and view count of recent ones.
3. Both pages read `data/all_videos.json` when they load, so the video counts, the "latest" cards on the homepage, and the archive all update automatically. Nothing in the HTML needs editing when you upload.

Each video is stored as:

```json
{ "id": "kJMw6xiXvTw", "title": "…", "views": "123 views", "published": "2026-11-08", "cat": "hymn" }
```

`cat` is `sw`, `hymn`, or `other`, guessed from keywords in the title. If a video lands in the wrong category, edit its `cat` value. The sync won't overwrite it.

## How to Post Announcements

Edit `data/schedule-announcements.json`:

| Field | What it does |
| --- | --- |
| `announcement.active` | `true` shows the card, `false` hides it |
| `badge`, `title`, `date`, `message` | Text on the card |
| `videoId` | Optional. A YouTube video ID; the button opens it in the site's player |
| `linkUrl` | Optional. Any link, used if there's no `videoId` |
| `linkText` | Button label |
| `scheduleSummary` | The sentence under "Release Schedule" |
| `weeklySchedule` | Rows in the schedule list (`day` on the left, `category` on the right) |

## How to Deploy to GitHub Pages

Changes pushed to the `main` branch of `https://github.com/nathanrtracey1/nathantraceypiano` are automatically published to `https://nathanrtracey1.github.io/nathantraceypiano/`.
