#!/usr/bin/env python3
"""Refresh data/meetings.js from the club's public Meetup iCal feed.

Meetup serves the feed without CORS headers, so the browser cannot read it
directly. This runs server-side (in CI) and writes a plain JS file, which the
page loads with a <script> tag -- that works over file:// as well as https://,
so opening index.html locally still shows a populated calendar.
"""

import json
import re
import sys
import urllib.request
from datetime import datetime, timezone

FEED = "https://www.meetup.com/alamocitylocksport/events/ical/"
OUT = "data/meetings.js"
UA = "Mozilla/5.0 (compatible; alamo-city-locksport-site/1.0)"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def unfold(raw):
    """iCal wraps long lines with a leading space on the continuation."""
    return raw.replace("\r\n ", "").replace("\r\n", "\n").replace("\n ", "")


def parse(raw):
    events = []
    for block in re.findall(r"BEGIN:VEVENT(.*?)END:VEVENT", unfold(raw), re.S):
        fields = {}
        for line in block.strip().split("\n"):
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            fields[key.split(";")[0]] = value.strip()

        start = fields.get("DTSTART", "")
        # Meetup emits floating local time: 20260905T190000
        m = re.match(r"^(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})", start)
        if not m:
            continue
        y, mo, d, h, mi, s = m.groups()

        if fields.get("STATUS", "CONFIRMED").upper() == "CANCELLED":
            continue

        events.append({
            "start": f"{y}-{mo}-{d}T{h}:{mi}:{s}",
            "title": fields.get("SUMMARY", "Club meeting"),
            "url": fields.get("URL", "https://www.meetup.com/alamocitylocksport/"),
        })

    events.sort(key=lambda e: e["start"])
    return events


def main():
    try:
        events = parse(fetch(FEED))
    except Exception as exc:                       # noqa: BLE001
        print(f"feed fetch/parse failed: {exc}", file=sys.stderr)
        return 1

    if not events:
        # Never blank out a good calendar because the feed hiccuped.
        print("feed returned no events; leaving existing file alone", file=sys.stderr)
        return 1

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    body = (
        "// Generated from the Meetup iCal feed. Do not edit by hand --\n"
        "// scripts/update_meetings.py overwrites this file.\n"
        f"// Last updated: {stamp}\n"
        "window.CLUB_MEETINGS = "
        + json.dumps(events, indent=2)
        + ";\n"
    )

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(body)

    print(f"wrote {len(events)} meetings to {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
