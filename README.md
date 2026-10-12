# mjonescon.no

The one-page site for Mjønes Consulting (org. no. 937 553 196). Plain HTML and CSS, no build step, no external
requests, no cookies. Dark first, light when the visitor's system asks for it.

- The site is `docs/`; that folder is what GitHub Pages publishes.
- Preview: `python tools/serve.py`, then open the address it prints (it serves `docs/` with the file types GitHub
  Pages uses).
- Icons are Lucide (ISC licence), drawn inline; the notice is in `docs/licenses.txt`.
- Putting it online: [DEPLOY.md](DEPLOY.md).
- Link-preview picture: `python tools/og-image.py` redraws `docs/og-image.png`.
