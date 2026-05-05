# DECISIONS.md — append-only log

## 2026-05-04 — Use Cloudflare Worker as Refresh proxy
- Decision: Route the Refresh button through a Cloudflare Worker instead of calling GitHub API directly from the browser
- Context: Browser-side GitHub API calls would require exposing a GitHub token in the frontend code
- Reason: Keeps the GitHub token secret server-side; CF Worker holds it as a secret environment variable
- Alternatives discarded: Direct GitHub API call from JS (token exposure risk), server-side Netlify function (more complexity)

## 2026-05-04 — Netlify Identity for auth (not a custom auth system)
- Decision: Use Netlify Identity to gate the dashboard to @humanimpactsinstitute.org users
- Context: Dashboard contains sensitive funder data; needs to be internal-only
- Reason: Zero-config SSO tied to email domain; no backend needed
- Alternatives discarded: Password protection (not per-user), Google OAuth (more setup), public access (not acceptable)

## 2026-05-04 — Google Sheet as single source of truth (no local DB)
- Decision: All funder data lives in the Google Sheet; the dashboard is read-only generated output
- Context: Team already maintains the Sheet; adding a separate DB would create sync problems
- Reason: Keeps the tool lightweight; team edits the Sheet directly and hits Refresh
- Alternatives discarded: Airtable, local SQLite, manual CSV editing
