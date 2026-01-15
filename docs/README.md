# Fundraising Dashboard (Public)

This folder hosts the GitHub Pages site.

The dashboard tables are generated automatically from a Google Sheet and injected into
`docs/index.md` between `<!-- DASHBOARD:START -->` and `<!-- DASHBOARD:END -->`.

## Refresh button
The "Refresh" button triggers a GitHub Actions workflow via a Cloudflare Worker proxy.

Setup checklist:
- Add a repository secret named `SOURCE_URL` with the Google Sheets CSV URL.
- Configure and deploy the Cloudflare Worker in the repo root.
- Put the Worker URL in `docs/assets/refresh-config.js` as `window.REFRESH_PROXY_URL`.
