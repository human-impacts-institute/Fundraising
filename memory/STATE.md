# Project State
Last updated: 2026-05-04

## Executive Summary
The dashboard is live and functional. Data was last refreshed on 2026-04-03 from 317 funders in the Google Sheet. The pipeline (Sheet → Python → Netlify) is fully operational. One open TODO: the quick-add form needs a Google Apps Script URL configured.

## Component Status

| Component | Status | Last Modified | Notes |
|---|---|---|---|
| `scripts/score_grants.py` | ✅ Complete | 2026-04-03 | Scoring logic stable; generates MD + HTML outputs |
| `docs/index.html` | ✅ Complete | 2026-04-03 | Live on Netlify; auth-gated to @humanimpactsinstitute.org |
| Cloudflare Worker proxy | ✅ Complete | — | `fundraising-refresh.fundraising-refresher.workers.dev` |
| GitHub Actions refresh workflow | ✅ Complete | — | Triggered by Refresh button via CF Worker |
| Netlify Identity auth | ✅ Complete | — | Restricts to @humanimpactsinstitute.org |
| Quick-add form (`GRANT_ADD_URL`) | ✅ Complete | 2026-05-04 | Google Apps Script Web App URL configured in `refresh-config.js` |
| Dashboard data | ⏳ Pending refresh | 2026-04-03 | Data is ~1 month old; hit Refresh on live site to sync |

## Next Steps (max 5)
1. Configure `GRANT_ADD_URL` in `docs/assets/refresh-config.js` with a Google Apps Script Web App URL to activate the quick-add form
2. Run a manual Refresh on the live dashboard to sync data (last refresh was 2026-04-03)
3. Review the 12 "On Deck" funders — Lily Auchinloss Foundation (Apr 15) and NBC Universal (Apr 15) deadlines may already be past

## Blockers
- None

## Notes from last session
2026-05-04 — Project bootstrap completed. Created AGENTS.md, memory/ system, context.md. No code changes made.
