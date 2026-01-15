# Fundraising Dashboard

This repo generates a live fundraising priority dashboard from a Google Sheet.

## How it works
Google Sheet → Python scoring script → Markdown dashboard

## Dashboard
See the dashboard here:
- Public GitHub Pages: docs/index.md
- Generated Markdown: dashboards/grants_dashboard.md

## Refresh workflow
The `Refresh` button triggers a GitHub Actions workflow via a secure proxy. Configure:
- `SOURCE_URL` repo secret (Google Sheets CSV URL).
- `docs/assets/refresh-config.js` with the proxy URL.
Details: `docs/README.md`.
