# Alamo City Locksport

One-page website for Alamo City Locksport — San Antonio, Texas. A TOOOL affiliate.

**Live site:** https://dougray.github.io/alamo-city-locksport/

## Structure

Single self-contained `index.html` — all CSS inline, no build step, no framework.
The only external requests are one Google Font (Oswald) and the two OpenStreetMap
embeds in "Two Ways In".

Built on the same pattern as `longhorn-lockpicking`; if you change one, consider
whether the other wants the same change.

## The calendar

Two data files drive the Calendar section. They load via `<script src>` rather
than `fetch()` on purpose: a fetch of JSON fails under `file://`, which would make
the calendar look broken when you open `index.html` locally.

| File | Who maintains it |
|---|---|
| `data/meetings.js` | **Generated.** Do not hand-edit. |
| `data/conferences.js` | **Yours.** Nothing overwrites it. |

`data/meetings.js` comes from the group's public Meetup iCal feed via
`scripts/update_meetings.py`, run daily by `.github/workflows/update-meetings.yml`.
It commits only when dates change. Run it by hand with:

```
python3 scripts/update_meetings.py
```

Event titles come straight from Meetup, so "Labyrinths and Locksport" and the
monthly meetup show up under their own names. The renderer trims a trailing
"… for Alamo City Locksport" since the club name is redundant here.

`data/conferences.js` is the hand-maintained Texas security conference list,
shared in substance with the Longhorn site. The file header documents the fields.

## Assets

- `assets/logo.jpg` — the Alamo/ACL mark, from the @aclocksport_tx Instagram
  avatar. **150×150 is the largest copy available publicly**, so the footer logo
  and favicon are soft. Replace this file if a high-resolution or vector original
  turns up, then regenerate the icon:

```
sips -s format png -Z 180 assets/logo.jpg --out assets/apple-touch-icon.png
```

Brand colours are sampled from the logo: red `#C1272D`, blue `#3E7FA6`.

## Venues

Two recurring gatherings, both listed on the page:

- **Monthly meetup** — Flying Saucer, 11255 Huebner Rd (`29.5466, -98.5777`)
- **Labyrinths & Locksport** — Court of Gamers, 2824 Thousand Oaks Dr
  (`29.5787767, -98.4426711`)

The Flying Saucer pin is placed from the street address; OSM has several
businesses at 11255 Huebner Rd and no node for the venue itself, so the pin marks
the complex rather than the unit.
