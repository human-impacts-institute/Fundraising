# LESSONS.md — append-only log

## 2026-05-04 — dashboards/ and docs/index.html are auto-generated
- Context: Both output files look like editable content
- Problem: Any manual edits are silently overwritten the next time `score_grants.py` runs
- Lesson: All formatting, structure, and content changes must be made in `scripts/score_grants.py`, not in the output files
- Severity: 🔴 Critical

## 2026-05-04 — data/source_url.txt contains a private Google Sheets URL
- Context: The file exists in the repo directory alongside committed files
- Problem: If accidentally committed or logged, it exposes the private Sheet URL
- Lesson: Verify `data/source_url.txt` is in `.gitignore`; in CI always use the `SOURCE_URL` env var secret instead
- Severity: 🔴 Critical

## 2026-05-04 — Cloudflare Worker requires GITHUB_TOKEN set as a dashboard secret
- Context: `wrangler.toml` does not (and should not) contain the token
- Problem: Deploying the Worker without setting `GITHUB_TOKEN` in the CF dashboard causes all Refresh requests to return 500
- Lesson: After any Worker redeployment, verify the secret is still set in the Cloudflare dashboard under the Worker's Settings → Variables
- Severity: 🟡 Important

## 2026-05-04 — deadline countdown uses local date parsing to avoid UTC off-by-one
- Context: `dashboard.js` splits "YYYY-MM-DD" manually instead of using `new Date(isoString)`
- Problem: `new Date("2026-05-01")` parses as UTC midnight, which displays as Apr 30 in negative-UTC timezones
- Lesson: Keep the manual split in `dashboard.js`; don't "simplify" it to `new Date(raw)`
- Severity: 🟢 Minor
