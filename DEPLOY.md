# Putting mjonescon.no online (GitHub Pages, personal account)

The site is the plain files in `docs/`: `index.html`, `style.css`, `404.html`, `favicon.svg`, `og-image.png`,
`img/aster.webp`, `licenses.txt`, `robots.txt`, `CNAME` (which holds `mjonescon.no`) and `.nojekyll`. GitHub Pages
serves that folder as it is; nothing is built, and the rest of the repo (this file, `tools/`) is not published.

It goes on your personal GitHub account, `9876543214`, never on K2's organisation or K2's Azure.

## 1. The code is on GitHub
- A **public** repository on your personal account holds this folder's `main` branch. `main` already holds the whole
  site as one commit, so pushing `main` is what publishes it. A free account can only serve Pages from a public
  repository. Nothing in the repo is private: everything on the page is already public in Enhetsregisteret.
- Create an empty repository named `mjonescon.no` on github.com while signed in as `9876543214` (no README, no
  licence), then push from Git Bash:

```bash
git -C "/c/Users/UlrikNordvikMjønes/IT-utvikling/Egne prosjekter/business-website" remote add origin https://9876543214@github.com/9876543214/mjonescon.no.git
git -C "/c/Users/UlrikNordvikMjønes/IT-utvikling/Egne prosjekter/business-website" push -u origin main
```

The username in the address makes Git sign in as your personal account, not the K2 account this laptop may already
hold. If a «Connect to GitHub» sign-in window opens, sign in there as `9876543214` (in the browser, or with a code);
it is asking for your personal account, never for K2's. If the push answers «Permission to 9876543214/mjonescon.no.git
denied to Ulrikmjones-k2», Git used the K2 account: run the push again, and pick or sign in to `9876543214` when asked.

If you name the repository something else, change `mjonescon.no.git` in the first line to match; the custom domain
works with any name.

## 2. GitHub knows the domain is yours (do this before the DNS records)
- In your **profile** settings (not the repository's), under Pages, add `mjonescon.no` as a verified domain.
- GitHub shows a TXT record. Add it on the DNS page of the shop you bought mjonescon.no from (step 4 says more):

| Host | Type | Value |
|---|---|---|
| `_github-pages-challenge-9876543214` | TXT | the code GitHub shows you |

- Back on GitHub, Verify passes. Keep the TXT record for good: it stops anyone else from claiming the domain on GitHub.

## 3. The repository serves Pages
- In the repository's settings, under Pages: source «Deploy from a branch», branch `main`, folder `/docs`.
- The custom domain field shows `mjonescon.no` (GitHub reads it from the `CNAME` file). If it is empty, type
  `mjonescon.no` and save.

## 4. The domain points at GitHub
The records go in the shop you bought mjonescon.no from, on its DNS page for the domain. That shop runs the domain's
nameservers: on 2026-10-12 they were `ns1.no1.groupdnsservice.com` and `ns2.no1.groupdnsservice.com`. To see them
yourself:

```bash
nslookup -type=ns mjonescon.no
```

There:

- **Remove** any A, AAAA or CNAME record for the bare domain and for `www`, and any web forwarding or parking on the
  domain. They would compete with GitHub's. On 2026-10-12 both names answered `151.249.121.9`, a «mjonescon.no is not
  set up yet» page: those are the records to remove.
- **Keep** any MX records and SPF TXT record: those carry e-mail for the domain.
- **Add** these nine records. A host of `@` means the bare domain; some panels show it as an empty host field.

| Host | Type | Value |
|---|---|---|
| `@` | A | `185.199.108.153` |
| `@` | A | `185.199.109.153` |
| `@` | A | `185.199.110.153` |
| `@` | A | `185.199.111.153` |
| `@` | AAAA | `2606:50c0:8000::153` |
| `@` | AAAA | `2606:50c0:8001::153` |
| `@` | AAAA | `2606:50c0:8002::153` |
| `@` | AAAA | `2606:50c0:8003::153` |
| `www` | CNAME | `9876543214.github.io.` |

Never add a wildcard record (`*`). GitHub warns that it lets anyone take over your subdomains.

Values from GitHub's docs, «Managing a custom domain for your GitHub Pages site», read 2026-10-12.

## 5. HTTPS is on
- Within minutes to a few hours, the repository's Pages settings show the DNS check passing, and GitHub issues the
  certificate itself. Then tick «Enforce HTTPS». It can take up to 24 hours before the box can be ticked.

## 6. It works when
- `https://mjonescon.no` shows the page with a padlock.
- `https://www.mjonescon.no` lands on `https://mjonescon.no`.
- `https://mjonescon.no/anything` shows the site's own «This page does not exist» page.
- The organisation number on the page opens Mjønes Consulting in the Brønnøysund register.
- A mail sent to the contact address on the page arrives in your inbox. (The e-mail settings in the shop you bought
  the domain from can usually forward that address to the inbox you already use.)

To check the DNS from Git Bash while you wait (both should list GitHub's addresses):

```bash
nslookup mjonescon.no
nslookup www.mjonescon.no
```

## Changing the site later
Edit the files in `docs/`, commit on `main`, push. GitHub Pages republishes within a minute or two. If the name or the
tagline changes, run `python tools/og-image.py` to redraw the link-preview picture.
