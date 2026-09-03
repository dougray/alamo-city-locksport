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

The logo is the Alamo silhouette with a keyhole archway and a paw-and-crossbones
flag. The club's original artwork is kept in `assets/source/`:

| File | What it is |
|---|---|
| `alamo-locksport-2.0.psd` | the layered Photoshop original, 1832x1800 |
| `alamo-locksport-2.0.png` | 1832x1800, greyscale + alpha - the working master |
| `alamo-locksport-2.0.jpg` | flattened JPEG of the same |
| `alamo-locksport-1.0-no-flag.jpg` | the earlier version, before the flag was added |

**Keep these.** They were nearly lost once: the artist has gone dormant and for a
while the only copy anywhere public was a 192px Redbubble sticker mockup. This
repo is now one of the places that original lives.

The site's vectors are traced from `alamo-locksport-2.0.png`. Its alpha channel
is an exact mask, so a marching-squares contour trace at ~1200px, simplified with
Ramer-Douglas-Peucker, reproduces the artwork faithfully - wordmark included.

| File | Where it is used |
|---|---|
| `logo-mark.svg` / `logo-mark-white.svg` | emblem only, no wordmark - the hero |
| `logo.svg` / `logo-white.svg` | full lockup with wordmark - the footer |
| `favicon.svg` | emblem on a white rounded square |
| `apple-touch-icon.png` | 180x180 raster of `favicon.svg` |

The hero deliberately uses the emblem *without* the wordmark, because the page
already sets the club name in Oswald as real text - sharper, selectable, and
readable by screen readers. The footer uses the full lockup.

`logo.svg` and `logo-mark.svg` use `fill="currentColor"`, so they take their
colour from CSS; the `-white` variants are for the dark hero and footer.

## Venues

Two recurring gatherings, both listed on the page:

- **Monthly meetup** — Flying Saucer, 11255 Huebner Rd (`29.5466, -98.5777`)
- **Labyrinths & Locksport** — Court of Gamers, 2824 Thousand Oaks Dr
  (`29.5787767, -98.4426711`)

The Flying Saucer pin is placed from the street address; OSM has several
businesses at 11255 Huebner Rd and no node for the venue itself, so the pin marks
the complex rather than the unit.
