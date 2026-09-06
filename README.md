# Nathan Tracey Piano Website

Official website for **Nathan Tracey Piano** ([nathantraceypiano.com](https://nathanrtracey1.github.io/nathantraceypiano/)).
Featuring 528+ piano arrangements across the Star Wars galaxy, sacred worship hymns, downloadable audio library, and weekly release schedule.

## Folder Organization

```text
nathantraceypiano/
├── index.html                  # Apple-style Homepage & Showcase
├── videos.html                 # Dedicated 528-Video Archive with Search & Filters
├── favicon.svg                 # Root browser favicon
├── README.md                   # Documentation & guide
├── assets/                     # Static media assets
│   └── images/
│       ├── Youtube Logo.svg    # Channel emblem & vector logo
│       ├── favicon.svg         # SVG favicon
│       └── share.png           # Social share banner
├── data/                       # Structured JSON databases
│   ├── all_videos.json         # 528 channel videos catalog
│   └── schedule-announcements.json # Weekly schedule & announcement bulletin
└── archive/                    # Design iterations & draft archives
    ├── index-2.html
    └── modernized_nathan_tracey_piano_website.html
```

## How to Post Announcements
Edit `data/schedule-announcements.json` directly. The homepage will automatically display the latest bulletin!

## How to Deploy to GitHub Pages
Changes pushed to the `main` branch of `https://github.com/nathanrtracey1/nathantraceypiano` are automatically published to `https://nathanrtracey1.github.io/nathantraceypiano/`.
