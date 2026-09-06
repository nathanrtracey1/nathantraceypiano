#!/usr/bin/env python3
"""
Sync Nathan Tracey Piano YouTube uploads to data/all_videos.json
Channel ID: UCo_jpiaZdQ837h6xTueAV6Q
RSS URL: https://www.youtube.com/feeds/videos.xml?channel_id=UCo_jpiaZdQ837h6xTueAV6Q
"""

import urllib.request
import ssl
import re
import json
import os
import sys

CHANNEL_ID = "UCo_jpiaZdQ837h6xTueAV6Q"
RSS_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"

SW_KEYWORDS = [
    "star wars", "mandalorian", "ahsoka", "andor", "bad batch", "clone wars",
    "jedi", "sith", "vader", "luke", "yoda", "grogu", "thrawn", "order 66",
    "shadow lord", "darth maul", "han solo", "palpatine", "boba fett", "obi-wan",
    "anakin", "tarkin", "death star", "tie fighter", "x-wing", "force theme",
    "across the stars", "duel of the fates", "imperial", "cantina", "skeleton crew",
    "baylan", "marrok", "vode an", "republic commando"
]

HYMN_KEYWORDS = [
    "hymn", "worship", "psalm", "glory", "praise", "jesus", "christ", "god", "grace",
    "faith", "cross", "angels", "heaven", "risen", "holy", "blessed", "assurance",
    "savior", "bleed", "our god", "ages past", "how deep", "thine be", "abide with me",
    "rock of ages", "come thou fount", "vision", "redeemer", "grateful", "anchor",
    "soul", "getty", "church", "father", "lord", "mercy", "calvary", "hallelujah",
    "peaceful", "peace", "trials", "abide", "fountain"
]

def categorize_title(title):
    t = title.lower()
    if any(k in t for k in SW_KEYWORDS):
        return "sw"
    elif any(k in t for k in HYMN_KEYWORDS):
        return "hymn"
    return "other"

def sync_videos():
    # Find data/all_videos.json
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(script_dir, ".."))
    data_file = os.path.join(root_dir, "data", "all_videos.json")

    if not os.path.exists(data_file):
        print(f"Error: {data_file} not found!")
        sys.exit(1)

    with open(data_file, "r", encoding="utf-8") as f:
        existing_videos = json.load(f)

    existing_ids = set(v["id"] for v in existing_videos)
    print(f"Current catalog has {len(existing_videos)} videos.")

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(RSS_URL, headers={"User-Agent": "Mozilla/5.0"})
    try:
        xml_content = urllib.request.urlopen(req, context=ctx).read().decode("utf-8", "ignore")
    except Exception as e:
        print(f"Failed to fetch RSS feed: {e}")
        return False

    entries = re.findall(r"<entry>(.*?)</entry>", xml_content, re.DOTALL)
    new_videos = []

    for entry in entries:
        vid_match = re.search(r"<yt:videoId>([^<]+)</yt:videoId>", entry)
        title_match = re.search(r"<title>([^<]+)</title>", entry)
        pub_match = re.search(r"<published>([^<]+)</published>", entry)

        if not vid_match or not title_match:
            continue

        vid_id = vid_match.group(1)
        title = title_match.group(1).replace("&amp;", "&").replace("&quot;", '"').replace("&#39;", "'")
        pub_date = pub_match.group(1)[:10] if pub_match else "Recently"

        if vid_id not in existing_ids:
            cat = categorize_title(title)
            new_item = {
                "id": vid_id,
                "title": title,
                "views": "New upload",
                "published": pub_date,
                "cat": cat
            }
            new_videos.append(new_item)
            existing_ids.add(vid_id)
            print(f"Found new video: [{cat.upper()}] {title} ({vid_id})")

    if new_videos:
        # Prepend new videos to the front
        updated_catalog = new_videos + existing_videos
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(updated_catalog, f, indent=2)
        print(f"Successfully added {len(new_videos)} new video(s)! Total is now {len(updated_catalog)}.")
        return True
    else:
        print("Catalog is already completely up to date. No new videos found.")
        return False

if __name__ == "__main__":
    sync_videos()
