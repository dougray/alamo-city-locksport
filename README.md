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

The logo is the Alamo silhouette with a keyhole in the archway and a
paw-and-crossbones flag, by `ythpstrmoby`.

The only copy available was a 192x192 Redbubble sticker mockup
(`assets/acl-original.png`) - complete with the white die-cut border and a grey
product background, and no alpha channel. Rather than upscale that, the artwork
was **traced to vector**: the mark is flat black, so thresholding by luminance
isolates it cleanly from the white border and grey backdrop. A marching-squares
contour trace at 6x supersampling, simplified with Ramer-Douglas-Peucker, gives
16 closed loops and 346 points in about 4.9 KB.

| File | What it is |
|---|---|
| `logo.svg` | the mark, `fill="currentColor"` - recolour by CSS |
| `logo-white.svg` | white fill, for the dark hero and footer |
| `favicon.svg` | the mark on a white rounded square |
| `apple-touch-icon.png` | 180x180 raster of `favicon.svg` |
| `acl-original.png` | the source mockup, kept for provenance |

The wordmark is **not** part of the vector. It was too small to trace cleanly at
192px, and the page already sets the club name in Oswald as real text - which is
sharper, selectable, and readable by screen readers.

Being vector, this no longer has a resolution ceiling: it is crisp at any size.
If the true original artwork ever surfaces, it is still worth swapping in, since
this trace is faithful to a small mockup rather than to the artist's file.

## Venues

Two recurring gatherings, both listed on the page:

- **Monthly meetup** — Flying Saucer, 11255 Huebner Rd (`29.5466, -98.5777`)
- **Labyrinths & Locksport** — Court of Gamers, 2824 Thousand Oaks Dr
  (`29.5787767, -98.4426711`)

The Flying Saucer pin is placed from the street address; OSM has several
businesses at 11255 Huebner Rd and no node for the venue itself, so the pin marks
the complex rather than the unit.
